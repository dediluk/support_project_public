FROM python

ENV PYTHONDONTWRITTENBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

