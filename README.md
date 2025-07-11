# WeatherBot – AI Powered Weather Assistant

WeatherBot is an intelligent chatbot that provides real-time weather information for any city. It uses **Google’s Gemma LLM** to understand natural language queries and the **Weatherstack API** to fetch accurate weather data. The chat interface is built using **Streamlit** for a sleek, simple and interactive experience.

---

## Features

- **LLM-Powered Query Understanding :**  
  Understands natural language queries like _“What's the weather in Mumbai?” or "Shall I carry an umbrella in London?"_ using [Google's Gemma-3 model](https://huggingface.co/google/gemma-3-1b-it).

- **Real-Time Weather Data :**  
  Retrieves live weather data from the [Weatherstack API](https://weatherstack.com/).

- **Interactive Chat Interface :**  
  Built with Streamlit’s chat UI for an intuitive and responsive user experience.

---
## Setup Instructions


### 1. Clone the Repository

```bash
git clone https://github.com/ChinmayKanawade10/weather-bot.git
cd weather-bot
````

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

In the root directory, create a `.env` file and add your API keys:

```env
weatherstack_api=your_weatherstack_api_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```
---

## Example Query

> *"Can you tell me the weather in Tokyo today?"*

WeatherBot will extract **Tokyo**, fetch the current weather, and respond with a natural-sounding summary.

> *"Is it raining in New York?"*

WeatherBot will extract **New York** and it's current weather, and answer whether it is raining in New York or not.

---

## Requirements

* Python (python-3.11 used in this project)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/index)
* [Streamlit](https://streamlit.io/)
* [Weatherstack API](https://weatherstack.com/)

---

## NOTE
The above project was designed to use the "gemma-3-1b-it" model locally by downloading it in local machine and placing the necessary files inside a gemma-3-model directory in the main project directory !!
If you want to use Hugging Face Token to make API calls to Hugging Face Hub and communicate with "gemma-3-1b-it" model, make the following changes in the model setup code in 'bot.py'

```bash
hugging_face_token = os.getenv('huggingface_api')
gemma_model = 'google/gemma-3-1b-it'
tokenizer = AutoTokenizer.from_pretrained(gemma_model, token=hugging_face_token)
model = AutoModelForCausalLM.from_pretrained(gemma_model, token=hugging_face_token, device_map='auto')
llm_pipeline = pipeline('text_generation', model=model, tokenizer=tokenizer)
```

Also create a Hugging Face Token on https://huggingface.co/ and update the .env file as 
```env
huggingface_api=your_huggingface_token_here
weatherstack_api=your_weatherstack_api_key_here
```

---

## Author

**Chinmay Kanawade.**
*AI/ML Engineer.*
[GitHub](https://github.com/ChinmayKanawade10) 
