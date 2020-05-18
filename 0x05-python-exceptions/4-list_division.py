#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0 for i in range(0, list_length)]
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            pass
    return new_list
