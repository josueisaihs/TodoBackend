def todo_schema(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "active": todo["active"],
        "tags": todo["tags"]
    }

def todos_schema(todos: list[dict], model) -> list:
    return [model(**todo_schema(todo)) for todo in todos]