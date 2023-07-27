FROM python:3.9

WORKDIR /app
COPY requirements.txt /app/requirements.txt
# Actualiza y no genera cache al instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app
# Mantiene el contenedor corriendo todo el tiempo
CMD bash -c "while true; do sleep 1; done"