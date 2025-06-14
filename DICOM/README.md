# DICOM

## 数据结构与文件格式

### 层次化信息模型
- 信息对象定义（IOD）​​：描述影像及相关信息（如患者 ID、检查参数）的结构化数据集。
- 数据元素（Data Element）​​：由唯一标签（Tag）、值类型（VR）、值长度和值组成，例如(0010,0010)对应患者姓名。
- 数据集（Data Set）​​：多个数据元素的集合，封装为.dcm 文件存储。

### 实体关系层级
- Study（检查）​​：单次完整诊断过程（如一次 CT 扫描）；
- Series（序列）​​：同一部位的多张图像；
- Instance（实例）​​：单张图像文件（可含多帧）。

结构示例：Study/Series/Instance.dcm 目录存储模式便于检索与管理。

## 网络传输机制

### ​协议栈基础​​
基于TCP/IP协议，通过​​关联控制服务元素（ACSE）​​建立设备间会话，协商传输语法（如JPEG无损压缩）与服务类。

关联控制服务元素（ACSE, Association Control Service Element）是​​OSI（开放系统互连）参考模型应用层的核心协议​​，用于建立、维护和释放两个应用实体（AE）之间的应用关联（Application Association），并协商应用上下文（Application Context）。

### 服务角色与消息交换​​
- ​​SCU（服务类用户）​​：发起请求的客户端（如CT设备）；
- SCP（服务类提供者）​​：响应请求的服务端（如PACS服务器）；
- 关键操作指令​​：
  - C-STORE：影像存储（如上传至PACS）；
  - C-FIND：查询患者检查记录；
  - C-MOVE：跨设备调取影像。

## 核心服务功能​
- ​存储服务：设备向PACS归档影像，确保数据持久化，扫描完成后自动备份至服务器；
- ​查询/检索服务：基于患者ID、检查类型等条件筛选影像，医生调阅历史影像对比；
- ​打印服务：控制DICOM打印机输出标准化胶片，急诊科即时打印诊断报告；
- ​工作流管理：同步检查日程、设备状态（Modality Worklist），优化放射科资源调度；
​- Web集成（WADO）：通过HTTP协议访问DICOM影像，支持浏览器直接浏览，移动端远程会诊；

## 学习资料
- https://orthanc.uclouvain.be/book/dicom-guide.html#dicom-guide