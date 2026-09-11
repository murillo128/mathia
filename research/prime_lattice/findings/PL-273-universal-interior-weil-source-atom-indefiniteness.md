# PL-273 — Every interior Weil source atom is eventually indefinite in the full Galerkin tower

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-STRUCTURAL + DECISIVE-NEGATIVE + UNIVERSAL-ATOMIC-SIGN-CLASSIFICATION + PRIOR-ART-ADJACENT`

## Claim

`PL-272` exhibited one positive source atom, `delta_{1/2}`, whose finite-Weil source matrix is indefinite on the constant/first-cosine compression. That midpoint is not exceptional. In Groskin's source calculus, **every nontrivial interior atom** has an indefinite compression once the Galerkin band is large enough.

Let `Q_N[delta_omega]` denote the level-`N` source matrix for a point mass at `omega in [0,1]`. On the normalized even Fourier modes

\[
T_0(t)=1,
\qquad
T_k(t)=\sqrt2\cos(2\pi k t),\quad k\ge1,
\]

Groskin's exact kernel formula gives

\[
\langle T,Q_N[\delta_\omega]T\rangle
=2\int_0^\omega T(t)T(\omega-t)\,dt.
\]

The constant direction is always positive in the interior:

\[
K_0(\omega)=2\omega>0.
\]

For a pure cosine mode one obtains exactly

\[
\boxed{
K_k(\omega)
=2\omega\cos(2\pi k\omega)
+\frac{\sin(2\pi k\omega)}{\pi k}.
}
\]

For every `0<omega<1` there exists a mode `k` with `K_k(omega)<0`. Once such a mode has entered the Galerkin space, the same positive constant direction and negative cosine direction remain in every larger compression. Hence there is `N_0(omega)` such that

\[
\boxed{
Q_N[\delta_\omega]\text{ is indefinite for every }N\ge N_0(\omega),
\qquad 0<\omega<1.
}
\]

On the even Fourier tower the endpoints have the opposite behavior:

\[
Q_N[\delta_0]=0,
\qquad
Q_N[\delta_1]=2I.
\]

Thus the source-atom sign classification is sharp: zero at the invisible endpoint, positive at the opposite endpoint, and eventually permanently indefinite at every interior frequency.

For the rational-prime source, an active prime power `q=p^a<c` occurs at

\[
\omega_q(c)=1-\frac{\log q}{\log c}\in(0,1).
\]

Therefore **every active prime-power atom is eventually indefinite as the Galerkin band grows**. Its actual coefficient `-Lambda(q)/sqrt(q)` reverses the form but cannot remove indefiniteness. The midpoint control from `PL-272` is therefore a special low-band witness of a universal interior obstruction, not a tuned pathology.

## 1. Exact cosine compression

For `T_k(t)=sqrt(2) cos(2 pi k t)`, the product-to-sum identity yields

\[
2T_k(t)T_k(\omega-t)
=2\cos(2\pi k\omega)
+2\cos(4\pi k t-2\pi k\omega).
\]

Integrating from `0` to `omega` gives

\[
\begin{aligned}
K_k(\omega)
&=2\int_0^\omega T_k(t)T_k(\omega-t)\,dt\\
&=2\omega\cos(2\pi k\omega)
+\frac{\sin(2\pi k\omega)}{\pi k}.
\end{aligned}
\]

The correction term is uniformly bounded by `1/(pi k)`. Consequently any arbitrarily large modes for which the phase `k omega mod 1` stays in an arc where the cosine is bounded above by a negative constant give a negative direction.

## 2. Every interior frequency supplies arbitrarily large negative modes

### Irrational `omega`

If `omega` is irrational, the rotation orbit `{k omega mod 1 : k>=1}` is dense in the circle. Every tail of the orbit is dense as well. Hence there are arbitrarily large `k` for which

\[
\{k\omega\}\in[1/3,2/3],
\qquad
\cos(2\pi k\omega)\le -\frac12.
\]

For any such sufficiently large `k`,

\[
K_k(\omega)
\le -\omega+\frac1{\pi k}<0.
\]

### Rational `omega`

Write `omega=a/b` in lowest terms, with `b>=2`. Put `r=floor(b/2)`. Then

\[
\frac rb\in[1/3,1/2],
\qquad
\cos(2\pi r/b)\le-\frac12.
\]

Since `a` is invertible modulo `b`, choose `j` with `ja congruent r (mod b)`. Every `k=j+mb` has the same phase, and such `k` are arbitrarily large. Again

\[
K_k(\omega)
\le -\omega+\frac1{\pi k}<0
\]

for all sufficiently large members of that residue class.

Thus each interior `omega` has at least one negative pure-cosine direction. Since `K_0(omega)=2omega>0`, the compression to the span of `T_0` and that `T_k` is indefinite. This compression is contained in every level `N>=k`, proving the permanent all-higher-band statement.

No quantitative bound uniform in `omega` is claimed. As `omega` approaches an endpoint, the first witnessing mode can move arbitrarily far out in the tower.

## 3. Endpoint controls

At `omega=0`, the defining integral has zero length, so every source matrix vanishes. This is exactly the invisible `delta_0` direction isolated in `PL-271`.

At `omega=1`, every even integer-frequency trigonometric polynomial satisfies `T(1-t)=T(t)`. Hence

\[
K_T(1)=2\int_0^1 |T(t)|^2\,dt,
\]

and in the normalized even Fourier basis the compression is `2I`. The positive endpoint therefore does not contradict the interior theorem.

For arithmetic source events, the endpoint `omega=1` would correspond to `q=1`, for which `Lambda(1)=0`; it is not a prime-power source atom. A genuine active prime power has `0<omega_q(c)<1` and is covered by the indefinite case.

There is also no conflict with threshold statements for the moving cutoff path. At `c=q`, one has `omega_q(c)=0`, so the fixed source atom matrix itself is zero. A rank-one negative-semidefinite object arising from differentiating the moving cutoff through the threshold is a different quantity from `Q_N[delta_omega]` at fixed `omega`.

## 4. Consequence for the source-positivity route

`PL-270` showed that one Galerkin band sees a finite quotient of the prime source; `PL-271` showed that the complete tower recovers the finite source modulo the zero atom; `PL-272` then proved that positivity of the source measure does not imply positivity of its matrix image. The present classification strengthens the last step from one atom and an open neighborhood to **all interior atoms**.

Therefore no argument can recover Weil positivity by claiming that sufficiently fine Galerkin resolution eventually makes the individual von-Mangoldt source atoms positive. The opposite is true: for every fixed active prime-power atom, increasing the band eventually exposes both a positive and a negative direction, and that sign defect persists thereafter.

This leaves only mechanisms that are genuinely global in the arithmetic source or in the completed Weil form: cancellation among different atoms, coupling to the pole/archimedean terms, cross-cutoff identities, or a transformed object whose positivity is not atomwise positivity of Groskin's source matrices. In particular, source positivity, projective identifiability, and arbitrarily high Galerkin resolution still do not furnish the missing order structure.

## 5. Prior-art and adversarial audit

The load-bearing source identity is prior art: Groskin's Lemma 2.3 gives the kernel `K_v(omega)`, and the pure-cosine formula is an immediate specialization of that exact finite source calculus. `PL-272` already records adjacent prior art from de Andrade Silva showing parity-dependent and mixed-sign localized prime contributions. No novelty claim is made for the underlying kernel or for the general fact that localized prime blocks can have mixed sign.

The durable mathematical delta here is the **all-interior-frequency classification** and its prime-power consequence: the midpoint counterexample of `PL-272` extends, by the rotation arithmetic of `k omega`, to every `omega in (0,1)`, with permanent indefiniteness after a frequency-dependent finite band. The literature audit did not establish an existing statement of this exact classification, so it is recorded only as a derived, prior-art-adjacent extension within this research line.

The main adversarial checks are built into the proof. Rational frequencies are not an exceptional escape because a fixed congruence class supplies arbitrarily large negative-phase modes; irrational frequencies are handled by density of irrational rotations; multiplication by the negative von-Mangoldt coefficient preserves indefiniteness; and the endpoint behaviors are separated explicitly. The argument uses only an even compression, which is sufficient: indefiniteness of a compression forces indefiniteness of the full source matrix containing it.

A possible future strengthening would require a quantitative estimate for the first negative mode in terms of `omega` (or, arithmetically, in terms of `log q/log c`). Such a bound is not needed for the qualitative obstruction proved here and is not asserted.

## Sources

- Akiva Groskin, **“A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3 [math.NT] (revised 14 August 2026). Lemma 2.3 supplies the exact atomic source kernel and Corollary 2.4 its finite Fourier representation; already anchored in `research/prime_lattice/SOURCES.md`.
- Breno Wilson de Andrade Silva, **“A Loewner divided-difference formula for the prime contribution in the localized Weil quadratic form, and a parity sign law,”** Zenodo record 20710075 (15 June 2026), DOI `10.5281/zenodo.20710075`. Adjacent prior art for mixed-sign localized prime contributions; already audited in `PL-272`.