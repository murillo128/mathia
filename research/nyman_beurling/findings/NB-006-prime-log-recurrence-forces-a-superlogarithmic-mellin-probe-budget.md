# NB-006 — prime-log recurrence forces a superlogarithmic Mellin probe budget

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUANTITATIVE-MELLIN-ALIASING + PRIME-LOG-DIMENSION + GROWING-PROBE-OBSTRUCTION`. `NB-004` shows qualitatively that every fixed finite family of Bagchi dilation probes admits target-orthogonal approximate Mellin aliases. `NB-005` then identifies a real norm boundary: summable full-semigroup defect norms remain noncoercive, while the projected pure-Mellin aliases have logarithmically divergent full `ell^2` defect. That leaves open whether a **growing truncated harmonic probe family** can supply quantitative anti-aliasing.

There is an exact obstruction before any source-selection theorem enters. For every finite scale cutoff `M>=2` and every `0<epsilon<=1`, there is a unit vector `w` in the canonical discrete Nyman space, exactly orthogonal to the target, such that

\[
\boxed{
\|(A_m^*-m^{-1/2}I)w\|
\le \frac{\varepsilon}{\sqrt m}
\qquad(2\le m\le M),
}
\tag{1}
\]

and hence

\[
\boxed{
\frac1{\log M}
\sum_{m=2}^{M}
\|(A_m^*-m^{-1/2}I)w\|^2
\le \varepsilon^2.
}
\tag{2}
\]

More importantly, the witness can be chosen from the projected Mellin family of `NB-004` with an explicit frequency ceiling. Put

\[
d=\pi(M),
\qquad
Q=\left\lceil\frac{4\pi\log_2 M}{\varepsilon}\right\rceil,
\tag{3}
\]

where `pi(M)` is the number of primes at most `M` and `log_2 M=log M/log 2`. Then one may choose an **integer** Mellin frequency `tau` satisfying

\[
\boxed{
5\le \tau\le 5Q^{\pi(M)}.
}
\tag{4}
\]

Thus the effective recurrence dimension of the first `M` integer dilation probes is only the number of prime logarithms, not `M`. For fixed `epsilon`, the prime number theorem calibrates the guaranteed alias ceiling as

\[
\log \tau
\le (1+o(1))\frac{M\log\log M}{\log M}.
\tag{5}
\]

Consequently, even after moving to the nonsummable harmonic boundary isolated by `NB-005`, a positive semigroup certificate still needs a quantitative **scale-versus-Mellin-bandwidth theorem**. Against the explicit projected-Mellin aliases, excluding every frequency up to a large bandwidth `T` cannot follow from the first `M` scales when the recurrence ceiling in (4) still lies below `T`; at fixed accuracy this places the natural obstruction around

\[
M\asymp
\frac{\log T\,\log\log T}{\log\log\log T}
\tag{6}
\]

up to asymptotic constants. This is a necessary scale pressure against this alias mechanism, not a sufficient anti-aliasing theorem and not a statement about actual best-approximation residuals.

## 1. The target-orthogonal Mellin aliases have an exact scale defect

Retain the real-space Bagchi model and notation of `NB-004`. The canonical discrete space `\mathcal M` is invariant under the integer dilation isometries `T_m`, with compressed operators

\[
A_m=T_m|_{\mathcal M},
\]

and the target `e=1` satisfies

\[
A_m^*e=m^{-1/2}e.
\tag{7}
\]

For real `tau`, let

\[
h_\tau(x)=x^{i\tau},
\qquad
v_\tau=P_{\mathcal M}h_\tau,
\qquad
u_\tau=\frac{v_\tau}{\|v_\tau\|}.
\tag{8}
\]

`NB-004` proves exactly

\[
A_m^*v_\tau=m^{-1/2-i\tau}v_\tau
\tag{9}
\]

and, after writing

\[
a_\tau=\langle \nu_\tau,e\rangle,
\qquad
w_\tau=
\frac{\nu_\tau-a_\tau e}{\sqrt{1-|a_\tau|^2}},
\tag{10}
\]

one obtains a unit vector in `\mathcal M\cap e^\perp` with

\[
\boxed{
\|(A_m^*-m^{-1/2}I)w_\tau\|
=
\frac{m^{-1/2}|m^{-i\tau}-1|}
     {\sqrt{1-|a_\tau|^2}}.
}
\tag{11}
\]

The same finding gives, for `|tau|>=1`,

\[
\|v_\tau\|^2
\ge
\frac{\cos^2(1/4)}{\lceil2|\tau|\rceil},
\qquad
\langle v_\tau,e\rangle=\frac1{1+i\tau}.
\tag{12}
\]

For integer `tau>=5`, therefore

\[
|a_\tau|^2
\le
\frac{2\tau}{\cos^2(1/4)(1+\tau^2)}
<\frac34.
\tag{13}
\]

For the last elementary inequality it is already enough to use `cos(1/4)>3/4`; the displayed rational function decreases for `tau>=1` and is below `3/4` at `tau=5`. Hence

\[
\boxed{
(1-|a_\tau|^2)^{-1/2}<2
\qquad(\tau\in\mathbb Z,\ \tau\ge5).
}
\tag{14}
\]

This uniform bound lets a simultaneous phase return be converted into a quantitative target-orthogonal defect without losing control in the orthogonalization step.

## 2. Simultaneous recurrence needs only the prime logarithms

List the primes at most `M` as

\[
p_1,\ldots,p_d,
\qquad d=\pi(M),
\]

and put

\[
\alpha_j=\frac{\log p_j}{2\pi}.
\tag{15}
\]

Partition the torus `[0,1)^d` into `Q^d` half-open cubes of side `1/Q`. Consider the `5Q^d+1` points

\[
\{n(\alpha_1,\ldots,\alpha_d)\}
\qquad(0\le n\le5Q^d),
\tag{16}
\]

where braces denote coordinatewise fractional part. One cube contains at least six of these points. Let `n_-<n_+` be the smallest and largest indices among six points in the same cube and set

\[
\tau=n_+-n_-.
\tag{17}
\]

Then

\[
\boxed{
5\le\tau\le5Q^d,
\qquad
\left\|\frac{\tau\log p}{2\pi}\right\|_{\mathbb R/\mathbb Z}
<\frac1Q
\quad(p\le M,\ p\ \text{prime}).
}
\tag{18}
\]

This is the simultaneous Dirichlet/Kronecker recurrence needed here, with the lower bound `tau>=5` built into the same pigeonhole argument. No rational independence of the prime logarithms is required for the existence estimate.

Now let `2<=m<=M` and write

\[
m=\prod_{p\le M}p^{\nu_p(m)}.
\]

The distance to the nearest integer is subadditive, so (18) gives

\[
\begin{aligned}
\left\|\frac{\tau\log m}{2\pi}\right\|_{\mathbb R/\mathbb Z}
&\le
\frac1Q\sum_{p\le M}\nu_p(m)\\
&=\frac{\Omega(m)}Q\\
&\le\frac{\log_2 M}{Q}.
\end{aligned}
\tag{19}
\]

Since `|e^{-2\pi i x}-1|<=2\pi\|x\|_{R/Z}`, equations (3) and (19) imply

\[
\boxed{
|m^{-i\tau}-1|
\le \frac{2\pi\log_2 M}{Q}
\le\frac\varepsilon2
\qquad(2\le m\le M).
}
\tag{20}
\]

Thus controlling the prime phases automatically controls every composite phase below `M`. Composite probes add algebraic consequences of the same prime-log coordinates; they do not increase the recurrence dimension in this test.

## 3. The entire truncated harmonic defect can be made arbitrarily small

Insert (14) and (20) into the exact defect formula (11). The vector `w=w_\tau` from (10) is a unit vector exactly orthogonal to `e`, and for every `2<=m<=M`,

\[
\|(A_m^*-m^{-1/2}I)w\|
\le
2m^{-1/2}\frac\varepsilon2
=rac\varepsilon{\sqrt m}.
\tag{21}
\]

This proves (1). Squaring and summing gives

\[
\sum_{m=2}^M
\|(A_m^*-m^{-1/2}I)w\|^2
\le
\varepsilon^2
\sum_{m=2}^M\frac1m.
\tag{22}
\]

The elementary harmonic bound `H_M<=1+log M` yields

\[
\sum_{m=2}^M\frac1m=H_M-1\le\log M,
\tag{23}
\]

and therefore exactly the normalized estimate (2).

This closes one possible overreading of `NB-005`. The fact that every **fixed nonzero** Mellin frequency has truncated `ell^2` defect asymptotic to `2 log M` does not imply a uniform target-orthogonal lower bound when the frequency is allowed to depend on `M`. Diagonal recurrence can retune the Mellin frequency as the probe family grows and make the normalized defect arbitrarily small at each finite depth.

The distinction is the same finite-versus-uniform issue that appears throughout the Nyman problem: pointwise divergence in `M` is not a coercivity theorem on a scale-dependent class of vectors.

## 4. Quantitative recurrence gives a bandwidth pressure

The construction already contains its quantitative cost. From (3)--(4),

\[
\boxed{
\tau
\le
5\left\lceil
\frac{4\pi\log_2 M}{\varepsilon}
\right\rceil^{\pi(M)}.
}
\tag{24}
\]

Hence if a proposed source theorem admits projected-Mellin aliases throughout a bandwidth `|tau|<=T`, and

\[
T\ge
5\left\lceil
\frac{4\pi\log_2 M}{\varepsilon}
\right\rceil^{\pi(M)},
\tag{25}
\]

then the first `M` dilation probes necessarily contain an `epsilon`-alias in that admitted band. A positive lower bound on the truncated harmonic defect cannot hold on that class.

For fixed `epsilon`, the classical prime number theorem gives

\[
\pi(M)\sim\frac M{\log M},
\qquad
\log Q=\log\log M+O_\varepsilon(1),
\]

so (24) yields the calibration

\[
\boxed{
\log\tau
\le
(1+o(1))
\frac{M\log\log M}{\log M}.
}
\tag{26}
\]

Inverting this scale shows where the constructive recurrence pressure becomes comparable with a putative Mellin bandwidth `T`: the corresponding `M` is of order

\[
\boxed{
\frac{\log T\,\log\log T}
     {\log\log\log T}.
}
\tag{27}
\]

No sharp threshold is claimed. Equation (24) is an **upper bound on the frequency at which an alias is guaranteed to occur**. Aliases may recur much earlier, and a lower frequency ceiling is not obtained. Therefore (27) is only a necessary probe-depth pressure against this explicit recurrence mechanism, not a sufficient number of scales for quantitative target identification.

## 5. Consequence for the finite-section frontier

`NB-001` says that target-aware finite sections must retain the target pairings; `NB-002` says absolute multiplicative scale changes target capture even when the local Gram block is unchanged; `NB-004` says finitely many fixed semigroup probes cannot infer the target direction; and `NB-005` says summable full-semigroup norms remain noncoercive while fixed-frequency Mellin aliases pay logarithmic `ell^2` cost.

The present result makes the remaining semigroup option more precise. Merely letting the scale cutoff grow is not enough. One must also control the **admitted Mellin bandwidth** of the source-selected finite-section residual, because a growing alias frequency can outrun every finite probe set. The exact prime-log dimension in (24) supplies a quantitative interface for such a theorem.

A viable positive route can now take one of two forms. It may prove that actual near-optimal Nyman residuals have Mellin content confined to a bandwidth `T_N` and choose a scale cutoff `M_N` large enough that the recurrence obstruction no longer guarantees an alias inside that band. Or it may bypass semigroup inference and work directly with the explicit target pairings `b_N` or a norm-controlled primal/dual certificate. In either case, a statement about arbitrary vectors in `\mathcal M` is stronger than necessary: the unresolved source-selection question is whether the canonical finite-section residual class excludes the aliases constructed here.

This finding does **not** bound `d_N`, prove any lower bound for the target-weighted small-eigenvalue mass, or show that projected Mellin characters occur as best-approximation residuals. It turns the vague requirement “let the probe family grow” into an explicit scale-versus-frequency obligation.

## 6. Prior art and audit boundary

The load-bearing Nyman input remains Bagchi's canonical dilation semigroup, already anchored in `research/nyman_beurling/SOURCES.md`. The quantitative recurrence proof in Section 2 is included in full and is the elementary simultaneous Dirichlet approximation argument on the prime-log torus. Its general mechanism is classical Kronecker/Bohr almost periodicity for ordinary Dirichlet frequencies: prime logarithms supply the independent coordinates and composite logarithms are their integer combinations. A targeted search of Nyman--Beurling dilation-semigroup, approximate-eigenvector, Mellin-character, and Diophantine-recurrence literature did not locate (24) or the resulting target-orthogonal harmonic-defect obstruction as a named Nyman theorem. This is a prior-art boundary, not a novelty claim.

Several falsification controls are essential. First, the vector depends on `M`; `NB-005` remains correct for each fixed nonzero Mellin frequency. Second, the recurrence theorem concerns the whole canonical Hilbert space, not the source-selected residuals of `V_N`; restricting those residuals could invalidate the alias witness and would be genuine new information. Third, (24) is only a guaranteed **upper** recurrence time and cannot be reversed into a sufficient anti-aliasing scale. Fourth, approximating only prime phases is legitimate here because every integer `m<=M` factors over those primes and the defect phase is exactly multiplicative; this reduction would fail for a different probe family without that algebraic closure.

The result is unconditional and does not use RH, a zero-density hypothesis, or a conjectural zeta moment. It gives no improved Nyman approximation rate and no RH conclusion. Its durable mathematical content is the explicit quantitative obstruction that any growing semigroup-based target certificate must beat.