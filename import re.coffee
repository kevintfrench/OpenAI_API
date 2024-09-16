import re

def extract_email_or_phone(text):
    # Regex pattern for email extraction
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Regex pattern for phone number extraction (matches a 10-digit phone number)
    phone_pattern = r'(\d{3})(\d{3})(\d{4})'
    
    # Try to find an email first
    email_match = re.search(email_pattern, text)
    if email_match:
        return f"Email found: {email_match.group(0)}"
    
    # If no email, try to find a phone number
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        # Format the phone number as 603*475*7681
        formatted_phone = f"{phone_match.group(1)}*{phone_match.group(2)}*{phone_match.group(3)}"
        return f"Phone number found: {formatted_phone}"
    
    return "No email or phone number found."

# Example usage:
text = '''6034757681@vtext.com'''
result = extract_email_or_phone(text)
print(result)