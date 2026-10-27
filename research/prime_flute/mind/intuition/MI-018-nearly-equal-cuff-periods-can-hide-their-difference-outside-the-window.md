# MI-018 — Concentration of each cuff trace does not control their difference

**Evidence level:** supported by the scalar estimates and explicit
composite-label construction in
[PF-368](../../findings/PF-368-fixed-single-cuff-bands-concentrate-in-actual-windows-in-density.md)
and [PF-369](../../findings/PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows.md).
Prime realization and actual pant-energy consequences are open.

Let `H[f]=int_R |f(t)|^2 sech(t)dt`. A trace on one exact period-`L`
Fourier lattice with fixed frequency span `W` satisfies

\[
\frac{H_{|t|>T}[f]}{H[f]}
\le\frac{4N^2}{\pi}e^{c(W)L-T},\qquad
c(W)=\frac4{\pi^2}\int_0^{\pi W/4}\log\coth u\,du<\frac12,
\quad N\le\lfloor WL/(2\pi)\rfloor+1.
\]

Thus `T/L->1/2` concentrates each fixed-band trace uniformly in its
coefficients. Two distinct periods can violate the corresponding bound
for their **difference**, even when they are exponentially close.

Fix `alpha>1/log(16)`, `n=ceil(alpha L)`, and
`L'=L+delta_L`, where `0<|delta_L|=o(L^2 e^(-L/2))`. PF-369 supplies
exact-lattice traces `f_L,f_(L')`, each on indices `n,...,3n`, whose
difference `g_L` obeys

\[
\frac{\int_{-L/2}^{L/2}|g_L(t)|^2\operatorname{sech}t\,dt}{H[g_L]}
\le C_\alpha\left(\frac{e^L}{n^2 16^n}
+\frac{\delta_L^2e^L}{L^4}\right)\longrightarrow0.
\]

The mechanism retains the small denominator. Set
`q(t)=cos^(2n)(pi t/L)` and take the Fourier partial sum `P_n` of the
periodic extension of `tq(t)` on `[-L/2,L/2]`. The exact discarded tail
gives `||tq-P_n||_infinity<=L/(2pi n4^n)` there. Modulate:
`Q=e^(4pi int/L)q=sum_(j=n)^(3n)c_j e^(2pi ijt/L)`,
`c_j=4^(-n) binom(2n,j-n)`, and `A=e^(4pi int/L)P_n`.
Then `R=tQ-A` is tiny centrally, but `R(L+s)=LQ(s)+R(s)` is of size `L`
for `|s|<=1`.

With `d_j=2pi j(1/L'-1/L)`, replace `tQ` by genuine divided differences:

\[
g_L(t)=\sum_{j=n}^{3n}\frac{c_j}{id_j}
\left(e^{2\pi ijt/L'}-e^{2\pi ijt/L}\right)-A(t),\qquad
|g_L-R|\le C_\alpha |\delta_L|t^2/L.
\]

The escaping-mass lower bound is `H[g_L]>=cL^2 e^(-L)`, so the error must
be compared with that scale; fixed-`L` divided-difference convergence would
not suffice. In this normalization individual coefficient absolute sums
can grow as `L/|delta_L|`. Scaling both traces leaves the mass ratio and
their relative energy costs unchanged. At `delta_L=0` this construction is unavailable and the
two lattices collapse to one: uniformity is singular at equal periods.

The exact cotangent flute from composite labels `6m+3`, `m>=1`, has
neighboring cuff periods satisfying
`delta_L=(8+o(1))e^(-L/2)>0`. Its prescribed corridor window has
`L/2-T=1+log(2/vartheta)+o(1)>0`, for the fixed small geometric
`vartheta>0`. With `alpha=1/2`, the central fraction is `O(L^(-4))`.
Each trace concentrates in this actual window while their difference
escapes it. A real or imaginary component gives the same obstruction
with real zero-mean traces.

Separate concentration estimates bound residual tails by
`H[f_L]+H[f_(L')]`, which may dwarf `H[f_(L')-f_L]`. They cannot supply
a broad-band scalar window/full-norm comparison from period agreement
and cotangent geometry alone. The construction does not price tangential,
mass or seam energy, identify an actual minimizing residual, contradict
the sufficiently narrow combined-band result, or establish such a prime
subsequence. It proves no compactness or shorted-angle obstruction for
the completed pant operator.
