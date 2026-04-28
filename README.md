# AI IT Helpdesk Chatbot

A simple machine learning based IT helpdesk chatbot built with Python and Streamlit.

The chatbot:
- Trains an intent classification model using `TF-IDF + LogisticRegression`
- Predicts user intent from chat messages
- Returns predefined IT support responses in a chat-style web UI

## Project Structure

```text
ai-it-helpdesk-chatbot/
|- app/
|  `- app.py
|- data/
|  `- intents.csv
|- model/
|  `- chatbot_model.pkl (generated after training)
|- report/
|- train_model.py
|- requirements.txt
`- README.md
```

## Prerequisites

- Python 3.10+ recommended
- `pip`

## Setup

### 1) Clone the repository

```bash
git clone https://github.com/TahaGabu/ai-it-helpdesk-chatbot.git
cd ai-it-helpdesk-chatbot
```

### 2) Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

Before running the app, train the chatbot model:

```bash
python train_model.py
```

This creates:

- `model/chatbot_model.pkl`

## Run the Streamlit App

```bash
streamlit run app/app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Screenshot

Main UI:

![IT Helpdesk Chatbot UI](assets/first%20screen.png)

## How It Works

1. Training data is loaded from `data/intents.csv`
2. `train_model.py` trains and evaluates a text classification pipeline
3. The trained model is saved with `joblib`
4. `app/app.py` loads the model and serves a chat interface with Streamlit

## Notes

- If `model/chatbot_model.pkl` does not exist, run `python train_model.py` first.
- Low-confidence predictions return a fallback response: `"Sorry, I didn't understand that."`
