# AllRedir

## 📝 Условие

Write a program `allredir.c` that:
- takes a command, an input file, and an output file;
- forks and execs the command with `stdin` redirected from the input file and `stdout` redirected to the output file;
- waits for the child to terminate and prints `received <exit_code>`.

Example:
```bash
./allredir hexdump input.txt dump.txt
```

## ℹ️ Примечание

Решение должно быть реализовано в файле `allredir.c`. Используйте `fork`, `execvp`, `dup2`, `open`, `waitpid`, `WEXITSTATUS`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 03_allredir
make                                  # собрать программу
./allredir cat input.txt output.txt   # пример использования
python3 -m unittest discover -v tests # запуск автотестов
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add allredir.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```