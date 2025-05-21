# ArgRedir (Strict)

## 📝 Условие

Improve your previous `argredir.c` to:
- check the return values of **all system calls** and
- print errors using `perror()` when failures occur.

## ℹ️ Примечание

Файл с решением: `argredir_strict.c`.  
Проверяйте возврат всех вызовов: `open`, `dup2`, `fork`, `execvp`, `waitpid`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 06_argredir_strict
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
git add argredir_strict.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```