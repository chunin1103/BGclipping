from rembg import remove
import pyscreenshot
  
# im=pyscreenshot.grab(bbox=(X1,Y1,X2,Y2))
# im = pyscreenshot.grab(bbox=(100, 50, 1000, 1000)) 
im = pyscreenshot.grab() 

im = remove(im)
# To view the screenshot
im.show()
  
# To save the screenshot
# image.save("GeeksforGeeks.png")