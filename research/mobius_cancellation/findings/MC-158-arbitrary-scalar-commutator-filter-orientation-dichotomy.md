# MC-158 — Arbitrary scalar prime-commutator filters split into support or Möbius orientation

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation and one fixed prime `p` from `MC-156`–`MC-157`:

\[
B_p:=S_p^*[D_\mu,S_p],
\qquad
B_p\varepsilon_n=b_p(n)\varepsilon_n,
\qquad
b_p(n)=\mu(pn)-\mu(n)\in\{-2,-1,0,1,2\}.
\tag{1}
\]

`MC-157` classified every **odd** scalar spectral filter of this five-point alphabet. The full scalar functional calculus has an exact extension of that classification.

Let

\[
h:\{-2,-1,0,1,2\}\to\mathbb C
\tag{2}
\]

be arbitrary, and write its even/odd data as

\[
h_0:=h(0),
\qquad
u_2:=\frac{h(2)+h(-2)}2,
\qquad
v_2:=\frac{h(2)-h(-2)}2,
\tag{3}
\]

\[

u_1:=\frac{h(1)+h(-1)}2,
\qquad
v_1:=\frac{h(1)-h(-1)}2.
\tag{4}
\]

Define the cumulative scalar readout

\[
T_{p,h}(x):=\sum_{n\le x}h(b_p(n)),
\tag{5}
\]

together with

\[
Q(x):=\sum_{n\le x}\mu(n)^2,
\qquad
S_p(x):=\sum_{\substack{n\le x\\p\mid n}}\mu(n)^2,
\tag{6}
\]

and

\[
M(x):=\sum_{n\le x}\mu(n),
\qquad
A_p(x):=\sum_{\substack{n\le x\\p\mid n}}\mu(n).
\tag{7}
\]

Then there is an exact orthogonal-in-information decomposition

\[
\boxed{
T_{p,h}(x)=E_{p,h}(x)+R_{p,h}(x),
}
\tag{8}
\]

where the **orientation-blind support baseline** is

\[
\boxed{
E_{p,h}(x)
=h_0\lfloor x\rfloor
+(\nu_2-h_0)Q(x)
+(\nu_1-\nu_2)S_p(x),
}
\tag{9}
\]

and the entire **orientation-sensitive residual** is

\[
\boxed{
R_{p,h}(x)
=-v_2M(x)+(v_2-v_1)A_p(x).
}
\tag{10}
\]

Moreover

\[
A_p(x)=-\sum_{j\ge1}M(x/p^j),
\tag{11}
\]

so

\[
\boxed{
R_{p,h}(x)
=-v_2M(x)
-(v_2-v_1)\sum_{j\ge1}M(x/p^j).
}
\tag{12}
\]

Thus `R_{p,h}` is exactly the `MC-157` readout for the odd part of `h`. This gives a complete scalar dichotomy:

1. if `v_1=v_2=0`, equivalently `h` is even on the nonzero spectrum, then `T_{p,h}` depends only on squarefree support and divisibility by `p`; it contains **no Möbius sign information**;
2. if `(v_1,v_2)\ne(0,0)`, then after subtracting the explicitly support-only baseline `(9)`, the remaining scalar family is a nonzero odd filter and therefore retains the full Mertens sequence across `p`-dilated scales.

The second statement is exact, not heuristic. If `D` denotes scale dilation `(Df)(x)=f(x/p)`, then

\[
\boxed{
(1-D)R_{p,h}
=-v_2M+v_1DM.
}
\tag{13}
\]

Hence if `v_2=0` and `v_1\ne0`,

\[
\boxed{
M(x)=\frac{R_{p,h}(px)-R_{p,h}(x)}{v_1},
}
\tag{14}
\]

while if `v_2\ne0`,

\[
\boxed{
M(x)
=\frac{v_1}{v_2}M(x/p)
-\frac{R_{p,h}(x)-R_{p,h}(x/p)}{v_2},
}
\tag{15}
\]

which terminates after finitely many downward `p`-dilations because `M(y)=0` for `0\le y<1`.

There is therefore **no intermediate scalar spectral quotient hidden in the even part of the commutator alphabet**. Even scalar data collapse to classical squarefree support; every surviving odd component is the already-classified Möbius-orientation channel. A genuinely intermediate Bost–Connes/semigroup carrier must retain a relation not reducible to scalar functional calculus followed by cumulative summation.

## 1. The five-point alphabet separates support from orientation exactly

`MC-156` gives the exhaustive coefficient cases

\[
b_p(n)=
\begin{cases}
0,&\mu(n)=0,\\
-2\mu(n),&\mu(n)\ne0\text{ and }p\nmid n,\\
-\mu(n),&\mu(n)\ne0\text{ and }p\mid n.
\end{cases}
\tag{16}
\]

