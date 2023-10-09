"""Generating image with Openai"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt="a black cat with deep blue eyes",
    n=1,
    size="1024x1024"

)
image_url = response['data'][0]['url']

print("Cat image url: ", image_url)
