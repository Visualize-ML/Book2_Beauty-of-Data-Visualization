import plotly.express as px
import streamlit as st
df = px.data.iris()
features = df.columns[:4]



with st.sidebar:
    st.title('鸢尾花数据')
    x_col = st.radio('横轴', features)
    y_col = st.radio('纵轴', features)
    marginal_x = st.radio('横轴边缘', [ "histogram", "rug", "box", "violin"])
    marginal_y = st.radio('纵轴边缘', [ "histogram", "rug", "box", "violin"])
    


fig = px.scatter(df, x=x_col, y=y_col, color="species", 
                 marginal_x = marginal_x, 
                 marginal_y = marginal_y,
                 width = 650, height = 600)

st.plotly_chart(fig)


