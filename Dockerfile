FROM python:3.9.6-buster 

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install -U pip && pip install pipenv

RUN pipenv install --system --ignore-pipfile

WORKDIR /app

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]