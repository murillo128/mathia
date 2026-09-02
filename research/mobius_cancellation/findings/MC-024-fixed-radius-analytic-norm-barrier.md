# MC-024 — Fixed-radius analytic norms are exponent-neutral under Huxley–Watt scale doubling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`.

## Claim

The full analytic-germ continuation left open by `MC-023` has two exact quantitative barriers before it can become a bootstrap mechanism.

First, after reciprocal-zeta centering the Huxley–Watt scale-doubling map is genuinely quadratic in the analytic state. On nested fixed disks, the regularized nonlinear term obeys an ordinary quadratic holomorphic norm estimate. Because the scale changes from `N` to `N^2`, a quadratic bound takes a power law `N^{-alpha}` exactly to

\[
N^{-2\alpha}=(N^2)^{-\alpha}.
\]

Thus a scale-uniform analytic-norm estimate of the form “next state is bounded by a constant times the square of the current state” is **power-exponent neutral**. It can improve constants but cannot bootstrap an exponent `alpha` to any larger exponent.

Second, a power-decaying norm on a fixed complex neighborhood of `t=0` necessarily controls points with negative real `t`, hence weighted Möbius Dirichlet sums to the left of `Re(s)=1`. If the norm decays faster than the leftward displacement, it already forces a fixed zero-free half-plane for zeta. Therefore a fixed-radius analytic norm cannot be treated as a cheap local-to-`s=1` input merely because its center is the pole at `s=1`.

The non-circular analytic continuation of `MC-023` is consequently narrowed to a shrinking-neighborhood or otherwise one-sided/structured control together with **additional signed arithmetic gain** beyond generic quadratic norm closure. A shrinking radius of order `1/log N` avoids a fixed power displacement and incurs only logarithmic Cauchy losses, but the exponent-neutrality obstruction remains.

This finding does not rule out the analytic family. It rules out the specific hope that an ordinary fixed-radius Banach/Hardy/sup-norm contraction for the centered Huxley–Watt germ, with only quadratic scale-uniform control, would by itself amplify a weak power-saving exponent into the RH exponent.

## 1. The centered nonlinear map is exactly homogeneous of degree two

Retain the notation of `MC-023`:

\[
F_N(t)=\sum_{n\le N}\frac{\mu(n)}{n^{1+t}},
\qquad
f(t)=\frac1{\zeta(1+t)},
\]

\[
A_N(t)=N^t\bigl(F_N(t)-f(t)\bigr),
\]

and

\[
B_N(t)=\sum_{m,n\le N}\mu(m)\mu(n)
\kappa_t\!\left(\frac{N^2}{mn}\right).
\]

The exact renormalized scale-doubling identity is

\[
A_{N^2}(t)
=
\frac{A_N(0)^2}{t}
-
\frac{A_N(t)^2}{f(t)}
-
\frac{B_N(t)}{N^2}.
\tag{1}
\]

Define the regularized nonlinear operator

\[
\mathcal Q[A](t)
:=
\frac{A(0)^2}{t}-\frac{A(t)^2}{f(t)}.
\tag{2}
\]

Since `f(t)=t h(t)` with `h` holomorphic and `h(0)=1`, there is a sufficiently small disk on which `h` is holomorphic and nonzero. On that disk,

\[
\mathcal Q[A](t)
=
\frac{A(0)^2-A(t)^2/h(t)}{t}.
\tag{3}
\]

The numerator vanishes at `t=0`, so `Q[A]` is holomorphic there. More importantly,

\[
\boxed{\mathcal Q[cA]=c^2\mathcal Q[A]}
\tag{4}
\]

for every scalar `c`. The reciprocal-zeta centering that removed the linear state in `MC-023` has therefore made the state-transfer term exactly degree two, not merely asymptotically quadratic.

## 2. Nested-disk sup norms give a genuine quadratic estimate

Choose fixed radii

\[
0<r<R
\]

inside a disk on which `h` is holomorphic and nonzero. Write

\[
\|A\|_R=\sup_{|t|\le R}|A(t)|.
\]

Set

\[
G_A(t)=\frac{A(t)^2}{h(t)}.
\]

Then `G_A(0)=A(0)^2` and (3) is the negative difference quotient

\[
\mathcal Q[A](t)=-\frac{G_A(t)-G_A(0)}{t}.
\tag{5}
\]

