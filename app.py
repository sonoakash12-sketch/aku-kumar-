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
.animated-heart:nth-child(2) { left: 30%; animati






