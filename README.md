# qa-has-power-automation

## What is needed:
### Virtual environment configuration - recommended option
1. Python 3 (e.g. 3.7)
2. pip:
    ```bash
    $ sudo apt install python3-pip
    ```
3. Virtual environment for Python
    
    1. Installation
        ```bash
        $ pip3 install virtualenvwrapper
        ```
    2. Add to file "~/.bashrc"
        ```bash
        $ echo 'VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> ~/.bashrc
        $ echo 'source `which virtualenvwrapper.sh`' >> ~/.bashrc
        $ source ~/.bashrc 
        ```
    3. Create your own virtualenv:
        ```bash
        $ mkvirtualenv qa-has-power -p `which python3.7`
        ```
    4. Switch to your virtualenv
        ```bash
        $ workon qa-has-power
        ```
    
4. Requirements:
    1. Behave and Selenium (installation from requirements):
        ```bash
        $ pip install -r requirements.txt
        ```

5. Chrome and chromedriver 
   ```bash
   $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
   $ wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip && sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && sudo chmod 755 /usr/local/bin/chromedriver;
   ```   

### Docker environment configuration - alternative option
1. Docker installation:
    ```bash
    $ ./install_docker.sh
    ```
2. Give access to show windows run in Docker
    ```bash
    $ xhost +local:root
    ```

3. Build docker image
    ```bash
    $ docker build -t docker_tag .
    ```

4. Run docker image
    ```bash
    $ docker run -it -v $PWD:/usr/src -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -t docker_tag bash
    ```


## Test: 
1. Run test file to check if your environment is ready to use:
    1. For virtualenv - with virtualenv switched on
        ```bash
        $ python ./check.py
        ```
    2. For Docker - inside the docker container (after command $ docker run...) :
        ```bash
        $ python check.py 
        ```
        


## Usage:
1. Run tests:
    ```bash
   $ behave
    ```
2. To debug during implementation - you can use ipdb, 
    1. Put this lines before line with error:
        ```python
       import ipdb 
       ipdb.set_trace()
        ```
    2. Run tests with parameter:
        ```bash
        $ behave --no-capture
        ```
    3. Tests should stop in correct place, there should be possible to n
