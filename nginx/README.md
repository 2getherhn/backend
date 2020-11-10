# NGINX IMAGE


###This is readme for nginx setup for 2gether-app. 
Certificates that are created are selfsigned and will be used for setting up nginx with SSL 
so all traffic between AWS ALB and our application is encrypted. Nginx is needed to handle
SSL termination and to serve static content from python application. 
There is only one image in the AWS ECR as nginx wont be changed that much so no CICD is needed. 
If there is a need for new image follow instructions

Go into the nginx folder of this repository and run following commands if run from MACos/Linux:

# Macos or linux
- aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin ECR-URL/together (for this to work AWS CLI newest version needs to be installed and AWS profile setup)

## If run from Windows:

- (Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin ECR-URL/together


## Build and deploy

docker build -t together-nginx .

docker tag together-nginx:latest ECR-URL/together:nginx

docker push ECR-URL/together:nginx