---
id: WP-318
title: Scalar Julia tangents are Boolean self-energies of derivative-biased boundary measures
branch: weil_positivity
status: supported
kind: infinite-collective-scalar-julia-boolean-self-energy-classification
claim_strength: exact classification of every regular scalar Julia response for a pure-measure Herglotz source, finite or infinite, as a scaled negative Boolean self-energy of the derivative-biased probability measure at the boundary node; after affine rescaling the normalized tangent is exactly tau minus K_nu, and every gap-supported probability law is realizable by a positive Herglotz matched control, so scalar Julia positivity is universal rather than arithmetic and any surviving Weil route must obtain source specificity and finite-archimedean coupling from an independent theorem on the derivative-biased law
created: 2026-09-15
related: [WP-304, WP-312, WP-314, WP-315, WP-316, WP-317]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for classical Julia-Nevanlinna reduction and Pick-class preservation
  - Roland Speicher and Reza Woroudi, Boolean convolution, Fields Institute Communications 12 (1997), 267-279, DOI 10.1090/fic/012/13, for the Boolean K-transform/self-energy linearization framework
---

# WP-318 — Scalar Julia tangents are Boolean self-energies of derivative-biased boundary measures

## Claim

`WP-315` leaves an infinite collective support-side scalar route open after the atom-mass normalization fails local compactness, while `WP-316` and `WP-317` show that one-pole and every fixed finite-multipole Julia response are classical and collapse under repeated reduction. The remaining question is whether an infinite positive boundary measure can make the same scalar Julia operation into a genuinely new arithmetic positivity mechanism.

For the pure-measure scalar Herglotz class the answer is no. There is an exact normal form that applies equally to finite and infinite positive measures.

Let

\[
f(z)=c+\int_{\mathbb R}\left(\frac1{x-z}-\frac{x}{1+x^2}\right)d\mu(x),
\qquad \mu\ge0,
\tag{1}
\]

with

\[
\int_{\mathbb R}\frac{d\mu(x)}{1+x^2}<\infty.
\tag{2}
\]

Choose a real regular node `t` lying in a support-free interval and assume

\[
d:=f'(t)=\int_{\mathbb R}\frac{d\mu(x)}{(t-x)^2}\in(0,\infty).
\tag{3}
\]

Define the derivative-biased probability measure

\[
\boxed{
d\nu_t(x):=\frac1d\frac{d\mu(x)}{(t-x)^2}.
}
\tag{4}
\]

For the Cauchy transform convention

\[
G_{\nu}(z):=\int_{\mathbb R}\frac{d\nu(x)}{z-x},
\tag{5}
\]

put

\[
K_{\nu}(z):=z-\frac1{G_{\nu}(z)}.
\tag{6}
\]

This is the standard Boolean `K`-transform/self-energy convention. If the normalized Julia response is

\[
\mathcal J_t[f](z)
=
\frac{d(z-t)(f(z)-f(t))}
{d(z-t)-(f(z)-f(t))}
+\beta,
\qquad \beta\in\mathbb R,
\tag{7}
\]

then identically on the upper half-plane,

\[
\boxed{
\mathcal J_t[f](z)-\beta
=
d\bigl(t-K_{\nu_t}(z)\bigr).
}
\tag{8}
\]

Thus **every regular scalar Julia response in this pure-measure class is exactly a scaled negative Boolean self-energy of one probability law**. Its positivity is universal: for every probability measure `nu`, `t-K_nu` is Herglotz. No prime distribution, explicit formula, zero data, or archimedean input is needed for that sign.

After any positive affine rescaling

\[
x=x_0+ru,
\qquad
t=x_0+r\tau,
\qquad r>0,
\tag{9}
\]

and pushforward of `nu_t` to a probability law `tilde nu` in the `u` coordinate,

\[
\boxed{
\frac{\mathcal J_t[f](x_0+r\zeta)-\beta}{dr}
=
\tau-K_{\widetilde\nu}(\zeta).
}
\tag{10}
\]

So the entire normalized scalar tangent problem is reduced to the weak-limit geometry of the derivative-biased probability laws. More strongly, every probability law supported a positive distance from the node is realized by a positive Herglotz matched control. The scalar sign mechanism therefore has no arithmetic selectivity by itself.

For the reflected Mangoldt source, arithmetic can still enter through the specific family of derivative-biased laws. A genuinely new route would have to prove a source-specific compactness, rigidity, or limiting theorem for those laws and then obtain the Gamma/global counterterms from an independent canonical coupling. Merely retaining infinitely many atoms does not make Julia positivity itself a Weil mechanism.

**Classification:** `EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION + SCALAR-JULIA + BOOLEAN-SELF-ENERGY + DERIVATIVE-BIASED-PROBABILITY + MATCHED-CONTROL-SURJECTIVITY + INFINITE-COLLECTIVE + NOT-WEIL-POSITIVITY`.

