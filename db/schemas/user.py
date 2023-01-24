def user_schema(user: dict) -> dict:
    return {
        "username": user["email"],
        "name": user["name"],
        "lastname": user["lastname"],
        "email": user["email"],
        "password": user["password"]
    }