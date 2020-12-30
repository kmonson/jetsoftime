import random as rand
import struct as st

shop_starts = list(range(0xC2C6F, 0xC2C9D, 2))
regular_shops = [0xC2C6F, 0xC2C73, 0xC2C77, 0xC2C79, 0xC2C85] + list(range(0xC2C89, 0xC2C91, 2))
good_shops = [0xC2C71, 0xC2C75, 0xC2C7D, 0xC2C81, 0xC2C83, 0xC2C87, 0xC2C93, 0xC2C97, 0xC2C99]
best_shops = [0xC2C7B, 0xC2C7F, 0xC2C9B]
forbid_shops = [0xC2C91, 0xC2C95]
llvlitems = [0x95, 0x98, 0x99, 0x97, 0x96, 0xA4, 0x02, 0x03, 0x12, 0x13, 0x20, 0x21, 0x2F, 0x30, 0x3C, 0x7E, 0x7F, 0x80,
             0x5C, 0x5D, 0x5E,
             0x5F, 0x60, 0x61]
llvlconsumables = [0xBD, 0xBE, 0xC6, 0xC7, 0xC8]
plvlitems = [0xAB, 0xA6, 0x9C, 0xB4, 0xAC, 0x04, 0x05, 0x0F, 0xB9, 0x14, 0x22, 0x23, 0x31, 0x81, 0x82, 0x62, 0x63, 0x64,
             0x65]
plvlconsumables = [0xBE, 0xC0]
mlvlitems = [0xA8, 0xA9, 0xA0, 0xA7, 0x9D, 0x9E, 0x9F, 0x06, 0x07, 0x08, 0x15, 0x16, 0x24, 0x25, 0x32, 0x33, 0x34, 0x3E,
             0x3F, 0x4C, 0x83,
             0x84, 0x8B, 0x66, 0x67, 0x75, 0x76, 0x77, 0x78, 0x79]
mlvlconsumables = [0xBF, 0xC1, 0xCA, 0xCB, 0xCC]
glvlitems = [0xAD, 0xB5, 0xB6, 0xB7, 0xA1, 0xA2, 0x09, 0x0A, 0x10, 0x17, 0x18, 0x26, 0x29, 0x35, 0x36, 0x40, 0x43, 0x4D,
             0x85,
             0x88, 0x92, 0x93, 0x68, 0x69, 0x71, 0x72, 0x73, 0x74]
glvlconsumables = [0xBF, 0xC2, 0xC4]
hlvlitems = [0x9A, 0x9B, 0xA3, 0xBA, 0x0B, 0x0C, 0x0D, 0x19, 0x1A, 0x27, 0x37, 0x38, 0x41, 0x4E, 0x89, 0x8A, 0x8C, 0x8D,
             0x8E, 0x6A, 0x6E, 0x70]
hlvlconsumables = [0xC3, 0xC4]
alvlitems = [0xBB, 0x0E, 0x53, 0x54, 0x55, 0x28, 0x39, 0x91, 0x86, 0x8F, 0x6C, 0x7A, 0x6D, 0x6B]
alvlconsumables = [0xC3, 0xC5]


def pick_items(shop, rand_num):
    if shop in regular_shops:
        if rand_num > 4:
            item = rand.choice(llvlconsumables + plvlconsumables)
        else:
            item = rand.choice(plvlitems + mlvlitems)
    elif shop in good_shops:
        if rand_num < 5:
            item = rand.choice(plvlconsumables + mlvlconsumables)
        else:
            item = rand.choice(mlvlitems + glvlitems)
    elif shop in best_shops:
        if rand_num < 5:
            item = rand.choice(glvlconsumables + hlvlconsumables + alvlconsumables)
        else:
            item = rand.choice(glvlitems + hlvlitems + alvlitems)
    return item


def write_slots(file_pointer, shop_start, items, shop_address):
    buffer = []
    item_count = items
    while items > 0:
        if items == 1:
            item = 0x00
        else:
            rand_num = rand.randrange(0, 10, 1)
            item = pick_items(shop_start, rand_num)
        # Guarantee for Lapises from Fritz's and Fiona's shop
        if shop_start == 0xC2C71 or shop_start == 0xC2C99:
            if items == item_count:
                item = 0xCA
        # Guarantee for Amulets from shops in Kajar and the Black Omen
        if shop_start == 0xC2C7B or shop_start == 0xC2C9B:
            if items == item_count:
                item = 0x9A
        if item in buffer:
            continue
        buffer.append(item)
        file_pointer.seek(shop_address)
        file_pointer.write(st.pack("B", item))
        shop_address += 1
        items -= 1
    return shop_address


def warranty_shop(file_pointer):
    shop_address = 0x1AFC29
    guaranteed_items = [0x0, 0xC8, 0xC7, rand.choice([0x6, 0x7, 0x8]), rand.choice([0x15, 0x16, 0x17]),
                        rand.choice([0x24, 0x25,
                                     0x26]), rand.choice([0x31, 0x32, 0x33]), rand.choice([0x3E, 0x3F, 0x40, 0x43])]
    shop_size = len(guaranteed_items) - 1
    while shop_size > -1:
        shop_address = write_guarantee(file_pointer, shop_address, guaranteed_items[shop_size])
        shop_size -= 1


def write_guarantee(file_pointer, shop_address, item):
    file_pointer.seek(shop_address)
    file_pointer.write(st.pack("B", item))
    shop_address += 1
    return shop_address


def randomize_shops(outfile):
    shop_pointer = 0xFC31
    shop_address = 0x1AFC31
    f = open(outfile, "r+b")
    warranty_shop(f)
    for start in shop_starts:
        if start in forbid_shops:
            f.seek(start)
            f.write(st.pack("H", shop_pointer + 1))
            continue
        shop_items = rand.randrange(4, 10)
        f.seek(start)
        f.write(st.pack("H", shop_pointer))
        shop_pointer += shop_items
        shop_address = write_slots(f, start, shop_items, shop_address)
    f.close


if __name__ == "__main__":
    randomize_shops("Project.sfc")
