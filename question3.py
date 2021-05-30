
def FindSubstringing(string_value):
 
    window_dic = {}
    start = end = 0
    low = high = 0
    while high < len(string_value):
        if window_dic.get(string_value[high]):
            while string_value[low] != string_value[high]:
                window_dic[string_value[low]] = False
                low = low + 1
 
            low = low + 1       
        else:
            window_dic[string_value[high]] = True
            
            if end - start < high - low:
                start = low
                end = high
 
        high = high + 1
 
    return string_value[start:end + 1]
 
 
if __name__ == '__main__':
 
    string_value = "geeksforgeeks"
    print(FindSubstringing(string_value))