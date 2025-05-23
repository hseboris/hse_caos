# MQSignal

## 📝 Условие

- Ожидать сообщения в очереди `/mqsignal`;
- Печать всех сообщений;
- Завершать работу при:
  - сообщении `"QUIT"` (строго 4 байта);
  - сигнале `SIGINT` (Ctrl+C);
- Обязательно:
  - закрывать очередь;
  - удалять очередь;
  - проверять все ошибки.

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

### Терминал 1:

```bash
cd ..
./mqsignal
```

### Терминал 2:

```bash
cd manual
./snd_mq /mqsignal "hello"
./snd_mq /mqsignal "QUIT"
```

или нажмите `Ctrl+C` в первом терминале.

## 🐳 Docker

```bash
docker build -t mqsignal-lab .
docker run -it -d --name mqsignal-container --cap-add SYS_ADMIN \
  --mount type=bind,source=$(pwd),target=/lab09/08_mqsignal \
  --mount type=tmpfs,destination=/dev/mqueue \
  mqsignal-lab
```

### Терминал 1:

```bash
docker exec -it mqsignal-container bash
cd /lab09/08_mqsignal
make
./mqsignal
```

### Терминал 2:

```bash
docker exec -it mqsignal-container bash
cd /lab09/08_mqsignal/manual
make
./snd_mq /mqsignal "Hello"
./snd_mq /mqsignal "QUIT"
```

### Остановить и удалить контейнер:

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