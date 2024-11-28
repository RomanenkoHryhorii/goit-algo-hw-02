#Перевірка паліндрому з використанням deque
from collections import deque

def is_palindrome(input_string):
    # Підготовка рядка: видалення пробілів, приведення до нижнього регістру
    cleaned_string = ''.join(input_string.lower().split())
    
    # Створення двосторонньої черги
    char_deque = deque(cleaned_string)
    
    # Перевірка паліндрому
    while len(char_deque) > 1:
        # Порівняння символів з обох кінців
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

def main():
    # Тестові приклади
    test_strings = [
        "A man a plan a canal Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "Madam Im Adam"
    ]
    
    for string in test_strings:
        result = is_palindrome(string)
        print(f"'{string}': {result}")

if __name__ == "__main__":
    main()