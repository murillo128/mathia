# WP-076 — Shifted-cover digamma mixing is a positive semigroup cocycle coboundary

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-CLASSICALIZATION`. `WP-075` found a positive shifted-resolvent defect whose trace contains both `log n` and a digamma correction, leaving open whether multiplicative assembly of the same defects could separate an exact finite-prime term from a positive archimedean term. It cannot do so by composition inside this family. The normalized root-cover operators make the defects an exact positive semigroup cocycle, while the entire digamma correction is a scalar coboundary for the degree action `c -> c/n`. Along every factorization it telescopes to an endpoint term and contains no irreducible cross-prime interaction. For positive real shift the defect is moreover strictly smaller than the zero-shift `log n` defect in operator order, so restoring exact finite coefficients requires a positive degree-dependent correction whose accumulated trace is the opposite of the apparent digamma remainder. At the critical complex shift the operator order itself disappears. This closes the direct "reorganize the same positive shifted defects" escape from `WP-075`; it does not rule out a genuinely nonseparable finite-archimedean coupling, quotient, compression, or different positive geometry.

## 1. Setup inherited from WP-073--WP-075

In the Hardy-coordinate realization of the pointed local Dirichlet space, write

\[
W_n e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
L e_k=\left(k+\frac12\right)e_k.
\]

The normalized cover operators satisfy

\[
W_mW_n=W_nW_m=W_{mn},
\tag{1}
\]

because either order partitions the basis into the same blocks of length `mn`.

For real `c>-1/2`, `WP-075` defines the positive trace-class Jensen defect

\[
R_{n,c}
=
 nW_n^*(L+cI)^{-1}W_n
-(L+c/n\,I)^{-1}
\succeq0,
\tag{2}
\]

with exact trace

\[
\tau_n(c):=\operatorname{Tr}R_{n,c}
=
\log n
+\psi\!\left(\frac12+\frac cn\right)
-\psi\!\left(\frac12+c\right).
\tag{3}
\]

At `c=0`, this is the inverse-scale defect `Q_n` of `WP-074` and

\[
\tau_n(0)=\log n.
\tag{4}
\]

The question here is whether the simultaneous appearance of `log n` and `psi` in (3) reflects a genuine finite--archimedean coupling under multiplicative cover composition, or only a reanchoring of one universal scale defect.

## 2. The defects satisfy an exact positive operator cocycle

Using (1), expand the defect for degree `mn`:

\[
R_{mn,c}
=
mnW_n^*W_m^*(L+cI)^{-1}W_mW_n
-(L+c/(mn)\,I)^{-1}.
\]

Insert and subtract `nW_n^*(L+c/m\,I)^{-1}W_n`. The terms group exactly as

\[
\boxed{
R_{mn,c}
=
nW_n^*R_{m,c}W_n
+R_{n,c/m}.
}
\tag{5}
\]

Since the `W_n` commute, the symmetric factorization also holds:

\[
\boxed{
R_{mn,c}
=
mW_m^*R_{n,c}W_m
+R_{m,c/n}.
}
\tag{6}
\]

For real `c>-1/2`, every term on the right of (5)--(6) is positive. Thus this is not merely a scalar identity after taking traces: the shifted defects form a **positive operator cocycle** for multiplicative block refinement, with the shift parameter acted on by

\[
c\longmapsto \frac cn.
\tag{7}
\]

The cocycle already exposes a major limitation. Composite degree does not create a new interaction term. It is assembled completely from positive pulled-back lower-degree defects, with only the scale parameter reanchored.

## 3. Trace scaling turns the digamma term into a pure coboundary

Every `R_{m,c}` is diagonal in the `e_k` basis. More generally, for any diagonal trace-class operator

\[
D e_j=d_j e_j,
\]

one has

\[
\langle e_k,W_n^*DW_ne_k\rangle
=\frac1n\sum_{r=0}^{n-1}d_{nk+r}.
\]

Summing over `k` enumerates every nonnegative integer exactly once, so

\[
\boxed{
n\operatorname{Tr}(W_n^*DW_n)=\operatorname{Tr}D.
}
\tag{8}
\]

Taking traces in (5) therefore gives

\[
\boxed{
\tau_{mn}(c)=\tau_m(c)+\tau_n(c/m).
}
\tag{9}
\]

Now set

\[
F(c)=\psi\!\left(\frac12+c\right).
\]

Then (3) is

\[
\tau_n(c)=\log n+\delta_n(c),
\qquad
\delta_n(c)=F(c/n)-F(c).
\tag{10}
\]

The correction is therefore exactly a coboundary for the multiplicative action (7):

\[
\delta_{mn}(c)
=
\delta_m(c)+\delta_n(c/m).
\tag{11}
\]

So the apparent `log degree + digamma` mixture in `WP-075` contains no new two-degree invariant. The logarithm is the additive semigroup character; the digamma part is an endpoint difference of the same scalar potential `F`.

## 4. Every prime factorization telescopes to the same endpoint

Let

\[
N_j=n_1n_2\cdots n_j,
\qquad N_0=1.
\]

Iterating (9) yields

\[
\tau_{N_r}(c)
=
\sum_{j=1}^r
\tau_{n_j}\!\left(\frac{c}{N_{j-1}}\right).
\tag{12}
\]

The digamma contributions telescope exactly:

\[
\sum_{j=1}^r
\left[
F\!\left(\frac c{N_j}\right)
-F\!\left(\frac c{N_{j-1}}\right)
\right]
=
F(c/N_r)-F(c).
\tag{13}
\]

In particular, if the `n_j` are primitive prime degrees, the `j`-th positive step has trace

\[
\log n_j
+
F(c/N_j)-F(c/N_{j-1}).
\tag{14}
\]

There is no residual depending on pairs or larger sets of prime factors. Reordering factors changes the intermediate scale at which individual terms are sampled, but the assembled operator is the same by (5)--(6) and the total scalar correction is always the endpoint (13).

This is precisely the wrong structure for the missing Mathia mechanism. A genuinely global Weil completion must introduce finite--archimedean coupling before positivity in a way that is not reducible to independent cover refinement plus an endpoint scalar.

## 5. Operator monotonicity makes the exact-weight obstruction one-sided

The diagonal entry of (2) can be written

\[
r_{n,c}(k)
=
\frac1n\sum_{r=0}^{n-1}
\frac1{k+(r+1/2+c)/n}
-
\frac1{k+1/2+c/n}.
\tag{15}
\]

Let

\[
x_r=k+\frac{r+1/2+c}{n},
\qquad
\mu=k+\frac12+\frac cn
=\frac1n\sum_{r=0}^{n-1}x_r.
\]

Differentiating (15),

\[
\frac{\partial r_{n,c}(k)}{\partial c}
=
\frac1n
\left[
\mu^{-2}
-
\frac1n\sum_{r=0}^{n-1}x_r^{-2}
\right]
<0
\qquad(n>1),
\tag{16}
\]

where strict negativity is Jensen convexity of `x -> x^{-2}` and the `x_r` are not all equal. Hence

\[
\boxed{
c_1<c_2
\quad\Longrightarrow\quad
R_{n,c_1}\succ R_{n,c_2}.
}
\tag{17}
\]

For `c>0`, therefore,

\[
0\prec R_{n,c}\prec Q_n:=R_{n,0},
\tag{18}
\]

and the positive correction needed to restore the exact finite trace is

\[
A_{n,c}:=Q_n-R_{n,c}\succ0,
\tag{19}
\]

with

\[
\operatorname{Tr}A_{n,c}
=
F(c)-F(c/n)>0.
\tag{20}
\]

For `-1/2<c<0`, the inequalities reverse and every shifted step has trace strictly **larger** than `log n`. This recovers the uniqueness statement of `WP-075` but strengthens its interpretation: `c=0` is not just the unique scalar solution of `tau_n(c)=log n`; it is the unique point where the positive cocycle has no endpoint coboundary at all.

## 6. The large-degree digamma remainder is endpoint data, not a positive local-to-global merger

For fixed real `c>-1/2`, as `N -> infinity`,

\[
F(c/N)-F(c)
\longrightarrow
F(0)-F(c)
=
\psi(1/2)-\psi(1/2+c).
\tag{21}
\]

For `c>0`, this endpoint remainder is strictly negative because `psi'(x)>0` for `x>0`. Equivalently, the positive operator difference in (19) has limiting trace

