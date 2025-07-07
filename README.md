# WeatherBot – AI Powered Weather Assistant

WeatherBot is an intelligent chatbot that provides real-time weather information for any city. It uses **Google’s Gemini LLM** to understand natural language queries and the **Weatherstack API** to fetch accurate weather data. The chat interface is built using **Streamlit** for a sleek, simple and interactive experience.

---

## Features

- **LLM-Powered Query Understanding**  
  Understands natural language queries like _“What's the weather in Mumbai?”_ using Gemini.

- **Real-Time Weather Data**  
  Retrieves live weather data from the [Weatherstack API](https://weatherstack.com/).

- **Interactive Chat Interface**  
  Built with Streamlit’s chat UI for an intuitive and responsive user experience.

---
## Setup Instructions


### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/weather-bot.git
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
gemini_api=your_gemini_api_key_here
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

* Python (3.11 used in this project)
* [Streamlit](https://streamlit.io/)
* [Google Generative AI SDK](https://ai.google.dev/)
* [Weatherstack API](https://weatherstack.com/)

---

## Author

**Chinmay Kanawade**
*AI/ML Engineer.*
[GitHub](https://github.com/ChinmayKanawade10) 