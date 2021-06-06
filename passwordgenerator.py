import string
import random

if __name__ == "__main__":
    al = string.ascii_lowercase
    au = string.ascii_uppercase
    d = string.digits
    p = string.punctuation
    plength = int(input("Enter password length\n"))
    
    time = ((95**plength)/30000000)
    hour=time/60
    day=hour/24
    
    if plength < 6:
      print("A password of length "+str(plength)+" is insecure, and it can be cracked by brute force in just " +str(round(day,4))+" days or " +str(round(hour,4))+" hours. Hence we suggest that you choose a password of length 6 or higher")
      plength = int(input("Enter password length\n"))
      time = ((95**plength)/30000000)
      hour=time/60
      day=hour/24
    s = []
    s.extend(list(al))
    s.extend(list(au))
    s.extend(list(d))
    s.extend(list(p))
    print("Your password is: ")
    print("".join(random.sample(s, plength)))
    print("This password can be cracked by brute force in " +str(round(day,4))+ " days or " +str(round(hour,4))+ " hours. ")
