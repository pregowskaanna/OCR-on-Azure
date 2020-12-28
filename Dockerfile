FROM python:3.8
WORKDIR /src
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
COPY ./src/src /src
RUN pip install -r requirements.txt
RUN uvicorn app:app --reload
#CMD ["uvicorn", "app:app"]