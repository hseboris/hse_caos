# ArgRedir

## 📝 Условие

Write a program `argredir.c` that:
- takes an input file, an output file, a command, and any number of arguments;
- forks and execs the command with `stdin` redirected from the input file and `stdout` redirected to the output file;
- waits for the child to terminate and prints `received <exit_code>`.

Example:
```bash
./argredir input.txt output.txt hexdump -C
```

## ℹ️ Примечание

Решение должно быть реализовано в файле `argredir.c`. Используйте `execvp` и `argv` с аргументами команды начиная с позиции 3.

## ⚙️ Быстрая сборка и тесты
```bash
cd 04_argredir
make
./argredir input.txt output.txt cat
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add argredir.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```