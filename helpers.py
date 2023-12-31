import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

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

def draw_text_on_image(list: list[str], color: str, size: int, img: str, font: str):
    #accepts list of strings and turns it into str separated by \n
    text = list_to_str(list=list)
    image = Image.open(f"templates/bgs/{img}.jpg")

    color = ImageColor.getrgb(color)

    draw = ImageDraw.Draw(image)
    w, h = image.size
    size = size * 2 if font == 'handwriting' else size

    paths = {
        'handwriting':r'templates/fonts/HelloKetta-d99oX.ttf', 
        'cursive':r'templates/fonts/Halimun-W7jn.ttf',
        'slantedCursive':r'templates/fonts/Tomatoes-O8L8.ttf'
    }
        
    # Specify the font and size
    fontPath = ImageFont.truetype(paths[font], size)
        
    draw.multiline_text((w/2, h/2), text, align='center', fill=color, font=fontPath, anchor='mm')

    # Save the modified image
    image.save("static/output_image.jpg")

    # Close the image
    image.close()

def list_to_str(list: list[str]):
    newStr = ''
    for item in list:
        newStr += item
        newStr +='\n'
    return newStr

