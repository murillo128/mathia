# WI-352 — Lipschitz equivariance automatically controls only the first charge moment

**Status:** `established`

**Claim type:** `EXACT-DERIVED + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + NON-RH`

**One-line statement:** In the `WI-351` setup, the first charge-Sobolev moment is not an independent hypothesis. If the phase-saturated feature map is `L`-Lipschitz and `U(1)`-equivariant, then along the normalized centered bow carrier
\[
B_1\le L,
\]
and hence `B_s<=L` for every `0<s<=1`. Combining this automatic bound with `WI-351` gives, with `h=H\Delta` and `x=L/(\mu\sqrt\tau)`,
\[
\boxed{r_\tau(G)\le (1+4x)(1+hx/2).}
\]
For `h<=1`, this implies
\[
\boxed{\frac L\mu\ge \sqrt\tau\,\frac{\sqrt{32r_\tau(G)+49}-9}{8}.}
\]
The regularity threshold is sharp: Lipschitz equivariance alone does not force any `B_{1+\varepsilon}<\infty`. Therefore the `s=1` charge-tail route in `WI-351` collapses to the already-generic square-root sensitivity tariff; genuinely stronger charge-tail information must come from more than ordinary Lipschitz equivariance.

## Why this matters

`WI-350` showed that finitely many active charges force a linear rank-versus-resolution cost. `WI-351` replaced hard charge count by a weighted tail moment `B_s` and left open whether ordinary smooth equivariance might itself control enough charge regularity to strengthen the generic `WI-348` square-root barrier.

There is an exact boundary. Ordinary Lipschitz control of an equivariant feature automatically supplies precisely one angular derivative in the Hilbert/Sobolev sense. That makes `B_1` bounded by the same sensitivity constant `L` already charged by the height cover, so the two apparent currencies in `WI-351` are not independent at `s=1`. Conversely, one angular derivative is the most that can be inferred: there are Lipschitz equivariant phase orbits with finite `B_1` and infinite `B_{1+\varepsilon}` for every `\varepsilon>0`.

Thus a stronger bow obstruction based on charge tails cannot be obtained merely by reusing the existing Lipschitz hypothesis. It must prove higher angular regularity, exploit source-specific arithmetic structure, or leave this feature class. This does not establish the distinguished `\Lambda-\Lambda^\sharp` covariance sign and does not improve a zeta-zero proportion.

## 1. Automatic first charge moment

Keep the notation and hypotheses of `WI-351`. The normalized centered source vector `z=z_U` has `\|z\|=1`, the output representation decomposes as
\[
\mathcal K=\widehat\bigoplus_{q\in\mathbb Z}\mathcal K_q,
\qquad
R(e^{i\phi})|_{\mathcal K_q}=e^{iq\phi}I,
\]
and
\[
v:=F(z)=\sum_{q\in\mathbb Z}v_q,
\qquad v_q=P_qv.
\]
Equivariance and the `L`-Lipschitz hypothesis give, for every real `t`,
\[
\begin{aligned}
\|R(e^{it})v-v\|
&=\|F(e^{it}z)-F(z)\|\\
&\le L\,\|e^{it}z-z\|\\
&=2L\left|\sin\frac t2\right|\|z\|.
\end{aligned}
\tag{1}
\]
Orthogonality of the charge decomposition therefore yields
\[
\sum_q
\frac{|e^{iqt}-1|^2}{t^2}\,\|v_q\|^2
\le
L^2\left(\frac{2\sin(t/2)}t\right)^2\|z\|^2.
\tag{2}
\]
Let `t->0`. For each fixed integer `q`,
\[
\frac{|e^{iqt}-1|^2}{t^2}\longrightarrow q^2.
\]
Fatou's lemma applied to the nonnegative series in (2) gives
\[
\boxed{
\sum_q q^2\|P_qF(z)\|^2\le L^2\|z\|^2.
}
\tag{3}
\]
Since `\|z_U\|=1` uniformly,
\[
\boxed{B_1\le L.}
\tag{4}
\]
No differentiability of `F` is assumed or inserted. Equation (3) is the direct Fourier form of the standard statement that a Lipschitz unitary orbit lies in the domain of its infinitesimal generator.

