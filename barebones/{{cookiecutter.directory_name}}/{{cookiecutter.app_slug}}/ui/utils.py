"""UI utility functions"""

def encode_state(state: dict):
    """Encode the state of filters into a Base64 encoded string so
    it can be stored in the URL"""
    from base64 import b64encode
    import json
    state_as_string = json.dumps(state)
    state=b64encode(state_as_string.encode()).decode()
    return state


def decode_state(encoded_state_string: str):
    """Decode state from a """
    from base64 import b64decode
    import json

    if encoded_state_string is None or encoded_state_string == "":
        return {}
    else:
        try:
            decoded_state_string = b64decode(encoded_state_string).decode()
            state = json.loads(decoded_state_string)
        except (UnicodeDecodeError, json.decoder.JSONDecodeError):
            return {}
        else:
            return state
