from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import streamlit as st
import io

import os

from PIL import Image



#load env variables
load_dotenv()

my_api_key = os.getenv("GEMINI_API-KEY")

#initializing a client
client = genai.Client(api_key=my_api_key)

#note generator
def note_generator(images):

    if images:
        pil_images = []
        for img in images:
            pil_img=Image.open(img)
            pil_images.append(pil_img)

    prompt=""""Summarize the picture in note format at max 100 words,
    make sure to add necessary markdown to differentiate diferent section"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[pil_images,prompt]
    )

    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang='en',slow=False)  #lang='bn' fir bangla text
    audio_buffer=io.BytesIO()  #this saves in RAM
    speech.write_to_fp(audio_buffer)
    
    return audio_buffer


def quiz_generator(images,difficulty):

    prompt=f"generate 3 quizes based on the {difficulty}. Make sure to add marks"
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

