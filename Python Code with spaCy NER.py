#pip install spacy
#python -m spacy download en_core_web_sm

from presidio_analyzer.nlp_engine import SpacyNlpEngine
from presidio_analyzer import AnalyzerEngine

# Set up spaCy NLP engine
nlp_engine = SpacyNlpEngine(models={'en': 'en_core_web_sm'})
analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["en"])

# Analyze text with spaCy-based Presidio
results = analyzer.analyze(text=text, language='en')

print("Detected Entities:", results)
