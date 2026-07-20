# 🎲 Probability Reference Guide

> 🟢 **Level:** Beginner  ·  **Prerequisites:** none

A quick, beginner-friendly reference for the probability ideas that show up most in data science and interviews — the **basic rules**, **conditional probability**, and **Bayes' rule** (the one interviewers love to sneak in).

> Interview tip: whenever a question asks for the probability of an event **"given that"** another event already happened, that's your cue to reach for **conditional probability / Bayes' rule**.

## 📚 Table of Contents

* [🧱 The Basics](#-the-basics)
* [➕ Combining Events](#-combining-events)
* [🔗 Conditional Probability](#-conditional-probability)
* [🔄 Bayes' Rule](#-bayes-rule)
* [🧩 Independence](#-independence)
* [🤖 Why It Matters for ML](#-why-it-matters-for-ml)
* [📚 Glossary](#-glossary)

---

## 🧱 The Basics

- A **probability** is a number between 0 and 1: `0` = impossible, `1` = certain.
- For equally likely outcomes: `P(event) = favorable outcomes / total outcomes`.
- The **complement**: `P(not A) = 1 − P(A)`.

Example: a fair die → `P(rolling a 4) = 1/6`; `P(not 4) = 5/6`.

---

## ➕ Combining Events

- **OR (union):** `P(A ∪ B) = P(A) + P(B) − P(A ∩ B)`  (subtract the overlap so it isn't double-counted).
- **AND (intersection), independent events:** `P(A ∩ B) = P(A) × P(B)`.
- **Mutually exclusive** events can't both happen, so `P(A ∩ B) = 0` and `P(A ∪ B) = P(A) + P(B)`.

---

## 🔗 Conditional Probability

We're often interested in the probability of **A given that B has occurred**, written `P(A | B)`:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Example: *What's the probability a patient has a disease, given that they tested positive?*

---

## 🔄 Bayes' Rule

Bayes' rule lets you "flip" a conditional probability — going from `P(B | A)` to `P(A | B)`:

$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

| Term        | Name        | Meaning                                     |
|-------------|-------------|---------------------------------------------|
| `P(A)`      | **Prior**   | Belief in A before seeing evidence B        |
| `P(B \| A)` | **Likelihood** | How likely B is if A is true             |
| `P(A \| B)` | **Posterior**  | Updated belief in A after observing B    |

> Pro Tip: If a problem gives you a "reverse" conditional (e.g., the test's accuracy `P(positive | disease)`) but asks for `P(disease | positive)`, that's Bayes' rule — almost always.

---

## 🧩 Independence

- **A and B are independent** if knowing B tells you nothing about A: `P(A | B) = P(A)`.
- **Conditional independence:** A and B can be independent *given* a third event C:
$$P(A \cap B \mid C) = P(A \mid C)\,P(B \mid C)$$
Given C has occurred, knowing B also occurred tells you nothing extra about A.

---

## 🤖 Why It Matters for ML

Bayes' rule is foundational in machine learning: the goal is frequently to identify the **best conditional distribution** for a variable given the available data (e.g., Naïve Bayes classifiers, Bayesian inference).

---

## 📚 Glossary

| Term          | Definition                                                    | When it matters               |
|---------------|--------------------------------------------------------------|-------------------------------|
| Conditional probability | Probability of A given B occurred                   | "Given that…" questions       |
| Prior         | Belief before seeing evidence                                | Bayesian updating             |
| Likelihood    | Probability of the evidence under a hypothesis               | Bayes' rule numerator         |
| Posterior     | Updated belief after evidence                                | The Bayes' rule answer        |
| Independence  | One event doesn't affect another's probability               | Simplifying joint probability |

---

🧠 **Pro Tips:**
* Watch for the phrase **"given that"** — it signals conditional probability.
* Draw a tree or a 2×2 table for tricky Bayes' problems; it prevents mix-ups.
* Remember the complement trick: `P(at least one) = 1 − P(none)`.

🔗 Helpful Links:
* https://www.khanacademy.org/math/statistics-probability/probability-library
* https://seeing-theory.brown.edu/
* https://en.wikipedia.org/wiki/Bayes%27_theorem
