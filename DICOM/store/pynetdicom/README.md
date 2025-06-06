Dependencies:
- pynetdicom

Test:
1. python scp.py
2. python scu.py

注意事项：
Q: 自己创建的dicom一致无法保存，DIMSE Status 0xc211: Error: Cannot understand。
A: 路径过长，Windows默认禁用长路径支持（>260字符），修改方式是将保存路径默认放在D盘根目录。