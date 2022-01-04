#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Food_App:
    def __init__(self):
        self.Food_list=[]
        self.Food_menu={}
        self.User_details=[]
        self.order=[]
    def SignUp(self):
        while True:
            S=input("Log In as \n 1.Admin\n 2.Customer\n 3.Exit\n")
            if S=="1":
                enter=input("Enter your choice\n 1.Add_food\n 2.Edit_food\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="1":
                    self.add_food()
                    enter=input("Enter your choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="2":
                    self.edit_food()
                    enter=input("Enter your choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="3":
                    self.list_of_food()
                    enter=input("Enter your choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                if enter=="4":
                    self.remove_food()
                    enter=input("Enter your choice\n 1.add_food\n 2.edit\n 3.list_of_foods\n 4.Remove_foods\n 5.Exit\n")
                else:
                    pass
            elif S=='2':
                choice=input("Enter your Choice\n 1.Register\n 2.Login\n")
                if choice=="1":
                    self.REgistration()
                    choice=input("Enter Choice\n 1.Register\n 2.Login\n") 
                if choice=="2":
                    self.login()
                    choice=input("Enter Choice\n 1.Register\n 2.Login\n")
                else:
                    pass
            else:
                print("wrong option")
                break
     
    def add_food(self):
        while True:
            variable=input("Do you want to add food (Y/N): ")
            
            if variable=="Y":
                try:
                    foods=input("Enter the name of food: ")
                    price=int(input("Enter the price of food: "))
                    quantity=int(input("Enter the quantity of food: "))
                    self.FOOD_Id=len(self.Food_menu)+1
                    self.Food_menu[self.FOOD_Id]={"Food name":foods,"Quantity":quantity,"price":price}
                    print("Here is the Food ID",self.FOOD_Id)
                    print("Here is the Menu : ",self.Food_menu)
                    self.Food_list.append(self.Food_menu[self.FOOD_Id])
                except KeyError:
                    print("Key Error")
            else:
                
                print("Thank you")
                break
        
    def edit_food(self):
        while True:
            var=input("Do you want to edit food (Y/N): ")
            if var=='Y':
                print("Press 1 to see the food list")
                print("Press 2 to quit")
                n=int(input("Enter your choice:  "))
                if n==1:
                    print("Food list",self.Food_menu)
                    v=int(input("Enter the food id if want to edit: "))
                    k=int(input("Enter the option which you want to edit\n 1.Food name\n 2.qty\n 3.price\n 4.Edit whole items\n 0.exit\n"))
                    if k==1:
                        print(self.Food_menu[v])
                        b=input("Enter the food name you want to edit: ")
                        self.Food_menu[v]["Food name"]=b
                        print( self.Food_menu)
                    elif k==2:
                        print(self.Food_menu[v])
                        a=input("Enter the food Quantity you want to edit: ")
                        self.Food_menu[v]["Quantity"]=a
                        print(self.Food_menu)
                    elif k==3:
                        print(self.Food_menu[v])
                        c=input("Enter the food Price you want to edit: ")
                        self.Food_menu[v]["price"]=c
                        print(self.Food_menu)
                    elif k==4:
                        print(self.Food_menu[v])
                        b=input("Enter the food name you want to edit: ")
                        a=input("Enter the food Stock you want to edit: ")
                        c=input("Enter the food Price you want to edit: ")
                        self.Food_menu[v]["Food name"]=b
                        self.Food_menu[v]["Quantity"]=a
                        self.Food_menu[v]["price"]=c
                        print(self.Food_menu)
                    elif k==0:
                        print("Thank You")
                elif n==2:
                    print("Thank You")
            else:
                break
                
    def remove_food(self):
        print(self.Food_menu)
        delete=int(input("Enter the food id you want to delete:  "))
        self.Food_menu.pop(delete)
        print("\nyour food is removed.",self.Food_menu)
    def list_of_food(self):
        print("Here is the list of food:")
        for i in self.Food_menu:
            print("Food Name: ",self.Food_menu[i]["Food name"])
            print("Quantity   : ",self.Food_menu[i]["Quantity"])
            print("Price    : ",self.Food_menu[i]["price"])
            
    def REgistration(self):
        
        print("Register on the Application : ")
        self.user_data={}
        Full_Name=input("Enter your full name :")
        Phone_No=input("Enter your phone number :")
        Email=input("Enter your email : ")
        Address=input("Enter your address :")
        Password=input("Enter your password :")
        print("\nYou have registered successfully.")
        self.user_data["Name"]=Full_Name
        self.user_data["Mobile"]=Phone_No
        self.user_data["Mail"]=Email
        self.user_data["Address"]=Address
        self.user_data["Password"]=Password
        
    
        
    def login(self):
      #  print("\nFrom here you can log in.")
        while True:
            print("\nFrom here you can log in.")
            Full_Name=input("\nEnter your Name for login : ")
            Password=input("Enter your passward :")
            if self.user_data["Name"]==Full_Name:
                if self.user_data["Password"]==Password:
                    print("\nlogin successfull")
                    while True:

                        user_input=int(input("\nPlease enter your preference :\n 1.Place New Order\n 2.order history\n 3.update profile :\n ENter your choice :"))
                        if user_input==1:
                            print("\nplease select your preference from below list :.")
                            self.show_foodlist()
                        elif user_input==2:
                            print("\nIF you want to see your order history please enter your name and number.")
                            self.order_history()
                        elif user_input==3:
                            print("\nUpdate your profile:")
                            self.update_profile()
                        else:
                            print("\nSorry!! you chosed a wrong digit.")
                            break

            else:
                print("\nPlease enter correct name and password.")
                break


            
    def show_foodlist(self):
       
        print("\nHere is the food list.")
        for i in self.Food_list:
            print(f"{self.Food_list.index(i)+1}. {i['Food name']} ({i['Quantity']}) [INR {i['price']}]")

        while True:
            user_choice=input("\nif you want to chose any item enter yes else no:")
            if user_choice=="yes":
                user_input=int(input("\nPlease select your choice by the FoodId number of the food :"))
                print("\nHere is your selected order : ",self.Food_list[(user_input)-1])
                items=self.Food_list[(user_input)-1]
                self.order.append(items)
            
            else:
                print("Not available")
                break
        
        
        print("\nHere is your complete items list :",self.order)
        confirmation=(input("\nDo you want to PLace the order:\n 1.yes\n 2.no\n "))
        if confirmation=="yes":
            print("\nyour order is placed.")
        else:
            print("\nyour order is canceled.")
            
    def order_history(self):
        Name=input("\nplease enter your registered name : ")
        Phone=input("please enter your registered phone number :")
        if Name==self.user_data["Name"]:
            if Phone==self.user_data["Mobile"]:
                print("\nHere is your order history :",self.order)
        else:
            print("\nNo previous order")
            
    def update_profile(self):
        print("\nIF you want to update your profile please fill below: ")
        while True:
            preference=int(input("\nEnter your choice :\n 1.Name\n 2.Number\n 3.Mail\n 4.Address\n 5.Password\n 6.Exit."))
            if preference==1:
                New_name=input("\nEnter your name :")
                self.user_data["Name"]=New_name
                self.User_details.append(self.user_data)
                print("\nHere is you new details :",self.User_details)
            elif preference==2:
                Number=input("Enter your number :")
                self.user_data["Mobile"]=Number
                self.User_details.append(self.user_data)
                print("\nHere is you new details :",self.User_details)
            elif preference==3:
                New_mail=input("Enter your Email :")
                self.user_data["Mail"]=New_mail
                self.User_details.append(self.user_data)
                print("\nHere is you new details :",self.User_details)

            elif preference==4:   
                New_address=input("Enter your address :")
                self.user_data["Address"]=New_address
                self.User_details.append(self.user_data)
                print("\nHere is you new details :",self.User_details)
            elif preference==5:
                New_password=input("Enter your password :")
                self.user_data["Password"]=New_password
                self.User_details.append(self.user_data)
                print("\nHere is you new details :",self.User_details)
            else:
                break

            


# In[15]:


a=Food_App()


# In[ ]:


a.SignUp()


# In[ ]:


a.Food_list


# In[ ]:





#  
