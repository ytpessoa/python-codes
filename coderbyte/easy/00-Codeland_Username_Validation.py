# Codeland Username Validation
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is 
# a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.
# Examples

# Input: "aa_"
# Output: false

# Input: "u__hello_world123"
# Output: true

#Solution 1
def CodelandUsernameValidation(str):
    string = str
    size = len(string)
   
    if( not(size >=4 and size <= 25)  ):
        return "false"
        
    
    if( not(string[0].isalpha() and string[-1] != '_' and (string[-1].isalpha() or string[-1].isnumeric()))   ):
        return "false"
    
    for i in string[1:-1]:
        if( i.isalpha() or i.isnumeric() or i == '_' ):
            pass
        else:
            return "false"
            

    return "true"        

#Solution 2:
# function CodelandUsernameValidation(str) { 

#   // code goes here  
#   const valid_reg = /^[A-Za-z]\w+[A-Za-z0-9]$/;
#   const valid_length = (str) => str.length >= 4 && str.length <= 25;
#   return valid_reg.test(str) && valid_length(str);
# }        

#Solution 3:
# function CodelandUsernameValidation(str) {
#   const regex = /^[a-zA-Z][a-zA-Z0-9_]*[^_]$/g
#   return str.length >= 4 && str.length <= 25 && regex.test(str)
# }
   

print (CodelandUsernameValidation("b3333434_"))
