import streamlit as st
import random
import time

# --------------------------
# CONFIG
# --------------------------
APP_TITLE = "Pravisha's Portal 💕"
SITE_PASSWORD = "loveyou"  # change this password

st.set_page_config(page_title=APP_TITLE, layout="centered")

# --------------------------
# SESSION STATE
# --------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --------------------------
# CSS for romantic effects
# --------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
    background-size: cover;
}

h1, h2, h3, h4, h5, h6, label, .css-16huue1, .css-10trblm {
    font-family: "Comic Sans MS", cursive, sans-serif !important;
    color: #d63384 !important;
}

.stButton > button {
    border-radius: 20px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Floating heart animation */
.heart {
    position: fixed;
    font-size: 30px;
    animation: floatUp 3s linear forwards;
    z-index: 999;
}

@keyframes floatUp {
    from { transform: translateY(0); opacity: 1; }
    to { transform: translateY(-200px); opacity: 0; }
}

/* NO button styling */
#no_btn {
    background-color:#ffcccc; 
    border:none; 
    padding:8px 20px; 
    border-radius:20px;
    cursor:pointer;
    position: relative;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# LOGIN PAGE
# --------------------------
if not st.session_state.authenticated:
    st.title(APP_TITLE)
    st.subheader("🔒 Enter password to continue")

    pw = st.text_input("Enter our secret password:", type="password")

    if st.button("Enter 🚪") or (pw and pw == SITE_PASSWORD):
        if pw == SITE_PASSWORD:
            st.session_state.authenticated = True
            st.success("Password accepted — welcome to your portal, Pravisha! 🎉")
            st.rerun()
        else:
            st.error("Oops! Wrong password, try again 💔")

# --------------------------
# QUESTIONS PAGE
# --------------------------
else:
    st.title("💌 Answer these, my love 💕")

    questions = [
        "Do you love me? 💖",
        "Will you be mine forever? 💍",
        "Do you like my silly jokes? 😂",
        "Can I get unlimited kisses from you? 😘",
        "Are you the best part of my life? 🌎",
        "Do you want cuddles right now? 🤗",
        "Will you go on a date with me soon? 🍷",
        "Do you like being pampered by me? 💆‍♀️",
        "Wanna plan a surprise trip together? ✈️",
        "Do you promise never to leave me? 💞",
    ]

    for i, q in enumerate(questions):
        st.subheader(q)
        col1, col2 = st.columns([1,1])

        with col1:
            yes_btn = st.button("Yes 💖", key=f"yes_{i}")
            if yes_btn:
                st.success(f"Yay!! You clicked YES for: {q}")
                # Floating hearts
                for j in range(10):
                    st.markdown(
                        f"<div class='heart' style='left:{random.randint(10,90)}%; top:{random.randint(60,90)}%;'>❤️</div>",
                        unsafe_allow_html=True
                    )
                    time.sleep(0.05)

        with col2:
            # Inject custom JS No button
            st.markdown(
                f"""
                <div>
                    <button id="no_btn_{i}">No 💔</button>
                </div>
                <script>
                const noBtn = document.getElementById("no_btn_{i}");
                noBtn.addEventListener("mouseover", function() {{
                    let x = (Math.random() * 200 - 100);
                    let y = (Math.random() * 200 - 100);
                    noBtn.style.transform = `translate(${{x}}px, ${{y}}px)`;
                }});
                </script>
                """,
                unsafe_allow_html=True
            )

    st.write("---")
    if st.button("Submit ❤️"):
        st.balloons()
        st.success("My dearest Pravisha, you are my forever love 💕\n\nYou make my world brighter, my heart fuller, and my life happier. 🌸")
        for i in range(20):
            st.markdown(
                f"<div class='heart' style='left:{random.randint(5,95)}%; top:{random.randint(60,90)}%;'>💖</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.05)



