import sys
import re

s=sys.argv[1]
s1="(\D+$+)@(\D+$+).(com)"
s2=re.match(s1,s)


print(s2.group(1))
