#!/usr/bin/python3
""" Find the peak """


def check_peak(list_of_integers, length, index):
    """ Chech if this index has a peak value """

    if index == 0 and list_of_integers[index] < list_of_integers[index + 1]:
        return True

    if index == length - 1 and \
       list_of_integers[index] > list_of_integers[index - 1]:
        return True

    if list_of_integers[index] > list_of_integers[index - 1] and \
       list_of_integers[index] > list_of_integers[index + 1]:
        return True

    if index - 1 >= 0 and index + 1 < length:
        if list_of_integers[index] == list_of_integers[index - 1] and \
           list_of_integers[index] == list_of_integers[index + 1]:
            return "right temp"

        if list_of_integers[index] == list_of_integers[index - 1] and \
           list_of_integers[index] > list_of_integers[index + 1]:
            return "right temp"

        if list_of_integers[index] > list_of_integers[index - 1] and \
           list_of_integers[index] == list_of_integers[index + 1]:
            return "left temp"

    if index + 1 < length and \
       list_of_integers[index] < list_of_integers[index + 1]:
        return "right"

    return "left"


def find_peak_half(list_of_integers, length, left, right, temp):
    """ Helper method """
    if (left > right):
        if temp != "SHOUKRY":
            return list_of_integers[temp]
        return None

    mid = int((left + right) / 2)
    valid = check_peak(list_of_integers, length, mid)

    if (valid is True):
        return list_of_integers[mid]

    if (valid == "right"):
        return find_peak_half(list_of_integers, length, mid + 1, right, temp)

    if (valid == "right temp"):
        temp = mid
        return find_peak_half(list_of_integers, length, mid + 1, right, temp)

    if (valid == "left temp"):
        temp = mid
        return find_peak_half(list_of_integers, length, left, mid - 1, temp)

    return find_peak_half(list_of_integers, length, left, mid - 1, temp)


def find_peak(list_of_integers):
    """ Method used to find the peak """

    if (list_of_integers is None):
        return (None)

    length = len(list_of_integers)

    return find_peak_half(list_of_integers, length, 0, length - 1, "SHOUKRY")
