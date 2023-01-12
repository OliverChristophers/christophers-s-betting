import xlsxwriter
import json


def stringlist_to_list(list_as_string):
    list_as_list = json.loads(list_as_string)
    return list_as_list

gamename = 'tottenham-v-portsmouth'

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'] 
ovun = ['-', '+']
exex = ['0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5', '0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5']

workbook = xlsxwriter.Workbook(f'{gamename}.xlsx')
worksheet = workbook.add_worksheet('over-under')

numb = -1

for lett in letters:
    numb += 1
    if lett in ['A', 'J']:
        worksheet.write(lett + str(1), 'Data Point Index')
    else:
        if numb <= (len(letters) - 2) / 2:
            worksheet.write(lett + str(1), ovun[0]+str(exex[letters.index(lett) - 1]))
        else:
            worksheet.write(lett + str(1), ovun[1]+str(exex[letters.index(lett) - 2]))



file = open(f'{gamename}.txt')
number = 0
count = 1
for line in file:
    number += 1
    if number % 3 == 0:
        count += 1
        y = line.split('Total Goals Over/Under, ')
        newy = y[-1]
        newtxt = ''
        for cvhar in newy:
            if cvhar != "'":
                newtxt += cvhar
        
        newadfg = ''
        for chara in newtxt:
            if chara == 'S':
                pass
            elif chara == 'P':
                newadfg += '0'
            else:
                newadfg += chara

        newy = stringlist_to_list(newadfg)

        list_ok = []
        list_cool = []
        list_swag = []
        if len(newy) >= 2:
            for inner in newy:

                list_ok.append([float(inner[0]), float(inner[1])])
            for inner in list_ok:
                if inner[0] not in list_cool:
                    list_cool.append(inner[0])
                    list_swag.append(inner)
                else:
                    list_swag[list_cool.index(inner[0])].append(inner[1])
            list_swag.sort(key=lambda x: x[0], reverse=False)
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'] 
            exex = ['0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5', '0.5', '1.5', '2.5', '3.5', '4.5', '5.5', '6.5', '7.5']
            worksheet.write('A' + str(count), count - 1)
            worksheet.write('J' + str(count), count - 1)
            for inner in list_swag:
                if len(inner) == 3:
                    ind = exex.index(str(inner[0]))
                    worksheet.write(letters[ind + 1] + str(count), inner[1])
                    worksheet.write(letters[int(ind + 10)] + str(count), inner[2])

workbook.close()