# Regex Replace

## 📝 Условие

Write a program that inputs three command-line arguments:

- `argv[1]` &ndash; regular expression;
- `argv[2]` &ndash; text;
- `argv[3]` &ndash; replacement.

The program finds all occurrences of the regular expression in the text and replaces all of them with the specified replacement string. The updated text is stored in a separate buffer and printed to the console in the end.

> 💡 Algorithm is as follows. Allocate a buffer for the new text. Find a regular expression match. Copy to the buffer text before match. Copy to the buffer replacement. Find the next regular expression match and so on.

## ℹ️ Примечание

- The problem when the size of the allocated buffer is not enough to store the text can be solved by using the `realloc` function to allocated additional space.

## ⚙️ Быстрая сборка и тесты

```bash
cd 01_regex_replace
make                                      # сборка программы
python3 -m unittest discover -v tests     # запуск автотестов
```

## 🧹 Очистка

```bash
make clean
```

## 🚀 Автотесты в GitHub Actions

```bash
git add .
git commit -m "Ваше сообщение"
git push                              # результат появится во вкладке Actions ✅
```