FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./ /app

RUN pip3 install --upgrade pip
RUN pip3 install spacy
RUN python -m spacy download en_core_web_sm
