import openai 

openai.api_key = "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"

prompt = "tell me about python"
model = "text-davinci-002"

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50
)

generated_text = response.choices[0].text
print(generated_text)
