# Questions Marks
# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers 
# that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 
# 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

# Examples

# Input: "aa6?9"
# Output: false

# Input: "acc?7??sss?3rr1??????5"
# Output: true

#char --> str
def QuestionsMarks(string):
     
  if( len(string) >=5 ):    
    sum10=0
    for i, char in enumerate(string):           
      if(char.isdigit() and int(char)<=10):   #"7??sss?3rr1??????5"       
        sum10 += int(char)
        #print(f"sum10:{sum10}")
        count = 0
        for j, char2 in enumerate(string[i+1:]):              
              if(char2 == '?' and count <=2):
                  count +=1
                  #print(f"aqui char:{char} char2:{char2} count:{count}")
              elif(char2.isdigit() and count == 3 ):
                  sum10 += int(char2)
                  if(sum10 == 10):
                    return "true"
                  else:
                    return "false"
              else:
                  continue                             
      else:
        continue
    else:
      return "false"  
  else:
      return "false"
      

# 1. For input "9???1???9??1???9" the output was incorrect. The correct output is false

# 2. For input "5??aaaaaaaaaaaaaaaaaaa?5?5" the output was incorrect. The correct output is false

QuestionsMarks("arrb6???4xxbl5???eee5")