For `|t|<=r`, the fundamental theorem along the segment from `0` to `t` gives

\[
|\mathcal Q[A](t)|\le \sup_{|z|\le r}|G_A'(z)|.
\]

Cauchy's derivative estimate on the larger disk yields

\[
\sup_{|z|\le r}|G_A'(z)|
\le
\frac{1}{R-r}\sup_{|w|\le R}|G_A(w)|.
\]

Hence

\[
\boxed{
\|\mathcal Q[A]\|_r
\le
C_{r,R}\|A\|_R^2,
\qquad
C_{r,R}=\frac{\|1/h\|_R}{R-r}.
}
\tag{6}
\]

No number-theoretic estimate enters (6); it is an elementary holomorphic consequence of the exact regularization.

Substituting (6) into (1) gives

\[
\|A_{N^2}\|_r
\le
C_{r,R}\|A_N\|_R^2
+
\frac{\|B_N\|_r}{N^2}.
\tag{7}
\]

This makes precise what an ordinary analytic-norm closure would have to improve.

## 3. Quadratic scale doubling preserves, rather than improves, a power exponent

Suppose for some `alpha>0` one has at scale `N`

\[
\|A_N\|_R\le C N^{-\alpha}
\tag{8}
\]

and the normalized residual is controlled at the corresponding quadratic scale,

\[
\frac{\|B_N\|_r}{N^2}
\le C_B N^{-2\alpha}.
\tag{9}
\]

Then (7) gives

\[
\|A_{N^2}\|_r
\le
(C_{r,R}C^2+C_B)N^{-2\alpha}
=
(C_{r,R}C^2+C_B)(N^2)^{-\alpha}.
\tag{10}
\]

Thus the exponent is unchanged.

This is not an artifact of the sup norm. Whenever a source-natural state norm supports a scale-uniform estimate

\[
\|\mathcal Q[A]\|\le C\|A\|^2
\tag{11}
\]

and the residual is no larger than the same quadratic scale, the map `N -> N^2` converts the state exponent by

\[
\alpha\longmapsto \frac{2\alpha}{2}=\alpha.
\]

Even a strict contraction constant smaller than `1` changes only the multiplicative constant under repeated squaring. It does not create a larger power exponent.

Therefore an exponent bootstrap must contain information absent from a generic quadratic contraction. For a proposed improved exponent `beta>alpha`, at least one of the following must occur:

- the signed nonlinear term is smaller than its generic quadratic size by a factor of order `N^{-2(beta-alpha)}`;
- the residual `B_N/N^2` carries such a gain and is coupled to the nonlinear term without losing it;
- an independent arithmetic relation removes the leading quadratic contribution;
- or the effective state transfer has genuinely higher-than-quadratic power after all normalizations.

Simply proving boundedness or contractivity of the same quadratic map in a nicer analytic norm is not enough.

## 4. A fixed-radius left edge already contains zero-free information

The second obstruction concerns what it means to control the analytic state on a fixed disk.

Fix `delta>0` inside the admissible disk and evaluate at the negative real point `t=-delta`. From the definition of `A_N`,

\[
F_N(-\delta)-f(-\delta)
=N^{\delta}A_N(-\delta).
\tag{12}
\]

Suppose an analytic norm controlling point evaluation gives

\[
|A_N(-\delta)|=O(N^{-\alpha})
\qquad\text{with}\qquad
\alpha>\delta.
\tag{13}
\]

Then

\[
F_N(-\delta)
=\sum_{n\le N}\frac{\mu(n)}{n^{1-\delta}}
\longrightarrow
f(-\delta)=\frac1{\zeta(1-\delta)}.
\tag{14}
\]

Hence the Möbius Dirichlet series converges at the real abscissa `sigma=1-delta`. Standard Dirichlet-series theory then gives convergence and holomorphy throughout

\[
\Re(s)>1-\delta.
\]

On the overlap `Re(s)>1` the sum equals `1/zeta(s)`, so the identity theorem identifies the continued Dirichlet sum with `1/zeta(s)` on the whole connected half-plane. Consequently

\[
\boxed{
\zeta(s)\ne0
\quad\text{for}\quad
\Re(s)>1-\delta.
}
\tag{15}
\]