For a squarefree `n` with `p\nmid n`, equations `(3)` and `(16)` give

\[
h(b_p(n))=\nu_2-v_2\mu(n),
\tag{17}
\]

while for squarefree `n` with `p\mid n`,

\[
h(b_p(n))=\nu_1-v_1\mu(n).
\tag{18}
\]

On nonsquarefree `n`, the value is simply `h_0`. Summing the three disjoint sectors proves `(8)`–`(10)`.

The point is not merely the formal even/odd decomposition of a function on a symmetric finite set. Here the even part has a concrete arithmetic meaning: it sees only whether `n` is squarefree and, inside the squarefree sector, whether `p` divides `n`. All parity orientation `(-1)^{\Omega(n)}` is concentrated in the two odd coefficients `v_2,v_1`.

## 2. The support baseline is unconditionally controlled at square-root scale

The classical squarefree-counting estimate recorded in `MC-S12` gives

\[
Q(x)=\delta x+O(\sqrt x),
\qquad
\delta:=\frac6{\pi^2}.
\tag{19}
\]

The `p`-divisible squarefree count satisfies the exact recursion

\[
S_p(x)=Q(x/p)-S_p(x/p),
\tag{20}
\]

because a squarefree integer divisible by `p` is uniquely `pm` with `m` squarefree and `p\nmid m`. Iterating `(20)` gives

\[
S_p(x)=\sum_{j\ge1}(-1)^{j-1}Q(x/p^j),
\tag{21}
\]

and therefore, for fixed `p`,

\[
\boxed{
S_p(x)=\frac{\delta}{p+1}x+O_p(\sqrt x).
}
\tag{22}
\]

Substitution into `(9)` yields

\[
\boxed{
E_{p,h}(x)=\kappa_{p,h}x+O_{p,h}(\sqrt x),
}
\tag{23}
\]

with

\[
\kappa_{p,h}
=h_0
+\delta(\nu_2-h_0)
+\frac{\delta}{p+1}(\nu_1-\nu_2).
\tag{24}
\]

Thus for every fixed exponent `\theta>1/2`,

\[
T_{p,h}(x)-\kappa_{p,h}x=O(x^\theta)
\quad\Longleftrightarrow\quad
R_{p,h}(x)=O(x^\theta).
\tag{25}
\]

The even part cannot conceal an unknown super-square-root arithmetic contribution: its centered error is already controlled at the critical power scale by elementary squarefree counting. Any power-cancellation difficulty above `1/2` lies entirely in the orientation residual `(12)`.

In particular, if `h` is even, then

\[
T_{p,h}(x)=\kappa_{p,h}x+O_{p,h}(\sqrt x)
\tag{26}
\]

unconditionally. A critical-half threshold seen in such an even scalar statistic is therefore support geometry, not evidence for Mertens cancellation.

## 3. The orientation residual has an exact scale-recursion decoder

For `A_p` in `(7)`, writing `n=pm` and using the squarefree cases gives

\[
A_p(x)
=-\sum_{\substack{m\le x/p\\p\nmid m}}\mu(m)
=-M(x/p)+A_p(x/p).
\tag{27}
\]

Iteration proves `(11)`. Substituting into `(10)` proves `(12)`.

Applying `1-D` to `(12)` telescopes the geometric scale tail and gives `(13)`. Equations `(14)`–`(15)` follow immediately.

This also exposes a quantitative conditioning boundary that exact reconstruction alone does not show. Suppose `v_2\ne0` and write

\[
r:=\left|\frac{v_1}{v_2}\right|.
\tag{28}
\]

If `R_{p,h}(x)=O(x^\theta)`, downward iteration of `(15)` preserves the exponent `\theta` whenever

\[
r<p^\theta.
\tag{29}
\]

At equality one may pay a logarithm, while if `r>p^\theta` the bare recurrence permits amplification to the artificial exponent

\[
\alpha=\log_p r>\theta.
\tag{30}
\]

Indeed the homogeneous scale equation `-v_2H(x)+v_1H(x/p)=0` has `p`-orbit solutions with growth `x^{\alpha}` in magnitude. This is a conditioning statement about the scalar transform, not a claim that the actual Mertens function contains such a mode.

Consequently the centered scalar criterion

\[
T_{p,h}(x)-\kappa_{p,h}x
=O_\varepsilon(x^{1/2+\varepsilon})
\tag{31}
\]

is immediately RH-equivalent through this elementary decoder when either

- `v_2=0`, `v_1\ne0`; or
- `v_2\ne0` and `|v_1/v_2|\le\sqrt p`.

