# WP-211 — KMS Duhamel canonical correlation erases the critical half-density and still needs infinite Mangoldt mass

**Status:** `DERIVED + EXACT + BOST-CONNES-KMS + BOGOLIUBOV-KUBO-MORI + DUHAMEL-CORRELATION + LOGARITHMIC-MEAN + SOURCE-FORCED-CRITICAL-TEMPERATURE + HALF-DENSITY-LOSS + BOUNDED-MASS-OBSTRUCTION + SUPPORT-PRESERVING + MATCHED-CONTROL + PRIOR-ART-AUDITED + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-209` shows that the Bost–Connes critical KMS midpoint canonically supplies the Weil factor `q^{-1/2}`, but no bounded GNS correlation can carry the required all-prime Mangoldt mass. `WP-210` then closes the scalar free-energy repair: the canonical `1/k` primitive is just the Euler logarithm, while inverse-temperature Hessian positivity inserts the wrong prime-power multiplicity.

There is a distinct canonical thermodynamic positivity that those arguments do not yet test: the Bogoliubov–Kubo–Mori / Duhamel canonical correlation, obtained by averaging a KMS two-point function across the imaginary-time strip. For a bounded self-adjoint observable with KMS spectral weights

\[
C_X(t)=\sum_{q\in\mathbb Q_+^\times}c_q q^{it},
\qquad
c_q\ge0,
\qquad
c_{q^{-1}}=q^{-\beta}c_q,
\qquad
\sum_qc_q<\infty,
\]

the normalized strip average is

\[
D_X(t)
:=\frac1\beta\int_0^\beta C_X(t+iu)\,du.
\]

It has the exact positive Fourier weights

\[
\boxed{
D_X(t)
=c_1+2\sum_{q>1}
c_q\frac{1-q^{-\beta}}{\beta\log q}\cos(t\log q).
}
\]

The multiplier is the logarithmic mean of `1` and `q^{-\beta}`. Hence this is a genuine positive thermodynamic quadratic form, not a hand-picked kernel. But precisely because the whole KMS strip is averaged, the midpoint half-density is no longer retained. Writing `E=log q`,

\[
\frac{1-q^{-\beta}}{\beta\log q}
=q^{-\beta/2}
\frac{2\sinh(\beta E/2)}{\beta E}.
\]

At the Bost–Connes critical value `beta=1`, the second factor grows like `q^{1/2}/log q`; it cancels the critical square-root Boltzmann decay asymptotically. The canonical Duhamel/Kubo–Mori positivity therefore converts the source-forced midpoint carrier into a logarithmic-mean carrier rather than preserving the Weil half-density.

Matching the exact finite Weil prime-power coefficient is still impossible for a bounded observable. At `beta=1`, exact equality would require

\[
\boxed{
c_{p^k}
=
\frac{\Lambda(p^k)p^{-k/2}}{(1-p^{-k})/(k\log p)}
=
\frac{k(\log p)^2p^{-k/2}}{1-p^{-k}}.
}
\]

Already on the prime subfamily,

\[
c_p
=\frac{(\log p)^2}{\sqrt p(1-p^{-1})}
>\frac1p
\]

for all sufficiently large primes, so Euler's divergence of `sum_p 1/p` gives

\[
\sum_pc_p=\infty.
\]

This contradicts the finite GNS mass of every bounded correlation. Moreover the logarithmic-mean multiplier is strictly positive on every nonzero rational-log grade, so Duhamel averaging cannot create prime-power support: all unwanted mixed/composite grades must already vanish in the source observable.

Thus replacing scalar heat-capacity/variance positivity by the full noncommutative KMS canonical correlation does not open the `WP-209` escape. It gives a stronger matched control:

\[
\boxed{
\text{critical KMS source}
+\text{canonical Duhamel/BKM positivity}
\Longrightarrow
\text{positive logarithmic-mean spectrum},
}
\]

but

\[
\boxed{
\text{positive logarithmic-mean spectrum}
\not\Longrightarrow
\frac{\Lambda(n)}{\sqrt n}
\text{ from any bounded GNS observable}.
}
\]

The result does **not** rule out unbounded affiliated observables, distributional KMS vectors, closable forms, nontrivial boundary/cohomological assembly, or a genuinely global finite–archimedean coupling. It rules out the most canonical bounded noncommutative thermodynamic Hessian/canonical-correlation repair after `WP-210`.

## 1. Strip averaging gives the logarithmic mean exactly

Keep the `WP-209` KMS spectral decomposition at arbitrary inverse temperature `beta>0`:

\[
C_X(t)=\phi_\beta(X^*\sigma_t(X))
=\sum_qc_q q^{it},
\tag{1}
\]

with `c_q>=0`, finite total mass, and for self-adjoint `X`

\[
c_{q^{-1}}=q^{-\beta}c_q.
\tag{2}
\]

For an analytic element define

\[
D_X(t)
=\frac1\beta\int_0^\beta
C_X(t+iu)\,du.
\tag{3}
\]

The usual analytic-approximation/modular formulation gives the same canonical correlation on the natural bounded KMS domain. Termwise on a homogeneous grade `q!=1`,

