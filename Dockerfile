FROM python:3.8
WORKDIR /src
COPY ./src/src /src
RUN pip install -r requirements.txt
RUN uvicorn app:app --reload
#CMD ["uvicorn", "app:app"]
