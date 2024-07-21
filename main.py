# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
my_dict={'Vasya': 1987, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Vasya'])
my_dict['Ilya']= 1900
print(my_dict['Ilya'])
my_dict.update({'Vasya': 2024,'Ilya': 2023})
print(my_dict)
del my_dict['Ilya']
print(my_dict.get('Ilya'))
print(my_dict)
a=my_dict.pop('Vasya')
print(a)
print(my_dict)

my_set={1,'f',3,8,5,5,'f','d',8}
print(my_set)
print(my_set.add(2)),(my_set.add(7))
print(my_set)
print(my_set.discard(2))
print(my_set)