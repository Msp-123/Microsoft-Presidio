#pip install presidio-analyzer presidio-anonymizer


from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import warnings
import logging

warnings.filterwarnings('ignore')
logging.getLogger("presidio-analyzer").setLevel(logging.ERROR)

text = "My name is John Doe, and I live in New York. I work at OpenAI as a research scientist. " \
       "You can contact me via email at john.doe@example.com or call me at 212-555-5555. " \
       "I was born on January 15, 1985, in Los Angeles, but I moved to New York in 2010."

# Set up the engine
analyzer = AnalyzerEngine()

# Analyze text for sensitive information
results = analyzer.analyze(text=text,
                           entities=["PHONE_NUMBER", "PERSON", "LOCATION", "EMAIL_ADDRESS"],
                           language='en')

# Initialize anonymizer
anonymizer = AnonymizerEngine()
anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

# Generate text with entity labels (e.g., John Doe<PERSON>)
text_with_labels = text
for res in sorted(results, key=lambda x: x.start, reverse=True):
    text_with_labels = (text_with_labels[:res.end] + f"<{res.entity_type}>" +
                        text_with_labels[res.end:])

# Print outputs
print("Detected Entities:", results)
print("Anonymized Text:", anonymized_text.text)
print("Text with Entity Labels:", text_with_labels)
print("Anonymized Items:", anonymized_text.items)
