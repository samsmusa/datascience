  1.3.6.2. Related Distributions ![](../../gifs/nvgtbr.gif)        

1. [Exploratory Data Analysis](../eda.htm)  
1.3. [EDA Techniques](eda3.htm)  
1.3.6. [Probability Distributions](eda36.htm)  
  

1.3.6.2.
--------

Related Distributions
---------------------

Probability distributions are typically defined in terms of the probability density function. However, there are a number of probability functions used in applications.

_Probability Density Function_

For a continuous function, the probability density function (pdf) is the probability that the variate has the value x. Since for continuous distributions the probability at a single point is zero, this is often expressed in terms of an integral between two points.

\\( \\int\_{a}^{b} {f(x) dx} = Pr\[a \\le X \\le b\] \\)

For a discrete distribution, the pdf is the probability that the variate takes the value x.

\\( f(x) = Pr\[X = x\] \\)

The following is the plot of the normal probability density function.

![plot of the normal probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norpdf.gif)

_Cumulative Distribution Function_

The cumulative distribution function (cdf) is the probability that the variable takes a value less than or equal to x. That is

$ F(x) = Pr\[X \\le x\] = \\alpha $

For a continuous distribution, this can be expressed mathematically as

\\( F(x) = \\int\_{-\\infty}^{x} {f(\\mu) d\\mu} \\)

For a discrete distribution, the cdf can be expressed as

\\( F(x) = \\sum\_{i=0}^{x} {f(i)} \\)

The following is the plot of the normal cumulative distribution function.

![plot of normal cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norcdf.gif)

The horizontal axis is the allowable domain for the given probability function. Since the vertical axis is a probability, it must fall between zero and one. It increases from zero to one as we go from left to right on the horizontal axis.

_Percent Point Function_

The percent point function (ppf) is the inverse of the cumulative distribution function. For this reason, the percent point function is also commonly referred to as the inverse distribution function. That is, for a distribution function we calculate the probability that the variable is less than or equal to x for a given x. For the percent point function, we start with the probability and compute the corresponding x for the cumulative distribution. Mathematically, this can be expressed as

\\( Pr\[X \\le G(\\alpha)\] = \\alpha \\)

or alternatively

\\( x = G(\\alpha) = G(F(x)) \\)

The following is the plot of the normal percent point function.

![plot of the normal percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norppf.gif)

Since the horizontal axis is a probability, it goes from zero to one. The vertical axis goes from the smallest to the largest value of the cumulative distribution function.

_Hazard Function_

The hazard function is the ratio of the probability density function to the survival function, _S_(x).

\\( h(x) = \\frac {f(x)} {S(x)} = \\frac {f(x)} {1 - F(x)} \\)

The following is the plot of the normal distribution hazard function.

![plot of the normal hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norhaz.gif)

Hazard plots are most commonly used in reliability applications. Note that [Johnson, Kotz, and Balakrishnan](../section4/eda43.htm#Johnson) refer to this as the conditional failure density function rather than the hazard function.

_Cumulative Hazard Function_

The cumulative hazard function is the integral of the hazard function.

\\( H(x) = \\int\_{-\\infty}^{x} {h(\\mu) d\\mu} \\)

This can alternatively be expressed as

\\( H(x) = -\\ln {(1 - F(x))} \\)

The following is the plot of the normal cumulative hazard function.

![plot of the normal cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norcha.gif)

Cumulative hazard plots are most commonly used in reliability applications. Note that [Johnson, Kotz, and Balakrishnan](../section4/eda43.htm#Johnson) refer to this as the hazard function rather than the cumulative hazard function.

_Survival Function_

Survival functions are most often used in reliability and related fields. The survival function is the probability that the variate takes a value greater than x.

\\( S(x) = Pr\[X > x\] = 1 - F(x) \\)

The following is the plot of the normal distribution survival function.

![plot of the normal survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norsurv.gif)

For a survival function, the y value on the graph starts at 1 and monotonically decreases to zero. The survival function should be compared to the cumulative distribution function.

_Inverse Survival Function_

Just as the percent point function is the inverse of the cumulative distribution function, the survival function also has an inverse function. The inverse survival function can be defined in terms of the percent point function.

\\( Z(\\alpha) = G(1 - \\alpha) \\)

The following is the plot of the normal distribution inverse survival function.

![plot of the normal inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/norisurv.gif)

As with the percent point function, the horizontal axis is a probability. Therefore the horizontal axis goes from 0 to 1 regardless of the particular distribution. The appearance is similar to the percent point function. However, instead of going from the smallest to the largest value on the vertical axis, it goes from the largest to the smallest value.

![](../../gifs/nvgbrbtm.gif)