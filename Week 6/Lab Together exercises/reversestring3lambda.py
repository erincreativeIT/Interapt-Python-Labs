def reverse_string( str_tb_reversed ):
    str_as_list = list( str_tb_reversed )
    print(f'{str_as_list = }')
    str_as_list.reverse( )
    print(f'After list reverse: {str_as_list = }')

    return "" .join(str_as_list)

print(reverse_string("Lou Marco"))