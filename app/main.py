from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import main as ask_me_policy

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/submit", response_class=HTMLResponse)
async def submit_question(request: Request, question: str = Form(...)):
    answer = ask_me_policy.process_question(question)
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
