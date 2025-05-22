# Parallel Sum (C++)

## 📝 Условие

Write a program that:
- inputs integer `N` (N ≥ 16);
- allocates an array of `N` random integers;
- splits it into 4 approximately equal parts;
- creates 4 worker threads:
    - each thread computes the sum of its section;
    - each adds its result to a shared `sum` variable;
- the main thread:
    - prints the full array;
    - waits for all threads;
    - prints the final result stored in `sum`.

## ℹ️ Примечание

Используйте `std::thread`, `std::mutex`, `std::lock_guard`.  
Все участки массива должны быть безопасно просуммированы.

## ⚙️ Быстрая сборка и тесты
```bash
cd cpp
make
echo 32 | ./sum_threads
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
make clean
```

## 🚀 Автотесты в GitHub Actions
```bash
git add sum_threads.cpp
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```