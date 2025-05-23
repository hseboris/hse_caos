# ChildCtl (3x)

## 📝 Условие

Modify the previous `childctl` program so that it:

- accepts `<timeout> <quit_signal> <signal1> [signal2 ...]` as arguments;
- prints `Parent heartbeat: N` every `<timeout>` seconds;
- installs signal handlers for all listed signals;
- prints `[Caught: SIGNAL_DESCRIPTION]` on every handled signal;
- terminates **only after receiving `quit_signal` three times**.

## ℹ️ Примечание

- Use `strsignal`, `sigaction`, `SA_RESTART`, and `sigemptyset`.
- Use `sig_atomic_t` to count `quit_signal` arrivals.
- You must check all syscall return values and print errors with `perror()` or `fprintf(stderr, ...)`.

## ⚙️ Быстрая сборка и тесты

```bash
cd 05_childctl_3x
make                                      # сборка программы
python3 -m unittest discover -v tests     # запуск автотестов
```

## 🧹 Очистка

```bash
make clean
```

## 🚀 Автотесты в GitHub Actions

```bash
git add .
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```