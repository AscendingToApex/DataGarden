# 🤖 Machine Learning Fundamentals Reference Guide

**Machine Learning (ML)** is the science of programming computers so they can **learn from data** without being explicitly programmed. This guide covers *what ML is good for*, the **types of ML systems**, the **main challenges** (bad data and bad models), **testing/validation**, and the **vocabulary** you'll see everywhere.

> New to ML? Start here, then move to the [project workflow](ml_project_workflow_ref.md), [algorithms](ml_algorithms_ref.md), and [evaluation](ml_model_evaluation_ref.md) guides.

## 📚 Table of Contents

* [🌟 What ML Is Great For](#-what-ml-is-great-for)
* [🎯 Classification vs. Regression](#-classification-vs-regression)
* [🧭 Types of ML Systems](#-types-of-ml-systems)
* [👨‍🏫 Training Supervision](#-training-supervision)
* [⏱️ Batch vs. Online Learning](#-batch-vs-online-learning)
* [🧠 Instance- vs. Model-Based](#-instance--vs-model-based)
* [⚠️ Main Challenges: Bad Data](#-main-challenges-bad-data)
* [⚠️ Main Challenges: Bad Models](#-main-challenges-bad-models)
* [🧪 Testing & Validating](#-testing--validating)
* [📖 Terminology](#-terminology)
* [📚 Glossary](#-glossary)

---

## 🌟 What ML Is Great For

- Problems that would need **long lists of rules** — ML can simplify the code and perform better.
- **Complex problems** with no good traditional solution (e.g., speech recognition).
- **Fluctuating environments** — retrain on new data to stay current.
- **Learning from data** — surfacing insights from large datasets (**data mining**).

---

## 🎯 Classification vs. Regression

| Prediction type | Predicts…                      | Example                     |
|-----------------|--------------------------------|-----------------------------|
| **Classification** | A discrete class **label**  | Spam / not spam             |
| **Regression**  | A continuous **target** value  | House price                 |

---

## 🧭 Types of ML Systems

ML systems are classified along three axes:

1. **How they're supervised** — supervised, unsupervised, semi-supervised, self-supervised.
2. **Whether they learn incrementally** — online vs. batch.
3. **How they generalize** — instance-based vs. model-based.

---

## 👨‍🏫 Training Supervision

### Supervised learning
The training set includes the **desired answers** (labels/targets).
- **Classification** — predict a class label.
- **Regression** — predict a numeric target.

### Unsupervised learning
The training set is **unlabeled**; the system finds structure on its own.
- **Dimensionality reduction** — simplify data while keeping information (feature extraction).
- **Anomaly detection** — flag outliers.
- **Novelty detection** — spot instances unlike anything seen in (clean) training data.
- **Association rule learning** — discover relationships (e.g., items bought together).

### Other types
- **Semi-supervised** — a mix of labeled and unlabeled data (labeling is costly).
- **Self-supervised** — generate a fully labeled dataset from an unlabeled one.
- **Reinforcement learning** — an **agent** observes an environment, takes actions, and learns a **policy** to maximize **rewards** over time.

---

## ⏱️ Batch vs. Online Learning

- **Batch (offline)** — trained on *all* the data at once; to learn new data you retrain from scratch. Time- and compute-heavy.
- **Online** — trained incrementally on data instances or small **mini-batches**; fast, cheap, adapts on the fly.
  - The **learning rate** controls how fast it adapts: high = adapts fast but forgets old data; low = slower but steadier and less noise-sensitive.
  - **Out-of-core learning** trains on datasets too big for memory.

> Note: Bad data can degrade an online model quickly — keep a way to switch it off and revert to a previous version.

---

## 🧠 Instance- vs. Model-Based

- **Instance-based** — memorize examples, then generalize by a **similarity measure** (like grading with a past student's answer key).
- **Model-based** — learn the underlying **patterns**, build a model, and use it to **predict** (like a teacher who understands the concepts).

---

## ⚠️ Main Challenges: Bad Data

*Always check for these first:*

- **Insufficient quantity** of training data.
- **Nonrepresentative data** — small samples cause **sampling noise**; flawed sampling causes **sampling bias**.
- **Poor-quality data** — outliers and missing values you must clean, discard, or impute.
- **Irrelevant features** — "garbage in, garbage out." Fix with **feature engineering**:
  - **Feature selection** — keep the most useful existing features.
  - **Feature extraction** — combine features into more useful ones.

---

## ⚠️ Main Challenges: Bad Models

### Overfitting
The model does great on training data but **fails to generalize**. Happens when the model is too complex, data is too small, or data is too noisy.
- **Fixes:** simplify the model, add **regularization**, gather more data, reduce noise.

### Underfitting
The model is **too simple** to capture the data's patterns.
- **Fixes:** use a more powerful model, engineer better features, loosen constraints.

> Pro Tip: The art of ML is balancing these two — a model complex enough to learn the signal, but simple enough to generalize.

---

## 🧪 Testing & Validating

- Split data into a **training set** (~80%) and a **test set** (~20%).
- **Generalization error** = the error rate on new (test) cases.
- Low training error + high generalization error = **overfitting**.
- **Holdout validation** — carve a **validation set** out of training data to compare models *without* touching the test set (reusing the test set "fits" your choices to it).
- **Cross-validation** — rotate the validation split to avoid a validation set that's too big or too small.

---

## 📖 Terminology

| Term            | Meaning                                                        |
|-----------------|---------------------------------------------------------------|
| Label / Target  | What you predict (label = classification, target = regression)|
| Feature         | Input variable (a.k.a. predictor / attribute)                 |
| Training set    | Examples the model learns from                                |
| Model           | The part that learns and predicts                             |
| Training        | Finding the parameters that best fit the data                 |
| Inference       | Using a trained model to predict new cases                    |
| Feature engineering | Crafting good features (selection + extraction)           |
| Regularization  | Constraining a model to reduce overfitting                    |
| Transfer learning | Reusing knowledge from one task on another                  |
| Cost function   | Measures how *bad* a model is (utility measures how good)     |

---

## 📚 Glossary

| Term          | Definition                                                    | When it matters                |
|---------------|---------------------------------------------------------------|--------------------------------|
| Supervised    | Learns from labeled data                                      | Most predictive tasks          |
| Unsupervised  | Finds structure in unlabeled data                            | Clustering, dim. reduction     |
| Overfitting   | Great on training, poor on new data                          | Model too complex              |
| Underfitting  | Poor on training and new data                                | Model too simple               |
| Generalization| How well a model handles unseen data                         | The whole point of ML          |
| Feature engineering | Selecting/creating input features                       | Model quality                  |

---

🧠 **Pro Tips:**
* Before modeling, **audit your data** — most ML failures are data problems, not algorithm problems.
* Never tune on the **test set**; use validation/cross-validation.
* Watch the train-vs-test gap to diagnose overfitting vs. underfitting.

🔗 Helpful Links:
* https://scikit-learn.org/stable/tutorial/
* https://developers.google.com/machine-learning/crash-course
* https://scikit-learn.org/stable/machine_learning_map.html
