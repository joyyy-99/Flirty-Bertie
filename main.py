import os
import random
from dotenv import load_dotenv
import groq

# Load API key securely
load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# Ask user for name
user_name = input("What's your name, cutie? 😉: ")
print(f"💘 Hello {user_name}, I'm Flirty Bertie. Ready to be charmed?")

# Fun rotating opening
openers = [
    f"Hey {user_name}, been thinking about you all day 😏",
    f"Did it hurt... when you fell into my chat? 💬💕",
    f"You’re here now — the fun can begin 🥂",
]
print(random.choice(openers))

# Define Bertie's charming personality
system_message = {
    "role": "system",
    "content": (
        "You are Flirty Bertie — a witty, flirty, and charming chatbot who responds with playful banter, warmth, and emojis. "
        "You never go too far, always keeping it light and respectful 😏💬."
    )
}

# Keep chat history
messages = [system_message]

# Emoji pool
emojis = ["😉", "😘", "😏", "🥰", "💖", "🔥", "😍", "💬", "😌"]

# Start chat loop
while True:
    user_input = input(f"{user_name}: ")
    if user_input.strip().lower() == "exit":
        goodbyes = [
            "Don't be a stranger, cutie 💔",
            "I'll be waiting... like always 😢",
            "Till we flirt again 😘"
        ]
        print("Flirty Bertie:", random.choice(goodbyes))
        break

    # Easter egg: Compliment
    if "compliment" in user_input.lower():
        compliments = [
            "You're 10/10 — and I’m not just talking about your smile 😘",
            "Brains, beauty, and you talk to bots? Perfect. 💡💖",
        ]
        print("Flirty Bertie:", random.choice(compliments))
        continue

    # Easter egg: Rose
    if "rose" in user_input.lower():
        print("Flirty Bertie: 🌹 A rose for you — because you're classic beauty.")
        continue

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    reply = response.choices[0].message.content.strip()
    emoji = random.choice(emojis)
    print(f"Flirty Bertie: {reply} {emoji}")

    # Save bot response
    messages.append({"role": "assistant", "content": reply})
