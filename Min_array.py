#read a list of numbers and find the minimum  
if __name__ == '__main__':

    # count = int(input("Please enter the number of numbers dumma "))

    elements = list(map(int, input("please enter a string of numbers seperated by spaces to find the minimum : ").strip().split()))

    answer = min(elements)

    print(answer)
