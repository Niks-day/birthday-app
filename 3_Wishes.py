import html
import json
import os

import streamlit as st
from utils import inject_css, page_header

st.set_page_config(page_title="Wishes - Mr. Tangerine", page_icon="💌")
inject_css()
page_header("💌 Leave a Birthday Wish")

WISHES_FILE = os.path.join(os.path.dirname(__file__), "..", "wishes.json")


def load_wishes():
    if os.path.exists(WISHES_FILE):
        try:
            with open(WISHES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_wishes(wishes):
    try:
        with open(WISHES_FILE, "w", encoding="utf-8") as f:
            json.dump(wishes, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


st.markdown(
    "<div class='tangerine-card'>Drop a birthday message for Mr. Tangerine. Puns encouraged. "
    "🍊</div>",
    unsafe_allow_html=True,
)

name = st.text_input("Your name (optional)")
wish = st.text_area("Your wish", placeholder="May your day be as bright as your namesake... 🍊")

if st.button("🎈 Send wish"):
    if wish.strip():
        wishes = load_wishes()
        wishes.append({"name": name.strip() or "Anonymous", "wish": wish.strip()})
        save_wishes(wishes)
        st.success("Wish delivered! 🎉")
        st.balloons()
    else:
        st.warning("Write something first — even a tangerine pun counts. 🍊")

st.markdown("### 🎉 Wishes so far")
all_wishes = load_wishes()
if not all_wishes:
    st.write("No wishes yet — be the first!")
else:
    for w in reversed(all_wishes):
        safe_name = html.escape(str(w.get("name", "Anonymous")))
        safe_wish = html.escape(str(w.get("wish", ""))).replace("\n", "<br>")
        st.markdown(
            f"<div class='tangerine-card'><b>{safe_name}</b><br>{safe_wish}</div>",
            unsafe_allow_html=True,
        )
