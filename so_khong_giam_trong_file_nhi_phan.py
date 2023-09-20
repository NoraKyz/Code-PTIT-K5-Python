import re, collections, math, fractions, itertools

def check(data):
    data = str(data)

    if len(data) < 2:
        return False
    
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            return False
    return True

def solve(data1, data2):
    d1 = {}
    d2 = {}

    st = set()

    for i in data1:
        if not check(i):
            continue

        d1[i] = d1.get(i, 0) + 1
        st.add(i)
    
    for i in data2:
        if not check(i):
            continue

        d2[i] = d2.get(i, 0) + 1
        st.add(i)

    for i in st:
        print(i, d1.get(i, 0), d2.get(i, 0))

def main():
    file = open("DATA1.in","rb")
    data1 = bytearray(file.read(3))
    
    file = open("DATA2.in","rb")
    data2 = bytearray(file.read(3))

    solve(data1, data2)

main()