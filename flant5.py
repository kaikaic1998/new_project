# from transformers import AutoModelForSeq2SeqLM
# from transformers import AutoTokenizer
# from transformers import GenerationConfig

# model_name='google/flan-t5-base'

# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base", device_map="auto")

input_text = "where is London?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))