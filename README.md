# dogAPI
This application uses the Flask framework in Python to integrate a dog API
## Project Description 
Using Flask, I implement an API with pictures and breed information for various dogs. The web application supports two functionalities: finding 10 random images of a specific dog breed and listing all dog breeds. The ideal route that the user should follow is:
1. Identify all the dog breeds
2. Choose one dog breed based on the list of dog breeds
3. Search for 10 images of their specific dog breed 

The web application aligns with my passion for pets and explores the realm of Flask, Docker, and Jinja2 templating engine. 
## Features 
* **Clear Design:** Two functions that support the Dog API using HTTP requests
## Technology 
Modern lightweight technologies and frameworks
* Docker
* Jinja2
* Flask
## How to Run
First, Download the starter files. I would recommend running the project locally first using the terminal (I assume all dependencies are installed): 

1. Create a Python virtual environment (Change env with the name of your choice): ```python3 -m venv env```
2. Activate the environment: ```source env/bin/activate```
3. Install the dependencies from requirements.txt: ```pip install -r requirements.txt```
4. Launch the application using Python: ```python app.py```

If everything is running smoothly and normally, then deploy with Google Cloud using Cloud Shell:

1. Build the Docker image using gcloud build specifying timeout and personalized tag
```gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/Github```
2. Deploy the container image using gcloud run specifying the docker image, service account, platform scope, region, and access scope
```
gcloud run deploy Github \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/Github
  --service-account guestbook@cloud-castr-vicastro.iam.gserviceaccount.com \
  --platform managed \
  --region us-west1 \
  --allow-unauthenticated
```
Use your service account and change the parameters based on your requirements. 
## External Sources 
* https://media.pdx.edu/media/t/1_xopzs30j
