import os
from PIL import Image, ImageDraw, ImageFont

def setup():
    # Specify the path to your commands.txt file
    commands_file_path = "commands.txt"

    # Read and process the commands from the file
    with open(commands_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("export "):
                key, value = line[len("export "):].split("=", 1)
                os.environ[key] = value

def draw_text_on_image(text):

    image = Image.open("templates/marble.jpg")
    draw = ImageDraw.Draw(image)

    # Specify the font and size
    font = ImageFont.load_default()
    font_size = 36

    # Specify the text and position
    position = (50, 50)

    # Specify the text color (R, G, B)
    text_color = (255, 255, 255)

    # Add the text to the image
    draw.text(position, text, fill=text_color, font=font)

    # Save the modified image
    image.save("output_image.jpg")

    # Close the image
    image.close()
    # this is a compmdkasda
    