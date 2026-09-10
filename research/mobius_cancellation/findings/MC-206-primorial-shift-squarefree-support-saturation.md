# MC-206 — Primorial shifts reduce sign/support relation to sparse square-defect sampling

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CANDIDATE-NEW-STRUCTURE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-205` identifies the centered mixed shift term

\[
K_w
=
\sum_a\sum_j\sum_{h\ne0}w_hu_{a,j}v_{a,j+h}
\]

as the genuinely labelled-site information that survives after the principal and class-support modes are separated. For arbitrary ternary source arrays that is a real representation escape. On the actual logarithmic-primorial Möbius source, however, the first sign-times-squarefree-support shift family has a much sharper specialization: **its relational information is supported entirely on the sparse squarefree-defect set.**

Work at the complete block and notation of `MC-205`,

\[
X=Nq,
\qquad
q=q_y=\prod_{p\le y}p,
\qquad
y=c\log X,
\qquad 0<c<\frac12,
\]

with reduced classes `a mod q`,

\[
x_{a,j}=\mu(a+jq),
\qquad
z_{a,j}=x_{a,j}^2,
\qquad
0\le j<N.
\]

Put

\[
A_a=\sum_jx_{a,j},
\qquad
B_a=\sum_jz_{a,j},
\qquad
S=\sum_aA_a,
\qquad
Q=\sum_aB_a,
\qquad
\phi=\varphi(q),
\]

and define the squarefree-hole field

\[
\delta_{a,j}:=1-z_{a,j}\in\{0,1\},
\qquad
D:=\sum_{a,j}\delta_{a,j}=N\phi-Q.
\tag{1}
\]

For each nonzero cyclic shift `h`, define the signed defect sample

\[
\Delta_h
:=
\sum_a\sum_jx_{a,j}\delta_{a,j+h},
\tag{2}
\]

where `j+h` is taken modulo `N`. For weights `w_h`, set

\[
R_w:=\sum_{h\ne0}w_h,
\qquad
\Delta_w:=\sum_{h\ne0}w_h\Delta_h.
\tag{3}
\]

Then the mixed cyclic statistic from `MC-205` satisfies the exact identity

\[
\boxed{
T_w
=(w_0+R_w)S-\Delta_w.
}
\tag{4}
\]

Combining `(4)` with `MC-205`'s exact decomposition

\[
T_w
=\left(w_0+R_w\frac{Q}{\phi N}\right)S
+\frac{R_w}{N}C_{1,2}
+K_w
\]

gives

\[
\boxed{
K_w
=R_w\left(1-\frac{Q}{\phi N}\right)S
-\frac{R_w}{N}C_{1,2}
-\Delta_w.
}
\tag{5}
\]

Moreover every shift is a permutation of the target sites inside each class, so

\[
|\Delta_h|\le D,
\qquad
\boxed{
|\Delta_w|\le D\sum_{h\ne0}|w_h|.
}
\tag{6}
\]

This has two immediate consequences.

First, for a pure off-diagonal mean-zero shift filter,

\[
w_0=0,
\qquad R_w=0,
\]

one has

\[
\boxed{
T_w=K_w=-\Delta_w,
\qquad
|K_w|\le D\sum_{h\ne0}|w_h|.
}
\tag{7}
\]

Thus a small mean-zero relational signal can arise **without any Möbius sign cancellation at all**: it is automatically small relative to the full pre-sieved population simply because it only sees sites whose shifted partner fails squarefreeness.

Second, for a single nonzero shift,

\[
\boxed{
K_h
=\left(1-\frac{Q}{\phi N}\right)S
-\frac1N C_{1,2}
-\Delta_h.
}
\tag{8}
\]

So the first source-aligned escape left open by `MC-205` is substantially narrower than an arbitrary mixed shift correlation. After the old principal/support bookkeeping is removed, its only new arithmetic content is the signed sampling of squarefree holes.

`MC-201` already proves that in this same complete logarithmic-primorial block

\[
\frac{D}{\phi N}
=1-\frac{Q}{\phi N}
\sim\frac1{y\log y}.
\tag{9}
\]

Hence the defect population is logarithmically sparse but not fixed-power sparse. At `y=c log X`, the trivial bound `(7)` is still an exponent-one bound up to logarithms, far above the RH-scale `X^{1/2+\varepsilon}` target. The representation therefore creates neither a free power saving nor a no-go theorem: it identifies a more precise arithmetic object that would actually have to cancel.

No improved estimate for `S`, `M(X)`, `K_w`, or the Riemann zero set is claimed.

## 1. Exact support-saturation identity

For every site,

\[
z_{a,j}=1-\delta_{a,j}.
\]

Since `x_{a,j}z_{a,j}=x_{a,j}^3=x_{a,j}`, the diagonal part of `T_w` is `w_0S`. For a nonzero cyclic shift,

\[
\sum_{a,j}x_{a,j}z_{a,j+h}
=
\sum_{a,j}x_{a,j}(1-\delta_{a,j+h})
=S-\Delta_h.
\tag{10}
\]

Weighting `(10)` and summing over `h` proves `(4)`. Equation `(5)` is then just subtraction of the `MC-205` principal/covariance decomposition.

For fixed `h`, the map `(a,j) -> (a,j+h)` permutes all `N phi` target sites. Therefore exactly `D` target positions have `delta=1`, and each contributes at most one in absolute value to `Delta_h`. This proves `(6)` without any number-theoretic estimate.

The same argument is valid for any ternary array. The arithmetic specialization enters through `(9)`: logarithmic primorial pre-sieving makes the support-hole fraction small because every site is already coprime to every prime `p<=y`.

## 2. Why the holes are large-prime-square defects

For every reduced class `a mod q`,

\[
(a+jq,q)=1.
\]

Thus a nonsquarefree site `m=a+jq` cannot be divisible by `p^2` for any prime `p<=y`; all such primes divide `q` and do not divide `m` even once. Consequently

\[
\delta_{a,j}=1
\]

implies that `m` is divisible by `p^2` for some prime `p>y`.

This is the same sparse defect field isolated in `MC-201`, but `(5)` shows a new role for it: **the entire labelled-site correction of the bilinear sign/support shift family is a signed probe of translated copies of that defect field.** Full permutation symmetry erased source order in `MC-204`; cyclic shifts restore order, but for this particular second field they restore it only through where the rare large-prime-square holes occur.

The distinction matters. A theorem that merely proves `K_w=o(N phi)` or another logarithmic relative saving may be measuring support sparsity rather than Möbius orientation. A genuine cancellation theorem must beat the trivial defect-count scale `(6)` by using the signs `x_{a,j}` on those defect-selected sites.

## 3. Linear shifts expose the exact arithmetic bill

The ordinary non-wrapped shift has a direct integer interpretation. For `h>0`, define

\[
\Delta_h^{\mathrm{lin}}
:=
\sum_{\substack{n\le X-hq\\(n,q)=1}}
\mu(n)\left(1-\mu^2(n+hq)\right).
\tag{11}
\]

Using the classical square-divisor identity

\[
\mu^2(m)=\sum_{d^2\mid m}\mu(d),
\]

one gets exactly

\[
\boxed{
\Delta_h^{\mathrm{lin}}
=-
\sum_{\substack{d>y\\(d,q)=1\\d^2\le X}}
\mu(d)
\sum_{\substack{n\le X-hq\\(n,q)=1\\n\equiv-hq\pmod{d^2}}}
\mu(n).
}
\tag{12}
\]

The restriction `d>y` is forced, not imposed: if a nontrivial square divisor of `n+hq` contained a prime `p<=y`, then `p` would divide both `q` and the reduced-class integer `n+hq`, impossible.

Equation `(12)` identifies the live source problem precisely. Improving the defect bound means obtaining cancellation for Möbius on a structured family of square-modulus progressions, followed by enough cancellation or summability across the square-divisor variable `d`. This is materially sharper than asking for a generic fixed-shift correlation estimate.

The cyclic and linear observables differ only by the boundary already quantified in `MC-205`: for a bandwidth `H<N/2`,

\[
|T_w^{\mathrm{lin}}-T_w^{\mathrm{cyc}}|
\le
\phi\sum_{0<|h|\le H}|h|\,|w_h|.
\tag{13}
\]

Thus narrow source-aligned kernels can be studied through `(12)` without losing track of the exact cyclic decomposition.

## 4. Prior-art audit and what it does not provide

The ingredients used to derive `(4)`--`(12)` are classical: the ternary identity `x^3=x`, the squarefree indicator `mu^2`, square-divisor inclusion-exclusion, and elementary permutation bookkeeping. No novelty is claimed for those ingredients or for the statement that primorial pre-sieving removes small-prime square divisors.

The unsigned support side is already well inside established squarefree-distribution theory. `MC-201` records the elementary reduced-class estimate and the much stronger smooth-modulus results of Alexander P. Mangerel, *Squarefree Integers in Arithmetic Progressions to Smooth Moduli*, Forum of Mathematics, Sigma 9 (2021), e72, DOI `10.1017/fms.2021.67`, arXiv `2008.11163`. That work obtains power-saving asymptotics for squarefree integers in reduced classes to sufficiently smooth squarefree moduli through a range far beyond the logarithmic primorial used here. It strengthens the conclusion that unsigned support regularity is not the missing sign mechanism.

For the signed inner sums in `(12)`, Xuancheng Shao, *Gowers norms of multiplicative functions in progressions on average*, Algebra & Number Theory 11 (2017), 961--982, arXiv `1607.01814`, proves in particular averaged progression control for Möbius over moduli up to `X^(1/2-sigma)` and arbitrary coprime residue classes. This is close in language but does not discharge `(12)`: the relevant moduli are the structured squares `d^2`, the residue `-hq mod d^2` need not be coprime when `(d,h)>1`, the source is simultaneously restricted by `(n,q)=1`, and the sum over a wide family of `d` must preserve a fixed-power gain.

William D. Banks and Igor E. Shparlinski, *Sums with the Möbius function twisted by characters with powerful moduli*, Transactions of the American Mathematical Society 373 (2020), 249--272, DOI `10.1090/tran/7914`, arXiv `1801.10276`, provide another adjacent powerful-modulus theory. Their character-twisted estimates and associated zero-free-region machinery show that square/powerful moduli are not an untouched analytic setting, but they do not give the aggregate square-divisor progression estimate required by `(12)` without additional work and hypotheses.

Classical squarefree-pattern results going back to Mirsky control joint occurrence of squarefree values at fixed additive patterns. Those results concern unsigned `mu^2` patterns; they do not supply cancellation of the Möbius sign sampled on the complement of a shifted squarefree pattern, especially for the growing primorial shifts `hq` considered here.

The literature audit therefore supports only a frontier classification, not a novelty claim: the exact reduction `(5)` and `(12)` says which established analytic languages are relevant and what extra uniformity would be needed before they can help the Mertens target.

## 5. Consequence for the active frontier

The broad lesson of `MC-203`--`MC-205` survives but becomes more selective.

- Permutation-invariant support statistics remain too coarse.
- Nonuniform cyclic shifts do retain source order abstractly.
- For the first mixed field `z=x^2`, however, the restored order is carried only by translated large-prime-square holes.
- Mean-zero shift filters can suppress the principal mode while remaining small for the trivial reason `(7)`; that smallness must not be misread as sign cancellation.

The next viable theorem in this branch is therefore not another choice of shift kernel. It is one of two concrete things: either prove a power-saving estimate for the signed defect transform `(12)` (or for a weighted family of such transforms) that survives the square-modulus, residue, pre-sieving, and `d`-summation losses, or replace the squarefree-support field by a source-aligned relation whose nonprincipal variation is not already confined to an exponent-one sparse defect set.

A decisive positive result would show, for a nontrivial range of `h` and `y=c log X`, a bound for `Delta_h^{lin}` or an appropriate weighted aggregate that beats the defect-count scale by a fixed power and transfers through `(5)` with all boundary terms controlled. A decisive negative result would construct a matched multiplicative source or prove an analytic barrier showing that the available progression technology cannot produce such a gain in the required square-modulus family.