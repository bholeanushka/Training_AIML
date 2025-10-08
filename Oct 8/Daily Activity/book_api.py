from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app = FastAPI()

#Pydantic model for validation

class Book(BaseModel):
    id:int
    title:str
    author:str
    price:float
    in_stock:bool

#In-memory "database"
books = [
    {
    "id":1,
    "title":"Wings of Fire",
    "author":"APJ",
    "price": 350,
    "in_stock":True
    }
]

@app.get("/books")
def get_all_books():
    return {"Books ": books}

@app.get("/books/available")
def available_books():
    avail_book=[]
    for e in books:
        if e["in_stock"] == True:
            avail_book.append(e)

    return {"available books " : avail_book}
@app.get("/books/count")
def count_books():
    return {"Total Books",len(books)}




@app.get("/books/search")
def search_books(title:str,author:str):
    for e in books:
        if e["title"] == title and e["author"] == author:
            return e
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/{b_id}")
def get_book(b_id: int):
    for e in books:
        if e["id"] == b_id:
            return {"Book detail": e}
    raise HTTPException(status_code=404, detail="Book not found")

# ----- POST-----

@app.post("/books",status_code=201)
def add_book(b: Book):
    for e in books:
        if e["id"] == b.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    books.append(b.dict())
    return{"message":"Book added successfully","Book":b}


# #----- PUT -----
@app.put("/books/{b_id}")
def update_book(b_id: int,updated_books: Book):
    for i,e in enumerate(books):
        if e["id"] == b_id:
            books[i] = updated_books.dict()
            return {"message":"Books updated","book":updated_books}
    raise HTTPException(status_code=404, detail="Book not found")

# #----- DELETE -----
@app.delete("/books/{b_id}")
def delete_book(b_id: int):
    for i,e in enumerate(books):
        if e["id"] == b_id:
            deleted_book = books.pop(i)
            return {"message":"Book deleted","Books":deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")

