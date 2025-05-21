# Fork

## 📝 Условие

Write a program called `fork.c` that:
- creates a child process and waits for it to complete;
- the child process creates another child process and waits for it to complete;
- each process prints a message identifying itself:
    - Parent prints `Hello from Parent`
    - First child prints `Hello from Child1`
    - Second child prints `Hello from Child2`

## ℹ️ Примечание

Решение нужно написать в файле `fork.c`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 01_fork
make                                  # собрать программу
./fork                                # запустить
python3 -m unittest discover -v tests # запустить тесты
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add fork.c
git commit -m "Ваше сообщение"
git push                              # результат проверки появится в Actions ✅
```