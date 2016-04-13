import numpy as np
from matplotlib import pyplot as plt,cm
from skimage import data


def draw_h(image,coords,in_place=True):
    green=[0,255,0]
    row,col=coords
    height=24
    width=20
    thick=3
    if not in_place:
        image=image.copy()
    image[row:(row+height),col:(col+thick),:]=green
    image[row:(row+height),(col+width-thick):(col+width),:]=green
    strut=row+height//2
    image[strut:strut+thick,col:col+width,:]=green
    return(image)

def main():
    lena=data.lena()
    lena_h=draw_h(lena,(50,-50),in_place=False)
    plt.imshow(lena_h)
    plt.show()


if __name__ == '__main__':
    main()
