# คู่มือการติดตั้ง
# การติดตั้ง Meshroom 
## ***ผู้ใช้งานต้องทำการดาวโหลดไฟล์ ติดตั้ง CUDA Toolkit จากเว็บไซต์ https://developer.nvidia.com/cuda-zone ***
![](https://github.com/birdyyy123/DentalGrammetry/image/1.PNG)

 
##    1.ดาวโหลดโปรแกรม Meshroom 

![](image/2.PNG)

 ##    2.ดาวโหลด Source code ของ Meshroom ให้ตรงตาม Version ในข้อที่ 1 จากเว็บไซต์ https://github.com/alicevision/AliceVision/releases และทำการแตกไฟล์
![](image/3.PNG)

##    3.นำ Folder aliceVision, lib, qtPlugins ในข้อที่ 1 Copy ไปใส่ไว้ใน Folder ของข้อที่ 2
![](image/4.PNG)


## 4.ทำการติดตั้ง libary จากคำสั่ง
    
    cd {PathToSourceCodeMeshroom}
    pip install -r requirements.txt -r dev_requirements.txt

## 5.สร้างไฟล์ meshroom.sh

![](image/5.PNG)

## 6.สร้างไฟล์ meshroom_photogrammetry.sh

![](image/6.PNG)

## 7.ใช้คำสั้งเพื่อให้ไฟล์ meshroom_photogrammetry.sh ใช้งานได้

    chmod +x meshroom.sh meshroom_photogrammetry.sh

# การติดตั้ง CloudCompare

    $ sudo snap install cloudcompare

# การติดตั้ง NodeJS
    
    $ sudo apt update
    $ sudo apt install nodejs

    $ sudo apt-get install curl
    $ curl -fsSL https://deb.nodesource.com/setup_15.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

# การติดตั้ง OBJ2GLTF

    npm install -g obj2gltf


