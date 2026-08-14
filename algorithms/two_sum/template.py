"""
Задача: Two Sum

Дан массив целых чисел nums и целое число target.

Нужно найти два различных индекса i и j таких, что:

nums[i] + nums[j] == target

Гарантируется, что существует ровно одна пара.

Вернуть индексы найденных элементов.

Требуется решение за O(n).

Пример:

nums = [2, 7, 11, 15]
target = 9

Ответ:

[0, 1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    pass


def test():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, start=1):
        result = two_sum(nums, target)

        assert sorted(result) == sorted(expected), (
            f"Test {i} failed:\n"
            f"nums={nums}\n"
            f"target={target}\n"
            f"expected={expected}\n"
            f"got={result}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test()