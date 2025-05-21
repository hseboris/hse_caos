# Pip2Redir

## 📝 Условие

Write a new program called `pip2redir.c` that:
- forks **two child processes**: one runs `command1`, the other `command2`;
- connects them via an unnamed pipe (`command1 | command2`);
- waits for both to finish and prints the **exit status** of both.

Note: `wait()` may return early, use `ECHILD` to detect when all children are reaped.

Example:
```bash
./pip2redir date hexdump -C
```

## ℹ️ Примечание

Используйте `fork`, `pipe`, `dup2`, `execvp`, `wait`, `WIFEXITED`, `WEXITSTATUS`, `errno`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 07_pip2redir
make
./pip2redir echo wc
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add pip2redir.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```