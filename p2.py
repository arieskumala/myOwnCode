# nama file p2.py
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

# netacad email cth: 'abcd@gmail.com'
email = 'arieskumala@gmail.com'

# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

import random, math
# Graded
def isPointInCircle(x, y, r, center=(0, 0)):
    # MULAI KODEMU DI SINI
    persamaan = (((x - center[0]) ** 2) + ((y - center[1]) ** 2))
    rKuadrat = r ** 2

    if persamaan < rKuadrat or persamaan == rKuadrat:
        return True
    else:
        return False

# Graded
def generateRandomSquarePoints(n, length, center=(0, 0)):
    # MULAI KODEMU DI SINI
    minx = center[0] - length / 2
    miny = center[1] - length / 2

    # Gunakan list comprehension dengan variable minx, miny, length, dan n
    points = [[random.uniform(minx, -(minx)), random.uniform(miny, -(miny))] for x in range(n)]

    return points

# Graded
def MCCircleArea(r, n=100, center=(0, 0)):
    # MULAI KODEMU DI SINI
    pass
    numberOfHits = 0

    points = generateRandomSquarePoints(n, length=2, center=(0, 0))

    for x in range(n):
        a = isPointInCircle(points[x][0], points[x][1], 1, center=(0, 0))
        if a == True:
            numberOfHits += 1
    pi = (numberOfHits / n) * (2 * (r * 2))
    return pi

#Graded
def LLNPiMC(nsim,nsample):
    # MULAI KODEMU DI SINI
    pass
    nilaiPi = []
    sigmaX = 0
    for simulasi in range(nsim):
        nilaiPi.append(MCCircleArea(1, nsample))

    for i in nilaiPi:
        sigmaX += i
    estpi = sigmaX / nsim
    return estpi

# Graded
def relativeError(act, est):
    # MULAI KODEMU DI SINI
    pass
    errRelative = (abs((est - act)/act) * 100)
    return errRelative