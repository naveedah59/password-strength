import streamlit as st
import string

def check_password_strength(password):
    length_score = len(password) >= 8
    upper_score = any(char.isupper() for char in password)
    lower_score = any(char.islower() for char in password)
    digit_score = any(char.isdigit() for char in password)
    special_score = any(char in string.punctuation for char in password)

    score = sum([length_score, upper_score, lower_score, digit_score, special_score])

    if score == 5:
        return "Strong", "🟢 Your password is strong!"
    elif score >= 3:
        return "Moderate", "🟡 Your password is okay, but could be stronger."
    else:
        return "Weak", "🔴 Your password is weak. Try making it longer and include different character types."

# Streamlit App
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    level, message = check_password_strength(password)
    st.subheader(f"Strength: {level}")
    st.info(message)
