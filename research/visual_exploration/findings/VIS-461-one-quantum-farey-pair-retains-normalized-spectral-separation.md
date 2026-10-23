# VIS-461 — One-quantum Farey instability survives spectral normalization

## Claim and evidence status

Take exactly the reflected artificial reassemblies \(\sigma=BACRD\) and
\(\tau=DACRB\) of
[FD-333](../../farey_discrepancy/findings/FD-333-one-quantum-fixed-rank-farey-spectral-instability.md),
with \(v=3,u=4\), along primes \(p\equiv7\pmod {12}\) tending to infinity.
They have the same directed-gap inventory and six defect ranks, with
ordered index-value difference \((-1,1,0,0,1,-1)/p\).
For either its transport vector \(w^\omega\) or full discrepancy
\(D^\omega\), use the orthonormal Dirichlet sine transform
\[
\widehat w_r=\sqrt{2/N}\sum_{k=1}^{N-1}w_k\sin(\pi rk/N),
\qquad N=\sum_{q\le p}\varphi(q),
\quad \pi_p^\omega(r)=\frac{|\widehat w_r^\omega|^2}{\|w^\omega\|_2^2},
\tag{1}
\]
extending the probability by zero for \(r\ge N\).
Denote the full-discrepancy probabilities by \(\Pi_p^\omega\).

There are explicit, distinct probability laws \(q^\sigma,q^\tau\) on
positive even modes such that
\[
\pi_p^\omega\longrightarrow q^\omega,\qquad
\Pi_p^\omega\longrightarrow q^\omega
\quad\hbox{in total variation},
\tag{2}
\]
and consequently both pairwise distances converge to the same constant
\[
\boxed{\Delta_*:=\operatorname{TV}(q^\sigma,q^\tau)>0,
\qquad \Delta_*\approx0.0490847588.}
\tag{3}
\]
A fixed-mode certificate, already sufficient without the numerical value
in (3), is
\[
\boxed{q^\sigma(6)=\frac{256}{171\pi^2},\qquad
q^\tau(6)=\frac{300}{211\pi^2},\qquad
q^\sigma(6)-q^\tau(6)=\frac{2716}{36081\pi^2}>0.}
\tag{4}
\]
Thus even the binary observation “mode 6 or another mode” retains positive
limiting separation, about \(0.00762696\), for both transport and full
reassembled discrepancy. Separate energy normalization does not erase this
pair's macroscopic distinction.

**Evidence:** EXACT-DERIVED + PNT/DIRICHLET-ASSISTED-ASYMPTOTIC +
CLASSICAL-FOURIER-SPECIALIZATION + EXACT-RATIONAL-CHECKS.
This is a source-specific distinction at the spectral-probability quotient.
It asserts neither a convergence rate nor a theorem for every \(v\ge3\),
general phase retrieval, genuine Farey order, or RH.

## Exact vectors and their limiting profiles

For this specialization put \(i=(p+1)/4\), \(j=(p-1)/3\).
In the source's original order the five consecutive excursion blocks have
lengths \((a,b,h,b,a)\), where \(2a+2b+h=N-2\). Define
\[
x=\frac aN-\frac{i-1}{p},\qquad
y=\frac bN-\frac{j-i}{p},\qquad
z=\frac hN-\frac{p-2j}{p}.
\]
The complete right-endpoint transport vectors on ranks \(1,\ldots,N-1\)
are the following constant blocks:

| Length | 1 | \(b\) | \(a\) | \(h\) | \(a\) | \(b\) |
| --- | --- | --- | --- | --- | --- | --- |
| \(w^\sigma\) | 0 | \(x\) | \(-y\) | 0 | \(y\) | \(-x\) |
| \(w^\tau\) | 0 | \(x+y+z\) | \(-y\) | 0 | \(y\) | \(-x-y-z\) |

The leading singleton is necessary: finite transport is not asserted to
be exactly antisymmetric in rank. FD-333 equations (15)–(16), using its
PNT-based fixed-rational rank estimate, give
\[
\frac aN\to\frac14,\quad \frac bN\to\frac1{12},\quad
\frac N{p^2}\to c:=\frac3{\pi^2},\qquad
px\to\frac34,\quad py\to\frac7{12},\quad p(x+y+z)\to\frac23.
\tag{5}
\]
Let \(B=7/12\). For \(A\in\{3/4,2/3\}\) define the step function
\[
f_A(t)=
\begin{cases}
 A,&0<t<1/12,\\
 -B,&1/12<t<1/3,\\
 0,&1/3<t<2/3,\\
 B,&2/3<t<11/12,\\
 -A,&11/12<t<1.
\end{cases}
\tag{6}
\]
Values at the finitely many endpoints are immaterial. The step embedding
of \(p w^\sigma\) converges in \(L^2(0,1)\) to \(f_{3/4}\), and that of
\(p w^\tau\) to \(f_{2/3}\): the finitely many heights and endpoints
converge by (5). Their profile energies and finite energy limits are
\[
E_A:=\int_0^1 f_A^2=\frac{A^2}{6}+\frac{49}{288},
\quad E_{3/4}=\frac{19}{72},\quad E_{2/3}=\frac{211}{864},
\qquad \|w^\omega\|_2^2\to cE_{A_\omega}>0.
\tag{7}
\]

