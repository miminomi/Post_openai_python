import os

import openai
from dotenv import load_dotenv


# <-- グローバル環境変数を上書きします
load_dotenv(override=True)
load_dotenv(".env")

#APIキーの設定
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")
openai.api_key = OPEN_API_KEY

#Chatgptにリクエストする
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": "久保建英はすごいの？"
    },
    ],
)

print(response.choices[0]["message"]["content"].strip())