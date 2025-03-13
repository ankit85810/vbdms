from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import voice_assistent
import speech_recognition as sr
import tempfile
import os

app = FastAPI()

class CommandRequest(BaseModel):
    command: str

@app.post("/transcribe_audio/")
async def transcribe_audio(audio_file: UploadFile = File(...)):
    """
    Endpoint to transcribe audio file to text
    """
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            # Read content from uploaded file and write to temp file
            content = await audio_file.read()
            temp_audio.write(content)
            temp_path = temp_audio.name
        
        # Use speech recognition to transcribe
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        
        # Clean up temp file
        os.unlink(temp_path)
        
        return {"text": text}
    
    except sr.UnknownValueError:
        return JSONResponse(status_code=400, content={"error": "Could not understand audio"})
    except sr.RequestError as e:
        return JSONResponse(status_code=500, content={"error": f"Could not request results; {str(e)}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/process_voice_command/")
async def process_voice_command(request: CommandRequest):
    """
    Endpoint to process voice commands
    """
    try:
        response = voice_assistent.process_command(request.command)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))