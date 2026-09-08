# WP-200 — Power-law centered baths have a sharp source-variation stabilization threshold

**Status:** `DERIVED + EXACT + POWER-LAW-CLASSIFICATION + INFINITE-DIMENSIONAL + SHARP-SCHATTEN-THRESHOLD + FULL-WEIL-AUTOCORRELATION-CONE + UNIVERSAL-FINITE-PAYLOAD-STABILIZATION + MATCHED-CONTROL + NONARITHMETIC + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-198` exhibited one deliberately rough centered bath whose order-`4k` higher-order spectral-shift multiplier decays only like a positive `|xi|^{-1/2}` floor, and `WP-199` showed that enough copies of that bath can stabilize **every** fixed finite-dimensional monotone-positive payload on the full real Weil autocorrelation cone. The exponent `1/2` is not the real boundary.

For the complete power-law family

\[
n=4k,\qquad
H_\alpha=0,\qquad
V_\alpha=\operatorname{diag}(a_1,a_2,\ldots),
\qquad
a_j=j^{-\alpha},
\tag{1}
\]

there is an exact phase transition at the extra source-variation Schatten power:

\[
\boxed{
\frac1n<\alpha\le \frac1{n-1}
\quad\Longleftrightarrow\quad
\text{the centered power-law bath universally stabilizes every finite positive payload.}
}
\tag{2}
\]

Here “universally stabilizes” means that for every finite-dimensional self-adjoint pair

\[
H_f\ge0,\qquad V_f\ge0,
\tag{3}
\]

there is a finite multiplicity `M>=1` such that

\[
\widetilde H
=0^{\oplus M}\oplus H_f,
\qquad
\widetilde V
=V_\alpha^{\oplus M}\oplus V_f
\tag{4}
\]

belongs to the natural order-`n` Schatten class and satisfies

\[
\boxed{
\mathcal R_n(g*\widetilde g;\widetilde H,\widetilde V)>0
\quad\text{for every nonzero real }g\in C_c^\infty(\mathbb R).
}
\tag{5}
\]

For `alpha>1/(n-1)`, universal stabilization fails: already the one-dimensional off-zero payload `H_f=V_f=1` cannot be stabilized by any finite number of bath copies. Thus, within this canonical power-law model class, the boundary is exactly the divergence/convergence boundary of the `(n-1)`st source-jump mass. The special choice `alpha=1/(n-1/2)` in `WP-198` is only a convenient interior point of the rough phase, selected because it gives the particularly transparent `|xi|^{-1/2}` floor.

This strengthens the matched-control conclusion of `WP-199`: the source-blind sign manufacture is not a fragile consequence of one tuned decay law. It occupies the **entire** admissible power-law strip `S^n\setminus S^{n-1}`.

## 1. The Schatten phase diagram is exact

For (1),

\[
\operatorname{Tr}(V_\alpha^q)
=\sum_{j\ge1}j^{-\alpha q}.
\tag{6}
\]

Hence

\[
V_\alpha\in\mathcal S^q
\quad\Longleftrightarrow\quad
\alpha q>1.
\tag{7}
\]

The natural order-`n` higher-order spectral-shift category therefore requires

\[
\alpha>\frac1n.
\tag{8}
\]

Inside that category,

\[
V_\alpha\notin\mathcal S^{n-1}
\quad\Longleftrightarrow\quad
\alpha\le\frac1{n-1}.
\tag{9}
\]

At the endpoint `alpha=1/(n-1)` the missing moment is exactly harmonic:

\[
\sum_j a_j^{n-1}=\sum_j\frac1j=\infty.
\tag{10}
\]

Thus the candidate transition in (2) coincides exactly with the point where the total source-boundary jump variation used in the `WP-198` zero-mode theorem ceases to be finite.

## 2. A general truncated-moment lower bound for centered diagonal baths

The proof does not need a power law until the final estimate. Let `a_j>0` with

\[
\sum_j a_j^n<\infty,
\tag{11}
\]

and take the centered commuting bath `H=0`, `V=diag(a_j)`. For one scalar centered channel, `WP-198` gives the exact even multiplier

