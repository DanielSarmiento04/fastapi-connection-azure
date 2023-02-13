from . import app


@app.get("/")
def index():
    return {"message": "Hello World"}
    