# PL-215 — Bost–Connes temperatures are disjoint type-III sectors; the canonical prime-product measure class changes at `beta=1`, not `1/2`

## Claim

The state-dependent modular escape left open after `PL-213` and `PL-214` has a decisive classical obstruction when it is implemented by comparing the canonical Bost–Connes equilibrium states at **different inverse temperatures**.

Let `phi_beta` denote the unique Bost–Connes `KMS_beta` state for

\[
0<\beta\le 1.
\]

Neshveyev's type theorem gives

\[
\pi_{\phi_\beta}(\mathcal A)''\ \text{of type }III_1.
\]

Takesaki's 1970 disjointness theorem then applies directly: if `psi_gamma` is any `KMS_gamma` state for the same dynamics with `gamma != beta`, the GNS representations of `phi_beta` and `psi_gamma` are disjoint. In particular, two distinct high-temperature states `phi_beta` and `phi_gamma` do not belong to a common normal factorial folium.

This has an exact prime-lattice matched control. In the adelic realization the canonical `W`-invariant KMS measure is

\[
\mu_\beta=\bigotimes_p\mu_{\beta,p},
\]

and its restriction to

\[
\mathcal R=\prod_p\mathbb Z_p
\]

is a product probability measure whose valuation coordinate has geometric law

\[
\boxed{
\mu_{\beta,p}\{v_p=k\}
=(1-p^{-\beta})p^{-k\beta},
\qquad k\ge0.
}
\]

For two distinct parameters `beta,gamma`, Kakutani's product-measure criterion shows that these canonical diagonal measures are mutually singular whenever

\[
\min(\beta,\gamma)\le1,
\]

while for `beta,gamma>1` their restrictions to `R` are equivalent. Thus the global prime product already makes temperature a **measure-class sector label** at the thermodynamic threshold `beta=1`; it supplies no distinguished measure-class event at the Riemann half `beta=1/2`.

Consequently a proposed RH mechanism based on a relative modular operator or Connes cocycle **between different Bost–Connes temperatures** cannot be formed as a faithful normal comparison inside one canonical high-temperature GNS factor. One may place disjoint sectors in the universal enveloping representation, or choose an external identification between abstract factors, but then the common-sector coupling is extra data rather than a source-forced consequence of the prime lattice. Same-temperature perturbations, relative modular data between normal states/weights already living in one sector, and later adelic/Weil trace constructions are not ruled out.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. Takesaki already forbids normal cross-temperature comparison in a type-III KMS sector

Masamichi Takesaki proved the relevant general theorem in 1970. Let `(A,sigma)` be a `C*`-dynamical system, let `phi` be a `KMS_beta` state and `psi` a `KMS_gamma` state, and suppose that at least one of their cyclic GNS von Neumann algebras is of type III. Then

\[
\boxed{
\beta\ne\gamma
\quad\Longrightarrow\quad
\pi_\phi\perp\pi_\psi.
}
\]

Here disjointness is representation-theoretic: the two GNS representations have no nonzero quasi-equivalent subrepresentations. This is stronger than merely saying that the equilibrium states are different.

The primary source is:

- Masamichi Takesaki, “Disjointness of the KMS States of Different Temperatures,” *Communications in Mathematical Physics* **17** (1970), 33–41. DOI `10.1007/BF01649582`. Theorem 5 states that if one of the cyclic representations of two KMS states is type III, then distinct inverse temperatures force the representations to be disjoint.

For the classical Bost–Connes system, `PL-213` already records the required premise from Neshveyev: for every `0<beta<=1`, the unique `KMS_beta` state generates a type `III_1` factor. Therefore, for every fixed

\[
0<\beta\le1,
\]

and every `gamma>0` with `gamma != beta`, **any** Bost–Connes `KMS_gamma` state is disjoint from `phi_beta`. The second temperature may lie above or below the phase transition; only one of the two representations needs to be type III.

The relevant Bost–Connes sources are:

- Sergey Neshveyev, “von Neumann Algebras Arising from Bost–Connes Type Systems,” *International Mathematics Research Notices* **2011**(1) (2011), 217–236. DOI `10.1093/imrn/rnq067`, arXiv `0907.1456`. It proves type `III_1` for the rational high-temperature KMS factors throughout `0<beta<=1`.
- Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proceedings of the American Mathematical Society* **130**(10) (2002), 2999–3003. DOI `10.1090/S0002-9939-02-06449-3`, arXiv `math/0002141`. It gives the canonical adelic KMS measures used below.

No novelty is claimed for the disjointness statement. The line-specific content is the consequence for the surviving relative-modular search direction and the explicit prime-coordinate matched control.

