import streamlit as st
from Transcribe import *
from googletrans import Translator
tr = Translator()

def app():
    
    st.title("NBA × 英語で学ぶ")
    st.write('▼このページで出来ることは以下の通りです。')
    st.write('スマホで録画した動画またはパソコンの動画ファイルの文字起こし＆和訳')
    url='[高精度の翻訳はこちらから！](https://www.deepl.com/ja/translator)'
    

    fileObject = st.file_uploader(label = '下の"Browse files"をタップ（クリック）して音声ファイルをアップロードしてください' )

    if fileObject:
        token, t_id = upload_file(fileObject)
        result = {}

        with st.spinner("少々お待ちください....."):
            while result.get("status") != 'completed':
                result = get_text(token,t_id)

        trans=tr.translate(result['text'],src='en',dest='ja').text

        st.balloons()
        st.subheader("▼文字起こしの結果")
        st.write(result['text'])

        st.subheader('▼翻訳結果')
        st.write(trans)
        st.write('------------------------------')
        st.write('翻訳する際にGoogleを用いているため、翻訳の精度はあまり高くありませんし、不自然な日本語になってしまうことがあります。その場合は、以下のリンクに飛んでいただいて文字起こしされた文章をコピペしてみてください。かなり高精度で翻訳してくれます。')
        st.markdown(url,unsafe_allow_html=True)
    
