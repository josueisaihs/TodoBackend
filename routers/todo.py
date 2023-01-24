from fastapi import APIRouter, status, HTTPException, Response
from bson import ObjectId

from db.models.todo import TodoRegistered, Todo
from db.client import db_client
from db.schemas.todo import todo_schema, todos_schema

'''
    CRUD for the model Todo
'''
router = APIRouter(
    prefix='/todos',
    tags=['todos',],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'message': 'Not Found'
        }
    }
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[TodoRegistered]|list)
async def get_todos(respose: Response):
    todos = get_alls()
    if len(todos) < 1:
        # if no items, status 204
        respose.status_code = status.HTTP_204_NO_CONTENT
    return todos

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Todo|list)
async def set_todo(todo: Todo, response: Response):
    if type(search_todo("title", todo.title)) == Todo:
        response.status_code = status.HTTP_409_CONFLICT
        return [{"message": "This TODO already exists."}]
    return create_todo(todo)

@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=Todo|list)
async def update_todo():    
    return [{'message': 'OK'}]

@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo():
    return {'message': 'OK'}


# Cree las funciones para consultar las bases de datos aquí.
def search_todo(field: str, key: str, exception_mode: bool = False) -> Todo:
    # returns the "x" if it is found in the database, if it is not found it returns a json 
    # with the message that NOT found, in case the exception mode is activated it throws an exception 400
    try:
        todo = todo_schema(db_client.todo.find_one({field: key}))
        return Todo(**todo)
    except:
        if exception_mode:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad request :("
            )
        return {"error": "Not found."}

def get_alls() -> list[TodoRegistered]:
    # Returns all todos in the database
    return todos_schema(db_client.todo.find(), TodoRegistered)

def create_todo(todo: Todo) -> TodoRegistered:
    todo_obj = dict(todo)
    if "id" in todo_obj:
        # If key id exists, remove it
        del todo_obj["id"]

    id = db_client.todo.insert_one(todo_obj).inserted_id
    
    new_todo = todo_schema(db_client.todo.find_one({"_id": id}))

    return TodoRegistered(**new_todo)