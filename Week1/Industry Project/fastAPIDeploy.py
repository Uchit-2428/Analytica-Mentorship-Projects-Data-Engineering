import fastapi
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home(): #root
  return{"Data":"Test"}

@app.get("/about")
def about():
  return{"Data":"Help"}

from fastapi.responses import FileResponse

@app.get("/What was the best month for sales")
def question1():
	return FileResponse("sales vs month.png")
@app.get("/What city sold the most product")
def question2():
	return FileResponse("sales vs cities.png")
@app.get("/What time should we display advertisements to maximize likelihood of customer's buying product")
def question3():
	return FileResponse("hour vs no. of orders.png")
@app.get("/What products are most often sold together")
def question4():
	return FileResponse("products sold together.png")
@app.get("/What product sold the most")
def question5():
	return FileResponse("quantity ordered vs product vs price.png")
