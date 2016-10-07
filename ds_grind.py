#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111

from operator import eq, ge
from os import getenv
from dictator import Dictator


def case_count(result, _try, op):
    return float(sum(int(v) for k, v in result.items() if op(int(k), _try)))


def main():
    _try = 1
    result = Dictator(db=int(getenv('redis_db', '2')))
    while True:
        probability = case_count(result, _try, eq) / (case_count(result, _try, ge) or 0.00000001)
        print "Try {0}. Probability {1}. Respawned? y/N".format(_try, probability),
        answer = raw_input()
        if answer.lower() != 'y':
            _try += 1
            continue
        result[_try] = int(result.get(_try, 0)) + 1
        _try = 1


if __name__ == '__main__':
    main()
