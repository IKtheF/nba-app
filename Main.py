import streamlit as st
from Transcribe import *
from googletrans import Translator
tr = Translator()

def app():
    
    st.title("NBA × 英語で学ぶ")
    st.write('このページで出来ることは以下の通りです。')
    st.write('--------------------------------------------------')
    
    st.write('①パソコンの音声ファイルや、スマホで録画した動画の文字起こし＆翻訳')
    st.write('②入力したテキストの和訳または英訳')
    st.header('～音声ファイルの文字起こし ＆ 翻訳～')
    fileObject = st.file_uploader(label = "音声ファイルをアップロードしてください" )

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
    
    st.write('--------------------------------------------------')

    st.header('～お好きな言葉を翻訳～')
    input_text=st.text_input('翻訳したい言葉を入力して下さい')

    st.write('▼言語選択')
    pre_option=st.selectbox('翻訳前の言語を選択してください（日本語を英訳するなら「日本語」を選択）',
    ('日本語','英語'))
    st.write('選択中の言語:',pre_option)

    if pre_option == '英語':
        pre='en'
        post='ja'
    else:
        pre='ja'
        post='en'

    if input_text is not None:
        if st.button('翻訳開始！'):
            result = tr.translate(input_text,src=pre,dest=post).text
            st.subheader('▼翻訳結果')
            st.write(result)
