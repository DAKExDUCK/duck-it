# DUCK-IT

## Setup

### Linux

1. Clone the repository:

```sh
$ git clone https://github.com/DAKExDUCK/duck-it.git
$ cd duck-it
```

2. Create venv and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Then install the dependencies:

```sh
(venv) $ pip install -r requirements.txt
```


### Windows

Will be later


## Migrations

1. Install mysql server and start it

2. Create `secret_key`
```sh
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

3. Create `.env` file
```
SECRET_KEY="secret_key"

DB_NAME="name"
DB_USER="user"
DB_PASSWD="passwd"
DB_HOST="localhost"
DB_PORT="port"
```

4. Make migrations
```sh
python manage.py makemigrations
```

5. Create super user
```sh
python manage.py createsuperuser
```
