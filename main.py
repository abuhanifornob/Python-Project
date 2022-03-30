email=input('Email Address: ')
s,u=0,0
if len(email)>=6:
    if email[0].isalpha():
        if '@' in email and (email.count('@')==1):
            if (email[-4]=='.' ) ^ ( email[-3]=='.' ):
                for i in email:
                    if i.isalpha():
                        if i==i.upper():
                            u=1
                    elif i==('_') or i==("@") or i==("."):
                        continue
                    elif i==i.isdigit():
                        continue
                    elif i ==i.isspace():
                        s=1
                if u==1 or s==1:
                    print(' Wrong Email 5')
            else:
                print(' Worng Email 4 ')
        else:
            print(" Worng Email 3")
    else:
        print(" Worng Email 2 ")
else:
    print(' Worng Email 1')
