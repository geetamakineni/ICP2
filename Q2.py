def string_alternative(input):
    lst_inp = list(input)
    lst_out =[]
    for i in range(len(lst_inp)):
        if (i%2==0):
            lst_out.append(lst_inp[i])
    str = ''.join(lst_out)
    return str
def __main():
    String = input(("Enter Input String:"))
    print("Input is:", String)
    return string_alternative(String)
print("Output is:",__main())