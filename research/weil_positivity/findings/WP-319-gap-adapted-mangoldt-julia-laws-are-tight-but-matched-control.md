---
id: WP-319
title: Gap-adapted Mangoldt Julia laws are tight but limit to matched-control inverse-square lattice profiles
branch: weil_positivity
status: supported
kind: gap-adapted-mangoldt-derivative-law-compactness-and-control-obstruction
claim_strength: exact literature-backed compactness and subsequential-limit classification for the WP-318 derivative-biased Mangoldt probability laws at regular mid-gap nodes selected from infinitely many Maynard bounded prime-gap neighborhoods; normalizing by the actual adjacent prime-power support gap repairs the atom-mass noncompactness of WP-315 and yields inverse-square probability laws on a shifted arithmetic lattice, but every such limit remains exactly realizable by a non-arithmetic positive Herglotz matched control, so the recovered local arithmetic fingerprint does not make scalar Julia positivity source-selective or supply the archimedean/global Weil terms
created: 2026-09-15
related: [WP-304, WP-315, WP-318]
prior_art:
  - James Maynard, Small gaps between primes, Annals of Mathematics 181 (2015), no. 1, 383-413, DOI 10.4007/annals.2015.181.1.7, arXiv:1311.4600, for the unconditional existence of infinitely many bounded gaps between consecutive primes and, more generally, bounded prime clusters
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for classical Julia-Nevanlinna reduction and Pick-class preservation
  - Roland Speicher and Reza Woroudi, Boolean convolution, Fields Institute Communications 12 (1997), 267-279, DOI 10.1090/fic/012/13, for the Boolean K-transform/self-energy framework used in WP-318
---

# WP-319 — Gap-adapted Mangoldt Julia laws are tight but limit to matched-control inverse-square lattice profiles

## Claim

`WP-315` proved that the intrinsic Mangoldt **atom-mass** scale is not locally precompact: bounded prime clusters collapse arbitrarily many order-one atoms into every fixed normalized neighborhood. It explicitly left open the different possibility of scaling by the **actual adjacent support gap**. `WP-318` then showed that every regular scalar Julia response is completely determined, after affine normalization, by its derivative-biased probability law.

For the reflected Mangoldt source, the gap-adapted route can now be classified on an unavoidable infinite family of microscopic gaps. Let

\[
\mu=\sum_{n\ge2} a_n\,\delta_{-\log n},
\qquad
a_n:=\frac{\Lambda(n)}{n+1},
\tag{1}
\]

where terms with `Lambda(n)=0` are absent. Maynard's bounded-gap theorem supplies infinitely many primes `p_j` having a later prime within a fixed additive distance `B`. Let `m_j` be the **least prime power strictly larger than** `p_j`. Then

\[
1\le d_j:=m_j-p_j\le B,
\tag{2}
\]

so, after passing to an infinite subsequence, `d_j=d` is constant.

The interval between `-log m_j` and `-log p_j` is support-free. Put its midpoint and width

\[
t_j:=-\frac{\log p_j+\log m_j}{2},
\qquad
g_j:=\log\frac{m_j}{p_j}.
\tag{3}
\]

Let `nu_j` be the derivative-biased probability law of `WP-318` at `t_j`, and push it to the **gap coordinate**

\[
u=\frac{x-t_j}{g_j}.
\tag{4}
\]

Call the resulting probability law `rho_j`. Then:

1. the family `{rho_j}` is tight;
2. every subsequence has a further subsequence for which there are coefficients

\[
\theta_h\in\{0\}\cup\left\{\frac1k:k\in\mathbb N\right\},
\qquad h\in\mathbb Z,
\tag{5}
\]

with

\[
\theta_0=1,
\qquad
\theta_h=0\quad(0<h<d),
\tag{6}
\]

such that

\[
\boxed{
\rho_j\Longrightarrow
\rho=
\frac1Z
\sum_{h\in\mathbb Z\atop h\ne d/2}
\frac{\theta_h}{(h-d/2)^2}
\,\delta_{\,1/2-h/d},
}
\tag{7}
\]

where zero coefficients contribute no atom and

\[
Z=
\sum_{h\in\mathbb Z\atop h\ne d/2}
\frac{\theta_h}{(h-d/2)^2}
\in(0,\infty).
\tag{8}
\]

If `d` is even, the omitted index `h=d/2` lies strictly inside the support-free gap, so its coefficient is identically zero before taking the limit.

