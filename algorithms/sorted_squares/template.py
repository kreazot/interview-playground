"""
Задача: Squares of a Sorted Array

Дан массив nums, отсортированный по неубыванию.

Нужно вернуть новый массив, содержащий квадраты всех элементов nums,
также отсортированный по неубыванию.

Требуемая сложность: O(n).

Пример:

nums = [-4, -1, 0, 3, 10]

Ответ:
[0, 1, 9, 16, 100]
"""


def sorted_squares(nums: list[int]) -> list[int]:
    pass


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