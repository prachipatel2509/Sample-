import re
a=raw_input()
if re.search("[aeiouAEIOU]",a):
    print("Vowel")
else:
    print("Consonant")    
