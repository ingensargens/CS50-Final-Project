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

def draw_text_on_image(list: list[str]):
    #accepts list of strings and turns it into str separated by \n
    text = list_to_str(list=list)
    image = Image.open("templates/bgs/marble.jpg")
    draw = ImageDraw.Draw(image)
    w, h = image.size
    print(w, h)

    # Specify the font and size
    font = ImageFont.truetype(r'templates\fonts\Tomatoes-O8L8.ttf', 20)
        
    draw.multiline_text((w/2, h/2), text, align='center', fill='black', font=font, anchor='mm')

    # Save the modified image
    image.save("output_image.jpg")

    # Close the image
    image.close()

def list_to_str(list: list[str]):
    newStr = ''
    for item in list:
        newStr += item
        newStr +='\n'
    return newStr