For every `0<s<=1`, integer charges satisfy `|q|^{2s}<=q^2` for `q\ne0`; the zero charge contributes nothing to either homogeneous moment. Hence
\[
\boxed{B_s\le B_1\le L\qquad(0<s\le1).}
\tag{5}
\]

## 2. The resulting effective-rank bound

`WI-351`, equation (26), proves for `s=1`
\[
r_\tau(G)
\le
\left(1+\frac{4B_1}{\mu\sqrt\tau}\right)
\left(1+\frac{H\Delta L}{2\mu\sqrt\tau}\right).
\tag{6}
\]
Insert (4), and write
\[
x:=\frac{L}{\mu\sqrt\tau},
\qquad h:=H\Delta.
\]
Then
\[
\boxed{
r_\tau(G)\le(1+4x)(1+hx/2)
=1+(4+h/2)x+2hx^2.
}
\tag{7}
\]
If `0<h<=1`, inversion of the quadratic gives the exact necessary condition
\[
\boxed{
x\ge
\frac{
\sqrt{(8+h)^2+32h(r_\tau(G)-1)}-(8+h)
}{8h}.
}
\tag{8}
\]
At the natural aperture `h<=1`, the weakest member of (8) is obtained at the coarse bound `h=1`, giving
\[
\boxed{
\frac L\mu
\ge
\sqrt\tau\,\frac{\sqrt{32r_\tau(G)+49}-9}{8}
=\left(\sqrt{\frac\tau2}+o(1)\right)\sqrt{r_\tau(G)}.
}
\tag{9}
\]
For the degenerate centered-width case `h=0`, (7) becomes `r_\tau(G)<=1+4x`, so the phase orbit alone retains the stronger linear relation `x>=(r_\tau(G)-1)/4`.

The order in (9) is the same generic square-root sensitivity tariff isolated in `WI-348`, though with a much sharper constant inside the equivariant class. Thus `B_1` does not create a second independent obstruction on top of the Lipschitz cost: it is already paid for by `L`.

## 3. Why higher charge moments do not follow from Lipschitz control

The threshold at one angular derivative is genuine. Let
\[
\mathcal K=\ell^2(\{2,3,\ldots\}),
\qquad
R(e^{i\phi})e_q=e^{iq\phi}e_q,
\]
and choose a nonzero vector
\[
v=\sum_{q\ge2}a_qe_q,
\qquad
|a_q|^2=\frac{c^2}{q^3(\log q)^2}
\tag{10}
\]
with any fixed `c>0`. Then
\[
B_1(v)^2
=c^2\sum_{q\ge2}\frac1{q(\log q)^2}<\infty,
\tag{11}
\]
whereas for every `\varepsilon>0`,
\[
B_{1+\varepsilon}(v)^2
=c^2\sum_{q\ge2}
\frac{q^{-1+2\varepsilon}}{(\log q)^2}
=\infty.
\tag{12}
\]

Take the phase-saturated unit input orbit `S^1\subset\mathbb C` and define
\[
F(e^{i\phi})=R(e^{i\phi})v.
\tag{13}
\]
This map is exactly `U(1)`-equivariant and has constant nonzero output norm. Because `B_1(v)<\infty`, its phase derivative exists in `\ell^2` with constant norm `B_1(v)`. For the shortest angular distance `d\in[0,\pi]`,
\[
\|F(e^{i\phi})-F(e^{i\psi})\|
\le B_1(v)d
\le\frac\pi2B_1(v)|e^{i\phi}-e^{i\psi}|.
\tag{14}
\]
Hence `F` is Lipschitz on its phase-saturated domain while every higher moment in (12) diverges.

So no theorem using only the `WI-351` assumptions of Lipschitz equivariance and a transmission floor can silently upgrade (4) to `B_{1+\varepsilon}<\infty`, even for arbitrarily small positive `\varepsilon`.

## 4. Consequence for the `WI-351` escape analysis

