# Proc

## 📝 Условие

Write a program `proc.c` (based on `endless.c` [link](https://andrewt0301.github.io/hse-acos-course/part2os/09_IPC/lecture.html)) that:
- accepts one command-line argument `<timeout>` — the number of seconds;
- loops endlessly;
- each `<timeout>` seconds:
    - prints its PID using `getpid()`;
    - prints and increments a counter.

Example:
```bash
$ ./proc 5
26475: 0
26475: 1
26475: 2
...
```

## ℹ️ Примечание

Используйте `sleep`, `getpid`, `fflush(stdout)` и проверьте корректность аргумента.

## ⚙️ Быстрая сборка и тесты
```bash
cd 01_proc
make
timeout 6 ./proc 2               # пример запуска на 6 секунд с паузой 2 сек
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add proc.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```