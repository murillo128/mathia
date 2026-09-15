---
id: WP-315
title: Mangoldt atom-mass blow-ups are not locally Radon-precompact because bounded prime clusters collapse
branch: weil_positivity
status: supported
kind: support-side-atom-mass-scaling-obstruction
claim_strength: exact literature-backed obstruction for support-side localizations of the WP-304 reflected Mangoldt Herglotz source at the canonical atom-mass scale; Maynard's bounded prime clusters force arbitrarily many comparable prime atoms to collapse into every fixed normalized neighborhood, so the mass-scaled local measures are not uniformly locally bounded and no uniform isolated-pole Julia tangent exists at that scale
created: 2026-09-15
related: [WP-304, WP-305, WP-312, WP-314]
prior_art:
  - James Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), no. 1, 383-413, DOI 10.4007/annals.2015.181.1.7, arXiv:1311.4600, especially the unconditional theorem that liminf_n (p_{n+m}-p_n) is finite for every fixed m
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for the classical Julia-Nevanlinna reduction used by WP-312 and WP-314
---

# WP-315 — Mangoldt atom-mass blow-ups are not locally Radon-precompact because bounded prime clusters collapse

## Claim

`WP-314` leaves support-side moving Julia nodes as the only classical scalar moving-boundary route that can still retain the arithmetic pole geometry. A natural first attempt is to scale locally by the mass of the nearby Mangoldt atom, because for the positive source

\[
\mu=\sum_{n=p^k} a_n\,\delta_{\log n},
\qquad
a_n:=\frac{\Lambda(n)}{n+1},
\tag{1}
\]

the prime atom at `E_p=log p` has the intrinsic weight

\[
a_p=\frac{\log p}{p+1}\sim\frac{\log p}{p}.
\tag{2}
\]

That scale does **not** produce a uniformly local one-pole geometry. Define the translated, atom-mass-normalized positive measure

\[
\nu_p(B)
:=\frac1{a_p}\,
\mu\bigl(\log p+a_p B\bigr),
\qquad p\ \text{prime}.
\tag{3}
\]

Then for every fixed `r>0`,

\[
\boxed{
\limsup_{p\to\infty\atop p\ \mathrm{prime}}
\nu_p((-r,r))=+\infty.
}
\tag{4}
\]

Hence the family `{nu_p}` is not uniformly locally bounded and therefore is not relatively compact in the vague topology of locally finite positive Radon measures. There is no subsequence-independent locally finite tangent measure forced by the canonical single-atom mass normalization.

The same obstruction is visible directly in the reflected Herglotz response of `WP-305`/`WP-314`,

\[
m(z)=\int_0^\infty
\left(-\frac1{E+z}+\frac{E}{1+E^2}\right)d\mu(E).
\tag{5}
\]

At the atom-mass height above the pole `-log p`, positivity gives

\[
\operatorname{Im}m(-\log p+i a_p)
=
\sum_{n=q^k}
\frac{a_n a_p}
{(\log n-\log p)^2+a_p^2}.
\tag{6}
\]

Along bounded prime clusters, arbitrarily many prime summands in (6) tend individually to `1`. Consequently

\[
\boxed{
\limsup_{p\to\infty\atop p\ \mathrm{prime}}
\operatorname{Im}m(-\log p+i a_p)=+\infty.
}
\tag{7}
\]

Thus even the Pick/Herglotz field itself has no uniformly bounded single-pole tangent on the atom-mass scale.

There is also a two-sided boundary-node consequence. Maynard's theorem with three primes in a bounded interval yields infinitely many middle primes `p` for which the immediately adjacent prime support points on **both** sides satisfy

\[
\frac{\log p-\log p_-}{a_p}\to0,
\qquad
\frac{\log p_+-\log p}{a_p}\to0.
\tag{8}
\]

Prime-power atoms can only shorten the actual adjacent support-free intervals. Therefore any classical regular boundary node that is required to remain in one of the two gaps immediately adjacent to that focal pole must, along this subsequence, move on a scale `o(a_p)`, not on a scale comparable with `a_p`.

The conclusion is deliberately narrower than a no-go for all support-side moving nodes. A real node at distance comparable with `a_p` can still be regular if it lands in a farther gap after crossing other poles. What fails is the interpretation of the atom mass as a canonical **local isolated-pole scale**: on unavoidable prime-cluster subsequences, a mass-scale chart contains arbitrarily many comparable source atoms, while an actually adjacent regular node is forced below that scale.

