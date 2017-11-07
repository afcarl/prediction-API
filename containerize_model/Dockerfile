FROM python:3.6.2

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./api_requirements.txt /usr/src/app/api_requirements.txt

RUN pip install -r api_requirements.txt

ARG model_dir

# Add requirements to leverage Docker cache
ADD $model_dir/model_dir/requirements.txt /usr/src/app/requirements.txt

# Install requirements
RUN pip install -r requirements.txt

ADD ./app.py /usr/src/app/app.py
ADD ./base_model.py /usr/src/app/base_model.py
ADD ./manage.py /usr/src/app/manage.py

# Add the project to the docker container
# ADD D:/DoingDataScience/predictionAPI /usr/src/app
ADD $model_dir /usr/src/app

# Run the server
CMD python manage.py runserver -h 0.0.0.0