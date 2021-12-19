def count_substring(string, sub_string):
    z = 0
    for i in range (0,len(string)):
        if string[i:(i+int(len(sub_string)))] == sub_string:
            z += 1
    return z
string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print (count)