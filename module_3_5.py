def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        rezul = first * get_multiplied_digits(int(str_number[1:]))
        # print(rezul)  #контроль
        return rezul
    else:
        return (int(str_number))


print(get_multiplied_digits(40203))
