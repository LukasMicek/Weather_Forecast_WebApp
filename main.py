import streamlit as st
import plotly.express as px
from beckend import get_data

# Title, text input, slider, select box and subheader
st.title("Weather Forecast for 5 days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Get temp/sky data from the API
if place:
    try:
        data = get_data(place, days)
        match option:
            # Create temp plot
            case "Temperature":
                t = [dict["main"]["temp"] for dict in data]
                d = [dict["dt_txt"] for dict in data]
                figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)
            # Create images of the sky
            case "Sky":
                sky = [dict["weather"][0]["main"] for dict in data]
                images = {"Clear"}
                for i in sky:
                    st.image(f"images/{i.lower()}.png", width=115)
    except KeyError:
        st.error("This place not exists")
