#===============Soal Nomor 1===============
import random, math
# Graded
def isPointInCircle(x, y, r, center=(0, 0)):
    return True if (((x - center[0]) ** 2) + ((y - center[1]) ** 2)) < (r ** 2) or (((x - center[0]) ** 2) + ((y - center[1]) ** 2)) == (r ** 2) else False

#===============Soal Nomor 2===============
def generateRandomSquarePoints(n, length, center=(0, 0)):
    minx = center[0] - (length / 2)
    miny = center[1] - (length / 2)
    maxx = center[0] + (length/2)
    maxy = center[1] + (length/2)
    return [[random.uniform(minx, maxx), random.uniform(miny, maxy)] for x in range(n)]

#===============Soal Nomor 3===============
def MCCircleArea(r, n=100, center=(0, 0)):
    nTitikDalam = 0
    sisiPersegi = 2*r
    points = generateRandomSquarePoints(n, sisiPersegi, center)
    for x in range(n):
        nTitikDalam += 1 if isPointInCircle(points[x][0], points[x][1], r, center) == True else False
    return (nTitikDalam / n) * (sisiPersegi ** 2)

#===============Soal Nomor 4===============
def LLNPiMC(nsim,nsample):
    sigmaX = 0
    for simulasi in range(nsim):
      sigmaX += MCCircleArea(1, nsample)
    return sigmaX / nsim

#===============Soal Nomor 5===============
def relativeError(act, est):
    return (abs((est - act)/act) * 100)