from PIL import Image

class UploadImageModel:
    
    #update image
    def __init__(self,filename , imagedestination):
        im1 = Image.open(filename)
        width, height = im1.size  
        im2 = im1.copy()
        size=(72,72)
        im2 = im2.resize(size)
        im2.save("image/"+imagedestination)
            
    