from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os

import requests
from datetime import date, datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

app  = FastAPI()
credential = os.getenv('CREDENTIAL')

@app.get("/")
def read_root():
    data = open("./templates/first.html").readlines()
    htmlData = """"""
    for line in data:
        htmlData = htmlData + line
    return HTMLResponse(content=htmlData, status_code=200)