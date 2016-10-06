#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111

from os import getenv
from dictator import Dictator


def case_count(result, _try):
    return float(sum(int(result.get(x, 0)) for x in result.keys() if int(x) == _try))


def case_count_greater(result, _try):
    return float(sum(int(result.get(x, 0)) for x in result.keys() if int(x) >= _try))


def main():
    _try = 1
    result = Dictator(db=int(getenv('redis_db', '2')))
    while True:
        probability = case_count(result, _try) / (case_count_greater(result, _try) or 0.00000001)
        print "Try {0}. Probability {1}. Respawned? y/N".format(_try, probability),
        answer = raw_input()
        if answer.lower() != 'y':
            _try += 1
            continue
        result[_try] = int(result.get(_try, 0)) + 1
        _try = 1


if __name__ == '__main__':
    main()
