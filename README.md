# README #

### What is this repository for? ###

* The project is about sending messages to multiple recipients (bulk sms)

### How do I get set up? ###

* Download the project or clone from the repo
* Ensure you have `pipenv` installed
* Do a `pipenv install` to install dependencies
* Activate virtualenv `pipenv shell`
* You should have an africastalking account https://africastalking.com/.
  get your API key and username from your account
* copy the `sms/local_settings.example` to `sms/local_settings.py` and edit database settings according to your local database settings, africastalking api key & username and SECRET_KEY
* Create a `secrets.py` file on the same directory as `settings.py` and add the following
* Run `python manage.py migrate`
* Run `python manage.py runserver`

### Setup using Docker ###
* Make sure you have docker (https://docs.docker.com/install/linux/docker-ce/ubuntu/) and docker-compose installed

STEPS TO INSTALL Docker-compose:
* apt install jq -y
* VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | jq .name -r)
* DESTINATION=/usr/bin/docker-compose
* sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
* sudo chmod 755 $DESTINATION

GET STARTED
* git clone https://github.com/AthmanZiri/jenga.git
* cd jenga
* create local_settings.py and add this line from jenga.settings import *
* docker-compose -f docker-compose.prod.yaml up -d --build
* docker-compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput
* docker-compose -f docker-compose.prod.yaml exec web python manage.py createsuperuser
* docker-compose -f docker-compose.prod.yaml exec web python manage.py collectstatic --no-input --clear

you should be able to see the app running on http://<ip-address>

you can run the following to troubleshoot
* docker ps  # list containers created. they should be running
* docker images  # list images created 
* docker-compose logs -f # check logs
* docker-compose exec db psql --username=jenga_io --dbname=jenga_io_prod  # log into database and check if all tables have been created

### To Do List ###

* Project documentation
* Add email backend - Ziri
* Add search functionality
* Admin dashboard - for charts, graphs
* import contacts from csv, excel

### Issues ###

* Caching
* Redirect to contact group creation when nono exists

### Who do I talk to? ###

* Repo owner/admin @athmanziri, @bmwasaru
* Team contacts @ckchivatsi
