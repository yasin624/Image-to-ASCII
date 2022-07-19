import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
from tqdm import tqdm
#yol=r"C:\Users\msi\Desktop\archive\resimler"
#size=(500,500)

first_page="""                      
####################################################################################################
####################################################################################################
####################################################################################################
###                                                                                              ###
###     |#|   |##|   |##|     |###|                                                              ###
###     |#|   |###|  ###|    |#|  ||                                          |                  ###
###     |#|   |#|#| |#|#|   |#|                                               ||                 ###
###     |#|   |#||# |||#|   |#| ###|                        |||||              ||                ###
###     |#|   |#||#|#||#|   |#|  |#|                           ||||||          |||               ###
###     |#|   |#||### |#|   |#|  |#|                           |||||||||       ||#||             ###
###     |#|   |#| |#| |#|    |#| |#|                           |#| ||||| |    | |||||            ###
###     |#|   |#| |#| |#|     |####                            ||    |||||||||||  |#||           ###
###                                                          ||||||     ||| ||||  |||||          ###
###                                                          ||||||     ||| ||||  |||||          ###
###                                                         |||||||||    ||||#||| ||||||         ###
###                                                        ||||||||||||| |#|  #|||||||| |        ###
###                                                      ||#|||||||||||||||||  |||||||#||        ###
###                                                     ||||||||||||#|  ||||||||#|||||#||        ###
###                                                   ||||#||||||||||||| ||||||||###||#||        ###
###     ######| |####                                ||||||| ||||||||||   |||||  #||||#||        ###
###       |#   |#|  ##                             |||||||  |||#||||||||   ||||   |||#|||        ###
###       |#  |#|   |#|                           |||  |||  ||||||||||||    |||   #||#|#|        ###
###       |#  |#|   |#|                           |      |||||||||||||||          |||#|||        ###
###       |#  |#|   |#|                                 ||||#||||#||||||| | ||     ||| ||        ###
###       |#  |#|   |#|                               ||||||||||##|||||||||| ||    ||||||        ###
###       |#   ##   ##                               |||||#|||||##||||||||| ||||   ||  |#        ###
###       |#    |###|                                ||||||||||||||#|||||||   ||| ||||||#        ###
###                                                 ||||||||| ||||||||||||||| || |   |||||       ###
###                                                 |||||||||  |||||##||||||   ||||  |||||       ###
###                                                ||||||||||  ||||||#|||||||||||||| |#|         ###
###                                                ||||||||| |||||||#||||||||||||||| |||         ###
###                                               |||| |  | |||||| |||#||||||||||||   |||        ###
###                                               |||  |     ||#| ||#|#|||#|||||||||  ||         ###
###                                               |||       |##|   |||||||||||||||||  ||         ###
###       |##|   |##|   |### |#||#|               |||       |##|   |||||||||||||||||  ||         ###
###       ||#|  |#| || |#| |||#||#|              |||        |#|    ||#|||||||#|||||||| |         ###
###       #||#  |#|   |#|    |#||#|              ||         |||    ||##|||||||||||||| |||        ###
###      |#||#|  ###| |#|    |#||#|              ||         |||    ||###||||||||||||#|  ||       ###
###      |# |#|   |##||#|    |#||#|               |         ||       ||#|||||||#|||||   ||       ###
###     |######     #||#|    |#||#|               |         |||      |||| ||||||||||||||||       ###
###     |#|  |#||| |#| |#  |||#||#|               |         |||      |||| ||||||#||||||||        ###
###     |#   |#| ###|   |### |#||#|               ||        |||         |||||||||||#|||||        ###
###                                               ||         ||||       | |||||||||||||          ###
###                                                |         ||| |      ||||||||||||||||         ###
###                                                                                              ###
###                                                                                              ###
###                                                                                              ###
####################################################################################################
####################################################################################################
####################################################################################################         
                                     

"""




