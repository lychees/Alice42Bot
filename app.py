from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests
import json
from telegram import ChatAction
import os

def hello(update: Update, context: CallbackContext) -> None:
    intro_text = """
    🤖 Greetings human! \n
🤗 I'm a bot hosted on Hugging Face Spaces. \n
🦾 I can query the mighty GPT-J-6B model and send you a response here. Try me.\n
✉️ Send me a text to start and I shall generate a response to complete your text!\n\n
‼️ PS: Responses are not my own (everything's from GPT-J-6B). I'm not conscious (yet).\n
Blog post: https://dicksonneoh.com/portfolio/deploy_gpt_hf_models_on_telegram/
    """
    update.message.reply_text(intro_text)

def get_gpt_response(text):
    r = requests.post(
        url="https://hf.space/embed/dnth/gpt-j-6B/+/api/predict/",
        json={"data": [text]},
    )
    response = r.json()
    return response["data"][0]

API_URL = "https://api-inference.huggingface.co/models/mio/amadeus"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    print(payload)
    response = requests.post(API_URL, headers=headers, json=json.dumps(payload))
    return response.json()    

def respond_to_user(update: Update, context: CallbackContext):
    update.message.chat.send_action(action=ChatAction.TYPING)
    # response_text = get_gpt_response(update.message.text)
    response_text = query({"inputs:": update.message.text})
    # print(response_text)
    # update.message.chat.send_audio(audio=response_text)
    update.message.reply_text(response_text)

updater = Updater(os.environ['telegram_token'])
updater.dispatcher.add_handler(CommandHandler("start", hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_user))
updater.start_polling()
updater.idle()

