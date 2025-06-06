import pydicom
import numpy as np
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ImplicitVRLittleEndian, ExplicitVRLittleEndian, UID

ds = Dataset()
ds.PatientName = "Test^Patient"
ds.PatientID = "ID12345"         
ds.Modality = "OT"
              
image_data = np.random.randint(0, 256, (512, 512), dtype=np.uint8)
ds.Rows, ds.Columns = image_data.shape
ds.PixelData = image_data.tobytes()

ds.BitsAllocated = 8   
ds.BitsStored = 8      
ds.HighBit = 7        
ds.SamplesPerPixel = 1  
ds.PhotometricInterpretation = "MONOCHROME2"  
ds.PixelRepresentation = 0  

ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.7"
ds.SOPInstanceUID = pydicom.uid.generate_uid()

file_meta = Dataset()
file_meta.MediaStorageSOPClassUID = ds.SOPClassUID 
file_meta.MediaStorageSOPInstanceUID = ds.SOPInstanceUID
file_meta.TransferSyntaxUID = ImplicitVRLittleEndian

ds.file_meta = file_meta

path = "../../data/test_dicom.dcm"
ds.save_as(path, enforce_file_format=True)

print(f"Load dataset from: {path} ...")
ds = pydicom.dcmread(path)
print(ds)

# import matplotlib.pyplot as plt
# plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
# plt.show()