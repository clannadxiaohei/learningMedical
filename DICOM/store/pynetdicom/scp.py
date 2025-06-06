import os
from pynetdicom import AE, evt, AllStoragePresentationContexts
from pynetdicom.sop_class import EnhancedMRImageStorage
from pynetdicom import ALL_TRANSFER_SYNTAXES
from pydicom.uid import UID

output_folder = 'd:\\dicom_storage'
os.makedirs(output_folder, exist_ok=True)

def handle_store(event):
    ds = event.dataset
    patient_id = ds.PatientID
    study_uid = ds.StudyInstanceUID
    series_uid = ds.SeriesInstanceUID
    
    try:
      save_path = os.path.join(output_folder, patient_id, study_uid, series_uid)
      os.makedirs(save_path, exist_ok=True)
      file_path = os.path.join(save_path, f"{ds.SOPInstanceUID}.dcm")

      ds.save_as(file_path, write_like_original=True)
    except Exception as e:
      print(f"🔥 全局异常：{str(e)}")
    return 0x0000  # 成功状态码

ae = AE(ae_title='MY_LOCAL_SCP', )
ae.supported_contexts = AllStoragePresentationContexts
ae.add_supported_context(EnhancedMRImageStorage, "1.2.840.10008.1.2.4.91")
ae.add_supported_context("1.2.840.10008.5.1.4.1.1.7")

ae.start_server(('127.0.0.1', 11112), evt_handlers=[(evt.EVT_C_STORE, handle_store)])