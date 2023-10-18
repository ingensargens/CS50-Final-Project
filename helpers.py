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



from PIL import Image, ImageDraw, ImageFont

def draw_text_on_image(text):
    image = Image.open("templates/bgs/marble.jpg")
    draw = ImageDraw.Draw(image)
    w, h = image.size

    # Specify the font and size
    font = ImageFont.truetype(r'C:\Users\arjan\OneDrive\Desktop\coding\finalProject\templates\fonts\Tomatoes-O8L8.ttf', 20)

    # Calculate the center of the image
    center_x = w // 2
    center_y = h // 2

    # Calculate the total height of the text
    total_text_height = len(text) * (font.getsize(" ")[1] + 10)
    
    # Calculate the starting Y position
    position_y = center_y - (total_text_height // 2)

    # Specify the text color (R, G, B)
    text_color = (255, 255, 255)

    # Add the text to the image
    for item in text:
        text_width, text_height = draw.textsize(item, font)
        position_x = center_x - (text_width // 2)
        draw.text((position_x, position_y), item, fill='black', font=font)
        position_y += text_height + 10

    # Save the modified image
    image.save("output_image.jpg")

    # Close the image
    image.close()

