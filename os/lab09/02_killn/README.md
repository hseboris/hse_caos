# Killn

## 📝 Условие

Write a program `killn.c` that:
- takes two arguments: `PID` and `SIGNAL_NAME`;
- sends the signal to the process using `kill()`;
- uses a hardcoded array of signal names;
- if signal name is invalid, prints `No such signal` and returns 1;
- if `kill()` fails, prints error with `perror()`.

Example:
```bash
$ ./killn 12345 TERM
$ ./killn 0 XYZ
No such signal
```

## ℹ️ Примечания

- Используйте `kill`, `perror`, `strcmp`, `atoi`;
- Список сигналов можно получить через `kill -l`;
- Все сообщения об ошибках должны выводиться в **stderr**.

💡 Дополнительные баллы:
- +2 балла — если напишете `bash`-скрипт для генерации массива сигналов;
- +2 балла — если массив будет формироваться во время выполнения программы.

## ⚙️ Быстрая сборка и тесты

```bash
cd 02_killn
make
./killn 99999 TERM                        # несуществующий процесс
python3 -m unittest discover -v tests
```

## 🧹 Очистка

```bash
make clean
```

## 🚀 Автотесты в GitHub Actions

```bash
git add killn.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```