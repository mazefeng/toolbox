import sys
import time

D = 3600 * 24
BJ_OFFSET = 3600 * 8

M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N = [0] * 12

N[0] = M[0] - 1
for t in range(len(N) - 1):
    N[t + 1] = N[t] + M[t + 1]
N = [0, -1] + N

K = [(y - 1970) * D * 365 for y in range(3000)]

L = lambda y, m : (1 if m >= 3 and ((y % 100 == 0 and y % 400 == 0) or (y % 100 != 0 and y % 4 ==0)) else 0)

def parser(s):

    year, month, date, hour, minute, second = map(int, [s[0 : 4], s[5 : 7], s[8 : 10], s[11 : 13], s[14 : 16], s[17 : 19]])

    t = K[year] \
        + (N[month] + date + (year - 1969) / 4 + L(year, month)) * D \
        + hour * 3600 + minute * 60 + second - BJ_OFFSET

    return t

if __name__ == '__main__':

    # s = '2015-03-13 15:46:24'
    # ss = '1426232784'

    T = range(0, 1420070400, 1654)
    # T = T[0 : 10]
    S = list()

    for t in T:
        S.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))

    print >> sys.stderr, 'start'
    
    start = time.time()
    for s in S:
        t1 = time.strptime(s, '%Y-%m-%d %H:%M:%S')
        t1 = int(time.mktime(t1)) 
        # t2 = parser(s)
        # print t1, t2
    terminate = time.time()

    print >> sys.stdout, terminate - start
