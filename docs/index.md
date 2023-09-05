# Backend Workshop
## HackDuke 2023

Welcome to the backend workshop for [HackDuke 2023](https://2023.hackduke.org/)!
We're going to work on an API that allows users to configure _weather alerts_,
and calls the National Weather Service's own API to fetch data.

This workshop is structured as two companion documents:

- [overview slides](slides/index.html)
- [practical lab](lab/00_prerequisites/)

This site is available at: [**bit.ly/hd23be**](https://bit.ly/hd23be).

The code is available at:
[**github.com/johnjameswhitman/hackduke2023backend**](https://github.com/johnjameswhitman/hackduke2023backend).

# Project layout

The API for this project is organized as follows:

```
├── auth  # app
├── config  # Project setup
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core  # shared functionality
├── docs  # documentation site
├── manage.py
├── requirements
│   ├── base.txt
│   └── development.txt
└── weather  # app
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── services.py  # NWS api client
    ├── tests
    └── views.py
```
