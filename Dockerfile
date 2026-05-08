FROM python:3.10-slim
RUN apt-get update -qq && apt-get -y install ffmpeg git
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-m", "bot" ]
