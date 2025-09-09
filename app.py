import streamlit as st
import random
import time

# --------------------------
# CONFIG
# --------------------------
APP_TITLE = "Pravisha's Portal 💕"
SITE_PASSWORD = "loveyou"

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
    background: linear-gradient(-45deg, #ffdde1, #ee9ca7, #ffb3c6, #ffc8dd);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    overflow: hidden;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* floating hearts background */
@keyframes floatHearts {
    0% { transform: translateY(100vh) scale(0.5); opacity: 1;}
    100% { transform: translateY(-10vh) scale(1.2); opacity: 0;}
}
.animated-heart {
    position: fixed;
    bottom: -10vh;
    color: rgba(255,0,100,0.5);
    font-size: 24px;
    animation: floatHearts 12s linear infinite;
    z-index: 0;
}

.animated-heart:nth-child(1) { left: 10%; animation-delay: 0s; }
.animated-heart:nth-child(2) { left: 30%; animation-delay: 3s; }
.animated-heart:nth-child(3) { left: 50%; animation-delay: 6s; }
.animated-heart:nth-child(4) { left: 70%; animation-delay: 9s; }
.animated-heart:nth-child(5) { left: 90%; animation-delay: 12s; }

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
    background: linear-gradient(135deg,#ff99cc,#ff6699);
    color:white;
}

/* Floating heart click animation */
.heart {
    position: fixed;
    font-size: 30px;
    animation: floatUp 3s linear forwards;
    z-index: 9999;
}
@keyframes floatUp {
    from { transform: translateY(0); opacity: 1; }
    to { transform: translateY(-200px); opacity: 0; }
}
</style>

<!-- background floating hearts -->
<div class="animated-heart">❤️</div>
<div class="animated-heart">💖</div>
<div class="animated-heart">💕</div>
<div class="animated-heart">💞</div>
<div class="animated-heart">💘</div>
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
        col1, col2 = st.columns([1, 1])

        # YES button
        with col1:
            yes_btn = st.button("Yes 💖", key=f"yes_{i}")
            if yes_btn:
                st.success(f"Yay!! You clicked YES for: {q}")
                # Floating hearts when clicked
                for j in range(10):
                    st.markdown(
                        f"<div class='heart' style='left:{random.randint(10,90)}%; top:{random.randint(60,90)}%;'>❤️</div>",
                        unsafe_allow_html=True
                    )
                    time.sleep(0.05)

        # NO button (runs away)
        with col2:
            st.markdown(
                f"""
                <div style="position: relative; height:50px;">
                    <button id="no_btn_{i}" 
                        style="
                            background-color:#ffcccc; 
                            border:none; 
                            padding:8px 20px; 
                            border-radius:20px;
                            cursor:pointer;
                            position:absolute;
                            left:0;
                            top:0;
                        ">
                        No 💔
                    </button>
                </div>

                <script>
                const btn = document.getElementById("no_btn_{i}");
                btn.addEventListener("mouseover", function() {{
                    let x = Math.floor(Math.random() * 300) - 150;
                    let y = Math.floor(Math.random() * 300) - 150;
                    btn.style.transform = `translate(${{x}}px, ${{y}}px)`;
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





