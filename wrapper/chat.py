import os
import openai
from api.validate import num_tokens_from_string

import logging
logger = logging.getLogger(__name__)

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

class ChatPrompt:
    def __init__(self, temperature: float):
        openai.api_key = get_file_contents(".open_ai_key")

        self.chat_model_id = "gpt-3.5-turbo"
            
        self.temperature = temperature
        self.max_tokens = 2048
        self.top_p = 1
        self.time_out = 7
    
    def run(self, prompt):
        return self._post_request_chat(prompt)

    def _post_request_chat(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model=self.chat_model_id,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                frequency_penalty=0,
                presence_penalty=0
            )
            res = response['choices'][0]['message']['content']
            logger.debug(response)
            return res, True
        except Exception as e:
            logger.debug(e)
            return "", False