from display import *
from draw import *
from parsing import *
from matrix import *
import math

screen = new_screen()
color = [102, 161, 255]
edges = []
transform = new_matrix()


parse_file("script", edges, transform, screen, color)
