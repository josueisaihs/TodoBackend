**TODO API** itself is open source with a [public](https://github.com/josueisaihs/TodoBackend) on GitHub.

### Install
---
#### Unix
Clone the repository
```sh
git clone https://github.com/josueisaihs/TodoBackend
```

Create virtual environment and activate it:
```sh
cd drones
python -m venv venv/
source venv/bin/activate
```

Install dependencies:
```sh
cd src
pip install -r requirements.txt
```

Create the database with [Mongodb Atlas](https://www.mongodb.com/docs/), you can also use another MongoDB server.
Create the environment variables file in "`config/.env`".

```r
MONGODB_CONNECTION="mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
```

The `SECRET_KEY` key can be any text string, but we recommend generating it as
```sh
openssl rand -hex 32
```
