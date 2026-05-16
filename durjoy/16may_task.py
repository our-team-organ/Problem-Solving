#!/usr/bin/env python3

# ===============================================
# >>> INITIALIZING SYSTEM . . .
# ===============================================
# FILE   : 16may_task.py
# AUTHOR : DURJOY-DEBUG
# DATE   : 2026-05-16
# STATUS : RUNNING
# ===============================================

def login():
    username=input("enter your username: ")
    password=input("enter your password(must be 8 characters): ")
    
    if len(password) >=8:
       print("hurreh! you logged in successfully")
    else:
       print("password is too short")
       login()

def register():
    username=input("enter your username: ")
    email=input("enter your email: ")
    phone_number=input("enter your phone number: ")
    password=input("enter your password(must be 8 characters): ")

    if len(password) >=8:
       print("hurreh! you registered successfully")
    else:
       print("password is too short")
       register()

def exit():
    print("exiting the system")

while True:
  user=input("enter your choice(1,2,3): ")
  if user =="1":
     login()
     break
  elif user == "2":
     register()
     break
  elif user == "3":
     exit()
     break
  else:
     print("invalid input")
    