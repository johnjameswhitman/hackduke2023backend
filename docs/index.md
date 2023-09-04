# Backend Workshop
## HackDuke 2023

Welcome to the backend workshop for HackDuke 2023! This workshop is structured
as two companion documents:

- [overview slides](slides/index.html)
- [practical lab](lab/00_prerequisites/)

This site is available at: [**bit.ly/hd23be**](https://bit.ly/hd23be).

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
    ├── services.py
    ├── tests
    └── views.py
```
