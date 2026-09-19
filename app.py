import streamlit as st
from utils import inject_css, page_header

st.set_page_config(page_title="Mr. Tangerine's Birthday", page_icon="🍊", layout="centered")
inject_css()

page_header("🍊 Happy Birthday, Mr. Tangerine! 🎉", "The one-man unofficial happiness department.")

st.markdown(
    """
    <div class="tangerine-card">
    Somewhere between a sunrise and a good punchline, Mr. Tangerine was born — and the world got a
    little brighter for it. 🌤️<br><br>
    He's the guy who walks into a room and somehow the whole room forgets it had a bad day.
    Contagious happiness should honestly require a warning label. 😄<br><br>
    So today, we celebrate the human equivalent of citrus sunshine. Use the sidebar to explore
    trivia, mini-games, and a page to leave your birthday wish. 🎈
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    if st.button("🎈 Make a wish"):
        st.balloons()
        st.success("Wish sent into the tangerine skies! 🍊✨")
with col2:
    if st.button("🎉 Say happy birthday"):
        st.snow()
        st.info("Somewhere, Mr. Tangerine just felt a happiness spike. 📈")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#7A8A99;'>"
    "👈 Use the sidebar to explore Trivia, Mini Games, and Wishes."
    "</p>",
    unsafe_allow_html=True,
)
