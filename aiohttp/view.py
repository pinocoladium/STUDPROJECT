import json

from aiohttp import web
from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy.exc import IntegrityError

from models import Anno, Base, Session, Token, User, engine


def hash_password(password: str):
    password = password.encode()
    password = hashpw(password, gensalt())
    password = password.decode()
    return password


def check_password(password: str, hashed_password: str):
    password = password.encode()
    hashed_password = hashed_password.encode()
    return checkpw(password, hashed_password)


def get_http_error(http_error_class, message):
    return http_error_class(
        text=json.dumps({"error": message}), content_type="application/json"
    )


async def get_user(user_id: int, session: Session) -> User:
    user = await session.get(User, user_id)
    if user is None:
        raise get_http_error(web.HTTPNotFound, "user not found")
    return user


async def get_token(token_id: int, session: Session) -> Token:
    token = await session.get(Token, token_id)
    if token is None:
        raise get_http_error(web.HTTPNotFound, "token not found")
    return token


async def get_anno(anno_id: int, session: Session) -> Anno:
    anno = await session.get(Anno, anno_id)
    if anno is None:
        raise get_http_error(web.HTTPNotFound, "anno not found")
    return anno


class UserView(web.View):
    @property
    def session(self) -> Session:
        return self.request["session"]

    @property
    def user_id(self) -> int:
        return int(self.request.match_info["user_id"])

    async def get(self):
        user = await get_user(self.user_id, self.session)
        return web.json_response(
            {
                "id": user.id,
                "name": user.name,
                "creation_time": user.creation_time.isoformat(),
            }
        )

    async def post(self):
        json_data = await self.request.json()
        json_data["password"] = hash_password(json_data["password"])
        new_user = User(**json_data)
        token = Token(user=new_user)
        try:
            self.session.add(new_user)
            self.session.add(token)
            await self.session.commit()
        except IntegrityError as err:
            raise get_http_error(web.HTTPConflict, "user already exists")
        return web.json_response({"id": new_user.id, "token": token.id})

    async def patch(self):
        json_data = await self.request.json()
        if "password" in json_data:
            json_data["password"] = hash_password(json_data["password"])
        user = await get_user(self.user_id, self.session)
        token = await get_token(json_data.pop("token"), self.session)
        if token.user_id != user.id:
            raise get_http_error(web.HTTPConflict, "user has no access")
        for key, value in json_data.items():
            setattr(user, key, value)
        try:
            self.session.add(user)
            await self.session.commit()
        except IntegrityError as err:
            raise get_http_error(web.HTTPConflict, "user already exists")
        return web.json_response({"id": user.id})

    async def delete(self):
        json_data = await self.request.json()
        user = await get_user(self.user_id, self.session)
        token = await get_token(json_data.pop("token"), self.session)
        if token.user_id != user.id:
            raise get_http_error(web.HTTPConflict, "user has no access")
        await self.session.delete(user)
        await self.session.commit()
        return web.json_response(
            {"id": user.id, "name": user.name, "status": "deleted"}
        )


class AnnoView(web.View):
    @property
    def session(self) -> Session:
        return self.request["session"]

    @property
    def anno_id(self) -> int:
        return int(self.request.match_info["anno_id"])

    @property
    def user_id(self) -> int:
        return int(self.request.match_info["user_id"])

    async def get(self):
        anno = await get_anno(self.anno_id, self.session)
        return web.json_response(
            {
                "id": anno.id,
                "header": anno.header,
                "creation_time": anno.creation_time.isoformat(),
            }
        )

    async def post(self):
        json_data = await self.request.json()
        json_data["user_id"] = self.user_id
        user = await get_user(self.user_id, self.session)
        token = await get_token(json_data.pop("token"), self.session)
        if token.user_id != user.id:
            raise get_http_error(web.HTTPConflict, "user has no access")
        new_anno = Anno(**json_data)
        self.session.add(new_anno)
        await self.session.commit()
        return web.json_response({"id": new_anno.id, "header": new_anno.header})

    async def patch(self):
        json_data = await self.request.json()
        token = await get_token(json_data.pop("token"), self.session)
        anno = await get_anno(self.anno_id, self.session)
        if token.user_id != anno.user_id:
            raise get_http_error(web.HTTPConflict, "user has no access")
        for key, value in json_data.items():
            setattr(anno, key, value)
        self.session.add(anno)
        await self.session.commit()
        return web.json_response(
            {
                "status": "success",
                "id": anno.id,
                "header": anno.header,
                "description": anno.description,
            }
        )

    async def delete(self):
        json_data = await self.request.json()
        anno = await get_anno(self.anno_id, self.session)
        token = await get_token(json_data["token"], self.session)
        if token.user_id != anno.user_id:
            raise get_http_error(web.HTTPConflict, "user has no access")
        await self.session.delete(anno)
        await self.session.commit()
        return web.json_response(
            {"id": anno.id, "header": anno.header, "status": "deleted"}
        )