Thus the actual support-gap scale **does repair local compactness**. The surviving scalar arithmetic data are concrete: a shifted integer lattice and reciprocal-square derivative bias, decorated by limiting prime-power coefficients `theta_h`.

But this does not produce a Weil sign mechanism. The limit support stays a positive distance from the normalized node `0`, and `WP-318` constructs, for **every** such probability law `rho`, a non-arithmetic positive Herglotz measure whose derivative-biased law is exactly `rho`. Consequently the normalized Julia profile

\[
-K_\rho(\zeta)
\tag{9}
\]

has the same universal Pick positivity in the arithmetic source and in a matched control. Gap normalization recovers a local arithmetic fingerprint, not source-selective positivity, and it still produces no Gamma term or global counterterm.

**Classification:** `LITERATURE+DERIVED + EXACT-DERIVED + POSITIVE-COMPACTNESS + SUBSEQUENTIAL-CLASSIFICATION + GAP-ADAPTED-SCALING + DERIVATIVE-BIASED-MANGOLDT-LAW + INVERSE-SQUARE-LATTICE + MATCHED-CONTROL-OBSTRUCTION + SCALAR-JULIA + NOT-WEIL-POSITIVITY`.

## 1. Bounded prime gaps force infinitely many bounded prime-power support gaps

Maynard proves in particular that there is a finite constant `B` and infinitely many pairs of consecutive primes

\[
p_j<q_j,
\qquad
q_j-p_j\le B.
\tag{10}
\]

For each such left endpoint `p_j`, let `m_j` be the least integer greater than `p_j` with `Lambda(m_j)>0`. Because `q_j` itself is prime,

\[
p_j<m_j\le q_j,
\tag{11}
\]

which proves (2). Since `d_j` is an integer in the finite set `{1,...,B}`, one value `d` occurs infinitely often. Restrict to that subsequence:

\[
m_j=p_j+d.
\tag{12}
\]

By construction there is no prime power strictly between `p_j` and `p_j+d`; therefore (3) is a genuine regular boundary node for the reflected support (1). The logarithmic gap satisfies

\[
g_j=\log\left(1+\frac d{p_j}\right)
=\frac d{p_j}+O(p_j^{-2}).
\tag{13}
\]

This scale is qualitatively different from the atom-mass scale of `WP-315`:

\[
a_{p_j}\sim\frac{\log p_j}{p_j},
\qquad
\frac{g_j}{a_{p_j}}\sim\frac d{\log p_j}\to0.
\tag{14}
\]

So bounded prime clustering forces the adjacent regular gap to live precisely in the sub-mass regime that `WP-315` identified but did not classify.

## 2. Derivative bias gives a uniformly tight gap-scale family

Write

\[
D_j:=
\sum_{n\ge2}
\frac{a_n}{(\log n-\ell_j)^2},
\qquad
\ell_j:=\frac{\log p_j+\log(p_j+d)}2.
\tag{15}
\]

This is the finite positive boundary derivative at `t_j=-ell_j`. The pushed-forward probability `rho_j` places at

\[
u_{j,n}:=
\frac{\ell_j-\log n}{g_j}
\tag{16}
\]

the mass

\[
\rho_j(\{u_{j,n}\})
=
\frac{a_n/(\log n-\ell_j)^2}{D_j}.
\tag{17}
\]

The focal prime alone gives the lower bound

\[
D_j\ge
\frac{a_{p_j}}{(g_j/2)^2}
=\frac{4a_{p_j}}{g_j^2}
\asymp p_j\log p_j.
\tag{18}
\]

To control the rest, first restrict to `p_j/2<=n<=2p_j` and write `n=p_j+h`. On this range the mean-value theorem gives constants independent of `j` such that

\[
|\log n-\ell_j|
\asymp
\frac{|h-d/2|}{p_j}
\tag{19}
\]

away from the empty interior of the gap. Since `Lambda(n)<=log n`,

\[
\frac{a_n}{(\log n-\ell_j)^2}
\ll
\frac{p_j\log p_j}{(h-d/2)^2}.
\tag{20}
\]

Moreover `|u_{j,n}|>R` implies `|h-d/2|\gg_d R` for large `j`. Hence

\[
\sum_{p_j/2\le n\le2p_j\atop |u_{j,n}|>R}
\frac{a_n}{(\log n-\ell_j)^2}
\ll_d
\frac{p_j\log p_j}{R}.
\tag{21}
\]

