import struct as st
import random as rand
import patcher as bossmutator
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
early_boss_ids = [0x90,0x97,0x98,0x99,0xA6,0xA7,0xA9,0xB3,0xB4,0xBA,0xBB]
mid_boss_ids = [0x3A,0x93,0x94,0x9B,0x9C,0x9E,0x9F,0xAD,0xB5,0xB6,0xB7,0xBD,0xBE,0xC7,0xCB,0xCC,0xCD,0xCE,0xCF,0xD4,
0xD7,0xD8,0xEB,0xED,0xEF,0xF6,0xF7,0xF8]
late_boss_ids = [0x0A,0x25,0x95,0x9A,0x6E,0x6F,0xB0,0xB1,0xB2,0x35,0x36,0x37,0x38,0xA0,0xA5,0xA8,0xBC,0xD1,0xD2,0xD3,
0xF9]

"""boss_ids = [0x0A, 0x0B, 0x0F, 0x25, 0x35, 0x37, 0x3A, 0x4F, 0x6E, 0x90, 0x95, 0x99,
0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA5, 0xA8, 0xA9, 0xAD, 0xB0, 0xB4, 0xB8, 0xBA, 0xBB, 0xBC, 
0xBD, 0xBE, 0xC7, 0xD1, 0xD4, 0xD8, 0xCB, 0xCC, 0xCD, 0xCE, 0xE6, 0xEB, 0xEF, 0xF6, 0xF8, 0xF9]

tabs =[0xCD,0xCD,0xCD,0xCD,0xCE,0xCE,0xCE,0xCE,0xCF,0xCF]"""
enemy_drop_address = 0xC5E04
enemy_charm_address = 0xC5E05
common_enemy_ids = [0x08,0x0C,0x0D,0x10,0x11,0x12,0x13,0x15,0x19,0x1A,0x1C,0x1E,0x23,0x33,0x45,0x47,0x48,0x4B,0x50,
0x5B,0x5E,0x66,0x71,0x73,0x74,0x8D,0x92]
uncommon_enemy_ids = [0x01,0x03,0x04,0x05,0x16,0x17,0x1D,0x22,0x26,0x27,0x29,0x2A,0x2E,0x2F,0x31,0x32,0x34,0x3D,
0x3E,0x3F,0x46,0x4A,0x4C,0x4E,0x51,0x54,0x55,0x57,0x5B,0x5C,0x5D,0x61,0x63,0x65,0x69,0x6A,0x6B,0x6C,0x79,0x7B,0x7C,
0x7D,0x83,0x86,0x87,0x88,0x89,0x8A,0x8C,0x97,0x98,0xA3,0xAE,0xEE,0xF2]
rare_enemy_ids = [0x02,0x07,0x09,0x0E,0x1B,0x20,0x28,0x2B,0x2D,0x30,0x39,0x3A,0x40,0x41,0x42,0x49,0x52,0x53,0x56,0x58,
0x59,0x62,0x6A,0x6D,0x70,0x75,0x76,0x7A,0x81,0x84,0x85,0x8B,0x8E,0x96,0xA4,0xAA,0xAC,0xC1,0xC8,0xD5,0xD6,0xD9]
rarest_enemy_ids = [0,0x2C,0x43,0x5F,0x82]
def randomize_enemy_stuff(f,difficulty):
  outfile = f
  f = open(f, "r+b")
  randomize_boss_stuff(f,difficulty)
  randomize_midbosses(outfile,f)
  if difficulty == "hard":
      for enemy in common_enemy_ids:
          drop = 0
          charm = 0
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in uncommon_enemy_ids:
          drop = 0
          charm = rand.choice(mlvlconsumables + glvlconsumables)
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in rare_enemy_ids:
          drop = rand.choice(plvlconsumables+mlvlconsumables+glvlconsumables)
          charm = rand.choice(mlvlitems+glvlitems)
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in rarest_enemy_ids:
          rand_num = rand.randrange(0,10,1)
          if rand_num > 8:
              drop = rand.choice(mlvlitems+glvlitems+hlvlitems+alvlitems)
          else:
              drop = rand.choice(mlvlconsumables+glvlconsumables+hlvlconsumables+alvlconsumables)
          charm = drop
          if rand_num < 7:
              drop = 0
          write_enemy_stuff(drop,charm,f,enemy)
  else:
      for enemy in common_enemy_ids:
          rand_num = rand.randrange(0,10,1)
          if rand_num > 7:
              drop = rand.choice(plvlitems+llvlitems)
          else:
              drop = rand.choice(plvlconsumables+llvlconsumables)
          charm = drop
          if rand_num < 5:
              drop = 0	 
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in uncommon_enemy_ids:
          rand_num = rand.randrange(0,10,1)
          if rand_num > 7:
              drop = rand.choice(mlvlitems+glvlitems)
          else:
              drop = rand.choice(mlvlconsumables+glvlconsumables)
          charm = drop
          if rand_num < 6:
              drop = 0	 
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in rare_enemy_ids:
          rand_num = rand.randrange(0,10,1)
          if rand_num > 7:
              drop = rand.choice(mlvlitems+glvlitems+hlvlitems)
          else:
              drop = rand.choice(mlvlconsumables+glvlconsumables+hlvlconsumables)
          charm = drop
          if rand_num < 6:
              drop = 0	 
          write_enemy_stuff(drop,charm,f,enemy)
      for enemy in rarest_enemy_ids:
          rand_num = rand.randrange(0,10,1)
          if rand_num > 8:
              drop = rand.choice(hlvlitems+alvlitems)
          else:
              drop = rand.choice(glvlconsumables+hlvlconsumables+alvlconsumables)
          charm = drop
          if rand_num < 7:
              drop = 0	 
          write_enemy_stuff(drop,charm,f,enemy)
  #Small block to randomize status inflicted by Obstacle/Chaotic Zone
  rand_num = rand.randrange(0,10,1)
  f.seek(0xC7EEB)
