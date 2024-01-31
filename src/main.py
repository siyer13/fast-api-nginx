from fastapi import FastAPI 
import socket

app = FastAPI()

@app.get('/api-endpoint')
async def first_api():
    return {"Container ID": socket.gethostname()}