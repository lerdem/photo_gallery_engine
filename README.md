[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Photo gallery
[![Python version](https://img.shields.io/badge/python-3.6.5-blue.svg)](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-5-final)
[![PyPI version](https://img.shields.io/badge/django-1.11.13-brightgreen.svg)](https://pypi.org/project/Django/1.11.13/)
[![Docker](https://img.shields.io/badge/docker-CE-brightgreen.svg)](https://www.docker.com/community-edition)

# Table of contents

- [Installation](#installation)
- [Start](#start)
- [Updating](#updating)
- [Uninstallation](#uninstallation)


# Installation

[(Back to top)](#table-of-contents)
```
git clone https://github.com/lerdem/photo_gallery_engine.git
```
# Start
For running project
```
cd photo_gallery_engine
docker-compose up -d --build
```
For running migrations
```
docker exec -it django_photo_gallery ./src/manage.py migrate
```
Create super user for django admin
```
docker exec -it django_photo_gallery ./src/manage.py createsuperuser
```

# Updating

[(Back to top)](#table-of-contents)

Locate in <you-paht>/photo_gallery_engine
```
git pull origin master
```


# Uninstallation

[(Back to top)](#table-of-contents)

```
rm -r photo_gallery_engine/
```
