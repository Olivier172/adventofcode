#objective : In how many assignment pairs do the ranges overlap?

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
        if( (startSection2<=startSection1<=endSection2) or (startSection2<=endSection1<=endSection2) or (startSection1<=startSection2<=endSection1) or (startSection1<=endSection2<=endSection1)):
            count+=1
    print(f"There are {count} assignment pairs that have overlap")

main()

# output
# There are 830 assignment pairs that have overlap