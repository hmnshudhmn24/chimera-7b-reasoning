from transformers import AutoTokenizer
AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B-Instruct').save_pretrained('tokenizer')
