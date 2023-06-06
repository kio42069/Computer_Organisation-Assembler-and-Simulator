'''float converter function--
float 8 bits--
last 8 bits of register, register is string--
3 new operations
fadd fsub- check if value >max value, then error must be thrown accordingly for now
only do for normal numbers currently
bias 3 in this case--
in mantissa, 5 bits, 1st bit 2^-1--
find max min in range for overflow--

conversions and three functions'''
import EE

"binary string to floating binary"


def binary_to_float(strvalue):
    flag = False

    for i in range(len(strvalue)):  # remove trailing 0s
        if strvalue[i] != "1":
            if strvalue[i] != ".":
                strvalue = strvalue[i:]
            else:
                break
        else:
            break
    powerbit = len(strvalue)-1

    for i in range(len(strvalue)):
        if strvalue[i] == ".":
            powerbit = i-1
            flag = True
            break

    if flag:
        strvalue = strvalue.replace(".", "")

    val = bin_to_dec(strvalue)

    zeroeth_bit = strvalue[0]
    if zeroeth_bit == "1":
        mantissa = strvalue[1:6]
        mantissa = mantissa + "0" * (5 - len(mantissa))
        exponentindec = powerbit + 3
        exponent = str(EE.decimal_to_binary(exponentindec))
        exponent = "0" * (3 - len(exponent)) + exponent

    # Main difficulty here:
    else:
        mantissa = strvalue[1:6]
        mantissa = mantissa + "0" * (5 - len(mantissa))
        exponent = "0"*3

    return (exponent + mantissa)


"floating binary to binary string"


def float_to_binary(strfloat):
    exponent = strfloat[:3]
    mantissa = strfloat[3:]

    exponentindec = EE.binary_to_decimal(int(exponent)) - 3
    mantissa = "1" + mantissa[:exponentindec] + "." + mantissa[exponentindec:]

    return mantissa


"floating binary to decimal value"


def float_to_dec(strfloat):
    exponent = strfloat[:3]
    mantissa = strfloat[3:]

    if exponent != "000":
        mant_sum = 1
        for i in range(5):
            mant_sum += (int(mantissa[i])) / (2**(i+1))

        exp_val = 2**(EE.binary_to_decimal(int(exponent)) - 3)
        dec_val = exp_val * mant_sum

    else:
        dec_val = denormal_float_to_dec(strfloat)

    return dec_val


def denormal_float_to_dec(strfloat):
    exp = 2**(-2)
    mant = strfloat[3:]
    mant_sum = 0
    for i in range(5):
        mant_sum += (int(mant[i])) / (2**(i+1))

    dec_val = exp * mant_sum

    return dec_val


"decimal value to binary string"


def dec_to_bin(decval):
    out = ""
    integral = int(decval)
    flt = decval % 1
    bininteg = bin(integral)[2:]
    cnt = 0

    while flt != 0 or cnt == 10:
        flt = flt * 2
        out += str(int(flt))
        flt = flt % 1
        cnt += 1

    out = str(bininteg) + "." + out
    return out


"binary string to decimal value"


def bin_to_dec(strbin):
    if "." in strbin:
        integ, flt = strbin.split(".")
    else:
        integ = strbin
        flt = ""
    integ = integ[::-1]
    decs = 0
    flts = 0
    for i in range(len(integ)):
        decs += (int(integ[i]))*(2**(i))

    for i in range(len(flt)):
        flts += (int(flt[i]))/(2**(i+1))

    sum = decs + flts
    return sum


def max_float():
    max = float_to_dec("11011111")
    return max


def min_float():
    min = float_to_dec("00000001")
    return min


def f_addition(reg1, reg2, reg3, overflow_flag):
    reg1 = reg2 + reg3
    if reg1 > max_float():
        reg1 = 0
        overflow_flag = 1
    reg1 = binary_to_float(dec_to_bin(reg1))
    return reg1


# def f_subtraction(reg1, reg2, reg3)
print(dec_to_bin(0.3))
print(bin_to_dec("0.01001"))
print(denormal_float_to_dec("00001001"))
print(float_to_dec(binary_to_float(dec_to_bin(0.3)[0:10])))
