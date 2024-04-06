import aiohttp
import asyncio
import nest_asyncio  # For handling event loop in Jupyter notebook
import base64
import asyncio
import os




async def generate_caption(image_path, endpoint_url="http://35.233.231.20:5003/api/generate"):
  """
  Generates a caption for an image using the LLaVa endpoint.

  Args:
      image_path (str): Path to the image file on your local machine.
      endpoint_url (str, optional): URL of the LLaVa endpoint. Defaults to "http://35.233.231.20:5003/api/generate".

  Returns:
      str: The generated caption for the image, or None if error occurs.
  """
  try:
    # Read image file and encode in base64
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    image_encoded = base64.b64encode(image_bytes).decode("utf-8")

    # Prepare data for LLaVa endpoint
    data = {
        "model": "llava:34b-v1.6",
        "prompt": "What is in this picture?",
        "stream": False,
        "images": [image_encoded]
    }

    # Send request and get response
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint_url, json=data) as response:
            if response.status == 200:
                response_json = await response.json()
                return response_json[0]["generated_text"]
            else:
                print(f"Error: {response.status} - {await response.text()}")
                return None
  except Exception as e:
      print(f"An error occurred: {e}")
      return None


# Run asynchronously within Jupyter notebook (assuming IPython > 7 and IPykernel > 5)
image_folder = "C:\\Users\\KIIT\\Desktop"

if __name__ == "__main__":
  image_filename = "damian-trevor-beautiful-green-nature-mountain-lake-landscape-photography-damian-trevor.jpg"
  image_path = os.path.join(image_folder, image_filename)  # Import os module
asyncio.run(generate_caption(image_path))
