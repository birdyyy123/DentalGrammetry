# DentalGrammetry
## คู่มือการติดตั้ง
## การติดตั้ง Meshroom 
### ***ผู้ใช้งานต้องทำการดาวโหลดไฟล์ ติดตั้ง CUDA Toolkit จากเว็บไซต์ https://developer.nvidia.com/cuda-zone ***
![](d1.JPG)
### 1.ดาวโหลดโปรแกรม Meshroom 
![](d1.JPG)
### 2.ดาวโหลด Source code ของ Meshroom ให้ตรงตาม Version ในข้อที่ 1 จากเว็บไซต์ https://github.com/alicevision/AliceVision/releases และทำการแตกไฟล์
![](d1.JPG)
### 3.นำ Folder aliceVision, lib, qtPlugins ในข้อที่ 1 Copy ไปใส่ไว้ใน Folder ของข้อที่ 2
![](d1.JPG)
### 4.ทำการติดตั้ง libary จากคำสั่ง
#### cd {PathToSourceCodeMeshroom}
#### pip install -r requirements.txt -r dev_requirements.txt