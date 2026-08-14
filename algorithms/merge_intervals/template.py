"""
Задача: Merge Intervals

Дан массив интервалов intervals, где каждый интервал представлен
парой [start, end].

Нужно объединить все пересекающиеся интервалы и вернуть массив
непересекающихся интервалов, покрывающих те же диапазоны.

Интервалы [a, b] и [c, d] пересекаются, если c <= b
при условии, что интервалы отсортированы по start.

Пример:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

Результат:

[[1, 6], [8, 10], [15, 18]]
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    pass


def test():
    test_cases = [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
        ),
        (
            [],
            [],
        ),
        (
            [[5, 7], [1, 2], [2, 4], [10, 12]],
            [[1, 4], [5, 7], [10, 12]],
        ),
        (
            [[1, 10], [2, 3], [4, 8]],
            [[1, 10]],
        ),
        (
            [[1, 2]],
            [[1, 2]],
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 2], [3, 4]],
        ),
    ]

    for i, (intervals, expected) in enumerate(test_cases, start=1):
        result = merge_intervals(intervals)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"intervals: {intervals}\n"
            f"expected: {expected}\n"
            f"got: {result}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test()