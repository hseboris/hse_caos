# Swap

## Условие

Write a program in C that inputs two integer values `x` and `y`, call function `swap` that takes the values as arguments and swaps them, prints the values after the `swap`.

## Примечания

- `swap` должна быть функцией и принимать на вход указатели;
- за просто вывод в обратном порядке всё домашнее задание будет оценено $0$&nbsp;баллов.

## Локальное тестирование

1. Перейдите в папку `task1_swap`.
2. Сборка
```bash
make
```
3. Запуск
```bash
./swap
```

4. Тестирование
```bash
python3 -m unittest discover -v tests
```

## Очистка сборки

Чтобы удалить все скомпилированные файлы и артефакты, в той же папке выполните:

```bash
make clean
```

## Проверка на GitHub Actions

После того, как вы закоммитите и запушите изменения:

```bash
git add solution.c
git commit -m "Ваше сообщение"
git push
```