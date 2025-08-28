# Flirty Bertie

Flirty Bertie is a playful, emoji-loving chatbot powered by [Groq’s LLaMA 3 API](https://console.groq.com). 



## Features

- Witty, respectful flirty persona
- Randomized greetings and emoji reactions
- Easter eggs for special prompts (`compliment`, `rose`)
- Chat context awareness via `messages` memory
- Written in Python with `.env` support for secure API keys



## Usage

### 1. Clone the repo

```bash
git clone https://github.com/joyyy-99/Flirty-Bertie.git
cd Flirty-Bertie
````

### 2. Install dependencies

```bash
pip install python-dotenv groq
```

### 3. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the bot

```bash
python main.py
```


## Easter Eggs

* Type `compliment` for some Bertie-approved praise.
* Type `rose` to get a 🌹 just for you.
* Type `exit` to leave... if you can handle the heartbreak 💔.



## Model Info

* **Model**: `llama3-8b-8192` via Groq API
* **Framework**: Python (CLI)
* **Hosting**: Local (no server required)


## Future Ideas

* Add voice support (Text-to-Speech)
* Deploy as a web app
* More personality presets (Sassy Stella? Nerdy Ned?)


