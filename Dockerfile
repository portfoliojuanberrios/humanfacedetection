# Usa una imagen base específica de Python 3.11
FROM python:3.11-slim

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala las dependencias del sistema, incluyendo libGL y los paquetes adecuados para Debian Bookworm
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y instala las dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
