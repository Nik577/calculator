# Builder stage
FROM python:3.11-alpine AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage (легковесный образ)
FROM python:3.11-alpine

WORKDIR /app
# Копируем зависимости из builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY main.py .

CMD ["python", "main.py"]
