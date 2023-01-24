# TODO API

Task management microservice demo.

## Features
- Create, Read, Update and Replace a task.

## Tech

This project is developed with [FastApi](https://fastapi.tiangolo.com) and [MongoDB](https://www.mongodb.com) and of course **TODO API** itself is open source with a [public](https://github.com/josueisaihs/TodoBackend) on GitHub.

## Install
---
### Unix
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

### Run server
Finally, run the following to launch the local server.
```sh
uvicorn main:app --reload
```

Now, to know how it works, consult the documentation in [documentation](http://localhost:8000/docs).

---
## Next step

Authentication using JWT.