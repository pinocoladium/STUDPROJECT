import json
from hashlib import md5

from flask.views import MethodView
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from flask import Flask, jsonify, request
from models import Anno, Session, Token, User
from scheme import (CreateAnno, CreateUser, DeleteAnnoUser, UpdateAnno,
                    UpdateUser)

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: dict | str | list):
        self.status_code = status_code
        self.message = message


def validate(json_data, schema):
    try:
        model = schema(**json_data)
        return model.dict(exclude_none=True)
    except ValidationError as err:
        error_message = json.loads(err.json())
        raise HttpError(400, error_message)


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    http_response = jsonify({"status": "error", "message": er.message})
    http_response.status_code = er.status_code
    return http_response


SALT = "3twerf3we4twgrehbtybtyby44t"


def hash_password(password: str):
    password = f"{SALT}{password}"
    password = password.encode()
    password = md5(password).hexdigest()
    return password


def get_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
    return user


def get_anno(anno_id: int, session: Session):
    anno = session.get(Anno, anno_id)
    if anno is None:
        raise HttpError(404, "anno not found")
    return anno


def get_token(token_id, session: Session):
    token = session.get(Token, token_id)
    if token is None:
        raise HttpError(404, "token not found")
    return token


class UsersView(MethodView):
    def get(self, users_id):
        with Session() as session:
            user = get_user(users_id, session)
            return jsonify({"id": user.id, "name": user.name})

    def post(self):
        json_data = validate(request.json, CreateUser)
        json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            new_user = User(**json_data)
            token = Token(user=new_user)
            session.add(token, new_user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "user already exists")
            return jsonify({"id": new_user.id, "token": token.id})

    def patch(self, users_id):
        json_data = validate(request.json, UpdateUser)
        if "password" in json_data:
            json_data["password"] = hash_password(json_data["password"])
        with Session() as session:
            user = get_user(users_id, session)
            token = get_token(json_data.pop("token"), session)
            if token.user_id != user.id:
                raise HttpError(403, "user has no access")
            for key, value in json_data.items():
                setattr(user, key, value)
            session.add(user)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(408, "user already exists")
            return jsonify({"status": "success"})

    def delete(self, users_id):
        json_data = validate(request.json, DeleteAnnoUser)
        with Session() as session:
            user = get_user(users_id, session)
            token = get_token(json_data["token"], session)
            if token.user_id != user.id:
                raise HttpError(403, "user has no access")
            session.delete(user)
            session.commit()
            return jsonify({"status": "success"})


class AnnoView(MethodView):
    def get(self, anno_id):
        with Session() as session:
            anno = get_anno(anno_id, session)
            return jsonify(
                {"id": anno.id, "header": anno.header, "description": anno.description}
            )

    def post(self):
        json_data = validate(request.json, CreateAnno)
        with Session() as session:
            user = get_user(json_data["user_id"], session)
            token = get_token(json_data.pop("token"), session)
            if token.user_id != user.id:
                raise HttpError(403, "user has no access")
            new_anno = Anno(**json_data)
            session.add(new_anno)
            session.commit()
            return jsonify({"id": new_anno.id, "header": new_anno.header})

    def patch(self, anno_id):
        json_data = validate(request.json, UpdateAnno)
        with Session() as session:
            anno = get_anno(anno_id, session)
            token = get_token(json_data.pop("token"), session)
            if token.user_id != anno.user_id:
                raise HttpError(403, "user has no access")
            for key, value in json_data.items():
                setattr(anno, key, value)
            session.add(anno)
            session.commit()
            return jsonify(
                {
                    "status": "success",
                    "id": anno.id,
                    "header": anno.header,
                    "description": anno.description,
                }
            )

    def delete(self, anno_id):
        json_data = validate(request.json, DeleteAnnoUser)
        with Session() as session:
            anno = get_anno(anno_id, session)
            token = get_token(json_data["token"], session)
            if token.user_id != anno.user_id:
                raise HttpError(403, "user has no access")
            session.delete(anno)
            session.commit()
            return jsonify({"status": "success"})


user_view = UsersView.as_view("users")
app.add_url_rule("/users/", view_func=user_view, methods=["POST"])
app.add_url_rule(
    "/users/<int:users_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"]
)
anno_view = AnnoView.as_view("anno")
app.add_url_rule("/anno/", view_func=anno_view, methods=["POST"])
app.add_url_rule(
    "/anno/<int:anno_id>", view_func=anno_view, methods=["GET", "PATCH", "DELETE"]
)

if __name__ == "__main__":
    app.run()