**Classification:** `LITERATURE+DERIVED + EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SUPPORT-SIDE-LOCALIZATION + MAYNARD-PRIME-CLUSTERS + NONPRECOMPACT-ATOM-MASS-TANGENT + PICK/HERGLOTZ-BOUNDARY + NOT-WEIL-POSITIVITY`.

## 1. Maynard clusters collapse under the intrinsic atom-mass dilation

Maynard proves unconditionally that for every fixed integer `M>=1`,

\[
H_M:=\liminf_{n\to\infty}
(p_{n+M}-p_n)<\infty.
\tag{9}
\]

Fix `M`. Therefore there is a finite constant `C_M` and infinitely many indices `n` such that

\[
p_n<p_{n+1}<\cdots<p_{n+M},
\qquad
p_{n+M}-p_n\le C_M.
\tag{10}
\]

Choose any prime `p=p_{n+j}` in such a block. For every prime `q=p_{n+ell}` in the same block,

\[
|q-p|\le C_M.
\tag{11}
\]

As `p->infinity`, the logarithmic displacement obeys

\[
|\log q-\log p|
\le
\frac{|q-p|}{\min(p,q)}
\le
\frac{C_M}{p-C_M},
\tag{12}
\]

while (2) gives `a_p~(log p)/p`. Hence

\[
\frac{|\log q-\log p|}{a_p}
\le
\frac{C_M(p+1)}{(p-C_M)\log p}
\longrightarrow0.
\tag{13}
\]

The corresponding atom masses are asymptotically equal:

\[
\frac{a_q}{a_p}
=
\frac{\log q}{\log p}\frac{p+1}{q+1}
\longrightarrow1.
\tag{14}
\]

Now fix `r>0`. For all sufficiently large clusters satisfying (10), all `M+1` prime atoms lie inside the normalized interval `(-r,r)` around `p`. From (3), (13), and (14),

\[
\nu_p((-r,r))
\ge
\sum_{ell=0}^{M}\frac{a_{p_{n+ell}}}{a_p}
=M+1+o(1).
\tag{15}
\]

Because `M` is arbitrary, (4) follows. Notice that prime powers have been discarded in the lower bound; their presence can only increase the normalized local mass.

This is stronger than merely saying that some prime gaps are unusually small. The natural source normalization makes the focal atom have mass one, yet the number of other order-one atoms inside every fixed normalized neighborhood is not uniformly bounded. Any vague limit in the category of locally finite positive measures would require bounded mass on compact subsets, so no global tangent family can be extracted without an additional cluster-dependent normalization or a more selective subsequence hypothesis.

## 2. The Herglotz field inherits the same blow-up

For `z=x+iy` with `y>0`, the real regularizing term in (5) contributes no imaginary part, and positivity gives

\[
\operatorname{Im}m(x+iy)
=
\int_0^\infty
\frac{y}{(E+x)^2+y^2}\,d\mu(E).
\tag{16}
\]

Take

\[
x=-\log p,
\qquad
y=a_p.
\tag{17}
\]

A prime `q` in the same bounded cluster contributes exactly

\[
\frac{a_q a_p}
{(\log q-\log p)^2+a_p^2}
=
\frac{a_q/a_p}
{1+\left((\log q-\log p)/a_p\right)^2}
\longrightarrow1
\tag{18}
\]

by (13)-(14). For any fixed `M`, a cluster of `M+1` primes therefore gives

\[
\operatorname{Im}m(-\log p+i a_p)
\ge M+1+o(1).
\tag{19}
\]

Letting `M` grow proves (7).

This rules out the simplest support-side continuation of `WP-314`: there is no universal atom-mass-scaled Pick profile obtained by treating a high prime atom as one pole plus a uniformly subordinate analytic background. The obstruction is not a sign failure—the source remains positive and Herglotz throughout—but a failure of **local geometric compactness** at the very scale supplied by the atom weight.

Equivalently, after the local change of coordinate

\[
E=\log p+a_p u,
\tag{20}
\]

every prime in a bounded Maynard cluster has `u->0` and normalized weight `a_q/a_p->1`. Along cluster subsequences the nominal single pole at `u=0` is therefore accompanied by arbitrarily many comparable poles collapsing to the same normalized location. A scalar Julia reduction may still be performed at regular points between poles, but its limiting data cannot be inferred from a one-atom model on this scale.

## 3. Adjacent regular boundary nodes are forced below the mass scale

