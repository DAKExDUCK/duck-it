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

1. Clone the repository:

```sh
git clone https://github.com/DAKExDUCK/duck-it.git
cd duck-it
```

2. Create venv and activate it:

```sh
python -m venv venv
venv\Scripts\activate.bat
```

3. Then install the dependencies:

```sh
(venv) pip install -r requirements.txt
```


## Migrations

1. Install MySQL server (or MariaDB) and start it 

2. Create `secret_key`
#### Linux:
```sh
$ python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
#### Windows:
```sh
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
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
python manage.py migrate
```

5. Create super user
```sh
python manage.py createsuperuser
```
