from PIL import Image

def jpeg_to_png_with_transparency(input_jpeg, output_png):
    # Open the image
    img = Image.open(input_jpeg).convert("RGBA")

    # Create a new transparent image with the same size
    new_img = Image.new("RGBA", img.size, (255, 255, 255, 0))

    # Loop over the pixels and set the background to transparent
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            # Assuming white background (you can modify this for other colors)
            if r > 240 and g > 240 and b > 240:
                # Set pixel to transparent
                new_img.putpixel((x, y), (255, 255, 255, 0))
            else:
                # Keep the pixel
                new_img.putpixel((x, y), (r, g, b, a))

    # Save the new image as PNG with transparency
    new_img.save(output_png, "PNG")

# Usage
input_jpeg = "/Users/avischwarzschild/Downloads/Minimalist Black Binoculars Logo on White Background.jpg"
output_png = "images/logo.png"
jpeg_to_png_with_transparency(input_jpeg, output_png)
