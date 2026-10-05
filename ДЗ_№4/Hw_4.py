import asyncio

# Задание 1.
async def prepare_drink(name, delay):

    await asyncio.sleep(delay)
    print(f"Напиток {name} готов")

async def main():

    await prepare_drink("чай", 1)
    await prepare_drink("какао", 2)

async def main():

    await prepare_drink("чай", 1)
    await prepare_drink("какао", 2)

asyncio.run(main())

# Задание 2.
async def serve_orders(orders):

    tasks = []
    for name, delay in orders:
        tasks.append(asyncio.create_task(prepare_drink(name, delay)))
    await asyncio.gather(*tasks)

async def main():

    await serve_orders([("какао", 2), ("чай", 1)])
    await serve_orders([("кофе", 2), ("какао", 3), ("чай", 1)])

asyncio.run(main())