\[
\operatorname{Tr}A_{N,c}
\longrightarrow
\psi(1/2+c)-\psi(1/2)>0.
\tag{22}
\]

Thus there are only two descriptions inside this family:

```text
shifted positive defect:
    R_{N,c}
    trace = log N + [negative endpoint digamma correction]   (c>0)

exact finite defect:
    Q_N = R_{N,c} + A_{N,c}
    trace = log N
    with A_{N,c} >= 0 carrying the opposite endpoint correction
```

The second line does produce a positive digamma-shaped difference, but it is not a separate finite-neutral archimedean term at finite degree: it depends on `N`, and adding it back removes the digamma from the total trace exactly. Taking `N -> infinity` makes the correction universal only as an endpoint limit. It therefore does not provide the single intrinsic finite-plus-archimedean positive form demanded by the research mandate.

If one instead inserts the Riemann spectral shift `c=(s-1)/2`, then on the critical line `s=1/2+it` the shift is

\[
c=-\frac14+\frac{it}{2},
\]

which is non-real for `t != 0`. The self-adjoint ordering (17)--(19), and hence the independent positive theorem for this resolvent family, no longer applies. Analytic continuation of the scalar trace is not a substitute for operator positivity.

## 7. Matched controls and novelty audit

The operator identities above use only block-replication isometries, the half-integer scale operator, and integer degree multiplication. They do not use primality, cyclotomic coefficients, zeta zeros, the zeta functional equation, or any arithmetic distinction between prime and composite cover degrees. Consequently the cocycle/coboundary structure survives unchanged for matched non-arithmetic cyclic-cover systems with the same degree semigroup. It is therefore **universal cover geometry**, not evidence for an arithmetic global positivity theorem.

