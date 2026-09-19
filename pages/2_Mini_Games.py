import random
import time

import streamlit as st
from utils import inject_css, page_header

st.set_page_config(page_title="Mini Games - Mr. Tangerine", page_icon="🎮")
inject_css()
page_header("🎮 Mini Games")

tab1, tab2 = st.tabs(["🍊 Click the Tangerine", "🧠 Memory Match"])

# ---------------------------------------------------------------------------
# Click the Tangerine
# ---------------------------------------------------------------------------
with tab1:
    st.markdown(
        "<div class='tangerine-card'>Click as fast as you can for 10 seconds. Every click is one "
        "more unit of joy delivered to Mr. Tangerine. 🍊</div>",
        unsafe_allow_html=True,
    )

    if "click_count" not in st.session_state:
        st.session_state.click_count = 0
    if "click_start" not in st.session_state:
        st.session_state.click_start = None

    def start_challenge():
        st.session_state.click_count = 0
        st.session_state.click_start = time.time()

    def register_click():
        if st.session_state.click_start is not None:
            elapsed = time.time() - st.session_state.click_start
            if elapsed <= 10:
                st.session_state.click_count += 1

    c1, c2 = st.columns(2)
    with c1:
        st.button("🚦 Start 10s Challenge", on_click=start_challenge)
    with c2:
        st.button("🍊 CLICK!", on_click=register_click)

    if st.session_state.click_start is not None:
        elapsed = time.time() - st.session_state.click_start
        remaining = max(0.0, 10 - elapsed)
        if remaining > 0:
            st.progress(remaining / 10)
            st.write(f"⏱️ Time left: {remaining:.1f}s — Clicks: {st.session_state.click_count}")
        else:
            st.markdown(f"### ⏰ Time's up! Final score: {st.session_state.click_count} clicks")
            if st.session_state.click_count >= 30:
                st.balloons()
                st.success("Tangerine Overlord status achieved! 🍊👑")
            elif st.session_state.click_count >= 15:
                st.info("Certified sunshine spreader! ☀️")
            else:
                st.warning("A gentle glow. Try again for full radiance! 🍊")

# ---------------------------------------------------------------------------
# Memory Match
# ---------------------------------------------------------------------------
with tab2:
    st.markdown(
        "<div class='tangerine-card'>Find every matching pair. Simple, chaotic, weirdly addictive. "
        "🎉</div>",
        unsafe_allow_html=True,
    )

    EMOJIS = ["🍊", "🎈", "🎉", "🎁", "🌟", "🎂"]

    def new_memory_game():
        deck = EMOJIS * 2
        random.shuffle(deck)
        st.session_state.memory_deck = deck
        st.session_state.memory_revealed = [False] * len(deck)
        st.session_state.memory_matched = [False] * len(deck)
        st.session_state.memory_selection = []
        st.session_state.pending_hide = None

    if "memory_deck" not in st.session_state:
        new_memory_game()

    st.button("🔄 New game", key="new_memory", on_click=new_memory_game)

    cols = st.columns(4)
    for idx, emoji in enumerate(st.session_state.memory_deck):
        col = cols[idx % 4]
        revealed = st.session_state.memory_revealed[idx] or st.session_state.memory_matched[idx]
        label = emoji if revealed else "🟦"
        disabled = (
            st.session_state.memory_matched[idx]
            or revealed
            or bool(st.session_state.pending_hide)
            or len(st.session_state.memory_selection) >= 2
        )
        if col.button(label, key=f"card_{idx}", disabled=disabled):
            st.session_state.memory_revealed[idx] = True
            st.session_state.memory_selection.append(idx)
            if len(st.session_state.memory_selection) == 2:
                a, b = st.session_state.memory_selection
                if st.session_state.memory_deck[a] == st.session_state.memory_deck[b]:
                    st.session_state.memory_matched[a] = True
                    st.session_state.memory_matched[b] = True
                    st.session_state.memory_selection = []
                else:
                    st.session_state.pending_hide = (a, b)

    if st.session_state.pending_hide:
        st.info("Not a match — take a peek, then continue. 👀")
        if st.button("👉 Continue"):
            a, b = st.session_state.pending_hide
            st.session_state.memory_revealed[a] = False
            st.session_state.memory_revealed[b] = False
            st.session_state.memory_selection = []
            st.session_state.pending_hide = None
            st.rerun()

    if all(st.session_state.memory_matched):
        st.balloons()
        st.success("All matched! Mr. Tangerine is officially delighted. 🍊🎉")
