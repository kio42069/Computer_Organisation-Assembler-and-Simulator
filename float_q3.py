import EE

def number_to_float(val):
    if 0.25 <= val and val<=15.75:
        flag = "Normal"

    elif val>=15.75:
        flag = "Overflow"

    elif 0 <= val and val < 0.25:
        flag = "Denormal"

    if flag=="Normal":
        flag_1 = True
        strval = str(val)
        whole, mant = strval.split(".")
        mant=(float("0."+mant))
        dectobin_converted_val = dec_to_bin(val)
        if dectobin_converted_val[0] == "0":
            flag_1 = False
        
        init_whole, init_mant = dectobin_converted_val.split(".")

        if flag_1:
            exp = len(dectobin_converted_val)-1             
            init_mant = ""
            for i in range(len(dectobin_converted_val)):
                if dectobin_converted_val[i] == ".":
                    exp = i-1
                    break
                else:
                    init_mant += dectobin_converted_val[i]

            numofmantbits = 5 - (exp)

        else:
            init_mant=""
            for i in range(len(dectobin_converted_val)):
                if dectobin_converted_val[i] == "1":
                    exp = -(i-1)
                    break

            numofmantbits = 5
            new_mant = dectobin_converted_val[i+1:]
            print(new_mant, "new")
            mant = EE.binary_to_decimal(new_mant)
            print(mant, "conv")
            mant = (float("0." + str(mant))) 
            print(mant, "huh")

        mantarr = [0,0,0,0,0]

        for i in range(1, 6):
            if mant-(2**(-i)) >= 0:
                mant -= 2**(-i)
                mantarr[i-1] = 1

        final_mant = init_mant[1:]
        for i in range(numofmantbits):
            final_mant += str(mantarr[i])


        exp = exp + 3
        exponent = str(EE.decimal_to_binary(exp))
        exponent = "0" * (3 - len(exponent)) + exponent
        out = exponent + final_mant

    if flag == "Overflow":
        out = "11100000"

    elif flag == "Denormal":
        init_mant = "000"
        val = val * 4
        flt = val
        cnt=0
        out=""
        while flt!=0 or cnt==5:
            flt = flt * 2
            out += str(int(flt))
            flt = flt%1
            cnt+=1

        out = init_mant + out 

    return out
        

def dec_to_bin(decval):
    out = ""
    integral = int(decval)
    flt = decval%1
    bininteg = bin(integral)[2:]
    cnt=0

    while flt!=0 or cnt==5:
        flt = flt * 2
        out += str(int(flt))
        flt = flt%1
        cnt+=1

    if len(out)>5:
        out = out[:5]
    else:
        out = out + "0"*(5-cnt)

    out = str(bininteg) + "." + out
    return out

print(number_to_float(0.3))