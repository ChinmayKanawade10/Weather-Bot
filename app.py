import os
from dotenv import load_dotenv
import streamlit as st
import bot
# from bot import extract_city, get_weather, generate_response

load_dotenv()

weather_token = os.getenv('weatherstack_api')

#STREAMLIT UI
st.title("🌦️ Weather-Bot")
st.subheader("Get your weather report!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

user_query = st.chat_input("Ask about the weather...")

if user_query:
    st.chat_message("user").markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    city = bot.extract_city(user_query)
    weather_details = bot.get_weather(city)
    bot_response = bot.generate_response(weather_details, user_query)

    st.chat_message("assistant").markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})