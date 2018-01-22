import os
import getopt
import sys
from PIL import Image

# parse the arguments.
opts, args = getopt.getopt(sys.argv[1:], 'd:w:')
 
# Set some default values to the needed variables.
directory = ''
width = -1
 
# If an argument was passed in, assign it to the correct variable.
for opt, arg in opts:
    if opt == '-d':
        directory = arg
    elif opt == '-w':
        width = int(arg)
    
 
# We have to make sure that all of the arguments were passed.
if width == -1 or directory == '':
    print('Invalid command line arguments. -d [directory] ' \
          '-w [width] are required')
 
    # If an argument is missing exit the application.
    exit()

# Iterate through every image given in the directory argument and resize it.
for image in os.listdir(directory):
    print('Resizing image ' + image)
 
    # Open the image file.
    img = Image.open(os.path.join(directory, image))
    
    #set ratio from width user-input
    widthpercent = (width/float(img.size[0]))
    heightsize = int((float(img.size[1])*float(widthpercent)))

    # Resize it.
    img = img.resize((width, heightsize), Image.ANTIALIAS)
 
    img = img.convert('RGB')

    # Save it back to disk.
    img.save(os.path.join(directory, 'resized-' + image))
 
print('Batch processing complete.') 
