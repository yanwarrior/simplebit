def numb2Bit(numerik):
    """mengubah angka ke bit"""
    return bin(numerik).replace("b","")

def listNum2Bit(listNumerik):
    """mengubah list numerik ke bit"""
    try:
        return [numb2Bit(bit) for bit in listNumerik]
    except:
        return None

def string2Bit(string):
    """mengubah string menjadi serangkaian bit"""
    try:
        return [numb2Bit(ord((i))) for i in string]
    except:
        return None


def addBitStr(bitString, add):
    """menambakhan bit bit string"""
    try:
        return bitString.rjust(add, '0')
    except:
        return None


def addBitList(listBitString, add = 8):
    """menambahkan bit bit list bentuk string"""
    try:
        return [i.rjust(add, '0') for i in listBitString]
    except:
        return None

def file2Bit(filename):
    """konversi file ke bit"""
    try:
        with open(filename, "rb") as f:
            data = f.read()
        bit = [ord(i) for i in data]
        bit = [numb2Bit(i) for i in bit]
        bit = addBitList(bit)
        return bit
    except:
        return None

def setBit2String(listBit):
    """gabung bit"""
    return "".join(listBit)



