# AF-190 — Finite-overlap Euler resonances have a theta fidelity profile

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-189 proves that the first accessible Euler harmonic alone controls the full parity-cluster band discrepancy when the finite-difference order satisfies `m/q^2 -> infinity`. The complementary finite-overlap regime has a different exact limit: neighboring reciprocal resonances survive with order-one weight and combine into a discrete Gaussian, equivalently Jacobi-theta-type, profile.

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
r=e^{-\sigma x}\in(0,1),
\qquad
a=\sigma x.
\tag{1}
\]

Let `\delta\downarrow0`, and let positive integers `q=q_\delta` and `m=m_\delta` satisfy

\[
q_\delta\to\infty,
\qquad
\frac{m_\delta}{q_\delta^2}\longrightarrow\tau\in(0,\infty),
\qquad
m_\delta q_\delta\delta\longrightarrow0.
\tag{2}
\]

Use the same normalized positive parity-split controls as AF-182--AF-189,

\[
\nu_\delta
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta},
\tag{3}
\]

and the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it.
\tag{4}
\]

Put

\[
T_\delta=\frac{\pi}{q_\delta\delta},
\qquad
D_\delta=
\sup_{|t|\le T_\delta}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{5}
\]

For `u\ge0` define

\[
\Phi_{a,\tau}(u)
=
\sum_{n\in\mathbb Z}
\exp\!\left[
-an-
\frac{\pi^2\tau}{8}(n-u)^2
\right]
\tag{6}
\]

and

\[
M(a,\tau)
=
\sup_{0\le u\le1}\Phi_{a,\tau}(u).
\tag{7}
\]

Then

\[
\boxed{
D_\delta
=(2+o(1))
\frac{r^{q_\delta}}{q_\delta}
M(a,\tau).
}
\tag{8}
\]

The profile is finite and satisfies the exact quasi-periodicity

\[
\Phi_{a,\tau}(u+1)=e^{-a}\Phi_{a,\tau}(u),
\tag{9}
\]

so the supremum over all `u\ge0` is already the compact supremum in `(7)`.

For every finite `\tau`,

\[
M(a,\tau)\ge\Phi_{a,\tau}(0)>1,
\tag{10}
\]

whereas

\[
M(a,\tau)\longrightarrow1
\qquad(\tau\to\infty).
\tag{11}
\]

Thus AF-189's single-resonance constant is not merely unproved at finite `m/q^2`: it is genuinely the infinite-separation limit of a nontrivial resonance-overlap profile. Source complexity enters the destination observable through the dimensionless ratio `m/q^2`, and the Euler coefficients bias the otherwise Gaussian resonance comb through the factor `e^{-an}`.

## Exact response and local resonance scaling

Write `q=q_\delta`, `m=m_\delta`, `\theta=t\delta`, and

\[
R_\delta(t)
=
\int F_{\sigma+it}(u)\,d\nu_\delta(u).
\tag{12}
\]

As in AF-188--AF-189,

\[
R_\delta(t)
=
2^{1-m}
\sum_{k\ge1}
\frac{r^k e^{-iktx}}{k}
\left(e^{-k(\sigma+it)\delta}-1\right)^m,
\tag{13}
\]

and with

\[
b_{k,\delta}(\theta)
=
\frac{|1-e^{-k\sigma\delta}e^{-ik\theta}|}{2},
\tag{14}
\]

we have

\[
|R_\delta(t)|
\le
2\sum_{k\ge1}
\frac{r^k}{k}b_{k,\delta}(\theta)^m.
\tag{15}
\]

Condition `(2)` implies `q^3\delta\to0`, hence also `q\delta\to0` and `m\delta\to0`.

Fix `u\ge0`, set

\[
\theta_0=\frac{\pi}{q+u},
\tag{16}
\]

and write `k=q+n` for fixed `n\in\mathbb Z`. Then

\[
k\theta_0-\pi
=
\frac{\pi(n-u)}{q+u}.
\tag{17}
\]

Using

\[
b_{k,\delta}(\theta)^2
=
e^{-k\sigma\delta}\sin^2\frac{k\theta}{2}
+
\frac{(1-e^{-k\sigma\delta})^2}{4},
\tag{18}
\]

and `mq\delta\to0`, the real damping is negligible on this local scale. The Taylor expansion `\log\cos z=-z^2/2+O(z^4)` gives

\[
\boxed{
b_{q+n,\delta}(\theta_0)^m
\longrightarrow
\exp\!\left[-\frac{\pi^2\tau}{8}(n-u)^2\right].}
\tag{19}
\]

At the same time,

\[
\frac{q}{q+n}r^n\longrightarrow r^n=e^{-an}.
\tag{20}
\]

Therefore the normalized magnitude contribution of every fixed neighboring harmonic converges to the corresponding summand of `(6)`.

A particularly transparent band-edge corollary is obtained from `u=0`. For every fixed integer `j\ge1`, the magnitudes of the `k=q-j` and `k=q+j` harmonics relative to the `k=q` harmonic tend respectively to

