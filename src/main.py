#!/usr/bin/env python3
"""
Учебный проект по Git
Студент: Комнацкий Роман, группа ББИ-242
"""


def greet(name: str) -> str:
    """Возвращает приветствие для указанного имени."""
    return f"Привет, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """Возвращает сумму двух чисел."""
    return a + b


def main():
    print("=== Учебный проект по Git ===")
    print(greet("Мир"))
    print("Студент: Комнацкий Роман")
    print("Группа: ББИ-242")
    # Новый вывод: демонстрация арифметической функции
    result = calculate_sum(10, 32)
    print(f"10 + 32 = {result}")


if __name__ == "__main__":
    main()
