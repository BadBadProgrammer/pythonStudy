使用 4 空格缩进，而非 TAB
在小缩进（可以嵌套更深）和大缩进（更易读）之间，4空格是一个很好的折中。TAB 引发了一些混乱，最好弃用

使用空行分隔函数和类，以及函数中的大块代码

统一函数和类命名
推荐类名用 驼峰命名， 函数和方法名用 小写_和_下划线。总是用 self 作为方法的第一个参数

永远继承自 object 并使用新式类,Python 2 来说遵循这条准则很重要
# good
class JSONWriter(object):
    pass

列表/字典/集合推导式优于 map/filter
# bad
map(truncate, filter(lambda x: len(x) > 30, items))
# good
[truncate(x) for x in items if len(x) > 30]

用 isinstance(obj, cls), 不要用 type(obj) == cls
因为 isinstance 涵盖更多情形，包括子类和抽象基类。同时，不要过多使用 isinstance，因为通常应该使用鸭子类型！

用 with 处理文件和锁
with 语句能够巧妙地关闭文件并释放锁，哪怕是在触发异常的情况下。
# bad
somefile = open("somefile.txt", "w")
somefile.write("sometext")
return
 
# good
with open("somefile.txt", "w") as somefile:
    somefile.write("sometext")
return

和 None 相比较要用 is
# bad
if item == None:
    continue
# good
if item is None:
   continue