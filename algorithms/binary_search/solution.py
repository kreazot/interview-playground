"""
Задача: Binary Search

Короткая формула для памяти: mid → compare → отбрасываем половину
Сложность: O(log n) время, O(1) память
Инвариант: если target существует, он находится внутри [left, right]
"""


def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        pivot = nums[mid]
        if target == pivot:
            return mid
        if target > pivot:
            left = mid + 1
        else:
            right = mid - 1
    return -1


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