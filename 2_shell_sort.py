# -*- coding:utf-8 -*-

# ref: http://python.jobbole.com/82270/
# shell sort.
#基本思想： 
#	插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
#从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。
#是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
#但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素
#（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
#
#   希尔排序是对插入排序的改进。 设定一定的步长，比如3，把原序列分为三组，对他们分别进行直接插入排序
#	然后再把步长改为2,在分别进行排序，
#	最后设为1，再进行排序。

# 步长  n/2   n/4   n/8  n/16......1
class solution:
	def shell_sort_1(self,lists):
		count = len(lists)
		step = 2
		#group 是步长
		group = count / step
		while group > 0:
			#i 是可以被分成的组的数量，且是每个小组第一个元素的下标
			
			#对step 个小组的排序
			for i in range(0, group):
				#j是小组第二个元素的下标
				j = i + group

				#对一个数组的插入排序
				while j < count:
					#插入排序
					k = j - group
					key = lists[j]
					while k >= 0:
						if lists[k] > key:
							lists[k + group] = lists[k]
							lists[k] = key
						k -= group
					j += group
			
			#替换为新的步长
			group /= step
		return lists

if __name__ == '__main__':
	s=solution()
	list1 = [1,3,4,5,9,1,5,2,11,3]
	print s.shell_sort_1(list1)