**Source normalization check.** With ordinary Lebesgue measure on
\((0,1)\), the isometric embedding of the *unscaled discrete difference*
has limit
\(\sqrt c\,(1/12)(\mathbf1_{(0,1/12)}-\mathbf1_{(11/12,1)})\).
Its squared norm is \(6(1/12)^3/\pi^2\), in agreement with FD-333
(8), (14), (16) and (19). The last continuum-profile sentence in that
source's §3 instead writes \(\sqrt6\,d/\pi\), which would give twice its
stated energy under the standard \(L^2(0,1)\) convention. Equations
(5)–(7) fix the normalization explicitly; the source's finite formulas
and coefficient/energy limits, rather than that sentence, are used here.

## Normalized sine laws and a fixed witness

Antisymmetry of (6) kills odd sine coefficients. For positive even \(r\),
put
\[
H_A(r)=A-(A+B)\cos(\pi r/12)+B\cos(\pi r/3).
\]
Integration on the first two intervals and reflection give
\[
\int_0^1 f_A(t)\sin(\pi rt)\,dt=\frac{2H_A(r)}{\pi r}.
\]
The fixed-mode Riemann-sum limit in (1) is
\(\widehat w_r\to\sqrt{2c}\int f_A\sin(\pi rt)\).
Dividing its squared modulus by (7) yields
\[
q_A(r)=
\begin{cases}
\displaystyle\frac{8H_A(r)^2}{\pi^2 r^2E_A},&r\text{ even},\\
0,&r\text{ odd}.
\end{cases}
\tag{8}
\]
Continuous sine Parseval gives \(\sum_{r\ge1}q_A(r)=1\).
At \(r=6\), \(H_A(6)=A+B\); substitution proves (4).
This tests the squared, individually normalized coefficients directly.
Unequal raw energy or noncollinear profiles alone would not suffice.

For an exact expression for (3), define for \(j=1,\ldots,6\)
\[
F_j=\frac{H_{3/4}(2j)^2}{E_{3/4}}
       -\frac{H_{2/3}(2j)^2}{E_{2/3}}.
\]
The sequence \(F_j\), extended to all integer \(j\), is 12-periodic,
with \(F_{12-j}=F_j\) and \(F_{12}=0\). Grouping the absolutely
convergent series in (8) therefore gives
\[
\Delta_*=
\sum_{j=1}^{5}\frac{|F_j|}{144\sin^2(\pi j/12)}
+\frac{|F_6|}{288}.
\tag{9}
\]
Here \(\sum_{k\in\mathbb Z}(j+12k)^{-2}
=\pi^2/[144\sin^2(\pi j/12)]\); the self-paired residue 6 contributes
half its two-sided sum. Thus the displayed decimal is an evaluation of a
finite exact expression, not a fitted infinite-frequency truncation.

## Tail control and full-discrepancy transfer

For each nonzero finite block, the geometric-sum bound gives
\[
\left|\sum_{k=L}^{R}\sin(\pi rk/N)\right|
\le\frac1{\sin(\pi r/(2N))}\le\frac Nr,
\qquad 1\le r<N.
\]
There are a fixed number of blocks, their heights are \(O(p^{-1})\),
and \(\sqrt N/p\) is bounded. Hence, uniformly for large allowed primes,
\[
|\widehat w_r^\omega|\le C/r,\qquad
\pi_p^\omega(r)\le C'/r^2.
\tag{10}
\]
The energy floor in (7) justifies the second bound. A fixed finite set of
coefficients converges by the Riemann-sum calculation, and the sum outside
\(r\le R\) is \(O(1/R)\), uniformly in \(p\). This proves
\(\ell^1\), hence total-variation, convergence in (2); no escaping
high-frequency mass is being ignored. The triangle inequality then gives
convergence of the pairwise distances to (9).