The preceding argument permits a node at distance `~a_p` to cross many poles and land in some farther support gap. To isolate the genuinely local boundary-node statement, use Maynard's theorem with `M=2`. There are infinitely many consecutive triples

\[
p_-<p<p_+
\tag{21}
\]

whose total diameter is bounded by an absolute constant `C_2` along that subsequence. Consequently

\[
0<\log p_+-\log p
\le\frac{C_2}{p},
\tag{22}
\]

and

\[
0<\log p-\log p_-
\le\frac{C_2}{p-C_2}.
\tag{23}
\]

Dividing by `a_p=log p/(p+1)` gives (8).

The full support of (1) contains every prime support point and additional prime powers. Therefore the maximal support-free component immediately to either side of `log p` has width no larger than the corresponding quantity in (22)-(23). Reflecting to the support of `m` changes only the sign of the coordinate. Hence a regular boundary node kept in either immediately adjacent gap must satisfy

\[
\frac{|x_p+\log p|}{a_p}\longrightarrow0
\tag{24}
\]

along this infinite triple-cluster subsequence.

So a side-adaptive choice does not rescue the **adjacent-gap** atom-mass ansatz. Both sides become sub-mass-scale simultaneously. What remains possible is qualitatively different: choose the actual gap scale, cross poles and use a farther gap, or treat the cluster collectively before scalarization.

## 4. Aggressive falsification and exact boundary of the result

Several stronger statements would be false or unproved and are intentionally excluded.

First, (4) does **not** say that every atom-mass-scaled subsequence diverges. Prime gaps vary strongly, and selected sparse subsequences may have locally finite tangents. The theorem says there is no tangent forced uniformly by the intrinsic mass scale across the arithmetic source.

Second, (24) does **not** say that no real regular point exists at distance comparable with `a_p`. Such a point can lie beyond neighboring support atoms. It then belongs to a different gap and its reduction necessarily samples multi-pole structure rather than a local isolated atom.

Third, no claim is made that a gap-adapted scaling fails. One can normalize by the actual neighboring support distance. But that scale is a separate arithmetic input, fluctuates with prime-power spacing, and is not determined by the positive atom mass alone. It therefore requires a fresh derivation of any canonical positive limit and of the archimedean/global counterterms.

Fourth, a cluster-dependent normalization could divide by the number or total mass of nearby atoms and restore local boundedness. That changes the proposed geometry: the normalization is no longer the single-atom invariant `a_p` and must itself be derived canonically before it can enter a Weil-positivity mechanism.

Finally, the result does not touch matrix/operator-valued reductions or a nonseparable finite-archimedean coupling performed before scalarization. Those remain genuine category changes rather than loopholes inside the single-atom scalar tangent analyzed here.

## 5. Prior-art and novelty audit

The number-theoretic input is classical. Maynard's 2015 theorem proves (9), and no novelty is claimed for bounded clusters of primes. Classical Julia-Nevanlinna reduction is likewise prior art, as already recorded in `WP-312` and `WP-314`.

The derived content here is the consequence for the specific positive Mangoldt source forced by `WP-304`: its atom weight is `log p/(p+1)`, exactly of the mean logarithmic-spacing scale `log p/p`, while Maynard supplies arbitrarily large prime clusters on the much smaller bounded-`p` scale. Equations (3)-(7) turn that mismatch into an exact local-noncompactness obstruction for the remaining support-side scalar route.

Searches around Herglotz/Julia reduction, von-Mangoldt measures, and prime-gap boundary interpolation found the classical ingredients separately but no established theorem identifying this particular atom-mass tangent obstruction. It should therefore be read as a Mathia-specific literature-backed corollary, not as a new prime-gap theorem or a new Julia-reduction theorem.

## Consequence for the research line

`WP-314` showed that moving Julia nodes on the positive empty side become universal and arithmetic-blind. The most obvious source-sensitive replacement—move to the support side and use the local Mangoldt atom mass as the intrinsic microscopic scale—now fails to define a uniform local geometry:

\[
\boxed{
\text{empty-side global scale}
\Rightarrow\text{universal logarithmic tangent},
\qquad
\text{support-side atom-mass scale}
\Rightarrow\text{nonprecompact prime-cluster collapse}.
}
\tag{25}
\]

A viable support-side continuation must therefore use information beyond one atom's positive weight. The remaining scalar possibilities are spacing-adapted or genuinely collective multi-pole constructions; otherwise the search should move to matrix/operator-valued or finite-archimedean coupled geometry. None of these remaining possibilities yet supplies the independent global Weil positivity required by the line mandate.
