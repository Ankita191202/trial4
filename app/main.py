# from fastapi import FastAPI
# from app.routes import router

# app = FastAPI()

# app.include_router(router)

# @app.get("/")
# def root():
#     return {"message": "API is running trial2"}


from fastapi import FastAPI, HTTPException
from app.routes import router
import os

app = FastAPI()

app.include_router(router)

DATA = []

@app.get("/")
def root():
    return {"message": "Server running"}

# ❌ 1. Syntax error (missing colon)
@app.get("/items")
def get_items():
    return {"items": DATA}


# ❌ 2. Logic + runtime error
@app.post("/items")
def create_item(name: str, price: int):
    if price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")

    DATA.append({"name": name, "price": price})
    return {"message": "Item added"}


# ❌ 3. Division by zero risk
@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": a / b}


# ❌ 4. Undefined variable
@app.get("/debug")
def debug():
    return {"value": None}  # Fixed: removed undefined variable


# ❌ 5. Wrong async usage
@app.get("/async-test")
async def async_test():
    import asyncio
    result = await asyncio.get_event_loop().run_in_executor(None, slow_function)
    return {"result": result}


# ❌ 6. Function defined incorrectly
def slow_function():
    import time
    time.sleep(2)
    return "done"


# Fixed: removed duplicate route
@app.get("/another")
def another_root():
    return {"message": "Duplicate route fixed"}


# ❌ 8. Bad import usage
@app.get("/env")
def get_env():
    return {"env": os.getenv("APP_ENV", "development")}  # Fixed: use string key


# ❌ 9. Wrong return type
@app.get("/wrong")
def wrong():
    return {"values": list(set([1, 2, 3]))}  # Fixed: serialize as list


# ❌ 10. Missing return
@app.get("/no-return")
def no_return():
    x = 10 + 20
    return {"result": x}


# ❌ 11. Type issue
@app.get("/concat")
def concat(a: int, b: int):
    return {"result": str(a) + "test"}  # Fixed: convert int to str


# ❌ 12. Bad exception handling
@app.get("/error")
def error():
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        raise HTTPException(status_code=500, detail=str(e))  # Fixed: handle error properly