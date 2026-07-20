# 🧠 Deep Learning & Modern AI Intro Reference Guide

> 🟡 **Level:** Intermediate  ·  **Prerequisites:** [ML Fundamentals](ml_fundamentals_ref.md), [ML Algorithms](ml_algorithms_ref.md)  ·  **Related:** [ML Model Evaluation](ml_model_evaluation_ref.md) · [ML Data Prep](ml_data_prep_ref.md)

A gentle, conceptual introduction to **deep learning**, **neural networks**, and the **transformers / large language models (LLMs)** behind modern AI. This is a map of the landscape for analysts and entry-level data scientists — *what the ideas are and when to use them*, not a math-heavy course.

> Deep learning is a *subset* of machine learning. Everything in [ML Fundamentals](ml_fundamentals_ref.md) still applies — training data, overfitting, evaluation — just with much more flexible models.

## 📚 Table of Contents

* [🌐 Where Deep Learning Fits](#-where-deep-learning-fits)
* [🕸️ Neural Networks in Plain Terms](#-neural-networks-in-plain-terms)
* [🏋️ How They Learn](#-how-they-learn)
* [🧩 Common Architectures](#-common-architectures)
* [🤖 Transformers & LLMs](#-transformers--llms)
* [🛠️ The Ecosystem](#-the-ecosystem)
* [⚖️ When to Use (and Not Use)](#-when-to-use-and-not-use)
* [📚 Glossary](#-glossary)

---

## 🌐 Where Deep Learning Fits

- **Artificial Intelligence** → the broad goal of machines doing "smart" things.
- **Machine Learning** → systems that learn patterns from data (linear/logistic regression, trees, KNN…).
- **Deep Learning** → ML using **neural networks with many layers**; excels at unstructured data (images, text, audio).

> Note: For **tabular** business data, classic models (Random Forest, gradient boosting) often match or beat deep learning with far less data and compute. Deep learning shines on **images, text, and audio**.

---

## 🕸️ Neural Networks in Plain Terms

A **neural network** is layers of simple units ("neurons") connected by **weights**:

- **Input layer** — your features.
- **Hidden layers** — each neuron computes a weighted sum, then applies a non-linear **activation function** (e.g., ReLU). Stacking these lets the network learn complex patterns.
- **Output layer** — the prediction (a class probability, a number).
- **Deep** simply means "many hidden layers."

The **weights** are the parameters the network *learns* — millions or billions of them in large models.

---

## 🏋️ How They Learn

Training is an iterative loop:

1. **Forward pass** — run inputs through the network to get a prediction.
2. **Loss function** — measure how wrong the prediction is.
3. **Backpropagation** — compute how each weight contributed to the error.
4. **Gradient descent** — nudge every weight to reduce the loss; repeat over many **epochs**.

Key knobs: **learning rate** (step size), **batch size**, **epochs**, and regularization like **dropout** to fight overfitting.

> Pro Tip: The same overfitting/underfitting and train-test discipline from [ML Fundamentals](ml_fundamentals_ref.md) applies — deep models overfit *easily*, so watch that validation curve.

---

## 🧩 Common Architectures

| Architecture | Best for | Idea |
|--------------|----------|------|
| **Feedforward (MLP)** | Tabular / general | Fully connected layers |
| **CNN** (Convolutional) | Images | Learns spatial features (edges → shapes → objects) |
| **RNN / LSTM** | Sequences (older) | Processes data step by step with memory |
| **Transformer** | Text, and now almost everything | Attention over the whole sequence at once |

---

## 🤖 Transformers & LLMs

The **transformer** (2017) is the architecture behind modern AI. Its key idea is **attention** — each element of the input can "look at" every other element to decide what matters, in parallel.

**Large Language Models (LLMs)** like the Claude, GPT, and Gemini families are giant transformers trained to predict the next **token** (a word-piece) on enormous text corpora:

- **Pre-training** — learn general language patterns from vast text.
- **Fine-tuning / alignment** — specialize and make the model helpful and safe.
- **Prompting** — you steer a pre-trained model with instructions instead of retraining it.
- **Embeddings** — models turn text into vectors, powering **semantic search** and **RAG** (Retrieval-Augmented Generation).

> Note: As an analyst you'll usually **consume** LLMs via an API (e.g., for classification, summarization, extraction) rather than train one. Knowing the vocabulary — tokens, context window, embeddings, RAG, fine-tuning — is what matters most.

---

## 🛠️ The Ecosystem

- **Frameworks:** **PyTorch** (research default) and **TensorFlow/Keras** (production-friendly). See the Keras and TensorFlow cheat sheets in `Machine_Learning/cheat-sheets/`.
- **Pre-trained models:** **Hugging Face** hosts thousands you can use off the shelf.
- **Transfer learning** — start from a pre-trained model and adapt it to your task with far less data (see [ML Fundamentals](ml_fundamentals_ref.md)).
- **Hardware:** GPUs/TPUs accelerate training; cloud notebooks (Colab) give free GPU access.

---

## ⚖️ When to Use (and Not Use)

**Reach for deep learning when:**
- Data is **unstructured** (images, text, audio).
- You have **lots** of it (typically tens of thousands+ of examples).
- The pattern is too complex for classic models.

**Prefer classic ML when:**
- Data is **tabular** and modest in size.
- You need **interpretability** for stakeholders.
- Compute, time, or labeled data is limited.

> Pro Tip: Start simple. A logistic regression or gradient-boosted tree baseline tells you whether deep learning's extra cost is even worth it.

---

## 📚 Glossary

| Term | Definition | When it matters |
|------|------------|-----------------|
| Neural network | Layers of weighted units with activations | The core deep-learning model |
| Weight / parameter | A learned value in the network | What training adjusts |
| Backpropagation | Assigns error blame to weights | How networks learn |
| Epoch | One pass over the training data | Training loop |
| CNN / RNN / Transformer | Architectures for images / sequences / text | Choosing a model |
| Token | A word-piece an LLM processes | LLM inputs/outputs |
| Embedding | Text/data as a vector | Semantic search, RAG |
| Transfer learning | Reusing a pre-trained model | Small-data tasks |

---

🧠 **Pro Tips:**
* Deep learning is ML with flexible models — the **data discipline doesn't change**.
* For **tabular** data, try gradient boosting before neural nets.
* You'll mostly **use** pre-trained models and LLM APIs — learn the vocabulary before the math.

🔗 Helpful Links:
* https://www.deeplearning.ai/
* https://huggingface.co/learn
* https://pytorch.org/tutorials/
