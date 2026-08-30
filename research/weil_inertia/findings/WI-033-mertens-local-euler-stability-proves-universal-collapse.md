# WI-033 — Mertens mass plus local Euler stability proves the deterministic universal-collapse step

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** establish the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It closes a specific analytic subproblem inside the public Yang--Yang deterministic singular-series model: once their exact `b1,b2` zone formula and corrected gamma coefficients are taken as the object to be evaluated, the claimed collapse onto the universal `(1,1)` continuum class follows from classical Mertens estimates plus an explicit local-Euler stability bound. Combined with WI-030 and WI-032, this gives

\[
\boxed{
\operatorname{core}_{\rm det}(T)
=-\frac1{48}+O\!\left(\frac1{\log T}\right)
}
\]

for that deterministic source object.

The still-load-bearing step is upstream: prove that the actual zeta fourth-moment off-diagonal is bounded/replaced by this deterministic singular-series object at the exact strength asserted by the structured-shift/MRT/gluing layer, and close the remaining finite remainder/zone ledger. Nothing below imports the paper's final `69.16%`, `70.31%`, or larger claims as established evidence.

## 1. Source and scope

The source is pinned at

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

The relevant exact implementation pieces are:

- `scripts/m1_suite.py`: prime-power weights `Lambda(b)/b`, the exact selector, the four-leg overlap geometry `qvec`, and the full singular-series row sum;
- `scripts/tail_bound.py`: the corrected tensor factorization of `gamma_d^free` for general prime-power `b1,b2`;
- `scripts/quadrature_cert.py` / `scripts/sawtooth_cert.py`: the universal `(1,1)` continuum scaling;
- `paper.tex`, Lemma `CL`: the explicit claim that Mertens mass concentrates on large-prime pairs and the deterministic core collapses onto the universal `(1,1)` class, with the rate write-out named as unfinished in the grading note.

Pinned URLs:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/m1_suite.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/tail_bound.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/quadrature_cert.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex

Classical arithmetic input:

- Franz Mertens, *Ein Beitrag zur analytischen Zahlentheorie*, J. reine angew. Math. 78 (1874), 46--62. In the form used here,
  `sum_{p<=x} 1/p = log log x + O(1)` and, after the standard prime-power/von-Mangoldt reformulation,
  `sum_{n<=x} Lambda(n)/n = log x + O(1)`.

No novelty is claimed for Mertens summation, weak convergence of the resulting logarithmic prime measure, or tensor-product `l1` estimates. The derived content is their exact application to the Yang--Yang local gamma system and source geometry.

## 2. Exact scaled form of the source geometry

Write

\[
X=\frac{T}{2\pi},
\qquad
\ell=\log X,
\qquad
\ell_1=\ell+2\log2-1.
\]

For a prime power `b=p^a<=X`, put

\[
\beta(b)=\frac{\log b}{\ell}.
\]

On the deep zone use

\[
\theta=2\pi e^{-t\ell},
\qquad 0\le t\le1.
\tag{1}
\]

The two source selectors in `m1_suite.py` become exactly

\[
\beta_{\max}\le\frac{1+t}{2},
\qquad
\beta_{\min}\ge t.
\tag{2}
\]

Thus the beta domain is the continuum domain already isolated in WI-030.

Every argument of the source overlap functions is a logarithm linear in `ell`; `max`, `min`, and positive part are homogeneous of degree one. Consequently the symmetrized four-ordering geometry has the exact form

\[
Q_{\ell}(b_1,b_2;t)
=\ell\,F_t(\beta_1,\beta_2),
\tag{3}
\]

where `F_t` is a bounded piecewise-affine function supported on (2). A deliberately loose source-independent bound is

\[
|F_t|\le24,
\tag{4}
\]

because each ordered `qvec` contains four leg orderings times three overlap lengths, each at most `ell`, and the source symmetrization adds at most a second ordered copy. The number of affine pieces and their slopes are uniformly bounded in `t`, so `F_t` has uniformly bounded two-dimensional variation.

The fixed-`theta` edge outside the scaled interval has `t`-width `O(1/ell)` and contributes only `O(1/ell)` after the source normalization; this is the same edge layer separated in WI-030.

## 3. The local gamma law is stable when the base primes are large

Let

\[
c_p=\frac1{p-1}.
\]

For an odd prime not dividing `2b1b2`, `tail_bound.py` gives the generic local gamma factor

\[
v_p=(1-c_p^2,\ c_p^2)
\tag{5}
\]