The growth condition in `WI-351` says that, if an equivariant feature retains the sharp generic height-resolution regime `L/\mu=O(\sqrt r)`, then finite `B_s` must satisfy
\[
B_s/\mu=\Omega(r^{s/2}).
\]
For `s=1`, the automatic upper bound `B_1/\mu<=L/\mu` has exactly the same `\sqrt r` scale. There is therefore no additional asymptotic contradiction to extract: first-order angular complexity can grow at precisely the rate already permitted by the generic sensitivity budget.

For `0<s<1`, the required `r^{s/2}` growth is weaker still. The first potentially stronger Sobolev-charge input begins strictly above `s=1`, and Section 3 shows that such information is not a consequence of ordinary Lipschitz equivariance. Any future use of `WI-351` to beat the generic square-root feature barrier must therefore identify a genuine higher-angular-regularity theorem for the arithmetic witness, or use a different source-specific invariant rather than counting `B_1` as independent complexity.

This is a route-specific no-go, not a theorem that all equivariant feature methods fail. Correlations between height and charge, non-Sobolev tail information, explicit source arithmetic, vanishing transmission, growing aperture, or a different witness architecture remain outside the statement.

## 5. Prior art and novelty boundary

The harmonic-analysis ingredients are classical. Stone's theorem identifies the domain of the generator of a strongly continuous one-parameter unitary group with vectors admitting a strong orbit derivative; see M. H. Stone, **On One-Parameter Unitary Groups in Hilbert Space**, *Annals of Mathematics* 33:3 (1932), 643--648, DOI `10.2307/1968538`. The Fourier/Sobolev interpretation of one angular derivative as square-summability of frequency-weighted coefficients is standard; see the *Encyclopedia of Mathematics*, **Sobolev space**, https://encyclopediaofmath.org/wiki/Sobolev_space. The compact-abelian charge decomposition and Fourier-tail step were already anchored in `WI-350`--`WI-351`.

The proof of (3) deliberately does not invoke a differentiability theorem: the Lipschitz chord estimate, orthogonal charge decomposition, and Fatou give the generator-energy bound directly. The sequence (10) is the standard strictness phenomenon between first-order and higher Sobolev regularity.

No novelty is claimed for those facts. The durable Mathia delta is their exact interaction with `WI-351`: `B_1` is automatically bounded by the same `L` already present in the bow height cover, yielding (7)--(9), while no `B_{1+\varepsilon}` control follows from the same hypotheses. Repository audit found `WI-351` identifying `B_1` with the phase-generator norm but not deriving this automatic bound or its sharp higher-order failure. The finding therefore closes a specific apparent independent-complexity escape without redefining the accepted distinguished-twist problem.

## 6. Boundary conditions and falsification

The automatic estimate uses all of the following:

- `F` is Lipschitz on the **phase-saturated** source domain, not merely along the physical height curve;
- the equivariance uses a strongly continuous unitary `U(1)` representation;
- the input phase action is ordinary scalar multiplication;
- the centered bow carrier is normalized, so `\|z_U\|=1`;
- the charge decomposition is the same one used in `WI-351`.

If Lipschitz control is known only in height, or if the relevant arithmetic map is not controlled uniformly along its full phase orbit, (3) need not follow. Likewise this finding does not prohibit a source theorem that proves `B_s` for some `s>1`; it says such a theorem would be genuinely additional regularity rather than a repackaging of the existing Lipschitz assumption.

A decisive falsification would therefore be either an explicit `WI-351`-admissible Lipschitz equivariant map violating (3), or an error in applying the orthogonal charge decomposition/Fatou passage. The sharpness example already rules out strengthening the conclusion to any universal `B_{1+\varepsilon}` bound under the same assumptions.

## Research consequence

The generic phase-feature branch is now cleaner. Finite charge count (`WI-350`) gives a linear rank cost; soft charge tails (`WI-351`) can improve on the generic geometry only when they encode more than one angular derivative; and ordinary Lipschitz equivariance automatically supplies exactly that first derivative and no more. The remaining high-value target is therefore still the accepted source-specific clue: a theorem forcing the distinguished signed `\Lambda-\Lambda^\sharp` off-diagonal covariance, or a genuinely arithmetic mechanism that creates higher angular/charge regularity. Further bookkeeping of `B_1` as an independent feature-complexity parameter cannot by itself move the RH-facing frontier.