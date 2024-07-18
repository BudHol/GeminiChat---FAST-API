from fastapi import FastAPI, Request, Form 
from fastapi.templating import Jinja2Templates 
import os 
import google.generativeai as genai 

os.environ['GOOGLE_API_KEY']="AIzaSyCPKy-E9Q3uAp41InvZf7XMZMqx5_b37so"  
genai.configure(api_key=os.environ['GOOGLE_API_KEY']) 

model = genai.GenerativeModel("gemini-1.5-flash") 

app = FastAPI() 
templates = Jinja2Templates(directory='templates') 

@app.get("/") 
async def root(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request}) 
@app.post("/")
async def handle_input(request: Request, user_input:str = Form(...)): 
    response_data = model.generate_content(user_input) 
    return templates.TemplateResponse("index.html", {"request": request, "response_data": response_data.text}) 
