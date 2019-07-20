#Filename continue.py
while True:
    s = input('Enter something here: ')
    if s =="quit":
        break
    elif len(s)<3:
        continue
    else:
        print ('Input is of sufficient length')
print('Done.')