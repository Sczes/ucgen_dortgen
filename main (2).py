cevap = input("Ucgenin mi Dortgenin mi tipini bulmak istiyorsunuz?").lower()
if(cevap == 'Dortgen'.lower()):
    k1 = int(input("Kenar giriniz: "))
    k2 = int(input("Kenar giriniz: "))
    k3 = int(input("Kenar giriniz: "))
    k4 = int(input("Kenar giriniz: "))
    if(k1==k2 and k2==k3 and k3==k4):
        print("Girilen uzunluklar kareye aittir.")
    elif((k1==k2 and k3==k4) or (k1==k3 and k2==k4) or (k1==k4 and k2==k3)):
        print("Girilen uzunluklar dikdörtgene aittir.")
    else:
        print("Bu herhangi bir dörtgen olabilir.")
elif(cevap == "Ucgen".lower()):
    a = int(input("Kenar girin: "))
    b = int(input("Kenar girin: "))
    c = int(input("Kenar girin: "))
    if(abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b):
        if(a==b and b==c):
            print("Girilen uzunluklar eskenar ucgene aittir.")
        elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("Girilen uzunluklar ikizkenar ucgene aittir.")
        else:
            print("Girilen uzunluklar cesitkenar ucgene aittir.")
    else:
        print("Ucgen belirtmiyor.")
else:
    print("Gecersiz sekil.")
            
            
            
    