\[
F_a(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^a
(1-\cos(t\xi))(a-t)^{n-3}\,dt
>0
\qquad(\xi\ne0).
\tag{12}
\]

Whenever `a|xi|>=4`, the same elementary restriction to `0<=t<=a/2` yields

\[
F_a(\xi)
\ge
\frac{a^{n-2}}
{2^{n-1}(n-3)!\,\xi^2}.
\tag{13}
\]

Therefore the full centered bath multiplier satisfies the reusable lower bound

\[
\boxed{
F(\xi)
\ge
\frac{c_n}{\xi^2}
\sum_{a_j\ge4/|\xi|}a_j^{n-2}
\qquad(|\xi|\text{ large}).
}
\tag{14}
\]

Equation (14) identifies the actual analytic resource that overwhelms finite source oscillation: not dimension by itself, but sufficiently large **truncated `(n-2)`nd moment near the singular-value origin**. In particular, any centered bath for which

\[
\liminf_{r\downarrow0}
r\sum_{a_j\ge r}a_j^{n-2}>0
\tag{15}
\]

has a positive floor `F(xi)>=c/|xi|` at high frequency and can therefore dominate the `O(1/|xi|)` sign defect of every fixed finite payload after a finite multiplicity increase. Condition (15) is only a sufficient criterion in this generality; no necessity claim is made beyond the power-law family classified below.

## 3. Every admissible rough power law has a slow enough positive floor

Return to `a_j=j^{-alpha}` and assume

\[
\frac1n<\alpha\le\frac1{n-1}.
\tag{16}
\]

Let

\[
J(\xi)
=
\left\lfloor (|\xi|/4)^{1/\alpha}\right\rfloor.
\tag{17}
\]

For every `j<=J(xi)`, `a_j|xi|>=4`, so (14) gives

\[
F_\alpha(\xi)
\ge
\frac{c_n}{\xi^2}
\sum_{j\le J(\xi)}j^{-\alpha(n-2)}.
\tag{18}
\]

Set

\[
p=\alpha(n-2).
\tag{19}
\]

The upper bound in (16) implies

\[
p\le\frac{n-2}{n-1}<1.
\tag{20}
\]

Consequently the elementary integral estimate for the partial power sum gives

\[
\sum_{j\le J}j^{-p}\ge c_p J^{1-p}
\tag{21}
\]

for large `J`. Substitution into (18) yields

\[
\boxed{
F_\alpha(\xi)
\ge
c_{n,\alpha}
|\xi|^{1/\alpha-n}
\qquad(|\xi|\text{ sufficiently large}).
}
\tag{22}
\]

It is useful to write

\[
\beta_\alpha
=n-\frac1\alpha.
\tag{23}
\]

Because `alpha>1/n` and `alpha<=1/(n-1)`,

\[
0<\beta_\alpha\le1,
\tag{24}
\]

so

\[
F_\alpha(\xi)
\ge c_{n,\alpha}|\xi|^{-\beta_\alpha}
\tag{25}
\]

with decay no faster than `1/|xi|`. At the endpoint `alpha=1/(n-1)`, (25) is exactly a `c/|xi|` lower floor. At the `WP-198` choice

\[
\alpha=\frac1{n-1/2},
\tag{26}
\]

one gets `beta_alpha=1/2`, recovering its displayed `|xi|^{-1/2}` estimate.

The multiplier is also continuous and strictly positive on all of `R`: uniform convergence follows from `sum a_j^n<infinity`, every scalar centered contribution is positive away from zero, and at zero the total spectral-shift mass is positive and finite.

## 4. The floor stabilizes every finite positive payload

Let `(H_f,V_f)` be any finite-dimensional pair satisfying (3), without assuming commutativity. `WP-199`, using the finite-dimensional source-jump structure from `WP-197`, gives a continuous even multiplier

\[
G_f(\xi)
=\widehat{\eta_f^{\rm ev}}(\xi)
\tag{27}
\]

with

\[
|G_f(\xi)|\le\frac{C_f}{|\xi|}
\qquad(|\xi|\ge R_f).
\tag{28}
\]

Combining (25) and (28),

\[
\frac{|G_f(\xi)|}{F_\alpha(\xi)}
\le
C_{f,n,\alpha}|\xi|^{\beta_\alpha-1}
\tag{29}
\]

at high frequency. Since `beta_alpha<=1`, the ratio is bounded there; if `beta_alpha<1` it even tends to zero. On compact intervals the denominator has a strictly positive minimum. Hence

\[
K_{f,\alpha}
:=
\sup_{\xi\in\mathbb R}
\frac{|G_f(\xi)|}{F_\alpha(\xi)}
<\infty.
\tag{30}
\]

Choose an integer

\[
M>K_{f,\alpha}.
\tag{31}
\]

Direct-sum additivity of the Taylor trace remainder gives the completed multiplier

\[
\widetilde F(\xi)
=M F_\alpha(\xi)+G_f(\xi)>0
\qquad(\xi\in\mathbb R).
\tag{32}
\]

The exact order-`4k` Fourier criterion of `WP-193` then gives (5). Because only finitely many bath copies are added and (8) holds,

\[
\widetilde V\in\mathcal S^n.
\tag{33}
\]

No commutativity condition on the finite payload was used. Thus the whole rough strip in (16) is a universal finite-payload stabilizer.

## 5. Above the threshold even one scalar off-zero payload cannot be stabilized

Now assume

\[
\alpha>\frac1{n-1}.
\tag{34}
\]

Then

\[
V_\alpha\in\mathcal S^{n-1}.
\tag{35}
\]

Take the fixed one-dimensional payload

\[
H_f=1,\qquad V_f=1.
\tag{36}
\]

For every finite `M`, the pair (4) is commuting and positive, its perturbation lies in `S^{n-1}`, and

\[
\widetilde H\widetilde V
=0^{\oplus M}\oplus1
\ne0.
\tag{37}
\]

But `WP-198` proves for every commuting positive pair with perturbation in `S^{4k-1}` that full order-`4k` Weil-autocorrelation positivity forces

\[
\widetilde H\widetilde V=0.
\tag{38}
\]

Therefore no finite bath multiplicity can stabilize (36). Universal stabilization fails. Together with Section 4 this proves the equivalence (2).

The necessity argument deliberately uses only one scalar control. It does **not** assert that every noncommuting infinite-dimensional completion in `S^{n-1}` is classified by `WP-198`; `WP-197` supplies that rigidity only in finite dimension. One counterexample payload is enough to disprove the universal stabilization property above the threshold.

## 6. Aggressive falsification and matched controls

**Is the endpoint an artifact of the lower-bound estimate?** No for the universal power-law classification. The rough side is proved directly by the Fourier floor, while the smooth side is killed independently by the `S^{n-1}` zero-mode theorem applied to the scalar payload. Both arguments meet at `alpha=1/(n-1)`, where `sum a_j^{n-1}` diverges harmonically and the lower floor is still strong enough.

**Could positivity at the endpoint fail because the finite payload also has a `1/|xi|` tail?** No. The ratio in (29) need not tend to zero there, but it is uniformly bounded. Multiplicity `M` is allowed to depend on the finite payload, exactly as in `WP-199`, and choosing `M>K_{f,alpha}` gives strict positivity pointwise.

**Could the result be arithmetic because the payload is arithmetic?** No. The bath depends only on `(n,alpha)`, and the proof works unchanged after replacing a finite arithmetic truncation by any finite positive matrix pair of comparable or completely unrelated spectrum. The sign theorem is carried by source-blind roughness, not by Mangoldt, Gamma, the pole terms, or a finite--archimedean incidence.

**Does the theorem produce a candidate Weil form?** No. It classifies a failure mode. The completed remainder remains a higher-order spectral-shift functional, and its positive reservoir can be appended after the payload is chosen. It therefore fails the branch mandate's explanatory test even though its sign is mathematically independent of RH.

**Could a genuinely coupled infinite arithmetic sector evade this control?** Yes. Equations (4) and (32) use an orthogonal direct-sum reservoir. A source-forced infinite geometry in which finite and archimedean/arithmetic degrees of freedom interact before the sign theorem is formed is not ruled out.

## 7. Prior-art and novelty boundary

The operator-theoretic infrastructure is classical. Potapov, Skripka, and Sukochev, *Spectral shift function of higher order*, Inventiones Mathematicae **193** (2013), 501--538, DOI `10.1007/s00222-012-0431-2`, establishes existence and `L^1` control of higher-order spectral-shift functions for `S^n` perturbations. Subsequent relative/resolvent-comparable work enlarges that perturbation category. A targeted audit for higher-order spectral-shift Fourier positivity, source-boundary Schatten thresholds, and regularly varying/power-law perturbations found this established trace-formula theory but no directly matching theorem that classifies the universal finite-payload stabilization property above.

No broad novelty claim is made from absence of a matching phrase. The durable Mathia contribution is narrower and internal: combine the exact centered multiplier estimate of `WP-198`, the arbitrary finite-payload `O(1/|xi|)` boundary from `WP-199`, and the `S^{n-1}` zero-mode obstruction into one sharp power-law phase diagram. The partial-sum estimate in Section 3 is elementary regular-variation calculus rather than a new Tauberian theorem.

This remains outside the desired Weil bridge and outside any claim to improve classical Weil positivity, Hilbert--Polya, Connes/trace, Sonin/localization, Frobenius/cohomological, or intersection-form approaches.

## 8. Consequence for `weil_positivity`

The infinite-dimensional escape left by `WP-197` is now narrower conceptually but broader as a matched control. In the natural power-law family, **every** bath that is admissible at order `4k` but rough enough to miss exactly one Schatten moment can manufacture full Weil-cone positivity around arbitrary finite positive geometry. Once the missing `(4k-1)`st source variation becomes summable, the universal manufacture disappears immediately.

So the relevant boundary is not the special `|xi|^{-1/2}` tail of `WP-198`; it is the source-boundary variation threshold itself:

\[
\boxed{
\mathcal S^{4k}\setminus\mathcal S^{4k-1}
\quad\text{is the entire universally stabilizing power-law strip,}
}
\tag{39}
\]

while the smoother `S^{4k-1}` side fails even on a one-channel off-zero control.

This strengthens the branch's no-repackaging gate. A future infinite-dimensional proposal cannot count full-cone positivity as explanatory merely because a rough sector is present. It must show that the critical roughness and its finite--infinite coupling are themselves forced by the Mathia arithmetic/archimedean geometry, and that the sign distinguishes that source-forced structure from the generic power-law reservoirs classified here.