# SumSum

## 📝 Условие

Write a shell script `sumsum.sh` that:

- defines a function `sum()` that:
    - sums all of its arguments (any number allowed);
    - returns the sum if all arguments are valid numbers;
    - returns 0 if any argument is invalid (e.g., contains letters);
    - suppresses all error messages (`2>/dev/null`);
- reads two lines of input (arrays of numbers or mixed content);
- compares the sums from each line;
- prints `Equal` if they are equal (including both being 0), otherwise `Not equal`.

Example:
```bash
$ ./sumsum.sh
1 3 5
2 4 6
Not equal

$ ./sumsum.sh
1 5 6
4 4 4
Equal

$ ./sumsum.sh
1 2 w
3 4 e
Equal
```

## ℹ️ Примечание

Используйте `expr` для арифметики и проверяйте `$?` после каждой операции.  
Ошибки должны быть скрыты: `2>/dev/null`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 02_sumsum
chmod +x sumsum.sh
./sumsum.sh                         # вводить строки вручную
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
rm -f output.txt
```

## 🚀 Автотесты в GitHub Actions
```bash
git add sumsum.sh
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```