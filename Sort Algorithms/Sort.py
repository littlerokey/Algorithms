"""
1.1插入排序
	基本思想：通过构建有序序列，对于未排序数据，在已排序序列中从后往前扫描，找到相应位置并插入；
	算法步骤：1.将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列；
				2.从头到尾一次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
				（如果待插入元素与有序序列中的某个元素相等，则将待插入的元素插入到相等元素的后面《稳定》）。
"""
def insert_sort(lists):
	count = len(lists)
	for i in range(1, count):
		key = lists[i]
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j + 1] = lists[j]
				lists[j] = key
			j -= 1
	return lists

"""
1.2希尔排序
	基本思想：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录基本有序时，再对全体记录进行一次直接插入排序；
	算法步骤：1.选择一个增量序列t1,t2,...,tk,其中ti>tj,tk=1；
				2.按增量序列个数k，对序列进行k趟排序；
				3.每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m的子序列，分别对各子序列进行直接插入排序。
				仅增量因子为1时，整个序列作为一个表来处理，表长度即为整个序列的长度;
"""
def shell_sort(lists):
	count = len(lists)
	step = 2
	group = count / step
	while group > 0:
		for i in range(0, group):
			j = i + group
			while j < count:
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						lists[k + group] = lists[k]
						lists[k] = key
					k -= group
				j += group
		group /= step
	return lists

"""
2.1直接选择排序
	基本思想：
	算法步骤：1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；
				2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾；
				3.重复第二步，直到所有元素均排序完毕；
"""
def select_sort(lists):
	count = len(lists)
	for i in range(0, count):
		min = i
		for j in range(i + 1, count):
			if lists[min] > lists[j]:
				min = j
		lists[min], lists[i] = lists[i], lists[min]
	return lists
"""
2.2堆排序
	基本思想：堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是小于（或大于）它的父节点；
	算法步骤：1.创建一个堆H[0...n-1]
				2.把堆首（最大值）和堆尾互换；
				3.把堆的尺寸缩小1，并调用shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
				4.重复步骤2，直到堆的尺寸为1；
	
"""
def adjust_heap(lists, i, size):
	lchild = 2 * i + 1
	rchild = 2 * i + 2
	max = i
	if i < size / 2:
		if lchild < size and lists[lchild] > lists[max]:
			max = lchild
		if rchild < size and lists[rchild] > lists[max]:
			max = rchild
		if max != i:
			lists[max], lists[i] = lists[i], lists[max]
			adjust_heap(lists, max, size)

def build_heap(lists, size):
	for i in range(0, (size/2))[::-1]:
		adjust_heap(lists, i, size)

def heap_sort(lists):
	size = len(lists)
	build_heap(lists, size)
	for i in range(0, size)[::-1]:
		lists[0], lists[i] = lists[i], lists[0]
		adjust_heap(lists, 0, 1)
"""
3.1交换排序--冒泡排序
	基本思想：重复地走访过要排序的数列，一次比较两个元素，小元素交换至前面；
	算法步骤：1.比较相邻的元素，如果第一个比第二个大，就交换；
				2.对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对；
				3.针对所有元素重复以上的步骤；
				4.持续每次对越来越少的元素重复以上的步骤，直到没有任何一对数字需要比较；
"""
def bubble_sort(lists):
	count = len(lists)
	for i in range(0, count):
		for j in range(i + 1, count):
			if lists[i] > lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	return lists
"""
3.2交换排序--快速排序
	基本思想：使用分治法策略把一个串行分为两个子串行；
	算法步骤：1.从数列中挑出一个元素，称为基准；
				2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准后面；在这个分区退出之后，该基准就处于数列中间，这称为分区操作；
				3.递归地把小于基准值元素的子数列和大于基准值元素的字数列排序；
"""
def quick_sort(lists, left, right):
	if left >= right:
		return lists
		key = lists[left]
		low = left
		high = right
		while left < right:
			while left < right and lists[right] >= key:
				right -= 1
			lists[left] = lists[right]
			while left < right and lists[left] <= key:
				left += 1
			lists[right] = lists[left]
		lists[right] = key
		quick_sort(lists, low, left - 1)
		quick_sort(lists, left + 1, high)
	return lists
			pass

#另一种写法
def QuickSort(myList, start, end):
	#判断是否小于high，如果为false，直接返回
	if start < end:
		i, j = start, end
		#设置基准数
		base = myList[i]

		while i < j:
			#如果列表后边的数，比基准大或相等，则前移一位直到有比基准小的数出现
			while (i < j) and (myList[j] >= base):
				j = j - 1

			#如找到，则把第j个元素赋值给第i个元素，此时表中i,j个元素相等
			myList[i] = myList[j]

			while (i < j) and (myList[i] <= base):
				i = i + 1
			myList[j] = myList[i]
		#做完第一轮比较后，列表被分成了两个半区，并且i=j，需要设置回base
		myList[i] = base

		#递归前后半区
		QuickSort(myList, start, i - 1)
		QuickSort(myList, j + 1, end)
	return myList


"""
4.1归并排序
	算法步骤：1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
				2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；
				3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
				4.重复步骤3直到某一指针达到序列尾；
				5.将另一序列剩下的所有元素直接复制到合并序列尾；
"""
def merge(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	num = len(lists) / 2
	left = merge_sort(lists[:num])
	right = merge_sort(lists[num:])
	return merge(left, right)
"""
5.1基数排序
	基本思想：属于分配式排序，又称桶子法bucker sort或bin sort，是通过键值的部分资讯，将要排序的元素分配至某些桶中，藉以达到排序的作用；
"""
import math
def radix_sort(lists, radix = 10):
	k = int(math.ceil(math.log(max(lists), radix)))
	bucket = [[] for i in range(radix)]
	for i in range(1, k + 1):
		for j in lists:
			bucket[j/(radix**(i-1)) % (radix**i)].append(j)
		del lists[:]
		for z in bucket:
			lists += z
			del z[:]
	return lists

