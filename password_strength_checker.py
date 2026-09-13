import re

print("🔐 Password Strength Checker")
print("-" * 30)

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase
if re.search(r"[A-Z]", password):
    score += 1

# Check lowercase
if re.search(r"[a-z]", password):
    score += 1

# Check number
if re.search(r"[0-9]", password):
    score += 1

# Check special character
if re.search(r"[^A-Za-z0-9]", password):
    score += 1

# Display result
if score <= 2:
    strength = "Weak ❌"
elif score <= 4:
    strength = "Medium ⚠️"
else:
    strength = "Strong ✅"

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")
