# PipeRedir

## 📝 Условие

Write a program `piperedir.c` that:
- takes two commands: `command1`, `command2`, and optional arguments for the second;
- forks and execs `command1`, and separately forks and execs `command2`;
- connects the stdout of `command1` to the stdin of `command2` through an unnamed pipe.

Example:
```bash
./piperedir date hexdump -C
```

## ℹ️ Примечание

Решение нужно реализовать в файле `piperedir.c`. Используйте `pipe`, `dup2`, `execvp`, `fork`, `waitpid`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 05_piperedir
make
./piperedir echo wc
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add piperedir.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```