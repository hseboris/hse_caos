# ChildCtl

## 📝 Условие

Write a program `childctl.c` that:
- takes `<timeout> <quit_signal> <signal1> [signal2 ...]` as arguments;
- forks a child that runs infinitely;
- parent process:
    - every `<timeout>` seconds prints heartbeat counter and its PID;
    - installs signal handlers for listed signals, printing signal descriptions;
    - when `quit_signal` is received, prints "Quitting...", kills the child, waits for it, and exits.

Example:
```bash
$ ./childctl 2 TERM INT USR1
Forked child: 12345
Parent heartbeat: 0
Parent heartbeat: 1
^C[Caught: Interrupt]
Parent heartbeat: 2
[Caught: User defined signal 1]
Parent heartbeat: 3
[Caught: Terminated]
Quitting...
Child terminated. Exit status: 9
```

## ℹ️ Примечание

- Используйте `fork`, `sleep`, `strsignal`, `sigaction`, `kill`, `waitpid`, `getpid`.
- Не все сигналы обрабатываются одинаково на разных платформах — рекомендуется тестировать поведение вручную с `SIGINT`, `SIGTERM`, `USR1`.
- Автотесты покрывают только базовый сценарий (`SIGINT` как сигнал завершения).

## ⚙️ Быстрая сборка и тесты
```bash
cd 04_childctl
make
./childctl 2 TERM INT USR1
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add childctl.c
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```