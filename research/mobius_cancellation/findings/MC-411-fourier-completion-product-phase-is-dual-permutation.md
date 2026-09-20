# MC-411 — Fourier completion of the product character phase is only a dual-mode permutation

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The ordinary additive Fourier completion suggested as a possible escape after `MC-410` does **not** create the missing nonseparable arithmetic variable for the factorable upper-sieve form.

Let `chi` be a primitive Dirichlet character modulo `q`, let `r` be an integer, and let `(a_m)` be any finitely supported complex sequence. If `(r,q)=1`, then

\[
\boxed{
\sum_m a_m\chi(rm)=\chi(r)\sum_m a_m\chi(m).
}
\tag{1}
\]

This is of course immediate from complete multiplicativity. The point relevant to the current frontier is that **performing additive completion first does not evade `(1)`**. Using the finite Fourier expansion of a primitive character,

\[
\chi(n)=\frac{\tau(\chi)}{q}
\sum_{h\bmod q}\overline{\chi}(h)e(-hn/q),
\qquad e(x):=e^{2\pi i x},
\tag{2}
\]

one obtains

\[
\sum_m a_m\chi(rm)
=
\frac{\tau(\chi)}q
\sum_{h\bmod q}\overline{\chi}(h)
\sum_m a_m e(-hrm/q).
\tag{3}
\]

The apparent bilinear phase `e(-hrm/q)` is spurious. Since multiplication by the unit `r` permutes the residue classes modulo `q`, set `k=hr (mod q)`. Then

\[
\overline{\chi}(h)
=
\overline{\chi}(kr^{-1})
=
\chi(r)\overline{\chi}(k),
\tag{4}
\]

and `(3)` becomes exactly

\[
\chi(r)\frac{\tau(\chi)}q
\sum_{k\bmod q}\overline{\chi}(k)
\sum_m a_m e(-km/q),
\tag{5}
\]

which is `(1)` again.

Thus multiplication by a source coefficient in the primal variable becomes only a **permutation of additive Fourier modes plus the same scalar character factor** in the dual variable. Ordinary completion cannot turn the raw product phase `chi(rm)` into the reciprocal, translated, or Kloosterman-type geometry needed to defeat the separability obstruction of `MC-410`.

For the factorable upper-sieve representation `r=uv`, this means that completing the `m`-sum in

\[
\sum_{uvm\le N}\alpha_u\beta_v\chi(uvm)
\tag{6}
\]

does not create arithmetic coupling between `(u,v)` and a dual frequency. If the cutoff is sharp, the completed kernel still carries `u,v` only through the scalar `chi(uv)` and the archimedean length `N/(uv)`. If the cutoff is smooth, the Fourier transform has the same property: the scale depends on `uv`, but the residue-class phase can be reindexed away.

If `(r,q)>1`, then `chi(rm)=0` for every `m`; those terms vanish rather than produce a new coupling. Hence the conclusion covers every term of the source-character sum.

This removes **plain one-variable completion/Poisson summation** from the list of possible mechanisms that might rescue `MC-409`. A surviving transform must contain additional arithmetic data that obstructs the dual reindexing—for example an additive translation, a congruence comparing two independently varying products, a reciprocal variable, or another relation in which `r` cannot be absorbed by permuting Fourier modes.

No estimate for `M(x)` follows.

## 1. Completion is equivariant under multiplication by units

For a primitive character, the Gauss sum is separable and the finite Fourier expansion `(2)` is exact. Let

\[
\widehat a_q(h):=\sum_m a_m e(-hm/q).
\tag{7}
\]

Then `(3)` may be written

\[
\sum_m a_m\chi(rm)
=
\frac{\tau(\chi)}q
\sum_{h\bmod q}\overline{\chi}(h)\widehat a_q(hr).
\tag{8}
\]

For `(r,q)=1`, the map `h -> hr` is a permutation of `Z/qZ`. Equation `(4)` therefore gives

\[
\boxed{
\sum_{h\bmod q}\overline{\chi}(h)\widehat a_q(hr)
=
\chi(r)
\sum_{k\bmod q}\overline{\chi}(k)\widehat a_q(k).
}
\tag{9}
\]

The additive Fourier transform has not produced a second source coordinate. It has merely moved the action of the multiplicative dilation `m -> rm` to the permutation `h -> hr` on the dual group. The primitive character is an eigenvector for this action, with eigenvalue `chi(r)`.

This is the Fourier-side form of the convolution-algebra statement in `MC-410`: the source character diagonalizes multiplicative dilation before and after completion.

## 2. Smooth Poisson completion also leaves only archimedean coupling

Let `W` be a Schwartz function and consider, for `r>=1`,

\[
T_r(N):=\sum_{m\in\mathbf Z}\chi(rm)W(rm/N).
\tag{10}
\]

When `(r,q)=1`, complete multiplicativity gives

\[
T_r(N)
=
\chi(r)\sum_m\chi(m)W\!\left(\frac{m}{N/r}\right).
\tag{11}
\]

Applying `(2)` and ordinary Poisson summation to the right-hand side expresses `(11)` as a dual sum whose Fourier-transform argument is scaled by `N/(rq)`. The only dependence on `r` is therefore

