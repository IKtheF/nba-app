import Home
import Chart
import Quize
import Use
import Main
import streamlit as st

PAGES={
    "ホーム":Home,
    "音声ファイルの文字起こし＆翻訳":Main,
    #"数字で見るNBA": Chart,
    "NBAクイズ":Quize,
    "使い方": Use
}

st.sidebar.title('MENU')
selection=st.sidebar.radio("選択してください", list(PAGES.keys()))
page=PAGES[selection]
page.app()
