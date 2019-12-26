#read a list of numbers and find the minimum  
def max_array(elements):
    array_length = len(elements)
    max_value = 0
    for i in range(0, array_length):
        if elements[i] > max_value:
         max_value = elements[i]
    return max_value

if __name__ == '__main__':

    # count = int(input("Please enter the number of numbers dumma "))

    elements = list(map(int, input("please enter a string of numbers seperated by spaces to find the Maximum : ").strip().split()))

    answer = max_array(elements)

    print(answer)
    
    #Check step
    built_in_answer = max(elements)
    print("Validation success" if built_in_answer == answer else "Validation Failure")
