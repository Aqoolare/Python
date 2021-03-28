import cmath


# def solve(a, b, c):
#     d_sqrt = (b**2 - 4*a*c) ** (1/2)
#     a2 = 2 * a
#     x1 = (-b - d_sqrt) / a2
#     x2 = (-b + d_sqrt) / a2
#     return (x1, x2) 


# def solve(a, b, c):
#     d_sqrt = (b**2 - 4*a*c) ** (1/2)
#     if a != 0:    
#         a2 = 2 * a
#         x1 = (-b - d_sqrt) / a2
#         x2 = (-b + d_sqrt) / a2
#         return (x1, x2)
#     else:
#         return (-c / b)


# def solve(a, b, c):
#     d_sqrt = (b**2 - 4*a*c) ** (1/2)
#     if a != 0:    
#         a2 = 2 * a
#         x1 = (-b - d_sqrt) / a2
#         x2 = (-b + d_sqrt) / a2
#         return (round(x1, 2), round(x2, 2))
#     else:
#         return (round(-c / b, 2))


# def solve(a, b, c):
#     d_sqrt = cmath.sqrt(b**2 - 4*a*c)
#     if is_complex(a) and is_complex(b) and is_complex(c):
#         a = complex(a)
#         b = complex(b)
#         c = complex(c)
#         if a != 0:    
#             a2 = 2 * a
#             x1 = (-b - d_sqrt) / a2
#             x2 = (-b + d_sqrt) / a2
#             return (complex(round(x1.real, 2), round(x1.imag, 2)),
#             complex(round(x2.real, 2), round(x2.imag, 2)))
#         else:
#             res = -c / b
#             return (complex(round(res.real, 2), round(res.imag, 2)))


# def solve(a, b, c):
#     d_sqrt = cmath.sqrt(b**2 - 4*a*c)
#     if is_complex(a) and is_complex(b) and is_complex(c):
#         a = complex(a)
#         b = complex(b)
#         c = complex(c)
#         if a != 0:    
#             a2 = 2 * a
#             x1 = (-b - d_sqrt) / a2
#             x2 = (-b + d_sqrt) / a2
#             return (complex(round(x1.real, 2), round(x1.imag, 2)),
#             complex(round(x2.real, 2), round(x2.imag, 2)))
#         elif b != 0:
#             res = -c / b
#             return (complex(round(res.real, 2), round(res.imag, 2)))
#         elif c != 0:
#             return None
#         else:
#             return 'inf'


def solve(a, b, c):
    if is_complex(a) and is_complex(b) and is_complex(c):
        d_sqrt = cmath.sqrt(b**2 - 4*a*c)
        a = complex(a)
        b = complex(b)
        c = complex(c)
        if a != 0:    
            a2 = 2 * a
            x1 = (-b - d_sqrt) / a2
            x2 = (-b + d_sqrt) / a2
            return (complex(round(x1.real, 2), round(x1.imag, 2)),
            complex(round(x2.real, 2), round(x2.imag, 2)))
        elif b != 0:
            res = -c / b
            return (complex(round(res.real, 2), round(res.imag, 2)))
        elif c != 0:
            return None
        else:
            return 'inf'
    else:
        return 'wrong args'


def is_complex(n):
    try:
        complex(n)
        return True
    except ValueError:
        return False