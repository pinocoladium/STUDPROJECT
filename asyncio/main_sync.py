import asyncio
import datetime
import json

import aiohttp
import requests
from more_itertools import chunked

from models import Base, Session, SwapiPeople, engine

CHUNK_SIZE = 5

async def get_people(client, people_id):
    response = await client.get(f"https://swapi.dev/api/people/{people_id}")
    if response.status == 404:
        return None
    json_data = await response.json()
    return json_data

def get_data_sync(urls):
    results = []
    for el in urls:
        if el:
            responce = requests.get(el).json()
            results.append(responce)
    return results

async def insert_to_db(results, id):
    async with Session() as session:
        swapi_people_list = [
            SwapiPeople(
                id_personage=id,
                birth_year=results["birth_year"],
                eye_color=results["eye_color"],
                films=", ".join([i["title"] for i in get_data_sync(results["films"])]),
                gender=results["gender"],
                hair_color=results["hair_color"],
                height=results["height"],
                homeworld=", ".join(
                    [i["name"] for i in get_data_sync([results["homeworld"]])]
                ),
                mass=results["mass"],
                name=results["name"],
                skin_color=results["skin_color"],
                species=", ".join(
                    [i["name"] for i in get_data_sync(results["species"])]
                ),
                starships=", ".join(
                    [i["name"] for i in get_data_sync(results["starships"])]
                ),
                vehicles=", ".join(
                    [i["name"] for i in get_data_sync(results["vehicles"])]
                ),
            )
        ]
        session.add_all(swapi_people_list)
        await session.commit()


async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
    async with aiohttp.ClientSession() as client:
        for ids_chunk in chunked(range(1, 90), CHUNK_SIZE):
            for i in ids_chunk:
                print(i)
                coros = [get_people(client, i)]
                results = await asyncio.gather(*coros)
                if results[0]:
                    insert_to_db_coro = insert_to_db(results[0], i)
                    asyncio.create_task(insert_to_db_coro)
    current_task = asyncio.current_task()
    tasks_to_await = asyncio.all_tasks() - {
        current_task,
    }
    for task in tasks_to_await:
        await task


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)