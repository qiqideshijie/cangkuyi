import xlrd
book=xlrd.open_workbook(r"E:\Pythonevn\2020年每个月的销售情况.xlsx",encoding_override=True)
sheet1 = book.sheet_by_index(0)
rows,cols = sheet1.nrows,sheet1.ncols
for row in range(rows):
    for col in range(cols):
        print(sheet1.cell(row,col).value,end='')
    print('')
sumcount=0;
for i in range(1,31):
    sumcount+=sheet1.cell(i,4).value
print("销售量：",sumcount)
sumoney =0
for j in range(1,31):
    sumoney+=sheet1.cell(j,2).value*sheet1.cell(j,4).value
print("总销售额：",sumoney)
print("平均销售量：",sumcount/30)

y,n,f,p,t,c =0,0,0,0,0,0
for o in range(1,31):
    if sheet1.cell(o,1).value=='羽绒服':
        y +=sheet1.cell(o,4).value
    elif sheet1.cell(o,1).value=='牛仔裤':
        n += sheet1.cell(o, 4).value
    elif sheet1.cell(o, 1).value == '风衣':
        f += sheet1.cell(o, 4).value
    elif sheet1.cell(o, 1).value == '皮草':
        p += sheet1.cell(o, 4).value
    elif sheet1.cell(o, 1).value == 'T血':
        t += sheet1.cell(o, 4).value
    elif sheet1.cell(o, 1).value == '衬衫':
        c += sheet1.cell(o, 4).value

    print('羽绒服销售占比：', 253.6 * y / sumoney * 100, '%')
    print('牛仔裤销售占比：', 86.3 * n / sumoney * 100, '%')
    print('风衣销售占比：', 96.8 * f / sumoney * 100, '%')
    print('皮草销售占比：', 135.9 * p / sumoney * 100, '%')
    print('T血销售占比：', 65.8 * t / sumoney * 100, '%')
    print('衬衫销售占比：', 49.3 * c / sumoney * 100, '%')
