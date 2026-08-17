"""
Задача: Merge Intervals

Короткая формула для памяти: sort → compare with last → merge or append
Сложность: O(n log n) время, O(n) память
Инвариант: все уже обработанные интервалы объединены правильно, а новый интервал достаточно сравнить только с последним в result
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # сортируем на месте по началам отрезков O(n log n)
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0].copy()]
    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result


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