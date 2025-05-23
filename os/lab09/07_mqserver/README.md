# MQServer

## 📝 Условие

Write a program `mqserver.c` that:

- creates a POSIX message queue `/mqserver`;
- waits and receives messages in a loop using `mq_receive`;
- prints every message received;
- if the message is equal to `"QUIT"` (5 bytes including `\0`), exits;
- unlinks the queue before exiting.

Example:
```bash
$ ./mqserver
Received: hello
Received: one
Received: two
```

## ℹ️ Примечание

- Use `mq_open`, `mq_receive`, `mq_close`, `mq_unlink`;
- Messages are compared using `strcmp(buf, "QUIT")`;
- Memory should be dynamically allocated based on `mq_attr.mq_msgsize`.

## ⚙️ Быстрая сборка и тесты

```bash
cd 07_mqserver
make
python3 -m unittest discover -v tests
```

## 🧪 Ручное тестирование

```bash
cd manual
make

# в одном терминале:
../mqserver

# в другом:
./snd_mq /mqserver "msg1"
./snd_mq /mqserver "msg2"
./snd_mq /mqserver "QUIT"
```

Ожидаемый результат:

```
Received: msg1
Received: msg2
```

## 🧪 Запуск на macOS через Docker

Если вы используете macOS и хотите протестировать POSIX message queues:

### 1. Соберите Docker-образ

```bash
docker build -t mqserver-lab .
```

### 2. Запустите контейнер

```bash
docker run --rm -it --cap-add SYS_ADMIN \
  --mount type=bind,source=$(pwd),target=/lab09/07_mqserver \
  --mount type=tmpfs,destination=/dev/mqueue \
  mqserver-lab
```

### 3. Внутри контейнера

```bash
cd manual
make

../mqserver &
./snd_mq /mqserver "Hello"
./snd_mq /mqserver "QUIT"
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