FD-333 supplies the exact decomposition
\(D^\omega=P_\omega D+w^\omega\), with
\(\|P_\omega D\|_2=\|D\|_2=o(1)\). For nonzero real vectors \(s,t\)
and any common orthogonal transform \(U\),
\[
\operatorname{TV}\!\left(
\frac{|Us|^2}{\|s\|^2},\frac{|Ut|^2}{\|t\|^2}\right)
\le\left\|\frac{s}{\|s\|}-\frac{t}{\|t\|}\right\|_2
\le\frac{2\|s-t\|_2}{\|t\|_2}.
\tag{11}
\]
The first inequality is Cauchy–Schwarz applied to difference times sum;
the second is the reverse triangle inequality for the norms. Apply (11)
with \(s=D^\omega,t=w^\omega\), using (7). Each full spectrum differs
from its transport spectrum by \(o(1)\), proving the second part of (2)
and transfer of (3)–(4). The source gives no quantified residual adequate
to assert a prime-asymptotic convergence rate. Full-discrepancy odd modes
vanish exactly by reflection; transport odd mass need only tend to zero.

## Falsification checks and visual consequence

An independent Farey recurrence generated the actual rational vertices and
directed denominator-edge gaps for \(p=19,31,43\). Reassembling those gaps
and summing them with exact fractions verified endpoints, the complete
transport table coordinate by coordinate, all six common defect ranks,
and the index-numerator difference \((-1,1,0,0,1,-1)\).
A direct sine matrix and the orthonormal type-I DST agreed within
\(4\cdot10^{-15}\) per coefficient on those cases.

Complete spectra, without a high-mode cutoff, were also checked at
\(p=67,103,211,499,1039,2503\), using the exact Farey vertices and
permutation formula to avoid cumulative floating gap-sum error. Across
all nine primes, probability mass errors were below \(10^{-13}\).
Replacing a transport by \(-3\) times itself changed its normalized
spectrum by less than \(3\cdot10^{-14}\) per mode, confirming the scalar
amplitude/sign control.

At \(p=19,103,2503\), transport distances were respectively about
\(0.0494819,0.0471340,0.0478382\); full-discrepancy distances were
\(0.0046610,0.0477659,0.0475740\). The signed transport mode-6 difference
is negative at 19 and 31 but about \(0.0074172\) at 2503. These finite
checks test bookkeeping and implementation, not an asymptotic rate or
monotonicity. The
[paired visualization](../visualizations/one-quantum-normalized-spectral-separation.md)
shows the unit-energy profiles, limiting powers and signed residual, and
both finite-prime distances.

## Prior art and boundary

Sine orthogonality, Parseval, geometric-sum/BV tails, and continuity of
normalized squared coefficients are classical. Stein and Shakarchi,
*Fourier Analysis: An Introduction* (2003), Chapter 3 §1 and Exercise 9,
supply Parseval and the reciprocal-square identity used in (9).
The bounded-variation context is already recorded in this line's
Taibleson/Wu sources. Hall–Shiu's *The index of a Farey sequence* (2003),
DOI [10.1307/mmj/1049832901](https://doi.org/10.1307/mmj/1049832901),
is the classical index reference, not the source of this artificial pair.

Magnitude ambiguity is also established prior art: Beinert and Plonka,
[*Ambiguities in one-dimensional phase retrieval of structured functions*](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/beinert_robert/Preprints/BeinertPlonka2015a.pdf),
explain why differing signals need not have differing Fourier magnitudes.
That literature is a reason to compute (4), not a general uniqueness
result for the sine observation used here. Targeted searches of Farey
index/permutation spectra and equivalent magnitude-retrieval formulations
support no claim of a new general Fourier or reconstruction theorem.

FD-333 already supplies raw energy and coefficient separation. The delta
here is distinct limiting **probability** laws, with uniform tail control,
an exact normalized finite-mode witness, and stability under its
unquantified \(o(1)\) discrepancy residual. In contrast,
[VIS-460](VIS-460-five-defect-rank-pair-has-inverse-prime-spectral-separation.md)
concerns a different pair whose boundary-localized difference vanishes in
normalized spectral distance. Its collapse does not extend to the
macroscopic blocks here.

This resolves the specified \(v=3\) test in the
[one-quantum clue](../clues/CLUE-one-quantum-farey-normalized-spectral-separation.md).
General \(v\), arbitrary probability pushforwards, and prime-uniform rates
are outside the result. Both words are artificial labeled-edge controls;
their seam labels need not be reduced denominators of the reconstructed
vertices. Exact rank-and-value identifiability is compatible with this
one-quantum instability. No genuine-Farey or RH estimate is improved.
