import os
from uuid import UUID, uuid4

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods: GET, POST, DELETE, etc.
    allow_headers=["*"],  # Allow all headers
)

class TodoItem(BaseModel):
    id: int
    content: str


class TodoItemCreate(BaseModel):
    content: str

id_counter = 1
todos: list[TodoItem] = []

@app.post("/todos/", response_model=TodoItem)
async def create_todo(item: TodoItemCreate):
    global id_counter
    new_todo = TodoItem(id=id_counter, content=item.content)
    todos.append(new_todo)
    id_counter+=1
    return new_todo


@app.get("/todos", response_model=list[TodoItem])
async def read_todos():
    return todos


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
