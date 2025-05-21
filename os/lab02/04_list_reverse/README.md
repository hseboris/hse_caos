# List Reverse

## 📝 Условие

Write a program in C, which does the following:
- creates a singly-linked list;
- add to the list numbers from the standard input until user inputs `0`;
- reverses the list;
- prints the resulting list;
- deallocates the list.


## ℹ️ Примечание
- Используйте `malloc` и `free`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 04_list_reverse
make                                  # собрать программу
./list_reverse                        # запустить
python3 -m unittest discover -v tests # запустить тесты
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add solution.c
git commit -m "Ваше сообщение"
git push                               # результат проверки появится в Actions ✅
```