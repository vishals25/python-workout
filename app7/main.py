from matplotlib import dates
import streamlit as st
import plotly.express as px
from backend import get_data
import datetime

st.set_page_config(page_title="WEATHER FORECAST",page_icon="cloud")

st.header("Weather Forecast App")

place=st.text_input(label="Enter place:",placeholder="chennai",key="input_place")

days=st.slider(label="No of days:",min_value=1,max_value=5,help="Select number of days to be Forecasted in the webpage",key="days")

data_view=st.selectbox(label="select the data to view",options=["Temperature","Sky"],key="data_view")


if place:
    st.subheader(f"{data_view} for the next {days} in {place}")
    datas,dates=get_data(place,days,data_view)

    if data_view=="Temperature":

        datas=[(data-273) for data in datas]

        plotly=px.line(x=dates,y=datas,labels={'x':'Dates','y':'Temperature(c)'})

        st.plotly_chart(plotly)
    else:
        col = 1
        zone=0
        for i in range(days):
            st.markdown('---')
            st.markdown(f'## Day {i + 1}')
            st.markdown('---')
            col1, col2, col3, col4 = st.columns(4)
            columns = [col1, col2, col3, col4]
            
            for image, time in zip(datas[(i*8):(i+1)*8], dates[(i*8):(i+1)*8]):
                with columns[col - 1]:
                    if image == 'Clear':
                        st.image('images/clear.png')
                    elif image == 'Clouds':
                        st.image('images/cloud.png')
                    elif image == 'Rain':
                        st.image('images/rain.png')
                    elif image == 'Snow':
                        st.image('images/snow.png')
                        
                    st.write(image)
                    st.write(time)
                
                col = col % 4 + 1  # Move to the next column
                zone+=1
                if zone==8:
                    zone=0
                    break
