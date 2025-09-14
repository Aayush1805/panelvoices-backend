from fastapi import APIRouter, HTTPException
from configurations import collection
from database.models import VoiceCreate, VoiceResponse

router = APIRouter(prefix="/voice", tags=["Voice"])


@router.post("/", response_model=VoiceResponse)
async def add_voice(voice: VoiceCreate):
    data = {"language": voice.language.lower(), "audio_url": voice.audio_url}
    collection.insert_one(data)
    return VoiceResponse(**data)

@router.get("/{language}", response_model=VoiceResponse)
async def get_voice(language: str):
    voice = collection.find_one({"language": language.lower()})
    if not voice:
        raise HTTPException(status_code=404, detail="Language not found")
    return VoiceResponse(language=voice["language"], audio_url=voice["audio_url"])