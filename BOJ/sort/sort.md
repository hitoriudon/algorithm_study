## 👉ㅤㅤ정렬(Sort)

  💡ㅤㅤ입력된 n개의 (대소 구분이 가능한) 숫자를, **사용자가 정한 기준**으로 순서에 맞게 정리하는 행위를 뜻함

## 👉ㅤㅤ병합 정렬(Merge Sort)

  💡ㅤㅤ**분할 정복(Divide and Conquer)** 방법을 차용. 하나의 리스트를 두 개의 균등한 크기로** 분할(Divide)**하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법.


![merge](https://user-images.githubusercontent.com/90544907/210303827-1dbacab5-025f-499e-9e8e-e3bb4443a27a.gif)

## 👉ㅤㅤSource Code

```Python
# 리스트 슬라이싱 기호 ':'를 안 쓴 이유: 메모리 낭비가 심함.
# mergeSort 함수 내의 분할 과정에서 재귀가 아닌 :를 사용할 경우,
# 절반으로 슬라이싱한 배열을 새롭게 만들어내는 것이기 때문에, 메모리 낭비가 심하다.
# sublist 길이가 지금처럼 10이 아니라 1000000이라면,
# 50만 50만의 배열을 복제해서 새롭게 만드는 것인데... 메모리 낭비 심함.

numbers = [10,8,7,5,3,1,2,6,4,9]

def mergeSort(unsorted_list, left, right): 
	if left >= right: 
		return # mergeSort -> mergeSort -> merge
	mid = (left + right) // 2
	mergeSort(unsorted_list, left, mid)
	mergeSort(unsorted_list, mid+ 1, right) #divide
	merge(unsorted_list, left, mid + 1, right)

def merge(unsorted_list, left, right, end):
	temp = []
	l, r = left, right
	while l < right and r <= end:
		if unsorted_list[l] <= unsorted_list[r]:
			temp.append(unsorted_list[l])
			l +=1
		else:
			temp.append(unsorted_list[r])
			r +=1
	while l < right:
		temp.append(unsorted_list[l])
		l +=1
	while r <= end:
		temp.append(unsorted_list[r])
		r+=1
	l = left
	for n in temp:
		unsorted_list[l] = n	
		l +=1

print(numbers)
mergeSort(numbers, 0, len(numbers) - 1)
print(numbers)
```

## 📝 출처
_https://bblackscene21.tistory.com/8_
_https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html_
