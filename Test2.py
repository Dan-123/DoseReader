import pydicom, numpy as np

dose = pydicom.read_file('DoseVolumeTest.dcm')
#d = np.fromstring(dose.PixelData, dtype=np.int16)
#d = d.reshape((dose.NumberOfFrames, dose.Columns, dose.Rows))


# Build x, y, z, position grids
xgrid = np.arange(dose.ImagePositionPatient[0], dose.Rows, dose.PixelSpacing[0])
ygrid = np.arange(dose.ImagePositionPatient[1], dose.Columns, dose.PixelSpacing[1])
zgrid = np.arange(dose.ImagePositionPatient[2], dose.NumberOfFrames, int(dose.GridFrameOffsetVector[1-0]))


# Reshape 1D arrays to 3D Cubes for both x,y,z axis
# Determine how to index like MATLAB does
xcube = np.stack((xgrid, xgrid, xgrid))
ycube = np.stack((ygrid, ygrid, ygrid))
zcube = np.stack((zgrid, zgrid, zgrid))

# Compute gradient matrix
grad = np.gradient(dose.pixel_array)

gradnorm = np.sqrt(grad[0]**2 + grad[1]**2 + grad[2]**2)


# minimum dose in Gy

dosethreshold = 0.5
mindose = dosethreshold * np.max(dose.pixel_array * dose.DoseGridScaling)

# Find indicies which satsify dosethreshold requirements
#index = np.argwhere(dose.pixel_array > mindose)
index = np.nonzero(dose.pixel_array > mindose)

xindex = index[0]
yindex = index[1]
zindex = index[2]


mingrad = 100
gradindex = np.nonzero(gradnorm < mingrad)

xgrad = gradindex[0]
ygrad = gradindex[1]
zgrad = gradindex[2]


# Dose at point 0
print(dose.pixel_array[xindex[0]][yindex[0]][zindex[0]])

# Gradient at point 0
print(gradnorm[xindex[0]][yindex[0]][zindex[0]])