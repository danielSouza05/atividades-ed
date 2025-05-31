# 1 teste
A = 10
B = 15
C = 4

if A < B and A < C or C != 0:
    print("Verdadeiro")
else:
    print("Falso")

# 2 teste
A = 10
B = 15
C = 4

if A < B or (A < C or C != 0):
    print("Verdadeiro")
else:
    print("Falso")

# 3 teste
A = 1
B = 9
C = 0

if not (A >= 0 and B == C):
    print("Verdadeiro")
else:
    print("Falso")

# 4 teste
A = 1
B = 9
C = 9

if not(A >= 0) and not (B == C):
    print("Verdadeiro")
else:
    print("Falso")

# 5 teste
A = 1
B = 9
C = 0

if (A >= 0 or B == C) and B > A:
    print("Verdadeiro")
else:
    print("Falso")

# 6 teste
A = 0
B = 1
C = 0

if A == 0 and B != 0 and C == 0:
    print("Verdadeiro")
else:
    print("Falso")

# 7 teste
A = -2
B = 0
C = 2

if not (A <= B) or C > B:
    print("Verdadeiro")
else:
    print("Falso")

# 8 teste
A = -2
B = 0
C = 2

if not (A <= 0 or C > B):
    print("Verdadeiro")
else:
    print("Falso")

# 9 teste
A = 5
B = 0
C = 0

if A == 0 and B != 0 and C == 0:
    print("Verdadeiro")
else:
    print("Falso")

# 10 teste
A = 5
B = 0
C = 0

if A == 0 or B != 0 or C == 0:
    print("Verdadeiro")
else:
    print("Falso")