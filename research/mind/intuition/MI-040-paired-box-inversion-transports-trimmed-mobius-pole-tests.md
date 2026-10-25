# MI-040 — Paired-box inversion transports trimmed Möbius pole tests

**Evidence level:** supported conditional cross-line deduction from
[PL-475](../../prime_lattice/findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md),
[MC-528](../../mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md), and
[MC-531](../../mobius_cancellation/findings/MC-531-bounded-jumps-recover-trimmed-mobius-variance.md).
The local mechanisms are retained in [Prime Lattice MI-067](../../prime_lattice/mind/intuition/MI-067-two-box-lengths-recover-smooth-pole-tests-at-macroscopic-scale.md)
and [Möbius MI-103](../../mobius_cancellation/mind/intuition/MI-103-bounded-jumps-price-deleted-starts-in-pole-tests.md).
This composition is Mind synthesis, not a separately reviewed finding,
an arithmetic upper estimate, formal verification or a novelty claim.

The transferable object is a fixed **smooth mean-zero test**, not the
prime logarithmic derivative or its residue weights. Conditional on a
zeta zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\), of multiplicity
\(m\), MC-528 supplies
\[
T_\phi(X)=\sum_n\mu(n)\phi(n/X)
=X^{\rho_0}Q_{m-1}(\log X)+O(X^{\sigma_1}),
\quad 1/2<\sigma_1<\beta,
\]
with nonzero leading coefficient of \(Q_{m-1}\). Its input Gevrey bump
may be chosen inside \((\log(4/3),\log(5/3))\); the convergent
derivative series preserves support. Thus
\(\phi\in C_c^\infty((4/3,5/3))\) and \(\int\phi=0\), exactly
the input class of PL-475's source-independent inverse.

Write \(A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv\). For sufficiently large
integers \(X\) and integer \(1\le H\le X/20\), put
\(K=\lfloor\sqrt2H\rfloor\), \(L_1=H\), \(L_2=K\). The two uniformly
bounded, mean-zero tests satisfy
\[
A_{H/X}f_1+A_{K/X}f_2=\phi+R_X,
\qquad \|R_X\|_\infty=O(X^{-1}),
\]
with the tests supported in one compact subset of \((1,2)\) and the
residual in a fixed compact set. Since \(|\mu(n)|\le1\),
the coefficient sum of this rounding error is \(O(1)\), rather than
the prime source's \(O(\log X)\). Hence, for arbitrary constants
\(c_1,c_2\), the sum of the complete pairings
\[
P_i=L_i^{-1}\int_X^{2X}\{M(y+L_i)-M(y)-c_i\}f_i(y/X)\,dy,
\qquad i=1,2,
\]
has modulus \(\gg X^\beta(\log X)^{m-1}\). When \(H=K\), these
are still two tests; their data may coincide and no independence is used.

Choose separate masks \(E_i\subset I_X=\{X,\ldots,2X-1\}\),
\(B_i=|E_i|<X/2\), and let
\[
V_i=\sum_{j\in I_X\setminus E_i}
|M(j+L_i)-M(j)-c_i|^2.
\]
The integer-window jump bound and MC-531's reconstruction lemma give
\(|P_i|\ll(\sqrt{XV_i}+B_i^2)/L_i\). The triangle inequality therefore
transfers the pole certificate to
\[
\boxed{
\frac{\sqrt{XV_1}+B_1^2}{H}
+\frac{\sqrt{XV_2}+B_2^2}{K}
\gg X^\beta(\log X)^{m-1}.}
\tag{*}
\]
All constants are independent of \(X,H\), masks and centers once the
selected zero and full zero set are fixed. The two repairs act on
different losses: two kernels recover the smooth target through the box
zeros; bounded jumps recover the complete pairing from omitted starts.
No cut test, incomplete contour or equality of the two centers is used.

At \(H=\lfloor X/20\rfloor\), suppose both channels on one unbounded
set of integer scales obey, for every \(\varepsilon>0\),
\[
B_i\ll_\varepsilon X^{3/4+\varepsilon},\qquad
V_i\ll_\varepsilon X^{1+\varepsilon}L_i,\qquad i=1,2.
\]
The scale set, masks and centers are fixed before the epsilon
quantifier. The left side of (*) is
\(O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2+2\varepsilon})\),
contradicting any \(\beta>1/2\) when \(2\varepsilon<\beta-1/2\).
Thus those **unproved joint estimates** would imply RH. This costs a
second length but removes the single-box logarithmic restriction from
the trimmed criterion. With empty masks, direct-sum Cauchy–Schwarz also
gives \(V_1/H^2+V_2/K^2\gg X^{2\beta-1}(\log X)^{2m-2}\).

The transfer uses the reciprocal-zeta test with its full Laurent term;
it does not identify reciprocal residues with same-sign prime residues.
The inverse alone has no arithmetic selectivity. A lone small variance,
a qualitative exceptional density, or a start-dependent fitted center
does not supply (*). The bounded-jump tent control establishes only the
generic absolute-mass cost, not optimality of the Möbius deletion budget.
Full-zero-set dependence and non-effective onset remain unchanged.
