import tkinter as tk
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

model = TFGPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_text():
    category='inspiration'
    author='Mark Twain'
    prompt = f"Generate a {category} quote by {author}:"
    input_ids = tokenizer.encode(prompt, return_tensors="tf")

    # Generate text using the GPT-2 model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    result_text.config(text=generated_text)

# Tkinter GUI setup
root = tk.Tk()
root.title("Generative AI Example")

generate_button = tk.Button(root, text="Generate Text", command=generate_text)
generate_button.pack(pady=10)

result_text = tk.Label(root, text="", wraplength=400)
result_text.pack(pady=10)

root.mainloop()
