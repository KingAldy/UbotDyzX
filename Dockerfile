FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libx11-6 libgl1 && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "PyroUbot"]
