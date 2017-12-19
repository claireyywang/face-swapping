from packages import *

# feature overlay using Ordinary Procrustes analysis
def warp_img(img, M, dimensions):
  warped_img = np.zeros(dimensions, dtype=img.dtype)
  cv2.warpAffine(img,M[:2],(dimensions[1],dimensions[0]),dst=warped_img, borderMode=cv2.BORDER_TRANSPARENT, flags=cv2.WARP_INVERSE_MAP)
  return warped_img