The external ingredients are classical. The weighted-composition semigroup itself is already the Noor / Manzur--Noor--Santos Hardy-space semigroup retained in `SOURCES.md`. The scalar digamma multiplication identities are classical Gauss multiplication formulas; NIST DLMF §5.5(iii), especially equation 5.5.9, records the corresponding psi multiplication law, and DLMF §5.15.1 gives

\[
\psi'(x)=\sum_{k\ge0}(k+x)^{-2}>0
\qquad(x>0),
\]

used for the sign in (21). A directed search around the exact Hardy weighted-composition semigroup, resolvent/Jensen defects, digamma multiplication, and semigroup cocycles did not identify a source asserting this Mathia-specific obstruction. No theorem-level novelty is claimed for semigroup cocycles, Jensen convexity, or digamma identities. The durable content is the classification of the `WP-075` candidate: its apparent finite--archimedean mixing is a positive degree cocycle with a pure scalar coboundary, so multiplicative assembly cannot supply the missing nonseparable global interaction.

## 8. Exact falsification surface

This finding can be falsified by any of the following:

1. failure of the exact semigroup law `W_mW_n=W_mn` for the normalized operators used in `WP-074`;
2. failure of either operator cocycle identity (5)--(6);
3. failure of the trace-scaling identity (8) for the diagonal trace-class defects;
4. failure of the `WP-075` trace formula (3);
5. a non-endpoint interaction term surviving in (12)--(13);
6. failure of the strict operator monotonicity (17) for real `c>-1/2`;
7. a positivity-preserving construction **within the same shifted-defect cocycle** that leaves every primitive finite trace exactly `log p`, produces a nonzero prime-independent archimedean term before taking a singular endpoint limit, and does not import that term by hand.

Item 7 is intentionally narrower than a global no-go. A construction that changes the Hilbert object, introduces a nonseparable finite--archimedean block before the sign theorem, takes a genuine quotient/compression with new geometry, or otherwise exits the cocycle hypotheses is not excluded.

## Research consequence

`WP-075` showed that shifting a single positive inverse-scale defect cannot simultaneously retain exact finite weights and expose the Gamma profile. `WP-076` shows that **multiplicative assembly does not repair that failure**: the whole shifted family is compositional, and its digamma correction telescopes as a coboundary.

The next viable route therefore has to break this universality before positivity is read out. In the current pointed-cover branch, merely refactoring `R_{n,c}` over prime degrees, reordering covers, or sending the total degree to infinity cannot create the required global coupling. A survivor must introduce a non-coboundary interaction -- for example a canonical cross-prime/archimedean compression, quotient, boundary coupling, or cohomological pairing -- while still preserving the exact `Lambda(p^k)/sqrt(p^k)` finite data and deriving its sign independently of RH or inserted zero data.
