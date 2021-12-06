from fastapi import FastAPI
from cassandra.cluster import Cluster

app = FastAPI()
cluster = Cluster(['194.163.141.181'])
session = cluster.connect()

@app.get("/")
async def root():
    return {"message": "Hello World"}