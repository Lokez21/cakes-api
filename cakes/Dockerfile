# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /cakes

# Copy the requirements file into the container at /cakes/
COPY requirements.txt /cakes/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /cakes/
COPY . /cakes/

# Run the collectstatic command during the image build
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 80

# Run the specified command within the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
