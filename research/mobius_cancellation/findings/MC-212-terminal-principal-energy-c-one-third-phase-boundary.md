# MC-212 — Scale-uniform terminal principal energy has a `c=1/3` Mertens phase boundary

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-211` shows that the lowest-shell principal energy becomes RH-equivalent once it is controlled simultaneously at a prefix `U`, at the one-prime rescaling `U/p`, and across the finite `q`-divisor prefix family required by the rough/smooth inverse. It deliberately leaves a possible loophole: perhaps one can prove a diagonal-scale estimate only at the **single terminal prefix attached to each ambient scale**, without obtaining same-scale prefix stability.

That loophole is narrower than it first appears. Fix

\[
0<c<\frac12.
\]

For every large ambient scale `Z`, define

\[
y_Z=c\log Z,
\qquad
q_Z=\prod_{\ell\le y_Z}\ell,
\qquad
T_Z=Z-q_Z,
\]

and, for root-modulus shells `D<d\le2D`, define the terminal principal energy

\[
\boxed{
P_D^{\rm term}(Z)
:=
\sum_{\substack{D<d\le2D\\
\mu^2(d)=1\\
(d,q_Z)=1\\
d^2\le Z}}
 d\,
\frac{|R_{q_Zd}(T_Z)|^2}{\varphi(d^2)^2},
}
\tag{1}
\]

where

\[
R_Q(U):=\sum_{\substack{n\le U\\(n,Q)=1}}\mu(n).
\]

Assume the **scale-uniform terminal hypothesis**

\[
\boxed{
(H_c):
\qquad
P_D^{\rm term}(Z)
\ll_{c,\varepsilon} Z^{1+\varepsilon}
}
\tag{2}
\]

for every `epsilon>0`, every sufficiently large `Z`, and every root-modulus shell with `D\ge y_Z` and `D\ll\sqrt Z`.

Then

\[
\boxed{
M(X)
\ll_{c,\varepsilon}
X^{\beta(c)+\varepsilon},
\qquad
\beta(c)
=
\frac12+rac c2\max(3c-1,0).
}
\tag{3}
\]

In particular,

\[
\boxed{
0<c\le\frac13
\quad\Longrightarrow\quad
(H_c)\iff RH.
}
\tag{4}
\]

The reverse implication `RH => (H_c)` holds for every fixed `0<c<1/2`. For `1/3<c<1/2`, `(H_c)` is not shown equivalent to RH, but `(3)` would still give a fixed-power Mertens estimate far beyond the known unconditional zero-free-region scale; as `c\uparrow1/2`, the exponent supplied by this argument remains below `5/8`.

The mechanism is an **ambient-scale transport** of the `MC-211` one-prime decoder. To bound the fixed-primorial prefix `R_{q_X}(X/e)`, one does not ask `(H_c)` for that nonterminal prefix. Instead one changes the ambient scale from `X` to `Z=X/e` and absorbs the missing primes between `q_Z` and `q_X` into the square-modulus root `d`. The energy weight charges this transport by `d^{3/2}`. The competition between the shorter prefix and that transport cost is exactly what produces the slope `3c-1` and the threshold `c=1/3`.

Thus a future proof that handles the principal part of `MC-210` separately cannot claim to evade the Mertens barrier merely because its theorem is stated only at the natural terminal point `T_Z`. If it works uniformly in the ambient scale and reaches diagonal size on every root shell, then for `c\le1/3` it already contains RH-level cancellation. The surviving escape is narrower: one must exploit the **raw principal–centered interference** in `W_D`, or a genuinely nonuniform/scale-local phenomenon not covered by `(H_c)`.

No estimate `(2)` is proved here, and no improved unconditional bound for `M(X)` or the zeta zero set is claimed.

## Derivation

### 1. Terminal energy gives a pointwise root-modulus bound

Suppose `(H_c)` holds. Any admissible square-free `d` belongs to one of the shells covered by `(2)`. Since every summand in `(1)` is nonnegative,

\[
 d\frac{|R_{q_Zd}(T_Z)|^2}{\varphi(d^2)^2}
\ll Z^{1+\varepsilon}.
\]

Using only `\varphi(d^2)\le d^2`,

\[
\boxed{
|R_{q_Zd}(T_Z)|
\ll
Z^{1/2+\varepsilon}d^{3/2}.
}
\tag{5}
\]

The loss `d^{3/2}` is the conditioning cost of extracting one member of the positive principal-energy family. It is the only fixed-power loss needed below.

The prime number theorem in Chebyshev-`theta` form gives

\[
\log q_Z=\vartheta(c\log Z)=c\log Z+o(\log Z),
\]

hence

\[
\boxed{q_Z=Z^{c+o(1)}.}
\tag{6}
\]

Because `c<1/2`, replacing `T_Z=Z-q_Z` by `Z` costs at most `q_Z`, which is sub-square-root at the ambient scale. We keep that endpoint error explicit when transporting between scales.

### 2. Transport a fixed `q_X` prefix to the terminal theorem at its own ambient scale

Fix large `X` and write

\[
Q=q_X.
\]

The exact inverse transform from `MC-210` is

\[
\boxed{
M(X)=\sum_{e\mid Q}\mu(e)R_Q(X/e).
}
\tag{7}
\]

Since `(6)` gives `Q=X^{c+o(1)}`, every divisor `e\mid Q` satisfies

\[
e=X^{\alpha},
\qquad
0\le\alpha\le c+o(1).
\tag{8}
\]

Put

\[
U=X/e.
\]

Choose a prime `p` with

\[
y_X<p\le2y_X.
\tag{9}
\]

For large `X` such a prime exists, and `p=X^{o(1)}`. Since `p\nmid Q`, the exact one-prime deletion identity used in `MC-211` gives

\[
\boxed{
R_Q(U)=R_{Qp}(U)-R_{Qp}(U/p).
}
\tag{10}
\]

We bound the two terms on the right by applying the **terminal** hypothesis at two different ambient scales rather than demanding a nonterminal theorem.

For `j=0,1`, set

\[
Z_j=U/p^j,
\qquad
q_j=q_{Z_j},
\qquad
 d_j=\frac{Q}{q_j}\,p.
\tag{11}
\]

Because `Z_j\le X`, one has `q_j\mid Q`; because `p>y_X`, the new prime does not divide `Q`. Thus `d_j` is square-free, `(d_j,q_j)=1`, and

\[
\boxed{q_jd_j=Qp.}
\tag{12}
\]

The prime-number-theorem asymptotic `(6)` also gives

\[
\begin{aligned}
\log d_j
&=\vartheta(c\log X)-\vartheta(c\log Z_j)+\log p\\
&=c\log(X/Z_j)+o(\log X)\\
&=c\alpha\log X+o(\log X),
\end{aligned}
\]

because `\log p=o(\log X)`. Therefore

\[
\boxed{d_j=X^{c\alpha+o(1)}.}
\tag{13}
\]

These transported roots remain inside the allowed square-modulus range. Indeed

\[
\frac{\log(d_j^2/Z_j)}{\log X}
=
2c\alpha-(1-\alpha)+o(1)
\le
2c^2-(1-c)+o(1),
\]

and

\[
2c^2+c-1=(2c-1)(c+1)<0.
\tag{14}
\]

Also `d_j>y_{Z_j}` because it contains the prime `p>y_X\ge y_{Z_j}`. Hence `d_j` lies in an admissible root shell for `(H_c)`.

Applying `(5)` at ambient scale `Z_j` and using `(12)`--`(13)` yields

\[
|R_{Qp}(T_{Z_j})|
\ll
X^{\frac{1-\alpha}{2}+\frac32c\alpha+\varepsilon+o(1)}.
\tag{15}
\]

The endpoint replacement costs

\[
|R_{Qp}(Z_j)-R_{Qp}(T_{Z_j})|
\le q_j
=Z_j^{c+o(1)}.
\tag{16}
\]

For `0<c<1/2` and `0\le\alpha\le c`, this error is smaller than the exponent in `(15)`; explicitly the difference between

\[
\frac12+\frac{3c-1}{2}\alpha
\]

and `c(1-\alpha)` stays positive on that rectangle. Thus `(15)` also bounds the exact prefixes at `Z_0=U` and `Z_1=U/p`. Combining with `(10)` gives

\[
\boxed{
|R_Q(X/e)|
\ll
X^{\frac12+\frac{3c-1}{2}\alpha+\varepsilon+o(1)}.
}
\tag{17}
\]

This is the key transport estimate. No bound at a nonterminal prefix was assumed; the shorter prefix was converted into a new ambient problem whose primorial mismatch appears only through the root-modulus factor `d_j`.

### 3. The `c=1/3` phase boundary appears after exact primorial inversion

The number of divisors of `Q=q_X` is subpower:

\[
\tau(Q)=2^{\pi(c\log X)}=X^{o(1)}.
\tag{18}
\]

Insert `(17)` into `(7)`. The worst exponent is obtained by maximizing

\[
b_c(\alpha)
:=
\frac12+\frac{3c-1}{2}\alpha
\tag{19}
\]

over `0\le\alpha\le c`.

If `c\le1/3`, the slope is nonpositive, so the maximum is `1/2` at `\alpha=0`. Hence

\[
M(X)\ll X^{1/2+\varepsilon+o(1)},
\]

which is the classical Mertens criterion for RH.

If `1/3<c<1/2`, the slope is positive and the largest divisor scale `\alpha=c` is worst. Therefore

\[
M(X)
\ll
X^{\frac12+\frac c2(3c-1)+\varepsilon+o(1)},
\]

which is `(3)`.

The threshold is therefore not a formal artifact of `MC-211`'s same-scale two-prefix formulation. It is the exact point, for this ambient-scale transport, at which the `d^{3/2}` extraction loss starts growing faster than the square-root gain obtained by shortening the prefix through the `q_X` divisor inversion.

### 4. RH supplies the terminal principal-energy bound

Assume RH. Then for every fixed `delta>0`,

\[
M(V)\ll_\delta V^{1/2+\delta}.
\tag{20}
\]

For `Q=q_Zd`, the exact forward rough/smooth transform from `MC-210` gives

\[
R_Q(V)
=
\sum_{\substack{r\le V\\r\in\mathcal S_Q}}M(V/r).
\tag{21}
\]

Uniformly for the square-free `y_Z`-rough roots `d\le\sqrt Z`, the corresponding Euler/semigroup overhead is `Z^{o(1)}`; this is the same subpower-complexity estimate established in `MC-210` and used in `MC-211`. Consequently

\[
R_{q_Zd}(T_Z)
\ll
Z^{1/2+\delta+o(1)}.
\tag{22}
\]

Moreover, because every prime divisor of `d` exceeds `y_Z=c\log Z`,

\[
\varphi(d^2)=d^2(1+o(1))
\tag{23}
\]

uniformly in the admissible range. Therefore

\[
\begin{aligned}
P_D^{\rm term}(Z)
&\ll
Z^{1+2\delta+o(1)}
\sum_{D<d\le2D}\frac{d}{\varphi(d^2)^2}\\
&\ll
Z^{1+2\delta+o(1)}
\sum_{D<d\le2D}\frac1{d^3}\\
&\ll
Z^{1+2\delta+o(1)}.
\end{aligned}
\tag{24}
\]

Choosing `delta` sufficiently small relative to `epsilon` proves `(H_c)`. Combined with the forward implication above, this establishes the equivalence `(4)`.

## Why it matters

`MC-209` exposed a potentially useful raw prescribed-residue variance target. `MC-210` then showed that standard centering projects out a Mertens-complete principal mode, while leaving aggregate control of that mode as a possible escape. `MC-211` closed the escape when the principal estimate is stable under the explicit one-prime rescaling and the full `q`-divisor prefix family.

The present result removes a further apparent freedom. **A theorem need not advertise prefix stability to contain it implicitly.** If the same terminal theorem holds at every ambient scale, the change of ambient scale manufactures the missing prefixes. The price is the primorial mismatch `q_X/q_Z`, which becomes part of the root modulus and is measured exactly by the energy weight. For small enough logarithmic pre-sieve constant, that price is still below the critical budget.

This leaves the live square-defect route with a much sharper target. Treating principal and centered pieces separately is viable only if the principal theorem is genuinely weaker than `(H_c)` in scale coverage or shell coverage, or if one deliberately works beyond the `c=1/3` equivalence range and can exploit the resulting exponent tradeoff. The structurally cleaner escape remains the one already identified in `MC-210`--`MC-211`: prove the **raw** energy `W_D` in a way that uses interference between the principal and centered residue components instead of bounding two positive energies independently.

For `c>1/3`, `(3)` is also a useful falsification threshold. A claimed proof of `(H_c)` would automatically imply a fixed-power bound `M(X)\ll X^{\beta(c)+\varepsilon}`. Any proposed argument assembled only from inputs known to give merely zero-free-region/subexponential cancellation must therefore contain a hidden strengthening somewhere; the exponent `(3)` identifies how large that strengthening would be.

## Boundary / conditions

- `(H_c)` is a **family over all sufficiently large ambient scales `Z`**. A bound proved only at one isolated value of `Z`, or on a sparse set with no transport to the scales `X/e` and `X/(ep)`, is not covered.
- The criterion concerns the **separate principal energy** from `MC-210`, not the raw prescribed-residue energy `W_D`. No lower bound for `W_D` or impossibility result for principal--centered interference is asserted.
- Uniformity over the root-modulus shells is load-bearing. The transported roots `d_j=(q_X/q_{Z_j})p` move with the divisor `e`; omitting those shells can break the decoder.
- The result uses the logarithmic primorial `y_Z=c\log Z` and fixed `c<1/2`. The admissibility estimate `(14)` is specific to that regime.
- The exact threshold `c=1/3` belongs to the present extraction method, through the factor `d^{3/2}` in `(5)`. The finding does **not** prove that no more efficient use of the aggregate energy can extend RH equivalence beyond `c=1/3`.
- Endpoint replacement `T_Z\leftrightarrow Z` uses only the trivial length bound and `q_Z=Z^{c+o(1)}`; no Möbius cancellation, zero-free region, or contour shift is inserted there.
- For `c>1/3`, `(H_c)` is not claimed equivalent to the exponent in `(3)` or to any zero-free half-plane. Only the displayed implication is established.

## Prior-art audit

The Mertens criterion `M(X)=O_\varepsilon(X^{1/2+\varepsilon}) iff RH`, the prime number theorem estimate `\vartheta(x)\sim x`, and the local Euler-factor rough/smooth transforms are classical. Their role here is structural bookkeeping, not a novelty claim. The exact transforms and their subpower complexity in the logarithmic-primorial regime were already audited internally in `MC-181`, `MC-210`, and `MC-211`.

Halupczok and Suger, *Partial sums of the Möbius function in arithmetic progressions assuming GRH* (arXiv:1111.3305), obtain uniform upper bounds for Mertens sums in arithmetic progressions under GRH. That literature is an adjacent pointwise/conditional control surface; it does not provide `(H_c)` unconditionally and is not used in the forward implication.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences* (Journal of the London Mathematical Society 112 (2025), e70293; arXiv:2412.19644), proves centered progression-variance estimates for general sequences. As explained in `MC-210`, that framework removes the principal residue mean rather than controlling `(1)`. The present result therefore does not follow by applying a standard centered BDH theorem.

The square-modulus BDH/large-sieve literature audited in `MC-209` is likewise adjacent to the shell averaging in `(1)`, but it does not supply this scale-uniform terminal principal-energy hypothesis. A targeted literature search found no source used here as evidence for the line-specific transport criterion `(2)`--`(4)`. This is not a literature-absence or novelty claim.

The durable contribution is the exact frontier refinement: **terminal-only principal control is not automatically a cheap escape from Mertens. Once it is uniform across ambient scales, the primorial mismatch can be transported into the root modulus, and the resulting conditioning budget crosses the RH threshold at `c=1/3`.**