import re

input_string = input("Say some thing to your friend: ")

def extract_phone_number(input_string):
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    match = re.search(phone_pattern, input_string)
    
    if match:
        return match.group()
    else:
        return None

output = extract_phone_number(input_string)
print(f"🗣️ Remember that {output} is my personal phone number.") 