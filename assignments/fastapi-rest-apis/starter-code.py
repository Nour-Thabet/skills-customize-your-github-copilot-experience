from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI - Items API")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# In-memory "database"
items_db: List[Item] = [
    Item(id=1, name="Sample", description="Un item exemple", price=9.99)
]


@app.get("/items", response_model=List[Item])
def list_items():
    return items_db


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # Simple uniqueness check
    if any(existing.id == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="ID déjà utilisé")
    items_db.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item non trouvé")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
