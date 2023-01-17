Create sum formula of polinomial functions
=========================================

This algorithm help compute the sum formula of known function. 

# Usage
## Check algorithm work

    python .\sumfor.py -h
    
Output:

    usage: sumfor.py [-h] [-f FORMULA] [-v] [-s START] [-t STEP]

    optional arguments:
      -h, --help            show this help message and exit
      -f FORMULA, --formula FORMULA
                            Sum formula of function
      -v, --version         show version
      -s START, --start START
                            Start point (default = 1)
      -t STEP, --step STEP  Step (default = 1)

To use the algorithm, use the following syntax:
    
    python .\sumfor.py -f <formula input> -s <start point> -t <step>

##  Example
### Example 1
For example, we have to compute the sum formula of the $x^3-2x^2+1$ function from $1$, mean $\sum\limits_{i = 1}^x {({x^3} - {2x^2} + 1)}$.

Running algorithm by the following syntax to find the sum formula.

    python .\sumfor.py -f x^3-2x^2+1

Result:

    +2/3*x^1-3/4*x^2-1/6*x^3+1/4*x^4

So the sum formula of $x^3-x^2+1$ from $1$ is $\frac{2}{3}x - \frac{3}{4}{x^2} - \frac{1}{6}{x^3} + \frac{1}{4}{x^4}$. 

It means:
$$\sum\limits_{i = 1}^x {{x^3} - {2x^2} + 1} = \frac{2}{3}x - \frac{3}{4}{x^2} - \frac{1}{6}{x^3} + \frac{1}{4}{x^4}$$

### Example 2
If we need to compute the sum formula of the $x^2-1$ from $-1$, mean $\sum\limits_{i = -1}^x {({x^2} - 1)}$.

Similarly, we execute the following syntax:

       python .\sumfor.py -f x^2-1 -s -1
       
Output:
        
        3x^0-5/6*x^1+1/2*x^2+1/3*x^3

Mean:

$$\sum\limits_{i = -1}^x {({x^2} - 1)} = 3 - \frac{5}{6}x + \frac{1}{2}{x^2} + \frac{1}{3}{x^3}$$

### Example 3


# Algorithm mechanism

## The basis
Base on the [Triagle matrix of polinomial sum](https://github.com/Truongphi20/Forposum) was created before. Apply a simple rule about the formula for the sum of sum functions:

$$
\sum {\left( {{k_0} + {k_1}{x^1} + \ldots + {k_n}{x^n}} \right)}  = {k_0}\sum {{x^0}}  + {k_1}\sum {{x^1}} + \ldots + {k_n}\sum {{x^n}}
$$

   - With $k_0,k_1,\ldots,k_n$ are the coefficients of the corresponding exponent. 

   - $\sum {{x^0}},\sum {{x^1}},\ldots,\sum {{x^n}}$ can be computed easily in matrix the Triagle matrix.

## Order of algorithm execution

- Processing input data
- Determine the largest power exponent
- Multiply coefficients by the corresponding sum formula 
- Add the sum formulas together

## Introduction to the Hit Sum Function
