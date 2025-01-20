import streamlit as st
import google.generativeai as genai
import random

# Make sure your Google API key is set
api_key = "AIzaSyC6ZfkRE2ddXj9DcxDKYVGrygeOwQrFFSc"  # Replace this with your actual API key
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not set. Please configure your Google API key.")

# Create the model using Gemini 1.5 Flash
model = genai.GenerativeModel("gemini-1.5-flash")

# List of symbols and emojis for random selection based on the topic
symbols = ["🌱", "🌾", "🌿", "🍅", "🥕", "🍆", "🍓", "🌻", "🍃", "🌞", "🌍", "🍏"]

def generate_farming_info(input_text):
    """Function to call the Gemini API and get the generated organic farming content."""
    try:
        # Prepare the prompt to generate content related to organic farming
        prompt = f"Provide educational information and guidelines on organic farming related to: '{input_text}'. Include best practices for sustainable farming, eco-friendly fertilizers, and certification procedures. Ensure the content is engaging and informative."

        # Generate content using the model
        response = model.generate_content(prompt)
        generated_text = response.text.strip()

        # Randomly select symbols for content formatting
        random_symbol_title = random.choice(symbols)
        random_symbol_content = random.choice(symbols)

        # Add symbols to content dynamically
        fancy_title = f"{random_symbol_title} **Organic Farming: {input_text.upper()}** {random_symbol_title}"
        fancy_content = f"{random_symbol_content} {generated_text} {random_symbol_content}"

        # Return the formatted content with relevant hashtags
        return f"""
        <div style="padding: 10px; border-radius: 10px; border: 2px solid #4CAF50; background-color: black;">
            <h3 style="color: #2d6a4f; font-family: 'Arial', sans-serif; font-weight: bold; font-size: 20px; text-align: center;">
                {fancy_title}
            </h3>
            <p style="font-size: 16px; line-height: 1.6; color: #333; font-family: 'Arial', sans-serif; text-align: justify;">
                {fancy_content}
            </p>
            <p style="text-align: center; font-size: 14px; color: #333;">
                 <span style="color: #4CAF50;">#OrganicFarming #SustainableAgriculture #EcoFriendly #FarmersEducation</span>
            </p>
        </div>
        """
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Streamlit UI
st.title('Organic Farming Chatbot - Educate and Empower Farmers')

st.write(
    "Welcome to the Organic Farming Chatbot! Ask anything about organic farming practices, natural fertilizers, and certification processes, and get informative answers."
)

# Input field for the topic
input_statement = st.text_area("Enter your organic farming topic", "", key="input")

# Button to generate content
if st.button('Generate Information'):
    if input_statement:
        with st.spinner("Thinking..."):
            response = generate_farming_info(input_statement)

        # Display formatted content
        st.markdown(response, unsafe_allow_html=True)

    else:
        st.warning("Please enter a topic.")
