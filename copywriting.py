from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

def generate_slogan(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=30, num_return_sequences=5, do_sample=True, temperature=0.7)

    slogans = []
    for output in outputs:
        slogan = tokenizer.decode(output, skip_special_tokens=True)
        slogans.append(slogan)

    return slogans

def generate_slogan_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r') as file:
        prompt = file.read()

    return generate_slogan(prompt)

#Direct input
prompt = "Create a catchy slogan for a pizza restaurant that promises the cheesiest experience."
slogans = generate_slogan(prompt)
for i, slogan in enumerate(slogans):
    print(f"Slogan {i+1}: {slogan}")

#From file
file_path = "prompt.txt"
slogans = generate_slogan_from_file(file_path)
for i, slogan in enumerate(slogans):
    print(f"Slogan {i+1}: {slogan}")