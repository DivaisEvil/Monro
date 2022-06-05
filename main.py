from PIL import Image


def main():
    image = Image.open("monro.jpg")
    red, green, blue = image.split()

    crop = 100
    top_crop = 0
    left_crop_coordinates = (crop, top_crop, red.width, red.height)
    left_croped_red = red.crop(left_crop_coordinates)
    side_cropping_coordinates = (crop / 2, top_crop, image.width - crop / 2, image.height)
    left_right_croped_red = red.crop(side_cropping_coordinates)
    croped_red = Image.blend(left_croped_red, left_right_croped_red, 0.5)

    right_crop_coordinates = (0, 0, blue.width - crop, blue.height)
    right_croped_blue = blue.crop(right_crop_coordinates)
    left_right_croped_blue = blue.crop(side_cropping_coordinates)
    croped_blue = Image.blend(right_croped_blue, left_right_croped_blue, 0.5)

    centr_croped_green = green.crop(side_cropping_coordinates)

    transformation_image = Image.merge("RGB", (croped_red, croped_blue, centr_croped_green))
    transformation_image.save("transformation_image.jpg")

    transformation_image.thumbnail((80, 80))
    transformation_image.save('finish_image.jpg')


if __name__ == '__main__':
    main()