on valuations `0,1`, with `l1` norm exactly one.

If `p` divides exactly one of the two prime-power bases, independently of its exponent the local beta table is

\[
B_p(0)=1,
\qquad
B_p(1)=-c_p,
\qquad
B_p(v)=0\quad(v\ge2),
\]

so the Mobius difference `g_p(v)=B_p(v)-B_p(v+1)` is

\[
u_p=(1+c_p,\ -c_p).
\tag{6}
\]

Therefore

\[
\boxed{
\|u_p-v_p\|_1
=2(c_p+c_p^2)
=\frac{2p}{(p-1)^2}
\ll\frac1p.
}
\tag{7}
\]

The class piece in `gamma_free=gamma_full-gamma_class` changes at the same prime from a delta mass at valuation zero to (6), so

\[
\|u_p-\delta_0\|_1=\frac{2}{p-1}\ll\frac1p.
\tag{8}
\]

Tensor-product telescoping now gives the key stability estimate. If

\[
b_1=p^a,
\qquad
b_2=q^b,
\qquad
p\ne q,
\qquad
p,q>2,
\]

then, comparing with the universal `(1,1)` coefficient sequence,

\[
\boxed{
\|\gamma^{b_1,b_2}-\gamma^{1,1}\|_{\ell^1(d)}
\ll \frac1p+\frac1q.
}
\tag{9}
\]

The implied constant is absolute: every generic local factor has norm one and every special odd local factor has norm at most `1+2/(p-1)<=2`.

The exceptional cases are harmless. If the two bases have the same prime base, or one base is a power of `2`, the corrected local tables in `tail_bound.py` still have uniformly bounded finite `l1` norm. Hence

\[
\|\gamma^{b_1,b_2}\|_1+
\|\gamma^{1,1}\|_1\ll1
\tag{10}
\]

uniformly in their exponents.

## 4. Gamma stability gives a uniform row-kernel bound

The exact source sawtooth satisfies

\[
|G_0(x)|\le\pi.
\tag{11}
\]

For a general base pair define, as in the source gamma resummation,

\[
y_{b_1,b_2}(\theta)
=-\frac1\theta
\sum_{d\ge1}\gamma_d^{b_1,b_2}G_0(d\theta).
\tag{12}
\]

Equations (9)--(12) imply for distinct odd prime bases

\[
\boxed{
|y_{p^a,q^b}(\theta)-y_{1,1}(\theta)|
\ll
\frac1\theta\left(\frac1p+\frac1q\right).
}
\tag{13}
\]

For the exceptional same-base / base-2 pairs the same argument with (10) gives the coarse but uniform

\[
|y_{b_1,b_2}(\theta)-y_{1,1}(\theta)|
\ll\frac1\theta.
\tag{14}
\]

These estimates use the **corrected** special-prime normalization in `tail_bound.py`; the older pre-correction helper in `mains_envelope.py` is not used.

## 5. The source selector kills the apparent `1/theta` loss

On every selected source cell, (2) gives

\[
t\le\beta_{\min}.
\]

Therefore

\[
\begin{aligned}
\int_{\rm selected}\frac{dt}{\theta(t)}
&\le
\frac1{2\pi}
\int_0^{\beta_{\min}} e^{t\ell}\,dt\\
&\le
\boxed{
\frac{b_{\min}}{2\pi\ell}.
}
\end{aligned}
\tag{15}
\]

This elementary inequality is the key cancellation: the dangerous exponential growth of `1/theta` is exactly compensated by the `1/b` weights in the prime-power sum.

The source normalization, after `T/(pi ell X)=2/ell`, the change of variables (1), and (3), is of the form

\[
-\frac{2\ell}{\ell_1^4}
\sum_{b_1,b_2}
\frac{\Lambda(b_1)}{b_1}
\frac{\Lambda(b_2)}{b_2}
\int y_{b_1,b_2}(\theta(t))
F_t(\beta_1,\beta_2)\,dt,
\tag{16}
\]

with the source's unordered-plus-symmetrized convention equivalent to the corresponding ordered double sum.

## 6. The non-universal arithmetic part is `o(1)`

For the distinct odd-prime-base contribution, insert (13) and (15) into (16). Up to an absolute constant the error is bounded by

\[
\frac1{\ell_1^4}
\sum_{p^a,q^b\le X}
\frac{\log p}{p^a}
\frac{\log q}{q^b}
\min(p^a,q^b)
\left(\frac1p+\frac1q\right).
\tag{17}
\]

For the `1/p` half use `min(p^a,q^b)<=p^a`:

