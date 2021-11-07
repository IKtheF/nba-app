import Chart
import Quize
import Use
import Home
import Main
import streamlit as st

PAGES={
    "文字起こし＆和訳":Main,
    "テキストを翻訳":Home,
    "NBAクイズ":Quize,
    "数字で見るNBA": Chart,
    "概要や使い方など": Use
}

st.sidebar.title('MENU')
selection=st.sidebar.radio("選択してください", list(PAGES.keys()))
page=PAGES[selection]
page.app()
