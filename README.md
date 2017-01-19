# Andelabs2
MISSING NUMBER
```python
def find_missing(lst1,lst2):
	if not lst1 and not lst2:
		return 0
		if not set(lst1) ^ set(lst2):
			return 0
		else:
			return list(set(lst1)^ set(lst2))[0]
```
Above is a python function that compares contents of two lists ,lst1 and lst2.
If the two lists are empty,the function returns 0(`if not lst1 and not lst2:`) The function passes to the next `if` if both lists have content and returns 0 if the conntents of the lists are the same and equal e.g `[1,2,3]` and `[1,2,3]`.Otherwise the function returns the differnce of the two lists i.e `else:return list(set(lst1)^ set(lst2))[0]` as a number .
