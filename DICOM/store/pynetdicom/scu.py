from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import CTImageStorage, MRImageStorage, EnhancedMRImageStorage  
from pynetdicom import ALL_TRANSFER_SYNTAXES

debug_logger()
ae = AE(ae_title='MY_LOCAL_SCU')

ae.add_requested_context(CTImageStorage)
ae.add_requested_context(MRImageStorage)
ae.add_requested_context(EnhancedMRImageStorage, ALL_TRANSFER_SYNTAXES)

server_ip = '127.0.0.1'
server_port = 11112
server_ae_title = 'MY_LOCAL_SCP'

dicom_path = 'path/to/your.dcm'

assoc = ae.associate(server_ip, server_port, ae_title=server_ae_title)
if assoc.is_established:
    status = assoc.send_c_store(dicom_path)
    if status:
        print(f"✅ 发送成功！状态码: {status.Status}")
    else:
        print("❌ 发送失败，无响应")
    assoc.release()
else:
    print(f"🔥 关联失败：{assoc.reason}")