#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res_a = 0
    res_b = 0
    try:
        res_a = tuple_a[0] + tuple_b[0]
    except Exception:
        try:
            res_a = 0 + tuple_b[0]
        except Exception:
            try:
                res_a = tuple_a[0] + 0
            except Exception:
                res_a = 0 + 0

    try:
        res_b = tuple_a[1] + tuple_b[1]
    except Exception:
        try:
            res_b = 0 + tuple_b[1]
        except Exception:
            try:
                res_b = tuple_a[1] + 0
            except Exception:
                res_b = 0 + 0

    return(res_a, res_b)
