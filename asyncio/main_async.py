import asyncio
import datetime

import aiohttp
from more_itertools import chunked

from models import Base, Session, SwapiPeople, engine

CHUNK_SIZE = 5

async def get_people(client, people_id):
    response = await client.get(f"https://swapi.dev/api/people/{people_id}")
    if response.status == 404:
        return None
    json_data = await response.json()
    return json_data

async def get_data_async(urls, client):
    results = []
    for el in urls:
        if el:
            response = await client.get(el)
            json_data = await response.json()
            results.append(json_data)
    return results


async def insert_to_db(results, id, client):
    async with Session() as session:
        swapi_people_list = [
            SwapiPeople(
                id_personage=id,
                birth_year=results["birth_year"],
                eye_color=results["eye_color"],
                films=", ".join([i["title"] for i in (await asyncio.gather(get_data_async(results["films"], client)))[0]]),
                gender=results["gender"],
                hair_color=results["hair_color"],
                height=results["height"],
                homeworld=", ".join(
                    [i["name"] for i in (await asyncio.gather(get_data_async([results["homeworld"]], client)))[0]]
                ),
                mass=results["mass"],
                name=results["name"],
                skin_color=results["skin_color"],
                species=", ".join(
                    [i["name"] for i in (await asyncio.gather(get_data_async(results["species"], client)))[0]]
                ),
                starships=", ".join(
                    [i["name"] for i in (await asyncio.gather(get_data_async(results["starships"], client)))[0]]
                ),
                vehicles=", ".join(
                    [i["name"] for i in (await asyncio.gather(get_data_async(results["vehicles"], client)))[0]]
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
        for ids_chunk in chunked(range(1, 100), CHUNK_SIZE):
            for i in ids_chunk:
                print(i)
                coros = [get_people(client, i)]
                results = await asyncio.gather(*coros)
                if results[0]:
                    insert_to_db_coro = insert_to_db(results[0], i, client)
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