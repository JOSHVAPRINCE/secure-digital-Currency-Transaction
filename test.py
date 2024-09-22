import os
import random


class split_and_store():
    def split_file(self,txt,id):
        letters_and_digits = txt


        result_str = ''.join((random.choice(letters_and_digits) for i in range(5)))
        lst = []
        for i in result_str:
            lst.append(i)
        result = []
        for x in lst:
            temp = txt.split(x)
            tmp1 = len(temp)
            if tmp1 < 2:
                result.append(temp[tmp1 - 1])
            else:
                result.append(str(temp) + str(tmp1))
        dir1 = 'blockchain_server/1'
        dir2 = 'blockchain_server/2'
        dir3 = 'blockchain_server/3'
        dir4 = 'blockchain_server/4'
        dir5 = 'blockchain_server/5'

        if not os.path.exists(dir1):
            os.makedirs(dir1)
        if not os.path.exists(dir2):
            os.makedirs(dir2)
        if not os.path.exists(dir3):
            os.makedirs(dir3)
        if not os.path.exists(dir4):
            os.makedirs(dir4)
        if not os.path.exists(dir5):
            os.makedirs(dir5)
        file1 = os.path.join(dir1, (str(id) + ".txt"))
        file2 = os.path.join(dir2, (str(id) + ".txt"))
        file3 = os.path.join(dir3, (str(id) + ".txt"))
        file4 = os.path.join(dir4, (str(id) + ".txt"))
        file5 = os.path.join(dir5, (str(id) + ".txt"))

        f = open(file1, 'w')
        f.write(txt)

        f = open(file2, 'w')
        f.write(txt)
        f = open(file3, 'w')
        f.write(txt)

        f = open(file4, 'w')
        f.write(txt)

        f = open(file5, 'w')
        f.write(txt)

    def encrypt(self,message, key):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        LETTERS = LETTERS.lower()
        encrypted = ''
        # print(message)
        for chars in message:
            # print(chars)
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num += key
                encrypted += LETTERS[num]
        return encrypted
    def match_file(self,file):
        id=file
        dir1 = 'blockchain_server/1'
        dir2 = 'blockchain_server/2'
        dir3 = 'blockchain_server/3'
        dir4 = 'blockchain_server/4'
        dir5 = 'blockchain_server/5'
        file1 = os.path.join(dir1, (str(id) + ".txt"))
        file2 = os.path.join(dir2, (str(id) + ".txt"))
        file3 = os.path.join(dir3, (str(id) + ".txt"))
        file4 = os.path.join(dir4, (str(id) + ".txt"))
        file5 = os.path.join(dir5, (str(id) + ".txt"))

        f1= open(file1, "r")
        d1=f1.read()

        f2 = open(file2, "r")
        d2 = f2.read()

        f3 = open(file3, "r")
        d3 = f3.read()

        f4= open(file4, "r")
        d4 = f4.read()

        f5 = open(file5, "r")
        d5 = f5.read()
        if d1==d2==d3==d4==d5:
            return "ok"
        return "refund"











