from PIL import Image
import numpy as np

image_path = input("Enter the image path: ")
imagem = Image.open(image_path)
width, height = imagem.size

image_matrix = np.array(imagem)

relief_map = []

for i in range(height):
    row = []
    for j in range(width):
        height = int(np.mean(image_matrix[i, j])) - 128
        color_info = f'0x{image_matrix[i, j][0]:02x}{image_matrix[i, j][1]:02x}{image_matrix[i, j][2]:02x}'
        point_info = f'{height},{color_info}'
        row.append(point_info)
    relief_map.append(row)

save_image = input("Enter the name that the image will be saved: ")
with open(save_image, 'w') as file:
    for row in relief_map:
        file.write(" ".join(row) + '\n')
