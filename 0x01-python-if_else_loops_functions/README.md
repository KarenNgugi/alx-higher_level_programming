# Python - if/else, loops, functions

## Learning Objectives
### General
- Why Python programming is awesome
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How is Python’s `for` different from C‘s?
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version `3.8.5`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the `pycodestyle` (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`


### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## Project Tasks
### 0. Positive anything is better than negative nothing
**Description:** This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
- The output of the program should be:
  - The number, followed by
    - if the number is greater than 0: `is positive`
    - if the number is 0: `is zero`
    - if the number is less than 0: `is negative`
  - followed by a new line

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `0-positive_or_negative.py` <br>

### 1. The last digit
**Description:** This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
  - The string `Last digit of`, followed by
  - the number, followed by
  - the string `is`, followed by the last digit of `number`, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  - followed by a new line

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `1-last_digit.py` <br>

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `2-print_alphabet.py` <br>

### 3. When I was having that alphabet soup, I never thought that it would pay off
**Description:** Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- Print all the letters except `q` and `e`
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `3-print_alphabt.py` <br>

### 4. Hexadecimal printing
**Description:** Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `4-print_hexa.py` <br>

### 5. 00...99
**Description:** Write a program that prints numbers from `0` to `99`.
- Numbers must be separated by `,`, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `5-print_comb2.py` <br>

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
**Description:** Write a program that prints all possible different combinations of two digits.
- Numbers must be separated by `,`, followed by a space
- The two digits must be different
- `01` and `10` are considered the same combination of the two digits `0` and `1`
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 `print` functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `6-print_comb3.py` <br>

### 7. islower
**Description:** Write a function that checks for lowercase character.
- Prototype: `def islower(c):`
- Returns `True` if `c` is lowercase
- Returns `False` otherwise
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `7-islower.py` <br>

### 8. To uppercase
**Description:** Write a function that prints a string in uppercase followed by a new line.
- Prototype: `def uppercase(str):`
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `8-uppercase.py` <br>

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
**Description:** Write a function that prints the last digit of a number.
- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit
- You are not allowed to import any module

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `9-print_last_digit.py` <br>

### 10. a + b
**Description:** Write a function that adds two integers and returns the result.
- Prototype: `def add(a, b):`
- Returns the value of `a + b`
- You are not allowed to import any module

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `10-add.py` <br>

### 11. a ^ b
**Description:** Write a function that computes `a` to the power of `b` and return the value.
- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`
- You are not allowed to import any module

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `11-pow.py` <br>

### 12. Fizz Buzz
**Description:** Write a function that prints the numbers from 1 to 100 separated by a space.
- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
- For numbers which are multiples of both three and five print `FizzBuzz`.
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space
- You are not allowed to import any module

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `12-fizzbuzz.py` <br>

### 13. Insert in sorted linked list
**Description:** 
**Technical interview preparation:**
- You are not allowed to google anything
- Whiteboard first

Write a function in C that inserts a number into a sorted singly linked list.
- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or `NULL` if it failed
```
carrie@ubuntu:0x01$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
```

```
carrie@ubuntu:0x01$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
```

```
carrie@ubuntu:0x01$ cat 13-main.c 
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}
```

```
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
carrie@ubuntu:0x01$  
```

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `13-insert_number.c, lists.h` <br>

### 14. Smile in the mirror (advanced task)
**Description:** Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `100-print_tebahpla.py` <br>

### 15. Remove at position (advanced task)
**Description:** Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).
- Prototype: `def remove_char_at(str, n):`
- You are not allowed to import any module

You don’t need to understand `__import__`

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `101-remove_char_at.py` <br>

### 16. ByteCode -> Python #2
**Description:** Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
[tips - ByteCode](https://docs.python.org/3.4/library/dis.html)

GitHub repository: `alx-higher_level_programming` <br>
Directory: `0x01-python-if_else_loops_functions` <br>
File: `102-magic_calculation.py` <br>
