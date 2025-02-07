# Extra Credit: Python Decorators

### 1. What is a higher-order function and how is it different from a functor?

- ***Higher-Order Function***:
A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. Examples in Python include `map`, `filter`, and decorators.

- ***Functor***:
A functor is an object in programming (commonly in object-oriented languages) that can be called as if it were a function, typically implemented using the `__call__` method in Python.

- ***Difference***:
A higher-order function works directly with functions, while a functor is an object that behaves like a function but also encapsulates state or behavior.


### 2. What are first-class objects? What is the significance of functions being first-class objects?

- ***Definition***:
In Python, first-class objects are entities that can be passed as arguments, returned from functions, assigned to variables, and stored in data structures. Functions in Python are first-class objects.

- ***Significance***:

  - Functions can be used flexibly, enabling powerful programming patterns like decorators and closures.

  - Allows for functional programming paradigms within Python, increasing code modularity and reusability.

### 3. What are inner functions? Why is the major benefit of inner functions and why is it important for decorators?

- ***Definition***:
An inner function is a function defined within another function.

- ***Benefits***:

  - Encapsulation: Inner functions can access variables from the enclosing function, enabling localized logic without exposing it globally.

  - Closures: They can capture and carry data from their enclosing scope.

- ***Importance for Decorators***:

  - Decorators use inner functions to wrap additional behavior around the original function without modifying it.

### 4. Discuss the benefits and drawbacks of using decorators in Python.

- ***Benefits***:

  - Clean and concise way to extend functionality without altering the original function.

  - Promotes reusable and modular code.

  - Useful for cross-cutting concerns like logging, authentication, and timing.

- ***Drawbacks***:

  - Can obscure the logic of the wrapped function if overused.

  - Harder to debug since the stack trace involves the decorator.

### 5. Why @ symbol is called syntactic sugar? What's the biggest advantage of using it when decorators are used?

- ***Syntactic Sugar***:
The `@` symbol is a shorthand for applying a decorator to a function. For example:

```
@decorator
def func():
    pass
```
is equivalent to:

```
def func():
    pass
func = decorator(func)
```

- ***Advantage***:

  - Enhances readability and reduces boilerplate code.

  - Clearly indicates the function is being decorated, making the code easier to understand.

### 6. How would it help Python's weak encapsulation of Class?

- ***Encapsulation in Python***:
Python relies on naming conventions for encapsulation (e.g., `_private` and `__mangled` names) rather than strict access modifiers.

- ***Role of Decorators***:

  - `@property`: Converts methods into attributes, providing controlled access to class attributes.

  - Enables validation and computation within getter and setter methods while maintaining a clean interface.

### Summary

The use of decorators demonstrates Python's functional programming capabilities and enhances modularity and reusability of code. Through this exercise, the understanding of decorators and their application in real-world scenarios, such as timing functions or managing access in classes, is solidified

# Code Output

### Attemtpt 1:

```
Enter a number for the list of prime numbers: 33

'Start': 5.99280, 'End': 5.99291, 'Time Efficiency': 0.00011
List of prime numbers up to 33: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
```

### Attempt 2:

```
Enter a number for the list of prime numbers: 101

'Start': 1.40164, 'End': 1.40176, 'Time Efficiency': 0.00012
List of prime numbers up to 101: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
```