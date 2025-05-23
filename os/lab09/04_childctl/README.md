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
$ ./childctl 2 TERM INT ALRM
Forked child: 12345
Parent heartbeat: 0
Parent heartbeat: 1
[Caught: Alarm]
Parent heartbeat: 2
[Caught: Interrupt]
Quitting...
Child terminated. Exit status: 9
```

## ℹ️ Примечание

- Используйте `fork`, `sleep`, `strsignal`, `sigaction`, `kill`, `waitpid`, `getpid`.
- Сигналы `INT`, `TERM`, `ALRM`, `QUIT` надёжно перехватываются и подходят для тестирования.
- Не все сигналы могут быть обработаны (например, `KILL`, `STOP` нельзя перехватить).

## ⚙️ Быстрая сборка и тесты
```bash
cd 04_childctl
make
./childctl 2 INT ALRM TERM
python3 -m unittest discover -v tests
```

## 🧪 Ручное тестирование

1. Запусти программу:
   ```bash
   ./childctl 2 INT TERM
   ```

2. В другом терминале узнай PID процесса (или смотри в выводе программы).

3. Отправь сигналы:
   ```bash
   kill -TERM <pid>   # печатает "[Caught: Alarm]"
   kill -INT <pid>    # завершает программу
   ```

Ожидаемый вывод:
```
12345: 0
12345: 1
[Caught: Terminated]
12345: 2
[Caught: Interrupt]
Exiting gracefully on signal INT
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