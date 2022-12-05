# --- Day 1 ---
import numpy as np

in_file = open("01_input.txt",'r')
lines = in_file.readlines()

elf_dict = {}

n_elf = 0
elf_dict[n_elf] = np.array([])
elf_sum = np.array([])

for line in lines:
    if len(line) == 1:
        elf_sum = np.append(elf_sum,elf_dict[n_elf].sum())
        n_elf += 1
        elf_dict[n_elf] = np.array([])
    else:
        elf_dict[n_elf] = np.append(elf_dict[n_elf],float(line))

print(max(elf_sum))

print(np.sort(elf_sum)[-3:].sum())
