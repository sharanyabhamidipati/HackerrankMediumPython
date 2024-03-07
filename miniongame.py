def minion_game(string):
    # The Minion Game
    k_count=0
    s_count=0
  #The number of substrings equals to length of the string minus the index of the substring. 
  #Eg: for ANANA, the number of substrings are 'ANANA', 'ANAN', 'ANA', 'AN', 'A' which is 5. If you subtract total length minus the index, you will get the value.
  #For NANA you will get NANA, NAN, NA, N
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            k_count+=len(string)-i
        else:
            s_count+=len(string)-i
    if k_count>s_count:
        print('Kevin',k_count)
    elif k_count<s_count:
        print('Stuart',s_count)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
