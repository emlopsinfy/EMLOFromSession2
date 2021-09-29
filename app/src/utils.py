from PIL import Image
from io import BytesIO
from base64 import b64encode


def get_image(img_byte):
    return Image.open(BytesIO(img_byte))


def get_encoded_img(img):
    return b64encode(img)
