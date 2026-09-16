# WI-313 — Saturated capped tails encode source sign only at the deep threshold

**Status:** `EXACT-DERIVED + CLASSICAL-MINMAX + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

**Parent findings:** WI-310, WI-311, WI-312.

WI-311 constructs, on every fixed outer aperture, an exact source decomposition

\[
Q=\widehat{\mathcal D}+\widehat{\mathcal T}
\]

whose retained capped tail satisfies

\[
\left(\frac12-\delta\right)I
\preceq \widehat{\mathcal T}
\preceq \frac12 I,
\qquad
\delta=\frac1{4N}+\frac\epsilon2.
\tag{1}
\]

The point of the present finding is that (1) determines **exactly which inertia statistic of the comparison still carries source-sign information**. Ordinary negative index is the wrong statistic in the saturated regime: it asymptotically counts source spectrum below `1/2`, not source spectrum below zero. The source-sign statistic is instead the negative spectrum of `Dhat` lying below the full compensation depth

\[
-c,
\qquad
c:=\frac12-\delta.
\]

More generally, every source spectral sublevel is sandwiched by a shifted comparison sublevel with uncertainty exactly `delta`. Thus tail saturation is a spectral-resolution device, not a route by itself to small total negative index.

This is an exact consequence of form order and the classical min--max principle; no commutation between `Q` and `That` is used.

## 1. Variational spectral counts avoid domain and commutation assumptions

For a lower-semibounded closed Hermitian form `a` on the common fixed-aperture form domain, define the strict variational spectral count

\[
\mathcal N_a(t)
:=
\sup\left\{
\dim V:
 a[v]<t\|v\|^2
 \text{ for every }0\ne v\in V
\right\}.
\tag{2}
\]

The value may be infinite. When `a` is represented by a self-adjoint operator `A`, (2) is the usual min--max count

\[
\mathcal N_a(t)=\dim \mathbf 1_{(-\infty,t)}(A).
\]

If `a\preceq b`, then every subspace strictly below level `t` for `b` is also strictly below level `t` for `a`, hence

\[
\mathcal N_a(t)\ge \mathcal N_b(t).
\tag{3}
\]

This monotonicity is classical spectral theory; the new content here is only its application to the source-exact capped-tail decomposition.

## 2. Exact spectral-count sandwich

From `Q=Dhat+That` and (1),

\[
Q-\frac12I
\preceq
\widehat{\mathcal D}
\preceq
Q-\frac12I+\delta I.
\tag{4}
\]

Apply (3) at the comparison level

\[
t=s-\frac12.
\]

The right inequality in (4) gives

\[
\mathcal N_Q(s-\delta)
=
\mathcal N_{Q-I/2+\delta I}(s-I/2)
\le
\mathcal N_{\widehat{\mathcal D}}(s-I/2),
\]

while the left inequality gives the opposite side. Therefore, for every real `s`,

\[
\boxed{
\mathcal N_Q(s-\delta)
\le
\mathcal N_{\widehat{\mathcal D}}\!\left(s-\frac12\right)
\le
\mathcal N_Q(s).
}
\tag{5}
\]

Equation (5) is the exact spectral information retained by a tail that is `delta`-close to the maximal cap `I/2`. It requires neither simultaneous diagonalization nor an eigenvalue-by-eigenvalue matching.

## 3. Total negative index is contaminated by positive source spectrum

Set `s=1/2` in (5). Since the negative index of `Dhat` is

\[
n_-(\widehat{\mathcal D})
=
\mathcal N_{\widehat{\mathcal D}}(0),
\]

we obtain

\[
\boxed{
\mathcal N_Q\!\left(\frac12-\delta\right)
\le
n_-(\widehat{\mathcal D})
\le
\mathcal N_Q\!\left(\frac12\right).
}
\tag{6}
\]

Hence a saturating sequence `delta -> 0` drives the total negative index toward the source count below `1/2`, not toward the source negative count. In particular, source modes with energies in `(0,1/2)` are expected to become negative comparison modes even though they carry no negative-source information.

When `N_Q(1/2)` is finite, continuity from below of spectral projections gives

\[
\mathcal N_Q(1/2-\delta)\uparrow \mathcal N_Q(1/2),
\]

so the integer squeeze in (6) eventually stabilizes at exactly `N_Q(1/2)`. If that count is infinite, (6) still shows the same obstruction in extended-cardinality form.

Thus minimizing or eliminating **all** negative comparison eigenvalues is structurally misaligned with the source-sign problem in the maximally compensated architecture. A strong retained tail creates false negative comparison modes from genuinely positive source spectrum.

## 4. The deep threshold recovers source sign up to a `delta` window

The full guaranteed compensation depth is

\[
c=\frac12-\delta.
\]

Set `s=delta` in (5). Since `delta-1/2=-c`,

\[
\boxed{
\mathcal N_Q(0)
\le
\mathcal N_{\widehat{\mathcal D}}(-c)
\le
\mathcal N_Q(\delta).
}
\tag{7}
\]

This is the RH-relevant threshold statement. Every strictly negative source subspace forces a comparison subspace strictly below `-c`; conversely, every comparison subspace below `-c` comes from source spectrum lying below `delta`. The only false positives live in the source window

\[
[0,\delta).
\]

Consequently, if the source has no spectrum in that window,

\[
\mathcal N_Q(\delta)=\mathcal N_Q(0),
\]

then the deep comparison count is exact:

\[
\boxed{
\mathcal N_{\widehat{\mathcal D}}(-c)
=
\mathcal N_Q(0).
}
\tag{8}
\]

At a source null vector `v`, the pointwise form identity gives

\[
\widehat{\mathcal D}[v]
=-\widehat{\mathcal T}[v]
\le
-c\|v\|^2.
\tag{9}
\]

Thus a null direction lies at or below the compensation boundary; a strictly negative source direction lies strictly beyond it. The use of a strict count in (7) is important: equality at the boundary is not silently counted as negative source mass.

Equation (5) also gives the same conclusion at every source level `s`: the shifted `Dhat` sublevel resolves the source sublevel with spectral uncertainty exactly `delta`.

## 5. Sign resolution has a componentwise Hilbert--Schmidt price

WI-312 quantifies the cost of the same saturation mechanism. For the smooth frequency-multiplexed construction of WI-311, let `mu` be the normalized frequency-energy law and let

\[
\eta:=\mathcal Q_\mu(h),
\qquad
h=T_{B_L}.
\]

WI-311 gives

\[
\eta<\frac1{2N}+\epsilon=2\delta.
\tag{10}
\]

WI-312 proves that for a fixed sufficiently small archimedean cutoff `a_0 in (0,2L)`, whenever `eta<=1/8`, the continuous localization-defect component satisfies

\[
\|C_R\|_{\mathrm{HS}}^2
\ge
\frac{2L-a_0}{2}
\left(
\frac{\pi h}{128\eta}-\frac1{a_0}
\right).
\tag{11}
\]

For `delta<=1/16`, (10) implies `eta<=2delta<=1/8`, and hence

\[
\boxed{
\|C_R\|_{\mathrm{HS}}^2
\ge
\frac{2L-a_0}{2}
\left(
\frac{\pi h}{256\delta}-\frac1{a_0}
\right).
}
\tag{12}
\]

Therefore resolving source sign to a window of width `delta` by this smooth capped-tail saturation costs at least

\[
\|C_R\|_{\mathrm{HS}}^2=\Omega(\delta^{-1}),
\qquad
\|C_R\|_{\mathrm{HS}}=\Omega(\delta^{-1/2})
\]

for that continuous archimedean component. The two previous findings therefore fit together sharply: shrinking the false-positive spectral window in (7) necessarily destroys uniform componentwise `S_2` control in the WI-311 construction.

This does **not** imply that the recombined source correction has large operator norm or large deep negative index. WI-312 already leaves open cancellation between the continuous and discrete localization defects, and (12) does not close that escape route.

## 6. Stress tests and scope

Several tempting stronger interpretations are invalid.

First, (5) is not an eigenvalue matching theorem. It is a variational count sandwich, which is exactly why no commutation of `Q` and `That` is needed.

Second, (6) does not assert that the actual Weil source has positive spectrum below `1/2`; it says that **if such spectrum is present**, total comparison inertia counts it together with genuinely negative source spectrum. Therefore total negative index alone cannot distinguish the two populations in this architecture.

Third, (7) does not prove positivity of the Weil source, RH, or absence of off-critical zeros. It identifies the correct comparison invariant: the sector below `-c`, with a false-positive window of width `delta` on the source side.

Fourth, the Hilbert--Schmidt blow-up (12) is only componentwise. A source-valid recombination may cancel the large continuous contribution, and an operator-norm, determinant, principal-minor, or direct deep-sector estimate might avoid an `S_2` budget entirely.

Finally, nothing here alters the unconditional two-thirds simple-critical-zero proportion. This finding belongs to the complementary structural program: making the finite negative sector source-informative enough to distinguish genuine source-sign defect from comparison artefacts.

## 7. Prior art and novelty audit

The only abstract ingredient in (3)--(8) is the classical min--max/variational spectral-count monotonicity for ordered self-adjoint forms. A convenient reference is Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM 157 (2014), Part 1, Chapter 4, especially the min--max theorem and eigenspace estimates:

https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/index.html

A targeted search for combinations of Weil explicit forms, capped or clipped source tails, negative-index comparison, and shifted/deep spectral thresholds did not locate a prior statement of (5)--(8) in this source-exact localization setting. That negative search is not a priority claim. The novelty asserted here is the exact deduction from the already established Mathia decomposition and the resulting research redirection, not the min--max principle itself.

The immediate prior Mathia facts are source-exact: WI-310 establishes the `1/2` cap, WI-311 gives smooth saturation with error `delta`, and WI-312 proves the anti-concentration/archimedean `S_2` obstruction. No result from `research/weil_positivity/` or another line is used as an assumption.

## 8. Consequence for the research frontier

The saturated-tail program should no longer optimize **total** negative index as its primary objective. The correct observable is the **deep negative sector relative to the guaranteed tail floor**:

\[
\boxed{
\text{source sign below }0
\quad\longleftrightarrow\quad
\text{comparison spectrum below }-c
\quad\text{up to a source window of width }\delta.
}
\]

This produces a precise next gate. Either control the deep index `N_Dhat(-c)` directly, or exploit recombined continuous/discrete cancellation strongly enough to let `delta -> 0` without paying the componentwise Hilbert--Schmidt divergence of WI-312. Any method that controls only `n_-(Dhat)` is now known to target the wrong spectral population in the saturating regime.