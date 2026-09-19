# MC-397 — Source-mode averaging collapses to an endpoint signature projector

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the physical source-subspace setup of `MC-377`, `MC-381`, `MC-392`, and `MC-396`. Let

\[
W\le \mathbf F_2^R,
\qquad H:=|W|,
\]

be a source-mode subgroup whose quadratic source characters are represented on one common square-free source radical

\[
P=\prod_{p\in U}p.
\]

For each `I\in W`, extend the source character to the common modulus `P` by the principal factors on source primes not appearing in its primitive conductor; denote the resulting imprimitive character by `\chi_I`. Then

\[
\chi_I\chi_J=\chi_{I+J}
\tag{1}
\]

as Dirichlet characters modulo `P`.

Put

\[
G:=(\mathbf Z/P\mathbf Z)^\times.
\]

Evaluation of the source family defines the exact **source-signature map**

\[
\Phi:G\longrightarrow\widehat W,
\qquad
\Phi(u)(I):=\chi_I(u).
\tag{2}
\]

The characters indexed by `W` are distinct in the endpoint construction, so `W\hookrightarrow\widehat G` is injective. By finite duality, `(2)` is therefore surjective and

\[
K:=\ker\Phi
\quad\text{satisfies}\quad
[G:K]=H.
\tag{3}
\]

For arbitrary coefficients `a=(a_I)_{I\in W}`, define

\[
A_a(n):=\sum_{I\in W}a_I\chi_I(n),
\qquad
\widehat a(\omega):=\sum_{I\in W}a_I\omega(I)
\quad(\omega\in\widehat W).
\tag{4}
\]

Then for every integer `n`,

\[
\boxed{
A_a(n)
=
\mathbf 1_{(n,P)=1}\,\widehat a(\Phi(n)).
}
\tag{5}
\]

Hence the complete source-family quadratic expression is already diagonalized before any character-sum estimate:

\[
\boxed{
\left|\sum_{I\in W}a_I\chi_I(n)\right|^2
=
\mathbf 1_{(n,P)=1}\,
|\widehat a(\Phi(n))|^2.
}
\tag{6}
\]

In particular, for the normalized uniform source average

\[
a_I=H^{-1/2},
\]

finite Walsh orthogonality gives the exact projector

\[
\boxed{
\left|H^{-1/2}\sum_{I\in W}\chi_I(n)\right|^2
=
H\,\mathbf 1_{(n,P)=1}\mathbf 1_{n\bmod P\in K}.
}
\tag{7}
\]

Thus **inside the present Selberg/Bombieri prime-frame architecture, the source-mode index cannot by itself play the role of the extra arithmetic averaging variable in Stadlmann's modified `q`-van der Corput argument**. Summing the source modes exactly does not leave an additional oscillatory family variable inside differencing; it converts the family into a nonnegative signature weight, and in the uniform case into one multiplicative subgroup projector of exact residue density `1/H` modulo `P`.

This does not say that collective source information is useless. It says that its remaining content is an arithmetic **distribution problem for the signature map `\Phi` on the relevant short interval/Selberg support**, rather than a free `H`-fold averaging gain. Re-expanding the signature weight in Fourier modes returns exactly to weighted source characters, so no new independent oscillatory variable has been created.

The proposed averaged-`q`-van-der-Corput clue therefore survives only in a narrower form: a Stadlmann-type gain would have to retain a genuinely arithmetic variable already present before the source-mode collapse—most naturally a Selberg divisor/lcm variable, or another arithmetic shell/source variable whose presence changes the diagonal geometry under Cauchy/differencing. Pure averaging over the dual source index is ruled out as that variable.

No estimate for `M(x)` follows.

## 1. Common-modulus source characters form a finite Fourier system

For each source coordinate prime, the endpoint source character is quadratic. Extending every product character to the common radical `P` by principal factors preserves endpoint values on shell primes and gives `(1)`: on units modulo `P` this is the ordinary product law, while on non-units both sides vanish.

For fixed `u\in G`, the map

\[
I\mapsto\chi_I(u)
\]

is consequently a character of the additive group `W`, proving that `\Phi(u)\in\widehat W`. Multiplicativity in `u` makes `\Phi` a homomorphism.

The source modes in the physical subspace are distinct: if `\chi_I=\chi_J`, then `\chi_{I+J}` is principal on the common source group, hence its endpoint restriction is the trivial endpoint mode, contradicting independence unless `I=J`. Therefore the homomorphism

\[
W\hookrightarrow\widehat G,
\qquad I\mapsto\chi_I,
\]

is injective. Dualizing this inclusion gives the surjection `G\twoheadrightarrow\widehat W` in `(2)`, and `(3)` follows.

Equation `(5)` is now only finite Fourier evaluation. For `(n,P)=1`,

\[
A_a(n)
=
\sum_I a_I\Phi(n)(I)
=\widehat a(\Phi(n));
\]

