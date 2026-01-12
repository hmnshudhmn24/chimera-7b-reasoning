
# chimera-7b-reasoning

A SLERP-based merge of **Llama-3 Chat** and **DeepSeek-Math**, built to deliver strong logical and mathematical reasoning while maintaining natural conversational fluency.

---

## ✨ Overview

**chimera-7b-reasoning** combines the strengths of:
- a chat-optimized LLM (instruction following, fluency)
- a math-specialized LLM (reasoning, accuracy)

The merge uses **SLERP (Spherical Linear Interpolation)** instead of naive averaging to preserve useful weight directions and avoid performance collapse.

---

## 🚀 Features

- Strong logical & mathematical reasoning
- Improved GSM8K-style performance
- Retains chat and instruction-following ability
- SLERP-based model merging
- Fully reproducible research pipeline
- Hugging Face–compatible outputs

---

## 📁 Project Structure

```
chimera-7b-reasoning/
├── merge/
│   ├── merge_config.yaml
│   └── slerp_merge.py
├── tokenizer/
│   └── export_tokenizer.py
├── eval/
│   └── eval_gsm8k.py
├── inference/
│   └── inference.py
├── requirements.txt
├── .gitattributes
├── LICENSE
└── README.md
```

---

## 🛠️ Requirements

- Python 3.9+
- CUDA-enabled GPU (recommended)
- Access to base models:
  - meta-llama/Meta-Llama-3-8B-Instruct
  - deepseek-ai/deepseek-math-7b

```bash
pip install -r requirements.txt
```

---

## 🔀 Model Merge (SLERP)

```bash
python merge/slerp_merge.py
```

---

## 🔤 Tokenizer Export

```bash
python tokenizer/export_tokenizer.py
```

---

## 📊 Evaluation (GSM8K)

```bash
python eval/eval_gsm8k.py
```

---

## 🧪 Inference Example

```bash
python inference/inference.py
```

---

## ⚠️ Notes

- Code-only repository
- Upload weights to Hugging Face, not GitHub
- Use Git LFS for large files

---

## 📜 License

Apache License 2.0
