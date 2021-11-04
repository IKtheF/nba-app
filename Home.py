import streamlit as st
import datetime as dt

def app():
    st.title('This Is My House')
    now = dt.date.today()
    st.write(f"Today is {now}")
    st.image('nba_all_team.jpg')

    st.header('概要')
    st.write('このアプリは、TwitterなどでNBA選手たちのインタビューを見ていて「この人たちが何を言っているのか知りたい！」、「選手たちの生きた英語を利用して英語の学習がしたい！」\
    と思い作成したものです。')
    st.write('メインの機能は「音声ファイルの文字起こし＆翻訳」ですが、その他にも様々な機能を搭載しているので是非使用してみて下さい。詳しい使い方は、サイドバーの「使い方」からご覧ください。')

    st.header('お知らせ')
    st.write('また、InstagramにNBAの絵を投稿しています。もし興味を持っていただけたなら、一度覗いてみてください！フォローもしていただけると嬉しいです！！')
    st.write('リンクに飛べない方は"l3gacy_flash"で検索していただけると幸いです。')
    st.markdown('<a href="https://www.instagram.com/l3gacy_flash">Instagramはこちらから！</a>',unsafe_allow_html=True)

    st.header('おまけ')
    music='videoplayback.mp4'
    st.write('NBA好きならテンション上がること間違いなしの音楽を貼っておくので、ぜひ聞いてみてください！')
    st.audio(music)
