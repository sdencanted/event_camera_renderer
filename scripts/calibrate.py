import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:5].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('../calib_source/*.png')
imgs=[]
for fname in images:
    print("finding corners for ",fname)
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (8,5), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (8,5), corners2, ret)
        imgs.append(img)
    else:
        print("failed to find corners")
# for img in imgs:
#     cv.imshow('img', img)
#     cv.waitKey(0)
cv.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(mtx)
# print(cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None))

# EVK4 16mm lens
# [[3.34434100e+03 0.00000000e+00 5.34432275e+02]
#  [0.00000000e+00 3.34663269e+03 4.21466317e+02]
#  [0.00000000e+00 0.00000000e+00 1.00000000e+00]]