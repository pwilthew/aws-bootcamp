FROM python:3.10-slim-buster

# Inside container
WORKDIR /backend-flask

# Outside container -> Inside container
COPY requirements.txt requirements.txt

# Inside container
RUN pip3 install -r requirements.txt

# Outside container -> Inside container
# . means everything in the cur dir
# First . means /backend-flask (outside container)
# Second . means /backend-flask (inside container)
COPY . .

# Set Env Vars inside container
ENV FLASK_ENV=development

EXPOSE ${PORT}

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]