\[
(17)
\ll
\frac1{\ell^4}
\left(
\sum_{p^a\le X}\frac{\log p}{p}
\right)
\left(
\sum_{q^b\le X}\frac{\log q}{q^b}
\right).
\tag{18}
\]

The second factor is `ell+O(1)` by Mertens. For the first,

\[
\sum_{p^a\le X}\frac{\log p}{p}
\le
\ell\sum_{p\le X}\frac1p
=O(\ell\log\ell).
\tag{19}
\]

Hence distinct bases contribute

\[
\boxed{
O\!\left(\frac{\log\ell}{\ell^2}\right).
}
\tag{20}
\]

For equal odd prime bases, (14)--(15) leave

\[
\frac1{\ell^4}
\sum_{p\le X}(\log p)^2
\sum_{a,b\ge1}p^{-\max(a,b)}.
\]

The inner sum is exact:

\[
\sum_{a,b\ge1}p^{-\max(a,b)}
=\frac{p+1}{(p-1)^2}
\ll\frac1p.
\tag{21}
\]

Since

\[
\sum_{p\le X}\frac{(\log p)^2}{p}
\le
\ell\sum_{p\le X}\frac{\log p}{p}
=O(\ell^2),
\]

the equal-base error is `O(ell^{-2})`. The base-2 families obey the same `O(ell^{-2})` bound by summing the geometric `2^{-a}` weights and using the Mertens bound for the other base.

Combining the cases,

\[
\boxed{
\operatorname{core}_{\rm det}(T)
=\operatorname{core}_{\rm univ}(T)
+O\!\left(\frac{\log\ell}{\ell^2}\right)
+O\!\left(\frac1\ell\right)_{\rm edge}.
}
\tag{22}
\]

Thus the dependence of the gamma law on the actual prime bases is asymptotically negligible in exactly the normalization consumed by the source.

## 7. Mertens mass becomes Lebesgue measure on logarithmic beta scale

Define the probability-scale prime-power measure

\[
\mu_\ell
=\frac1\ell
\sum_{p^a\le X}
\frac{\log p}{p^a}
\delta_{\log(p^a)/\ell}.
\tag{23}
\]

The classical prime-power Mertens estimate gives, uniformly for `0<=u<=1`,

\[
\mu_\ell([0,u])
=\frac1\ell
\sum_{p^a\le X^u}\frac{\log p}{p^a}
=u+O\!\left(\frac1\ell\right).
\tag{24}
\]

Hence `mu_ell` converges to Lebesgue measure on `[0,1]`, with discrepancy `O(1/ell)`. Because every `F_t` is a uniformly bounded finite piecewise-affine function of uniformly bounded variation, repeated one-dimensional summation by parts gives, uniformly in `t`,

\[
\boxed{
\sum_{b_1,b_2}
\frac{\Lambda(b_1)}{b_1}
\frac{\Lambda(b_2)}{b_2}
F_t(\beta_1,\beta_2)
=\ell^2 Q(1+t)+O(\ell),
}
\tag{25}
\]

where `Q` is exactly the continuum geometric kernel integrated in WI-030:

\[
Q(1+t)
=\frac{(1-t)^3}{6}
+\frac{(1-2t)_+^3}{6}.
\tag{26}
\]

Equation (25) supplies the missing rigorous meaning of the paper's phrase “Mertens mass concentrates on pairs of large primes”: not point concentration, but weak convergence of the logarithmic prime-power weight to flat beta measure, with a quantitative discrepancy sufficient for the source geometry.

## 8. WI-032 supplies the universal row law with a bounded offset

WI-032 proved for the same universal `(1,1)` parity-mean object

\[
y_{1,1}(\theta)
=\log\frac1\theta
+\log\frac\pi2-1
+O_\delta(\theta^\delta).
\tag{27}
\]

In particular, on `0<theta<=2pi` the difference

\[
y_{1,1}(\theta)-\log(1/\theta)
\]

is bounded: it converges at zero by (27) and is bounded on every compact interval away from zero by the exact sawtooth series/partial-sum representation. With (1), uniformly for `0<=t<=1`,

\[
\boxed{
y_{1,1}(2\pi e^{-t\ell})=t\ell+O(1).}
\tag{28}
\]

The exact value of `c*` affects only the `O(1)` term and therefore one order below the limiting core, consistent with WI-030.

## 9. The deterministic core limit is `-1/48`

Insert (25) and (28) into the universalized form of (16). The `O(ell)` discrepancy in (25), multiplied by the source prefactor and `y=O(ell)`, contributes `O(1/ell)`. Thus

