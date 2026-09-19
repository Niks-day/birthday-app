import streamlit as st
from utils import inject_css, page_header

st.set_page_config(page_title="Trivia - Mr. Tangerine", page_icon="🧠")
inject_css()
page_header("🧠 The Mr. Tangerine Trivia Challenge")

st.markdown(
    """
    <div class="tangerine-card">
    <b>Official Lore (100% legally binding):</b><br>
    Legend says Mr. Tangerine's happiness is so contagious he once made a silent elevator burst into
    laughter in under 10 seconds. His favorite color is, obviously, tangerine. He's convinced soft
    blue skies exist purely to match his vibe on his birthday. Read carefully — there will be a quiz. 📜
    </div>
    """,
    unsafe_allow_html=True,
)

questions = [
    {
        "q": "What did Mr. Tangerine once do to a silent elevator?",
        "options": ["Made it play music", "Made it burst into laughter", "Got it stuck", "Redecorated it"],
        "answer": "Made it burst into laughter",
    },
    {
        "q": "What is Mr. Tangerine's favorite color?",
        "options": ["Forest green", "Tangerine", "Beige", "Maroon"],
        "answer": "Tangerine",
    },
    {
        "q": "Why does Mr. Tangerine think the sky is blue?",
        "options": [
            "Pure coincidence",
            "To match his birthday vibe",
            "Science he ignores",
            "He's never noticed",
        ],
        "answer": "To match his birthday vibe",
    },
    {
        "q": "How fast can Mr. Tangerine turn a bad mood around?",
        "options": ["Under 10 seconds", "A few days", "Never happens, he has no bad moods", "Depends on coffee"],
        "answer": "Under 10 seconds",
    },
    {
        "q": "What's the most accurate description of Mr. Tangerine's energy?",
        "options": ["Contagious happiness", "Mildly grumpy", "Quietly plotting", "Allergic to fun"],
        "answer": "Contagious happiness",
    },
]

if "trivia_answers" not in st.session_state:
    st.session_state.trivia_answers = [None] * len(questions)

for i, item in enumerate(questions):
    st.markdown(f"**Q{i + 1}. {item['q']}**")
    st.session_state.trivia_answers[i] = st.radio(
        label=f"question_{i}",
        options=item["options"],
        index=None,
        key=f"trivia_{i}",
        label_visibility="collapsed",
    )
    st.write("")

if st.button("🍊 Submit answers"):
    answered = [a for a in st.session_state.trivia_answers if a is not None]
    if len(answered) < len(questions):
        st.warning("Answer every question — Mr. Tangerine expects full commitment. 😄")
    else:
        score = sum(
            1
            for i, item in enumerate(questions)
            if st.session_state.trivia_answers[i] == item["answer"]
        )
        st.markdown(f"### You scored {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
            st.success("Perfect score! You clearly know your tangerine lore. 🍊🏆")
        elif score >= len(questions) // 2:
            st.info("Solid effort! Mr. Tangerine approves. 😄")
        else:
            st.warning("Re-read the lore and try again — happiness rewards persistence. 🍊")
