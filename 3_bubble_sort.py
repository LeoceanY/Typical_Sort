# -*- coding:utf-8 -*-
# ref: http://python.jobbole.com/82270/
# bubble sort.
#基本思想： 

# 这种写法的解读, 每个元素都跟第一个位置比较，若小，则替换，那么一次循环之后，第一个位置必定是最小的元素。
# 之后，对第二个位置进行判断。以此类推。
class solution:

#每次对相邻元素两两比较，较轻的元素就会逐渐上浮。
#执行n遍，则所有元素都比较过了。
	def bubble_sort_2(self,list_orig):
		l = len(list_orig)
		for i in range(0,l):
			for j in range(0,l-i-1):
				if list_orig[j] > list_orig[j+1]:
						list_orig[j],list_orig[j+1] = list_orig[j+1],list_orig[j]
				print list_orig
			print "~~"
			print list_orig

if __name__ == '__main__':
	s=solution()
	list1 = [10,4,8,3,7,2]
	print s.bubble_sort_2(list1)

