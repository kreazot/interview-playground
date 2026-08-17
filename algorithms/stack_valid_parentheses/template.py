"""
Задача: Valid Parentheses

Дана строка s, состоящая только из символов:

'(', ')', '{', '}', '[', ']'

Нужно определить, является ли последовательность скобок корректной.

Последовательность корректна, если:

1. Каждая открывающая скобка закрывается скобкой того же типа.
2. Скобки закрываются в правильном порядке.
3. У каждой закрывающей скобки есть соответствующая открывающая.

Примеры:

"()"      -> True
"()[]{}"  -> True
"(]"      -> False
"([)]"    -> False
"{[]}"    -> True
"""


def is_valid(s: str) -> bool:
    pass


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