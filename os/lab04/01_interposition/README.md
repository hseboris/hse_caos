# Interposition

## 📝 Условие

Improve [Task 1 from Part 1](https://andrewt0301.github.io/hse-acos-course/part2os/04_Linking/libs.html):
- Provide _link-time_ interpositioning for the fred and john functions
- Provide _load-time_ interpositioning for the bill and sam functions
- Create a Make script to build the program.

## ℹ️ Примечание

- interposed functions can just print a message like &laquo;fred is called&raquo;.

## ⚙️ Быстрая сборка и тесты

```bash
cd 02_interposition
make                                  # собрать программу
make run                              # пропишите в cmake запуск
                                      # (в том числе вывод используемых динамических библиотек)
```

## 🧹 Очистка

```bash
make clean
```

## 🚀 Автотесты в GitHub Actions

```bash
git add .
git commit -m "Ваше сообщение"
git push                              # результат проверки появится в Actions ✅
```