import threading 
from threading import*
import time

db={} #'db' is the Database in which user stores the data

# we use create methode to create new key in database
# user have to use "create(key_name,value,ttl_value)" as syntax to create new key. as ttl is optional we can also continue by passing two arguments without ttl

def create(key,value,ttl=0):
    if key in db:            # checking whether the key is present in database or not
        print("error: this key already exists") 
    else:
        if(key.isalpha()):   #checking whether the key is a string or not
            if len(db)<(1024*1024*1024) and value<=(16*1024): #constraints for file size less than 1GB and Jsonobject value capped at 16KB 
                if ttl==0:
                    l=[value,ttl]
                else:
                    l=[value,time.time()+ttl]
                if len(key)<=32: #constraints for input key name capped at 32chars
                    db[key]=l
            else:
                print("error: Memory limit exceeded ")
        else:
            print("error: Invalid key name key name must contain only alphabets and no special characters or numbers are allowed")

#for delete operation
#use syntax "delete(key)"

def delete(key):
    if key not in db:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        i=db[key]
        if i[1]!=0:
            if time.time()<i[1]: #comparing the current time with expiry time
                del db[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del db[key]
            print("key is successfully deleted")
            

#for read operation
#use syntax "read(key)"
            
def read(key):
    if key not in db:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        i=db[key]
        if i[1]!=0:
            if time.time()<i[1]: #comparing the current time with expiry time
                stri=str(key)+":"+str(i[0]) #to print the value in the format of JsonObject i.e.,"key name:value"
                print(stri)
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(i[0])
            print(stri)
            
#this file based key value data store is purely built for Freshworks by Rahul  