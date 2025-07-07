import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

gemini_token = os.getenv('gemini_api')
weather_token = os.getenv('weatherstack_api')

genai.configure(api_key=gemini_token)

# gemini_model = "gemini-2.0-flash-lite"

def load_model():
    '''This function uses Google's Generative AI library's GenerativeModel()
     function to load the user specified model (in this case Gemini 2.0 Flash Lite)'''

    gemini_model = "gemini-2.0-flash-lite"
    return genai.GenerativeModel(model_name=gemini_model)

def extract_city(user_query):
    '''This function uses an LLM model to extract the city name from the
    user query which is about the weather of a specific city'''

    llm = load_model()
    prompt = f'''
    The query below contains a city name in it, extract the city name from the user query about weather:
    Query = "{user_query}"
    Only extract the city name and nothing else. Do not include any extra text or examples.'''
    response = llm.generate_content(prompt)
    city = response.text.strip()

    return city

def get_weather(city):
    '''This function uses the weatherstack api to fetch the weather data
    about the city requested in the user query'''

    url = f"http://api.weatherstack.com/current?access_key={weather_token}&query={city}"
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        if "current" in data: return data
        elif "error" in data: return {"error": f"API Error: {data['error']['info']}"}
    return {"error": "Failed to fetch weather data. Check API key or city name."}

def generate_response(weather_data, user_query):
    '''This function uses the llm, extracted weather data and user query
    to generate a response for the user query'''

    if "error" in weather_data: return weather_data['error']

    llm = load_model()

    prompt_template = f'''
    You are an advanced weather assistant. Answer the user's query based on the following weather data.
    Weather data: {weather_data}
    User query: {user_query}
    Generate a helpful and natural response aligning to the user query'''

    response = llm.generate_content(prompt_template)
    return response.text.strip()

'''
if __name__ == "__main__":
    query = ""
    while query != "//":
        query = input('Enter Query (type // to exit) : ')
        if query == "//":
            break
        city = extract_city(query)
        weather_details = get_weather(city)
        bot_response = generate_response(weather_details, query)
        print(bot_response)
'''
#streamlit UI in app.py