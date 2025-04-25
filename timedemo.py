import time

print(10*'-', '时间戳',10*'-')
print(time.time())
print(10*'-', '本地时间元组',10*'-')
localtime = time.localtime()
print(localtime)
print(str(localtime.tm_year)+'-'+str(localtime.tm_mon)+'-'+str(localtime.tm_mday)+' '+str(localtime.tm_hour))

print(10*'-', 'utc时间元组',10*'-')
print(time.gmtime())

print(10*'-', '时间戳的秒数转化时间字符串',10*'-')
print(time.ctime())
print(10*'-', '前一天',10*'-')
print(time.ctime(time.time()-24*60*60))

print(10*'-', '时间元组转为时间戳',10*'-')
print(time.mktime(time.localtime()))

print(10*'-', '时间元组格式化为常见格式',10*'-')
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print(10*'-', '常见格式字符串转为时间元组',10*'-')
print(time.strptime('2025/02/19 11:25:49','%Y/%m/%d %H:%M:%S'))
print(time.strptime('2025/02/19 11:25:49','%Y/%m/%d %H:%M:%S').tm_min)


print(10*'-', '获取一个月前的日期',10*'-')
print(time.ctime(time.time()-30*24*3600))
print(10*'-', '获取一个月前的日期',10*'-')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-30*24*3600)))



print(10*'######')
from  datetime import datetime

print(10*'-', '获取现在的日期',10*'-')
print(datetime.date(datetime.now()))
print(10*'-', '获取现在的时间',10*'-')
print(datetime.time(datetime.now()))
print(10*'-', '拼接日期时间',10*'-')
print(str(datetime.date(datetime.now()))+' '+str(datetime.time(datetime.now())))
print(10*'-', '格式化字符串日期时间',10*'-')
format_str_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(format_str_datetime, type(format_str_datetime))
print(10*'-', '格式化对象日期时间',10*'-')
format_obj_datetime=datetime.strptime(format_str_datetime,'%Y-%m-%d %H:%M:%S')
print(format_obj_datetime, type(format_obj_datetime))

print(10*'-', '一个月前时间日期',10*'-')
from datetime import timedelta
print((datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'))
print(10*'-', '7天后时间日期',10*'-')
print((datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S'))

