import time
#objective : In how many assignment pairs does one range fully contain the other?

def main():
    print("day4")
    file = open("input.txt","r")
    lines = file.readlines()
    count=0
    for line in lines:
        elf1 ,elf2 = line.split(",")
        startSection1, endSection1 = elf1.split('-')
        startSection2, endSection2 = elf2.split('-')
        startSection1=int(startSection1)
        startSection2=int(startSection2)
        endSection1=int(endSection1)
        endSection2=int(endSection2)
        if( ((startSection1>=startSection2) and (endSection1<=endSection2)) or ((startSection2>=startSection1) and (endSection2<=endSection1))):
            count+=1
    print(f"There are {count} assignment pairs where one range fully contains the other")
start = time.time()
main()
print((time.time() - start)*1000)
# output:
# There are 477 assignment pairs where one range fully contains the other