class image_to_ascii():
    def __init__(self):

        self.image_set=[]
        
    def keys(self,image):
        if image=="img":
            return {5:"#",
                    55:"|",
                    105:"@",
                    155:"(",
                    205:"&",
                    255:"*"}
        elif image=="icon":
            return {5:"#",
                    55:"#",
                    105:"|",
                    155:"|",
                    205:"|",
                    255:" "}
    def foreword(self,word="first"):
        if word=="first":
            print(first_page)
            
            print("""

                {1} Img convert to Ascii
                {2} icon convert to Ascii
                {3} quit

            """)
        elif word == "convert":
            print("""
        --------------------------------------------------------------
                !!!  warning
                
                semple :
                    path : "C:/..../.../img.jpg"  or "C:/..../.../images/
                    size : 500,500
        --------------------------------------------------------------
            """)
    def start(self,size,resp):
        size=size.split(",")
        print("hazırlıklar yapılıyor ...\n\n")
        print("resimler  yükleniyor ...\n\n")
        try:
            response=self.images_upgrade(resp,(int(size[0]),int(size[1])))
        except:
            response=False
            print("\n\n please enter  a real shape  ..\n\n" )
        if response:
            print("resimler  yüklendi ...\n\n")
            self.img_convert_and_save(resp)
            print("resimler dönüştürmeye hazırlanıyor ...\n\n")
        
    def main(self):
        while True:

            self.foreword()
            self.image_set=[]
            inp=input("respons ==>> ")
            
            
            if inp == "1":
                self.ascii_code=self.keys("img")
                self.foreword(word="convert")
                resp=input("path : ")
                size=input("size : ")
                self.start(size,resp)
                
            elif inp=="2":
                self.ascii_code=self.keys("icon")
                self.foreword(word="convert")
                resp=input("path : ")
                size=input("size : ")
                self.start(size,resp)
                
            elif inp=="3":
                break
            else:
                print("\n\n please select from the menu ..\n\n" )
    def images_upgrade(self,target,size):


        try:
            
            for i in os.listdir(target):
                
                if i.endswith("jpg"):
                    
                    foto=np.array(cv2.imread(target+"\\"+i,0))
                    
                    new_arry=self.orantılı(arr=foto, tam_dolgu=size)
                    
                    print("size : ",new_arry.shape)
                    self.image_set.append(new_arry)
        except:
            try:
                foto=np.array(cv2.imread(target,0))
                new_arry=self.orantılı(arr=foto, tam_dolgu=size)
                print("size : ",new_arry.shape)
                self.image_set.append(new_arry)
                self.image_set.append(new_arry)
            except:
                print("\n please enter a real url \n ")
                return False
        return True
        
    def translate(self,target):
        
        str_img=""
        
        for s1,i in enumerate(target):
            for s2,k in enumerate(i):
                if 25>=k:
                    str_img+=self.ascii_code[5]


                elif 25<k<=80:
                    str_img+=self.ascii_code[55]
                elif 80<k<=130:
                    str_img+=self.ascii_code[105]
                elif 130<k<=180:
                    str_img+=self.ascii_code[155]
                elif 180<k<=230:
                    str_img+=self.ascii_code[205]
                elif 230<k<=255:
                    str_img+=self.ascii_code[255]
                else:
                    str_img+=str(self.ascii_code[s1,s2])
            str_img+="\n"

        return str_img
    
    def img_convert_and_save(self,target):
        
        try:
            s=0
            for i in os.listdir(target):
                if i.endswith("jpg"):
                    with open(target+"\\"+i[:-4]+".txt","w") as file:
                        print(f"{i} resmi dönüştürülüyor  ...\n\n")
                        file.write(self.translate(self.image_set[s]))
                        print(f"{i} resmi dönüştürüldü  ...\n\n")
                        s+=1
        except:
             with open(target[:-4]+".txt","w") as file:
                    print(f"{target.split('/')[-1]} resmi dönüştürülüyor  ...\n\n")
                    file.write(self.translate(self.image_set[0]))
                    print(f"{target.split('/')[-1]} resmi dönüştürüldü  ...\n\n")
                    
    def orantılı(self, arr, tam_dolgu):

        for s in tqdm(range(len(arr))):

            #####################################  yeniden şekillendir ve kutuyu yerleştir
            istenilen_x = tam_dolgu[1]
            istenilen_y = tam_dolgu[0]
            arr_size = arr.shape
            
            orantı = arr_size[1] / arr_size[0]
            orantı_x = istenilen_y * orantı

            if orantı_x > istenilen_x:
                eksik_deger = orantı_x - istenilen_x

                orantı_x = int(orantı_x - eksik_deger)

                orantı_y = int((arr_size[0] / arr_size[1]) * istenilen_x)
            else:
                orantı_y = istenilen_y

            if orantı_x>orantı_y:
                yeni_resim = cv2.resize(arr, (int(orantı_x), int(orantı_y)))
            else:
                yeni_resim = cv2.resize(arr, (int(orantı_y), int(orantı_x)))

                

            

        return yeni_resim









img_to_asci=image_to_ascii()

img_to_asci.main()


