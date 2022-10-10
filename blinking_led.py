def conduct(instruction_mapping): 
    cmds = {'ADD': '00101000', 'SUB': '00100101', 'OR': '00111000', #001, 1
          'STR': '01011000', 'LDR': '01011001',
          'MOVW': '00110000', 'MOVT': '00110100',
          'B': '1010'}
    cond = {'AL': '1110', 'NE': '0001', 'PL': '0101'}

    instructions_list = []
    
    for x in instruction_mapping: 
        if x[0] in ['MOVW', 'MOVT']:
            register_number = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int(x[2], 16)))[2:]
            immediate_value = f'{"0"*(16-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{immediate_value[0:4]}{register_number}{immediate_value[4:8]}{immediate_value[8:12]}{immediate_value[12:16]}"
           
            # print(pattern)
        elif x[0] == 'ADD':
            source_register = '{:04b}'.format(int(x[2].replace('R','')))
            destination_register = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int(x[3], 16)))[2:]
            immediate_value = f'{"0"*(12-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{source_register}{destination_register}{immediate_value}"
            
            # print(pattern) 
        elif x[0] == 'LDR':
            source_register = '{:04b}'.format(int(x[2].replace('R','')))
            destination_register = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int("0", 16)))[2:]
            immediate_value = f'{"0"*(12-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{source_register}{destination_register}{immediate_value}"
            
            # print(pattern)
        elif x[0] == 'OR':
            source_register = '{:04b}'.format(int(x[2].replace('R','')))
            destination_register = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int(x[3], 16)))[2:]
            immediate_value = f'{"0"*(12-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{source_register}{destination_register}{immediate_value}"

            # print(pattern)
        elif x[0] == 'STR':
            source_register = '{:04b}'.format(int(x[2].replace('R','')))
            destination_register = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int("0", 16)))[2:]
            immediate_value = f'{"0"*(12-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{source_register}{destination_register}{immediate_value}"
            
            # print(pattern)
        elif x[0] ==  'SUB':
            source_register = '{:04b}'.format(int(x[2].replace('R','')))
            destination_register = '{:04b}'.format(int(x[1].replace('R','')))
            immbin = str(bin(int(x[3], 16)))[2:]
            immediate_value = f'{"0"*(12-len(immbin))}{immbin}'
            pattern = f"1110{cmds[x[0]][:4]}{cmds[x[0]][4:]}{source_register}{destination_register}{immediate_value}"
            
            # print(pattern)
        elif x[0] == 'BNE':
            immbin = str(bin(int(x[1], 16)))[2:]
            immediate_value = f'{"0"*(4-len(immbin))}{immbin}'
            pattern = '00011010' + immediate_value
            
            # print(pattern)
        elif x[0] == 'B': 
            immbin = str(bin(int(x[1], 16)))[2:]
            immediate_value = f'{"0"*(4-len(immbin))}{immbin}'
            pattern = '11101010' + immediate_value
            
            # print(pattern)
        print(' '.join([pattern[a:a+4] for a in range(0, len(pattern), 4)]))
        instructions_list.append(pattern)
    save_to_kernel(instructions_list)
            # print(' '.join([immediate_value[a:a+4] for a in range(0, len(immediate_value), 4)]))

def convertToBinary(n):
   # Function to print binary number for the input decimal using recursion
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

def save_to_kernel(arrayoflines): 
    # 11100011 01000011 01001111 00100000
    strbytes = ''
    for x in arrayoflines:
        bytelis = [x[a:a+8] for a in range(0, len(x), 8)] #splits the line into 8 bit section
        bytelis = [chr(int(a, 2)) for a in reversed(bytelis)] # turns each of those 8 bit things into char
        print(bytelis)
        strbytes += ''.join(bytelis) #combines all those characters to one line
    print(strbytes)
    file = open('kernel7.img', 'wb+') #write in byte form
    file.write(strbytes.encode('iso-8859-15')) #once it writes it above -> encoding turns into the format we want for the kernel file

def read_parser():
    filepath = 'pseudo.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 0
        instructions = []
        while line:
            instructions.append(line.strip().split())
            line = fp.readline()
            cnt += 1
    return instructions

conduct(read_parser())




 