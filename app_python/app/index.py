"""
This code generates HTML page with date and time using FAST API."""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import datetime
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/time", response_class=HTMLResponse)
async def read_item(request: Request):
	"""
	:param request: GET request from browser
	:return: HTML page with date and time generated by JS code snippet
	"""
	with open('time.txt', 'a') as fp:
		fp.write(str(datetime.datetime.now()) + '\n')
	return templates.TemplateResponse("date_time.html", {"request": request})


@app.get("/visits", response_class=HTMLResponse)
async def read_file(request: Request):
	return '\n'.join(open('time.txt', 'r').readlines())
