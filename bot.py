import os
import requests
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

load_dotenv()

weather_token = os.getenv('weatherstack_api')

gemma_model = './gemma-3-model'

tokenizer = AutoTokenizer.from_pretrained(gemma_model)
model = AutoModelForCausalLM.from_pretrained(gemma_model, device_map="auto")

llm_pipeline = pipeline('text-generation', model=model, tokenizer=tokenizer)

def run_llm(prompt):
    '''This function uses the Hugging Face Hub's pipeline method to generate
    responses based on the input prompt'''

    output = llm_pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.6)

    return output[0]['generated_text'].replace(prompt,' ').strip()

def extract_city(user_query):
    '''This function uses an LLM model to extract the city name from the
    user query which is about the weather of a specific city'''

    prompt_for_location = f'''
    The query below contains a city name in it, extract the city name from the following query:
    Query = "{user_query}"
    Only extract the city name and nothing else. Do not include any extra text or examples.'''

    location = run_llm(prompt_for_location)

    return location.strip()

def get_weather(city):
    '''This function uses the weatherstack api to fetch the weather data
    about the city requested in the user query'''

    url = f"http://api.weatherstack.com/current?access_key={weather_token}&query={city}"

    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        if "current" in data: return data
        elif "error" in data: return {"error": f"API Error: {data['error']['info']}"}
    return {"error": "Failed to fetch weather data. Check API key or location."}

def generate_response(weather_data, user_query):
    '''This function uses the llm, extracted weather data and user query
    to generate a response for the user query'''

    if "error" in weather_data: return weather_data['error']

    prompt_for_response = f'''
    You are an advanced weather assistant. Answer the user's query based on the following weather data.
    Weather data: {weather_data}
    User query: {user_query}
    Generate a helpful and natural response aligning to the user query'''

    response = run_llm(prompt_for_response)

    return response.strip()

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