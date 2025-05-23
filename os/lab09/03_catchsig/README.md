# CatchSig

## 📝 Условие

Write a program `catchsig.c` based on `killn.c` and `catch.c` ([link](https://andrewt0301.github.io/hse-acos-course/part2os/09_IPC/lecture.html)) that:
- takes an interval (in seconds) and a list of signal names;
- prints its PID and an incrementing counter every `<interval>` seconds;
- sets up handlers for the specified signals;
- when a handled signal is caught, prints its description via `strsignal()` (in brackets, without newline);
- continues running if signal is not fatal.

Example:
```bash
$ ./catchsig 5 INT ABRT SEGV
26775: 0
^C[Caught: Interrupt]26775: 1
[Caught: Segmentation fault]26775: 2
[Caught: Aborted]26775: 3
```

## ℹ️ Примечание

- Используйте `signal()`, `strsignal()`, `getpid()`, `sleep()`.
- Не все сигналы обрабатываются (`SIGKILL`, `SIGSTOP` нельзя перехватить).

## ⚙️ Быстрая сборка и тесты
```bash
cd 03_catchsig
make
./catchsig 2 INT ABRT
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add catchsig.c
git commit -m "Добавить catchsig"
git push
```