## 1. Exact derivative-biased probability normal form

Define

\[
Q_t(z):=
\int_{\mathbb R}
\frac{d\mu(x)}{(t-x)(z-x)},
\tag{11}
\]

and

\[
R_t(z):=
\int_{\mathbb R}
\frac{d\mu(x)}{(t-x)^2(z-x)}.
\tag{12}
\]

Regularity at `t` and (3) make these expressions well-defined in the upper half-plane. Direct subtraction in the Herglotz representation gives

\[
f(z)-f(t)=(z-t)Q_t(z).
\tag{13}
\]

Also

\[
\begin{aligned}
d-Q_t(z)
&=
\int
\left(
\frac1{(t-x)^2}
-
\frac1{(t-x)(z-x)}
\right)d\mu(x)\\
&=(z-t)R_t(z).
\end{aligned}
\tag{14}
\]

Substitution into (7) yields the exact quotient

\[
\mathcal J_t[f](z)-\beta
=
d\frac{Q_t(z)}{R_t(z)}.
\tag{15}
\]

Equation (14) is equivalently

\[
Q_t(z)=d+(t-z)R_t(z).
\tag{16}
\]

By (4)-(5),

\[
R_t(z)=dG_{\nu_t}(z).
\tag{17}
\]

Therefore

\[
\begin{aligned}
\mathcal J_t[f](z)-\beta
&=d(t-z)+\frac{d^2}{R_t(z)}\\
&=d\left(t-z+\frac1{G_{\nu_t}(z)}\right)\\
&=d\bigl(t-K_{\nu_t}(z)\bigr),
\end{aligned}
\tag{18}
\]

which proves (8). No finiteness of the support was used.

This also explains the finite cases without a separate mechanism. For a one-atom law, `K_{delta_x}=x`, so (8) is a real constant, exactly the collapse in `WP-316`. For an `N`-atom probability law, `K_nu` is rational and its poles are the `N-1` real interlacing zeros of `G_nu`; this is exactly the degree reduction in `WP-317`.

## 2. The sign is universal Boolean self-energy positivity

For `z=u+iv` with `v>0`, (5) gives

\[
-\operatorname{Im}G_{\nu}(z)
=
v\int_{\mathbb R}\frac{d\nu(x)}{|z-x|^2}.
\tag{19}
\]

Because `nu` is a probability measure, Cauchy-Schwarz gives

\[
|G_{\nu}(z)|^2
\le
\int_{\mathbb R}\frac{d\nu(x)}{|z-x|^2}.
\tag{20}
\]

Hence

\[
\operatorname{Im}\frac1{G_{\nu}(z)}
=
\frac{-\operatorname{Im}G_{\nu}(z)}{|G_{\nu}(z)|^2}
\ge v.
\tag{21}
\]

It follows that

\[
\operatorname{Im}K_{\nu}(z)
=
v-
\operatorname{Im}\frac1{G_{\nu}(z)}
\le0,
\tag{22}
\]

and therefore

\[
\operatorname{Im}\bigl(t-K_{\nu}(z)\bigr)\ge0.
\tag{23}
\]

This is an independent positive theorem, but it is independent in the wrong sense for the Weil objective: it holds for **every** probability law. The source-specific measure only chooses which member of a universal Boolean/Nevanlinna class appears. The sign itself cannot distinguish the Mangoldt source from a matched non-arithmetic positive measure.

## 3. Affine tangent covariance isolates the only scalar source data

Let `nu_t` be pushed forward under `x=x_0+ru` to `tilde nu`. Then

\[
G_{\nu_t}(x_0+r\zeta)
=
\frac1rG_{\widetilde\nu}(\zeta),
\tag{24}
\]

and consequently

\[
K_{\nu_t}(x_0+r\zeta)
=
x_0+rK_{\widetilde\nu}(\zeta).
\tag{25}
\]

Together with `t=x_0+r tau`, equation (8) becomes (10).

This is stronger than the fixed-multipole classifications. It says that even an unbounded or infinite local cluster does not create a new scalar sign theorem. Once the location, scale, positive slope, and irrelevant real additive constant are normalized away, the response is exactly `tau-K_tilde_nu`.

If a sequence of the rescaled probability laws is tight and converges weakly, then their Cauchy transforms converge locally uniformly on the upper half-plane, and so do the corresponding normalized Julia profiles. Conversely, loss of tightness is precisely loss of a probability-law tangent in this normalization. Thus the scalar infinite-collective frontier has become a concrete source-specific probability-limit problem rather than an unspecified Herglotz positivity problem.

## 4. Matched controls realize every gap-supported probability law

The strongest falsification is constructive. Fix a real node `tau`, a gap `epsilon>0`, and **any** probability measure `rho` supported in

\[
\mathbb R\setminus(\tau-\varepsilon,\tau+\varepsilon).
\tag{26}
\]

Define a positive Herglotz measure

