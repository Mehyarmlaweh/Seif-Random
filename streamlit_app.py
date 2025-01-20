import streamlit as st
import random

# Set up the Streamlit app
st.set_page_config(page_title="Random Number Generator", page_icon="🎲", layout="centered")

# Custom CSS for a fancy interface
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
    }
    .stMarkdown {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and description
st.title("🎲 Random Number Generator")
st.markdown("Generate random numbers between 1 and 443. You can choose how many numbers to generate and which numbers to exclude.")

# User inputs
col1, col2 = st.columns(2)

with col1:
    count = st.number_input("How many numbers do you want to generate?", min_value=1, max_value=443, value=10, step=1)

with col2:
    exclude_input = st.text_input("Enter numbers to exclude (separated by spaces):")

# Convert exclude input to a list of integers
exclude_list = []
if exclude_input:
    try:
        exclude_list = list(map(int, exclude_input.split()))
    except ValueError:
        st.error("Please enter valid numbers separated by spaces.")
        st.stop()

# Generate random numbers
if st.button("Generate Numbers"):
    try:
        # Generate a list of numbers from 1 to 443, excluding the numbers in exclude_list
        numbers = [num for num in range(1, 444) if num not in exclude_list]
        
        # Check if there are enough numbers to generate
        if count > len(numbers):
            st.error(f"Not enough numbers available after exclusions. Only {len(numbers)} numbers are available.")
        else:
            # Randomly sample 'count' numbers from the list
            random_numbers = random.sample(numbers, count)
            
            # Sort the numbers
            random_numbers.sort()
            
            # Display the result in a fancy box
            st.success("🎉 Here are your generated numbers:")
            st.write(
                f"""
                <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                    <h3 style="color: #333;">Generated Numbers:</h3>
                    <p style="font-size: 24px; color: #4CAF50;">{', '.join(map(str, random_numbers))}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
