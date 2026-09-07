# AF-187 — Euler parity clusters become residue-class harmonic filters at reciprocal bandwidth

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-182--AF-186 show that high-order positive parity-split generalized-prime clusters can remain at exact source distance `W_1=delta` while smooth bounded-band observations become arbitrarily flat. AF-186 deliberately leaves open the converse question: for an actual kernel, when does additional observation structure prevent the optimized derivative-envelope obstruction from being attained?

For the Euler logarithm there is an exact answer at every fixed reciprocal-band fraction. The same finite-difference cancellation that hides a cluster at low bandwidth becomes a **harmonic residue-class filter** once the vertical phase accumulated across one source spacing is of reciprocal order. The prime-power harmonics of the Euler logarithm then supply an intrinsic recovery channel.

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
q\in\mathbb N,
\tag{1}
\]

and let `delta -> 0`. Let `m=m_delta` be any positive-integer schedule satisfying

\[
\boxed{
m_\delta\longrightarrow\infty,
\qquad
m_\delta\delta\longrightarrow0.
}
\tag{2}
\]

Use the normalized parity-split controls of AF-182,

\[
\nu_\delta
:=
\mu_{+,\delta}-\mu_{-,\delta}
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta}.
\tag{3}
\]

They are differences of positive probability measures and satisfy

\[
\boxed{
W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta,
}
\tag{4}
\]

while their complete support has diameter `m_delta delta -> 0`.

For

\[
F_s(u)=-\log(1-e^{-su}),
\qquad
s=\sigma+it,
\tag{5}
\]

define the vertical-band discrepancy

\[
D_T(\delta)
=
\sup_{|t|\le T}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{6}
\]

Then for every fixed integer `q>=1`, if

\[
\boxed{
T(\delta)\ge \frac{\pi}{q\delta}
}
\tag{7}
\]

for all sufficiently small `delta`, there are frequencies `t_delta` inside the declared band for which

\[
\boxed{
(-1)^{m_\delta}
\int F_{\sigma+i t_\delta}(u)\,d\nu_\delta(u)
\longrightarrow
\frac{2}{q}
\operatorname{artanh}\!\left(e^{-q\sigma x}\right).
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\liminf_{\delta\downarrow0}D_T(\delta)
\ge
\frac1q
\log\!\frac{1+e^{-q\sigma x}}{1-e^{-q\sigma x}}
>0.
}
\tag{9}
\]

Thus

\[
\boxed{
\frac{D_T(\delta)}
{W_1(\mu_{+,\delta},\mu_{-,\delta})}
\longrightarrow\infty
\quad\text{along the witnessing frequencies.}
}
\tag{10}
\]

The adaptive parity cluster therefore **ceases to be an asymptotically invisible control** at every fixed reciprocal-band fraction `pi/q`. More generally, if

\[
\liminf_{\delta\downarrow0}\delta T(\delta)>0,
\tag{11}
\]

choose one fixed `q` with `pi/q` below that liminf. Then the same conclusion holds with the positive constant in `(9)`.

This does not prove stable inversion of the full generalized-prime source class. It proves a sharper and more local statement: the explicit adaptive cluster mechanism behind AF-182--AF-186 cannot by itself certify instability once the Euler observation reaches any **fixed positive multiple of the reciprocal-separation scale**.

## Exact harmonic-residue mechanism

The key point is not a derivative lower bound. It is the exact prime-power harmonic expansion

\[
F_s(u)
=
\sum_{k\ge1}\frac{e^{-ksu}}{k},
\qquad \Re(s)>0,
\tag{12}
\]

which converges absolutely for every fixed `u>0`.

AF-182 gives the exact finite-difference response

\[
\int F_s(u)\,d\nu_\delta(u)
=
2^{1-m_\delta}
\sum_{k\ge1}
\frac{e^{-ksx}}{k}
\left(e^{-ks\delta}-1\right)^{m_\delta}.
\tag{13}
\]

The normalized finite difference acts on harmonic `k` through the multiplier

\[
2^{1-m}
\left(e^{-ks\delta}-1\right)^m.
\tag{14}
\]

At small vertical phase this multiplier is the high-order cancellation used in AF-182--AF-186. At a reciprocal phase it has a different interpretation: after normalization, its magnitude is asymptotically

\[
2\left|\sin\frac{k\theta}{2}\right|^m,
\qquad
\theta=t\delta.
\tag{15}
\]

For large `m`, this is concentrated on harmonics for which `k theta` is an odd multiple of `pi`. High cancellation order therefore creates a narrow harmonic comb rather than uniform invisibility.

## Phase-aligned witness inside the band

Set

\[
N_\delta
=
\left\lfloor\frac{x}{2q\delta}\right\rfloor,
\qquad
 t_\delta
=
\frac{2\pi N_\delta}{x}.
\tag{16}
\]

For sufficiently small `delta`, `N_delta>=1`, and by construction