\[
\boxed{
\exp\!\left[
aj-
\frac{\pi^2\tau}{8}j^2
\right]}
\tag{21}
\]

and

\[
\boxed{
\exp\!\left[
-aj-
\frac{\pi^2\tau}{8}j^2
\right].}
\tag{22}
\]

Hence fixed neighboring resonances vanish relative to `k=q` exactly when `m/q^2\to\infty`. In particular, in the finite-overlap regime the first lower neighbor is individually larger than the `q`-th harmonic whenever

\[
\tau<\frac{8a}{\pi^2}.
\tag{23}
\]

This shows directly that the isolation condition used by AF-189 marks a real change of asymptotic mechanism rather than only a convenient proof hypothesis.

## Uniform upper envelope

It remains to pass from fixed neighboring harmonics to the supremum over the whole band.

By symmetry take `0\le\theta\le\pi/q`. The part `k>3q/2` is always negligible on the scale `r^q/q`, because

\[
\sum_{k>3q/2}\frac{r^k}{k}
=o\!\left(\frac{r^q}{q}\right).
\tag{24}
\]

If `0\le\theta\le\pi/(2q)`, then every `k\le3q/2` stays a fixed angular distance from the first antipodal resonance. Since `m\asymp q^2`, its filter factor is exponentially small in `q^2`; this dominates the at-most-exponential-in-`q` gain from replacing `r^q` by lower Euler coefficients. Thus this half-band contributes `o(r^q/q)`.

Now take

\[
\frac{\pi}{2q}\le\theta\le\frac{\pi}{q},
\qquad
y=\frac{\pi}{\theta}=q+u,
\qquad u\ge0.
\tag{25}
\]

The Gaussian localization estimate used in AF-189 gives, uniformly for `q/2\le k\le3q/2`,

\[
b_{k,\delta}(\theta)^m
\le
\exp[-c_0 m(k\theta-\pi)^2]
\tag{26}
\]

for one fixed `c_0>0`. Since `m/q^2` stays bounded above and below away from zero, `(26)` supplies a summable Gaussian majorant in the offset `n=k-q` around `u=y-q`. Combining that majorant with the Euler factor `r^n` shows two facts.

First, if `u\to\infty`, the normalized magnitude sum tends to zero. Intuitively the first reachable resonance has moved `u` harmonics above `q`, paying the coefficient factor `e^{-au}`, while harmonics remaining near `q` pay a Gaussian off-resonance penalty. More formally, shifting the integer index by `\lfloor u\rfloor` yields a bounded Gaussian lattice sum times `e^{-a\lfloor u\rfloor}`.

Second, on every bounded `u`-interval, `(19)`--`(20)` and the same Gaussian majorant permit dominated convergence. Therefore

\[
\limsup_{\delta\downarrow0}
\frac{q}{2r^q}D_\delta
\le
\sup_{u\ge0}\Phi_{a,\tau}(u).
\tag{27}
\]

Equation `(9)` follows by the index shift `n\mapsto n+1`, so

\[
\sup_{u\ge0}\Phi_{a,\tau}(u)
=
M(a,\tau).
\tag{28}
\]

This proves the upper half of `(8)`.

## Phase alignment makes the magnitude envelope sharp

The triangle-inequality envelope is not automatically attainable because the Euler harmonics carry different phases. Here the continuous vertical band has enough microscopic phase freedom to align them without moving appreciably on the resonance scale.

Ignoring the vanishing real damping for a moment, for `0<k\theta<2\pi`,

\[
e^{-ik\theta}-1
=-2i\,e^{-ik\theta/2}\sin\frac{k\theta}{2}.
\tag{29}
\]

Thus, apart from the common factor `(-i)^m`, the phase of the `k`-th term in `(13)` is

\[
\exp\!\left[-ik\theta
\left(\frac{x}{\delta}+\frac m2\right)\right].
\tag{30}
\]

Set

\[
A_\delta=rac{x}{\delta}+\frac m2.
\tag{31}
\]

Because `m\delta\to0`, the phase-alignment mesh

\[
\theta=\frac{2\pi\ell}{A_\delta},
\qquad \ell\in\mathbb Z,
\tag{32}
\]

has spacing `O(\delta)`. But neighboring reciprocal resonances near index `q` are separated on the much larger `q^{-2}` scale, and

\[
q^2\delta\longrightarrow0.
\tag{33}
\]

Choose `u_*\in[0,1]` maximizing `(7)`, put `\theta_0=\pi/(q+u_*)`, and choose the largest mesh point `(32)` not exceeding `\theta_0`. Call it `\theta_*`. Then `\theta_*\le\pi/q` and

\[
q^2|\theta_* - \theta_0|\longrightarrow0,
\qquad
\frac{\pi}{\theta_*}-q\longrightarrow u_*.
\tag{34}
\]

