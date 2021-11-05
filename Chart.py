import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app():
    st.title('～数字で見るNBA～')
    st.write('このページはNBA入門者に向けて作ったものです。NBAに関する様々な数字を見て楽しんでいただけると幸いです。\
        長年見ている方にとっては当たり前すぎるかもしれません。それでも見ていただけるNクラの皆さんには感謝申し上げます。')
    st.write('ここに載っている数字は、全てBASKETBALL REFERENCEから取ってきたものです。リンクを貼っておくので、気になる人は覗いてみてください。\
        色々な情報が載っていて面白いと思います。')
    st.markdown('<a href="https://www.basketball-reference.com/">BASKETBALL REFERENCE</a>',unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        st.image('warri.jpg', use_column_width=True)

    with col2:
        st.image('lakers.jpg',use_column_width=True)

    with col3:
        st.image('gianiss.jpg',use_column_width=True)
    

    st.header('▼2000-01 ~ 2020-21のスタッツの変化')
    st.write('※以下、 出てくるグラフの横軸"Season"は、2012-2013→13のように表記しています。')
    st.write('※ 慣れない形式で作成したので見づらいところが多々あると思います。\
        特にグラフに関しては軸の設定が上手くいかなかったので、数字上ではそこまで変わらないのにグラフ上ではすごく変化しているように見えてしまうことがあります。\
            申し訳ありません。')


    df_PTS=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Points Per Game':[94.8,95.5,95.1,93.4,97.2,97.0,98.7,99.9,100.0,100.4,99.6,96.3,98.1,101.0,100.0,102.7,105.6,106.3,111.2,111.8,112.1]
    })
    fig_PTS=px.line(df_PTS,x='Season',y='Points Per Game')

    df_TRB=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Total Rebounds Per Game':[42.5,42.4,42.3,42.2,41.9,41.0,41.1,42.0,41.3,41.7,41.4,42.2,42.1,42.7,43.3,43.8,43.5,43.5,45.2,44.8,44.3]
    })
    fig_TRB=px.line(df_TRB,x='Season',y='Total Rebounds Per Game')

    # df_shooting=pd.DataFrame({
    # 'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
    #     'FG':[44.3,44.5,44.2,43.9,44.7,45.4,45.8,45.7,45.9,46.1,45.9,44.8,45.3,45.4,44.9,45.2,45.7,46.0,46.1,46.0,46.6],
    #     'FG3P':[35.4,35.4,34.9,34.7,35.6,35.8,35.8,36.2,36.7,35.5,35.8,34.9,35.9,36.0,35.0,35.4,35.8,36.2,35.5,35.8,36.7]
    # })
    # fig_shooting=make_subplots(rows=1,cols=1)
    # fig_shooting.add_trace(go.Scatter(
    #     x=df_shooting.Season,
    #     y=df_shooting.FG,
    #     name='Field Goal Percentage'
    # ),row=1,col=1)

    # fig_shooting.add_trace(go.Scatter(
    #     x=df_shooting.Season,
    #     y=df_shooting.FG3P,
    #     name='3-Point Field Goal Percentage'
    # ),row=1,col=1)
    # fig=fig_shooting.update_layout(title_text='2Pointと3Point それぞれの成功率')

    df_FG=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Field Goal Percentage':[44.3,44.5,44.2,43.9,44.7,45.4,45.8,45.7,45.9,46.1,45.9,44.8,45.3,45.4,44.9,45.2,45.7,46.0,46.1,46.0,46.6]
    })
    fig_FG=px.line(df_FG,x='Season',y='Field Goal Percentage')
    
    
    df_3FG=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        '3-Point Field Goal Percentage':[35.4,35.4,34.9,34.7,35.6,35.8,35.8,36.2,36.7,35.5,35.8,34.9,35.9,36.0,35.0,35.4,35.8,36.2,35.5,35.8,36.7]
    })
    fig_3FG=px.line(df_3FG,x='Season',y='3-Point Field Goal Percentage')

    df_FGA=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Field Goal Attempts Per Game':[80.6,81.3,80.8,79.8,80.3,79.0,79.7,81.5,80.9,81.7,81.2,81.4,82.0,83.0,83.6,84.6,85.4,86.1,89.2,88.8,88.4]
    })
    fig_FGA=px.line(df_FGA,x='Season',y='Field Goal Attempts Per Game')

    df_FG3A=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        '3-Point Field Goal Attempts Per Game':[13.7,14.7,14.7,14.9,15.8,16.0,16.9,18.1,18.1,18.1,18.0,18.4,20.0,21.5,22.4,24.1,27.0,29.0,32.0,34.1,34.6]
    })
    fig_FG3A=px.line(df_FG3A,x='Season',y='3-Point Field Goal Attempts Per Game')

    df_PACE=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Pace':[91.3,90.7,91.0,90.1,90.9,90.5,91.9,92.4,91.7,92.7,92.1,91.3,92.0,93.9,93.9,95.8,96.4,97.3,100.0,100.3,99.2]
    })
    fig_PACE=px.line(df_PACE,x='Season',y='Pace')

    df_TOV=pd.DataFrame({
        'Season':['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'],
        'Turnovers Per Game':[15.0,14.5,14.9,15.0,14.5,14.4,15.1,14.1,14.0,14.2,14.3,14.6,14.6,14.6,14.4,14.4,14.0,14.3,14.1,14.5,13.8]
    })
    fig_TOV=px.line(df_TOV,x='Season',y='Turnovers Per Game')

    expander1=st.expander('▼シーズン毎のリーグ全体の平均得点の推移')
    expander1.write('ここ20年で平均得点は20点近くも伸びている。その原因を他のスタッツも見ながら考えてみる。')
    expander1.plotly_chart(fig_PTS,use_column_width=True)

    expander2=st.expander('▼シーズン毎のリーグ全体のリバウンド数の推移')
    expander2.write('平均得点が20点も伸びているということは、その分シュート試投数も増えているはずだが、リバウンド数はここ20年で約2本ほどしか増加していない。つまり、この20年で増えたシュートの試投は高確率で決まり、リバウンドに繋がっていないのだろうか。')
    expander2.write('それとも、シュートの試投数自体はあまり変化がないが、シュート成功率が上がったのだろうか。')
    expander2.plotly_chart(fig_TRB,use_column_width=True)

    expander3=st.expander('▼シーズン毎のリーグ全体のシュート成功率の推移')
    expander3.write('まずは、ここ20年でシュートの成功率はどのように変化してきたのかを見ていこう。')
    expander3.write('両方とも、毎年ほとんど変わらない成功率となっており、多くても1~2%の上昇となっていることが分かる。')
    expander3.plotly_chart(fig_FG,use_column_width=True)

    expander4=st.expander('▼シーズン毎のリーグ全体のフィールドゴール試投数の推移')
    expander4.write('ここでのフィールドゴールとは2Pointのシュートのことである。')
    expander4.write('20年前と比べると9本増加していることが分かる。2Pointの成功率は約45%であるので、この9本から生まれた得点は約8点分。\
        「▼シーズン毎のリーグ全体の平均得点の推移」を参照してもらうとわかるように、この8点だけでは補えないほど平均得点は増えている。')
    expander4.plotly_chart(fig_FGA,use_column_width=True)
    expander4.write('では、残りの原因として考えられるのは何だろうか。そう、Splash Brothersを中心に旋風を巻き起こし、時代を変えてしまった"3Point"である。')

    expander5=st.expander('▼シーズン毎のリーグ全体の3Pointの試投数の推移')
    expander5.write('Splash Brothersが真価を発揮して以降、試投数が増えていたことはもちろん知っていたが、まさか20年前に比べて30本近くも増えているとは、、、')
    expander5.plotly_chart(fig_FG3A,use_column_width=True)
    expander5.plotly_chart(fig_FG3A,use_column_width=True)

    expander6=st.expander('▼シーズン毎のリーグ全体のペースの推移')
    expander6.write('まず、ここで言うペースとは、An estimate of possessions per 48 minutes つまりチームが48分間（1試合）に使用するポゼッション数の推定値のことである。')
    expander6.write('とても簡単に説明するなら、ペースとは試合のテンポのことです。ペースの値が大きければ大きいほど試合のテンポも速くなります')
    expander6.plotly_chart(fig_PACE,use_column_width=True)
    expander6.write('ちなみに、2020-21シーズンで見てみると、ウィザーズが2位のバックスとウォリアーズに"2"の差をつけて1位でした。\
        （ウィザーズが106.4、バックスとウォリアーズが104.4）ウィザーズの試合や結果を見ていると納得の数字ですね（笑）')
    expander6.write('自分の応援しているチームのペースがどれくらいなのか知りたい方は、下記のリンクから飛んで見られますので是非。')
    expander6.markdown('<a href="http://www.espn.com/nba/hollinger/teamstats/_/sort/paceFactor">こちらから</a>',unsafe_allow_html=True)

    expander7=st.expander('▼シーズン毎のリーグ全体のターンオーバー数の推移')
    expander7.write('最後にターンオーバーの数を見ていく。')
    expander7.plotly_chart(fig_TOV,use_column_width=True)
    expander7.write('ペースも速くなりオフェンスの回数も増えたことから、それに応じてターンオーバー数も増えたであろうと予想していた。\
        だが実際は、増えるどころか減っている。何故なのだろうか、、、？昔に比べてディフェンスの激しさが無くなったから、、？分かる方がいれば教えてください（笑）')