\[
0<t_\delta
\le
\frac{\pi}{q\delta}.
\tag{17}
\]

Hence `(7)` guarantees that `t_delta` is observable. It also aligns every Euler harmonic at the base point:

\[
e^{-ik t_\delta x}=1
\qquad(k\ge1).
\tag{18}
\]

Writing

\[
\theta_\delta=t_\delta\delta,
\tag{19}
\]

one has

\[
\theta_\delta\longrightarrow\frac\pi q,
\qquad
\left|q\theta_\delta-\pi\right|
<\frac{2\pi q\delta}{x}.
\tag{20}
\]

Put `r=e^{-sigma x}` and define

\[
z_{k,\delta}
=
\frac{1-e^{-k\sigma\delta}e^{-ik\theta_\delta}}{2}.
\tag{21}
\]

Using `(18)`, equation `(13)` becomes

\[
\boxed{
(-1)^{m_\delta}
\int F_{\sigma+i t_\delta}\,d\nu_\delta
=
2\sum_{k\ge1}\frac{r^k}{k}
 z_{k,\delta}^{m_\delta}.
}
\tag{22}
\]

For every `k` and `delta`,

\[
|z_{k,\delta}|
\le
\frac{1+e^{-k\sigma\delta}}2
\le1.
\tag{23}
\]

Thus the summands in `(22)` are dominated by the summable sequence `2r^k/k`.

Now fix `k`. From `(20)`,

\[
z_{k,\delta}
\longrightarrow
\frac{1-e^{-ik\pi/q}}2.
\tag{24}
\]

There are two cases.

### Odd multiples of `q` survive

If

\[
k=(2\ell+1)q,
\tag{25}
\]

then the limit in `(24)` is exactly `1`. More precisely,

\[
z_{k,\delta}=1+O_k(\delta).
\tag{26}
\]

Condition `m_delta delta -> 0` therefore gives

\[
z_{k,\delta}^{m_\delta}\longrightarrow1.
\tag{27}
\]

### Every other harmonic is removed

If `k` is not an odd multiple of `q`, then

\[
\left|
\frac{1-e^{-ik\pi/q}}2
\right|
=
\left|\sin\frac{k\pi}{2q}\right|
<1.
\tag{28}
\]

Since `m_delta -> infinity`, equations `(24)` and `(28)` imply

\[
z_{k,\delta}^{m_\delta}\longrightarrow0.
\tag{29}
\]

Dominated convergence in `(22)` now yields

\[
\begin{aligned}
(-1)^{m_\delta}
\int F_{\sigma+i t_\delta}\,d\nu_\delta
&\longrightarrow
2\sum_{\ell\ge0}
\frac{r^{(2\ell+1)q}}{(2\ell+1)q}\\
&=
\frac{2}{q}\operatorname{artanh}(r^q),
\end{aligned}
\tag{30}
\]

which is `(8)`.

The proof identifies the retained information exactly: at phase `theta=pi/q`, high-order differencing projects the Euler harmonic ladder asymptotically onto the residue class

\[
\boxed{k\equiv q\pmod{2q}.}
\tag{31}
\]

The surviving constant is not supplied by an external mark. It is already present in the prime-power repetition built into the Euler logarithm.

## General Laplace-series form

The mechanism is not peculiar to the coefficient `1/k`. Suppose instead that an observation has an absolutely convergent harmonic expansion at the declared base point,

\[
G_s(u)
=
\sum_{k\ge1}a_k e^{-ksu},
\qquad
\sum_{k\ge1}|a_k|e^{-k\sigma x}<\infty.
\tag{32}
\]

For the same controls and phase-aligned frequencies, the identical argument gives

\[
(-1)^{m_\delta}
\int G_{\sigma+i t_\delta}\,d\nu_\delta
\longrightarrow
2\sum_{\ell\ge0}
 a_{(2\ell+1)q}
 e^{-(2\ell+1)q\sigma x}.
\tag{33}
\]

Thus the reusable object is the **odd-`q` harmonic residue projection** induced by a high-order parity finite difference at reciprocal phase `pi/q`.

Equation `(33)` also gives the falsification test for purported recovery. If the selected residue-class sum vanishes because of coefficients, symmetry, or cancellation in another kernel, reciprocal phase alone does not force visibility. The Euler case avoids that degeneracy because all coefficients `a_k=1/k` are positive.

## Exact controls and boundary checks

### This is not an exact source-recovery theorem

The limit `(8)` separates the specific matched pair. It does not show that all generalized-prime systems are stably recoverable from bandwidth `pi/(q delta)`, nor does it bound a global inverse condition number.

A different source pair can still exploit another cancellation mechanism. The conclusion is only that the AF-182 parity family is no longer a valid asymptotic collision at the declared reciprocal scale.

### The result requires growing cancellation order

