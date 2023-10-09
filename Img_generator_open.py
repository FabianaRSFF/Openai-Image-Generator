"""Generating image with Openai"""

import os
import openai


def get_cat_image_url():
    # Get your API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Use the OpenAI API to generate the image URL
    response = openai.Image.create(
       prompt="a white siamese cat",
       n=1,
       size="1024x1024"
    )
    image_url = response['data'][0]['url']

    # Return the image URL
    return image_url


# Call the function to get the cat image URL
cat_image_url = get_cat_image_url()

# Print or use the cat image URL as needed
print("Cat Image URL:", cat_image_url)
