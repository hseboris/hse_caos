# ChildCtl

## 📝 Условие

Write a program `childctl.c` that:
- takes `<timeout> <quit_signal> <signal1> [signal2 ...]` as arguments;
- forks a child that runs infinitely;
- parent process:
    - every `<timeout>` seconds prints heartbeat counter and its PID;
    - installs signal handlers for listed signals, printing signal descriptions;
    - when `quit_signal` is received, prints "Exiting gracefully ..." and exits.

Example:
```bash
$ ./childctl 2 INT QUIT
Parent heartbeat: 0
Parent heartbeat: 1
[Caught: Quit]
Parent heartbeat: 2
[Caught: Interrupt]
Exiting gracefully on signal INT
```

## ℹ️ Примечание

- Используйте `fork`, `sleep`, `strsignal`, `sigaction`, `kill`, `waitpid`, `getpid`.
- Рекомендуемые сигналы для тестирования: `INT`, `QUIT`, `TERM`.
- Сигналы `KILL`, `STOP` перехватить невозможно и не подходят.

## ⚙️ Быстрая сборка и тесты
```bash
cd 04_childctl
make
./childctl 2 INT QUIT
python3 -m unittest discover -v tests
```

## 🧪 Ручное тестирование

1. Запусти:
   ```bash
   ./childctl 2 INT QUIT
   ```

2. В другом терминале получи PID:
   ```bash
   ps aux | grep childctl
   ```

3. Отправь сигналы:
   ```bash
   kill -QUIT <pid>   # напечатает [Caught: Quit]
   kill -INT <pid>    # завершит программу
   ```

Ожидаемый вывод:
```
Parent heartbeat: 0
Parent heartbeat: 1
[Caught: Quit]
Parent heartbeat: 2
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