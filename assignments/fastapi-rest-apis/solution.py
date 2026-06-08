from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="FastAPI - Items API (Solution)")


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Item(ItemBase):
    id: int


# In-memory "database"
items_db: List[Item] = [Item(id=1, name="Sample", description="Un item exemple", price=9.99)]


@app.get("/items", response_model=List[Item])
def list_items():
    return items_db


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemBase):
    # Assign server-side ID
    next_id = max((i.id for i in items_db), default=0) + 1
    new_item = Item(id=next_id, **item.dict())
    items_db.append(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: ItemBase):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = Item(id=item_id, **updated.dict())
            return items_db[idx]
    raise HTTPException(status_code=404, detail="Item non trouvé")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item non trouvé")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("solution:app", host="127.0.0.1", port=8001, reload=True)
