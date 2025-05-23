# MQSignal

## 📝 Условие

Write a program `mqsignal.c` that:

- creates a POSIX message queue `/mqsignal`;
- installs a `SIGINT` handler to stop the server on Ctrl+C;
- receives messages in a loop via `mq_receive`;
- prints every message received;
- unlinks the queue and exits gracefully on `SIGINT`.

## ℹ️ Примечание

- Use `mq_open`, `mq_receive`, `mq_close`, `mq_unlink`, `signal`;
- Use `sig_atomic_t` flag to control termination from signal handler;
- Check every system call and print errors using `perror()`;
- The message queue should be properly freed/unlinked even on interruption.

## ⚙️ Быстрая сборка и тесты

```bash
cd 08_mqsignal
make
python3 -m unittest discover -v tests
```

## 🧪 Ручное тестирование

```bash
cd manual
make
```

### Терминал 1 (сервер):

```bash
cd ..
./mqsignal
```

### Терминал 2 (отправка сообщений):

```bash
cd manual
./snd_mq /mqsignal "Hello"
./snd_mq /mqsignal "Another"
```

### Прервать сервер:

Нажмите `Ctrl+C` в первом терминале.

Ожидаемый вывод:

```
Received: Hello
Received: Another
Server stopped by SIGINT
```

## 🧪 Запуск на macOS через Docker

```bash
docker build -t mqsignal-lab .
```

### Запуск контейнера:

```bash
docker run -it -d --name mqsignal-container --cap-add SYS_ADMIN \
  --mount type=bind,source=$(pwd),target=/lab09/08_mqsignal \
  --mount type=tmpfs,destination=/dev/mqueue \
  mqsignal-lab
```

### Терминал 1 (сервер):

```bash
docker exec -it mqsignal-container bash
cd /lab09/08_mqsignal
make
./mqsignal
```

### Терминал 2 (отправка сообщений):

```bash
docker exec -it mqsignal-container bash
cd /lab09/08_mqsignal/manual
make
./snd_mq /mqsignal "Hello"
./snd_mq /mqsignal "QUIT"
```

### Завершение:

```bash
docker stop mqsignal-container
docker rm mqsignal-container
```

## 🧹 Очистка

```bash
make clean
cd manual && make clean
```

## 🚀 Автотесты в GitHub Actions

```bash
git add .
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```