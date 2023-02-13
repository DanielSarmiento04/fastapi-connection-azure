from . import app
from fastapi.responses import JSONResponse, RedirectResponse

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/custom_response")    
def custom_response():
    # solve Access-Control-Allow-Origin
    response = JSONResponse(
        content={"message": "Hello World"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "POST, GET",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Expose-Headers": "*",
            "Access-Control-Max-Age": "3600",
        },

    )
    return response
