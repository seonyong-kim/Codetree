arrA = input().split()
mathScoreA, englishScoreA = int(arrA[0]), int(arrA[1])

arrB = input().split()
mathScoreB, englishScoreB = int(arrB[0]), int(arrB[1])

print(int(mathScoreA >  mathScoreB and englishScoreA > englishScoreB))