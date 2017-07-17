""" Finding missing value in a list
"""
def missing_numbers(num_list):
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))

if __name__=="__main__":
    n=input("Enter List: ")
    print(missing_numbers(n))
