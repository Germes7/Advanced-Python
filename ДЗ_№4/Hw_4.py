import asyncio
# Задание 1.
async def prepare_drink(name, delay):

    await asyncio.sleep(delay)
    print(f"Напиток {name} готов")

async def main():

    await prepare_drink("чай", 1)
    await prepare_drink("какао", 2)

asyncio.run(main())