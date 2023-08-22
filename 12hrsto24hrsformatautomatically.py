tim_e=input("enter the time")
#12:15:12 PM
print(len(tim_e))
print( tim_e[-2:])
if tim_e[-2:]=="PM":
    hr=tim_e[0:2]
    print( hr)
    if (int(hr)>= 1) and (int(hr)  < 12):
        hr = str(12+int(hr))
        print( hr)
    elif int(hr)==12:
        hr=12
    else:
        print("wrong num")
    print(str(hr)+tim_e[2:8])
else:
    hr=tim_e[0:2]
    if int(hr) ==12:
        hr="00"
        print(str(hr)+tim_e[2:8])
    else:
        print(tim_e[0:8])
        
        
 #   print(tim_e[0:8])
        
