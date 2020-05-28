![main](./png/main.png)
# Task 
![task](./png/task.png)

Необходимо выяснить хватит ли пуль на драконов или нет. Написать `True` если хватит и `False` если нет. 
# Solution

```python
def hero(bullets, dragons):
	survive = bullets/dragons
	print(survive)
	answer = None
	if survive>=2:
		answer=survive
	print(bool(answer))
	return bool(answer)
```

В python `По умолчанию любой объект имеет истинное значение.`, поэтому я использовал константу `None`

## Sample Tests: 
```python
Test.assert_equals(hero(10, 5), True)
Test.assert_equals(hero(7, 4), False)
Test.assert_equals(hero(4, 5), False)
Test.assert_equals(hero(100, 40), True)
Test.assert_equals(hero(1500, 751), False)
Test.assert_equals(hero(0, 1), False)
```