\[
\frac1\beta\int_0^\beta q^{i(t+iu)}\,du
=q^{it}\frac{1-q^{-\beta}}{\beta\log q}.
\tag{4}
\]

Set

\[
m_\beta(q)
:=\frac{1-q^{-\beta}}{\beta\log q}>0,
\qquad q\ne1,
\tag{5}
\]

with continuous value `m_beta(1)=1`. Therefore

\[
D_X(t)=\sum_q c_qm_\beta(q)q^{it}.
\tag{6}
\]

Every Fourier coefficient in (6) is nonnegative, so `D_X` is positive definite. Equation (5) is the normalized logarithmic mean

\[
m_\beta(q)=L(1,q^{-\beta}),
\qquad
L(a,b)=\frac{a-b}{\log a-\log b}.
\tag{7}
\]

Using detailed balance,

\[
\begin{aligned}
c_{q^{-1}}m_\beta(q^{-1})
&=q^{-\beta}c_q
\frac{1-q^{\beta}}{-\beta\log q}\\
&=c_qm_\beta(q).
\end{aligned}
\tag{8}
\]

Thus for self-adjoint `X`,

\[
\boxed{
D_X(t)
=c_1+2\sum_{q>1}c_qm_\beta(q)\cos(t\log q).
}
\tag{9}
\]

This is exactly the spectral content expected of the Bogoliubov/Duhamel canonical correlation: imaginary-time averaging converts the ordered KMS correlation into a symmetric positive logarithmic-mean pairing.

## 2. The full canonical correlation cancels the midpoint half-density

`WP-209` isolates the KMS midpoint coefficient

\[
s_q^{(\beta)}=q^{-\beta/2}c_q.
\tag{10}
\]

Equation (5) factors relative to it as

\[
\boxed{
m_\beta(q)
=q^{-\beta/2}
\frac{2\sinh\!\left(\frac\beta2\log q\right)}
{\beta\log q}.
}
\tag{11}
\]

The factor multiplying the midpoint is at least one and grows exponentially in `|log q|`. At the Bost–Connes phase boundary `beta=1`,

\[
m_1(q)=\frac{1-q^{-1}}{\log q}
\sim\frac1{\log q}
\qquad(q\to\infty),
\tag{12}
\]

whereas the midpoint factor alone is `q^{-1/2}`. In other words, the canonical thermodynamic averaging that supplies the Bogoliubov/Duhamel sign theorem integrates over the entire KMS strip and replaces the distinguished midpoint geometry by its logarithmic mean.

This is a genuine structural tension rather than a normalization convention. Keeping only the midpoint recovers the source-forced half-density but returns to `WP-209`'s bounded-mass obstruction. Averaging the strip supplies the canonical thermodynamic inner product but removes that half-density from the spectral response.

## 3. Exact Weil matching forces infinite underlying GNS mass

At `beta=1`, the positive coefficient of the `q>1` cosine mode in (9), before the harmless common factor `2`, is

\[
a_q=c_q\frac{1-q^{-1}}{\log q}.
\tag{13}
\]

The desired finite-place Weil coefficient is

\[
w_q=\frac{\Lambda(q)}{\sqrt q},
\tag{14}
\]

with support only on prime powers. Exact coefficient matching requires

\[
c_q
=w_q\frac{\log q}{1-q^{-1}}.
\tag{15}
\]

For `q=p^k`, `log q=k log p` and `Lambda(q)=log p`, hence

\[
\boxed{
c_{p^k}
=\frac{k(\log p)^2p^{-k/2}}{1-p^{-k}}.
}
\tag{16}
\]

For `k=1`,

\[
c_p
=\frac{(\log p)^2p^{-1/2}}{1-p^{-1}}.
\tag{17}
\]

For all sufficiently large `p`, `(log p)^2>1` and `(1-p^{-1})^{-1}>1`, so

\[
c_p>p^{-1/2}>p^{-1}.
\tag{18}
\]

Euler's classical divergence of the prime harmonic series implies

\[
\boxed{
\sum_pc_p=\infty.
}
\tag{19}
\]

But a bounded GNS correlation has

\[
\sum_qc_q=\phi_1(X^*X)<\infty.
\tag{20}
\]

Equations (19)--(20) contradict each other. The obstruction is therefore already present on first prime powers; no summation over repetitions, zero data, or RH input is involved.

## 4. Canonical averaging also cannot manufacture the prime-power selector

The logarithmic-mean multiplier satisfies

\[
m_\beta(q)>0
\qquad(q>0,\ q\ne1).
\tag{21}
\]

Consequently

\[
c_qm_\beta(q)=0
\quad\Longleftrightarrow\quad
c_q=0.
\tag{22}
\]

So the Duhamel/Bogoliubov transform preserves spectral support exactly. If the starting bounded observable has positive mass on a non-prime-power rational grade, the canonical correlation retains it. Exact Mangoldt support must therefore be built into the source observable or obtained by some different quotient/cohomological mechanism before this positivity is applied.

This matters because a positive transform that merely rescales an already hand-selected prime-power spectrum is not the Mathia-native selector sought by the mandate.

## 5. Aggressive falsification of nearby repairs

