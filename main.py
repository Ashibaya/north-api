from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from auth import auth
from navigation import nav_router


middleware = [Middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)]

app = FastAPI(root_path = "/api",middleware=middleware)


@app.get('/')
async def say_hello():
    return {"text": "Api is Work!"}

app.include_router(
    router=auth.router,
    prefix='/auth',
    responses={404: {"description": "Not found"}}
)

app.include_router(
    router=nav_router.router,
    prefix='/nav',
    responses={404: {"description": "Not found"}}
)
