from PIL import Image, ImageDraw

def remove_white_bg():
    img = Image.open('logo-branca.png').convert("RGBA")
    
    # We flood fill with transparency starting from the 4 corners
    # thresh=100 will allow removing near-white artifacts, 
    # since the burgundy color (77, 8, 29) has a distance of ~180 to white.
    target_color = (255, 255, 255, 0)
    
    ImageDraw.floodfill(img, (0, 0), target_color, thresh=100)
    ImageDraw.floodfill(img, (img.width-1, 0), target_color, thresh=100)
    ImageDraw.floodfill(img, (0, img.height-1), target_color, thresh=100)
    ImageDraw.floodfill(img, (img.width-1, img.height-1), target_color, thresh=100)
    
    img.save('logo-branca.png')
    print("Logo processed successfully!")

remove_white_bg()
