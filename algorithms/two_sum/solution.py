"""
Задача: Two Sum

Короткая формула для памяти: для num ждём target - num → нашли в seen → вернули пару
Сложность: O(n) время, O(n) память
Инвариант: seen хранит числа, которые мы ожидаем встретить дальше, и индекс элемента, которому они нужны
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # мапа с тем что мы ожидаем увидеть дальше
    for i, num in enumerate(nums):
        if num in seen:
            return [i, seen[num]]
        seen[target - num] = i



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