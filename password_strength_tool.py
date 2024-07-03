import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_char_criteria": special_char_criteria,
        "strength": strength
    }

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess: ")
    
    assessment = assess_password_strength(password)
    
    print("\nPassword Strength Assessment:")
    print(f"Length criteria (>= 8 characters): {'✓' if assessment['length_criteria'] else '✗'}")
    print(f"Uppercase letter criteria: {'✓' if assessment['uppercase_criteria'] else '✗'}")
    print(f"Lowercase letter criteria: {'✓' if assessment['lowercase_criteria'] else '✗'}")
    print(f"Number criteria: {'✓' if assessment['number_criteria'] else '✗'}")
    print(f"Special character criteria (@$!%*?&#): {'✓' if assessment['special_char_criteria'] else '✗'}")
    print(f"Overall Strength: {assessment['strength']}")

if __name__ == "__main__":
    main()
