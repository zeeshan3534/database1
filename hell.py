import kivy
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json
import re

from requests.api import get

class KivyApp(App):
    
    firebase_url = "https://kivydb-bc692-default-rtdb.firebaseio.com/.json"
    def build(self):


        box_layout = BoxLayout()
        #create buttons
        button = Button(text="Create database")
        button_get = Button(text="Get Data")
        button_post = Button(text="Get post")
        button_put = Button(text="Get Result")
        button_delete = Button(text="Get Delete")
        #binding all buttons
        button.bind(on_press=self.create_dataBase)
        button_get.bind(on_press=self.create_get)
        button_post.bind(on_press=self.create_post)
        button_put.bind(on_press=self.create_put)
        button_delete.bind(on_press=self.create_delete)
        #add widget
        box_layout.add_widget(button)
        box_layout.add_widget(button_get)
        box_layout.add_widget(button_post)
        box_layout.add_widget(button_put)
        box_layout.add_widget(button_delete)
        return box_layout

    def create_dataBase(self,*args):
        # print("Botton for database")
        # json_data = '{"Username":["Bilal0","Syed Abdul Ali1","Zeeshan2","Hammas3"],"Password":["1234","abcd","nanna","9876"],"Gmail":["bilala123@gmail.com","ali962001@gmail.com"],"daily_index":["0","5","0","0"]}'
        json_data = '{"Username0":["0","Bilal0","1234","bilala123@gmail.com"],"Username1":["0","Syed Abdul Ali1","abcd","bilala123@gmail.com"],"Username2":["0","Danial2","9876","bilala123@gmail.com"],"Username3":["0","Zeeshan3","qwerty","bilala123@gmail.com"]}'
     
        res = requests.put(url=self.firebase_url,json=json.loads(json_data))
        
    def create_get(self,*args):
        res = requests.get(url=self.firebase_url).json()
        for i,j in res.items():
            print(i,j)

            
    def create_post(self,*args):
        print("Botton Click")
    def create_put(self,*args):

        get_from_login = "Syed Abdul Ali1"

        index = get_from_login[-1]
        index = str(index)
        print(index)
    
        fire_base_url = "https://kivydb-bc692-default-rtdb.firebaseio.com/Username.json"
        # 
        fire_base_url = fire_base_url[0:57] + index +fire_base_url[57:]
        res = requests.get(url=fire_base_url).json()
        # print(res[0])
        # print(fire_base_url)
        # print(match)
        # user = "Bilal0"
        # print(fire_base_url)
        new_res = int(res[0])
        new_res += 1
        new_res = str(new_res)
        res[0] = new_res
        res = json.dumps(res)
        print(res)
        # resa = res[get_data]
        # resb = int(resa)
        # resb += 1
        # resb = str(resb)
        # res[get_data] = resb
        # print(res)
        # res = json.dumps(res)
        


        req = requests.put(url = fire_base_url,json=json.loads(res))
    def create_delete(self,*args):
        print("Botton Delete")


if __name__ == "__main__":
    KivyApp().run()