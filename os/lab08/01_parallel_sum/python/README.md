# Parallel Sum (Python)

## 📝 Условие

Write a program that:
- inputs integer `N` (N ≥ 16);
- creates an array of `N` random integers;
- splits it into 4 approximately equal parts;
- creates 4 `threading.Thread` workers:
    - each computes the sum of its chunk;
    - adds its result to a shared variable using a `Lock`;
- the main thread:
    - prints the array;
    - waits for threads;
    - prints the total sum.

## ℹ️ Примечание

Используйте `threading.Thread`, `threading.Lock`.  
Решение не должно использовать глобальные переменные без синхронизации.

## ⚙️ Быстрая сборка и тесты
```bash
cd python
echo 32 | python3 sum_threads.py
python3 -m unittest discover -v tests
```

## 🧹 Очистка
```bash
rm -f *.pyc
```

## 🚀 Автотесты в GitHub Actions
```bash
git add sum_threads.py
git commit -m "Ваше сообщение"
git push                              # статус проверки появится в Actions ✅
```