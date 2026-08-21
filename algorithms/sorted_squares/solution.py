"""
Задача: Squares of a Sorted Array

Короткая формула для памяти: сравниваем края → больший квадрат пишем с конца → двигаем его указатель
Сложность: O(n) время, O(n) память
Инвариант: всё правее write уже заполнено правильными квадратами в отсортированном порядке.
"""


def sorted_squares(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    write = len(nums) - 1

    results = [0] * len(nums)

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            results[write] = left_square
            left += 1
        else:
            results[write] = right_square
            right -= 1
        write -= 1
    return results


def test() -> None:
    test_cases = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([], []),
        ([1], [1]),
        ([-2], [4]),
        ([-3, -2, -1], [1, 4, 9]),
        ([0, 1, 2], [0, 1, 4]),
        ([-2, -2, 0, 2, 2], [0, 4, 4, 4, 4]),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = sorted_squares(nums)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"nums: {nums}\n"
            f"expected: {expected}\n"
            f"got: {result}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
