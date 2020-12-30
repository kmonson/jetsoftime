import struct as st
import random as rand
lowlvlchests = list(range(0x35F40C,0x35F41C,4)) + list(range(0x35F470,0x35F484,4)) + list(range(0x35F4A4,0x35F4B0,4)) \
+ list(range(0x35F7CC,0x35F7DC,4)) + [0x35F42C,0x35F440,0x35F4FC,0x35F500,0x35F7B0]
lmidlvlchests = [0x35F464,0x35F4C4,0x35F4A0] + list(range(0x35F430,0x35F440,4))  + list(range(0x35F488,0x35F49C,4)) \
+ list(range(0x35F4B0,0x35F4C8,4)) + list(range(0x35F4D0,0x35F4FC,4)) + list(range(0x35F584,0x35F5A4,4)) 
midlvlchests = [0x35F428,0x35F468,0x35F46C,0x35F49C,0x35F4C8,0x35F4CC,0x35F6B8,0x35F6BC,0x35F6DC,0x35F744,0x35F7DC] +\
list(range(0x35F444,0x35F464,4)) + list(range(0x35F504,0x35F530,4)) + list(range(0x35F56C,0x35F57C,4)) + \
list(range(0x35F580,0x35F584,4)) + list(range(0x35F678,0x35F6A0,4)) + list(range(0x35F6B8,0x35F6D4,4)) +  \
list(range(0x35F554,0x35F56C,4)) 
mhighlvlchests = [0x35F484,0x35F5E0,0x35F650,0x35F654,0x35F6D8,0x35F7A0] + list(range(0x35F430,0x35F554,4)) +\
list(range(0x35F5B8,0x35F5CC,4)) + list(range(0x35F5E8,0x35F630,4)) + list(range(0x35F630,0x35F678,4)) + \
list(range(0x35F6E4,0x35F6F4,4)) + list(range(0x35F77C,0x35F798,4)) + list(range(0x35F7A4,0x35F7B0,4)) + \
list(range(0x35F7B4,0x35F7CC,4)) + list(range(0x35F41C,0x35F428,4)) + list(range(0x35F5A4,0x35F5B8,4))
hawelvlchests = [0x35F798,0x35F79C] + list(range(0x35F5CC,0x35F5E0,4)) + list(range(0x35F6A0,0x35F6B8,4)) + \
list(range(0x35F6F4,0x35F73C,4)) + list(range(0x35F740,0x35F744,4)) + list(range(0x35F748,0x35F77C,4))
allpointers = lowlvlchests + lmidlvlchests + midlvlchests + mhighlvlchests + hawelvlchests
llvlitems = [0x95,0x98,0x99,0x97,0x96,0xA4,0x02,0x03,0x12,0x13,0x20,0x21,0x2F,0x30,0x3C,0x7E,0x7F,0x80,0x5C,0x5D,0x5E,
0x5F,0x60,0x61]
llvlconsumables = [0xBD,0xBE,0xC6,0xC7,0xC8,0xC9]
plvlitems = [0xAB,0xA6,0x9C,0xB4,0xAC,0x04,0x05,0x0F,0xB9,0x14,0x22,0x23,0x31,0x81,0x82,0x62,0x63,0x64,0x65]
plvlconsumables = [0xBE,0xC0]
mlvlitems = [0xA8,0xA9,0xA0,0xA7,0x9D,0x9E,0x9F,0x06,0x07,0x08,0x15,0x16,0x24,0x25,0x32,0x33,0x34,0x3E,0x3F,0x4C,0x83,
0x84,0x8B,0x66,0x67,0x75,0x76,0x77,0x78,0x79]
mlvlconsumables =[0xBF,0xC1,0xCA,0xCB,0xCC]
glvlitems = [0xAD,0xB5,0xB6,0xB7,0xA1,0xA2,0xAA,0x09,0x0A,0x10,0x17,0x18,0x26,0x29,0x35,0x36,0x40,0x43,0x4D,0x85,
0x88,0x92,0x93,0x68,0x69,0x71,0x72,0x73,0x74]
glvlconsumables = [0xBF,0xC2,0xC4]
hlvlitems = [0x9A,0x9B,0xA3,0xBA,0x0B,0x0C,0x0D,0x19,0x1A,0x27,0x37,0x38,0x41,0x4E,0x89,0x8A,0x8C,0x8D,0x8E,0x6A,0x6E,0x70]
hlvlconsumables = [0xC3,0xC4,0xCD,0xCE,0xCF]
alvlitems = [0xBB,0x0E,0x53,0x54,0x55,0x28,0x39,0x91,0x86,0x8F,0x6C,0x7A,0x6D,0x6B]
alvlconsumables = [0xC3,0xC5]