**Could one choose the KMS midpoint instead of the strip average?** Yes, and that is exactly `WP-209`: it restores `q^{-1/2}` canonically, but exact Mangoldt amplitudes force infinite bounded-correlation mass.

**Could one use the strip average and then one time derivative?** A time derivative multiplies the `q` and `q^{-1}` modes by opposite imaginary signs. It therefore destroys the even positive spectral measure that supplied the canonical-correlation sign theorem. The operation may generate arithmetic coefficients, but positivity is no longer inherited from Duhamel/Bogoliubov geometry.

**Could one grant the positive absolute generator `|delta|` instead?** Even this stronger sign-friendly concession does not repair bounded mass. Multiplying (13) by `log q` gives `c_q(1-q^{-1})`; matching (14) then requires

\[
c_{p^k}
=\frac{(\log p)p^{-k/2}}{1-p^{-k}},
\tag{23}
\]

whose `k=1` prime subseries again diverges, since eventually `log p/\sqrt p>1/p`.

**Could a different inverse temperature fix the mismatch?** At general `beta`, the canonical coefficient is `c_q(1-q^{-beta})/(beta log q)`. Changing `beta` changes this logarithmic-mean response but does not create prime-power support. More importantly, the Riemann half-density is source-selected only at the actual Bost–Connes boundary `beta=1`; choosing another temperature to fit coefficients would abandon the intrinsic feature that made the route interesting.

**Could the inverse BKM metric rather than the canonical observable correlation help?** It is a genuinely different object: the state-space BKM metric is dual to the logarithmic-mean canonical correlation and involves the reciprocal mean. This finding does not classify unbounded state-space tangent forms in the type-III critical phase. Any such route must specify its domain and show that the required tangent is a legitimate finite-energy object rather than a distribution chosen from the Weil coefficients.

**Could an affiliated or distributional observable evade (20)?** Yes. Equation (20) is exactly the bounded-vector gate. A surviving unbounded construction must prove closability/domain control and positivity intrinsically; it cannot infer them from finite truncations. That remains an explicit live route.

## 6. Prior-art and novelty boundary

No novelty is claimed for the Bogoliubov/Kubo–Mori/Duhamel canonical correlation, its positivity, the logarithmic mean, or its information-geometric interpretation. Petz and Toth, *The Bogoliubov inner product in quantum statistics*, Letters in Mathematical Physics 27 (1993), 205–216, DOI `10.1007/BF00739578`, develops the Bogoliubov scalar product as a natural positive geometry in quantum statistics. Petz, *Geometry of canonical correlation on the state space of a quantum system*, Journal of Mathematical Physics 35 (1994), 780–795, DOI `10.1063/1.530611`, identifies the canonical correlation/Kubo–Mori geometry with the infinitesimal relative-entropy geometry and proves monotonicity in the finite quantum-state setting. Petz, *Monotone metrics on matrix spaces*, Linear Algebra and its Applications 244 (1996), 81–96, DOI `10.1016/0024-3795(94)00211-8`, gives the broader operator-monotone metric classification.

The Bost–Connes thermodynamic source and its `zeta(beta)` phase transition are classical and already anchored in this line's `SOURCES.md`. A directed audit for combinations of Bost–Connes with Kubo–Mori/Bogoliubov/Duhamel canonical correlations did not reveal a prior source asserting the present Weil-matching conclusion. The durable Mathia delta is not the classical metric itself, but the exact application of its logarithmic-mean spectral multiplier to the `WP-209` critical rational-log lattice:

\[
\boxed{
q^{-1/2}\text{ midpoint}
\longrightarrow
\frac{1-q^{-1}}{\log q}\text{ canonical strip average},
}
\tag{24}
\]

followed by the exact finite-GNS-mass contradiction (16)--(20).

This also sharpens `WP-210`. That finding rules out scalar inverse-temperature curvature because it changes the repetition law. The present result rules out the canonical **noncommutative observable Hessian/canonical-correlation** repair for a different reason: its logarithmic-mean averaging removes the critical half-density, preserves unwanted spectral support, and exact coefficient restoration again requires a non-normalizable bounded correlation vector.

## 7. Consequence for the research frontier

The Bost–Connes phase boundary remains one of the few Mathia-adjacent structures that selects the exponent `1/2` intrinsically. But the three most direct positive thermodynamic uses of that fact are now separated cleanly:

1. midpoint KMS correlation: exact half-density, but bounded all-prime mass fails (`WP-209`);
2. Euler/free-energy primitive and scalar thermodynamic curvature: the exact `1/k` channel is classical and curvature misweights repetitions (`WP-210`);
3. Duhamel/Bogoliubov canonical correlation: independent positive logarithmic-mean geometry, but it integrates away the half-density and still requires infinite bounded GNS mass (this finding).

A surviving KMS route must therefore change category rather than choose another standard bounded thermodynamic pairing. The live possibilities are an affiliated/distributional critical object with a proved closable positive form, or a genuinely global boundary/cohomological coupling in which the finite prime-power sector and the archimedean/polar sector enter before the sign theorem. The construction must also generate the prime-power selector rather than assume its spectral support.
