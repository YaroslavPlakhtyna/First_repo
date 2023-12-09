# module 6 2:35:10
import base64
def encode_data_to_base64(data):
    result = []
    for user in data:
        user_bytes = user.encode()
        base64_bytes= base64.b64encode(user_bytes)
        result.append(base64_bytes.decode())
    return result