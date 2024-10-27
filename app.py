import streamlit as st
from datetime import datetime
import base64

# Function to add a background image using CSS
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()  # Encode image to base64
    # Inject the custom CSS into the Streamlit app
    bg_image_css = f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{encoded_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .sign-in-text {{
        font-family: 'Georgia', serif;
        font-size: 24px;
        color: #3e2c1b; /* Deep brown to match the background */
        text-shadow: 1px 1px 2px #d4a76a; /* Soft gold shadow to highlight the text */
        margin-bottom: 20px;
    }}
    .stButton>button {{
        background-color: #d4a76a; /* Warm gold for buttons */
        color: white;
        border-radius: 8px;
        border: none;
        font-family: 'Georgia', serif;
        font-size: 18px;
        padding: 8px 16px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Add depth to buttons */
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #b3874d; /* Darker shade of the button on hover */
        box-shadow: 3px 3px 7px rgba(0, 0, 0, 0.5); /* Add hover effect */
    }}
    input {{
        font-family: 'Garamond', serif;
        font-size: 18px;
        color: #3e2c1b; /* Match input text to the page theme */
        background-color: #f5e3c8; /* Light beige input box color */
        border: 1px solid #d4a76a; /* Matching border */
        border-radius: 5px;
        padding: 8px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }}
    </style>
    """
    st.markdown(bg_image_css, unsafe_allow_html=True)

# Sign In Page
def sign_in(username, password):
    if username == "user" and password == "password":
        st.session_state['signed_in'] = True
        st.session_state['current_page'] = "Home"
        st.success("Sign in successful! Redirecting to Home...")
        return True
    else:
        st.error("Invalid username or password")
        return False


# Raga Recommendation based on Time of Day and associated audio file
def get_raga_recommendation_and_audio():
    current_time = datetime.now().time()

    if current_time.hour < 6:
        return "Morning Raga: Bhairav, Todi", "audio/morning.mp3", "Morning"
    elif 6 <= current_time.hour < 12:
        return "Forenoon Raga: Ahir Bhairav, Deshkar", "audio/forenoon.mp3", "Forenoon"
    elif 12 <= current_time.hour < 16:
        return "Afternoon Raga: Bhimpalasi, Madhuvanti", "audio/afternoon.mp3", "Afternoon"
    elif 16 <= current_time.hour < 20:
        return "Evening Raga: Yaman, Marwa", "audio/evening.mp3", "Evening"
    else:
        return "Night Raga: Darbari Kanada, Malkauns", "audio/night.mp3", "Night"

# Sign In Page
def sign_in_page():
    st.title("Sign In to Aurora")
    add_bg_from_local('Home.jpg')  # Set the background image for sign-in page
    
    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign In"):
        if sign_in(username, password):
            st.session_state['signed_in'] = True
            st.session_state['current_page'] = "Home"
            st.success("Sign in successful! Redirecting to Home...")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Home Page
def home_page():
    st.title("Welcome to Aurora!")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    **Aurora** is a unique music recommendation system that uses the *Time Theory of Ragas* to recommend music that suits your emotional and mental state depending on the time of day.
    
    ### Benefits of Using Aurora:
    - Relieve stress by listening to Ragas associated with specific times of the day.
    - Feel a deeper connection to Indian Classical Music and its healing properties.
    - Explore different Ragas throughout the day for a holistic, meditative experience.
    """)

    if st.button("Let's Get Your Stress Relieved"):
        st.session_state['current_page'] = "Recommendation"
        st.experimental_rerun()

# Recommendation Page with audio playback and navigation to individual Raga pages
def recommendation_page():
    st.title("Music Recommendation Based on Time of Day")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    raga_recommendation, audio_file, raga_phase = get_raga_recommendation_and_audio()
    
    st.subheader("Current Raga Recommendation:")
    st.success(raga_recommendation)
    st.audio(audio_file)

    if st.button("Play Now"):
        st.audio(audio_file)
        st.markdown("Now playing: {}".format(raga_recommendation))

    if st.button("Why this Raag?"):
        st.session_state['current_page'] = raga_phase
        st.experimental_rerun()

# Individual Raga Pages with background
def morning_page():
    st.title("Morning Raga: Bhairav, Todi")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    ### History and Significance:
    - **Bhairav**: Known for its serious and devotional mood, Raga Bhairav is usually performed early in the morning and is associated with calmness and meditation. It’s one of the foundational Ragas in Indian classical music, with roots that stretch back centuries.
    - **Todi**: Often performed in the pre-dawn hours, Raga Todi is associated with a mood of devotion, introspection, and tranquility.
    """)

def forenoon_page():
    st.title("Forenoon Raga: Ahir Bhairav, Deshkar")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    ### History and Significance:
    - **Ahir Bhairav**: This Raga is a blend of Bhairav and Ahir, and is performed in the early morning hours. It’s known for its serenity and is used to evoke feelings of peace and spiritual longing.
    - **Deshkar**: Played in the early hours of the day, this raga invokes feelings of freshness and purity, making it an ideal forenoon Raga.
    """)

def afternoon_page():
    st.title("Afternoon Raga: Bhimpalasi, Madhuvanti")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    ### History and Significance:
    - **Bhimpalasi**: Associated with the scorching heat of the afternoon, Bhimpalasi creates a mood of longing and relaxation. It is traditionally performed during the mid-day hours and evokes feelings of devotion and reverence.
    - **Madhuvanti**: This Raga creates a sweet and tender mood, perfect for the later part of the afternoon, and is associated with feelings of love and desire.
    """)

def evening_page():
    st.title("Evening Raga: Yaman, Marwa")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    ### History and Significance:
    - **Yaman**: A serene and meditative Raga that is performed in the early evening. Yaman is one of the most commonly performed Ragas and is associated with a calm, contemplative mood.
    - **Marwa**: Known for its tension and dramatic feel, Raga Marwa is associated with the setting sun and creates a deep, spiritual experience.
    """)

def night_page():
    st.title("Night Raga: Darbari Kanada, Malkauns")
    add_bg_from_local('allpages.jpg')  # Set the background image for all pages except sign-in
    
    st.markdown("""
    ### History and Significance:
    - **Darbari Kanada**: This Raga is traditionally played in the late-night hours and is associated with royalty and grandeur. It evokes a deep, serious mood.
    - **Malkauns**: Performed at midnight, Malkauns is a majestic and heavy Raga, inducing a mood of peace and meditation.
    """)

# Main App Layout
def main():
    if 'signed_in' not in st.session_state:
        st.session_state['signed_in'] = False
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "Sign In"

    current_page = st.session_state['current_page']
    
    if current_page == "Sign In":
        sign_in_page()
    elif current_page == "Home":
        if st.session_state['signed_in']:
            home_page()
        else:
            st.warning("Please sign in first.")
            st.session_state['current_page'] = "Sign In"
            st.experimental_rerun()
    elif current_page == "Recommendation":
        if st.session_state['signed_in']:
            recommendation_page()
        else:
            st.warning("Please sign in first.")
            st.session_state['current_page'] = "Sign In"
            st.experimental_rerun()
    elif current_page == "Morning":
        morning_page()
    elif current_page == "Forenoon":
        forenoon_page()
    elif current_page == "Afternoon":
        afternoon_page()
    elif current_page == "Evening":
        evening_page()
    elif current_page == "Night":
        night_page()

# Run the app
if __name__ == "__main__":
    main()
