# import asyncio

# import aiohttp


# async def main():
#     async with aiohttp.ClientSession() as session:
# response = await session.post(
#     "http://127.0.0.1:8080/user/",
#     json={"name": "user_3", "password": '1234', "email": 'fvvfmrllllllfvjvjjnjggtnevjnr'}
# )
# data = await response.json()
# print(data)

# response = await session.get(
#     "http://127.0.0.1:8080/user/3/",

# )
# data = await response.json()
# print(data)

# response = await session.patch(
#     "http://127.0.0.1:8080/user/1/",
#     json={"name": "user_1/2.0", "token": "a5c2e029-98da-4acc-bf16-a1c6c1439eb7"}
# )
# data = await response.json()
# print(data)
#
# response = await session.get(
#     "http://127.0.0.1:8080/user/1/",
#
# )
# data = await response.json()
# print(data)

# response = await session.delete(
#     "http://127.0.0.1:8080/user/4/",
#     json={"token": "ef5ceb0c-d91b-4ce7-a0b4-e2b9400d738b"}
# # )
# )
# data = await response.json()
# print(data)

# response = await session.get(
#     "http://127.0.0.1:8080/user/4/",

# )
# data = await response.json()
# print(data)

# response = await session.post(
#     "http://127.0.0.1:8080/anno/user_id:5/",
#     json={"header": "gdbfgbgfbgt", "description": 'descriptionrvgfgrbrt', "token": "b9e0bc6f-6699-4257-8641-9f475411e2f9"}
# )
# data = await response.json()
# print(data)

# response = await session.get(
#     "http://127.0.0.1:8080/anno/4/",

# )
# data = await response.json()
# print(data)

# response = await session.patch(
#     "http://127.0.0.1:8080/anno/4/",
#     json={"header": "gdbfgbgfbgtLLLLL", "description": 'descriptionrvgfgrbrt"""', "token": "b9e0bc6f-6699-4257-8641-9f475411e2f9"}
# )
# data = await response.json()
# print(data)

# response = await session.get(
#     "http://127.0.0.1:8080/anno/4/",

# )
# data = await response.json()
# print(data)

#         response = await session.delete(
#             "http://127.0.0.1:8080/anno/4/",
#             json={"token": "b9e0bc6f-6699-4257-8641-9f475411e2f9"}
#         # )
#         )
#         data = await response.json()
#         print(data)

#         response = await session.get(
#             "http://127.0.0.1:8080/anno/4/",

#         )
#         data = await response.json()
#         print(data)

# asyncio.run(main())
