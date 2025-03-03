#pip install transformers torch presidio-analyzer presidio-anonymizer

from transformers import pipeline
from presidio_analyzer import AnalyzerEngine, RecognizerResult, EntityRecognizer

# Load a pre-trained BERT NER model from Hugging Face
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")

def custom_ner_recognizer(text):
    entities = []
    for entity in ner_pipeline(text):
        entities.append(
            RecognizerResult(entity_type=entity["entity_group"],
                             start=entity["start"],
                             end=entity["end"],
                             score=entity["score"])
        )
    return entities

# Initialize Presidio Analyzer
analyzer = AnalyzerEngine()

# Custom NER-based entity detection
text = "My name is Alice Johnson, and I live in San Francisco. My email is alice.j@example.com."
results = custom_ner_recognizer(text)

print("Detected Entities:", results)
