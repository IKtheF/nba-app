import streamlit as st

def app():
    cnt=0

    st.subheader('第1問')
    ans1=st.selectbox('レブロンジェームスがNBAでつけたことのある背番号は23と何？',
    ('','3','6','24','30'))
    if ans1=='6':
        cnt+=2

    st.subheader('第2問')
    ans2=st.selectbox('NBAの現在の球団数は？',
    ('','20','24','30','32'))
    if ans2=='30':
        cnt+=2

    st.subheader('第3問')
    ans3=st.selectbox('現在NBAの球団の中で唯一アメリカ以外に本拠地を置くチームがありますが、それはどこ？',
    ('','トロント','バンクーバー','モントリオール','オタワ'))
    if ans3=='トロント':
        cnt+=2

    st.subheader('第4問')
    ans4=st.selectbox('1シーズンでの3ポイント成功数歴代1位の402本を記録した選手は誰？',
    ('','レイアレン','クレイトンプソン','ステフィンカリー','ダミアンリラード'))
    if ans4=='ステフィンカリー':
        cnt+=2

    st.subheader('第5問')
    ans5=st.selectbox('スロベニア出身で2019年の新人王に選ばれた、「欧州の神童」と言えば誰？',
    ('','ステフィンカリー','ルカドンチッチ','ザイオンウィリアムソン','ニコラヨキッチ'))
    if ans5=='ルカドンチッチ':
        cnt+=2

    st.subheader('第6問')
    ans6=st.selectbox('ニューヨークに本拠地を置くチームは「ニューヨークニックス」と何？',
    ('','ネッツ','ホーネッツ','ペリカンズ','メッツ'))
    if ans6=='ネッツ':
        cnt+=2

    st.subheader('第7問')
    ans7=st.selectbox('コービーブライアントがルーキー時代から引退するまで所属していたチームは？',
    ('','シカゴブルズ','ボストンセルティックス','マイアミヒート','ロサンゼルスレイカーズ'))
    if ans7=='ロサンゼルスレイカーズ':
        cnt+=2

    st.subheader('第8問')
    ans8=st.selectbox('"Fear the Beard"で知られる左利きの選手は誰？',
    ('','クレイトンプソン','ジェームスハーデン','カワイレナード','ケビンデュラント'))
    if ans8=='ジェームスハーデン':
        cnt+=2

    st.subheader('第9問')
    ans9=st.selectbox('"The Greek Freak"で知られるギリシャ出身の選手は誰？',
    ('','ヤニスアデトクンポ','ニコラヨキッチ','マヌジノビリ','ルカドンチッチ'))
    if ans9=='ヤニスアデトクンポ':
        cnt+=2

    st.subheader('第10問')
    ans10=st.selectbox('過去四度得点王に輝き、現在はブルックリンネッツに所属している選手は誰？',
    ('','ジェームスハーデン','カーメロアンソニー','アレンアイバーソン','ケビンデュラント'))
    if ans10=='ケビンデュラント':
        cnt+=2

    st.subheader('第11問')
    ans11=st.selectbox('2000年以降（1999-2000シーズンも含ンで数えても良い）３連覇を達成した球団はどこ？',
    ('','ロサンゼルスレイカーズ','ボストンセルティックス','ゴールデンステイトウォリアーズ','マイアミヒート'))
    if ans11=='ロサンゼルスレイカーズ':
        cnt+=2

    st.subheader('第12問')
    ans12=st.selectbox('コービーブライアントは現役時代、何度シーズンMVPを獲得したでしょう',
    ('','1','2','3','4'))
    if ans12=='1':
        cnt+=2

    st.subheader('第13問')
    ans13=st.selectbox('2010年代のマイアミヒートの3連覇を阻んだチームはどこでしょう',
    ('','ゴールデンステイトウォリアーズ','サンアントニオスパーズ','ボストンセルティックス','オクラホマシティサンダー'))
    if ans13=='サンアントニオスパーズ':
        cnt+=2

    st.subheader('第14問')
    ans14=st.selectbox('2009年ドラフトで1巡目1位指名を受けたのは誰？',
    ('','ジェームスハーデン','ステフィンカリー','ブレイクグリフィン','リッキールビオ'))
    if ans14=='ブレイクグリフィン':
        cnt+=2

    st.subheader('第15問')
    ans15=st.selectbox('カワイレナードが初めてFMVPを獲得したシーズンは？',
    ('','2013-14','2014-15','2018-19','2019-20'))
    if ans15=='2013-14':
        cnt+=2

    st.subheader('第16問')
    ans16=st.selectbox('マイアミヒートが初めて優勝した時のファイナルの相手は？',
    ('','サンアントニオスパーズ','ダラスマーベリックス','オクラホマシティサンダー','ユタジャズ'))
    if ans16=='ダラスマーベリックス':
        cnt+=2

    st.subheader('第17問')
    ans17=st.selectbox('2003年でドラフト指名されたレブロンジェームス、ドウェインウェイド、クリスボッシュ、カーメロアンソニーの中で最初に優勝したのは誰？',
    ('','レブロンジェームス','ドウェインウェイド','クリスボッシュ','カーメロアンソニー'))
    if ans17=='ドウェインウェイド':
        cnt+=2

    st.subheader('第18問')
    ans18=st.selectbox('2006-07ファイナルでFMVPを獲得したのは誰？',
    ('','ティムダンカン','トニーパーカー','ポールピアース','コービーブライアント'))
    if ans18=='トニーパーカー':
        cnt+=2


    st.subheader('第19問')
    ans19=st.selectbox('ポールジョージがNBAに入ってから数年つけていた13の前の背番号は？',
    ('','23','24','33','34'))
    if ans19=='24':
        cnt+=2

    st.subheader('第20問')
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('melo.png', use_column_width=True)
    ans20=st.selectbox('このロゴは誰のものでしょう？',
    ('','ロンゾボール','カーメロアンソニー','ラメロボール','ジェイソンテイタム'))
    if ans20=='カーメロアンソニー':
        cnt+=2

    st.subheader('第21問')
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('klay.png',use_column_width=True)
    ans21=st.selectbox('このロゴは誰のものでしょう？',
    ('','カイリーアービング','クリスミドルトン','カイルラウリー','クレイトンプソン'))
    if ans21=='クレイトンプソン':
        cnt+=2

    st.subheader('第22問')
    ans22=st.selectbox('ジミーバトラー、ウェスリーマシューズ、ジェイクラウダーの出身大学は？',
    ('','UCLA','マーケット大学','ケンタッキー大学','ミシガン大学'))
    if ans22=='マーケット大学':
        cnt+=2

    st.subheader('第23問')
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('mas.jpg',use_column_width=True)
    ans23=st.selectbox('どのチームのマスコットでしょう？',
    ('','ロサンゼルスレイカーズ','インディアナペイサーズ','ゴールデンステイトウォリアーズ','デンバーナゲッツ'))
    if ans23=='デンバーナゲッツ':
        cnt+=2

    st.subheader('第24問')
    ans24=st.selectbox('NBA史上で最もトレードされた回数が多い選手は？',
    ('','サムキャセール','トレバアリーザ','マーカスキャンビー','デールエリス'))
    if ans24=="トレバアリーザ":
        cnt+=2

    st.subheader('第25問')
    ans25=st.selectbox('NBAのロゴになっている選手は誰？',
    ('','ジェリーウェスト','ウィリスリード','ジョンハブリチェック','ウィルトチェンバレン'))
    if ans25=='ジェリーウェスト':
        cnt+=2

    st.subheader('第26問')
    ans26=st.selectbox('NBAが使用しているバスケットボールの大きさは？',
    ('','6号','6.5号','7号','8号'))
    if ans26=='6.5号':
        cnt+=2

    st.subheader('第27問')
    ans27=st.selectbox('2010/01/01 ~ 2019/12/31の期間で最も勝利数が多いのはどのチームでしょう',
    ('','ゴールデンステイトウォリアーズ','オクラホマサンダー','サンアントニオスパーズ','マイアミヒート'))
    if ans27=='サンアントニオスパーズ':
        cnt+=2

    st.subheader('第28問')
    ans28=st.selectbox('2010/01/01 ~ 2019/12/31の期間で2番目に勝利数が多いのはどのチームでしょう',
    ('','ゴールデンステイトウォリアーズ','オクラホマシティサンダー','サンアントニオスパーズ','マイアミヒート'))
    if ans28=='オクラホマシティサンダー':
        cnt+=2

    st.subheader('第29問')
    ans29=st.selectbox('2010年代の勝利数が多い1位はレブロンジェームス、3位はジェームスハーデン、では2位は？',
    ('','ケビンデュラント','アンドレイグダーラ','ラッセルウェストブルック','サージイバカ'))
    if ans29=='サージイバカ':
        cnt+=2

    st.subheader('第30問')
    ans30=st.selectbox('2010/01/01 ~ 2019/12/31の期間で最も勝利数が少ないのはどのチームでしょう',
    ('','ミネソタティンバーウルブズ','サクラメントキングス','デトロイトピストンズ','クリーブランドキャバリアーズ'))
    if ans30=='サクラメントキングス':
        cnt+=2

    st.subheader('第31問')
    ans31=st.selectbox('球団設立から現在までで、最も勝利数が少ないのはどのチームでしょう',
    ('','オーランドマジック','ロサンゼルスクリッパーズ','ワシントンウィザーズ','ミネソタティンバーウルブズ'))
    if ans31=='ミネソタティンバーウルブズ':
        cnt+=2

    st.subheader('第32問')
    ans32=st.selectbox('2021/08/18の時点でTwitterのフォロワー数が最も多いのはレイカーズ、では第2位は？',
    ('','ニューヨークニックス','マイアミヒート','ボストンセルティックス','ゴールデンステイトウォリアーズ'))
    if ans32=='ゴールデンステイトウォリアーズ':
        cnt+=2

    st.subheader('第33問')
    ans33=st.selectbox('球団創設以来、一度もドラフト1巡目1位指名をしていないものの優勝を果たしたのはどのチームでしょう',
    ('','マイアミヒート','ゴールデンステイトウォリアーズ','フェニックスサンズ','シカゴブルズ'))
    if ans33=='マイアミヒート':
        cnt+=2

    st.subheader('第34問')
    ans34=st.selectbox('Sportsnetの解説者によってよく使われる"Captain Canada"とは誰のニックネームでしょう',
    ('','ケリーオリニク','スティーブナッシュ','アンドリューウィギンス','コリージョセフ'))
    if ans34=='スティーブナッシュ':
        cnt+=2

    st.subheader('第35問')
    ans35=st.selectbox('中国リーグへの移籍を機に"ザ・パンダズ・フレンド"に改名した選手は？',
    ('','メッタワールドピース','ランススティーブンソン','JRスミス','ジェレミーリン'))
    if ans35=='メッタワールドピース':
        cnt+=2

    st.subheader('第36問')
    ans36=st.selectbox('1971年にロサンゼルスレイカーズが記録した、現在でも上回られていない最長連勝記録は何連勝でしょう',
    ('','31','32','33','34'))
    if ans36=='33':
        cnt+=2

    st.subheader('第37問')
    ans37=st.selectbox('1シーズンでテクニカルファールを最も取られたのは誰？',
    ('','デマーカスカズンズ','デニスロッドマン','ラシードウォーレス','ケビンガーネット'))
    if ans37=='ラシードウォーレス':
        cnt+=2

    st.subheader('第38問')
    ans38=st.selectbox('2021/09/21の時点で現役の選手の中で、最も通算出場時間が長いのは誰？',
    ('','レブロンジェームス','カーメロアンソニー','ケビンデュラント','ラッセルウェストブルック'))
    if ans38=='レブロンジェームス':
        cnt+=2

    st.subheader('第39問')
    ans39=st.selectbox('White Chocolateの愛称で親しまれた選手は？',
    ('','マイクビビー','ジョンストックトン','ジェイソンウィリアムズ','クリスマリン'))
    if ans39=='ジェイソンウィリアムズ':
        cnt+=2

    st.subheader('第40問')
    col1,col2,col3=st.columns(3)
    with col1:
        st.image('tatoo.jpg', use_column_width=True)
    ans40=st.selectbox('誰のタトゥーでしょう',
    ('','KCP','アンソニーデイビス','レブロンジェームス','ドワイトハワード'))
    if ans40=='アンソニーデイビス':
        cnt+=2

    st.subheader('第41問')
    ans41=st.selectbox('ウォリアーズが73-9でシーズンを終えた2015-16シーズン、73勝目をかけた最終戦の相手は？',
    ('','メンフィスグリズリーズ','ニューオリンズペリカンズ','アトランタホークス','インディアナペイサーズ'))
    if ans41=='メンフィスグリズリーズ':
        cnt+=2

    st.subheader('第42問')
    ans42=st.selectbox('ビンスカーターとトレイシーマグレディの関係は？',
    ('','同じ高校','同じ大学','親戚','同じ病院で生まれた'))
    if ans42=='親戚':
        cnt+=2

    st.subheader('第43問')
    ans43=st.selectbox('NBAの長い歴史で唯一、引退後にファン投票でオールスターゲームに出場した選手は誰？',
    ('','マイケルジョーダン','マジックジョンソン','シャキールオニール','ビルラッセル'))
    if ans43=='マジックジョンソン':
        cnt+=2

    st.subheader('第44問')
    ans44=st.selectbox('在籍したことがないにも関わらず、マイケルジョーダンの背番号を永久欠番にしている球団は？',
    ('','マイアミヒート','ロサンゼルスレイカーズ','ボストンセルティックス','ダラスマーベリックス'))
    if ans44=='マイアミヒート':
        cnt+=2

    st.subheader('第45問')
    ans45=st.selectbox('"Three-peat"（3連覇を意味する）という言葉の生みの親は誰でしょう？',
    ('','マイケルジョーダン','フィルジャクソン','ビルラッセル','パットライリー'))
    if ans45=='パットライリー':
        cnt+=2

    st.subheader('第46問')
    ans46=st.selectbox('NBA 2K13のパッケージを飾ったのは、ブレイクグリフィン、ケビンデュラント、あと一人は誰でしょう？',
    ('','レブロンジェームス','ポールジョージ','デリックローズ','ステフィンカリー'))
    if ans46=='デリックローズ':
        cnt+=2

    st.subheader('第47問')
    ans47=st.selectbox('NBA 2K14 ~ 2K18の4年（2K16は除く）（20周年版のも含めると2K19までの5年間）続いたジンクスとは？',
    ('','パッケージの選手が移籍','パッケージの選手がシーズンMVPを獲得','パッケージの選手がオールスターMVP獲得','パッケージの選手が所属するチームがファイナルへ到達（優勝するとは限らないが）'))
    if ans47=='パッケージの選手が移籍':
        cnt+=2

    st.subheader('第48問')
    ans48=st.selectbox('NBA 2Kにおいて99 OVRを獲得した選手は歴代で6人いますが、現役ではレブロンとあと一人います。誰でしょう？',
    ('','ケビンデュラント','デリックローズ','ステフィンカリー','クリスポール'))
    if ans48=='クリスポール':
        cnt+=2

    st.subheader('第49問')
    ans49=st.selectbox('NBAが創設されてから2021-22シーズンで何年目になる？',
    ('','55','75','100','125'))
    if ans49=='75':
        cnt+=2

    st.subheader('第50問')
    ans50=st.selectbox('NBAは好きですか？',
    ('','大好きです最高！','まぁまぁ好きかな','普通','嫌い'))
    if ans50=='大好きです最高！':
        cnt+=2

    st.subheader('-------------------------------------------------------------------------------')
    st.write('これで全問終了です。すべて解き終わりましたら下の採点ボタンを押してください。')
    st.write('80点以上：殿堂入りクラス')
    st.write('60点以上80点未満：オールスターレベル')
    st.write('40点以上60点未満：スーパースターレベル')
    st.write('20点以上40点未満：プロレベル')
    st.write('20点未満：ルーキーレベル')
    if st.button('採点'):
        if cnt>=80:
            st.balloons()
            st.header('おめでとうございます。')
            st.header(f'あなたは{cnt}点で殿堂入りレベルです！！！！')
        elif 60<=cnt<80:
            st.balloons()
            st.header('おめでとうございます。')
            st.header(f'あなたは{cnt}点でスーパースターレベルです！！！')
        elif 40<=cnt<60:
            st.balloons()
            st.header('おめでとうございます。')
            st.header(f'あなたは{cnt}点でオールスターレベルです！！')
        elif 20<=cnt<40:
            st.balloons()
            st.header('おめでとうございます。')
            st.header(f'あなたは{cnt}点でプロレベルです！')
        else:
            st.balloons()
            st.header('おめでとうございます。')
            st.header(f'あなたは{cnt}点でルーキーレベルです。今後もNBAを楽しんでいきましょう！！')

        if cnt!=100:
            st.write('(不正解だった問題のみ解答を表示します。)')
            if ans1!='6':
                st.write('第1問：6')
            if ans2!='30':
                st.write('第2問：30')
            if ans3!='トロント':
                st.write('第3問：トロント')
            if ans4!='ステフィンカリー':
                st.write('第4問：ステフィンカリー')
            if ans5!='ルカドンチッチ':
                st.write('第5問：ルカドンチッチ')
            if ans6!='ネッツ':
                st.write('第6問：ネッツ')
            if ans7!='ロサンゼルスレイカーズ':
                st.write('第7問：ロサンゼルスレイカーズ')
            if ans8!='ジェームスハーデン':
                st.write('第8問：ジェームスハーデン')
            if ans9!='ヤニスアデトクンポ':
                st.write('第9問：ヤニスアデトクンポ')
            if ans10!='ケビンデュラント':
                st.write('第10問：ケビンデュラント')
            if ans11!='ロサンゼルスレイカーズ':
                st.write('第11問：ロサンゼルスレイカーズ')
            if ans12!='1':
                st.write('第12問：1')
            if ans13!='サンアントニオスパーズ':
                st.write('第13問：サンアントニオスパーズ')
            if ans14!='ブレイクグリフィン':
                st.write('第14問：ブレイクグリフィン')
            if ans15!='2013-14':
                st.write('第15問：2013-14')
            if ans16!='ダラスマーベリックス':
                st.write('第16問：ダラスマーベリックス')
            if ans17!='ドウェインウェイド':
                st.write('第17問：ドウェインウェイド')
            if ans18!='トニーパーカー':
                st.write('第18問：トニーパーカー')
            if ans19!='24':
                st.write('第19問：24')
            if ans20!='カーメロアンソニー':
                st.write('第20問：カーメロアンソニー')
            if ans21!='クレイトンプソン':
                st.write('第21問：クレイトンプソン')
            if ans22!='マーケット大学':
                st.write('第22問：マーケット大学')
            if ans23!='デンバーナゲッツ':
                st.write('第23問：デンバーナゲッツ')
            if ans24!='トレバアリーザ':
                st.write('第24問：トレバアリーザ')
            if ans25!='ジェリーウェスト':
                st.write('第25問：ジェリーウェスト')
            if ans26!='6.5号':
                st.write('第26問：6.5号')
            if ans27!='サンアントニオスパーズ':
                st.write('第27問：サンアントニオスパーズ')
            if ans28!='オクラホマシティサンダー':
                st.write('第28問：オクラホマシティサンダー')
            if ans29!='サージイバカ':
                st.write('第29問：サージイバカ')
            if ans30!='サクラメントキングス':
                st.write('第30問：サクラメントキングス')
            if ans31!='ミネソタティンバーウルブズ':
                st.write('第31問：ミネソタティンバーウルブズ')
            if ans32!='ゴールデンステイトウォリアーズ':
                st.write('第32問：ゴールデンステイトウォリアーズ')
            if ans33!='マイアミヒート':
                st.write('第33問：マイアミヒート')
            if ans34!='スティーブナッシュ':
                st.write('第34問：スティーブナッシュ')
            if ans35!='メッタワールドピース':
                st.write('第35問：メッタワールドピース')
            if ans36!='33':
                st.write('第36問：33')
            if ans37!='ラシードウォーレス':
                st.write('第37問：ラシードウォーレス')
            if ans38!='レブロンジェームス':
                st.write('第38問：レブロンジェームス')
            if ans39!='ジェイソンウィリアムズ':
                st.write('第39問：ジェイソンウィリアムズ')
            if ans40!='アンソニーデイビス':
                st.write('第40問：アンソニーデイビス')
            if ans41!='メンフィスグリズリーズ':
                st.write('第41問：メンフィスグリズリーズ')
            if ans42!='親戚':
                st.write('第42問：親戚')
            if ans43!='マジックジョンソン':
                st.write('第43問：マジックジョンソン')
            if ans44!='マイアミヒート':
                st.write('第44問：マイアミヒート')
            if ans45!='パットライリー':
                st.write('第45問：パットライリー')
            if ans46!='デリックローズ':
                st.write('第46問：デリックローズ')
            if ans47!='パッケージの選手が移籍':
                st.write('第47問：パッケージの選手が移籍')
            if ans48!='クリスポール':
                st.write('第48問：クリスポール')
            if ans49!='75':
                st.write('第49問：75')
            if ans50!='大好きです最高！':
                st.write('第50問：大好きです最高！')