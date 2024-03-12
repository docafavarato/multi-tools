# Multi-tools

## About
A multi-functional python module.

## Classes

### Lists
```sh
ascending() # returns the list in ascending order
```

```sh
descending() # returns the list in descending order
```

```sh
min(*args) # returns the lowest numeric item from the list
```

```sh
max(*args) # returns the highest numeric item from the list
```

```sh
sum(*args) # returns the sum of all the numeric items from the list
```

```sh
subtraction(*args) # returns the subtraction of all the numeric items from the list
```

```sh
product(*args) # returns the product of all the numeric items from the list
```

```sh
average(*args) # returns the average of all the numeric items from the given lists
```

```sh
intersection(*args) # returns the intersected items from two different lists
```

```sh
group(*args) # returns a list with all the items from the multiple lists grouped
```

```sh
inverse() # returns a inversed copy of the list
```

```sh
evenodd(*args, mode=0) # returns even or odd values from the list (0 = Even, 1 = Odd)
```

```sh
shuffle(*args) # returns a shuffled version of the list using the random module
```

```sh
to_dict() # transforms the list into a dictionary
```

```sh
clear(*args) # removes all the null items from the given lists
```

```sh
replace(*args, x, y) # replaces items from the given lists
```

### Math
```sh
fibonacci(amount) # returns the fibonacci sequence based on a given amount
```

```sh
pythagorean_theorem(a, b) # returns the unknown size of a right triangle
```

```sh
bhaskara(a, b, c) # returns the two roots of the given equation
```

```sh
arithmetic_progression(a, r, pos) # returns the n-th term of the sequence
```

```sh
logarithm(a, b) # returns the logarithm result
```

### Encryptor
```sh
encrypt(data) # returns a dictionary containing the encrypted data and the key
```

```sh
decrypt(data, key) # returns the decrypted data based on the given key
```

### db
```sh
insert(*values) # inserts data to the database
```

```sh
retrieve_all() # returns all the data
```

```
retrieve_by(key, value) # returns all the data that matches the given key
```

```
retrieve_by_contains(key, value) # returns all the data that contains the given key
```
