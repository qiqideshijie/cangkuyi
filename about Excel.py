#引用模块
import pymysql
import xlrd

con = pymysql.connect(host="localhost",user="root",password="123456",database="a")

#创建控制台
cursor = con.cursor()


#excel文件提取
wb = xlrd.open_workbook(filename=r"E:\python自动化测试\专属项目\python\day07\2020年每个月的销售情况.xlsx",encoding_override=True)
for i in ('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'):#循环创建12个表
    sql = """
    CREATE TABLE `%s` (
      `日期` varchar(20) DEFAULT NULL,
      `服装名称` varchar(20) DEFAULT NULL,
      `价格/件` decimal(20,2) DEFAULT NULL,
      `本月库存数量` int(11) DEFAULT NULL,
      `销售量/每日` int(11) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """ %i
#%s占位符，%i：把i赋给%s


#用控制台执行sql语句，提交到缓冲区
cursor.execute(sql)

#提交到数据库
con.commit()

#关闭资源，先开的后关，后开的前关。
cursor.close()
con.close()

for k in range(0,12):
    # 打开excel表选项卡
    table = wb.sheet_by_index(k)#循环12个选项卡
    #获取列
    lie = table.nrows
    for i in range(1,lie):
        #table.cell(i,0) 获取当前Excel表中第i行，第0列，并赋值给。。。
        riqi = table.cell(i,0).value
        mingcheng = table.cell(i,1).value
        jiage = table.cell(i,2).value
        kucun = table.cell(i,3).value
        shouliang = table.cell(i,4).value
        for j in ('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'):#循环写入到数据库12个表中
            sql = "insert into "+j+" values (%s,%s,%s,%s,%s)"#写入数据，+j+：在sql语句中，只有这样写才能把j表名循环
            param = [riqi,mingcheng,jiage,kucun,shouliang]
            cursor.execute(sql,param)  # 执行sql语句
            con.commit()  # 提交数据
            cursor.close()  # 关闭资源
            con.close()

