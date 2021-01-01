
#run the MODULE of MAIN FILE and import mainfile as a library 

import datastore as x 
#importing the main file("datastore" is the name of the file I have used) as a library 


x.create("sathyabama",25)
#to create a key with key_name,value given and with no time-to-live property


x.create("rahul",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("sathyabama")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("rahul")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("sathyabama",50)
#it returns an ERROR since the key_name already exists in the database

x.delete("sathyabama")
#it deletes the respective key and its value from the database(memory is also freed)
