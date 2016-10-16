FROM python:2.7
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT python manage.py makemigrations life_goals\
    python manage.py migrate
CMD python manage.py runserver 0.0.0.0:80