import numpy as np

# Simulated 6x6 12-bit X-ray scan slice (brighter center = denser tissue/bone)
xray_slice = np.array([
    [120, 150, 200, 180, 140, 110],
    [160, 850, 1200, 1150, 800, 150],
    [210, 1300, 3400, 3600, 1250, 190],
    [200, 1280, 3800, 4095, 1320, 185],
    [155, 820, 1180, 1100, 790, 145],
    [115, 140, 190, 175, 135, 105],
], dtype=np.float32)


#Analysing the scan and gitting all the usful data out of it
def analyse_scan(image: np.ndarray) -> dict:
    shapes = image.shape
    minVal = image.min()
    maxVal = image.max()
    meanval = image.mean()

    return {
        "Shape" : shapes,
        "Min_Intensity" : float(minVal),
        "Max_Intensity" : float(maxVal),
        "Mean_Intensity" : round(float(meanval),2),
    }

#Scaling pixel intensity to [0.0 , 1.0] using the Min-Max 
def normalize_image(image: np.ndarray) -> np.ndarray:
    minVal = image.min()
    maxVal = image.max()
    total = (image - minVal) / (maxVal - minVal)

    return total

#Extract and return centre regeion of intrest ROI of crop_size x crop_size
def crop_centre(image: np.ndarray, crop_size: int = 4) -> np.ndarray:
    imgHeight =  image.shape[0]
    imgWidth = image.shape [1]
    startHeight = (imgHeight - crop_size) // 2
    startWidth = (imgWidth - crop_size) // 2

    return image[ startHeight : (startHeight+crop_size),startWidth : (startWidth + crop_size)]


print(analyse_scan(xray_slice))
print(normalize_image(xray_slice))
print(crop_centre(xray_slice))