import os
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image  
import PIL 

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


# image_url = response.data[0].url
# image gen package with DALL-E Python API
# text to image URL for a segment
def generate_image(text):
    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image = response.data[0]
    path = f"/images/{image.url}.jpg"
    image = image.save(path)
    return path


