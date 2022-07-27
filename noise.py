import numpy as np
import cv2
from PIL import Image


def generate_mountain(x, i: int, j: int, cell_value: int):
    """
    Generate a value around the secret value.
    
    @param x: matrix;
    @param i: iteration number;
    @param j: iteration number;
    @param cell_value: secret cell value.
    @return: matrix.
    """
    x[i][j+1] = np.random.choice(range(1,cell_value))
    x[i][j-1] = np.random.choice(range(1,cell_value))
    x[i+1][j] = np.random.choice(range(1,cell_value))
    x[i-1][j] = np.random.choice(range(1,cell_value))
    x[i+1][j+1] = np.random.choice(range(1,cell_value))
    x[i-1][j+1] = np.random.choice(range(1,cell_value))
    x[i+1][j-1] = np.random.choice(range(1,cell_value))
    x[i-1][j-1] = np.random.choice(range(1,cell_value))
    return x
  
  
def diffusion(value: int) -> tuple:
    """
    Generate color for pixel.
    
    @param value: cell value
    @return default: color of pixel.
    """
    default: tuple = (255,255,255)
    if value == 1:
        return default
    else:
        value: int = value * 70
        default: tuple = (255-value,255-value,255-value,)
        return default

    
def blur_image(image_path: str) -> None:
    """
    Blur image with opencv2
    
    @param image_path: path to image.
    """
    img = cv2.imread(image_path) 
    blurImg = cv2.blur(img,(5,5)) 
    cv2.imwrite(image_path, blurImg)
    
    
def create_chunk(iter_count, x_max):
    """
    Main function.
    Create ones-matrix (x_max x x_max)
    Generate values around cell.
    
    @param iter_count: count of iterations.
    @param x_max: maximum height value.
    @return x: matrix
    """
    max_x, max_y = x_max, x_max
    x = np.ones((max_x, max_y), dtype=int)
    

    current_cell = 0
    for l in range(iter_count):
        random_cell = np.random.choice(range(65))
        cell_value = np.random.choice(range(3,6))
        for i in range(len(x)):
            for j in range(len(x[i])):
                current_cell += 1
                if current_cell == random_cell:
                    x[i][j] = cell_value
                    try:
                        x = generate_mountain(x, i, j, cell_value)
                    except IndexError:
                        pass

        for i in range(len(x)):
            for j in range(len(x[i])):
                current_cell = x[i][j]
                try:
                    if x[i][j+1] > current_cell:
                        x = generate_mountain(x, i, j+1, cell_value)
                except IndexError:
                    pass
    return x

def start(path_to_image: str):
    x_max: int = int(input("Maximum Pixelsize: "))
    iter_count: int = x_max // 8
    
    print(f"Maximum pixelsize: {x_max}")
    print(f"Iteration count: {iter_count}")
    
    x = create_chunk(iter_count, x_max)
    new = Image.new(mode="RGBA", size=(x_max,x_max), color="white")

    for i in range(len(x)):
        for j in range(len(x[i])):
            pixel = new.getpixel((i,j))
            color = diffusion(x[i][j])
            new.putpixel((i, j), color)

    new.save(path_to_image)
    blur_image(path_to_image)
start()
