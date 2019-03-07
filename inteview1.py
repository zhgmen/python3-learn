def read_txt(filename):
	'''
	return type: list

	'''
	with open(filename, 'r') as f:
		return f.readlines()

def read_iter(filename):
	with open(filename, 'r') as f:
		for i in f:
			yield i

from mmap import mmap

def read_mmap(filename):
	#要处理一个大小为10G的文件，但是内存只有4G
	with open(filename, 'r') as f:
		m = mmap(f.fileno(), 0)
		tmp = 0
		for i, char in enumerate(m):
			if char == b'\n':
				yield m[tmp:i+1].decode()
				tmp = i + 1


"""
这个函数接收文件夹的名称作为输入参数
返回该文件夹中文件的路径
以及其包含文件夹中文件的路径
"""
import os

def print_directory_contents(s_path):
	for s_child in os.listdir(s_path):
	    s_child_path = os.path.join(s_path, s_child)
	    if os.path.isdir(s_child_path):
	        print_directory_contents(s_child_path)
	    else:
	        print(s_child_path)
import datetime

def days():
	# 返回值：今天是今年的第几天
	data1 = datetime.date.today()
	data2 = datetime.date(data1.year, 1, 1)
	return (data1-data2).days + 1
#打乱一个排好序的list对象
import random
def unsorted(alist):
	random.shuffle(alist)
	return alist

def sort_as_value(adict):
	return sorted(d.items(), key = lambda x: x[1])
def to_dict(iterable):
	return {key: value for key, value in iterable}

def reverse(astr):
	return astr[::-1]

#将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
def str2dict(astr):
	d = {}
	for item in astr.split("|"):
		key, value = item.split(":")
		d[key] = value

	return d
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
sorted(alist, key = lambda x: x['age'], reverse=True)

#尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。
list = ['a','b','c','d','e']
print(list[10:])

#给定两个列表，怎么找出他们相同的元素和不同的元素？
#利用集合的交集和差集，数据结构
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)


#请写出一段python代码实现删除list里面的重复元素？
#利用集合或字典这两种数据结构的性质，利用哈希表，不会有重复key值
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)