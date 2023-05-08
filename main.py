from wrapper.chat import ChatPrompt
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    prompter = ChatPrompt(0.7)
    messages = [
        {'role': 'user', 'content': "What's 1+1? Answer in one word."}
    ]
    output = prompter.run(messages)
    logger.info(output)