for `(n,P)>1`, every common-modulus character vanishes. Squaring proves `(6)`.

For `a_I=H^{-1/2}`, character orthogonality on `W` gives

\[
\widehat a(\omega)
=
\begin{cases}
\sqrt H,&\omega=1,\\
0,&\omega\ne1,
\end{cases}
\]

which is exactly `(7)`. This is the source-frame analogue of the annihilator/coset projector already encountered in `MC-246`.

## 2. The collapse occurs before the Selberg off-diagonal estimate

Use the same shell and Selberg majorant as `MC-377`. Let `\mathcal R_y` be the shell-prime set, let `N=2y`, choose the sieve cutoff `B<y`, and write

\[
f(n)=\left(\sum_{d\mid n}g(d)\right)^2\ge0,
\]

with `g` supported on `d\le B`. For shell primes `r>y>B`, one has `f(r)=1`. Since shell primes are coprime to the lower-prime source radical `P`, for every coefficient vector `a`,

\[
\begin{aligned}
\sum_{r\in\mathcal R_y}|A_a(r)|^2
&\le
\sum_{n\le N}f(n)|A_a(n)|^2\\
&=
\boxed{
\sum_{\substack{n\le N\\(n,P)=1}}
 f(n)|\widehat a(\Phi(n))|^2.
}
\tag{8}
\end{aligned}
\]

Thus if the source family is retained until after forming the Bombieri/Selberg quadratic form, exact Fourier summation removes the source index completely.

Expanding the sieve weight makes the surviving arithmetic variables explicit. Put

\[
\ell=[d_1,d_2].
\]

Then `(8)` becomes

\[
\boxed{
\sum_{d_1,d_2\le B}g(d_1)g(d_2)
\sum_{m\le N/\ell}
\mathbf 1_{(\ell m,P)=1}
\left|\widehat a\!\left(\Phi(\ell m)\right)\right|^2.
}
\tag{9}
\]

Terms with `(\ell,P)>1` vanish. For the surviving terms, multiplicativity gives

\[
\Phi(\ell m)=\Phi(\ell)\Phi(m),
\tag{10}
\]

so the only remaining coupling to the source family is a translation of the arithmetic signature by the sieve lcm.

For the uniform source vector, `(9)` specializes to the exact subgroup-incidence expression

\[
\boxed{
H\sum_{\substack{d_1,d_2\le B\\(\ell,P)=1}}
 g(d_1)g(d_2)
\#\left\{
 m\le N/\ell:
 (m,P)=1,
 \Phi(m)=\Phi(\ell)^{-1}
\right\}.
}
\tag{11}
\]

Because `W` has exponent two, `\Phi(\ell)^{-1}=\Phi(\ell)`, but the inverse notation in `(11)` emphasizes the general subgroup-projection mechanism.

Equation `(11)` is the decisive structural test. The `H` source modes have not become `H` independent samples available to `q`-van der Corput. They have become one moving signature/coset condition. The exact global residue density of each signature class is `1/H`, but obtaining comparable density in intervals of length `N/\ell` when the common source modulus is large is itself the unresolved arithmetic problem. Assuming such equidistribution would simply move the required cancellation into the projector count.

For general `a`, the nonnegative weight `|\widehat a(\Phi(n))|^2` replaces the indicator. Fourier-expanding that weight gives

\[
|\widehat a(\Phi(n))|^2
=
\sum_{I,J\in W}a_I\overline{a_J}\chi_{I+J}(n),
\tag{12}
\]

which is exactly the original pair-character expansion. Thus switching between source modes and source signatures is an exact basis change, not an additional averaging resource.

## 3. Why this is different from Stadlmann's retained variable

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (arXiv:2309.00425; Adv. Math. 474 (2025), 110190) gives a useful control for what a genuine retained-variable gain looks like.

In the Type I argument sketched in her Section 1.1, the earlier `q`-van der Corput treatment did not use the summation over an arithmetic variable `y`. Its diagonal contribution forced

\[
\Delta<N/Y^2.
\]

Stadlmann reorganizes the congruence so that both `n` and `y` remain inside the `q`-van der Corput step. After Cauchy, the relevant congruence between `(n,\widetilde n,y,\widetilde y)` leaves only `O(N/Y)` diagonal choices in `n` for fixed outer data, making the diagonal contribution `O(\Delta N/Y)` and allowing

\[
\Delta<N/Y.
\]

The gain therefore comes from **changed diagonal combinatorics caused by retaining an arithmetic summation variable inside differencing**, not from averaging a finished collection of one-variable estimates.

Equations `(6)`--`(11)` show that the source-mode index in the current endpoint frame has the opposite behavior: it is a Fourier-dual label. Exact summation over that label diagonalizes it into a signature projector before the arithmetic differencing begins. There is no residual source-mode multiplicity whose Cauchy diagonal can automatically acquire a factor analogous to `1/Y`.

