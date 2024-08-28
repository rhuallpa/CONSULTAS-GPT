from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm import generate_sql_query
from database import query_db

app = FastAPI()

class UserQuery(BaseModel):
    query: str

@app.post("/human_query")
async def human_query(payload: UserQuery):
    sql_query = generate_sql_query(payload.query)
    if not sql_query:
        raise HTTPException(status_code=400, detail="Falló la generación de la consulta SQL")

    result = query_db(sql_query)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
