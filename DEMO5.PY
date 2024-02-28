import openai 
openai.api_key = "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"
openai.Model.list()

openai.Image.create(
    prompt = "Create a dog with hat",
    n=2,
    size ="512x512"
)
