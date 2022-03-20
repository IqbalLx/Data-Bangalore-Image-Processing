from cv2 import imdecode, IMREAD_GRAYSCALE
from base64 import b64decode
from numpy import fromstring, ndarray, uint8

def decode_b64_to_image(b64str: str) -> ndarray:
    b64decoded = b64decode(b64str)
    arr = fromstring(b64decoded, uint8)
    img = imdecode(arr, IMREAD_GRAYSCALE)

    return img