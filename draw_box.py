import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector

# Global Constants
img = None
tl_list = []
br_list = []
object_list = []

# Constants
image_folder = 'F:\CodeProjects\Datasets\images\pistols\\full'
save_dir = 'F:\CodeProjects\Datasets\images\pistols\annotations'
obj = 'pistol'


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def on_key_press(event):
    global object_list
    global tl_list
    global br_list
    global img

    if event.key == 'q':
        print(tl_list, br_list)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    toggle_selector.RS.set_active(True)

if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        image = image_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback, 
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', on_key_press)
        plt.show()