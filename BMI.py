import streamlit as st

st.title('Welcome to BMI Calculator')

# Choix de l'unité de mesure pour la taille
status = st.radio("Select your height unit", ('cms', 'meters', 'feet'))

weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)

if status == 'cms':
    height = st.number_input('Enter your height (in centimeters)', min_value=0.0)
    bmi = weight / ((height / 100) ** 2) if height > 0 else 0
elif status == 'meters':
    height = st.number_input('Enter your height (in meters)', min_value=0.0)
    bmi = weight / (height ** 2) if height > 0 else 0
else:
    height = st.number_input('Enter your height (in feet)', min_value=0.0)
    bmi = weight / ((height / 3.28) ** 2) if height > 0 else 0
if st.button('Calculate BMI'):
    if bmi == 0:
        st.text("Please enter valid values for weight and height.")
    else:
        st.text(f"Your BMI Index is {bmi:.2f}.")

        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        elif bmi >= 30:
            st.error("Extremely Overweight")
