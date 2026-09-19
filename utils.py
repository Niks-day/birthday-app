import streamlit as st

PRIMARY = "#FF7A33"


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Fredoka', sans-serif;
        }

        .stApp {
            background: linear-gradient(180deg, #EAF4FC 0%, #DCEEFB 100%);
        }

        .tangerine-card {
            background: #FFFFFF;
            border-radius: 20px;
            padding: 1.4rem 1.8rem;
            box-shadow: 0 4px 14px rgba(255, 122, 51, 0.15);
            border: 2px solid #FFD9B3;
            margin-bottom: 1.1rem;
            color: #1F2A37;
        }

        .tangerine-title {
            color: #FF7A33;
            text-align: center;
        }

        div.stButton > button {
            background-color: #FF7A33;
            color: white;
            border-radius: 999px;
            border: none;
            padding: 0.5rem 1.4rem;
            font-weight: 600;
        }
        div.stButton > button:hover {
            background-color: #FF974D;
            color: white;
        }
        div.stButton > button:disabled {
            background-color: #FFD9B3;
            color: #FFF6EE;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title, subtitle=""):
    st.markdown(f"<h1 class='tangerine-title'>{title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(
            f"<p style='text-align:center; color:#4A5A68;'>{subtitle}</p>",
            unsafe_allow_html=True,
        )
