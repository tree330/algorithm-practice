a,b= map(int, (input().split()))
yoil=0
while b>6:
     b=b-7     
if a==1 or a==10:
    yoil=yoil+b+6
elif a==2 or a==3 or a==11:
    yoil=yoil+b+2    
elif a==4 or a==7:
    yoil=yoil+b+5
elif a==5:
    yoil=yoil+b 
elif a==8:
    yoil=yoil+b+1
elif a==6:
    yoil=yoil+b+3                       
if a==9 or a==12:
    yoil=yoil+b+4       
if yoil%7==0:
        print("MON")     
elif yoil%7==1:
        print("TUE")
elif yoil%7==2:
        print("WED")
elif yoil%7==3:
        print("THU")
elif yoil%7==4:
        print("FRI")
elif yoil%7==5:
        print("SAT")
elif yoil%7==6:
        print("SUN") 

    