1. the scalar `chi(r)`; and
2. the real scale `N/r` in the transformed weight.

There is no residual congruence or phase relating `r` to the dual frequency. Equivalently, applying `(2)` before Poisson and starting from `chi(rm)` gives a phase `e(-hrm/q)`, but the change of dual variable `k=hr` used in `(4)` removes `r` from that phase exactly.

Therefore a product cutoff can still couple variables through support length, as already noted in `MC-410`, but ordinary completion converts none of that archimedean dependence into new arithmetic geometry.

## 3. Consequence for the `MC-409` factorable upper-sieve form

For one well-factorable component,

\[
S_\chi(N)=
\sum_{u,v}\alpha_u\beta_v\chi(uv)
M_\chi\!\left(\frac{N}{uv}\right).
\tag{12}
\]

A natural next attempt after `MC-410` is to complete the inner character sum. Equations `(8)`--`(11)` show exactly what happens: for each fixed `(u,v)`, the modular factor `uv` can be absorbed by a permutation of the dual frequency whenever it is a unit modulo the conductor, while nonunits contribute zero. The transformed sum therefore still has the schematic form

\[
\sum_{u,v}
\alpha_u\beta_v\chi(uv)
\sum_h\overline{\chi}(h)
\mathcal W\!\left(h;\frac{N}{uv},q\right),
\tag{13}
\]

where the `(u,v)` dependence inside `mathcal W` is through an archimedean length/scale, not a new residue relation.

This is not the geometry exploited by well-factorable distribution theorems. In those the factorable variable participates in a progression modulus or another arithmetic constraint before dispersion/completion. Here it is only a multiplicative scalar in the fixed source character.

Accordingly, a future argument cannot claim a new bilinear phase merely because additive completion displays `h uv m` in an exponential. Before estimating, one must first perform the invertible reindexing `(4)`. Any claimed gain that disappears under that reindexing is a coordinate artifact.

## 4. What remains live

The obstruction is specific and does not kill all transforms.

A translated phase such as

\[
\chi(rm+a)
\]

cannot be reduced to `chi(r)chi(m)` when `a` is nonzero; likewise a congruence coupling two products or a reciprocal/Kloosterman phase can retain the outer variable after completion. This is why genuinely bilinear multiplicative-character literature studies phases with additive structure rather than the bare product `chi(rm)`.

For example, Chang and Shparlinski study double character sums with phases of the form `chi(x+a lambda)` over an interval and a multiplicative subgroup. That is structurally different from the present product phase: the translation prevents the multiplicative scalarization used in `(1)` and the dual permutation used in `(4)`.

The current route therefore remains alive only if dispersion or another identity **first creates a relation not equivariant under multiplication of the completed variable by `uv`**. Completion may then help estimate that new relation, but completion itself is not the source of the missing arithmetic dimension.

## Prior art and novelty boundary

The finite Fourier expansion and separability of Gauss sums for primitive Dirichlet characters are classical. NIST DLMF §27.10, equations 27.10.10--27.10.12, records both the separability identity and the finite Fourier expansion used in `(2)`. No novelty is claimed for these formulas, Poisson summation, or the fact that multiplication by a unit permutes residue classes.

As a comparison class, Mei-Chu Chang and Igor E. Shparlinski, *Double Character Sums over Subgroups and Intervals* (2014), arXiv:1401.6611, estimate genuinely nonseparable sums containing `chi(x+a lambda)`. The paper is used only to mark the structural boundary between a translated multiplicative-character phase and the separable product phase here.

The line-specific durable result is the frontier classification: the most immediate `MC-410` completion escape is an exact dual-coordinate reparameterization and therefore cannot supply the retained arithmetic variable sought by the accepted source-frame clue.

## Boundaries and falsification tests

- **Primitive conductor is the natural completion modulus.** The argument is stated for the primitive character attached to a source mode. An imprimitive presentation at a larger common modulus may add zero masks, but it cannot be credited as new oscillation without showing that those masks survive as analytically useful arithmetic structure.
- **Archimedean dependence survives.** The length `N/(uv)` can matter analytically; the result says only that ordinary additive completion does not turn it into a modular phase coupling `uv` to the dual frequency.
- **A translated or reciprocal phase is not covered.** Those are precisely the structures that can prevent the reindexing `(4)` and remain legitimate candidates.
- **Family averaging is not covered.** Averaging several source characters may create covariance constraints; those must be audited separately against the source-signature collapse already identified in `MC-397`.
- **No estimate is inferred from completion.** The statement is structural, not a Burgess, Pólya--Vinogradov, large-sieve, or Mertens bound.

## Consequence for the research line

`MC-410` showed that coefficient factorization does not itself entangle the source character. `MC-411` now shows that the simplest proposed way to manufacture such entanglement—ordinary Fourier/Poisson completion of the inner character sum—also fails exactly: the apparent product phase in the additive dual variable is a permutation artifact.

The next admissible step is narrower. Start from an identity that already contains a nontrivial additive/congruence/reciprocal relation between independently varying factor variables, then test whether well-factorability lowers the resulting diagonal or source-cost term. Applying completion to the raw product-character form before such a relation exists cannot do so.