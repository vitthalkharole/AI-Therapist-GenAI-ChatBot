from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import graph,SYSTEM_PROMPT,parse_response

app = FastAPI()

#validation
class Query(BaseModel):
    message:str



@app.post("/ask")
async def ask(query: Query):

    # AI agent
    # response = ai_agent(query)
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)
    print(tool_called_name)
    return {"response":final_response,
            "tool_called":tool_called_name}


            
            

    

   
