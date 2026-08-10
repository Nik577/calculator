# Калькулятор

Консольное приложение "Калькулятор", разработанное на Python.

## Запуск (Docker)

Для начала скачайте репозиторий на свой компьютер:
```bash
git clone https://github.com/Nik577/calculator.git
cd calculator
```

Затем запустите приложение:
```bash
docker-compose up -d meme-sidecar
docker-compose run calculator
```

## Запуск (Python)
1. Запустите микросервис:
```bash
cd meme_sidecar
pip install -r requirements.txt
uvicorn main:app --port 8000
```
2. В другом терминале запустите калькулятор:
```bash
cd calculator
python main.py
```

## Описание
- Приложение работает с числами от 1 до 10 включительно.
- Поддерживаемые операции: `+`, `-`, `*`, `/`.
- Формат ввода: `число оператор число` (например `1 + 2`).
