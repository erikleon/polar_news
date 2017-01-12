# Polar News
Developers: Erik Karwatowski

### Development Setup
* Clone this repo
* Setup a local environment for testing using [Mamp](https://www.mamp.info/en/) or setup [Apache, Mysql, and PHP](https://coolestguidesontheplanet.com/get-apache-mysql-php-and-phpmyadmin-working-on-osx-10-11-el-capitan/) and [virtuals hosts](https://coolestguidesontheplanet.com/how-to-set-up-virtual-hosts-in-apache-on-mac-osx-10-11-el-capitan/)
* Styling is handled by sass, install [Compass](http://compass-style.org/install)
* Install [python ~3.5](https://www.python.org/downloads/).
* Install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
```
python get-pip.py
```
* Install required python packages
```
pip install requirements.txt
```

## Development
- Copy `polar_news/sample-settings.py` to `polar_news/settings.py` and populate your local MYSQL database, user, and password
- Prepare local environment
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
- Compile css
```sh
cd polar/static/stylesheets/ && compass compile watch
```


