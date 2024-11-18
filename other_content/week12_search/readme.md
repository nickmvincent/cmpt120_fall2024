# Week 12, Search

This folder will contain some exercise related to searching.

This is part of our light introduction to "dealing with data".

We'll cover:
- The linear and binary search algorithms and code
- The selection and merge sort algorithms and code
- The implications and “complexity” of these algorithms


## Search Efficiency


## What code you'll actually write

Of course, we won't build our own Google

But you will write Python code to search through lists and sort data.


## Linear Search

Assume you're given a list of numbers (e.g. of shoe sizes) and number that we're "looking for", can you write a function that will return True if the search term is in the list, and False otherwise? 

Example: We're given `scores = [1,7,10,17,22,25,49]`. We're looking for 49. Of course, we know we can do `49 in scores`.

But what does the function look like?

<details>
<summary> Show answer </summary>

```python
def linear_search_bool(input_list, search_term):
  for item in search_list:
    if item == search_term:
      return True
  return False
```
</details>

## Testing

Now, write 4 tests for this function (two different lists and two different search terms).

## Linear search with while loop


## Search for location of an item


## Is linear search the best we can do?

- If we assume our lists are sorted... we can do a lot better
- Intuition: if I promise you a list is sorted, it's really easy to get max and min!

How?

<details>

```python
my_max = scores[-1]
my_min = scores[0]
```

</details>

