
import torch
from transformers import AutoModelForCausalLM
from safetensors.torch import save_file

def slerp(a, x, y):
    x = x / torch.norm(x)
    y = y / torch.norm(y)
    dot = torch.sum(x * y)
    if dot > 0.999:
        return (1 - a) * x + a * y
    theta = torch.acos(dot)
    return (
        torch.sin((1 - a) * theta) / torch.sin(theta) * x +
        torch.sin(a * theta) / torch.sin(theta) * y
    )

def merge(m1, m2, alpha):
    out = {}
    for k in m1:
        out[k] = slerp(alpha, m1[k], m2[k]) if k in m2 and m1[k].shape == m2[k].shape else m1[k]
    return out

if __name__ == "__main__":
    m1 = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct", torch_dtype=torch.float16).state_dict()
    m2 = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-math-7b", torch_dtype=torch.float16).state_dict()
    save_file(merge(m1, m2, 0.55), "chimera-7b-reasoning.safetensors")
