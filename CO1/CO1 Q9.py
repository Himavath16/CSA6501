from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

prompt = "Natural language processing is"
inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(**inputs, max_length=25)
print(tokenizer.decode(output[0], skip_special_tokens=True))
