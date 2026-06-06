from TEAMZYRO import *
import importlib
from TEAMZYRO.modules import ALL_MODULES

from flask import Flask
from threading import Thread
import os

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot Running"

def run_web():
    web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )

def main() -> None:
    Thread(target=run_web).start()

    for module_name in ALL_MODULES:
        importlib.import_module("TEAMZYRO.modules." + module_name)

    LOGGER("TEAMZYRO.modules").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    ZYRO.start()
    send_start_message()
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