## 2. The canonical KMS measure is an independent geometric law on the prime-exponent coordinates

Neshveyev realizes the Bost–Connes algebra as the full corner of

\[
C_0(\mathcal A_f)\rtimes\mathbb Q_+^\times
\]

cut out by the characteristic function of

\[
\mathcal R=\prod_p\mathbb Z_p.
\]

A `KMS_beta` state corresponds to an adelic measure with the scaling law

\[
q_*\mu=q^\beta\mu,
\qquad
\mu(\mathcal R)=1.
\]

For every `beta>0` there is a canonical `W=R^*`-invariant solution

\[
\mu_\beta=\bigotimes_p\mu_{\beta,p},
\]

where, relative to normalized Haar measure `mu_{1,p}` on `Z_p`,

\[
\frac{d\mu_{\beta,p}}{d\mu_{1,p}}(a)
=
\frac{1-p^{-\beta}}{1-p^{-1}}
|a|_p^{\beta-1}.
\]

On the shell `p^k Z_p^*`, Haar mass is `(1-p^{-1})p^{-k}` and `|a|_p=p^{-k}`. Hence the shell mass is exactly

\[
\begin{aligned}
\mu_{\beta,p}(p^k\mathbb Z_p^*)
&=
\frac{1-p^{-\beta}}{1-p^{-1}}
 p^{-k(\beta-1)}
 (1-p^{-1})p^{-k}\\
&=(1-p^{-\beta})p^{-k\beta}.
\end{aligned}
\]

Thus under the diagonal equilibrium measure the exponent coordinates `v_p` are independent geometric random variables. This is a literal probabilistic realization of the positive prime-exponent lattice, but it is also a warning: changing `beta` changes **every prime coordinate at once**.

The formula is valid as a measure statement for real `beta>0`; it is not an analytic continuation of the Gibbs partition function `zeta(beta)` into `beta<=1`.

## 3. Kakutani gives an exact measure-class threshold at `beta=1`

Take distinct positive `beta,gamma` and set

\[
x=p^{-\beta},\qquad y=p^{-\gamma}.
\]

The Hellinger affinity of the two geometric valuation laws at prime `p` is

\[
\begin{aligned}
h_p(\beta,\gamma)
&=
\sum_{k\ge0}
\sqrt{(1-x)x^k(1-y)y^k}\\
&=
\frac{\sqrt{(1-x)(1-y)}}{1-\sqrt{xy}}.
\end{aligned}
\]

A direct calculation gives the exact identity

\[
\boxed{
1-h_p(\beta,\gamma)^2
=
\frac{(p^{-\beta/2}-p^{-\gamma/2})^2}
{(1-p^{-(\beta+\gamma)/2})^2}.
}
\]

Assume without loss of generality that `beta<gamma`. For all sufficiently large primes,

\[
p^{-(\gamma-\beta)/2}\le\frac12,
\]

so

\[
(p^{-\beta/2}-p^{-\gamma/2})^2
\ge\frac14p^{-\beta}.
\]

Since `0<h_p<=1`,

\[
1-h_p
=
\frac{1-h_p^2}{1+h_p}
\ge
\frac12
(p^{-\beta/2}-p^{-\gamma/2})^2
\ge
\frac18p^{-\beta}
\]

for all sufficiently large `p`. Therefore, if `beta<=1`,

\[
\sum_p(1-h_p)=\infty,
\]

because `sum_p 1/p` diverges and `p^{-beta}>=p^{-1}`. Kakutani's theorem then gives

\[
\boxed{
\mu_\beta|_{\mathcal R}
\perp
\mu_\gamma|_{\mathcal R}
\qquad
(\beta\ne\gamma,\ \min(\beta,\gamma)\le1).
}
\]

Conversely, if `beta,gamma>1`, then for large `p`

\[
1-h_p
\le
1-h_p^2
\ll p^{-\min(\beta,\gamma)},
\]

and the prime sum converges. Since the local measures are mutually absolutely continuous, Kakutani gives equivalence of the product measures on `R`:

\[
\boxed{
\mu_\beta|_{\mathcal R}
\sim
\mu_\gamma|_{\mathcal R}
\qquad
(\beta,\gamma>1).
}
\]

The product-measure theorem used here is classical:

- Shizuo Kakutani, “On Equivalence of Infinite Product Measures,” *Annals of Mathematics* (2) **49**(1) (1948), 214–224. DOI `10.2307/1969123`.

