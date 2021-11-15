import streamlit as st
st.title('ラーメン記録簿')
st.write('説明')
name= st.text_input('行ったお店の名前')
menu= st.text_input('頼んだメニュー')
price= float(st.number_input('価格（税込）') )
comment= st.text_input('感想')
left_column,right_column = st.columns(2)
button= right_column.button('確定')
if  button == True:
    st.write('行ったお店は''name')
    st.write('menu''を頼んだ''(''price'')')
    st.write('comment')
    