def choose_item(pointer,difficulty):
    rand_num = rand.randrange(0,11,1)
    if difficulty == "easy":
        if pointer in lowlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(plvlconsumables+mlvlconsumables)
            else: 
                writeitem = rand.choice(plvlitems+mlvlitems)
        elif pointer in lmidlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(mlvlconsumables+glvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    writeitem = rand.choice(glvlitems)
                else:
                    writeitem = rand.choice(mlvlitems)
        elif pointer in midlvlchests or mhighlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(glvlconsumables + hlvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                   if rand_num > 94:
                       writeitem = rand.choice(alvlitems)
                   else:
                       writeitem = rand.choice(hlvlitems)
                else:
                    writeitem = rand.choice(glvlitems)
        elif pointer in hawelvlchests:
            if rand_num > 6:
                writeitem = rand.choice(glvlconsumables + hlvlconsumables + alvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    writeitem = rand.choice(alvlitems)
                else:
                    writeitem = rand.choice(glvlitems + hlvlitems)
    elif difficulty == "hard":
        if pointer in lowlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(llvlconsumables)
            else: 
                writeitem = rand.choice(llvlitems)
        elif pointer in lmidlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(llvlconsumables+plvlconsumables)
            else:
                writeitem = rand.choice(plvlitems)
        elif pointer in midlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(plvlconsumables + mlvlconsumables)
            else:
                writeitem = rand.choice(mlvlitems)
        elif pointer in mhighlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(mlvlconsumables + glvlconsumables)
            else:
                writeitem = rand.choice(mlvlitems+glvlitems)
        elif pointer in hawelvlchests:
            if rand_num > 6:
                writeitem = rand.choice(mlvlconsumables + glvlconsumables + hlvlconsumables + alvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    writeitem = rand.choice(alvlitems)
                else:
                    writeitem = rand.choice(mlvlitems + glvlitems + hlvlitems)
    else:
        if pointer in lowlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(llvlconsumables)
            else: 
                writeitem = rand.choice(llvlitems)
        elif pointer in lmidlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(llvlconsumables+plvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    writeitem = rand.choice(mlvlitems)
                else:
                    writeitem = rand.choice(plvlitems)
        elif pointer in midlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(plvlconsumables + mlvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    if rand_num > 94:
                        writeitem = rand.choice(hlvlitems)
                    else:
                        writeitem = rand.choice(glvlitems)
                else:
                    writeitem = rand.choice(mlvlitems)
        elif pointer in mhighlvlchests:
            if rand_num > 5:
                writeitem = rand.choice(mlvlconsumables + glvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    if rand_num > 94:
                        writeitem = rand.choice(alvlitems)
                    else:
                        writeitem = rand.choice(hlvlitems)
                else:
                    writeitem = rand.choice(glvlitems)
        elif pointer in hawelvlchests:
            if rand_num > 6:
                writeitem = rand.choice(glvlconsumables + hlvlconsumables + alvlconsumables)
            else:
                rand_num = rand.randrange(0,100,1)
                if rand_num > 74:
                    writeitem = rand.choice(alvlitems)
                else:
                    writeitem = rand.choice(glvlitems + hlvlitems)
    return writeitem
def randomize_treasures(outfile,difficulty):
   f = open(outfile,"r+b")
   for p in allpointers:
      f.seek(p-3)
      f.write(st.pack("B",0x00))
      writeitem = choose_item(p,difficulty)
      f.seek(p)
      f.write(st.pack("B",writeitem))
   f.close
if __name__ == "__main__":
   randomize_treasures("Techwriter.sfc")