## ๐ใคใค์ ๋ ฌ(Sort)

  ๐กใคใค์๋ ฅ๋ n๊ฐ์ (๋์ ๊ตฌ๋ถ์ด ๊ฐ๋ฅํ) ์ซ์๋ฅผ, **์ฌ์ฉ์๊ฐ ์ ํ ๊ธฐ์ค**์ผ๋ก ์์์ ๋ง๊ฒ ์ ๋ฆฌํ๋ ํ์๋ฅผ ๋ปํจ

## ๐ใคใค๋ณํฉ ์ ๋ ฌ(Merge Sort)

  ๐กใคใค**๋ถํ  ์ ๋ณต(Divide and Conquer)** ๋ฐฉ๋ฒ์ ์ฐจ์ฉ. ํ๋์ ๋ฆฌ์คํธ๋ฅผ ๋ ๊ฐ์ ๊ท ๋ฑํ ํฌ๊ธฐ๋ก** ๋ถํ (Divide)**ํ๊ณ  ๋ถํ ๋ ๋ถ๋ถ ๋ฆฌ์คํธ๋ฅผ ์ ๋ ฌํ ๋ค์, ๋ ๊ฐ์ ์ ๋ ฌ๋ ๋ถ๋ถ ๋ฆฌ์คํธ๋ฅผ ํฉํ์ฌ ์ ์ฒด๊ฐ ์ ๋ ฌ๋ ๋ฆฌ์คํธ๊ฐ ๋๊ฒ ํ๋ ๋ฐฉ๋ฒ.


![merge](https://user-images.githubusercontent.com/90544907/210303827-1dbacab5-025f-499e-9e8e-e3bb4443a27a.gif)

## ๐ใคใคSource Code

```Python
# ๋ฆฌ์คํธ ์ฌ๋ผ์ด์ฑ ๊ธฐํธ ':'๋ฅผ ์ ์ด ์ด์ : ๋ฉ๋ชจ๋ฆฌ ๋ญ๋น๊ฐ ์ฌํจ.
# mergeSort ํจ์ ๋ด์ ๋ถํ  ๊ณผ์ ์์ ์ฌ๊ท๊ฐ ์๋ :๋ฅผ ์ฌ์ฉํ  ๊ฒฝ์ฐ,
# ์ ๋ฐ์ผ๋ก ์ฌ๋ผ์ด์ฑํ ๋ฐฐ์ด์ ์๋กญ๊ฒ ๋ง๋ค์ด๋ด๋ ๊ฒ์ด๊ธฐ ๋๋ฌธ์, ๋ฉ๋ชจ๋ฆฌ ๋ญ๋น๊ฐ ์ฌํ๋ค.
# sublist ๊ธธ์ด๊ฐ ์ง๊ธ์ฒ๋ผ 10์ด ์๋๋ผ 1000000์ด๋ผ๋ฉด,
# 50๋ง 50๋ง์ ๋ฐฐ์ด์ ๋ณต์ ํด์ ์๋กญ๊ฒ ๋ง๋๋ ๊ฒ์ธ๋ฐ... ๋ฉ๋ชจ๋ฆฌ ๋ญ๋น ์ฌํจ.

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

## ๐ ์ถ์ฒ
_https://bblackscene21.tistory.com/8_
_https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html_
