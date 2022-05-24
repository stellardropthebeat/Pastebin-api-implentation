# start from base
FROM python:3.9

# copy our application code
ADD . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt


# expose port
EXPOSE 5000

# start app
CMD [ "poetry", "run", "gunicorn", "-w", "4", "-b", "127.0.0.1:5000", "app:app" ]



