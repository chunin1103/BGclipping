from rembg import remove
import pyscreenshot
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk

im=pyscreenshot.grab(bbox=(3,3,1184,1184))
im.show()