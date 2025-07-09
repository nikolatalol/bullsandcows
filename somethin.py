def main(input):
    def guess(number1,number2):
        number1=str(number1)
        number2=str(number2)
        bulls=0
        cows=0
        for i in range(len(number1)):
            if number1[i] == number2[i]:
                bulls+=1
            elif number1[i] in number2:
                cows+=1
            else:
                continue
        return bulls,cows

    def swap(number,digit1,digit2):
        number_convert=list(number)
        number_convert[digit1],number_convert[digit2]=number_convert[digit2],number_convert[digit1]
        number="".join(number_convert)
        return number

    while True:
        try:
            player_input=int(input)
            if len(str(player_input))!=3:
                continue
            elif len(str(player_input)) != len(set(str(player_input))):
                continue
            elif "0" in str(player_input):
                continue
            break
        except ValueError:
            continue


    algo1=algo2=algo3=algo3_check=False
    number_list=[]

    for secret in [123,456,789]:
        bulls,cows=guess(secret,player_input)

        if bulls+cows>=3:
            algo1=True
            number_list.append([secret,bulls,cows])
            break
        elif bulls+cows==2:
            algo2=True
            algo2_number=str(secret)
            number_list.append([secret,bulls,cows])
        elif bulls+cows==1:
            if not number_list:
                algo3_check = True
            elif algo3_check and not algo2:
                algo3 = True
            number_list.append([secret,bulls,cows])
        
    digit_index = None
    second_index = None
    number_guess="000"
    if algo3:
        for i,number_stat in enumerate(number_list):
            number=str(number_stat[0])
            if i==0:
                if number_stat[2]==1:
                    #213
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    if cows==1:
                        temp_number=swap(number,2,1)
                        #132
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            temp_number=swap(number,1,2)
                            #132
                            temp_number=swap(temp_number,0,1)
                            #312
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[0]
                            elif bulls==1:
                                digit_index=0
                                number_guess=number[2]+number_guess[1:]
                        elif bulls==1:
                            temp_number=swap(number,1,0)
                            #213
                            temp_number=swap(temp_number,2,1)
                            #231
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[1]
                            elif bulls==1:
                                digit_index=1
                                number_guess=number_guess[0]+number[2]+number_guess[2]
                    elif bulls==1:
                        temp_number=swap(number,1,0)
                        #213
                        temp_number=swap(temp_number,2,1)
                        #231
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[0]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[1]+number_guess[1:]
                elif number_stat[1]==1:
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    #213
                    if cows==1:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[1]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[0]+number_guess[1:]
                    elif bulls==1:
                        digit_index=2
                        number_guess=number_guess[:2]+number[2]
            elif i==1:
                if number_stat[2]==1:
                    if digit_index==0:
                        temp_number=swap(number,1,2)
                    elif digit_index==1:
                        temp_number=swap(number,0,2)
                    elif digit_index==2:
                        temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    #465
                    if cows==1:
                        if digit_index==0:
                            temp_number=swap(number,0,1)
                        elif digit_index==1:
                            temp_number=swap(number,1,2)
                        elif digit_index==2:
                            temp_number=swap(number,2,1)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            if digit_index==0:
                                second_index=1
                                number_guess=number_guess[:2]+number[0]
                            elif digit_index==1:
                                second_index=2
                                number_guess=number[1]+number_guess[1:]
                            elif digit_index==2:
                                second_index=1
                                number_guess=number[2]+number_guess[1:]
                        elif bulls==1:
                            if digit_index==0:
                                second_index=2
                                number_guess=number_guess[0]+number[0]+number_guess[2]
                            elif digit_index==1:
                                second_index=0
                                number_guess=number_guess[:2]+number[1]
                            elif digit_index==2:
                                second_index=0
                                number_guess=number_guess[0]+number[2]+number_guess[2]
                    elif bulls==1:
                        if digit_index==0:
                            temp_number=swap(temp_number,0,1)
                        elif digit_index==1:
                            temp_number=swap(temp_number,1,2)
                        elif digit_index==2:
                            temp_number=swap(temp_number,2,1)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            if digit_index==0:
                                second_index=2
                                number_guess=number_guess[0]+number[2]+number_guess[2]
                            elif digit_index==1:
                                second_index=0
                                number_guess=number_guess[:2]+number[0]
                            elif digit_index==2:
                                second_index=0
                                number_guess=number_guess[0]+number[0]+number_guess[2]
                        elif bulls==1:
                            if digit_index==0:
                                second_index=1
                                number_guess=number_guess[:2]+number[1]
                            elif digit_index==1:
                                second_index=2
                                number_guess=number[2]+number_guess[1:]
                            elif digit_index==2:
                                second_index=1
                                number_guess=number[1]+number_guess[1:]
                elif number_stat[1]==1:
                    if digit_index==0:
                        temp_number=swap(number,0,1)
                    elif digit_index==1:
                        temp_number=swap(number,1,0)
                    elif digit_index==2:
                        temp_number=swap(number,2,1)
                    bulls,cows=guess(temp_number,player_input)

                    if cows==1:
                        if digit_index==0:
                            second_index=2
                            number_guess=number_guess[0]+number[1]+number_guess[2]
                        elif digit_index==1:
                            second_index=2
                            number_guess=number[0]+number_guess[1:]
                        elif digit_index==2:
                            second_index=0
                            number_guess=number_guess[0]+number[1]+number_guess[2]
                    elif bulls:
                        if digit_index==0:
                            second_index=1
                            number_guess=number_guess[:2]+number[2]
                        elif digit_index==1:
                            second_index=0
                            number_guess=number_guess[:2]+number[2]
                        elif digit_index==2:
                            second_index=1
                            number_guess=number[0]+number_guess[1:]
            elif i==2:
                if number_stat[2]==1:
                    if second_index==0:
                        temp_number=swap(number,1,0)
                    elif second_index==1:
                        temp_number=swap(number,0,1)
                    elif second_index==2:
                        temp_number=swap(number,1,2)
                    bulls,cows=guess(temp_number,player_input)
                    if cows==1:
                        if second_index==0:
                            number_guess=number[2]+number_guess[1:]
                        elif second_index==1:
                            number_guess=number_guess[0]+number[2]+number_guess[2]
                        elif second_index==2:
                            number_guess=number_guess[:2]+number[0]
                    elif bulls==1:
                        if second_index==0:
                            number_guess=number[1]+number_guess[1:]
                        elif second_index==1:
                            number_guess=number_guess[0]+number[0]+number_guess[2]
                        elif second_index==2:
                            number_guess=number_guess[:2]+number[1]
                elif number_stat[1]==1:
                    if second_index==0:
                        number_guess=number[0]+number_guess[1:]
                    elif second_index==1:
                        number_guess=number_guess[0]+number[1]+number_guess[2]
                    elif second_index==2:
                        number_guess=number_guess[:2]+number[2]
    elif algo2:
        for i,number_stat in enumerate(number_list):
            number=str(number_stat[0])
            if algo2_number!=number and i==0:
                if number_stat[2]==1:
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    if cows==1:
                        temp_number=swap(number,2,1)
                        #132
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            temp_number=swap(number,1,2)
                            #132
                            temp_number=swap(temp_number,0,1)
                            #312
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[0]
                            elif bulls==1:
                                digit_index=0
                                number_guess=number[2]+number_guess[1:]
                        elif bulls==1:
                            temp_number=swap(number,1,0)
                            #213
                            temp_number=swap(temp_number,2,1)
                            #231
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[1]
                            elif bulls==1:
                                digit_index=1
                                number_guess=number_guess[0]+number[2]+number_guess[2]
                    elif bulls==1:
                        temp_number=swap(number,1,0)
                        #213
                        temp_number=swap(temp_number,2,1)
                        #231
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[0]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[1]+number_guess[1:]
                elif number_stat[1]==1:
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    #213
                    if cows==1:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[1]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[0]+number_guess[1:]
                    elif bulls==1:
                        digit_index=2
                        number_guess=number_guess[:2]+number[2]
            elif algo2_number==number and i==1:
                if number_stat[2]==2:
                    if digit_index==0:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number_guess[0]+number[2]+number[1]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number_guess[0]+number[2]+number[0]
                            elif cows==1 and bulls==1:
                                number_guess=number_guess[0]+number[0]+number[1]
                    elif digit_index==1:
                        temp_number=swap(number,0,2)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number[2]+number_guess[1]+number[0]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number[2]+number_guess[1]+number[1]
                            elif cows==1 and bulls==1:
                                number_guess=number[1]+number_guess[1]+number[0]
                    elif digit_index==2:
                        temp_number=swap(number,0,1)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number[1]+number[0]+number_guess[2]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,1,2)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number[2]+number[0]+number_guess[2]
                            elif cows==1 and bulls==1:
                                number_guess=number[1]+number[2]+number_guess[2]
                elif number_stat[1]==2:
                    if digit_index==0:
                        number_guess=number_guess[0]+number[1:]
                    elif digit_index==1:
                        number_guess=number[0]+number_guess[1]+number[2]
                    elif digit_index==2:
                        number_guess=number[:2]+number_guess[2]
                elif number_stat[1]==1 and number_stat[2]==1:
                    if digit_index==0:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,2)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number_guess[0]+number[1]+number[0]
                            elif cows==2:
                                number_guess=number_guess[0]+number[0]+number[2]
                    elif digit_index==1:
                        temp_number=swap(number,0,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number[1]+number_guess[1]+number[2]
                            elif cows==2:
                                number_guess=number[0]+number_guess[1]+number[1]
                    elif digit_index==2:
                        temp_number=swap(number,0,1)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,2)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number[2]+number[1]+number_guess[2]
                            elif cows==2:
                                number_guess=number[0]+number[2]+number_guess[2]
            elif algo2_number==number and i==0:
                number=str(number_list[1][0])
                if number_list[1][2]==1:
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    if cows==1:
                        temp_number=swap(number,2,1)
                        #132
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            temp_number=swap(number,1,2)
                            #132
                            temp_number=swap(temp_number,0,1)
                            #312
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[0]
                            elif bulls==1:
                                digit_index=0
                                number_guess=number[2]+number_guess[1:]
                        elif bulls==1:
                            temp_number=swap(number,1,0)
                            #213
                            temp_number=swap(temp_number,2,1)
                            #231
                            bulls,cows=guess(temp_number,player_input)
                            if cows==1:
                                digit_index=2
                                number_guess=number_guess[:2]+number[1]
                            elif bulls==1:
                                digit_index=1
                                number_guess=number_guess[0]+number[2]+number_guess[2]
                    elif bulls==1:
                        temp_number=swap(number,1,0)
                        #213
                        temp_number=swap(temp_number,2,1)
                        #231
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[0]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[1]+number_guess[1:]
                elif number_list[1][1]==1:
                    temp_number=swap(number,0,1)
                    bulls,cows=guess(temp_number,player_input)
                    #213
                    if cows==1:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==1:
                            digit_index=1
                            number_guess=number_guess[0]+number[1]+number_guess[2]
                        elif bulls==1:
                            digit_index=0
                            number_guess=number[0]+number_guess[1:]
                    elif bulls==1:
                        digit_index=2
                        number_guess=number_guess[:2]+number[2]
            elif algo2_number!=number and i==1:
                number=str(number_list[0][0])
                if number_list[0][2]==2:
                    if digit_index==0:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number_guess[0]+number[2]+number[1]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number_guess[0]+number[2]+number[0]
                            elif cows==1 and bulls==1:
                                number_guess=number_guess[0]+number[0]+number[1]
                    elif digit_index==1:
                        temp_number=swap(number,0,2)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number[2]+number_guess[1]+number[0]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number[2]+number_guess[1]+number[1]
                            elif cows==1 and bulls==1:
                                number_guess=number[1]+number_guess[1]+number[0]
                    elif digit_index==2:
                        temp_number=swap(number,0,1)
                        bulls,cows=guess(temp_number,player_input)
                        if bulls==2:
                            number_guess=number[1]+number[0]+number_guess[2]
                        elif bulls==1 and cows==1:
                            temp_number=swap(number,1,2)
                            bulls,cows=guess(temp_number,player_input)
                            if cows==2:
                                number_guess=number[2]+number[0]+number_guess[2]
                            elif cows==1 and bulls==1:
                                number_guess=number[1]+number[2]+number_guess[2]
                elif number_list[0][1]==2:
                    if digit_index==0:
                        number_guess=number_guess[0]+number[1:]
                    elif digit_index==1:
                        number_guess=number[0]+number_guess[1]+number[2]
                    elif digit_index==2:
                        number_guess=number[:2]+number_guess[2]
                elif number_list[0][1]==1 and number_list[0][2]==1:
                    if digit_index==0:
                        temp_number=swap(number,1,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,2)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number_guess[0]+number[1]+number[0]
                            elif cows==2:
                                number_guess=number_guess[0]+number[0]+number[2]
                    elif digit_index==1:
                        temp_number=swap(number,0,2)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,1)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number[1]+number_guess[1]+number[2]
                            elif cows==2:
                                number_guess=number[0]+number_guess[1]+number[1]
                    elif digit_index==2:
                        temp_number=swap(number,0,1)
                        bulls,cows=guess(temp_number,player_input)
                        if cows==2:
                            temp_number=swap(temp_number,0,2)
                            bulls,cows=guess(temp_number,player_input)
                            if bulls==1 and cows==1:
                                number_guess=number[2]+number[1]+number_guess[2]
                            elif cows==2:
                                number_guess=number[0]+number[2]+number_guess[2]
    elif algo1:
        for i,number_stat in enumerate(number_list):
            number=str(number_stat[0])
            if number=="123":
                nothing_number='456'
            elif number=='456':
                nothing_number='123'
            elif number=='789':
                nothing_number='123'
            if number_stat[1]==3:
                number_guess=number
            elif number_stat[2]==3:
                temp_number=nothing_number[:2]+number[0]
                bulls,cows=guess(temp_number,player_input)
                if cows==1:
                    digit_index=1
                    number_guess=number_guess[0]+number[0]+number_guess[2]
                elif bulls==1:
                    digit_index=2
                    number_guess=number_guess[:2]+number[0]
                if digit_index==1:
                    number_guess=number[2]+number_guess[1]+number[1]
                elif digit_index==2:
                    number_guess=number[1]+number[2]+number_guess[2]
            elif number_stat[2]==2 and number_stat[1]==1:
                temp_number=nothing_number[:2]+number[2]
                bulls,cows=guess(temp_number,player_input)
                if cows==1:
                    temp_number=nothing_number[0]+number[1]+nothing_number[2]
                    bulls,cows=guess(temp_number,player_input)
                    if cows==1:
                        digit_index=0
                        number_guess=number[0]+number_guess[1:]
                    elif bulls==1:
                        digit_index=1
                        number_guess=number_guess[0]+number[1]+number_guess[2]
                elif bulls==1:
                    digit_index=2
                    number_guess=number_guess[:2]+number[2]
                if digit_index==0:
                    number_guess=number_guess[0]+number[2]+number[1]
                elif digit_index==1:
                    number_guess=number[2]+number_guess[1]+number[0]
                elif digit_index==2:
                    number_guess=number[1]+number[0]+number_guess[2]
    return number_guess


