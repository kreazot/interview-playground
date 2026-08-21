import asyncio
import time
from functools import wraps


def time_print(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = await func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"Время выполнения: {elapsed:.3f} сек")

        return result

    return wrapper


async def worker(name: str, delay: int) -> str:
    print(f"{name}: старт")
    await asyncio.sleep(delay)
    print(f"{name}: стоп")
    return name


# Последовательный запуск (закомментируй остальные блоки для проверки выполнения)
#
# Сначала полностью завершится worker A,
# только после этого начнёт выполняться worker B.
#
# Общее время: ~4 секунды.

@time_print
async def main():
    result_1 = await worker("A", 2)
    result_2 = await worker("B", 2)
# -------------------------------------------------------------------------------

# Конкурентный запуск через asyncio.create_task() (закомментируй остальные блоки для проверки выполнения)
#
# create_task() создаёт Task и планирует корутину
# для выполнения в event loop.
#
# Обе задачи начинают выполняться конкурентно.
#
# Общее время: ~2 секунды.

@time_print
async def main():
    task_1 = asyncio.create_task(worker("A", 2))
    task_2 = asyncio.create_task(worker("B", 2))

    result_1 = await task_1
    result_2 = await task_2
# -------------------------------------------------------------------------------

# Конкурентный запуск через asyncio.gather() (закомментируй остальные блоки для проверки выполнения)
#
# gather() принимает awaitable-объекты,
# запускает их конкурентно и возвращает результаты
# в том же порядке, в котором они были переданы.
#
# Общее время: ~2 секунды.

@time_print
async def main():
    results = await asyncio.gather(
        worker("A", 2),
        worker("B", 2),
    )
# -------------------------------------------------------------------------------

# Конкурентный запуск через asyncio.TaskGroup() (закомментируй остальные блоки для проверки выполнения)
#
# TaskGroup появился в Python 3.11.
# Это structured concurrency:
# жизненный цикл дочерних задач ограничен блоком TaskGroup.
#
# Выход из async with произойдёт только после завершения
# всех задач группы.
#
# Если одна задача завершится с обычным исключением,
# TaskGroup отменит остальные незавершённые задачи.
#
# Общее время: ~2 секунды.
#
@time_print
async def main():
    async with asyncio.TaskGroup() as tg:
        task_1 = tg.create_task(worker("A", 2))
        task_2 = tg.create_task(worker("B", 2))

    result_1 = task_1.result()
    result_2 = task_2.result()
# -------------------------------------------------------------------------------


if __name__ == "__main__":
    asyncio.run(main())
