import random

def write():
    f = open("bob.ppm", "a")
    f.write("P3 500 500 255\n")
    for x in range(500):
        for y in range(500):
            """
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            f.write(str(a) + " " + str(b) + " " + str(c) + " ")"""
            if (y % 167 == 0):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            if (x % 167 == 0):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            #draw x's
            if (x == y or x + y == 167):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            if (x + y == 501 and x >= 167 and y >= 167):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            if (x + y == 835 and x >= 334 and y >= 334):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            #draw o's
            if (250 <= x + y <= 417 and 167 <= x <= 334 and y <= 167):
                f.write(str(0) + " " + str(0) + " " + str(0) + " ")
                continue
            f.write(str(255) + " " + str(255) + " " + str(255) + " ")
        f.write("\n")
    f.close()

write()