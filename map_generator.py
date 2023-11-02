from PIL import Image, UnidentifiedImageError
import numpy as np
import sys

def get_image_path():
    try:
        while True:
            try:
                image_path = str(input('Enter the image path: '))
                image = Image.open(image_path)
            except (FileNotFoundError, UnidentifiedImageError):
                print('\033[31mInvalid Image Path, Please Try Again!!\033[m')
                continue
            else:
                break
    except (KeyboardInterrupt):
        print('\033[33m\n\nKeyboardInterrupt: Program terminated by the user.\033[m')
        sys.exit()
    return image

def parse_without_color(image):
    width, height = image.size
    image_matrix = np.array(image)
    
    relief_map = []
    for i in range(height):
        row = []
        for j in range(width):
            height = int(np.mean(image_matrix[i, j]))
            color_info = f'0xffffff'
            point_info = f'{height},{color_info}'
            row.append(point_info)
        relief_map.append(row)
    return relief_map    
    
def main():
    image = get_image_path()
    width, height = image.size
    image_matrix = np.array(image)
    use_default_color = False

    relief_map = []
    for i in range(height):
        row = []
        for j in range(width):
            try:
                height = int((np.mean(image_matrix[i, j])) - 128)
                r = image_matrix[i, j][0]
                g = image_matrix[i, j][1]
                b = image_matrix[i, j][2]
                color_info = f'0x{r:02x}{g:02x}{b:02x}'
                point_info = f'{height},{color_info}'
                row.append(point_info)
            except (IndexError):
                print('\033[31mUnable to parse image color :(\033[m')
                use_default_color = True
                break
        if use_default_color:
            break
        else:
            relief_map.append(row)

    if use_default_color:
        relief_map = parse_without_color(image)

    save_map = input('Enter the name that the map will be saved: ')
    with open(save_map, 'w') as file:
        for row in relief_map:
            file.write(" ".join(row) + '\n')
    print(f"\033[32m\nThe map '{save_map}' was created successfully!!\033[m")

if __name__ == '__main__':
    main()