At `\theta_*`, all zero-damping phases in `(30)` agree exactly. For every fixed local harmonic `k=q+n`, restoring the factor `e^{-k\sigma\delta}` perturbs the phase before taking the `m`-th power by `O(q\delta)`, hence the resulting phase error is

\[
O(mq\delta)=o(1).
\tag{35}
\]

Consequently every fixed block `|n|\le N` adds with asymptotically common phase and with magnitudes converging to `(6)`. The same Gaussian majorant used for the upper bound makes the normalized tail outside `|n|\le N` uniformly small as `N\to\infty`. Therefore

\[
\liminf_{\delta\downarrow0}
\frac{q}{2r^q}D_\delta
\ge
\Phi_{a,\tau}(u_*)
=M(a,\tau).
\tag{36}
\]

Together with `(27)` this proves `(8)`.

The alignment argument is also why a continuous vertical band is materially stronger here than a sparse set of sampled frequencies: it uses a phase mesh of spacing `O(\delta)` inside a resonance window of width `q^{-2}`.

## Theta structure and limiting regimes

Completing the square in `(6)` gives

\[
\Phi_{a,\tau}(u)
=
\exp\!\left[
-au+
\frac{2a^2}{\pi^2\tau}
\right]
\sum_{n\in\mathbb Z}
\exp\!\left[
-\frac{\pi^2\tau}{8}
\left(n-u+\frac{4a}{\pi^2\tau}\right)^2
\right].
\tag{37}
\]

The remaining lattice Gaussian is a standard Jacobi-theta-type sum. No special-function machinery is required for `(8)`; the representation only identifies the finite-overlap constant with a classical object rather than a new transcendental function.

Equation `(10)` follows because the `n=0` summand at `u=0` equals one and all other summands are positive. To prove `(11)`, split `u\in[0,1]` at its nearest endpoint. Away from `0` and `1` every Gaussian term is exponentially small in `\tau`; near `0` the `n=0` term tends uniformly to at most one and all other terms vanish, while near `1` quasi-periodicity bounds the limiting endpoint value by `e^{-a}<1`. Hence the compact supremum tends to one.

Thus the three source-complexity regimes for this exact control family are now qualitatively distinct:

- `m/q^2\to\infty`: isolated first resonance, AF-189, with constant `1` after normalization by `2r^q/q`;
- `m/q^2\to\tau\in(0,\infty)`: finitely overlapping resonance comb with constant `M(a,\tau)>1`;
- smaller `m/q^2`: the present theorem does not apply, and the growing-overlap regime requires a separate scaling analysis.

## Falsification and boundaries

The theorem is deliberately narrow.

- It concerns the AF-182 positive parity-split source pair, not arbitrary clustered measures.
- It uses the Euler local logarithm and its monotone coefficient magnitudes `r^k/k`. Different harmonic weights produce a different biased lattice profile.
- It uses a continuous vertical band. Discrete sampling can miss the phase-alignment mesh and needs an aliasing or Diophantine analysis.
- The condition `mq\delta\to0` removes real-damping effects at the resonance scale. If that quantity has a nonzero limit, the local profile acquires an additional attenuation and phase term.
- The result is a sharp forward discrepancy theorem for one matched-control family. It is not a stable inverse theorem for all generalized-prime systems and does not establish rational-prime specificity.
- The `\tau\downarrow0` transition is not covered. In that regime the effective number of overlapping harmonics grows and the fixed discrete-Gaussian profile is no longer the correct uniform limit without further rescaling.

These boundaries matter for the line-wide fidelity program: the destination kernel's internal harmonic architecture, the source-complexity scale, the real-damping scale, and the observation topology all enter the recovery profile separately.

## Prior art and novelty assessment

The ingredients sit inside established harmonic-analysis and super-resolution mathematics. David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is foundational prior art for bandwidth-limited recovery of sparse sources. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, gives sharp clustered partial-Fourier conditioning bounds whose exponents depend on local cluster size. NIST DLMF Chapter 20, especially §20.2, records the classical Jacobi theta series and quasi-periodic structure to which `(37)` belongs.

A targeted search over clustered Fourier/super-resolution, finite-difference, Euler-logarithm, and theta-function terminology did not identify an authoritative source stating the specialized asymptotic `(8)` for this Euler logarithm and the AF-182 parity controls. That search is not evidence of priority, and no novelty claim is made. The durable result is the exact closure of the finite-overlap boundary left explicit by AF-189.

## Dependencies and evidence boundary

The proof depends on the exact AF-188/AF-189 harmonic response `(13)` and the AF-189 Gaussian localization mechanism, but not on AF-189's assumption `m/q^2\to\infty`. The new ingredients are the finite Gaussian local limit `(19)`, the compactness/quasi-periodicity reduction `(27)`--`(28)`, and the microscopic phase-alignment construction `(29)`--`(36)`.

No numerical experiment is used as evidence. Numerical checks were not needed for the claim. No RH consequence, rational-prime uniqueness statement, or general recovery theorem follows from this finding.