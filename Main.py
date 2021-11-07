import streamlit as st
from Transcribe import *
from googletrans import Translator
tr = Translator()

def app():
    
    st.title("NBA × 英語で学ぶ")
    st.write('▼このページで出来ることは以下の通りです。')
    st.write('パソコンの音声ファイルや、スマホで録画した動画の文字起こし＆翻訳')
    
    st.header('～文字起こし ＆ 翻訳～')
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
    
