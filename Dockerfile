FROM python:3.7

RUN apt-get update && apt-get install -y unzip

WORKDIR /usr/src

COPY "./requirements.txt" .

RUN pip install -r requirements.txt

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Install Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;
