from google import genai
from dotenv import load_dotenv
import os, io
from PIL import Image
from gtts import gTTS

# loading the environment variable
load_dotenv()

my_api_key = os.getenv("Ab8RN6IYtY3D81fNZ4nH6BVZryTu959VO_ADSo2By6VHsSoxgw")

# initializing a client
client = genai.Client(api_key=my_api_key)

# note generator
def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words, make sure to add necessary markdown to differentiate different section"""

    pil_images = []
    for img in images:
        pil_images.append(Image.open(img))
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt]
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generator(images, difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer. After the quiz"

    pil_images = []
    for img in images:
        pil_images.append(Image.open(img))
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images, prompt]
    )

    return response.text