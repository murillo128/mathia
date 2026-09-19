# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Require finite-prefix identifiability before pricing joint pole recovery

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class` and the current shell-carrier/derivative-depth intuitions.

AF-416--AF-435 separate left-tail scaling, source selection and downstream transport. AF-436 shows that the exact Euler moments `s_k=zeta(2k)` retain the full reciprocal-square shell ladder, while AF-437 shows that sequential shell peeling is exponentially ill-conditioned.

AF-438 removes that particular representation artifact. The exact generating transform

`F(z)=sum_(k>=1) zeta(2k) z^(k-1)=sum_(m>=1) 1/(m^2-z)`

is a Stieltjes/Markov carrier whose poles expose all shells simultaneously with residue `-1`. Exact shell provenance is therefore present without recursive subtraction.

AF-439 moves the finite-data frontier one step earlier than conditioning. For every fixed moment depth `N`, even inside a nearby positive finite Stieltjes class with the same unit-residue normalization, there are local pole-moving fibres with exactly the same first `N` moments. The construction perturbs the constant elementary-symmetric coefficient of `N+1` positive nodes; Newton identities keep the first `N` power sums fixed while every pole moves. The perturbed nodes need not remain reciprocal integer squares, so this is a generalized-shell identifiability obstruction, not a second Riemann source.

AF-440 shows that this obstruction disappears sharply once the support and mark alphabet are source-rigid. For coefficients `a_m` in a finite separated alphabet on the exact reciprocal-square support, equality of the single depth-`N` moment already forces agreement through every index `m` satisfying `D m <= delta(2N-1)`, where `delta` is the alphabet separation and `D` its diameter. In the binary case this gives exact agreement through `m<=2N-1`. The same proof gives an explicit separation margin between competing prefixes, so the finite-prefix question now has a positive identifiability theorem as well as a negative moving-support theorem.

The live question is therefore no longer whether finite moments can ever identify remote shell data. It is to locate the boundary between AF-439 and AF-440: how much support uncertainty, residue freedom or tail flexibility can be admitted before the discrete dominance margin disappears, and how fast the surviving margin decays at the shell depth actually consumed downstream. Only after that gate is passed does it make sense to compare Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse by condition number.

## Keep source class, exact carrier, identifiability, conditioning and destination transport separate

Exact analytic continuation from the complete moment sequence is not finite-prefix recovery. Likewise, removing the artificial AF-437 peeling cascade does not prove that the remaining inverse is stable. AF-439 and AF-440 together make the source-class dependence explicit: nearby movable positive nodes remain nonidentified at every fixed depth, while exact reciprocal-square support with separated discrete marks has a linear-depth finite-prefix fidelity law.

A continuation should therefore state the admissible completion class explicitly, prove or refute target-purity of the finite observation fibre on that class, and then price the inverse at the precision and shell depth consumed downstream. The high-value boundary questions are now quantitative and structural: controlled support jitter, nonbinary separated residue alphabets, interval-valued marks, and tail classes that interpolate between the rigid reciprocal-square model and the movable Stieltjes fibre. Treating either AF-439 or AF-440 as universal would erase the source assumption doing the mathematical work.