from sympy import Matrix

class hardCoding():

    def __init__(self):
        self.glbCodVect = [
                           [9, 40, 46],
                           #[33, 99, 1],
                           [111, 94, 73],
                           #[9, 100, 50],
                           [17, 10, 59]
                           ]
        self.payloadVect = [[92,	80,	26,	92,	42,	89],
                            #[72,	43,	107, 10, 108, 84],
                            [85,	60,	120, 110, 90, 8],
                            #[83,	115, 83, 121, 81, 19],
                            [106, 87, 8,	88,	72,	0]]

        self.findIndepVct()

    def findIndepVct(self):
        codingMatrix = Matrix(self.glbCodVect)

        payloadMatrix = Matrix(self.payloadVect)
        inverse = codingMatrix.inv_mod(127)
        prod = inverse*payloadMatrix
        for i in prod:
            print chr(i%127)



def main():
    print 'start'
    inst = hardCoding()

if __name__ == '__main__':
    main()