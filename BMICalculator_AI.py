import streamlit as st
import google.genai as genai

google_api_key = st.secrets["google"]["api_key"]

client = genai.Client(api_key=google_api_key)


st.title("BMI Calculator with AI Insights")


height = st.slider(
    "Select your height (meters):",
    min_value=1.0,
    max_value=2.5,
    value=1.75,
    step=0.01
)

weight = st.slider(
    "Select your weight (kgs):",
    min_value=30,
    max_value=200,
    value=70,
    step=1
)

gender = st.selectbox(   "Select your gender:",    ["Male", "Female", "Prefer not to say"]
)

 


bmi = weight / (height ** 2)


st.write(f"Your BMI is: {bmi:.2f}")


prompt = (
    f"With this BMI {bmi:.2f}, please share some health insights "
    f"for a {gender} person with weight {weight} kgs "
    f"and height {height} metres."
)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# Display AI insights
st.write(response.text)
