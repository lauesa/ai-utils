import tiktoken

def num_tokens_from_string(string: str, model: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens

if __name__ == "__main__":
    encoding_name = "gpt-3.5-turbo"

    print(num_tokens_from_string("That's a very nice cat!", encoding_name))