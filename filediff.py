#!/usr/bin/env python3

import sys, json

def getdkpgfile(filename):

    packs = []
    file = open(filename, "r")
    fdata = [(line) for line in file]
    fdata = [f.strip().split("\n") for f in fdata]
    file.close()


    for itr, each in enumerate(fdata):
        d = ""
        pak = each[0].split()[1:3]
        descript = each[0].split()[4:]
        for each in descript:
            if d == None:
                d = each
            else:
                d = (d + " " + each)
        if len(pak) != 2:
            continue
        else:
            fdata[itr] = [pak[0], pak[1], d]
            packs.append(pak[0])

    return fdata, packs


def getfile(filename):

    packs = []
    file = open(filename, "r")
    fdata = [(line) for line in file]
    fdata = [f.strip().split("\n") for f in fdata]
    file.close()

    return fdata


def getpack(element):
        return element[0]

def formattedprint(counter, data):
    key, ver, desc = data
    print('{0:<5} {1:<50} {2:<50} {3:<100}'.format(counter, key, ver, desc))


def findpack(pack, datalist):
    for itr, each in enumerate(datalist):
        if each[0][:2] == "++" or each[0][:8] == "Desired=":
            continue
        if getpack(each) == pack:
            return itr


def diffdpkg():
    f1data, f1packs = getdkpgfile(sys.argv[1])
    f2data, f2packs = getdkpgfile(sys.argv[2])

    count1 = 0
    print("New packs:\n"+"="*160)
    for itr, elem in enumerate(f2packs):
        if elem[:6] == "Status" or elem[:4] == 'Err?':
            continue
        if elem in f1packs:
            continue
        else:
            count1 = count1 + 1
            formattedprint(count1, f2data[findpack(elem, f2data)])

    print("\nInstalled packs:", count1)


    count2 = 0
    print("\n\nUpdated packs:\n"+"="*160)
    for itr, elem in enumerate(f2data):
        if elem[0][:2] == "++" or elem[0][:8] == "Desired=":
            continue
        pack = getpack(elem)
        if pack in f1packs and elem not in f1data:
            count2 = count2 + 1
            formattedprint(count2, elem)
    print("\nUpdated packs:", count2)

    print("\nTotal packages installed/updated:", count1+count2)



def diffpip():
    f1data = getfile(sys.argv[1])[0]
    f2data = getfile(sys.argv[2])[0]

    count = 0
    for elem in f2data:
        if elem in f1data:
            continue
        else:
            count = count + 1
            print(elem[0])
    print("\nmismatched lines:", count)


def main():
    if len(sys.argv) != 3:
        print("Please provide 2 files to compare")
        print(sys.argv)
        exit(1)
    #print("Comparing files:", sys.argv[1], sys.argv[2], "\n")

    if sys.argv[1][:4] == "dpkg":
        diffdpkg()
    elif sys.argv[1][:3] == "pip":
        diffpip()



if __name__ == "__main__":
    main()