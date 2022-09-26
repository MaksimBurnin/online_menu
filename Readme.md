# Online Menu test task

for Alemira

## Installation

Docker compose

```bash
docker compose run web ./manage.py migrate
docker compose run web ./manage.py createsuperuser
```

## Usage

Run:
```bash
docker compose up
```


Fill Categories, Allergens, and Dishes by navigating to:

```
http://127.0.0.1:8000/admin
```


## API

Endpoints:

```
[GET]  /api/dishes
[POST] /api/dishes
```

HAR archive with examples is avalible here: [example_requests.har](example_requests.har).
It is importabe in both Insomnia and Postman.
