# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:05:28 2021

@author: Admin
"""
import requests
resp = requests.post("https://emlopsinfy.herokuapp.com/predict",
                     files={"file":open('bird_img.jpg','rb')})
print(resp.text)