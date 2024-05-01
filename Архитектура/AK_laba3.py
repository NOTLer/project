import re


def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# Пример использования:
text = "bca Пример текста с email адресами example@mail.com и another.email@example.com"

re.sub(r'^bca', 'cba', text)

print(text)
1