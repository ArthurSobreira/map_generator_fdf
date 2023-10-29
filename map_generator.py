from PIL import Image
import numpy as np

def main():
    try:
        while True:
            try:
                image_path = str(input('Enter the image path: '))
                imagem = Image.open(image_path)
            except (FileNotFoundError):
                print('\033[31mInvalid Image Path, Please Try Again!!\033[m')
                continue
            else:
                break
    except (KeyboardInterrupt):
        print('\033[33m\n\nKeyboardInterrupt: Program terminated by the user.\033[m')
        return

    width, height = imagem.size
    image_matrix = np.array(imagem)

    relief_map = []
    for i in range(height):
        row = []
        for j in range(width):
            height = int((np.mean(image_matrix[i, j])) - 128)
            color_info = f'0x{image_matrix[i, j][0]:02x}{image_matrix[i, j][1]:02x}{image_matrix[i, j][2]:02x}'
            point_info = f'{height},{color_info}'
            row.append(point_info)
        relief_map.append(row)

    save_map = input('Enter the name that the map will be saved: ')
    with open(save_map, 'w') as file:
        for row in relief_map:
            file.write(" ".join(row) + '\n')
    print(f"\033[32m\nThe map '{save_map}' was created successfully!!\033[m")

if __name__ == '__main__':
    main()