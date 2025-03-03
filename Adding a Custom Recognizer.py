from presidio_analyzer import Pattern, PatternRecognizer

# Define a custom recognizer for detecting Employee IDs
employee_id_recognizer = PatternRecognizer(supported_entity="EMPLOYEE_ID",
                                           patterns=[Pattern("\bEMP[0-9]{4}\b", score=0.9)])

# Add the custom recognizer to the analyzer
analyzer.registry.add_recognizer(employee_id_recognizer)
