import cmpt120image as ci
import green_checker as gc

ci.init()

kid = ci.get_image("kid-green.jpg")
beach = ci.get_image("beach.jpg")
# img = cmpt120image.get_image("chatgpt_raccoon.jpg")
# beach = cmpt120image.get_image("Sunset_in_la_jolla.jpg")

# Go through all pixels in image and say whether it is green or not
height = len(kid)  # num rows
width = len(kid[0])  # num cols

for row in range(height):
    for col in range(width):
        pixel_from_img = kid[row][col]
        # print(pixel_from_img)
        if gc.is_green(pixel_from_img):  # If pixel is green, replace it with color from beach
            kid[row][col] = beach[row][col]

ci.show_image(kid, 'merged')
input("Please any key to end the program.")