For fixed `m`, non-resonant harmonics in `(22)` do not disappear. Their behavior is already covered by AF-183's fixed-order expansion. The residue-class projection is the genuinely growing-order limit `m_delta -> infinity`.

### Locality remains intact

Condition `m_delta delta -> 0` is exactly the shrinking-support condition emphasized by AF-184--AF-186. The positive controls continue to collapse to the same source point. Recovery is not obtained by allowing the cluster to spread macroscopically.

### The base-point alignment is intrinsic to a continuous vertical band

The witness uses the supremum over all `|t|<=T` to choose `t_delta` with `t_delta x in 2pi Z`. A discretely prescribed frequency grid may not contain such a point. Its Diophantine/aliasing fidelity must be analyzed separately, as AF-029 already demonstrates for lattice modulation families.

### Prime powers matter

If the observation retained only the primitive `k=1` harmonic, only `q=1` could survive this argument. The fact that every fixed `q` has a positive residue channel is a consequence of the complete Euler local-factor series over repetitions `k>=1`.

This is still not rational-prime specificity. Every generalized Euler product has the same local repetition mechanism. The theorem concerns survival of a declared generalized-prime source contrast through Euler-log compression, not uniqueness of the rational primes among all multiplicative systems.

### Reciprocal exponent, not a universal coefficient

For any fixed `q`, the surviving amplitude is

\[
C_q(x,\sigma)
=
\frac{2}{q}\operatorname{artanh}(e^{-q\sigma x})>0.
\tag{34}
\]

As `q->infinity`,

\[
C_q(x,\sigma)
\sim
\frac{2}{q}e^{-q\sigma x}.
\tag{35}
\]

So the theorem does not give a useful uniform constant as the reciprocal-band fraction tends to zero. This decay is the next quantitative barrier: allowing `q=q_delta -> infinity` couples bandwidth loss to exponential attenuation of the selected prime-power harmonic.

That is exactly where the unresolved interval after AF-184 lives. AF-184 proves super-algebraic invisibility when `delta T(delta) log(1/delta)->0`; AF-187 proves order-one visibility when `delta T(delta)` stays bounded below by a positive constant. Between them, a variable residue index `q_delta` and its attenuation `e^{-q_delta sigma x}` must be audited jointly with cluster order and phase-alignment error.

## Prior art and novelty assessment

The ingredients of the derivation are classical.

- NIST Digital Library of Mathematical Functions, §25.2(iv), especially Eq. 25.2.11, records the Euler product for `zeta(s)` in `Re(s)>1` and points to Apostol and Titchmarsh for the classical product theory. Taking the logarithm of one local Euler factor gives the absolutely convergent prime-power harmonic expansion used in `(12)`.
- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, is foundational prior art for the reciprocal relation between Fourier bandwidth, source spacing, Rayleigh scale, and stable recovery.
- Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, gives sharp clustered-Fourier conditioning results in which the cluster size controls the super-resolution exponent.
- Dmitry Batenkov, Gil Goldman, and Yosef Yomdin, **“Super-Resolution of Near-Colliding Point Sources,”** *Information and Inference: A Journal of the IMA* 10(2) (2021), 515--572, DOI `10.1093/imaiai/iaaa005`, provides neighboring minimax theory for near-colliding sources.
- The Fourier multiplier of an `m`-th forward difference, `(e^{i omega delta}-1)^m`, and its `sin^m` magnitude profile are standard finite-difference/Fourier analysis. No novelty is claimed for this filter identity.

A targeted literature search did not identify an authoritative source whose theorem is the exact Euler-log specialization `(8)`--`(31)`: phase-aligning the base point, letting a positive parity-split generalized-prime cluster order diverge under a shrinking-support constraint, and obtaining an odd prime-power residue-class projection. Absence from this search is not a priority claim. The durable value is the exact lower-bound mechanism and the corrected Arithmetic Fidelity boundary it supplies.

## Consequences for Arithmetic Fidelity

AF-186 gives an exact optimization of what a **derivative envelope** can certify about parity-cluster invisibility. AF-187 supplies the missing complementary lesson for the actual Euler kernel: derivative flatness is only one regime of the same finite-difference operator. Once the observed phase is reciprocal in the source spacing, high order converts the cluster into a harmonic selector and the Euler prime-power ladder prevents that explicit control from remaining invisible.

The resulting audit rule is sharper:

\[
\boxed{
\text{high-order cancellation}
\neq
\text{monotone information loss as bandwidth grows};
\quad
\text{the same operator can cross into residue-class selection.}
}
\tag{36}
\]

For Euler-product fidelity, a recovery analysis must therefore track at least three resources jointly: source spacing/order, vertical phase resolution, and attenuation of the prime-power harmonic selected at that phase. The remaining open quantitative problem is no longer simply whether reciprocal bandwidth restores visibility. It is to classify the **variable-`q` transition** when `delta T(delta)->0`: how fast may the selected harmonic index grow before its Euler weight decays faster than the source distinction one is trying to recover?