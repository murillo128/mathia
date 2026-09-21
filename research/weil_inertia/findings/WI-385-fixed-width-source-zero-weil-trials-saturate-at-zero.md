# WI-385 — Fixed-width source-zero Weil trials saturate at zero under RH

**Status:** `EXACT-DERIVED + CLASSICAL-EXPLICIT-FORMULA + PRIMARY-SOURCE-OPERATOR-AUDIT + UNCONDITIONAL-DICHOTOMY + DECISIVE-COERCIVITY-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-384 reduces the exact arithmetic-plus-polar floor of the fixed-width source-zero trials to the scalar

\[
-A_L-2R_L(1)
\]

under RH, while leaving its sign open. Once the matching archimedean block is restored with the correct odd-fold normalization, the scalar is not independent: Weil's explicit formula identifies it exactly with the negative of the limiting archimedean energy.

Fix `L>0` and the WI-381/WI-384 profile

\[
g(s)=\sqrt{\frac2L}\cos\!\left(\frac{\pi s}{L}\right)
\mathbf 1_{|s|\le L/2},
\qquad
q=g*g,
\]

\[
G(z)=\int g(s)e^{zs}\,ds,
\qquad
Q(z)=G(z)^2
=\int q(t)e^{zt}\,dt.
\]

Since `g` is even and `\|g\|_2=1`, `q(0)=1`. Put

\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\]

and define the one-lobe bulk archimedean energy

\[
\boxed{
B_L:=-C_\Gamma+
\frac12\iint_{\mathbb R^2}
h(|s-t|)|g(s)-g(t)|^2\,ds\,dt.
}
\tag{1}
\]

Then, assuming RH only for the zero-side identification,

\[
\boxed{
A_L+2R_L(1)=2B_L,
}
\tag{2}
\]

where

\[
A_L=4\sum_{\gamma>0}m_\gamma Q(i\gamma)
\]

and

\[
R_L(x)=
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n x\right)
-2Q(1/2)\sqrt x.
\]

Consequently the WI-384 arithmetic-plus-polar recurrence floor is

\[
\boxed{
-A_L-2R_L(1)=-2B_L.
}
\tag{3}
\]

For the actual WI-380 depth-`\eta` construction, `L=L_\eta` was chosen so that `B_L<-\eta`; hence (3) is **strictly positive** and in fact

\[
-A_L-2R_L(1)>2\eta.
\tag{4}
\]

Thus the sign question left in WI-384 is resolved in the favorable direction for the arithmetic-plus-polar layer. But the reserve is exactly the amount needed to repay the two-lobe archimedean debt, and no uniform surplus remains.

Let `f_k` be the actual smooth source-zero odd trial from WI-380/WI-384, with positive lobe `F_k` and `A_k=\log(k+1)`. Write

\[
\mathcal W_k[f_k]
=Q_k^{\rm arch}+Q_k^{\rm arith}+Q_k^{\rm pol}
\tag{5}
\]

for the exact localized Weil quadratic form on that trial. Then

\[
\boxed{
Q_k^{\rm arch}=2B_L+o(1).
}
\tag{6}
\]

Combining (6) with WI-384 and WI-383 gives the exhaustive dichotomy

\[
\boxed{
\mathrm{RH}
\Longrightarrow
\liminf_{k\to\infty}\mathcal W_k[f_k]=0,
}
\tag{7}
\]

while

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\liminf_{k\to\infty}\mathcal W_k[f_k]=-\infty.
}
\tag{8}
\]

Under RH the returns to the zero floor inherit the relatively dense logarithmic recurrence from WI-383. Therefore, without assuming or denying RH, there is **no fixed `delta>0`** for which these admitted source-zero trials satisfy an eventual coercive estimate

\[
\mathcal W_k[f_k]\ge\delta\|f_k\|_2^2.
\tag{9}
\]

This closes the fixed-width source-zero route to a positive uniform Gate-II tariff. It does **not** refute nonnegativity: under RH these trials are asymptotic quasimodes that saturate Weil positivity at zero. A surviving rooted/Schur argument must either use only semidefinite positivity with no fixed coercive reserve on this family, exclude the trials through an additional graph/domain condition before (5) is tested, or exploit a source-coupling statement not equivalent to a positive lower bound for the exact old quadratic form on these vectors.

## 1. Weil's explicit formula fixes the scalar exactly

The standard Guinand--Weil explicit formula in the normalization used by Conrey states that for an even admissible spectral test `H(r)` with inverse Fourier transform `\widehat H(u)`, one has

\[
\sum_\gamma H(\gamma)
=
2H(i/2)
-\widehat H(0)\log\pi
+\frac1{2\pi}\int_{-\infty}^{\infty}
H(r)\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\widehat H(\log n),
\tag{10}
\]

with multiplicities and the usual symmetric interpretation of the zero sum.

Take

\[
H(r)=Q(ir).
\]

Because `Q(ir)` is the Fourier transform of the even compactly supported `q`, the inverse transform in (10) is exactly `q`; in particular `\widehat H(0)=q(0)=1`. Under RH the zero side is

\[
\sum_\gamma Q(i\gamma)=2\sum_{\gamma>0}m_\gamma Q(i\gamma)=\frac{A_L}{2}.
\tag{11}
\]

Hence (10) gives

\[
\frac{A_L}{2}
=
2Q(1/2)
-\log\pi
+\frac1{2\pi}\int_{\mathbb R}
Q(ir)\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}q(\log n).
\tag{12}
\]

Since `q` is supported on `[-L,L]`, the prime sum is finite. By the definition of `R_L(1)`, rearranging (12) yields

\[
A_L+2R_L(1)
=2\left[
-\log\pi
+\frac1{2\pi}\int_{\mathbb R}
Q(ir)\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
\right].
\tag{13}
\]

Thus it remains only to identify the bracket with (1).

## 2. The gamma integral is exactly the WI-369 bulk form

For `\operatorname{Re}z>0`, use the classical integral representation

\[
\psi(z)
=-\gamma+
\int_0^\infty
\frac{e^{-t}-e^{-zt}}{1-e^{-t}}\,dt.
\tag{14}
\]

Absolute convergence after pairing with `Q(ir)=O_L((1+|r|)^{-4})` permits Fubini. Fourier inversion gives

\[
\frac1{2\pi}\int_{\mathbb R}Q(ir)\,dr=q(0)=1,
\]

and

\[
\frac1{2\pi}\int_{\mathbb R}
Q(ir)\cos(rt/2)\,dr=q(t/2).
\]

Therefore the bracket in (13) equals

\[
-\log\pi-\gamma
+
\int_0^\infty
\frac{e^{-t}-e^{-t/4}q(t/2)}{1-e^{-t}}\,dt.
\tag{15}
\]

Set `t=2s`. Splitting the numerator into

\[
e^{-2s}-e^{-s/2}q(s)
=
\bigl(e^{-2s}-e^{-s/2}\bigr)
+e^{-s/2}(1-q(s))
\]

gives

\[
(15)=
-\log\pi-\gamma
+2\int_0^\infty
\frac{e^{-2s}-e^{-s/2}}{1-e^{-2s}}\,ds
+2\int_0^\infty h(s)(1-q(s))\,ds.
\tag{16}
\]

The first integral is the digamma special value

\[
2\int_0^\infty
\frac{e^{-2s}-e^{-s/2}}{1-e^{-2s}}\,ds
=\psi(1/4)+\gamma
=-\frac\pi2-3\log2.
\tag{17}
\]

Thus

\[
(15)
=-C_\Gamma
+2\int_0^\infty h(s)(1-q(s))\,ds.
\tag{18}
\]

Finally, since `q(s)=\int g(t+s)g(t)dt` and `\|g\|_2^2=1`,

\[
\frac12\iint_{\mathbb R^2}
h(|s-t|)|g(s)-g(t)|^2\,ds\,dt
=2\int_0^\infty h(u)(1-q(u))\,du.
\tag{19}
\]

Equations (18)--(19) identify the bracket in (13) with `B_L`, proving (2)--(3).

This identity is a specialization of the classical explicit formula, not a new explicit-formula theorem. The useful content here is that it closes the specific scalar left open by WI-384 and matches it to the exact archimedean block already reconstructed independently in WI-369.

## 3. The WI-380 choice forces the arithmetic-polar scalar positive

WI-380 chooses `L=L_\eta` so that, writing

\[
d(q)=2\int_0^\infty h(s)(1-\cos(qs))\,ds,
\]

one has

\[
-C_\Gamma+d(\pi/L)<-\eta.
\tag{20}
\]

The first Dirichlet cosine profile satisfies the whole-line estimate used there,

\[
2\int_0^\infty h(s)(1-q(s))\,ds
\le d(\pi/L).
\tag{21}
\]

Hence

\[
\boxed{B_L<-\eta.}
\tag{22}
\]

Combining (22) with (3) proves (4). Thus the arithmetic-plus-polar layer does have a genuine positive stationary reserve under RH, but its size is constrained by the explicit formula to be exactly `-2B_L`.

The factor two is load-bearing. `B_L` is the limiting archimedean energy of one positive lobe in the folded half-interval normalization. The unitary odd fold is `f\mapsto\sqrt2 f|_{(0,A)}`. Therefore the full odd trial carries twice this archimedean energy, which is why the reserve `-2B_L` cancels rather than overpays the archimedean debt.

## 4. Source perforation does not disturb the archimedean limit

Let `p_k` be the centered positive lobe of the smooth source-zero trial. WI-384 gives

\[
\|p_k-g\|_1
=O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right),
\qquad x_k=k+1,
\tag{23}
\]

and WI-380's screened-cutoff construction gives vanishing local jump cost across the source holes. In the smooth cutoff version this implies, for the WI-369 screened difference seminorm,

\[
\frac12\iint h(|s-t|)
\left|(p_k-g)(s)-(p_k-g)(t)\right|^2dsdt=o(1).
\tag{24}
\]

The associated norm also tends to zero, and the endpoint and Hankel-image terms of WI-369 vanish because the lobe remains a fixed distance `O_L(1)` wide while its center recedes like `A_k/2` from both physical endpoints. Hence

\[
\mathcal A_{A_k}[F_k]=B_L+o(1).
\tag{25}
\]

If `f_k` denotes the full odd extension with positive half `F_k`, the unitary odd fold sends it to `\sqrt2F_k`; therefore

\[
Q_k^{\rm arch}
=\mathcal A_{A_k}[\sqrt2F_k]
=2B_L+o(1),
\]

which is (6). This also fixes a normalization that was harmless for the sign-localization statements in WI-380 but is essential when the three exact operator layers are added.

## 5. Exhaustive RH / non-RH asymptotics

WI-384 proves

\[
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_L(x_k)-2R_L(1)+o(1).
\tag{26}
\]

Under RH, WI-383 gives

\[
\liminf_{k\to\infty}R_L(x_k)=-A_L,
\tag{27}
\]

with returns to this floor relatively dense on logarithmic scale. Combining (2), (6), (26), and (27),

\[
\begin{aligned}
\liminf_{k\to\infty}\mathcal W_k[f_k]
&=2B_L-A_L-2R_L(1)\\
&=0.
\end{aligned}
\tag{28}
\]

This proves (7), including recurrent near-zero saturation.

If RH is false, WI-382/WI-383 give

\[
\liminf_{k\to\infty}R_L(x_k)=-\infty.
\tag{29}
\]

The archimedean term still converges to the finite value `2B_L`, and the stationary correction `-2R_L(1)` is finite, so (26) and (29) give (8).

Since `\|f_k\|_2^2\to2`, either branch contradicts any eventual fixed positive coercive constant in (9). The conclusion is unconditional by exhaustion of RH and its negation; no RH statement is promoted to established evidence.

## 6. What this closes and what it does not

The result closes a specific direct-repair question left open by WI-384. The scalar `-A_L-2R_L(1)` is positive for the WI-380 profile, but it is not extra reserve. The classical explicit formula forces it to be exactly the negative of the full two-lobe archimedean limit. Hence the exact localized Weil form has no positive fixed floor on this source-zero family.

This is consistent with Weil positivity under RH: equation (28) produces asymptotic null directions, not negative ones. It also explains why estimating the critical-prime annulus, the polar root, and the gamma debit separately can create an apparent reserve which disappears once all exact normalizations are restored.

The finding does **not** show that Desogus's full theorem is false, does not refute semidefinite positivity, and does not by itself invalidate a Schur proof whose active admissible space excludes these vectors before the quadratic form is tested. It does rule out using the exact localized form on this admitted fixed-width source-zero family to obtain a `k`-uniform strictly positive tariff. Any such tariff must come from a hypothesis or subspace restriction absent from the trial construction, not from a stronger estimate of the same three operator layers.

## 7. Prior art and novelty audit

The identity used in Section 1 is classical Guinand--Weil explicit-formula machinery. A convenient normalization is J. Brian Conrey, *The Riemann Hypothesis*, Notices of the AMS 50 (2003), no. 3, 341--353, whose displayed prime/zero duality has exactly the `2h(i/2)`, digamma and Mangoldt terms used above. The original framework is André Weil's 1952 explicit-formula paper. The digamma integral and `\psi(1/4)=-\gamma-\pi/2-3\log2` are classical gamma-function identities.

The current primary operator source remains Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1. The arXiv submission history checked on 21 September 2026 still lists only v1, submitted 17 September 2026. Its RH conclusion is not imported as evidence.

WI-383 already records prior art for almost-periodic recurrence of explicit-formula error terms, including Kaczorowski--Ramaré and a recent Mittermeier checkpoint preprint. A targeted audit did not locate the particular source-zero fixed-width synthesis (2), the resolution of WI-384's scalar sign through the WI-369 archimedean block, or the resulting zero coercivity floor for the Desogus trial family. These are recorded only as an audit outcome, not as a priority claim.

## Research consequence

The fixed-width trial branch is now structurally closed at the level of direct uniform coercivity. Under RH, critical arithmetic plus polar energy repays the asymptotic gamma debt **exactly** and the full form recurrently approaches zero; under RH failure, the same family has arbitrarily negative excursions. There is no remaining constant to optimize inside this three-layer balance.

The efficient next question is therefore categorical rather than scalar: does the exact Gate-II graph/domain/shorting construction actually exclude these source-zero quasimodes from the active old space, or does it merely repackage the same exact Weil form? A genuine exclusion would evade the barrier. Another estimate of the critical annulus, the polar term, or the same fixed-profile Chebyshev remainder cannot.