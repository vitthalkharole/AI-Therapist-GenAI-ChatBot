
import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SafeSpace",
    page_icon="🧠",
    layout="centered"
)

BACKEND_URL = "http://localhost:8000/ask"


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 16px;
    margin-bottom: 30px;
}

.chat-container {
    max-width: 800px;
    margin: auto;
}

.stChatInput {
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">🧠 SafeSpace</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A safe space to talk, reflect, and get support.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Chat History
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.chat_history:

    with st.chat_message(
        message["role"],
        avatar="🧑" if message["role"] == "user" else "🧠"
    ):
        st.write(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input(
    "Share what's on your mind..."
)


if user_input:

    # Show user message immediately
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)

    # AI response
    with st.chat_message("assistant", avatar="🧠"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    BACKEND_URL,
                    json={"message": user_input},
                    timeout=60
                )

                if response.status_code == 200:

                    data = response.json()
                    ai_response = data.get(
                        "response",
                        "I'm unable to generate a response right now."
                    )

                else:

                    ai_response = (
                        "Sorry, I'm having trouble connecting "
                        "to the AI service."
                    )

            except requests.exceptions.ConnectionError:

                ai_response = (
                    "⚠️ Backend server is not running. "
                    "Please start your FastAPI server."
                )

            except requests.exceptions.Timeout:

                ai_response = (
                    "⏳ The AI is taking too long to respond. "
                    "Please try again."
                )

            except Exception as e:

                ai_response = (
                    "Something went wrong. Please try again."
                )

        st.write(ai_response)

    # Save AI response
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": ai_response
    })


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🧠 SafeSpace")

    st.write(
        "Your AI mental health companion for "
        "supportive conversations."
    )

    st.divider()

    st.subheader("💡 How it works")

    st.write("""
    - 💬 Share what's on your mind
    - 🧠 Get an AI-generated response
    - 🆘 Safety support for crisis situations
    - 📍 Find nearby professional help
    """)

    st.divider()

    if st.button("🗑️ Clear Conversation"):

        st.session_state.chat_history = []

        st.rerun()

    st.caption(
        "SafeSpace is an AI assistant and not a replacement "
        "for a qualified mental health professional."
    )

