import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    number_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    criteria = [
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        number_criteria,
        special_criteria
    ]

    strength = sum(criteria)

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")

    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Medium",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }

    return strength_levels[strength], feedback

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        strength, feedback = check_password_strength(password)
        
        print(f"Password Strength: {strength}")
        for message in feedback:
            print(f"- {message}")

        again = input("Do you want to check another password? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
