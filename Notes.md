# Obtaining Empirically Verified Solutions by Tree Method and Backwards Substitution

For this problem, we let ![18] be a recurrence relation in the form:

**\[1\]:**

[![Eq.1: _image of basic recurrence_][1]][1]

Our actual recurrence is given as:

**\[2\]:**

[![Eq.2: _main recurrence_][2]][2]

![eq 2.1] 

Note that ![19] is not a constant as it depends on ![20], so we cannot condense it into a negligible ![21] component of our recurrence (more on this later). This takes us to our first solution combining the tree method with the concepts of empirical analysis to derive an asymptotic bound.

## Tree Method + Empirical Verification

Let the following represent the recursive tree for ![18] from **\[2\]**:

**Fig.1:**

[![Fig.1: recurrence tree][3]][3]

We can observe that the operations being done at the leaves are the costliest. This observation allows us to determine the bounds in two ways.

**The first** is to add up cost of all calls which is simply equivalent to ![22] calls, thus ![20] or simply ![23]. We then add this to the summation of all (significant) costs per level, giving us:

**\[3\]:**

[![_summation of costs per level_][4]][4]

**The second option** is to simply solve for the problems at the leaves alone, but I'll only be covering the more general first approach here.
For simplicity, we refer to the summation component as ![24] (you'll see why that notation is used).

**\[4\]:**

[![Eq.4: _isolated summation function_][5]][5]

The evaluation/expansion of this summation is quite tricky but other answers have provided that. However, a simpler approach is to empirically verify the relationship between ![20] and ![24]; i.e. the input size and growth of the summation. The following is a graph for the results of 1 million n-values/data points at intervals of 1000 (with each iteration being the square of itself), in the range of 1\*10<sup>3</sup> to 1\*10<sup>9</sup>, meaning that the first and last n-values are (1\*10<sup>3</sup>)<sup>2</sup> and (1\*10<sup>9</sup>)<sup>2</sup> respectively.

**Fig.2:**
[![Fig.2: _growth rate of T(n)_][6]][6]

We can see line ![24] assume a _consistently inconsistent_ oscillating shape, as it zig-zags above and beneath ![20], thus cementing its status as an **oscillation function**<sup>[\[1\]][7]</sup>, hence, the notation<sup>[\[2\]][8]</sup>.

Due to the oscillating nature, the peaks in ![24] which periodically overtake ![20] means we can't simply say ![18] is ![23] as it's not always true as we've seen above. Notwithstanding, the **absolute difference** (represented by the orange line), which we will denote as ![rnd], between ![20] and ![24] is relatively negligible as a consequence of never exceeding ![20] asymptotically; this allows us to take ![23] as a **_consistent bound_** on the performance of the recurrence, therefore:

**\[5\]:**<span>&nbsp;&nbsp;&nbsp;&nbsp;</span>[![conclusion 1][9]][9]

**Q.E.D.**

## Backwards Substitution Method

This is quite straightforward, we simply expand by recursively substituting a portion of the recurrence into itself until we have malleable generalized terms and then obtain the bounds from the k<sup>th</sup> term<sup>[\[3\]][10][\[4\]][11]</sup>.

[![Eq6 substitution method part 1][12]][12]

[![Eq6 substitution method part 2][13]][13]

Since the remainder of ![eq k] is approximately equivalent to ![24], this means ![eq k] is simply equal to ![20] + ![24] (as we deduced in **\[3\]**, and empirically verified in **Fig.2**). Hence, bringing us to the same conclusion as in **\[5\]**:

[![conclusion 1][9]][9]

**Q.E.D.**

## Notes and Further Reading

1. Goodrich and Tamassia presented sophisticated techniques for solving recurrences in Chapter 11 of _'[Algorithm Design and Applications][14]'_.
2. Guzman & Limoanco conducted experiments on [approximating asymptotic tight bounds via empirical analysis][15]. 
3. Educator/YouTuber Abdul Bari has a [playlist][16] on a wide range of recurrence relation problems and solutions where he explains each succinctly. 
4. Source code for the visualization experiment can be found in [this GitHub repo][17].




  [1]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq1.svg
  [2]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq2.svg
  [3]: https://github.com/awwalm/EmpericalRecurrence/raw/master/Images/tree.bmp
  [4]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq3.svg
  [5]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq4.svg
  [6]: https://i.sstatic.net/66TT8VBM.png
  [7]: https://en.wikipedia.org/wiki/Oscillation_(mathematics)
  [8]: https://en.wikipedia.org/wiki/Angular_frequency
  [9]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq5.svg
  [10]: https://www.cs.colostate.edu/~cs200/Fall14/recitations/R9/RecurranceRelations.pdf
  [11]: https://cusack.hope.edu/Notes/Notes/DiscreteMath/Recurrence_examples.pdf
  [12]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq6.svg
  [13]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq7.svg
  [14]: https://www.amazon.com/Algorithm-Design-Applications-Michael-Goodrich/dp/1118335910
  [15]: https://www.jsoftware.us/vol12/308-TE023.pdf
  [16]: https://www.youtube.com/playlist?list=PLPGw-ZD97tXcoR1F6ZrjArSsv076IAo-L
  [17]: https://github.com/awwalm/EmpericalRecurrence

  [18]: https://latex.codecogs.com/svg.image?T(n)
  [19]: https://latex.codecogs.com/svg.image?f(n)
  [20]: https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;n
  [21]: https://latex.codecogs.com/svg.image?O(1)
  [22]: https://latex.codecogs.com/svg.image?n\times&space;O(1)
  [23]: https://latex.codecogs.com/svg.image?O(n)
  [24]: https://latex.codecogs.com/svg.image?\large&space;\dpi{100}\omega(n)
  [rnd]: https://latex.codecogs.com/svg.image?\large&space;\dpi{100}\Delta_{\omega(n)}
  [eq k]: https://latex.codecogs.com/svg.image?\inline&space;\large&space;[k]
  [eq 2.1]: https://raw.githubusercontent.com/awwalm/EmpericalRecurrence/master/Images/Eq2_1.svg