This calculation is not needed to prove Takesaki disjointness. It is a matched control that exposes the prime-lattice mechanism underneath it: in the high-temperature regime the infinitesimal statistical mismatch at each prime accumulates to a globally singular measure class.

## 4. Why this blocks the most direct relative-modular escape

`PL-213` deliberately left state-dependent relative modular operators open after showing that factor type and the Connes ratio set are too coarse. A first natural move would be to compare the canonical equilibrium states at two temperatures and ask whether a relative modular Hamiltonian retains more arithmetic information than the individual type-`III_1` factors.

Takesaki's theorem says that this comparison is not available in the naive form. If `beta != gamma` and one temperature lies in `(0,1]`, there is no representation of the original Bost–Connes algebra in which the two GNS sectors become quasi-equivalent normal thermal states of one factor. Therefore one cannot simply write a faithful normal Connes cocycle derivative

\[
(D\phi_\gamma:D\phi_\beta)_t
\]

**inside the canonical `beta`-factor** and interpret its spectrum as a source-forced cross-temperature arithmetic observable.

There are two important qualifications.

First, the universal enveloping von Neumann algebra can of course contain the normal extensions of both states. Disjointness then appears as orthogonal central sectors rather than as nonexistence of the states. Relative modular theory in sufficiently general standard-form language is not being denied. What fails is the hoped-for **single-factor normal coupling** whose spectrum could be read as intrinsic Bost–Connes data connecting the two temperatures.

Second, one could choose an external isomorphism or correspondence between the abstract factors and transport one state into the other's factor. But Takesaki disjointness says that such an identification is not induced by quasi-equivalence of the two representations of the original `C*`-dynamical system. For the research mandate this is exactly the programmability danger: the coupling map would have to carry additional arithmetic content and be justified independently, rather than being obtained for free from the prime lattice or the KMS family.

## 5. The half line is again not selected by the canonical thermal geometry

The result separates three structures that can otherwise be conflated:

\[
\begin{array}{rcl}
\text{Gibbs trace / symmetry-breaking threshold} &:& \beta=1,\\
\text{canonical diagonal measure-class threshold} &:& \beta=1,\\
\text{type-III temperature sectors} &:& \text{pairwise disjoint for distinct }\beta\le1.
\end{array}
\]

Nothing singular happens to these structures specifically at `beta=1/2`. The state at `1/2` is just one member of a continuum of mutually disjoint high-temperature sectors. The square-free second-moment support threshold at `1/2` found in `PL-211` remains a different, phase-blind phenomenon; it is not upgraded to zero localization by modular comparison across temperatures.

This also clarifies a tempting but invalid intuition. Because all high-temperature factors are type `III_1`, one might hope to identify them and regard `beta` as a continuous deformation parameter inside one fixed operator algebra. Abstract factor type does not supply that identification. As representations of the Bost–Connes `C*`-algebra, different temperatures are precisely separated into disjoint sectors.

## 6. Prior-art and adversarial boundary

The decisive theorem is classical Takesaki prior art, and the Bost–Connes hypotheses are classical Neshveyev/Bost–Connes prior art. The Hellinger/Kakutani calculation is an exact derivation from Neshveyev's published local product measure; it is recorded as a line-specific diagnostic, not as a novelty claim.

A targeted audit around Bost–Connes temperature disjointness, KMS relative modular comparison, the adelic measures `mu_beta`, and product-measure singularity found the general Takesaki theorem and the explicit Bost–Connes product measures, but no reason to claim a new theorem here. The correct classification is therefore a **decisive negative/prior-art redirect**.

The claim is intentionally narrow and falsifiable:

- it rules out cross-temperature **normal same-factor** modular comparison as an automatic Bost–Connes mechanism;
- it does not rule out relative modular operators between two faithful normal states or weights already defined in the same `beta`-sector;
- it does not rule out perturbing a KMS state by source-forced arithmetic operators inside one sector;
- it does not rule out correspondences/bimodules between temperature sectors if such a correspondence carries independent arithmetic rigidity;
- it does not identify the KMS inverse temperature `beta` with the complex zeta variable `s` and does not analytically continue a state through the critical strip;
- it does not rule out Connes' later adele-class trace formula, Weil positivity, endomotives, or other global constructions whose zero-sensitive content is not a comparison of two equilibrium temperatures.

The surviving modular question is consequently much tighter: **can one construct source-forced, zero-sensitive relative modular data inside a single canonical sector, or a canonical arithmetic correspondence between disjoint sectors, with a positivity/coercivity theorem that a generic type-`III_1` system does not possess?** Merely varying the Bost–Connes temperature does not provide that coupling.