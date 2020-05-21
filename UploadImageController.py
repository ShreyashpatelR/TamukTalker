import UploadImageModel

class UploadImageController:
    
    def __init__(self,filename,imagedestination):
        UploadImageModel.UploadImageModel(filename,imagedestination)
        