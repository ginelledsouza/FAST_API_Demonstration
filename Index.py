from fastapi import FastAPI, Request, File, UploadFile, Depends
from pydantic import BaseModel

app = FastAPI()

class Options(BaseModel):
    FileName: str
    FileDesc: str

#Accept request from the user and return a JSON payload as reponse  
@app.post("/acceptdata")
async def get_data(request: Request,options: Options):
    
    result = await request.json()
     
    return result

#Upload a file and return filename as reponse  
@app.post("/uploadfile")
async def create_upload_file(data: UploadFile = File(...)):
    
    print(data.filename)
    
    return {"Filename": data.filename}

#Accept request in form of data and file
@app.post("/uploadandacceptfile")
async def upload_accept_file(options: Options = Depends(),data: UploadFile = File(...)):
    
    data_options = options.dict()
    
    result = "Uploaded Filename: {}. JSON Payload: {}".format(data.filename,data_options)
    
    return result