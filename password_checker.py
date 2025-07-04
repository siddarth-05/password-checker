import re
import hashlib
import requests
#my other repo has this code - I refactored it but the logic is essentially the same
def password_strength(password: str) -> (bool, list):
    """Check password strength and return status and feedback."""
    feedback = []
    if len(password) < 14:
        feedback.append("Too short: use at least 14 characters.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        feedback.append("Add at least one digit.")
    if not re.search(r"[~!@#$%^&*()_+=;:,.?]", password):
        feedback.append("Add at least one special character.")
    return (len(feedback) == 0, feedback)

def check_pwned(password: str) -> str:
    """Check if the password has been exposed in data breaches."""
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    for line in response.text.splitlines():
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            return f" Password found in breaches {count} times. Consider changing it."
    return " Password not found in known breaches."

if __name__ == "__main__":
    password = input("Enter your password: ")
    strong, feedback = password_strength(password)
    if strong:
        print(" Strong password!")
    else:
        print(" Weak password:")
        for f in feedback:
            print(f"- {f}")
    print(check_pwned(password))

