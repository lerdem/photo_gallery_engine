FROM python:3.6-jessie
ENV PYTHONUNBUFFERED 1
ENV APP_DIR=/app/
RUN mkdir -p $APP_DIR &&\
	pip install -U pip &&\
	groupadd -r django_user &&\
	useradd -r -g django_user -d $APP_DIR -s /sbin/nologin -c "Docker image user" django_user
WORKDIR $APP_DIR
ARG dev=requirements.dev.txt
ARG prod=requirements.txt
COPY $dev $APP_DIR
COPY $prod $APP_DIR
RUN pip install -r $dev
COPY . $APP_DIR
RUN chown -R django_user:django_user $APP_DIR
