import asyncio                                    # Импортируем модуль asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):              # Цикл, где участник поднимает пять шаров
        await asyncio.sleep(1/power)   # Задержка обратнопропорциональна силе (power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    #  Функции отработают и не будет ждать задержку функции start_strongman для каждого участника
    numb_1 = asyncio.create_task(start_strongman("Pasha", 3))
    numb_2 = asyncio.create_task(start_strongman("Denis", 4))
    numb_3 = asyncio.create_task(start_strongman("Apollon", 5))
    # Ожидаем завершения задачи для каждого участника
    await numb_1
    await numb_2
    await numb_3

asyncio.run(start_tournament())   # Запускаем асинхронную функцию

