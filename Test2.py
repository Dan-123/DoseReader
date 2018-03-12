import pydicom, numpy as np

dose = pydicom.read_file('DoseVolumeTest.dcm')
d = np.fromstring(dose.PixelData, dtype=np.int16)
#d = d.reshape((dose.NumberOfFrames, dose.Columns, dose.Rows))

xgrid = np.arange(0, dose.Columns, dose.PixelSpacing[0])
ygrid = np.arange(0, dose.Rows, dose.PixelSpacing[1])
zgrid = np.arange(0, dose.NumberOfFrames, int(dose.GridFrameOffsetVector[1-0]))
grad = np.gradient(d)

