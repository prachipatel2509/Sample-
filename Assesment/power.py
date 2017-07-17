def Power(n):
        return n > 0 and (n & (n - 1)) == 0

if __name__=="__main__":
        n=int(input("Enter a no.: "))
        print(Power(n))
