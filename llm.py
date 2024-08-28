import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql_query(human_query: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a SQL assistant."},
            {"role": "user", "content": human_query},
        ],
    )
    sql_query = response.choices[0].message['content'].strip()
    return sql_query
