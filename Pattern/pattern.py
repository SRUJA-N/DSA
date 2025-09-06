def print1(n): """Decreasing triangle of stars""" for i in range(n, 0, -1): print("*" * i) # Example for n=4: # **** # *** # ** # *

def print2(n): """Numbers decreasing in length""" for i in range(1, n + 1): for j in range(1, n - i + 2): print(j, end="") print() # Example for n=4: # 1234 # 123 # 12 # 1

def print3(n): """Centered pyramid of stars""" for i in range(n): print(" " * (n - i - 1) + "*" * (2 * i + 1)) # Example for n=4: #    * #   *** #  ***** # *******

def print4(n): """Inverted centered pyramid of stars""" for i in range(n): print(" " * i + "*" * (2 * (n - i) - 1)) # Example for n=4: # ******* #  ***** #   *** #    *

def print5(n): """Diamond of stars""" for i in range(n): print(" " * (n - i - 1) + "" * (2 * i + 1)) for i in range(n): print(" " * i + "" * (2 * (n - i) - 1)) # Example for n=3: #   * #  *** # ***** # ***** #  *** #   *

def print6(n): """Triangle up and down""" for i in range(1, n + 1): print("" * i) for i in range(n - 1, 0, -1): print("" * i) # Example for n=3: # * # ** # *** # ** # *

def print7(n): """0-1 triangle pattern""" for i in range(1, n + 1): for j in range(1, i + 1): print("1" if (i + j) % 2 == 0 else "0", end="") print() # Example for n=4: # 1 # 01 # 101 # 0101

def print8(n): """Number palindrome with dashes in center""" for i in range(1, n + 1): print("".join(str(j) for j in range(1, i + 1)), end="") print("-" * ((n - i) * 2), end="") print("".join(str(j) for j in range(i, 0, -1))) # Example for n=4: # 1------1 # 12----21 # 123--321 # 12344321

def print9(n): """Continuous numbers in triangle""" num = 1 for i in range(1, n + 1): for _ in range(i): print(f" {num}", end="") num += 1 print() # Example for n=4: #  1 #  2 3 #  4 5 6 #  7 8 9 10

def print10(n): """Letters decreasing in rows""" for i in range(n, 0, -1): print("".join(chr(65 + j) for j in range(i))) # Example for n=4: # ABCD # ABC # AB # A

def print11(n): """Letters increasing in rows""" for i in range(1, n + 1): print("".join(chr(65 + j) for j in range(i))) # Example for n=4: # A # AB # ABC # ABCD

def print12(n): """Same letter repeated in row""" for i in range(1, n + 1): print(chr(64 + i) * i) # Example for n=4: # A # BB # CCC # DDDD

def print18(n): """Reverse letters triangle""" for i in range(n): print("".join(chr(69 - j) for j in range(i + 1))) # Example for n=4: # E # ED # EDC # EDCB

def print19(n): """Hourglass with stars and dashes""" for i in range(n // 2): stars = n // 2 - i dashes = i * 2 print("" * stars + "-" * dashes + "" * stars) for i in range(n // 2, 0, -1): stars = n // 2 - i dashes = i * 2 print("" * stars + "-" * dashes + "" * stars) # Example for n=6: # -- # ---- # ---- # --

def print20(n): """Hollow square""" for i in range(n): if i == 0 or i == n - 1: print("" * n) else: print("" + " " * (n - 2) + "*") # Example for n=4: # **** # *  * # *  * # ****

