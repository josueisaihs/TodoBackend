from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config.settings import Settings

from routers import todo

'''
Organization
 |
 |__ main.py
 |__ dependencies.py
 |__ routers
 |     |__ items.py
 |     |__ users.py
 |__ db
 |     |__models
 |     |        |__item.py
 |     |        |__user.py
 |     |__schemas
 |     |        |__item.py
 |     |        |__user.py
 |     |__client.py
 |__ config
 |     |__ .env
 |     |__ settings.py

Run server -> uvicorn main:app --reload 
Check response -> localhost:8000/
'''

settings = Settings()

app = FastAPI()
app.add_middleware(
    settings.cors_middleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# app.include_router(users.router)
app.include_router(todo.router)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return {'message': 'OK'}
