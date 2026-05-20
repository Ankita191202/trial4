# # from fastapi import APIRouter
# # from app.utils import add_numbers

# # router = APIRouter()

# # @router.get("/add")
# # def add(a: int, b: int):
# #     result = add_numbers(a, b)
# #     return {"result": result}


# from fastapi import APIRouter
# from app.utils import add_numbers, multiply_numbers, get_history

# router = APIRouter()

# @router.get("/add")
# def add(a: int, b: int):
#     return {"result": add_numbers(a, b)}

# @router.get("/multiply")
# def multiply(a: int, b: int):
#     return {"result": multiply_numbers(a, b)}

# @router.get("/history")
# def history():
#     return {"history": get_history()}


from fastapi import APIRouter
from app.utils import add_numbers, multiply_numbers, get_history

router = APIRouter()

@router.get("/add")
def add(a: int, b: int):
    return {"result": add_numbers(a, b)}

@router.get("/multiply")
def multiply(a: int, b: int):
    result = a * b
    return {"result": result}

@router.get("/history")
def history():
    data = get_history()
    return {"history": data}