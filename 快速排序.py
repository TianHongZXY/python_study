def quicksort(array):
	if len(array) < 2:#递归条件
		return array
	else:
		pivot = array[0] #基准值
		less = [i for i in array[1:] if i <= pivot] #原数组中所有小于基准值的元素构成的子数组
		greater = [i for i in array[1:] if i > pivot] #原数组中所有大于基准值的元素构成的子数组

		return quicksort(less) + [pivot] + quicksort(greater) #递归
if __name__ == '__main__':
	print(quicksort([3,2,1,5,4,7,3,8,6,413,23,3124,42134,3132]))
