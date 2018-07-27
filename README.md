
# Chatango [![N|Solid](http://www.robohash.org/set_set4/1337?size=75x60)]

[Check out Chatango Before Installing](https://chat-jango.herokuapp.com/)


##### JustAntoherTwitterClone ingredients:
- Made with Django==1.8.14
- Powered by Python and GoogleMapsAPI
- Designed using [Twitter Bootstrap] version 4.1 
- Icons and Gravatars  provided by [RoboHash](https://www.ronohash.org/) ![N|Solid](http://www.robohash.org/3.14422222224144414411444134233443433331331222111121?size=25x25)
- A dash of JavaScript for flavor
- Served up hot, fresh and free courtesey of [Heroku](https://heroku.com)

Chatango comes complete with all the fixings and is now available in a mobile friendly format that looks great on a mobile phone or a full size monitor.  Once installed users are able to post public messages to the Chatango Public feed as well as send DMs to other users. Other features include Friend/Follow capabilities, a Custom Authenticiation system to manage the Extended User Profile, Robot Gravatars courtsey of [RoboHash](https://www.ronohash.org/) and a variety of mapping options to track other users!!!  

### Getting Started
Before installing Chatango take a minute and verify that you have all the ingredients.  
- git 
- python 2.7
- pip or an equivlant python module installer
- virutalenv or it's equivalant
- virtualwrapper

### Installation
Once you have ensured that you have all the fixings listed above you can begin the installation process. If you have done this sort of thing before installation should be as easy as creating cloning the repository, creating a virtual environment and executing pip install on the requirements.txt file.  If this is your first time or you are new to Django or Python simply following the steps below and you should be up and running in no time.  

First you will need to clone the github repository which will download the software to your machine
```sh
$ git clone https://github.com/jasoncwilley/Chatango-front-end.git
```
Once the software finishes downloading you should create virtual enviroment to run the software in using following command.  
```sh
$ mkvirtualenv chatango
```

Now fire up the virtual environment
```sh
$ workon chatango
```
If all went well your command prompt should change from
```sh
$ 
```
to 
```sh
(chatango) $
```
Now that the vm is running cd into the Chatango directory
```sh
(chatango) $ cd Chatango-front-end.git
```
Install the the remaining dependencies by running the following command 
```sh
(chatango) $ pip install -r requirements.txt
```
Before you can use Chatango you need migrate the create/migrate the database
```sh
(chatango) $ python manage.py makemigrations
```
then update the database with 
```sh
(chatango) $ python manage.py migrate
```
You should be good to go if you made it this far and you can start Chatango with the following command
```sh
(chatango) $ python manage.py runserver 0.0.0.0:5555
```
Now open up a web browser and navigate to 0.0.0.0:5555 and you should see the registration page.  
