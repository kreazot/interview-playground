"""
Задача: Move Zeroes

Короткая формула для памяти: read ищет ненулевые → write уплотняет их слева → остаток заполняем нулями
Сложность: O(n) время, O(1) память
Инвариант: всё левее write — уже правильно записанные ненулевые элементы в исходном порядке.
"""


def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1

def test_move_zeroes() -> None:
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 2, 0, 0, 3], [1, 2, 3, 0, 0, 0]),
        ([-1, 0, -2, 0, 3], [-1, -2, 3, 0, 0]),
    ]

    for i, (nums, expected) in enumerate(test_cases, start=1):
        result = move_zeroes(nums)
        assert result is None, (
            f"Test {i} failed:\n"
            f"expected return: None\n"
            f"got: {result}"
        )

        assert nums == expected, (
            f"Test {i} failed:\n"
            f"expected: {expected}\n"
            f"got: {nums}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test_move_zeroes()
