from fastapi import APIRouter, status, HTTPException
# from bson import ObjectId

from db.models.user import User
from db.client import db_client

'''
    CRUD for the model User
'''
router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'message': 'Not Found'
        }
    }
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[User] | list)
async def get_users():
    
    return [{'message': 'OK'}]

@router.post('/', status_code=status.HTTP_201_CREATED, response_model = User)
async def set_users():
    
    return {'message': 'OK'}

@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model = User)
async def update_users():
    
    return {'message': 'OK'}

@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_users():
    
    return {'message': 'OK'}


# Create the functions to query the databases here.
