
def CustomValidation(start, end):
    # Custom Validation to check len of list and equal lenght of list
    if len(start) <= 2 and len(end) <= 2:
        print("{} {} Length of List is greater then 2 ".format(start, end))
    elif len(start) != len(end):
        print("Number of elements is not Equal")
    else:
        print("{} Number of activites for one person".format(NumberOfActivites(start, end)))

def NumberOfActivites(start, end):

    len_of_list = len(start)  # check len of list
    index_of_end = 0
    final_list = list() # Values of Activites
    for index_of_start in range(len_of_list):      
        if start[index_of_start] >= end[index_of_end]:
            index_of_end = index_of_start
            final_list.append(index_of_start)
    return final_list
if __name__ == "__main__":
    CustomValidation([1, 3, 2,5], [2,4,3,6])       # Enter Your List by replacing given list 
