# WI-018 — an off-lattice rational relaxation sharpens the collapsed MT Gram-defect ceiling to 31/46

**Status:** `EXACT-DERIVED + COMPUTATIONAL-INTERVAL + DECISIVE-NEGATIVE` for the collapsed single-profile Montgomery--Taylor Gram-defect interface of WI-015--WI-017. The witness, spectral comparison, tail estimate, and final rational inequality are exact. The finite kernel sum is enclosed by outward-rounded interval arithmetic and should be independently replayed before promotion to a stronger verification tier.

## Claim

Retain the collapsed stability interface

\[
S\ge HN+\mathcal D(M)-o(N),\qquad
H=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

with

\[
\mathcal D(M)=\operatorname{tr}\Psi(M),\qquad
\Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
\]

If a downstream argument uses only this inequality, the exact single-profile MT Gram geometry of the retained simple atoms, and scalar ordering/span/count data, then those data alone cannot force

\[
\boxed{S/N>31/46=0.6739130434782608\ldots.}
\]

This strictly lowers the best unit-lattice obstruction from WI-017, whose threshold lies between `0.6746624` and `0.674662668665667...`.

## Explicit period-46 witness

Put

\[
a=31/30,\qquad b=442/225,\qquad c=a+b=1349/450.
\]

Use the cyclic gap word

\[
\boxed{(a,b)^{15},a.}
\]

It has 31 gaps and

\[
15(a+b)+a=46.
\]

Equivalently, one period of positions is

\[
X=\{jc:0\le j\le15\}\cup\{jc+a:0\le j\le14\}\subset[0,46).
\]

Thus the retained density is exactly `r=31/46`. Multiplying positions by 450 gives the integer numerator set

\[
\{1349j:0\le j\le15\}\cup\{1349j+465:0\le j\le14\}
\]

inside a period of length `20700`, so every finite distance used below is an exact rational with denominator dividing 450.

## Pair energy upper-bounds the full spectral defect

For every `t>=0`,

\[
\Psi(t)\le(t-1)^2,
\]

because equality holds below `2` and, above `2`,

\[
(t-1)^2-(2t-3)=(t-2)^2\ge0.
\]

Therefore every finite MT Gram matrix satisfies

\[
\boxed{\mathcal D(M)\le\operatorname{tr}(M-I)^2
=\sum_{i\ne j}|M_{ij}|^2.}
\]

Unlike WI-015--WI-017, an off-lattice countermodel does not need a Gershgorin proof that the entire spectrum stays below the kink at `2`: an upper bound on `D(M)` is sufficient for self-consistency.

## Kernel and tail

For the normalized Montgomery--Taylor overlap,

\[
\boxed{
k(x)=\frac{\cos(\pi x)-A x\sin(\pi x)}{1-2\pi^2x^2},
\qquad A=\sqrt2\,\pi\cot(1/\sqrt2).}
\]

Since `tan u>u` for `u>0`, `cot(1/sqrt(2))<sqrt(2)`, hence `A<2pi<44/7<7`. With `pi>3`, for `x>=1`,

\[
|k(x)|\le\frac{8}{17x},\qquad w(x):=k(x)^2\le\frac{64}{289x^2}.
\]

Define the periodic quadratic pair-energy density

\[
d=\frac1{31}\sum_{x,y\in X}\sum_{q\in\mathbb Z}'w(|y-x+46q|).
\]

For `|q|<=20`, grouping equal distances gives 1,265 distinct rational arguments from 39,370 directed terms. Direct evaluation of the displayed kernel from the exact rational inputs with 50-decimal outward-rounded interval arithmetic gives

\[
0.0015574521201688155106194958876919250199303895529400923
<d_{20}<
0.0015574521201688155106194958876919250199303895529445347,
\]

so in particular

\[
\boxed{d_{20}<1558/10^6.}
\]

For `|q|>=21`, every distance is at least `46(|q|-1)`. Therefore

\[
\begin{aligned}
d-d_{20}
&\le2\cdot31\frac{64}{289\cdot46^2}\sum_{n\ge20}n^{-2}\\
&\le2\cdot31\frac{64}{289\cdot46^2}\left(20^{-2}+\int_{20}^{\infty}x^{-2}dx\right)\\
&=\frac{1302}{3822025}.
\end{aligned}
\]

Exact rational arithmetic then gives

\[
\frac{1558}{10^6}+\frac{1302}{3822025}<\boxed{19/10000},
\]

hence `d<19/10000`. Absolute summability makes periodic boundary losses `o(N)` on longer finite sections.

## Self-consistency

WI-016 already proved by alternating Taylor bounds

\[
H<672500704/10^9.
\]

Thus

\[
\frac{31}{46}\left(1-\frac{19}{10000}\right)
-\frac{672500704}{10^9}
=\boxed{\frac{189613}{1437500000}>0}.
\]

For `K` periods, `S_K=31K+O(1)` and the normalized span/count budget is `N_K=46K+O(1)`. The quadratic-energy bound above yields

\[
HN_K+\mathcal D(M_K)<S_K-cK+o(K)
\]

for some fixed `c>0`. Hence the explicit periodic off-lattice model satisfies the collapsed stability interface with strict room at density `31/46`.

## Interpretation and prior art

WI-017 correctly solves the **unit-lattice** subclass using the classical generalized-Wigner/most-homogeneous ground-state theorem. The present witness changes the sites themselves:

\[
1\mapsto1+1/30,\qquad 2\mapsto2-8/225.
\]

The continuous MT kernel is oscillatory, not a globally convex repulsive potential, so the lattice-gas theorem does not protect the integer configuration against this coherent phase relaxation. The useful correction is

\[
\boxed{\text{phase locking near integers is useful, but exact integer locking is not optimal.}}
\]

Direct prior art remains `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`, which uses balanced **integer** phase-locked periodic words to screen pair-energy/Bellman families. A targeted search for this off-grid relaxation, the rational witness above, and density `31/46` found no matching statement. No broad priority claim is made; the durable contribution is the explicit countermodel to Mathia's previously isolated collapsed interface.

## Boundaries and consequence

This is not asserted to be a zeta-zero configuration. A zeta-specific spacing/correlation theorem, the uncollapsed exceptional block of WI-004, genuinely independent profiles, or support greater than one can evade the obstruction. It also does not claim `31/46` is the optimal continuous countermodel.

The immediate falsification test is to replay the finite interval enclosure independently. Subject to that replay, the countermodel program must now screen against **continuous periodic configurations**, not only unit-lattice mechanical words. More importantly, a theorem materially above `31/46` cannot come from optimizing the already-collapsed single MT Gram defect alone; it must retain additional zeta-specific or multi-profile/arithmetic information.
