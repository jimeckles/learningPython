
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["combinedFilters.jpg","filter1.jpg","filter2.jpg","filter3.jpg","grey.jpg"]

# for i in images:
#   if os.path.exists(i):
#     os.remove(i)

print(images)
# map(lambda i: os.path.exists and os.remove, images)
def removeFile(file):
  print(f"removing {file!s}")
  
list(map(removeFile, images))
# print(x)

