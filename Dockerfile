FROM python:3.9

WORKDIR /code

COPY ./req.txt ./code/req.txt

RUN pip install -r ./code/req.txt

COPY ./server /code/server

WORKDIR /code/server

EXPOSE 5000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","5000"]
