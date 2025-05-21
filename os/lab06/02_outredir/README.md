# OutRedir

## 📝 Условие

Write a program `outredir.c` that takes a command and an output file, and runs the command with its `stdout` redirected to the specified output file.

For example:

```bash
./outredir ls out_of_ls
```

Should write the output of `ls` into the file `out_of_ls`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 02_outredir
make                                  # собрать программу
./outredir ls out.txt                 # пример запуска
python3 -m unittest discover -v tests # запустить автотесты
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add outredir.c
git commit -m "Ваше сообщение"
git push                              # результат проверки появится в Actions ✅
```