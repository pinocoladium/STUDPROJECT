from aiohttp import web

from models import Base, Session, engine
from view import AnnoView, UserView

app = web.Application()


async def orm_cntx(app: web.Application):
    print("START")
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    print("SHUT DOWN")


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request["session"] = session
        response = await handler(request)
        return response


app.cleanup_ctx.append(orm_cntx)
app.middlewares.append(session_middleware)

app.add_routes(
    [
        web.get("/user/{user_id:\d+}/", UserView),
        web.patch("/user/{user_id:\d+}/", UserView),
        web.delete("/user/{user_id:\d+}/", UserView),
        web.post("/user/", UserView),
        web.get("/anno/{anno_id:\d+}/", AnnoView),
        web.patch("/anno/{anno_id:\d+}/", AnnoView),
        web.delete("/anno/{anno_id:\d+}/", AnnoView),
        web.post("/anno/user_id:{user_id:\d+}/", AnnoView),
    ]
)

if __name__ == "__main__":
    web.run_app(app)
