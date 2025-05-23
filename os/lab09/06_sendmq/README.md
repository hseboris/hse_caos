# SendMQ

## 📝 Условие

Write a program `sendmq.c` that:

- accepts two arguments: a message queue name and a message string;
- opens the queue with `mq_open` in write-only mode;
- sends the message to the queue with priority 1 using `mq_send`.

Example:
```bash
$ ./sendmq /queue "Hello world"
```

## ℹ️ Примечание

- Use POSIX message queues (`mqueue.h`, `mq_open`, `mq_send`, `mq_close`);
- The queue must already exist and be open for writing;
- Print errors using `perror()` and return code 1 on failure.

## ⚙️ Быстрая сборка и тесты

```bash
cd 06_sendmq
make                                      # сборка программы
python3 -m unittest discover -v tests     # запуск автотестов
```

## 🧪 Ручное тестирование

1. Перейдите в подкаталог:

```bash
cd manual
make
```

2. Создайте очередь:

```bash
./crt_mq
```

3. Отправьте сообщение:

```bash
../sendmq /testmq "Hello, MQ!"
```

4. Прочитайте сообщение:

```bash
./rec_mq
```

Ожидаемый результат:

```
Received: Hello, MQ!
Priority: 1
```

5. Очистка:

```bash
make clean
```

## 🧪 Запуск на macOS через Docker

Если вы используете macOS и хотите протестировать POSIX message queues (которые не поддерживаются напрямую в macOS), выполните следующие шаги:

### 1. Соберите образ Docker

```bash
docker build -t sendmq-lab .
```

### 2. Запустите контейнер с монтированием папки и `/dev/mqueue`

```bash
docker run --rm -it --cap-add SYS_ADMIN \
  --mount type=bind,source=$(pwd),target=/lab09/06_sendmq \
  --mount type=tmpfs,destination=/dev/mqueue \
  sendmq-lab
```

### 3. Внутри контейнера

```bash
cd manual
make
./crt_mq

cd ..
make
./sendmq /testmq "Hello from Docker"

cd manual
./rec_mq
```

Ожидаемый результат:

```
Received: Hello from Docker
Priority: 1
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