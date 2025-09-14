from pydantic import BaseModel

class VoiceCreate(BaseModel):
    language: str
    audio_url: str

class VoiceResponse(BaseModel):
    language: str
    audio_url: str
