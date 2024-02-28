import openai 

openai.api_key = "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"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']