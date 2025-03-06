from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load the BioMedNLP-PubMedBERT model
MODEL_NAME = "michiyasunaga/BioLinkBERT-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)

# Create a Named Entity Recognition (NER) pipeline
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

def run_ner(text):
    """Runs PubMedBERT NER on input text and returns entities."""
    doc = nlp(text)
    return [{"text": ent["word"], "label": ent["entity"], "confidence": float(ent["score"])} for ent in doc]
