import torch
import transformers

from transformers import LlamaForCausalLM, LlamaTokenizer

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
device = "cuda:0"

model_dir = "./llama-2-7b-chat-hf"
model = LlamaForCausalLM.from_pretrained(model_dir, device_map = 'cuda')
# model = LlamaForCausalLM.from_pretrained(model_dir)

tokenizer = LlamaTokenizer.from_pretrained(model_dir)

pipeline = transformers.pipeline(
    "text-generation",

    model=model,

    tokenizer=tokenizer,

    torch_dtype=torch.int8,
    # torch_dtype=torch.bfloat16,

    device_map = 'cuda',
)

sequences = pipeline(
    'What is 10x23 equal to?\n',

    do_sample=True,

    top_k=5,

    num_return_sequences=1,

    eos_token_id=tokenizer.eos_token_id,

    max_length=400,
)

for seq in sequences:
    print(f"{seq['generated_text']}")

