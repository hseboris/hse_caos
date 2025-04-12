# Задача 01-01. Функция swap

## Условие

Write a program in C that inputs two integer values `x` and `y`, call function `swap` that takes the values as arguments and swaps them, prints the values after the swap.

## Структура проекта

- `src/swap.c` — исходный код программы
- `tests/test_swap.py` — юнит-тесты на Python
- `Makefile` — сборка программы
- `.github/workflows/test.yml` — CI (GitHub Actions)

## Как использовать

1. Склонируйте репозиторий:
    ```bash
    git clone ...
    cd swap-project
    ```

2. Соберите программу:
    ```bash
    make
    ```

3. Запустите тесты:
    ```bash
    python3 -m unittest discover tests
    ```

## GitHub Actions

При каждом коммите или pull request, GitHub автоматически собирает программу и запускает тесты.