This identifies the correct dictionary for future use of the Stadlmann clue. A viable transfer must exhibit an arithmetic variable in `(9)`—for example `\ell`, or a finer pre-lcm divisor variable—that remains inside the oscillatory/differencing stage and provably changes the diagonal count. Calling the source-character family an "extra average" is not enough.

## 4. Relation to the current source-cost frontier

`MC-382` shows that treating one source character at a time with iterated `q`-van der Corput incurs an intrinsic depth proportional to the fixed-power conductor exponent and hence an exponentially decaying saving exponent. `MC-396` improves the packing of source factors, but its remaining tariff is still the true `2^{O(A)}` differencing depth.

The natural escape was therefore to ask whether the whole source family could be kept averaged before the modewise collapse. The present finding gives the exact answer for the existing Selberg/Bombieri quadratic frame: **the family can indeed be summed first, but doing so produces `(9)`, not a Stadlmann-style extra oscillatory variable**.

This also clarifies the relation to two earlier obstructions:

- `MC-332` shows that arbitrary mode-dependent prime coefficients are too permissive because they can dephase each character exactly. The signature representation does not authorize such arbitrary coupling; it is the exact transform of one common coefficient vector.
- `MC-383` shows that a generic family theorem carrying a fixed positive power of the global modulus still cannot recover rank-linear source cost. The projector formulation avoids inserting such a tariff by definition, but replaces it with the concrete short-interval signature-distribution problem in `(11)`.

So the frontier is narrower, not closed. The source index itself is not the retained arithmetic variable. The remaining candidate mechanism is to exploit the **arithmetic variables that survive `(9)`**, or to prove a genuinely structured collective estimate for the signature-incidence operator that is not equivalent to reapplying individual character bounds.

## Prior art and novelty boundary

The finite-group content of `(2)`--`(7)` is classical character orthogonality/Pontryagin duality for finite abelian groups. `MC-246` already gives the closely related identity that summing an annihilator family of Dirichlet characters projects onto one multiplicative coset, so no novelty is claimed for the projector mechanism.

The Selberg expansion in `(8)`--`(11)` is the same standard sieve/Bombieri framework already audited in `MC-377`. The external comparison with Stadlmann is likewise prior art: her paper explicitly identifies the unused arithmetic summation variable and shows that retaining it changes the diagonal range from `\Delta<N/Y^2` to `\Delta<N/Y`.

A targeted mechanism-level audit on 19 September 2026 found no basis for treating the elementary composition here as a standalone novelty claim. The durable Mathia contribution is a **frontier classification** for the current endpoint construction: it performs the proposed pre-modewise source summation exactly and identifies what survives. That is enough to kill one interpretation of the averaged-source escape without claiming a new general theorem about character families.

## Boundaries and falsification tests

- **This is a statement about the current quadratic Selberg/Bombieri frame.** A genuinely different nonlinear or pre-quadratic representation is not ruled out merely because `(6)` diagonalizes the present one.
- **Common-modulus lifting is representation-preserving on the shell.** It introduces zeros on integers sharing a source prime with `P`; those terms vanish consistently in `(8)`--`(11)`. No claim is made that primitive conductors should be discarded in analytic estimates.
- **Exact residue density is not short-interval equidistribution.** From `[G:K]=H` one cannot infer that an interval shorter than `P` contains `1/H` of its integers in `K` with a useful error.
- **The outer Selberg coefficients remain signed.** Equation `(11)` is an exact expansion of the nonnegative quadratic majorant, not a termwise positive formula after the `d_1,d_2` expansion.
- **The sieve-divisor branch remains open.** The variables `d_1,d_2`, their lcm `\ell`, and any finer arithmetic variables before lcm compression may still provide the kind of retained arithmetic averaging that Stadlmann exploits. This finding does not estimate that possibility.
- **Structured collective estimates remain open.** A theorem controlling the signature-incidence operator directly could contain information not visible in worst-case individual character bounds; `(12)` only states the exact Fourier equivalence.
- **Arbitrary mode-dependent weights remain inadmissible.** Any proposed joint coefficient class must still pass the matched-filter obstruction of `MC-332`.
- **No analytic continuation or zero-free region is used.** Everything through `(12)` is finite character algebra plus the existing Selberg majorant.
- **No Möbius or RH conclusion.** The result only narrows the internal route toward a stronger source-cost/cancellation theorem.

## Consequence for the research line

The "average the source modes before bounding them" branch now has an exact normal form. In the present frame it is not an unexploited `q`-van der Corput average; it is a source-signature projector. Future work on the averaged-`q`-van der Corput clue should therefore stop treating the mode index itself as the missing variable and instead test whether an arithmetic variable surviving the Selberg expansion can be retained through differencing strongly enough to change the diagonal count, while respecting `MC-332` and avoiding the global-modulus tariff of `MC-383`.