from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    ...

@router.post("/login")
async def login(email: str, password: str):
    ...

@router.put("/update")
async def update():
    ...

@router.delete("/delete")
async def delete():
    ...