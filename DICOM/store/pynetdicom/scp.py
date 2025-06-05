import os
from pynetdicom import AE, evt, AllStoragePresentationContexts
from pynetdicom.sop_class import EnhancedMRImageStorage
from pynetdicom import ALL_TRANSFER_SYNTAXES

output_folder = './dicom_storage'
os.makedirs(output_folder, exist_ok=True)

def handle_store(event):
    ds = event.dataset
    patient_id = ds.PatientID
    study_uid = ds.StudyInstanceUID
    series_uid = ds.SeriesInstanceUID
    save_path = f"{output_folder}/{patient_id}/{study_uid}/{series_uid}"
    os.makedirs(save_path, exist_ok=True)
    ds.save_as(f"{save_path}/{ds.SOPInstanceUID}.dcm")
    return 0x0000  # 成功状态码

ae = AE(ae_title='MY_LOCAL_SCP')
ae.supported_contexts = AllStoragePresentationContexts
ae.add_supported_context(EnhancedMRImageStorage, "1.2.840.10008.1.2.4.91")
ae.start_server(('127.0.0.1', 11112), evt_handlers=[(evt.EVT_C_STORE, handle_store)])