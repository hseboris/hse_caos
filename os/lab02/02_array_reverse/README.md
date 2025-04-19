# Array Reverse

## 📝 Условие
Write a program in C, which does the following:
- inputs an integer value `n`;
- allocates an array of `n` integer elements;
- fills the array with integer values from the standard input;
- reverses the array;
- prints the resulting array;
- deallocates the array.

## ℹ️ Примечание
- Используйте `malloc` и `free`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 02_array_reverse
make                                   # собрать программу
./array_rev                            # запустить
python3 -m unittest discover -v tests  # запустить тесты
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

