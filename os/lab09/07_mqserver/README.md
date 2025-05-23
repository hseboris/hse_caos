# MQServer

## 📝 Условие

Write a program `mqserver.c` that:

- creates a POSIX message queue `/mqserver`;
- waits and receives messages in a loop using `mq_receive`;
- prints every message received;
- if the message is equal to "QUIT" (5 bytes including `\0`), exits;
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
```

> ⚠️ Важно: сначала запустите `mqserver`, чтобы очередь была создана.

### Терминал 1 (сервер):
```bash
cd ..
./mqserver
```

### Терминал 2 (отправка сообщений):
```bash
cd manual
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

Если вы используете macOS и хотите протестировать POSIX message queues (не поддерживаются напрямую в macOS), выполните следующие шаги:

### 1. Соберите Docker-образ

```bash
docker build -t mqserver-lab .
```

### 2. Запустите контейнер в фоновом режиме

```bash
docker run -it -d --name mqserver-container --cap-add SYS_ADMIN \
  --mount type=bind,source=$(pwd),target=/lab09/07_mqserver \
  --mount type=tmpfs,destination=/dev/mqueue \
  mqserver-lab
```

### 3. Откройте первый терминал (сервер)

```bash
docker exec -it mqserver-container bash
```

Внутри:
```bash
cd /lab09/07_mqserver
make
./mqserver
```

### 4. Откройте второй терминал (отправка сообщений)

```bash
docker exec -it mqserver-container bash
```

Внутри:
```bash
cd /lab09/07_mqserver/manual
make
./snd_mq /mqserver "msg1"
./snd_mq /mqserver "msg2"
./snd_mq /mqserver "QUIT"
```

### 5. Завершение контейнера

```bash
docker stop mqserver-container
```

(опционально)
```bash
docker rm mqserver-container
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