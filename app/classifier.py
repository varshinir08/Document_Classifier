def classify_document(text):
    if 'pay stub' in text.lower():
        return 'Pay Stub'
    elif 'passport' in text.lower():
        return 'Identity Document'
    elif 'application' in text.lower():
        return 'Application'
    else:
        return 'Other'
