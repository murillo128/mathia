# WP-111 — Chentsov naturality collapses critical statistical metrics back to divergent Fisher geometry

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + INFORMATION-GEOMETRY + CHENTSOV-CLASSIFICATION + CORRELATION-ROBUST + SHARP-THRESHOLD + PRIOR-ART-CLASSICALIZATION`.

`WP-102` proves that every exact critical positive completion of the one-prime Weil rays has infinite cylindrical Fisher energy. An apparent escape is to replace Fisher by another canonical positive Riemannian metric on the same prime-torus state. Under the standard Chentsov notion of statistical naturality, that escape is closed: a symmetric Riemannian 2-tensor assignment invariant under sufficient statistics is Fisher up to one positive global scale. Composed with `WP-102`, the exact critical moment obstruction therefore applies to every such natural statistical metric.

Let `P` be a finite set of primes and

\[
\eta_P=h_Pm_P,
\qquad
m_P=\bigotimes_{p\in P}\frac{d\theta_p}{2\pi},
\]

be a strictly positive regular probability marginal of a finite positive measure `mu_sigma` of mass `C` satisfying

\[
\widehat\mu_\sigma(e_p)=-\frac{\log p}{p^\sigma}
\qquad(p\in P).
\tag{1}
\]

Translate the `p`-th circle coordinate:

\[
h_{P,p,t}(\theta)=h_P(\theta-te_p),
\qquad
v_p:=\left.\frac d{dt}\right|_{t=0}h_{P,p,t}=-\partial_ph_P.
\tag{2}
\]

The Fisher--Rao squared norm of this tangent is exactly the spatial Fisher term used in `WP-102`:

\[
 g^F_{h_P}(v_p,v_p)
 =\int_{\mathbb T^P}\frac{|\partial_ph_P|^2}{h_P}\,dm_P
 =4\|\partial_p\sqrt{h_P}\|_2^2.
\tag{3}
\]

Suppose `g` is the restriction of a **single** natural symmetric Riemannian 2-tensor assignment on the relevant statistical models, invariant under sufficient statistics in the Chentsov sense. Then there is one constant `c>0`, independent of `P`, `h_P`, and tangent direction, such that

\[
\boxed{g=c\,g^F.}
\tag{4}
\]

Hence its prime-translation trace is

\[
\mathcal E^g_P(h_P)
:=\sum_{p\in P}g_{h_P}(v_p,v_p)
=c\,\mathcal I_P(\eta_P).
\tag{5}
\]

Using the correlation-independent bound from `WP-102`,

\[
\boxed{
\mathcal E^g_P(h_P)
\ge
\frac{c}{C^2}\sum_{p\in P}\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{6}
\]

Therefore

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal E^g_P(h_P)=+\infty
\qquad(\sigma\le1/2).
}
\tag{7}
\]

At the Weil exponent `sigma=1/2`, changing from Fisher to another smooth Riemannian information metric cannot regularize the exact critical completion while retaining sufficient-statistic naturality. A surviving statistical geometry must break that naturality or introduce additional Mathia structure before the metric is formed.

This is a prior-art redirect and branch-specific no-go, not a new characterization theorem and not a proof of Weil positivity.

## 1. WP-102 already measures Fisher--Rao geometry

For a smooth positive density `h` and zero-mass tangent density `v`, the Fisher quadratic form is

\[
g^F_h(v,v)=\int\frac{v^2}{h}\,dm.
\tag{8}
\]

For the translation model (2), `v_p=-\partial_p h_P`, so

\[
g^F_{h_P}(v_p,v_p)
=\int|\partial_p\log h_P|^2h_P\,dm_P
=4\|\partial_p\sqrt{h_P}\|_2^2.
\tag{9}
\]

Thus `WP-102` is not merely an analogy with information geometry: it is a lower bound on the trace of the Fisher--Rao metric over the canonical prime-coordinate translation directions. No derivative in `sigma`, zero data, or mixed-prime factorization is used.

## 2. Chentsov naturality removes the metric-choice freedom

Chentsov's theorem characterizes Fisher information, up to positive scale, by statistical invariance under the canonical lossless Markov/sufficient-statistic transformations. Campbell gave an extended finite-dimensional characterization. Ay, Jost, Le, and Schwachhofer formulated parametrized measure models on general sample spaces and established the corresponding uniqueness of the Fisher metric, up to scale, among symmetric 2-tensor fields invariant under sufficient statistics.

That hypothesis is exactly the candidate canonicality being tested here: the metric should be intrinsic to the statistical state and compatible with lossless coarse-graining, rather than carrying coefficients attached externally to prime labels.

Under this hypothesis, every regular finite prime-torus cylinder inherits (4). The scale is part of one natural tensor assignment. Choosing unrelated factors `c_P` for different cylinders, or prime-dependent factors `c_p`, is therefore outside the Chentsov-natural category. Such weights can still arise from additional arithmetic geometry, but then that extra structure—not statistical naturality—must force them.

The case `c=0` is not an escape: it gives a degenerate zero tensor, not a Riemannian sign source.

## 3. Critical divergence is correlation-independent and sharp

`WP-102` proves for every regular finite cylinder

\[
\mathcal I_P(\eta_P)
\ge
\frac1{C^2}\sum_{p\in P}\frac{(\log p)^2}{p^{2\sigma}},
\tag{10}
\]

using only the one-coordinate moments (1). Multiplication by the Chentsov constant proves (6), so mixed-prime correlations cannot cancel the lower bound. At `sigma=1/2`,

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{11}
\]

and (7) follows.

The threshold is matched rather than an artifact. For `sigma>1/2`, `WP-102` gives an exact positive product completion with finite cylindrical Fisher energy, hence finite `c g^F` energy. Thus the same architecture admits finite Chentsov-natural energy precisely on the convergent side of the critical boundary.

`WP-101` is also a useful falsifier: correlations can produce critical completions equivalent to Haar and, above the sharp mass, with a positive Haar background. The divergence here is therefore not the product singularity of `WP-100`; it persists through the exact first-coordinate Fisher lower bound.

For a free commutative generator system with energies `E_j` and moments `-E_j e^{-sigma E_j}`, the identical argument gives

\[
\mathcal E^g_J
\ge
\frac{c}{C^2}\sum_{j\in J}E_j^2e^{-2\sigma E_j}.
\tag{12}
\]

The rational-prime case is the specialization `E_j=log p_j`. This control prevents interpreting the divergence itself as Riemann-specific global arithmetic.

## 4. Exact boundary of the no-go

The Chentsov hypothesis is substantive. This finding does **not** rule out:

- a metric carrying additional prime/arithmetic labels and hence not determined solely by the statistical state;
- a degenerate or sub-Riemannian geometry, including a genuinely forced Kronecker direction;
- non-Riemannian/Finsler or nonsmooth positive functionals;
- singular boundary states together with a separately justified extension beyond the regular positive-density manifold;
- a nonseparable finite--archimedean construction that changes the state or tangent object before applying a statistical metric.

A cylinder-dependent rescaling `c_P -> 0` is a direct control against overclaiming: it can suppress the trace, but it does so by abandoning a single sufficient-statistic-natural tensor assignment. Likewise, prime-dependent weights can make the `WP-102` series summable, but unless a separate Mathia geometry forces those weights they are exactly the kind of inserted regularization excluded by the research mandate.

Thus the conclusion is not that every imaginable positive metric diverges. It is that **switching to another supposedly canonical Riemannian information metric does not create a new escape**: Chentsov naturality sends it back to Fisher.

## 5. Prior-art and novelty audit

The classification input is classical:

- N. N. Chentsov, *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs 53, AMS (1982), gives the foundational finite-sample characterization of Fisher geometry by statistical/Markov invariance.
- L. Lorne Campbell, *An extended Cencov characterization of the information metric*, Proceedings of the American Mathematical Society 98 (1986), 135--141, DOI `10.1090/S0002-9939-1986-0848890-5`, extends the characterization framework.
- Nihat Ay, Jurgen Jost, Hong Van Le, and Lorenz Schwachhofer, *Information geometry and sufficient statistics*, Probability Theory and Related Fields 162 (2015), 327--364, DOI `10.1007/s00440-014-0574-8`, extends Chentsov-type uniqueness to parametrized measure models on general sample spaces and characterizes the Fisher metric up to scale among symmetric 2-tensor fields invariant under sufficient statistics.

A targeted literature audit found no basis for claiming theorem-level novelty in this classification. The retained Mathia content is the exact composition of that classical uniqueness result with the critical prime-torus moment lower bound of `WP-102`. This is therefore **prior-art classicalization plus a branch-local obstruction**.

## Consequence for the research line

The current prime-torus route now satisfies the sharper implication

\[
\boxed{
\text{exact critical one-prime rays}
+\text{positive completion}
+\text{sufficient-statistic-natural Riemannian geometry}
\Longrightarrow
\text{infinite cylindrical energy}.
}
\tag{13}
\]

So the route

\[
\text{critical completion}
\to
\text{replace Fisher by another canonical statistical metric}
\to
\text{finite independent positive sign source}
\]

is closed under standard Chentsov naturality. A surviving construction must add genuinely non-statistical structure: an arithmetic/nonlocal metric, a forced degeneracy or quotient, or a nonseparable finite--archimedean object. It must still derive the finite prime part together with the Gamma/polar terms and prove nonnegativity before identifying the Weil consequence.