FROM python:3.13-alpine

WORKDIR /app

COPY app.py .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD wget -q --spider http://127.0.0.1:8000/health || exit 1

CMD ["python", "app.py"]
