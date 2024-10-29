def RotorStartPosition(Position):
    Order = []
    for i in len(Position):
        Order.append(int(Position[i]))
    return Order

Eintrittswalze = ""#Входное колесо

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

def Cipher(msg, Position, PlugPosition):
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
    
    RSP = list(str(int(Position)-111))# выбор стартового положения роторов
    if len(RSP) <3:
        RSP.insert(0, '0')
    
    cipher_msg = msg
    Steckerbrett(PlugPosition)#Прокидываем в программу положение проводов на панели
    replaceElements(cipher_msg)#Все Элементы проходят коммутационную панель на входе
    #шифрование от комм. панели до рефлектора
    
    #рефлектор
    
    #шифрование от Рефлектора до комм. панели
    
    replaceElements(cipher_msg)#Все Элементы проходят коммутационную панель на выходе
    
    
    
    
    
    
    
    
    
    return 0

