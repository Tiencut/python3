a,b = map(int, input().split())
if a == 0 and b == 0:
    print("The coordinate point (" + str(a) + ', ' + str(b) + ") lies at the origin.")
if a > 0 and b > 0:
    print("The coordinate point (" + str(a) + ', ' + str(b) + ") lies in the I quandrant.")
if a < 0 and b > 0:
    print("The coordinate point (" + str(a) + ', ' + str(b) + ") lies in the II quandrant.")
if a < 0 and b < 0:
    print("The coordinate point (" + str(a) + ', ' + str(b) + ") lies in the III quandrant.")
if a > 0 and b < 0:
    print("The coordinate point (" + str(a) + ', ' + str(b) + ") lies in the IV quandrant.")