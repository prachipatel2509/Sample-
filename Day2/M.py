result_str = ""
for r in range(0,7):
    for c in range(0,5):
        if(c==0 or c==4 or (c==1 and r==2) or (c==2 and r==3) or (c==3 and r==2)):
            result_str = result_str + "* "
        else:
            result_str = result_str + "  "
    result_str=result_str+"\n"
print(result_str)
