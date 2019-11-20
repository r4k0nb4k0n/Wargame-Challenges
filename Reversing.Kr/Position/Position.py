__author__ = "r4k0nb4k0n"
__license__ = "MIT"

import argparse
import re # Use regular expression to verify name and serial.
import exrex # Generate strings that match the regex.
import time # Get working time.

reg = {
    # Name should be 4 alphabet lowercase characters and different each other.
    'name': re.compile('^(?!.*(.).*\1)[a-z]{4}$'),
    # Serial should be 11 characters.
    'serial': re.compile('^[0-9]{5}-[0-9]{5}$')
}

def main(args):
    if args.verify:
        if args.name != None and args.serial != None:
            print(verify(args.name, args.serial))
        else:
            print("Name or serial is not given.")
    elif args.generate:
        if args.name != None:
            print(generate_serial_from(args.name))
        elif args.serial != None:
            for name in generate_name_from(args.serial):
                print(name)

def check_name(name):
    if reg['name'].match(name) != None:
        return True
    return False

def check_serial(serial):
    if reg['serial'].match(serial) != None:
        return True
    return False

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

def generate_serial_from(name):
    if not check_name(name):
        raise Exception("Name is not valid.")
    val = [[1] * 5 for i in range(len(name))]
    for i in range(len(name)):
        for j in range(5):
            val[i][j] = ((ord(name[i]) >> j) & 1) + (5 if i % 2 == 0 else 1)
    gen =  str(val[0][0] + val[1][2])
    gen += str(val[0][3] + val[1][3])
    gen += str(val[0][1] + val[1][4])
    gen += str(val[0][2] + val[1][0])
    gen += str(val[0][4] + val[1][1])
    gen += "-"
    gen += str(val[2][0] + val[3][2])
    gen += str(val[2][3] + val[3][3])
    gen += str(val[2][1] + val[3][4])
    gen += str(val[2][2] + val[3][0])
    gen += str(val[2][4] + val[3][1])
    return gen

@logging_time
def generate_name_from(serial):
    if not check_serial(serial):
        raise Exception("Serial is not valid.")
    ret = []
    for name in list(exrex.generate('(?!.*(.).*\1)[a-z]{4}')):
        if serial == generate_serial_from(name):
            ret.append(name)
    return ret

@logging_time
def verify(name, serial):
    if not check_name(name) or not check_serial(serial):
        return False
    if serial != generate_serial_from(name):
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", action="store", dest="name")
    parser.add_argument("-s", "--serial", action="store", dest="serial")

    parser.add_argument("-v", "--verify", action="store_true", dest="verify")
    parser.add_argument("-g", "--generate-with-given", action="store_true", dest="generate")

    args = parser.parse_args()
    main(args)