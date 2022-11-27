import numpy as np
import pandas as pd
def main():
    a = pd.Series(data=[1, 2, 3, 4])
    b = pd.Series(data=[4.9, 8.2, 5.6],
                  index=['x', 'y', 'z'])
    c = pd.Series(dtype=float)
    print(a.ndim, b.ndim)
    print(a.size, b.size)
    print(a.nbytes, b.nbytes)
    print(a.empty, b.empty, c.empty)
    print(a.hasnans, b.hasnans, c.hasnans)
    print(len(a), len(b))
    print(a.count(), b.count())
    d = a+b

if __name__ == '__main__':
    main()