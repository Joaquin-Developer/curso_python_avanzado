"""Palindrome"""

def is_palindrome(text: str) -> bool:
    """determinar si una cadena es palindrome"""
    text = text.replace(" ", "").lower()
    return text == text[::-1]


def main():
    """main"""
    strings = ["Ana", "pedro", 1000]

    for text in strings:
        print(is_palindrome(text))


if __name__ == "__main__":
    main()
    