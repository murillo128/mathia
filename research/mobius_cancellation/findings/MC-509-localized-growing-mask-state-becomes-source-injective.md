# MC-509 — Localized growing mask state becomes source-injective

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-508` proves that fixing the conductor phase and any **fixed finite** set of lower-prime mask roots does not constrain the first-exit prime: Chinese remaindering plus Dirichlet lets the same finite local data recur at arbitrarily distant primes. That leaves source localization and the full growing lower-prime profile as the live escape.

Localization changes the information geometry in the opposite direction from the one a profile-averaging argument would like. Once enough lower-prime mask coordinates are retained, the truncated root profile becomes a residue-number code for the first-exit prime itself.

Fix a conductor prime `p`, a nonzero shift `h`, and a nonzero conductor residue `a mod p`. Let `I` be an interval of integers of diameter at most `H`, and suppose every source prime `q in I` satisfies

\[
q\equiv a\pmod p.
\tag{1}
\]

Choose a cutoff `z<\min I`, and let

\[
\mathcal S_z
=\{\ell\le z:\ \ell\text{ prime},\ \ell\ne p,\ \ell\nmid h\},
\qquad
M_z=\prod_{\ell\in\mathcal S_z}\ell.
\tag{2}
\]

For each source prime `q`, retain the lower-prime moving-mask root coordinates already used in `MC-508`,

\[
\rho_\ell(q)\equiv-hq^{-1}\pmod\ell,
\qquad \ell\in\mathcal S_z.
\tag{3}
\]

Then equality of truncated profiles forces

\[
\boxed{
(\rho_\ell(q))_{\ell\in\mathcal S_z}
=(\rho_\ell(r))_{\ell\in\mathcal S_z}
\quad\Longrightarrow\quad
q\equiv r\pmod{pM_z}.
}
\tag{4}
\]

Consequently every profile fibre inside `I` has size at most

\[
\boxed{
1+\left\lfloor\frac{H}{pM_z}\right\rfloor,
}
\tag{5}
\]

and in particular

\[
\boxed{pM_z>H\quad\Longrightarrow\quad
q\mapsto(\rho_\ell(q))_{\ell\in\mathcal S_z}
\text{ is injective on the localized source set}.}
\tag{6}
\]

Because

\[
\log M_z=\sum_{\substack{\ell\le z\\ \ell\nmid hp}}\log\ell
=(1+o(1))z,
\tag{7}
\]

the injective regime is reached after only logarithmic mask depth. For example, in a dyadic source block `I=[Q,2Q]`, if `Q/p\to\infty`, then for every fixed `\varepsilon>0`,

\[
z=(1+\varepsilon)\log(Q/p)
\tag{8}
\]

satisfies `pM_z>Q` for all sufficiently large `Q`. If `Q\le p`, the fixed conductor residue already gives at most one source integer in any interval of diameter `<p`, even before any lower-prime coordinate is retained.

Thus the full localized growing mask state has a sharp representation-level danger:

> **past the CRT dynamic range, the profile is no longer a coarse arithmetic class over which source labels can average; it is an essentially lossless address for the source prime.**

This does not show that the physical hard-mask coefficient profile `B_{x,j}` is injective, and it does not bound the `MC-506` anti-diagonal collision excess. Different root vectors can still induce coefficient patterns whose mass collides after the physical map `t=x+j`. The result is instead a first-kill test for a tempting use of the surviving `MC-508` escape: exact conditioning on progressively more local mask roots cannot itself create repeated-profile averaging once the retained modulus exceeds the localized source width.

## 1. Exact CRT proof

Take source primes `q,r>z` satisfying `(1)` and suppose their root vectors in `(3)` agree. For every `ell in S_z`, both `q` and `r` are units modulo `ell`, and `h` is a unit modulo `ell`. Therefore

\[
-hq^{-1}\equiv-hr^{-1}\pmod\ell
\]

implies

\[
q^{-1}\equiv r^{-1}\pmod\ell
\quad\Longrightarrow\quad
q\equiv r\pmod\ell.
\tag{9}
\]

The moduli in `S_z` are pairwise coprime, so `(9)` gives

\[
q\equiv r\pmod{M_z}.
\tag{10}
\]

They also obey the same conductor condition `(1)`. Since `p` is excluded from `S_z`, `(p,M_z)=1`, hence

\[
q\equiv r\pmod{pM_z},
\]

which is `(4)`.

An interval of diameter at most `H` contains at most

\[
1+\left\lfloor\frac{H}{pM_z}\right\rfloor
\]

integers in one residue class modulo `pM_z`, proving `(5)` and `(6)`. Notice that primality is not needed for this counting step; restricting to primes can only decrease the fibre size.

The map in `(3)` is just a coordinatewise invertible recoding of the ordinary residue vector of `q` modulo the product `M_z`: multiplication by `-h` and inversion are permutations of each `F_ell^*`. The conductor coordinate adds the independent modulus `p`. Hence the representation has exact CRT dynamic range `pM_z` on the allowed unit classes.

## 2. The growing profile reaches source-label scale quickly

Let `theta(z)=sum_{ell<=z} log ell` be Chebyshev's theta function. Removing the fixed prime divisors of `h` changes this sum by only `O_h(1)`, and excluding `p` changes it by at most `log z` when `p<=z`. Therefore the prime number theorem in the equivalent form `theta(z)~z` gives `(7)`.

Suppose `I=[Q,2Q]`, so `H=Q`, and `Q/p->infinity`. With `z` as in `(8)`,

\[
\log M_z=(1+o(1))(1+\varepsilon)\log(Q/p),
\]

so

\[
pM_z
=p(Q/p)^{1+\varepsilon+o(1)}
=Q\,(Q/p)^{\varepsilon+o(1)}
>Q
\]

for sufficiently large `Q`. Also `z=o(Q)`, so the required `z<min I` is automatic in this asymptotic regime.

The number of retained coordinates is only

\[
\pi(z)\asymp \frac{\log(Q/p)}{\log\log(Q/p)}
\]

when the ratio tends to infinity. The important resource, however, is not the coordinate count but their aggregate logarithmic modulus budget:

\[
\log(pM_z)\simeq\log H.
\tag{11}
\]

This is exactly the information scale required to distinguish `H/p` possible integers in one conductor residue class. The growing root profile therefore crosses from a low-information local decoration into a source-identity code at the natural CRT capacity threshold; it does not furnish a free extra averaging dimension.

## 3. Consequence for the `MC-503`--`MC-508` frontier

The current hard-mask branch has successively isolated what a positive theorem would need:

- `MC-503` shows that a **fixed** hard-mask profile can sustain order-one normalized conductor bias only on a sparse set of starts unless its effective profile support is small.
- `MC-504` prices repeated exact profile classes through the product of source/start participation and profile support.
- `MC-505`--`MC-506` remove the need to choose profile classes and identify the physical anti-diagonal pushforward as the complete statistic seen by the centered conductor kernel.
- `MC-507` proves that marginal regularity does not control those anti-diagonal collisions.
- `MC-508` proves that finitely many fixed lower-prime mask coordinates remain programmable when the realizing prime is allowed to escape the source range.

The present result closes one naive reaction to `MC-508`: **retain more and more exact local coordinates until localization forces rigidity, then hope the resulting exact profile classes provide averaging.** Once `pM_z>H`, those exact root-state classes contain at most one localized source prime. The rigidity is real, but it is source identification rather than recurrence.

More generally, before using a truncated root state as a conditioning variable, its fibre budget should be charged by `(5)`. In the transition range `pM_z<=H`, a profile can recur at most `1+H/(pM_z)` times. Each newly retained prime modulus shrinks this upper bound multiplicatively. Any argument whose gain comes from many source labels sharing one exact root profile therefore gets weaker, not stronger, as the mask state approaches the full localized profile.

This is consistent with the source-information budget in `MC-434`--`MC-435`: canonical local decorations become source-specific only by paying enough aggregate label capacity. Here the payment can be computed exactly because the labels are CRT coordinates, and the dynamic range is `pM_z`.

## 4. What remains genuinely open

Injectivity of the root state is **not** a no-go for using the growing profile itself. An injective representation can carry useful arithmetic structure; it simply cannot be treated as a repeated coarse class for free averaging.

The `MC-506` target remains

\[
\Delta(B)=p\sum_t\left(\frac{c_t}{W}-\frac1p\right)^2,
\qquad
c_t=\sum_x B_{x,t-x},
\tag{12}
\]

for the actual localized coefficient table. Equation `(6)` gives no bound for `(12)`: distinct source primes with distinct root states may still send their mass to the same physical sum coordinate `t`, or may anti-correlate in a useful way. Nor does `(6)` say that the finite physical coefficient vector produced after clipping to an overlap segment uniquely determines the root tuple; distinct arithmetic root states can become observationally identical after scalarization or truncation.

The surviving positive mechanism must therefore use the growing state **relationally**, without conditioning away the source population. Plausible theorem surfaces now have to look like one of the following:

- a direct relation between changes in the CRT root state and displacement of the physical `x+j` coordinate;
- an averaged collision estimate over many distinct root states, with the source coefficients inserted before Cauchy/absolute values;
- a localization theorem showing that the specific map from source prime to coefficient table cannot align too much mass on one anti-diagonal;
- a genuinely signed or complex pre-aggregation identity in which the source-label dependence cancels before the nonnegative table `B` is formed.

What is no longer a live explanation is “the exact full mask profile repeats often enough to average the starts.” At logarithmic CRT depth it generically has enough capacity to name the localized source.

## Prior art and novelty boundary

The mathematical core is classical Chinese remainder theory. A tuple of residues modulo pairwise coprime moduli determines one residue class modulo their product; this is the standard dynamic-range statement behind residue-number systems. H. L. Garner, *The Residue Number System*, IRE Transactions on Electronic Computers **EC-8** (1959), no. 2, 140--147, DOI `10.1109/TEC.1959.5219515`, is classical adjacent literature for that representation viewpoint.

Likewise `log prod_{ell<=z} ell = theta(z)` and `theta(z)~z` are standard consequences/equivalents of the prime number theorem. No novelty is claimed for CRT reconstruction, residue-number systems, primorial growth, or the information-scale interpretation of a modulus product.

A targeted prior-art audit on 24 September 2026 found the expected residue-number-system formulation of CRT dynamic range and standard primorial/Chebyshev growth, but no reason to treat `(4)`--`(8)` as a new number-theory theorem. The durable Mathia contribution is the **line-specific frontier specialization**: the moving lower-prime roots from `MC-508`, when combined with the fixed conductor residue and the actual source localization, cross into a near-lossless source label after only logarithmic CRT depth. This sharply distinguishes localization-induced rigidity from the repeated-profile averaging resource sought in `MC-503`--`MC-504`.

## Boundaries and falsification tests

- **Exact root-state equality is load-bearing.** The theorem concerns the arithmetic coordinates `rho_ell(q)`, not equality of the clipped finite coefficient profiles ultimately entering `B_{x,j}`. Coefficient-profile fibres can be larger or smaller and require their own derivation.
- **Localization is load-bearing.** Without an interval restriction, `MC-508` applies: every finite root vector recurs at infinitely many primes in the corresponding CRT/Dirichlet class.
- **The conductor residue is charged explicitly.** The dynamic range is `pM_z`, not merely `M_z`. If conductor phase is not fixed, remove the factor `p` from `(4)`--`(6)`.
- **Primes dividing `h` are excluded.** Their local root coordinate is degenerate and contributes no invertible residue information. Omitting finitely many such primes does not change `(7)` for fixed `h`.
- **`z<min I` avoids a source prime appearing among the reconstruction moduli.** The asymptotic dyadic specialization satisfies this automatically.
- **Injectivity is not cancellation.** A one-to-one source representation gives no sign estimate, no character-sum saving, and no bound for `M(x)`.
- **Injectivity is not anti-diagonal dispersion.** The map from source labels/root states to the physical addition coordinate can still concentrate badly; `MC-506` remains the required target.
- **No random model is used.** The fibre bound is deterministic and exact.
- **No zero-free information or analytic continuation is used.** The asymptotic compression threshold needs only standard prime-distribution input far weaker in role than an RH-scale statement; the finite formula `(5)` itself is pure CRT.

The immediate next first-kill test is therefore more specific than after `MC-508`: do **not** seek rigidity by conditioning on an ever longer exact mask-root tuple. Instead derive the source-to-anti-diagonal map while keeping those distinct root states in the same average, and ask whether localization plus their structured CRT evolution forces the collision excess `(12)` below the level required by `MC-506`.