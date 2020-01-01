#read a list of numbers and find the minimum  
def min_array(elements):
    min = elements[0]
    for item in elements:
        if min > item:
         min = item
    return min

if __name__ == '__main__':

    # count = int(input("Please enter the number of numbers dumma "))

    elements = list(map(int, input("please enter a string of numbers seperated by spaces to find the minimum : ").strip().split()))

    answer = min_array(elements)

    print(answer)
    
    #Check step
    built_in_answer = min(elements)

    if built_in_answer == answer:
        print("Validation success")
    else:
        print("Validation failure")

