def classify_document(text):
    """
    Classifies the document based on its content (not just the heading).
    """
    text = text.lower()

    # Check for specific keywords or patterns in the entire text
    if 'pay stub' in text or 'wages' in text or 'salary' in text:
        return 'Pay Stub'
    elif 'passport' in text or 'identity' in text or 'national id' in text:
        return 'Identity Document'
    elif 'application' in text or 'form' in text or 'submission' in text:
        return 'Application'
    elif 'invoice' in text or 'receipt' in text or 'total due' in text:
        return 'Invoice/Receipt'
    else:
        return 'Unrecognized Document'  # Default category for unrecognized documents

