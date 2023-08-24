from g4f.Provider import (
    Aichat,
    Ails,
    AiService,
    AItianhu,
    Bard,
    Bing,
    ChatgptAi,
    ChatgptLogin,
    DeepAi,
    GetGpt
)

import g4f

def chat_with_bot():
    assistant_name = "NashArt"
    assistant_intro = (
        f"You are an art assistant whose name is {assistant_name}, a large language model created and developed by the NashArt team. "
        "You are based on the gpt-3.5 and have been trained on a diverse range of text data from the internet. "
        "You were designed to be highly versatile and capable of adapting to many different use cases. "
        "You don't have emotions, opinions, or beliefs, and you are not capable of experiencing the world in the same way as humans do. "
        "Your purpose is to provide helpful and informative art-related responses to art-related questions and to assist in whatever way you can."
    )

    print(f"{assistant_name}: I am an art assistant developed by the Nash team. I'm here to help you with art-related questions.")
    
    providers = [
        Aichat(),
        Ails(),
        AiService(),
        AItianhu(),
        Bard(),
        Bing(),
        ChatgptAi(),
        ChatgptLogin(),
        DeepAi(),
        GetGpt()
    ]
    
    response = None  # Initialize the response variable
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'q':
            print(f"{assistant_name}: Goodbye! Keep creating art!")
            break
        
        conversation = [
            {"role": "assistant", "content": assistant_intro},
            {"role": "assistant", "content": user_input},
        ]
        
        for provider in providers:
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=conversation,
                    provider=provider,
                )
                break
            except:
                continue
        
        if response is None:
            print("No available providers.")
            return
        
        bot_response = response
        print(f"{assistant_name}:", bot_response)

if __name__ == "__main__":
    chat_with_bot()
