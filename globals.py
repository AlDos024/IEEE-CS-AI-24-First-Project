import os
from time import sleep

def cls(n):
    sleep(n)
    os.system('cls' if os.name=='nt' else 'clear')

id = 0
students = {}
loaded = False
added = False
updated = False
deleted = False

