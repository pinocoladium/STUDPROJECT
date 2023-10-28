FROM python:3.9

COPY . /src
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt
ENV MY-ENV=crud_env
WORKDIR src
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]