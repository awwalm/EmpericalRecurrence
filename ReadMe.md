# Combining The Tree Method and Master Theorem with Empirical Asymptotic Analysis

For this problem, we let ![T(n)] be a recurrence relation in the form:

**\[1\]:**<br>
[![Eq.1: _image of basic recurrence_][1]][1]

Our actual recurrence is given as:

**\[2\]:**<br>
[![Eq.2: _main recurrence_][2]][2]

<img src="https://latex.codecogs.com/svg.image?\large&space;\text{From}\;[1]:a=2,b=2,c=1,d=1,f(n)=\log(n)" title="\text{From}\;[1]:a=2,b=2,c=1,d=1,f(n)=\log(n)" />

Note that ![f(n)] is not a constant as it depends on ![n], so we cannot condense it into a negligible ![O(1)] component of our recurrence (more on this later). This takes us to our first solution combining the tree method with the concepts of Master Theorem.

## Hybrid Tree/Empirical Visualization Method

Let the following represent the recursive tree for ![T(n)] from **\[2\]**:

**Fig.1:**

[![Fig.1: recurrence tree][3]][3]

We can observe that the operations being done at the leaves are the costliest. This observation allows us to determine the bounds with respect due to Master's Theorem in two ways.

**The first** is to add up all calls which is simply equivalent to ![n*O(1)] calls, thus ![n] or simply ![O(n)]. We then add this to the summation of all costs per level, giving us:

**\[3\]:**<br>
[![_summation of costs per level_][4]][4]

**The second option** is to simply solve for the problems at the leaves alone, but I'll only be covering the more general first approach here.
For simplicity, we refer to the summation component as ![omega(n)] (you'll see why that notation is used).

**\[4\]:**<br>
[![Eq.4: _isolated summation function_][5]][5]

The evaluation/expansion of this summation is quite tricky but other answers have provided that. However, a simpler approach is to empirically verify the relationship between; and growth of the summation and input size. The following is a graph for the results of 1 million n-values/data points at intervals of 1000 (with each iteration being the square of itself), in the range of 1\*10<sup>3</sup> to 1\*10<sup>9</sup>, meaning that the first and last n-values are (1\*10<sup>3</sup>)<sup>2</sup> and (1\*10<sup>9</sup>)<sup>2</sup> respectively.

**Fig.2:**
[![Fig.2: _growth rate of T(n)_][6]][6]

We can see line ![omega(n)] assume a _consistently inconsistent_ oscillating shape, as it zig-zags above and beneath ![n], thus cementing its status as an **oscillation function**<sup>[\[1\]][7]</sup>, hence, the notation<sup>[\[2\]][8]</sup>.

Due to the oscillating nature, the peaks in ![omega(n)] which periodically overtake ![n] means we can't simply say ![T(n)] is ![O(n)] as it's not always true as we've seen above. Notwithstanding, the **absolute difference** (represented by the orange line), which we will denote as ![rnd], between ![n] and ![omega(n)] is relatively negligible as a consequence of never exceeding ![n] nor subceeding ![omega(n)]; this allows us to take ![O(n)] as a **_consistent bound_** on the performance of the recurrence, therefore:

**\[5\]:**<span>&nbsp;&nbsp;&nbsp;&nbsp;</span>[![conclusion 1][9]][9]

**Q.E.D.**

## Substitution Method

This is quite straightforward, we simply expand and recursively substituting a portion of the recurrence into itself until we have malleable generalized terms and then obtain the bounds from the k<sup>th</sup> term.

[![Eq6: _growth rate of T(n)_][10]][10]

<img src="https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq7.svg"/>

## Master Theorem



  [T(n)]: https://latex.codecogs.com/svg.image?T(n)
  [f(n)]: https://latex.codecogs.com/svg.image?f(n)
  [n]: https://latex.codecogs.com/svg.image?n
  [O(1)]: https://latex.codecogs.com/svg.image?O(1)
  [n*O(1)]: https://latex.codecogs.com/svg.image?n\times&space;O(1)
  [O(n)]: https://latex.codecogs.com/svg.image?O(n)
  [omega(n)]: https://latex.codecogs.com/svg.image?\large&space;\dpi{100}\omega(n)
  [rnd]: https://latex.codecogs.com/svg.image?\large&space;\dpi{100}\Delta_{\omega(n)}

  
[1]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq1.svg
  [2]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq2.svg
  [3]: https://github.com/awwalm/EmpericalRecurrence/raw/master/Images/tree.bmp
  [4]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq3.svg
  [5]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq4.svg
  [6]: https://i.sstatic.net/66TT8VBM.png
  [7]: https://en.wikipedia.org/wiki/Oscillation_(mathematics)
  [8]: https://en.wikipedia.org/wiki/Angular_frequency
  [9]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq5.svg
[10]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq6.svg