The distant tails are smaller. The classical Chebyshev bound `psi(x)=sum_{n<=x} Lambda(n)=O(x)` and partial summation give

\[
\sum_{n<p_j/2}
\frac{a_n}{(\log n-\ell_j)^2}
=O(\log p_j),
\tag{22}
\]

while dyadic decomposition of `n>=2p_j` gives

\[
\sum_{n\ge2p_j}
\frac{a_n}{(\log n-\ell_j)^2}
=O(1).
\tag{23}
\]

Indeed, on `2^k p_j<=n<2^{k+1}p_j` the logarithmic denominator is `gg k^2`, whereas `sum Lambda(n)/n=O(1)` on each such dyadic block by `psi(x)=O(x)`.

Dividing (21)-(23) by (18) yields

\[
\limsup_{j\to\infty}
\rho_j(\{|u|>R\})
\ll_d\frac1R.
\tag{24}
\]

Therefore `{rho_j}` is tight. This is the exact opposite of the atom-mass blow-up in `WP-315`: using the actual support gap as the affine unit produces probability-law precompactness along this unavoidable bounded-gap family.

## 3. Every limit is an inverse-square arithmetic-mesh law

For each fixed integer `h`, define

\[
\theta_j(h):=
\frac{\Lambda(p_j+h)}{\log p_j}.
\tag{25}
\]

For fixed `h`, these coefficients are bounded. A diagonal subsequence makes `theta_j(h)` converge for every `h in Z`; write the limit as `theta_h`.

If `p_j+h` is not a prime power, the coefficient is zero. If

\[
p_j+h=r_j^{k_j},
\tag{26}
\]

then

\[
\theta_j(h)
=
\frac1{k_j}
\frac{\log(p_j+h)}{\log p_j}
=\frac1{k_j}+o(1).
\tag{27}
\]

After a further subsequence, either `k_j` is a fixed positive integer or `k_j->infinity`. This proves the quantization (5). Since `p_j` is prime, `theta_0=1`; because `(p_j,p_j+d)` contains no prime power, (6) holds.

For fixed `h`, (13) gives

\[
u_{j,p_j+h}
=
\frac{\frac12\log(1+d/p_j)-\log(1+h/p_j)}
{\log(1+d/p_j)}
\longrightarrow
\frac12-\frac hd.
\tag{28}
\]

Also

\[
p_j\bigl(\log(p_j+h)-\ell_j\bigr)
\longrightarrow h-\frac d2.
\tag{29}
\]

Consequently

\[
\frac1{p_j\log p_j}
\frac{a_{p_j+h}}
{(\log(p_j+h)-\ell_j)^2}
\longrightarrow
\frac{\theta_h}{(h-d/2)^2}
\tag{30}
\]

for every nonempty limiting support site. The tail estimate (24), applied before normalization together with the same reciprocal-square majorant, allows passage from every finite window to the full sum. Thus

\[
\frac{D_j}{p_j\log p_j}
\longrightarrow Z
\tag{31}
\]

with `Z` given by (8), and (7) follows. Positivity and `theta_0=1` give

\[
Z\ge\frac4{d^2}>0,
\tag{32}
\]

while `theta_h<=1` and the reciprocal-square tail give `Z<infinity`.

The limiting law is therefore not an unspecified compactness point. It is a rigid **arithmetic-mesh inverse-square law**: normalized gap geometry fixes the shifted lattice `1/2-(1/d)Z`, Julia derivative bias supplies the inverse-square envelope, and the remaining source information is the local prime-power pattern encoded by `theta_h`.

## 4. Julia profiles converge, but their sign remains universal

Choose the affine chart in `WP-318` with base point `x_0=t_j`, scale `r=g_j`, and normalized node `tau=0`. Its exact identity becomes

\[
\frac{\mathcal J_{t_j}[f](t_j+g_j\zeta)-\beta_j}
{D_j g_j}
=
-K_{\rho_j}(\zeta).
\tag{33}
\]

Tightness plus weak convergence in (7) gives local uniform convergence of Cauchy transforms on the upper half-plane and therefore

\[
-K_{\rho_j}(\zeta)
\longrightarrow
-K_\rho(\zeta)
\tag{34}
\]

locally uniformly away from the real support singularities.

The gap coordinate also preserves a uniform hole around the boundary node. The original interval between the two adjacent support atoms maps exactly to `(-1/2,1/2)`, so

