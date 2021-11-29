import streamlit as st

def app():
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

