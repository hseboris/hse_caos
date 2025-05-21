# Read Builtin

## 📝 Условие

Write a shell script that:
- prompts the user with `Enter your name: ` (no trailing newline);
- reads a line from stdin using the `read` builtin;
- if the user enters a name, print `Hello, <name>!`;
- if the user enters nothing (just presses Enter), print `Hello, tmpuser?`.

Example:
```bash
$ ./c8.sh
Enter your name: Spot
Hello, Spot!

$ ./c8.sh
Enter your name:
Hello, tmpuser?
```

## ℹ️ Примечание

Команда `read` является встроенной (builtin) в оболочку, поэтому используйте `help read` вместо `man read`.  
Чтобы вывести приглашение без перевода строки, используйте `echo -n`.

## ⚙️ Быстрая сборка и тесты
```bash
cd 01_read_builtin
chmod +x c8.sh                          # сделать скрипт исполняемым
./c8.sh                                 # запуск вручную
python3 -m unittest discover -v tests   # автотесты
```

## 🧹 Очистка
```bash
rm -f input.txt output.txt
```

## 🚀 Автотесты в GitHub Actions
```bash
git add c8.sh
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```