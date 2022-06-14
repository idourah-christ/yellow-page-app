FROM python:3.9.5-slim-buster as builder 

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFRED 1 

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc 

RUN pip install --upgrade pip 

RUN pip install flask

COPY . /usr/src/app/

# install dependecies 
COPY ./requirements.txt /usr/src/app/

RUN pip wheel --no-cache-dir  --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt 


FROM python:3.9.5-slim-buster

# create directory for the app user
RUN mkdir -p /home/app 

# create the app user 
RUN addgroup --system app && adduser --system app 

ENV HOME=/home/app 
ENV APP_HOME=/home/app/web 

RUN mkdir $APP_HOME

WORKDIR $APP_HOME 

# install dependencies 
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy the entrypoint.sh 
COPY ./entrypoint.sh $APP_HOME 

# copy the project 
COPY . $APP_HOME 

# chown all files to the app user
RUN chown -R app:app $APP_HOME

# change the user to app 
USER app 

CMD ["gunicorn","-b", "0.0.0.0:4000","manage:app"]

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

