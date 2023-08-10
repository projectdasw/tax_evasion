from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageMorph
import random
import json

from otree.api import *


author = 'Your name here'
doc = """
Your app description

"""
CHARSET = "123456789+-/*"
LENGTH = 3
TEXT_SIZE = 32
TEXT_PADDING = TEXT_SIZE
TEXT_FONT = Path(__file__).parent / "assets" / "FreeSerifBold.otf"
INPUT_TYPE = "text"
INPUT_HINT = "masukkan jawaban yang tepat"


def generate_puzzle_fields():
            number1 = random.randint(1, 9)
            number2 = random.randint(1, 9)
            number3 = random.randint(1, 9)
            type = random.randint(0, 7)

            if type == 0:
                solution = round((number1 * number2 + number3), 2)
                question = "{} x {} + {}".format(number1, number2, number3)
            elif type == 1:
                solution = round((number1 * number2 - number3), 2)
                question = "{} x {} - {}".format(number1, number2, number3)
            elif type == 2:
                solution = round((number1 + number2 * number3), 2)
                question = "{} + {} x {}".format(number1, number2, number3)
            elif type == 3:
                solution = round((number1 - number2 * number3), 2)
                question = "{} - {} x {}".format(number1, number2, number3)
            elif type == 4:
                solution = round((number1 / number2 + number3), 2)
                question = "{} / {} + {}".format(number1, number2, number3)
            elif type == 5:
                solution = round((number1 / number2 - number3), 2)
                question = "{} / {} - {}".format(number1, number2, number3)
            elif type == 6:
                solution = round((number1 + number2 / number3), 2)
                question = "{} + {} / {}".format(number1, number2, number3)
            elif type == 7:
                solution = round((number1 - number2 / number3), 2)
                question = "{} - {} / {}".format(number1, number2, number3)
            return dict(text=question, solution=solution)


def is_correct(response, puzzle):
    try:
        float(response)
        return float(puzzle.solution) == float(response)
    except ValueError:
        return False


def render_image(puzzle):
    text = puzzle.text
    dumb = Image.new("RGB", (0, 0))
    font = ImageFont.truetype(str(TEXT_FONT), TEXT_SIZE)
    w, h = ImageDraw.ImageDraw(dumb).textsize(text, font)
    image = Image.new("RGB", (w + TEXT_PADDING * 2, h + TEXT_PADDING * 2))
    draw = ImageDraw.Draw(image)
    draw.text((TEXT_PADDING, TEXT_PADDING), text, font=font)

    # distort
    img = image.convert("L")
    distortions = []
    for op in distortions:
        _, img = op.apply(img)
    return img

