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
    
The form of the input formula is a dictionary string with keys being the exponent and the values being the coefficient of that exponent. Example input form of $x^3-\frac{2}{3}x^2+1$ is `'{0:1,2:-2/3,3:1}'` (dictionary's keys order isn't matter).

##  Example
### Example 1
For example, we have to compute the sum formula of the $x^3-2x^2+1$ function from $1$, mean $\sum\limits_{x = 1}^x {({x^3} - {2x^2} + 1)}$.

Running algorithm by the following syntax to find the sum formula.

    python .\sumfor.py -f '{3:1,2:-2,0:1}'

Result:

    +2/3*x^1-3/4*x^2-1/6*x^3+1/4*x^4

So the sum formula of $x^3-x^2+1$ from $1$ is $\frac{2}{3}x - \frac{3}{4}{x^2} - \frac{1}{6}{x^3} + \frac{1}{4}{x^4}$. 

It means:
$$\sum\limits_{x = 1}^x {({x^3} - {2x^2} + 1)} = \frac{2}{3}x - \frac{3}{4}{x^2} - \frac{1}{6}{x^3} + \frac{1}{4}{x^4}$$

### Example 2
If we need to compute the sum formula of the $x^2+1$ from $-1$, mean $\sum\limits_{x = -1}^x {({x^2} + 1)}$.

Similarly, we execute the following syntax:

       python .\sumfor.py -f '{2:1,0:1}' -s -1
       
Output:
        
        3*x^0+7/6*x^1+1/2*x^2+1/3*x^3

Mean:

$$\sum\limits_{x = -1}^x {({x^2} + 1)} = 3 + \frac{7}{6}x + \frac{1}{2}{x^2} + \frac{1}{3}{x^3}$$


### Example 3
Were we have to find a [Hit Sum Function](#introduction-to-the-hit-sum-function) following:

$$\left. {{S_2}} \right|_{ - 1}^x\left( {{x^3} - 2{x^2} + 1} \right)$$

It means calculating the sum of formula  $x^3 - 2x^2 + 1$ from $-1$ to $x$, the step equals 2. We execute the following command:

    python .\sumfor.py -f '{3:1,2:-2,0:1}' -s -1 -t 2

Output:

    -13/8*x^0-1/6*x^1-1/2*x^2+1/6*x^3+1/8*x^4
    
That mean:

$$\left. {{S_2}} \right|_{_{ - 1}}^x\left( {{x^3} - 2{x^2} + 1} \right) = \frac{{ - 13}}{8} - \frac{1}{6}{x^1} - \frac{1}{2}{x^2} + \frac{1}{6}{x^3} + \frac{1}{8}{x^4}$$

# Algorithm mechanism

## The basic
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

The Hit Sum Function is just the generality form of the Sigma Sum Function with the additional element is the step.

$$\left. {{S_n}} \right|_a^bf\left( x \right) = f(a) + f(a + n) + f(a + 2n) +  \ldots  + f(b)$$

With the step equal to 1, Hit Sum Function is Sigma Sum.

$$\left. {{S_1}} \right|_a^bf\left( x \right) = \sum\limits_{x = a}^b {f(x)}$$

To calculate the Hit Sum Function, it is necessary to use the step conversion rule of the Hit Sum Function to convert it to a Sigma Sum Function.

The step conversion rule is:

<font size = 10>
    
$$\left. {{S_n}} \right|_a^bf(x) = \left. {{S_m}} \right|_{_{a.\frac{m}{n}}}^{^{b.\frac{m}{n}}}f(x.\frac{n}{m})$$
    
</font>

Therefore,

$$\left. {{S_n}} \right|_a^bf(x) = \sum\limits_{_{\frac{a}{n}}}^{\frac{x}{n}} {f(n.x)}$$

From here we can calculate the rule as mentioned in the [basic section](#the-basic) and then change the variable $x$ to $\frac{x}{n}$

# Application

- [Formal Regression](https://github.com/Truongphi20/FormalRegression): from the value points, regression to the polynomial function that generates those values
