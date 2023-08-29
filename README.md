# NashArt Discord Bot - Your 24/7 Art Assistant

NashArt is a powerful Discord bot designed to serve as your art assistant, capable of answering a wide range of art-related questions using the advanced GPT-3.5 language model. With NashArt, you can get instant responses to your queries, advice on artistic techniques, information about famous artists and artworks, and much more. The bot ensures user privacy by utilizing discord-interactions, making questions visible only upon user interaction.

## Developed by Team Nash

NashArt is a product of collaborative effort by a team of passionate developers, each contributing their unique expertise:

- **N** - [Najeeb](https://github.com/naa7)
- **A** - [Andy](https://github.com/Falselysium)
- **S** - [Sung](https://github.com/syi7190)
- **H** - [Haad](https://github.com/boolgerand5)

The name "Nash" is derived from the first initial of each developer's first name, with "Art" added to create the distinctive name for this innovative bot.

## Setup Instructions

Follow these steps to set up NashArt on your system:

1. Clone the repository on your Windows machine:

    ```
    git clone https://github.com/naa7/NashArt
    ```

2. Navigate to the cloned repository:

    ```
    cd NashArt
    ```

3. Set up the virtual environment:
 
    ```
    python3 -m venv env
    ```
4. Activate the virtual environment:
- Linux & MacOS
  
    ```
    source env/bin/activate
    ```
- Windows
  
    ```
    .\env\Scripts\activate
    ```

    If you encounter an Execution Policy Warning, run PowerShell as Administrator and use the following command:

    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

5. Install required dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Create an `.env` file in the root directory and store your Discord Token:

    ```
    # environment variables defined inside .env file
    DISCORD_TOKEN="YOUR_DISCORD_TOKEN"
    ```

7. Run the bot:

    ```
    python bot.py
    ```

## Discord Commands

NashArt provides the following commands to interact with the bot:

- `/tts-ask 'prompt'`: Asks a question using text-to-speech.
- `/ask 'prompt'`: Asks a question using regular text input.

**Example Usage:**

```
/ask Who painted the Mona Lisa?
```

![Mona Lisa](Example.png)

Feel free to ask anything art-related, and NashArt will provide you with insightful and informative responses.

---
By implementing NashArt as your dedicated art assistant using GPT-3.5, you can elevate your artistic journey with instant, 24/7 access to art-related knowledge and guidance.
