from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.delete("/api/users/2", response_model="204")
def delete_user():
    return "204"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)