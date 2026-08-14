"""
Задача: Binary Search

Дан отсортированный по возрастанию массив целых чисел nums
и целое число target.

Нужно найти индекс target в nums.

Если target присутствует в массиве — вернуть его индекс.
Если target отсутствует — вернуть -1.

Алгоритм должен работать за O(log n).

Пример:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Ответ:
4
"""


def binary_search(nums: list[int], target: int) -> int:
    pass


def test():
    test_cases = [
        # обычный поиск
        ([-1, 0, 3, 5, 9, 12], 9, 4),

        # элемента нет
        ([-1, 0, 3, 5, 9, 12], 2, -1),

        # один элемент
        ([5], 5, 0),
        ([5], 3, -1),

        # два элемента
        ([1, 2], 1, 0),
        ([1, 2], 2, 1),

        # середина
        ([1, 2, 3, 4, 5], 3, 2),

        # крайние элементы
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),

        # пустой массив
        ([], 1, -1),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, start=1):
        result = binary_search(nums, target)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"nums: {nums}\n"
            f"target: {target}\n"
            f"expected: {expected}\n"
            f"got: {result}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test()