import random as r
import tkinter as tk
import customtkinter as CTk


class GiftApp:
   def __init__(self, master):
      self.players = ["E", "c", "a", "j", "s", "p"]
      self.master = master
      CTk.set_appearance_mode('dark')
      CTk.set_default_color_theme('blue')
      title = CTk.CTkLabel(self.master, text= 'Secret Santa Program', font=('Arial', 16))
      title.place(relx=0, rely=0)
      self.player_pick()


   def player_pick(self):
      pList1 = self.players
      pList2 = pList1.copy()
      partneredList = []
      for player in pList1:
         tempList = []
         for pair in pList2:
            if player != pair:
               tempList.append(pair)
         index = r.randint(0, len(tempList) - 1)
         print("index: "+ str(index))
         partner = tempList.pop(index)
         print("partner: "+ partner)
         pList2.remove(partner)
         print("pList2: "+ str(pList2))
         print("pList1: "+ str(pList1))

         partneredList.append([player, partner])
      print(partneredList)
      return partneredList
         
      

if __name__ == '__main__':
   root = CTk.CTk()
   root.title('Secret Santa Program')
   root.geometry('1920x1080')
   appRun = GiftApp(root)
   root.mainloop()
   # open GYI window for the purpose of input data, and output data




   
