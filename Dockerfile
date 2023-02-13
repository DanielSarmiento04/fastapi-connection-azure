# Select the base image
FROM  python:3.10

# Set the working directory
WORKDIR /code

RUN python -m pip install --upgrade pip

# Install the dependencies
RUN apt-get update

COPY ./requirements.txt /code/requirements.txt


# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the source code
COPY ./app /code/app



COPY ./main.py /code/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]