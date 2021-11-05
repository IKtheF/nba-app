import streamlit as st

def app():
    st.header('使い方')
    st.write('このアプリの使い方を説明します。')
    
    st.subheader('▼音声の文字起こし＆翻訳の使い方')
    st.write('音声ファイルをアップロードしていただくと自動で音声を文字に起こして和訳してくれます。\
        実際に使っている動画を載せておくのでご覧ください。')
    st.write('パソコンでご利用の方はWAVファイル、MP4ファイル、MP3ファイルに対応しています。スマホでご利用の方は画面録画した動画でも対応可能です。\
        また、どうしても実際の音声と異なって文字に起こしてしまうこともあります。\
        予めご了承ください。')
    st.write('※画面の録画上、ファイル画面が開いている部分はカットしてあります。')

    video_file1=open('how_to_use1.mp4' , 'rb')
    video_bytes1=video_file1.read()
    st.video(video_bytes1)

    st.subheader('▼お好きな言葉を翻訳の使い方')
    st.write('テキストボックスに翻訳したい言葉を入力し、言語選択をしてください。\
        その後、翻訳開始ボタンを押すと翻訳が開始されます。')
    st.write('※現在は日本語と英語のみ対応しています。今後要望があればその他の言語も対応可能にしていきます。')

    video_file2=open('how_to_use2.mp4' , 'rb')
    video_bytes2=video_file2.read()
    st.video(video_bytes2)

    st.write('--------------------------------------------------')

    st.subheader('▼NBAクイズの使い方')
    st.write('詳しい使い方はこちらも「NBAクイズ」本編に記載してあります。\
        難易度は決して易しくはないですが、ぜひ80点以上の殿堂入り目指して頑張ってください！')
