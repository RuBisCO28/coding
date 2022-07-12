# Python Primer
## Object
- Python is a dynamically typed language, as there is no advance declaration associating an identifier with a particular data type
- The `temperature` identifier has been assigned to a new value, while original continues to refer to the previously existing value

```python
temperature = 98.6
original = temperature
temperature = temperature + 5

print(temperature) # 103.6
print(original) # 98.6
```

## accessors & mutators
- accessors: a.sort()
- mutators: sort(a)

P34

## Mutable vs Immutable
### Mutable
- The object ids are same
```python
a = [1,2,3]

print("a = %s" % a)
print("id(a) = %s" % id(a))

a.append(4)

print("a = %s" % a)
print("id(a) = %s" % id(a))

a = [1, 2, 3]
id(a) = 4397053320
a = [1, 2, 3, 4]
id(a) = 4397053320
```

### Immutable
- The object ids are changed
- Once an instance has been created, its value cannot be changed
  - although an identifier referencing that object can be reassigned to a different value

```python
a = "abc"

print("a = %s" % a)
print("id(a) = %s" % id(a))

a = a + "def"

print("a = %s" % a)
print("id(a) = %s" % id(a))

a = abc
id(a) = 4432244216
a = abcdef
id(a) = 4434341816
```

## Variable

|class|Immutable|
|--|--|
|bool|✅|
|int|✅|
|float|✅|
|list||
|tuple|✅|
|str|✅|
|set||
|frozenset|✅|
|dict||

## Multiple variable
### Mutable
```python
a = [1,2,3]
b = a

a.append(4)

print ("a = %s" % a)
print ("b = %s" % b)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
```

### Immutable
```python
a = "abc"
b = a

a = a + "def"

print ("a = %s" % a)
print ("b = %s" % b)

a = abcdef
b = abc
```

# Python Conveniences
## Conditional Expressions
```python
# Case 1
if n >= 0:
  param = n
else:
  param = −n

result = foo(param) # call the function

# Case 2
param = n if n >= 0 else −n # pick the appropriate value
result = foo(param)
```

## Comprehension Syntax
```python
# Case 1
result = []
for k in range(1, n+1):
  if n % k == 0:
    result.append(k)

# Case 2
result = [k for k in range(1, n+1) if n % k == 0]
```

## Packing and Unpacking of Sequences
```python
for x, y in [ (7, 2), (5, 8), (6, 4) ]:
for k, v in mapping.items():
```

## Simultaneous Assignments
```python
j = 1
k = 2
id(j) # 4343226616
id(k) # 4343226648

j,k = k, j

id(j) # 4343226648
id(k) # 4343226616
j # 2
k # 1
```

## Modules and the Import Statement
- If the module is imported from another scripts, the code under `if name == __main__ :` is not executed
- It is executed only when if the module is directly invoked as a script
```python
if name == __main__ :
```