\[
d\mu_{\rho}(u):=(\tau-u)^2d\rho(u).
\tag{27}
\]

It satisfies the standard Herglotz integrability condition because

\[
\frac{(\tau-u)^2}{1+u^2}
\tag{28}
\]

is bounded on the real line. The support gap makes `tau` a regular node, and

\[
\int\frac{d\mu_{\rho}(u)}{(\tau-u)^2}=1.
\tag{29}
\]

Therefore the derivative-biased law (4) is **exactly** `rho`, and the normalized Julia response is

\[
\mathcal J_{\tau}[f_{\rho}](z)-\beta
=
\tau-K_{\rho}(z).
\tag{30}
\]

Multiplying (27) by any positive constant merely changes the overall slope factor `d` and leaves the normalized profile unchanged.

So every gap-supported probability law occurs as a scalar Julia response of some positive Herglotz matched control. There is no hidden prime-only restriction in positivity, interlacing, infinite support, or the Boolean self-energy operation. Any arithmetic rigidity must be imposed by a theorem about the **specific derivative-biased measures generated by Mathia's source**, not by the scalar Julia transformation itself.

## 5. Mangoldt specialization

For the reflected finite-prime source used in the support-side program,

\[
x_n=-\log n,
\qquad
a_n=\frac{\Lambda(n)}{n+1},
\tag{31}
\]

with `n` restricted to prime powers. At a regular node `t`, the derivative-biased probability weights are

\[
\boxed{
\nu_t(\{x_n\})
=
\frac{a_n/(t-x_n)^2}
{\displaystyle\sum_m a_m/(t-x_m)^2}.
}
\tag{32}
\]

Equation (32) identifies exactly what survives as source-specific scalar information. `WP-315` showed that normalizing by the focal atom mass can blow up under bounded prime clustering. The present normalization instead divides by the total boundary derivative and therefore always produces a probability law whenever that derivative is finite. That repairs the scalar compactness variable, but not the Weil problem: the positivity of its Julia response is automatic for every such law.

A surviving scalar program must now establish something genuinely arithmetic about a family of laws (32): for example a canonical tight limit, a rigidity property not shared by matched controls, or a source-forced boundary decomposition. Even that would supply only the finite/source side. The same construction would still have to generate the Gamma and global counterterms canonically and match their exact normalization before it could qualify as global Weil positivity.

## Prior-art and novelty audit

[[research/prior_art/incremental/PA-julia-nevanlinna-boundary-reduction|Agler--Young]] places the reduction/augmentation operation itself squarely inside classical boundary Nevanlinna-Pick theory. [[research/prior_art/incremental/PA-boolean-convolution-self-energy|Speicher--Woroudi]] supplies the standard Boolean `K`-transform/self-energy framework. The identity (8) should therefore **not** be advertised as a new transform or a new positivity theorem.

The durable result here is narrower and route-specific: the Mathia support-side normalized Julia response is exactly this classical Boolean self-energy after derivative biasing; the affine tangent formula (10) reduces every finite or infinite scalar tangent to a probability law; and the construction (27) shows by matched controls that the entire gap-supported probability class is realizable. This turns the previously open `infinite collective scalar Julia` escape into a prior-art redirect plus a sharply defined arithmetic probability-limit problem.

No zero data or RH assumption enters the derivation. Conversely, no step generates the archimedean Gamma term, the pole/trivial-zero counterterms, or a prime-specific sign. The result narrows the search rather than proving a Weil criterion.

## Boundary conditions

The exact normal form above assumes the **pure-measure** Herglotz representation (1). A separate affine Herglotz term `alpha z` with `alpha>0` contributes to the boundary derivative without arising from a finite real measure; at order one it is naturally a mass-at-infinity/non-rational channel and is not closed by this finding.

The node must be regular and have finite nonzero derivative at each finite stage. The result also does not exclude matrix/operator-valued Julia reductions, nonseparable finite--archimedean coupling, a separately derived Gamma channel, or an independent theorem proving special rigidity of the Mangoldt derivative-biased laws.

It does exclude one specific hope: **infinite collective scalar Julia positivity itself is not the missing Mathia-native source of Weil positivity**. Its sign is the universal Boolean self-energy sign of a probability measure, and arbitrary matched positive measures realize the same mechanism.

## Consequence

The scalar support-side sequence is now unified:

- `WP-316`: one derivative-biased atom gives a removable real constant;
- `WP-317`: finitely many atoms give classical interlacing degree reduction;
- `WP-318`: arbitrary finite or infinite positive measure gives `d(t-K_nu)`, with every gap-supported probability law available as a matched control.

The remaining scalar question is no longer whether infinite collective Herglotz positivity can survive. It can, but universally. The only potentially arithmetic content is a **source-specific theorem about the derivative-biased probability laws themselves**, together with a canonical finite--archimedean coupling that is absent from the scalar Boolean mechanism.