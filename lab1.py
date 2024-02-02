'''
This function calculates the probability of 
playing tennis given the following features: 
outlook, temp, humid, wind, and tennis.
'''

def shouldPlay(outlook, temp, humid, wind):
    tennis = "yes"
    outlook = outlook.lower()
    temp = temp.lower()
    humid = humid.lower()
    wind = wind.lower()
    tennis = tennis.lower()
    outlook_lst = ["sunny", "sunny", "overcast", "rain", "rain", "rain", "overcast",
                   "sunny", "sunny", "rain", "sunny", "overcast", "overcast", "rain"]
    temp_lst = ["hot", "hot", "hot", "mild", "cool", "cool", "cool",
                "mild", "cool", "mild", "mild", "mild", "hot", "mild"]
    humid_lst = ["high", "high", "high", "high", "normal", "normal", "normal",
                 "high", "normal", "normal", "normal", "high", "normal", "high"]
    wind_lst = ["weak", "strong", "weak", "weak", "weak", "strong", "strong",
                "weak", "weak", "weak", "strong", "strong", "weak", "strong"]
    tn_lst = ["no", "no", "yes", "yes", "yes", "no", "yes",
              "no", "yes", "yes", "yes", "yes", "yes", "no"]
    if tennis not in tn_lst and outlook not in outlook_lst and temp not in temp_lst and humid not in humid_lst and wind not in wind_lst:
        return "Error: Invalid Input Value"
    
    p_indices = [index for index, value in enumerate(tn_lst) if value == tennis]
    not_p_indices = [index for index, value in enumerate(tn_lst) if value != tennis]
    
    p = len(p_indices) / 14 
    notP = len(not_p_indices) / 14
    
    oGivenP = sum(1 for index in p_indices if outlook_lst[index] == outlook)/p
    tGivenP = sum(1 for index in p_indices if temp_lst[index] == temp)/p
    hGivenP = sum(1 for index in p_indices if humid_lst[index] == humid)/p
    wGivenP = sum(1 for index in p_indices if wind_lst[index] == wind)/p
    
    
    oGivenNotP = sum(1 for index in not_p_indices if outlook_lst[index] == outlook)/notP
    tGivenNotP = sum(1 for index in not_p_indices if temp_lst[index] == temp)/notP
    hGivenNotP = sum(1 for index in not_p_indices if humid_lst[index] == humid)/notP
    wGivenNotP = sum(1 for index in not_p_indices if wind_lst[index] == wind)/notP
    
    givenP =  (oGivenP * tGivenP * hGivenP * wGivenP * p)
    notGivenP = (oGivenNotP * tGivenNotP * hGivenNotP * wGivenNotP * notP)
    if (givenP + notGivenP) == 0:
        return "Cannot calculate probabilities with zero probability of playing or not playing tennis."
    return round(givenP / (notGivenP + givenP), 3)
    # o_indices = len([outlook_lst[index] for index in p_indices if outlook_lst[index] == outlook])
    
if  __name__ == '__main__':
    
    # print(shouldPlay("sunny", "hot", "high", "weak"), "\n")
    print("sunny", "cool", "high", "strong")
    print(shouldPlay("sunny", "cool", "high", "strong"))
    
    # # Lists of possible values for each parameter
    # # tennis_values = ["no", "yes"]
    # outlook_values = ["sunny", "overcast", "rain"]
    # temp_values = ["hot", "mild", "cool"]
    # humid_values = ["high", "normal"]
    # wind_values = ["weak", "strong"]

    # # Iterate through all combinations
    # # for tennis in tennis_values:
    # for outlook in outlook_values:
    #     for temp in temp_values:
    #         for humid in humid_values:
    #             for wind in wind_values:
    #                 result = shouldPlay(outlook, temp, humid, wind)
    #                 print(f"Result for tennis= yes, outlook={outlook}, temp={temp}, humid={humid}, wind={wind}: {result}")
                        
    # print("---Error Testing---")
    # print(shouldPlay("sunny", "blah", "high", "strong"))
    
