import random
import string

#Метод генерации случайного порядка букв в алфавите для создания
#пар коммутационной панели
def SteckerbrettMachen():
    random_alphabet = list(string.ascii_uppercase)  
    random.shuffle(random_alphabet)  
    random_order = ''.join(random_alphabet)
    return(random_order)

#Чтобы каждый раз не прописывать переход с ротора на ротор, сделал функцию
#которая принимает на вход два списка и элемент сообщения
def LetterChanger(List1, List2, msg, increment):
    Index = List1.index(msg[increment])#Ищем номер элемента в 1 списке
    Buchstabe = List2[Index]#Берем элемент с таким же номером из 2 списка
    return Buchstabe #возвращаем элемент 2 списка

#я не помню для чего я это хотел использовать
def RotorStartPosition(Position):
    Order = []
    for i in range(0, len(Position)):
        Order.append(int(Position[i]))
    return Order

Eintrittswalze = ""#Входное колесо, имело смысл, но я сделал проще в итоге

def Steckerbrett(PlugPosition):
    PPZwei =PlugPosition[::-1]#Замена происходит и при обратном прохождении роторов, поэтому можно просто создать сразу
                            # обратные пары для коммутационной панели, так как метод replaceElements работает с левым
                            #символом каждой пары
    PlugOrder = []
    for l in range(0, len(PlugPosition), 2):
        PlugOrder.append((PlugPosition[l], PlugPosition[l+1]))
    for k in range(0, len(PPZwei), 2):
        PlugOrder.append((PPZwei[k], PPZwei[k+1]))
    return PlugOrder#Возвращаем список подключений, в котором лежат кортежи, показывающие соединения на комм. панели

def replaceElements(msg, PlugOrder):
    # Преобразуем строку в список символов для удобства замены
    msg_list = list(msg)
    
    for i in range(len(msg_list)):
        for pair in PlugOrder:
            if msg_list[i] == pair[0]:  # Проверяем, содержится ли элемент в PlugOrder
                msg_list[i] = pair[1]  # Заменяем на парный элемент
                break  # Прерываем внутренний цикл, чтобы избежать множественных замен

    # Преобразуем список обратно в строку
    return ''.join(msg_list)

