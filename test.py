from phonenumbers import parse, phonenumberutil

mylist = open("recip_list_copy.txt","r")

for l in mylist: 
    try:   
        x = parse(l, None)
        print(x)
    except phonenumberutil.NumberParseException:
        print(l + " does not look like a phone number in E.164 format")        

mylist.close()