The forward implication from RH is automatic for every fixed `h`, because `(12)` is a convergent finite-at-each-`x` geometric dilation combination of Mertens values and `(23)` controls the support baseline. The condition above is only the boundary for the elementary inverse implication supplied by `(15)`; filters outside it are not claimed to be non-equivalent by some deeper Möbius-specific argument.

This quantitative distinction prevents an information-theoretic statement from being mistaken for a free cancellation estimate: exact recoverability can still be badly conditioned at the power scale relevant to RH.

## 4. What this closes and what remains genuinely open

`MC-149`–`MC-155` showed that norms, essential norms, Schatten membership, simultaneous magnitude rows, and continuous one-state cluster data discard too much orientation and admit support-matched controls with linear bias. `MC-156` showed the opposite endpoint: exact signed state-labelled coefficients of one prime commutator reconstruct `\mu` pointwise by a cubic polynomial. `MC-157` then classified every odd scalar spectral filter after cumulative aggregation.

The present result fills the remaining scalar gap. Allowing an arbitrary function of the five-point spectrum does not create a third information type. Its even part is exactly squarefree/divisibility support with an unconditional square-root-scale asymptotic, and its odd part is exactly the `MC-157` Mertens channel.

Therefore further work should not search the scalar functional calculus of one raw prime commutator for a hidden phase-sensitive critical statistic. A surviving semigroup mechanism must change the information architecture: for example, a genuinely relational quotient between states or scales, a non-scalar/twisted operation not reducible to `h(B_p)`, a distributional relation not determined by scalar cumulative sums, or another source-forced coupling. Any such proposal must still show that it is cheaper than reconstructing the complete Möbius parity field and that it transfers to anchored additive excursion.

## Prior-art and novelty audit

The Bost–Connes system, its canonical semigroup representation, and nearby twisted-spectral-triple constructions are established prior art already audited in `MC-138`–`MC-157`. In particular, `MC-149` records Greenfield, Marcolli and Teh, *Twisted Spectral Triples and Quantum Statistical Mechanical Systems* (2014), as a boundary showing that richer twisted noncommutative structures exist beyond the raw commutators classified here.

A fresh targeted search for Bost–Connes commutator functional calculus together with Möbius arithmetic located the standard Bost–Connes and twisted-spectral-triple literature but did not locate this exact five-point even/odd cumulative classification. No novelty inference is drawn from that absence. Equations `(8)`–`(18)` are elementary consequences of the already-persisted coefficient classification in `MC-156`–`MC-157`.

The only arithmetic asymptotic used in the new support analysis is the classical squarefree count `MC-S12`; `(20)`–`(22)` are elementary consequences. No zero-free region, continuation of `1/\zeta`, Mertens estimate, random model, or RH-equivalent input enters the decomposition or the negative conclusion.

## Boundaries and falsification tests

- **One fixed prime and scalar functional calculus only.** The result concerns `h(B_p)` followed by ordinary cumulative summation. It does not classify joint noncommutative expressions involving several operators, twisted commutators, alternative representations, or state-to-state relational observables.
- **Support subtraction is explicit, not hidden zero information.** Exact recovery uses the exact support counts `Q,S_p`; power-scale statements need only their unconditional square-root asymptotics `(19)`–`(23)`. Neither contains Möbius orientation.
- **Exact recovery is not automatically a stable RH criterion.** Equation `(29)` records the inverse-conditioning requirement for the simple downward recurrence. When `|v_1/v_2|>\sqrt p`, no RH-equivalence is claimed from the scalar bound alone.
- **Even filters are genuinely phase-blind.** Matched sequences with the same squarefree support have exactly the same `E_{p,h}`; no rearrangement or probabilistic argument is needed.
- **No claim against richer Bost–Connes structure.** The conclusion is deliberately a no-go for one complete scalar class. A non-scalar, twisted, distributional, or cross-state mechanism lies outside its hypotheses.
- **No Mertens improvement.** The finding closes a representation-level route and sharpens its conditioning boundary; it does not improve the known bound for `M(x)` and is not evidence for or against RH.

## Consequence for the line

The scalar one-prime commutator branch is now complete at the level of arbitrary spectral filters. There is a sharp trichotomy only in **use**, not in information type:

- even filters are support-only and unconditionally square-root controlled after centering;
- non-even filters contain the same odd Möbius orientation channel as `MC-157`;
- among those orientation filters, only a quantitatively stable subclass transfers RH-scale bounds back through the elementary dilation recursion without exponent loss.

The next semigroup candidate should therefore be rejected at first kill if it reduces, after scalarization, to a function of the five-point `B_p` spectrum and ordinary prefix aggregation. The unresolved Bost–Connes question has moved beyond scalar spectral filtering to genuinely relational structure.