def Cipher(msg, Position, Nummer1, Nummer2, Nummer3, PlugPosition):
    
    #роторы
    Umkehrwalze = "AYBRCUDHEQFSGLIPJXKNMOTZVW"#Рефлектор, реализация под вопросом, слишком уж геморно он устроен
    
    rotorEinz = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"#Порядок букв на роторах
    rotorEinzNotch = "Q"#Буква, к которой привязан поворот следующего ротора
    
    rotorZwei = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotorZweiNotch = "E"#Буква, к которой привязан поворот следующего ротора
    
    rotorDrei = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotorDreiNotch = "V"#Буква, к которой привязан поворот следующего ротора  

    rotors = [rotorEinz,rotorZwei,rotorDrei, rotorEinzNotch,  rotorZweiNotch,
               rotorDreiNotch, Umkehrwalze]
    #создал список rotors, для упрощения удобства выбора порядка роторов
    
    UmkehrwalzeList = []
    for i in range(len(Umkehrwalze)//2):
        UmkehrwalzeList.append((Umkehrwalze[i], Umkehrwalze[i+13] ))
        UmkehrwalzeList.append((Umkehrwalze[i+13], Umkehrwalze[i] ))
    
    RSP = list(str(int(Position)-111))# выбор стартового положения роторов
    if len(RSP) <3:
        RSP.insert(0, '0')
    
    
    cipher_msg = msg
    Plugs = Steckerbrett(PlugPosition)#Прокидываем в программу положение проводов на панели
    cipher_msg = replaceElements(cipher_msg, Plugs)#Все Элементы проходят коммутационную панель на входе
    #если провода в комм панели нет - то буква проходит сразу в ротор
    #шифрование от комм. панели до рефлектора
    #Печатаем алфавит, типа клавиатура на входе
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Делаем списки букв роторов, чтобы удобнее было к ним обращаться, так как список крутить удобнее, чем строку
    STRList = list(rotors[int(RSP[0])])
    R1R2List = list(rotors[int(RSP[1])])
    R2R3List = list(rotors[int(RSP[2])])
    ALIST = list(ALPHABET)
    old_msg = []
    new_msg = []
    for i in range(0, len(msg)):
        if cipher_msg[i] == " ":
            old_msg.append(" ")
        else:
            old_msg.append(LetterChanger(ALIST, STRList, cipher_msg, i))
            old_msg[i] = (LetterChanger(STRList, R1R2List, old_msg, i))
            old_msg[i] = (LetterChanger(R1R2List, R2R3List, old_msg, i))
        STRList = STRList[-13:] + STRList[:-13]
        R1R2List = R1R2List[-13:] + R1R2List[:-13]
        R2R3List = R2R3List[-13:] + R2R3List[:-13]
        if old_msg[i] == " ":
            new_msg.append(" ")
        else:
            new_msg.append(LetterChanger(R2R3List, R1R2List, old_msg, i))
            R2R3List = R2R3List[-1:] + R2R3List[:-1]
            if Nummer3 != len(rotorDrei)-1:
                Nummer3 += 1
            else:
                Nummer3 = 0
            if rotors[int(RSP[2])][Nummer3] != rotors[int(RSP[2])+3]:
                if Nummer2  != len(rotorDrei)-1:
                    Nummer2 +=1
                else:
                    Nummer2 = 0
            else:
                if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                    if Nummer1  != len(rotorEinz)-1:
                        Nummer1 +=1
                    else:
                        Nummer1 = 0
                    if Nummer3 != len(rotorEinz)-1:
                        Nummer3 += 1
                    else:
                        Nummer3 = 0
            new_msg[i] = (LetterChanger(R1R2List, STRList, new_msg, i))
            R1R2List = R1R2List[-1:] + R1R2List[:-1]
            if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                if Nummer1  != len(rotorEinz)-1:
                    Nummer1 +=1
                else:
                    Nummer1 = 0
            new_msg[i] = (LetterChanger(STRList, ALIST, new_msg, i))
            STRList = STRList[-1:] + STRList[:-1]
            
    preResult = ""
    for l in range (0, len(new_msg)):
        preResult = preResult + str(new_msg[l])
    cipher_msg = preResult
    #шифрование от Рефлектора до комм. панели
    
    cipher_msg = replaceElements(cipher_msg, Plugs)#Все Элементы проходят коммутационную панель на выходе
    
    return cipher_msg

def Decipher(msg, Position, Nummer1, Nummer2, Nummer3, PlugPosition):
    #тут надо сделать input для msg, Position и PlugPosition
    
    #роторы
    Umkehrwalze = "AYBRCUDHEQFSGLIPJXKNMOTZVW"#Рефлектор
    rotorEinz = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"#Порядок букв на роторах
    rotorEinzNotch = "Q"#Буква, к которой привязан поворот следующего ротора
    rotorZwei = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotorZweiNotch = "E"#Буква, к которой привязан поворот следующего ротора  
    rotorDrei = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotorDreiNotch = "V"#Буква, к которой привязан поворот следующего ротора  
    #Уточнение
    #Так как порядок роторов выбирается пользователем - поворотная буква определена для каждого ротора
    rotors = [rotorEinz,rotorZwei,rotorDrei, rotorEinzNotch,  rotorZweiNotch,
               rotorDreiNotch, Umkehrwalze]
    #создал список rotors, для упрощения удобства выбора порядка роторов
    
    UmkehrwalzeList = []
    for i in range(len(Umkehrwalze)//2):
        UmkehrwalzeList.append((Umkehrwalze[i], Umkehrwalze[i+13] ))
        UmkehrwalzeList.append((Umkehrwalze[i+13], Umkehrwalze[i] ))
    
    RSP = list(str(int(Position)-111))# выбор стартового положения роторов
    if len(RSP) <3:
        RSP.insert(0, '0')
    
    
    cipher_msg = msg
    Plugs = Steckerbrett(PlugPosition)#Прокидываем в программу положение проводов на панели
    cipher_msg = replaceElements(cipher_msg, Plugs)#Все Элементы проходят коммутационную панель на входе
    #шифрование от комм. панели до рефлектора
    
    #рефлектор
    #вопрос, нужно ли реализовывать подмену букв в рефлекторе, если я могу просто строку отправить дальше
    #пойдя по задней грани роторов
    #TODO
    #тут надо сдвинуть все роторы на 13 или другим путём обеспечить доступ к 
    #символам обратной стороны роторов, но проще всего +13 (половина символов ротора) делать
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Делаем списки букв роторов, чтобы удобнее было к ним обращаться, так как список крутить удобнее, чем строку
    STRList = list(rotors[int(RSP[0])])
    R1R2List = list(rotors[int(RSP[1])])
    R2R3List = list(rotors[int(RSP[2])])
    STRList = STRList[13:] + STRList[:13]
    R1R2List = R1R2List[-13:] + R1R2List[:-13]
    R2R3List = R2R3List[-13:] + R2R3List[:-13]
    ALIST = list(ALPHABET)
    old_msg = []
    new_msg = []
    for i in range(0, len(msg)):
        if cipher_msg[i] == " ":
            old_msg.append(" ")
        else:
            old_msg.append(LetterChanger(ALIST, STRList, cipher_msg, i))
            old_msg[i] = (LetterChanger(STRList, R1R2List, old_msg, i))
            old_msg[i] = (LetterChanger(R1R2List, R2R3List, old_msg, i))
        STRList = STRList[13:] + STRList[:13]
        R1R2List = R1R2List[13:] + R1R2List[:13]
        R2R3List = R2R3List[13:] + R2R3List[:13]
        if old_msg[i] == " ":
            new_msg.append(" ")
        else:
            new_msg.append(LetterChanger(R2R3List, R1R2List, old_msg, i))
            R2R3List = R2R3List[-1:] + R2R3List[:-1]
            if Nummer3 != len(rotorDrei)-1:
                Nummer3 += 1
            else:
                Nummer3 = 0
            if rotors[int(RSP[2])][Nummer3] != rotors[int(RSP[2])+3]:
                if Nummer2  != len(rotorDrei)-1:
                    Nummer2 +=1
                else:
                    Nummer2 = 0
            else:
                if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                    if Nummer1  != len(rotorEinz)-1:
                        Nummer1 +=1
                    else:
                        Nummer1 = 0
                    if Nummer3 != len(rotorEinz)-1:
                        Nummer3 += 1
                    else:
                        Nummer3 = 0
            new_msg[i] = (LetterChanger(R1R2List, STRList, new_msg, i))
            R1R2List = R1R2List[-1:] + R1R2List[:-1]
            if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                if Nummer1  != len(rotorEinz)-1:
                    Nummer1 +=1
                else:
                    Nummer1 = 0
            new_msg[i] = (LetterChanger(STRList, ALPHABET, new_msg, i))
            STRList = STRList[-1:] + STRList[:-1]
            
    preResult = ""
    for l in range (0, len(new_msg)):
        preResult = preResult + str(new_msg[l])
    cipher_msg = preResult
    #шифрование от Рефлектора до комм. панели
    
    cipher_msg = replaceElements(cipher_msg, Plugs)#Все Элементы проходят коммутационную панель на выходе
    
    return cipher_msg

# print(Cipher("DAS IST GUT", 123, 1, 2, 3, "FNXEKSIYBWQLCRGAVDUPZHOMTJ"))
# print(Decipher("YJE QEB FRB", 123, 1, 2, 3, "FNXEKSIYBWQLCRGAVDUPZHOMTJ"))
# print(SteckerbrettMachen())