\[
\begin{aligned}
\operatorname{core}_{\rm univ}(T)
&=-\frac{2\ell^3}{\ell_1^4}
\int_0^1
y_{1,1}(2\pi e^{-t\ell})Q(1+t)\,dt
+O\!\left(\frac1\ell\right)\\
&=-2\frac{\ell^4}{\ell_1^4}
\int_0^1 tQ(1+t)\,dt
+O\!\left(\frac1\ell\right).
\end{aligned}
\tag{29}
\]

WI-030 evaluated the remaining finite integral exactly:

\[
-2\int_0^1tQ(1+t)\,dt
=-\frac1{48}.
\tag{30}
\]

Combining (22), (29), and (30),

\[
\boxed{
\operatorname{core}_{\rm det}(T)
=-\frac1{48}
+O\!\left(\frac1{\log T}\right).
}
\tag{31}
\]

This replaces the source's Richardson-based `-0.0209 +- 0.0026` continuum value and its unwritten universality-collapse rate by an analytic derivation for the deterministic source object. It also agrees with the numerical band, since `-1/48=-0.020833333...`.

## 10. What is still required for a zeta theorem

Equation (31) is **not** yet an unconditional fourth-moment theorem about zeta zeros. The following remain load-bearing and must not be silently imported from the candidate paper:

1. **Structured shifted correlations.** Audit the Matomaki--Radziwill--Tao input, the dispersion-swaps identity, structured-to-full aggregation, and the gluing weight at the exact uniformity/ranges used to replace the actual prime correlations by the singular-series deterministic model.
2. **Remainder ledger.** Interval-certify the finite deterministic/remainder terms and use WI-031's Rankin--Euler theorem for the infinite gamma tail; ensure omitted low zones, taper changes, endpoints, and finite-height charges are all in one consistent normalization.
3. **Consumer interface.** Only after a rigorous bound for the final `R(1)` is obtained may WI-028's scalar consumer be invoked to improve the established simple-critical proportion.

The strategic consequence is nevertheless material. Two items that the public paper itself listed inside N2/CL as computed or unwritten are now removed from the proof budget:

\[
\boxed{
\text{universal }c^*\text{ is exact (WI-032),}
\qquad
\text{deterministic universal collapse is analytic (WI-033).}
}
\]

The remaining uncertainty is concentrated much closer to the genuine zeta-to-arithmetic transport and finite certification layer.

## 11. Prior-art and novelty audit

The logarithmic prime measure and estimates (19), (24) are classical consequences of Mertens's theorems. Weak convergence against bounded-variation test functions is standard summation by parts. Tensor-product `l1` perturbation estimates are elementary. The Yang--Yang source already states the qualitative universal-collapse conclusion and already contains every local gamma factor used above.

Targeted searches of the pinned repository and public sources found no written proof of the collapse using the local estimate (7), no quantitative control of exceptional same-prime-power base pairs as in (21), and no source derivation of (22)--(31). This absence is **not** a priority claim. Mathia records the exact proof reconstruction and its role in shrinking the audit surface.

The finding should be classified as:

- `CLASSICAL-IDENTITY`: Mertens estimates, summation by parts, logarithmic prime measure;
- `LITERATURE+DERIVED`: source zone/gamma formulas and source qualitative collapse claim;
- `EXACT-DERIVED`: local gamma stability (7)--(10), selector cancellation (15), error bounds (20)--(22), and the quantitative collapse (31);
- `NEEDS-AUDIT`: any promotion from the deterministic model to the actual zeta fourth-moment theorem.

## 12. Decisive audit tests

Reject or correct this finding if any of the following fails:

1. derive (2) directly from the two boolean selectors in `m1_suite.py`;
2. verify the exact local tables (5)--(6) using the corrected `_gamma_free_exact` / `gamma_signed_array` logic in `tail_bound.py`;
3. tensor the full and class pieces separately and recover (9);
4. verify the source normalized change of variables leading to (16), including the unordered/symmetrized multiplicity;
5. repeat the prime-power sums in (17)--(21) without replacing `b=p^a` by primes only;
6. prove the uniform discrepancy statement (24) from the prime-power Mertens estimate and perform the two summation-by-parts steps for the actual piecewise-affine `F_t`;
7. combine the exact WI-032 row law with the WI-030 geometry and independently recover `-1/48`;
8. keep the MRT/structured-shift/glue and global remainder layers outside the established conclusion until separately audited.
