# mystr = "HellO"
# ans=""

# for i in range(len(mystr)):
#     if ord(mystr[i]) > 90:
#         ans += mystr[i]
#     else:
#         ans += chr(ord(mystr[i]) + ord('a') - ord('A'))

# print(ans)

# # Check if the given string is a palindrome
# given_string = "HelleH"
# isPalindrome = True
# for i in range(len(given_string) // 2):
#     if given_string[i] != given_string[len(given_string) - i - 1]:
#         isPalindrome = False
#         break
# if isPalindrome:
#     print("The given string is a palindrome")
# else:
#     print("The given string is not a palindrome")

#split binary string into two parts
bstr = "1100101011"
countzeros = 0
countones= 0
for i in bstr:
    if i == '0':
        countzeros += 1
    else:
        countones += 1

if countzeros%2 == 1 or countones%2 == 1:
    print("-1")
else:
    currones = 0
    currzeros = 0
    for i in range(len(bstr)//2):
        if bstr[i] == "1":
            currones += 1
        else:
            currzeros += 1
    
    if currones == countones // 2 and currzeros == countzeros // 2:
        for i in range(len(bstr)//2):
            print(bstr[i], end="")
        print(" ", end="")
        for i in range(len(bstr)//2, len(bstr)):
            print(bstr[i], end="")
        print("", end="")
    else:
        print("-1")