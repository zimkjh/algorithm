import numpy


def solution(arr1, arr2):
    arr1 = numpy.array(arr1)
    arr2 = numpy.array(arr2)
    answer = numpy.add(arr1, arr2)
    return answer.tolist()

