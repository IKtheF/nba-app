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
    st.write('メインの機能は「音声ファイルの文字起こし＆翻訳」ですが、その他にも様々な機能を搭載しているので是非使用してみて下さい。詳しい使い方は、左のサイドバーの「使い方」からご覧ください。')

    st.header('使い方')
    st.write('このアプリの使い方を説明します。')
    
    st.subheader('▼音声の文字起こし＆翻訳の使い方')
    st.write('音声ファイルをアップロードしていただくと自動で音声を文字に起こして和訳してくれます。\
        実際に使っている動画を載せておくのでご覧ください。')
    st.write('パソコンでご利用の方はWAVファイル、MP4ファイル、MP3ファイルに対応しています。スマホでご利用の方は画面録画した動画でも対応可能です。\
        また、どうしても実際の音声と異なって文字に起こしてしまうこともあります。\
        予めご了承ください。')
 

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


    st.subheader('▼数字で見るNBAの使い方')
    st.write('こちらに関しては、「数字で見るNBA」の本ページの方に詳しい説明は書いていますし、実際に触れていただいたほうが分かりやすいと思うので\
        ここでの説明は割愛させていただきます。')
    st.write('内容的にもかなり浅はかなものしか書いていませんが、もしよろしければご覧になってください（笑）')

    
    
    st.subheader('▼NBAクイズの使い方')
    st.write('詳しい使い方はこちらも「NBAクイズ」本編に記載してあります。\
        難易度は決して易しくはないですが、ぜひ80点以上の殿堂入り目指して頑張ってください！')
    
    st.header('お知らせ')
    st.write('また、InstagramにNBAの絵を投稿しています。もし興味を持っていただけたなら、一度覗いてみてください！フォローもしていただけると嬉しいです！！')
    st.write('リンクに飛べない方は"l3gacy_flash"で検索していただけると幸いです。')
    link='[Instagramはこちらから！](https://www.instagram.com/l3gacy_flash)'
    st.markdown(link,unsafe_allow_html=True)
    #st.markdown('<a href="https://www.instagram.com/l3gacy_flash">Instagramはこちらから！</a>',unsafe_allow_html=True)

    st.header('おまけ')
    music='videoplayback.mp4'
    st.write('NBA好きならテンション上がること間違いなしの音楽を貼っておくので、ぜひ聞いてみてください！')
    st.audio(music)

