FROM python:3.11

WORKDIR /server
COPY requirements.txt /server/requirements.txt
# Actualiza y no genera cache al instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY . /server
# Corre el comando de ejecución del servidor
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]