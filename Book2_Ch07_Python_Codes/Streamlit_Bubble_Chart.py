import plotly.express as px
import streamlit as st

df = px.data.gapminder()
df.rename(columns = {'country':'country or territory'},inplace = True)
# 表头用词不准确

with st.sidebar:
    st.title('气泡图')

fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
           animation_frame="year", 
           animation_group="country or territory",
           size="pop", 
           color="continent", 
           hover_name="country or territory",
           log_x=True, 
           size_max=55, 
           range_x=[100,100000], 
           range_y=[25,90])

st.plotly_chart(fig)