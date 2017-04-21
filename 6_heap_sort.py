# 堆排序
# http://blog.csdn.net/xiaoxiaoxuewen/article/details/7570621/

def adjust_heap(lists,i,size):
	'''lists 是数组，i为根节点的下标，size为数组长度'''
	#节点i的左右孩子
	lchild = 2*i+1
	rchild = 2*i+2
	max = i
	# size/2的长度限制，是因为所有的非叶子节点都在数组的前一半
	if i <size/2:
		#若左叶子大，则交换
		if lchild<size and lists[lchild]>lists[max]:
			max = lchild
		if rchild<size and lists[rchild]>lists[max]:
			max = rchild
		if max != i:
			lists[max],lists[i] = lists[i],lists[max]
			#对于非叶子节点，递归调整
			adjust_heap(lists,max,size)

def build_heap(lists,size):
	#对于每个节点，都进行大顶堆调整
	for i in range(0,size/2)[::-1]:
		adjust_heap(lists,i,size)

def heap_sort(lists):
	size = len(lists):
	build_heap(lists,size)
	for i in range(0,size)[::-1]:
		lists[0],lists[i] = lists[i],lists[0]
		adjust_heap(lists,0,i)