#  if rand_num < 2:
#      status_effect = rand.choice(1,0x40) #Blind, Poison
  if rand_num < 8:
      status_effect = rand.choice([2,8,0x20]) #Sleep, Lock, Slow
  else:
      status_effect = rand.choice([4,0x80]) #Chaos, Stop
  f.write(st.pack("B",status_effect))
  f.close
def randomize_boss_stuff(f,difficulty):
    for id in early_boss_ids:
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            drop = rand.choice(alvlitems)
        elif rand_num > 74:
            drop = rand.choice(glvlitems + hlvlitems)
        else:
            drop = rand.choice(mlvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            charm = rand.choice(alvlitems)
        elif rand_num > 74:
            charm = rand.choice(glvlitems + hlvlitems)
        else:
            charm = rand.choice(mlvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 74 or (difficulty == "hard" and rand_num > 49):
            drop = rand.choice(mlvlconsumables + glvlconsumables + hlvlconsumables + alvlconsumables)
        if difficulty == "hard":
            rand_num = rand.randrange(0,100,1)
            if rand_num > 49:
                drop = 0
        write_enemy_stuff(drop,charm,f,id)
    for id in mid_boss_ids:
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            drop = rand.choice(alvlitems)
        elif rand_num > 74:
            drop = rand.choice(glvlitems + hlvlitems)
        else:
            drop = rand.choice(glvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            charm = rand.choice(alvlitems)
        elif rand_num > 74:
            charm = rand.choice(glvlitems + hlvlitems)
        else:
            charm = rand.choice(glvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 74 or (difficulty == "hard" and rand_num > 49):
            drop = rand.choice(mlvlconsumables + glvlconsumables + hlvlconsumables + alvlconsumables)
        write_enemy_stuff(drop,charm,f,id)
    for id in late_boss_ids:
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            drop = rand.choice(alvlitems)
        else:
            drop = rand.choice(glvlitems + hlvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 94:
            charm = rand.choice(alvlitems)
        else:
            charm = rand.choice(glvlitems + hlvlitems)
        rand_num = rand.randrange(0,100,1)
        if rand_num > 74 or (difficulty == "hard" and rand_num > 49):
            drop = rand.choice(mlvlconsumables + glvlconsumables + hlvlconsumables + alvlconsumables)
        write_enemy_stuff(drop,charm,f,id)
def randomize_midbosses(outfile,f):
    magus_hp = rand.randrange(10000,16000,1000)
    tyrano_hp = rand.randrange(8000,14000,1000)
    magus_select = rand.randrange(0,7)
    tyrano_element = rand.randrange(0,5)
    f.seek(0xC57E4)
    f.write(st.pack("H",tyrano_hp))
    f.seek(0xC5D5F)
    f.write(st.pack("H",magus_hp))
    if magus_select == 0:
       bossmutator.patch_file("patches/magus_c.txt",outfile)
    elif magus_select == 1:
       bossmutator.patch_file("patches/magus_m.txt",outfile)
    elif magus_select == 2:
       bossmutator.patch_file("patches/magus_l.txt",outfile)
    elif magus_select == 3:
       bossmutator.patch_file("patches/magus_r.txt",outfile)
    elif magus_select == 4:
       bossmutator.patch_file("patches/magus_f.txt",outfile)
    elif magus_select == 5:
       bossmutator.patch_file("patches/magus_a.txt",outfile)
    if tyrano_element == 0:
       bossmutator.patch_file("patches/tyrano_i.txt",outfile)
    elif tyrano_element == 1:
       bossmutator.patch_file("patches/tyrano_l.txt",outfile)
    elif tyrano_element == 2:
       bossmutator.patch_file("patches/tyrano_s.txt",outfile)
    elif tyrano_element == 3:
       bossmutator.patch_file("patches/tyrano_n.txt",outfile)
def write_enemy_stuff(drop,charm,f,enemy_id):
  f.seek(enemy_drop_address + 7 * (enemy_id))
  f.write(st.pack("B",drop))
  f.seek(enemy_charm_address + 7 * (enemy_id))
  f.write(st.pack("B", charm))
if __name__ == "__main__":
   randomize_enemy_stuff("Project.sfc")