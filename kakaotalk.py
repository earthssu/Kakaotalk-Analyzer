def input_most(word) :
    file = open("data.txt",'r')
    ssay = {}
    while True :
        line = file.readline()
        if word in line :
             if '[' in line :
                line = line.replace('[','')
                data = line.split(']')
                if data[0] in ssay :
                    ssay[data[0]] += 1
                else :
                    ssay[data[0]] = 1
        if not line: break
    file.close()
    a = 0
    for per in ssay :
        b = ssay[per]
        if a <=b :
            a = b
    print(a)

def all_people() :
    file = open("data.txt",'r')
    people_say = {}
    while True :
        line = file.readline()
        if '[' in line :
            line = line.replace('[','')
            data = line.split(']')
            if data[0] in people_say :
                people_say[data[0]] += 1
            else :
                people_say[data[0]] = 1
        if not line: break
    file.close()
    for name, counts in people_say.items():
        print(name, counts)
        

if __name__ == "__main__":                
    while True :
        num = int(input("수행할 번호 입력: "))
        if num is 1 :
            word = input("문자 입력 : ")
            input_most(word)
        elif num is 2 :
            all_people()
        else :
            break     
        
