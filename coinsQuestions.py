number = int (input ("n bnsdcbnasbn"))
fivenum = int ((number - 4) / 5) 
rem_value=number-(5*fivenum)
two_value=0
if rem_value%2==0:
    two_value=(rem_value//2)-1
    one_value=2
else:
    two_value=rem_value%2
    one_value=1
    
print(fivenum,two_value,one_value)
