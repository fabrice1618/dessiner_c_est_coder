Looks like you’re working with **Pythagorean triples**  
The drawing shows a right triangle with:

\[
a^2 + b^2 = c^2
\]
and the constraint:
\[
1 <= a < b <= 100
\]

---

### ✅ What you probably want (in Python)

Generate all integer pairs \( (a, b, c) \) that satisfy the equation.

Here’s a simple Python solution:

```python
triples = []

for a in range(1, 101):
    for b in range(a + 1, 101):
        c2 = a*a + b*b
        c = int(c2 ** 0.5)
        if c * c == c2:
            triples.append((a, b, c))

print(triples)
```

---

### 🔍 What it does
- Loops over all \( a \) and \( b \) with \( a < b <= 100 \)
- Computes \( c = \sqrt{a^2 + b^2} \)
- Checks if \( c \) is an integer
- Stores valid triples

---

### ✨ Example output (first few)
```
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
(7, 24, 25)
...
```

