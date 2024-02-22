# DSA.py - LeetCode Solutions

This repository contains my solutions to various competitive programming problems and LeetCode challenges, all implemented in pure Python, SQL or Pandas (Depends on the category)

> [!IMPORTANT]
> The naming of the variables and functions may not follow a good standard.
> I named them as I consider more comfortable to solve the problems

## LeetCode

This section includes my solutions to LeetCode problems. For each problem, I strive to provide not only the solution but also an the result of its efficiency and complexity.

## Folder Structure

The repository is structured as follows:

```plaintext
.
├── <category>
│   ├── Easy
│   │   ├── NameOfTheProblemWithoutNumber_A.py
│   │   ├── NameOfTheProblemWithoutNumber_B.py
│   │   ├── ...
│   ├── Medium
│   │   ├── NameOfTheProblemWithoutNumber_A.py
│   │   ├── NameOfTheProblemWithoutNumber_B.py
│   │   ├── ...
│   ├── Hard
│   │   ├── NameOfTheProblemWithoutNumber_A.py
│   │   ├── NameOfTheProblemWithoutNumber_B.py
│   │   ├── ...
```

The `category` folder contains subfolders for each difficulty level. Each subfolder contains the solutions to the problems of that difficulty level.
In this repo you will find the following categories:

-   Algorithms
-   Database
-   Pandas

## How the solutions are shown

Each solution is implemented in a single file, named after the problem's name. The file contains the solution and a brief explanation of the problem and the solution.

As an example, the solution to the trivial problem `Convert the Temperature` is implemented in the file `Convert the Temperature` it is located in the `algorithms` folder, inside the `Easy` subfolder. The file contains the following code:

```python
# 2469. Convert the Temperature
'''
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
Return the array ans. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    # 26ms Beats 98.65%
    # 17.32MB Beats 14.24%
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
```

All the solutions are implemented in the same way.
