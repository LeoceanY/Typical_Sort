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
		while l > 0:
			#因为一次冒泡后，最大的数字肯定会沉到最底部，所以最后一个数字不用再交换了，l-1
			for j in range(1,l):
				if list_orig[j-1] > list_orig[j]:
						list_orig[j-1],list_orig[j] = list_orig[j],list_orig[j-1]
				print list_orig
			l = l - 1
			print "~~"
			print list_orig

if __name__ == '__main__':
	s=solution()
	list1 = [10,4,8,3,7,2]
	print s.bubble_sort_2(list1)

