import asyncio
#
# # Задание 1.
# async def prepare_drink(name, delay):
#
#     await asyncio.sleep(delay)
#     print(f"Напиток {name} готов")
#
# async def main():
#
#     await prepare_drink("чай", 1)
#     await prepare_drink("какао", 2)
#
# async def main():
#
#     await prepare_drink("чай", 1)
#     await prepare_drink("какао", 2)
#
# asyncio.run(main())
#
# # Задание 2.
# async def serve_orders(orders):
#
#     tasks = []
#     for name, delay in orders:
#         tasks.append(asyncio.create_task(prepare_drink(name, delay)))
#     await asyncio.gather(*tasks)
#
# async def main():
#
#     await serve_orders([("какао", 2), ("чай", 1)])
#     await serve_orders([("кофе", 2), ("какао", 3), ("чай", 1)])
#
# asyncio.run(main())

# Задание 3.
async def show_steps(name, count):

    if count == 0:
        return

    print(f"{name}: этап 1")

    for _ in range(2, count + 1):
        await asyncio.sleep(1)
        print(f"{name}: этап {_}")

async def main():
    await asyncio.gather(
        show_steps("Фото", 3),
        show_steps("Видео", 2),
    )
async def main():
    await show_steps("Текст", 1)
    await show_steps("Архив", 0)

asyncio.run(main())