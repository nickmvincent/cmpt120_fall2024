---
theme: seriph
background: images/kseniia-rastvorova-U2AwijfUNS4-unsplash.jpg
title: Week 11
info: |
  Slides for Week 11 of CMPT 120, Fall 2024, Section D300, Nicholas Vincent
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true
---

# Welcome to Week 11

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space to start <carbon:arrow-right class="inline"/>
  </span>
  <span> Photo by <a href="https://unsplash.com/@hixenia?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Kseniia Rastvorova</a> on <a href="https://unsplash.com/photos/trees-near-mountain-U2AwijfUNS4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  </span>
</div>

---

DRAFT

---

## Recursion

Recursion: functions that call themselves

---

Fractals?




---

## What is a recursive function?

A concise, elegant way to code a complex algorithm, without needing loops.

You need a function with...
- a base (terminating) case
- some branch in the function where it "calls itself" and moves towards the base case

---

## Recursive Vortex

---

Three parts

1. Function definition

`def my_recursive_func(...)`

2. base case that returns

```python
if n == 1:
    return 1
```

3. branch that "moves toward base case"

```python
else:
    print(n)
    my_recursive_func(n-1)
```

# put full func here

---

Any guesses:

What happens if we call the recursive function moving AWAY from the base case?

---


