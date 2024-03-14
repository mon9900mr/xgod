import time ,datetime ,platform ,requests ,os
def IP():
    Response = requests.get('https://api.ipify.org?format=json')
    IP_ADDR = Response.json()['ip']
ip_address = IP()
data = platform.system()
Name_PC = platform.node()
Time = datetime.datetime.now() 
Name_char = input('Enter User Name: ')
Question =  [
    'level 1 \nlanguage for programing security \nc++ ,html ,java ,javascript',
    'level 2 \noutput python: print("1" + "2") \n3 ,12 ,1+2 ,11',
    'level 3 \ncolor (0,255,0) \nblue ,green ,yellow ,red'
    
    ]
Answer = ['c++',
        '12',
        'green'
        ]
list_char = open('list.txt','r')
json = list(list_char)
for i in json:
    if json[2] == Name_PC and json[3] == ip_address:
        print('you have already tested!')
        time.sleep(3)
        os.system('exit')
    else:
        break
point = 0

for i in range(len(Question)) :
    print('point is :' ,point ,'\n' ,Question[i])
    test_input = input('Response: ')
    if test_input == Answer[i]:
        print('correct')
        point += 1
    else:
        print('incorrect')
        point -= 1
print('point is: ',point)
list_char = open('list.txt','a')
list_char.write('{'+f"Name: {Name_char} Type_system:{data} Name_PC: {Name_PC} IP: {ip_address} Point: {point} Time: {Time}"+'}\n')
time.sleep(2)
