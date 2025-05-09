from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse
import uvicorn
from docx_to_jats import convert_docx_to_jats

app = FastAPI()

@app.post("/convert", response_class=PlainTextResponse)
async def convert(file: UploadFile = File(...)):
    contents = await file.read()
    jats_xml = convert_docx_to_jats(contents)
    return jats_xml

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
