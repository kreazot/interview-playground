"""
Задача: Valid Parentheses:
сложность решения O(n), пространственная O(n) в худшем случае

Короткая формула для памяти:
открывающая → push, закрывающая → проверяем top и pop, в конце stack должен быть пуст.
"""


def is_valid(s: str) -> bool:
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
            continue
        if not stack:
            return False
        if stack.pop() != pairs[char]:
            return False
    return not stack



def test():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
        ("((())", False),
        ("{[()]}", True),
    ]

    for i, (s, expected) in enumerate(test_cases, start=1):
        result = is_valid(s)

        assert result == expected, (
            f"Test {i} failed:\n"
            f"s: {s}\n"
            f"expected: {expected}\n"
            f"got: {result}"
        )

    print("✅ All tests passed!")


if __name__ == "__main__":
    test()