\[
\operatorname{supp}\rho\cap(-1/2,1/2)=\varnothing.
\tag{35}
\]

Now apply the matched-control construction of `WP-318`. For this **same** probability law `rho`, define on the normalized line

\[
d\mu_\rho(u):=u^2\,d\rho(u).
\tag{36}
\]

It is a positive Herglotz measure, `0` is a regular node by (35), and derivative bias at `0` returns exactly `rho`. Hence a non-arithmetic positive source has the identical normalized Julia response

\[
-K_\rho(\zeta).
\tag{37}
\]

The sign of (34) is therefore not a theorem about primes. What is arithmetic is the selection of the particular coefficients `theta_h`; what is positive is the same Boolean/Pick theorem available to every gap-supported probability law.

This distinction matters for the line mandate. A local source fingerprint can be real and nontrivial while still failing to explain global Weil positivity if the positive theorem never uses the fingerprint.

## 5. Aggressive falsification and exact boundary

Several tempting stronger conclusions do not follow.

First, this is **not** a unique tangent theorem. The coefficient pattern `theta_h` depends on bounded-offset prime-power constellations along the chosen subsequence. Current bounded-gap theorems supply the existence of bounded clusters, not a canonical limiting constellation with all coefficients fixed. Gap scaling restores compactness, but it does not by itself choose one universal arithmetic law.

Second, (7) is not a finite-multipole statement. The limit may have infinitely many nonzero `theta_h`. The point is instead that even an infinite collective limit is confined to a reciprocal-square lattice class. `WP-318` then shows that scalar Julia positivity is still universal for that entire probability class.

Third, matched-control realizability of each limit law does not prove that one fixed non-arithmetic source reproduces the full family of arithmetic gap tangents simultaneously. Accordingly this finding does **not** close every possible family-level rigidity theorem for the Mangoldt derivative-biased laws. A surviving scalar route would have to use a coherent relation among many gaps that generic controls cannot satisfy, not merely positivity of any one tangent.

Fourth, the arithmetic mesh scale comes from the actual adjacent support gap. It is therefore source-sensitive information rather than an invariant extracted from positivity alone. Any proposed global mechanism must explain why this fluctuating local normalization is canonical and how different gaps are assembled before it can be compared with the fixed global normalization of the Weil explicit formula.

Finally, nothing here generates the archimedean Gamma contribution, the pole/trivial-zero counterterms, or a nonseparable finite--archimedean coupling. Those remain independent gates.

## 6. Prior-art and novelty audit

The number-theoretic input is classical: Maynard supplies infinitely many bounded prime gaps. The Julia/Nevanlinna and Boolean self-energy inputs are classical as recorded in `WP-318`. The Chebyshev estimate used only to control far tails is standard and far weaker than the prime number theorem.

The derived result is the interaction of those ingredients for Mathia's specific Mangoldt Herglotz source: choosing the **next prime-power support gap**, normalizing it to unit width, and then applying the derivative bias forced by scalar Julia reduction produces the compact inverse-square lattice class (7). Searches for Herglotz/Julia reduction combined with von-Mangoldt measures, bounded prime gaps, tangent measures, and reciprocal-square gap scaling located the classical ingredients separately but no established theorem identifying this particular local limit class. It should therefore be read as a Mathia-specific literature-backed corollary, not as a new prime-gap theorem or a new positivity theorem.

The negative half is even sharper in provenance: once (7) is known, the matched-control obstruction is an exact application of `WP-318`. No novelty is claimed for Boolean/Pick positivity itself.

## Consequence for the research line

The scalar support-side frontier is now narrower than after `WP-315`:

\[
\boxed{
\text{atom-mass scale}
\Rightarrow\text{nonprecompact cluster collapse},
\qquad
\text{actual bounded-gap scale}
\Rightarrow\text{tight inverse-square lattice laws}.
}
\tag{38}
\]

The second route is mathematically better behaved, but its positivity remains matched-control universal. The remaining scalar opportunity is therefore not "find a good local scale" in isolation. It must prove a **family-level arithmetic rigidity or coupling theorem** for the Mangoldt derivative-biased laws that generic positive Herglotz controls cannot reproduce, and then connect that structure canonically to the archimedean/global terms of the Weil form. Otherwise the line should leave the pure scalar Julia category for a genuinely coupled or operator-valued geometry.
