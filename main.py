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

app = FastAPI(middleware=middleware)


@app.get('/hello')
async def say_hello():
    return {"text": "Hello!"}

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
