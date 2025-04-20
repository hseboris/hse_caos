# Matrix Transpose

## 📝 Условие

Write a program in C, which does the following:
- inputs two integer values `N` and `M`;
- allocates a matrix of size `N * M` and fills it with values from standard input;
- transposes the matrix;
- prints the resulting matrix;
- deallocate the matrices.


## ℹ️ Примечание
- Используйте `malloc` и `free`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 03_matrix_transpose
make                                  # собрать программу
./matrix_transpose                    # запустить
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