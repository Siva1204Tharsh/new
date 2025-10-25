from transformers import AutoModelForSequenceClassification, AutoTokenizer
import joblib
import os

# Hugging Face model name
model_name = "ealvaradob/bert-finetuned-phishing"

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Make directory if not exists
save_dir = "backend/models"
os.makedirs(save_dir, exist_ok=True)

# Save both model and tokenizer as a .pkl
joblib.dump((tokenizer, model), os.path.join(save_dir, "phishing_model.pkl"))
