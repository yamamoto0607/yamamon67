import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
st.title('ラーメン記録簿')
st.write('食べたラーメンを記録しておくアプリです。')
name= st.text_input('行ったお店の名前')
menu= st.text_input('頼んだラーメン')
price= float(st.number_input('価格（税込）') )
menn = st.selectbox('麺は？',list(['極太麵','太麺','中太麺','中細麵''細麵','極細麺']))
soup = st.selectbox('味は？',list(['醤油','味噌','塩','豚骨','白湯系','魚介系','油そば','その他']))
if soup =='その他':
    soup2= st.text_input('その他（書き込み）')
ingredients = st.multiselect('具材は？',
                             ['焼豚','鶏肉','海苔','ねぎ','白髪ねぎ','メンマ','ほうれん草','卵','キャベツ','もやし','ナルト','紅ショウガ','コーン','バター','高菜','その他']
                             )
comment= st.text_area('感想')
left_column,right_column = st.columns(2)
button= right_column.button('確定')

land_marks = pd.DataFrame(
    data=[[36.65139,138.18111],
          [36.64354,138.18777],
          [36.65711,138.18139],
          [36.63098,138.18891],
          [36.61457,138.15137],
          [36.57684,138.19971]],
    index=["県庁","長野駅","信大（教）",'信大（工）','川中島駅','長野IC'],
    columns=["x","y"])

def AreaMarker(df,m):
    for index, r in df.iterrows(): 
        folium.Marker(
            location=[r.x, r.y],
            popup=index,
        ).add_to(m)
        folium.Circle(
            location=[r.x, r.y],
            popup=index,
            color="yellow",
            fill=True,
            fill_opacity=0.07
        ).add_to(m)
name2 = ('行ったお店は'+ name)
order = ( menu +'を頼んだ'+'('+ str(price)+'円)')
col1, col2 = st.columns(2)
if  button == True:
    col1.write('お店のデータ')
    col1.write( name2 )
    col1.write(order)
    col2.write('ラーメンのデータ')
    col2.write(menn)
    if soup=='その他':
        col2.write(soup2)
    else:
        col2.write(soup)
    col2.write(ingredients)
    st.write( comment )
    st.write('スクリーンショットで記録しましょう！')

st.title("地図") 
st.write('大体の場所を記録しましょう')
m = folium.Map(location=[36.65139,138.18111], zoom_start=14)
AreaMarker(land_marks,m)
folium_static(m) 

st.title('明日も美味しいラーメンを探しましょう。')
