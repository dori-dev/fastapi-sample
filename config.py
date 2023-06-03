import time
import datetime
import aiofiles

from fastapi import FastAPI, Request
from routers import users, items

app = FastAPI()
app.include_router(users.router, tags=['users'])
app.include_router(items.router, tags=['items'])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 100
    response.headers['X-Process-Time'] = f"{round(process_time, 2)}ms"
    return response


@app.on_event('startup')
async def startup_event():
    now = datetime.datetime.now()
    async with aiofiles.open('server_time.log', 'a') as log:
        await log.write(f'Application started at: {now}\n')


@app.on_event('shutdown')
async def shutdown_event():
    now = datetime.datetime.now()
    async with aiofiles.open('server_time.log', 'a') as log:
        await log.write(f'Application shutdown at: {now}\n')