Equivalently, Kronecker's lemma applied to the convergent series in (14) gives the arithmetic consequence

\[
M(N)=o(N^{1-\delta}).
\tag{16}
\]

Thus polynomial decay on a fixed analytic neighborhood is not merely local regularity near the pole. Once its decay exponent beats the neighborhood's leftward displacement, it already implies a fixed power-saving/zero-free region.

At the full critical scale there is an even simpler boundary already recorded in `MC-020`: `A_N(0)=H(N)`, and the bound `H(N)=O_epsilon(N^{-1/2+epsilon})` is itself RH-equivalent. The point of (12)–(16) is different: even **subcritical** fixed-radius analytic decay can carry nontrivial zero-free information through the negative-`t` edge.

## 5. Shrinking neighborhoods avoid the fixed-strip import but not exponent neutrality

The preceding argument suggests the natural non-circular analytic regime. Let the radius shrink, for example

\[
r_N\asymp \frac{c}{\log N}.
\tag{17}
\]

Then for `|t|<=r_N` and `n<=N`,

\[
|n^{-t}|\le e^{c},
\]

so the analytic perturbation changes the original reciprocal Möbius weights only by a bounded factor rather than by a fixed power of `n`. The leftmost point corresponds to

\[
\Re(s)=1-O(1/\log N),
\]

not to a fixed zero-free half-plane.

Using two comparable shrinking radii `r_N<R_N` with

\[
R_N-r_N\asymp \frac1{\log N},
\]

the Cauchy constant in (6) costs only

\[
C_{r_N,R_N}=O(\log N)
\tag{18}
\]

apart from the uniformly bounded local factor `1/h`. Such logarithmic losses are absorbable into `N^epsilon` at an RH-scale exponent.

So shrinking germ control is not killed by the fixed-radius zero-free argument. But (4) is unchanged: the nonlinear state transfer remains exactly quadratic, and a logarithmic Cauchy loss certainly does not create the missing polynomial gain. The surviving problem is therefore sharply arithmetic rather than functional-analytic:

> derive an `N`-dependent signed gain in the coupled nonlinear/residual term from information genuinely weaker than the target exponent.

This is a stricter continuation criterion than “find a norm in which the analytic map contracts.”

## 6. Prior art and novelty boundary

The parent scale-doubling identity is due to M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their theorem already allows arbitrary totally multiplicative `g`; `MC-023` specialized it to `g_t(n)=n^{-1-t}` and derived the centered germ recursion used here.

Cauchy derivative estimates, abscissae of convergence for Dirichlet series, Abel/partial summation, Kronecker's lemma, and the link between Möbius partial-sum exponents and zero-free half-planes are classical analytic-number-theory tools; standard references include Montgomery and Vaughan, *Multiplicative Number Theory I: Classical Theory*, especially its Dirichlet-series and zeta-zero chapters. No novelty is claimed for any of those ingredients.

A targeted search combining the Huxley–Watt identity with weighted Möbius `n^{-s}` specializations, analytic norms, scale doubling, and zero-free-region language located the original general identity and standard Möbius/Dirichlet-series zero-free principles, but no authoritative source explicitly presenting the exponent-neutrality and fixed-radius norm audit above. Absence from that search is not evidence of novelty. The durable contribution is the exact negative test for the specific active Mathia continuation of `MC-023`.

## 7. Consequence for the research line

`MC-023` left two broad possibilities: control the complete analytic state in a strong norm, or find an independent finite closure relation. The first possibility is now materially narrower.

A fixed-radius norm is dangerous in two independent ways: critical control already contains the RH-equivalent central harmonic mode, while sufficiently strong subcritical decay at a negative-`t` point imports a fixed zero-free half-plane. More importantly, even setting circularity aside, ordinary quadratic norm closure is algebraically incapable of improving a power exponent under the exact `N -> N^2` scaling.

The useful analytic target is therefore not a generic contraction theorem. It is a theorem that exhibits **strict signed scale gain** in

\[
\mathcal Q[A_N](t)-\frac{B_N(t)}{N^2}
\]

on a shrinking germ or another representation that does not presuppose a fixed zero-free strip. A matched multiplicative comparator for which both pieces remain of generic quadratic size would kill a proposed gain; a positive route must identify the Möbius-specific relation that makes their coupled sum smaller by a genuine power of `N`.
