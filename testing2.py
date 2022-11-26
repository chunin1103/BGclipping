from rembg import remove
from PIL import Image
import io
  

input_path ='eagle-pic-1280x800-23fd0ad.png'
output_path = input_path.replace('images', 'results')

im = Image.open(input_path)
# rgb_im = im.convert('RBG')
output = remove(im)
output.show()