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