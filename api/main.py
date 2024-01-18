from fastapi import FastAPI
import uvicorn
import File, UploadFile

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello I am alive"

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    img = read_file_as_image(await file.read())
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

