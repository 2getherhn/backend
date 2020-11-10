# 2Gether - logistics for times of need

This is a django app to coordinate the logistics between the ones that need help and the ones willing to provide it.

## Developers guide

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

### Local env
- [Python3.7+](https://www.python.org/downloads/) installed. 
- [PIP](https://pip.pypa.io/en/stable/installing/) installed - the officially recommended Python packaging tool.
- Virtual environment set up - we recommend using [conda](https://docs.conda.io/en/latest/) or [virtualenv](https://virtualenv.pypa.io/en/latest/).

and then creating to use your virtual env

* `pyenv virtualenv togetherapp` to create it
* `pyenv activate togetherapp` to activate it
* `pyenv deactivate` to activate it

### Docker env
- Docker
- Docker compose

 

### First steps
First you need to clone project from 2gether repository to your local machine. 

Simple 

```
git clone https://github.com/ayuda-app/backend
```
command will clone project on your local machine

### For local env:
Create and activate virtual environment:
```
python manage.py -m venv {name_of_the_environment}

. {name_of_the_environment}/bin/activate
```
This is one of many ways to create and activate venv. Alternatively, you can use one of the suggestions listed in prerequisites


### Installing

Execute

```
pip install -r requirements.txt
```

### Running
To run the server on your local machine:
- Setup [docker compose](https://docs.docker.com/compose):
- Then run 
    ```
    docker-compose up 
    ``` 
  Then you can access http://localhost:8000
  
#### Important note: 
Please make sure to assign yourself a ticket before working on it.

## Directories overview
```
    
    ├── app
    │    ├── migrations    contains database schema migrations   
    │    ├── models        contains app models
    │    ├── admin.py
    │    ├── apps.py
    │    ├── filters.py
    │    ├── test.py
    │    └── views.py
    │      
    ├── ngix
    ├── together
    │     ├── settings               contains settings for different environments
    │     │     ├── default.py
    │     │     ├── dev.py                  
    │     ├── asgi.py  
    │     ├── constants.py 
    │     ├── wsgi.py
    │     └── urls.py
    │
    │
    ├── static
    ├── manage.py
    ├── readme.md
    ├── .dockerignore
    ├── .gitignore
    ├── appspec_template.yaml
    ├── buildspec.yml
    ├── docker-compose.yml
    ├── Dockerfile
    └── requirements.txt
   
```


## Deployment


Deployment is done on every push to either dev/master branch. Code is deployed to dev/prod environments respectively. 
CodePipeline is setup to listen on changes on github repository. On every push, new docker image is built and pushed to the AWS ECR repo. 

Application is deployed in AWS ECS and is started using gunicorn. All traffic is being routed through nginx container which stips the SSL and doing the serving of static content. More details on the infrastructure is written in wiki page of the [2GETHER](https://github.com/ayuda-app/backend) repository. 

Important files/directories for deployment are:
- nginx/
- buildspec.yml
- appspec_template.yml
- Dockerfile

### Deploying

For deploy on AWS, it is enough to just commit, push, merge the code to the appropriate branch, and CICD will be triggered. After couple of minutes, new version of application will be available. 


## Contributing

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

## Dependencies

Dependencies used within project:
- [Django Rest Framework](https://www.django-rest-framework.org/) toolkit for building Web APIs
