# Import necessary libraries
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from transformers import pipeline
from fastapi.templating import Jinja2Templates
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

# Initialize the app
app = FastAPI()

# Initialize the chatbot model
tokenizer = AutoTokenizer.from_pretrained('output-small')
model = AutoModelWithLMHead.from_pretrained('output-small')

chat_history_ids = []
step = 0

# # Initialize the templates directory
# templates = Jinja2Templates(directory="WebStuff")

# Define the root endpoint
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
	return templates.TemplateResponse("main.html", {"request": request})

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/WebStuff", StaticFiles(directory="WebStuff"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("WebStuff/main.html")
# Define the chatbot endpoint
@app.post("/chatbot")
async def chatbot(payload: dict):
	global step
	global chat_history_ids
	if step>=5:
		step = 0
		chat_history_ids = []
		return {"message" : 'Fuck off, Kyle. Respect my authoritahhh and start the conversation again'}
	query = payload.get("query")
	#print(query)
	new_user_input_ids = tokenizer.encode(query + tokenizer.eos_token, return_tensors='pt')
	bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
	chat_history_ids = model.generate(
		bot_input_ids, max_length=200,
		pad_token_id=tokenizer.eos_token_id,  
		no_repeat_ngram_size=5,       
		do_sample=True, 
		top_k=100, 
		top_p=0.7,
		temperature = 0.7
	)
	step+=1

	response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
	return {"message": response}

# Run the app
if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)
