# WI-231 — local bow screens obey a radial Fejer count--depth tariff

**Status:** `EXACT-DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-210 proves that a local screen made only from critical-line zeros cannot cancel a dense symmetrized bow at all reciprocal harmonics: Fejer positivity makes the required critical-line count too large. WI-211--WI-212 show the precise escape: finitely many additional off-line functional-equation pairs can screen any fixed reciprocal packet, but the constructed pairs have normalized horizontal depth `a=log M+O(1)`. WI-227 then shows that shallow radial mass can be localized back toward the bow scale, leaving the depth of the off-line escape as the missing quantity to charge.

There is an exact quantitative bridge between these statements. If a local complementary population cancels the selected bow at the first `s` reciprocal harmonics, every off-line screening pair pays a **radial Fejer cost**

\[
\mathcal C_s(a)
:=2\sum_{k=1}^{s}(s+1-k)\bigl(\cosh(ka)-1\bigr).
\]

If the selected bow contains `M` right-half-plane labels, the local screen contains `R` complementary zero labels counted with multiplicity, and every one of the first `s` reciprocal harmonics is cancelled to error at most `eta M`, then

\[
\boxed{
\sum_j\mu_j\mathcal C_s(a_j)
\ge
\frac{s+1}{2}
\left((2s-s\eta)M-R\right).
}
\tag{1}
\]

Here `j` ranges over the additional off-line functional-equation pairs, `mu_j` is their multiplicity, and `a_j` is their normalized radial depth. Critical-line complementary zeros, including arbitrary multiplicity, contribute to `R` but not to the left side.

Thus the off-line escape from WI-210 is not free: whenever the local count is too small to pay the positive Fejer budget, the deficit must reappear as radial depth. For a full bow and the complete strictly interior reciprocal packet, the Riemann--von Mangoldt count from WI-184 forces the right side of (1) to be `Omega(M)`. Consequently every bounded-depth local screen contains a positive-density population of additional off-line pairs. Conversely, a sparse local screen must become deep.

The first harmonic gives an especially sharp count--depth law. If `a_max` is the largest screening depth, then

\[
\boxed{
R\cosh(a_{\max})\ge(2-\eta)M.
}
\tag{2}
\]

Hence a screen with `R=o(M)` necessarily has `a_max->infinity`; if `R=O(1)`, then `a_max>=log M+O(1)`. This proves that the logarithmic depth of the sparse WI-211--WI-212 screens is not an artifact of their self-reciprocal polynomial construction: it is forced already by the first reciprocal harmonic. In the zeta critical strip, (2) further gives the screen-count exponent constraint

\[
M=T^{\vartheta+o(1)},\quad
R=T^{\psi+o(1)},\quad d_T\to d
\qquad\Longrightarrow\qquad
\boxed{\psi\ge\vartheta-\frac1{2d}}
\tag{3}
\]

whenever the right side is positive. At the count-saturating bow spacing `d=2`, any same-interval local screen for a bow with `vartheta>1/4` therefore needs at least `T^{vartheta-1/4+o(1)}` complementary labels. An `O(1)` screen can exist only at `vartheta<=1/(2d)`, exactly the exponent threshold at which WI-212's sparse deep construction can remain inside the critical strip.

This does not prove that the required cancellation is local, does not exclude remote zeros or structured prime-side cancellation, and does not improve a global simple-critical proportion. Its value is to turn the qualitative WI-210 alternative "additional off-line mass or failure" into a quantitative two-currency ledger: **screen count versus radial depth**. That is the missing local interface needed for a genuine shallow-defect amplification or depth-escalation bootstrap.

## 1. Reciprocal-harmonic screen model

Use the WI-184/WI-210 normalization

\[
L_T:=\log T,
\qquad
x_j=\gamma_j\frac{L_T}{2\pi}=x_0+d_Tj,
\]

and let the selected bow contain `M` right-half-plane off-line labels. Write

\[
b_j=(\beta_j-\tfrac12)L_T>0.
\]

At the reciprocal harmonics

\[
\alpha_k=\frac{k}{d_T},
\qquad 1\le k<d_T,
\]

the selected zero and its compulsory same-ordinate functional-equation mirror have the common vertical phase. After rotating that phase away, the selected contribution is the positive real number

\[
B_k
=2\sum_{j\in J}\cosh\!\left(\frac{k b_j}{d_T}\right)
\ge2M.
\tag{4}
\]

Now suppose a complementary zero population in one local screen is decomposed into two parts. Critical-line labels have phases `z_l` on the unit circle and positive multiplicities `nu_l`; write

\[
S_k^{\rm crit}:=\sum_l\nu_l z_l^k,
\qquad
C:=\sum_l\nu_l.
\tag{5}
\]

Every additional off-line zero in the right half of the strip is grouped with its same-ordinate functional-equation mirror. For pair `j`, let `mu_j` be the multiplicity, let

\[
a_j:=\frac{(\beta_j-\tfrac12)L_T}{d_T}>0,
\qquad |w_j|=1,
\]

and write its reciprocal-harmonic contribution as

\[
S_k^{\rm off}
:=\sum_j2\mu_j\cosh(k a_j)w_j^k.
\tag{6}
\]

Put

\[
P:=\sum_j\mu_j,
\qquad
R:=C+2P.
\tag{7}
\]

Thus `R` is the number of complementary zero labels used by this screen, counted with multiplicity. Extra multiplicity at a selected bow point may be assigned to the selected side instead; if it is merely charged against the ambient count budget without being used in the screen, every bound below only becomes stronger.

Assume that for `1<=k<=s<d_T`,

\[
\boxed{
|B_k+S_k^{\rm crit}+S_k^{\rm off}|
\le\eta M.
}
\tag{8}
\]

The theorem is local and conditional on (8). It does not assert that the full zeta source has already been localized into such a population.

## 2. Radially corrected Fejer inequality

For `|z|=1`, the Fejer square is

\[
F_s(z)
:=|1+z+\cdots+z^s|^2
=(s+1)+2\sum_{k=1}^{s}(s+1-k)\Re z^k
\ge0.
\tag{9}
\]

For a mirror pair of depth `a` and phase `w=e^{i\theta}`, define its radially deformed Fejer expression

\[
G_s(a,\theta)
:=(s+1)
+2\sum_{k=1}^{s}(s+1-k)\cosh(ka)\cos(k\theta).
\tag{10}
\]

Separating the unit-circle part gives

\[
G_s(a,\theta)
=F_s(e^{i\theta})
+2\sum_{k=1}^{s}(s+1-k)
(\cosh(ka)-1)\cos(k\theta).
\]

Since `F_s>=0` and `cos(k theta)>=-1`,

\[
\boxed{
G_s(a,\theta)\ge-\mathcal C_s(a),
}
\tag{11}
\]

where

\[
\mathcal C_s(a)
:=2\sum_{k=1}^{s}(s+1-k)(\cosh(ka)-1).
\tag{12}
\]

Sum (9) over the critical-line screen with multiplicities. From (5),

\[
0\le
(s+1)C
+2\sum_{k=1}^{s}(s+1-k)\Re S_k^{\rm crit}.
\tag{13}
\]

Write the error in (8) as

\[
e_k:=B_k+S_k^{\rm crit}+S_k^{\rm off},
\qquad |e_k|\le\eta M.
\]

Substituting

\[
S_k^{\rm crit}=-B_k-S_k^{\rm off}+e_k
\]

into (13) yields

\[
\begin{aligned}
(s+1)C
&\ge
2\sum_{k=1}^{s}(s+1-k)B_k
+2\sum_{k=1}^{s}(s+1-k)\Re S_k^{\rm off}\\
&\qquad
-\eta M s(s+1),
\end{aligned}
\tag{14}
\]

because

\[
2\sum_{k=1}^{s}(s+1-k)|e_k|
\le\eta M s(s+1).
\]

For one off-line pair, equations (6) and (10) give

\[
4\mu_j\sum_{k=1}^{s}(s+1-k)
\cosh(k a_j)\cos(k\theta_j)
=2\mu_j\bigl(G_s(a_j,\theta_j)-(s+1)\bigr).
\]

Therefore (14), after adding `2(s+1)P` to both sides, becomes

\[
(s+1)R
\ge
2\sum_{k=1}^{s}(s+1-k)B_k
+2\sum_j\mu_jG_s(a_j,\theta_j)
-\eta M s(s+1).
\tag{15}
\]

Using `B_k>=2M`, (11), and

\[
\sum_{k=1}^{s}(s+1-k)=\frac{s(s+1)}2,
\]

we obtain

\[
(s+1)R
\ge
2s(s+1)M
-2\sum_j\mu_j\mathcal C_s(a_j)
-\eta M s(s+1).
\]

Rearranging proves (1):

\[
\boxed{
\sum_j\mu_j\mathcal C_s(a_j)
\ge
\frac{s+1}{2}
\bigl((2s-s\eta)M-R\bigr).
}
\tag{16}
\]

At `a=0`, the radial cost vanishes and (16) reduces to the positive-unit-circle count obstruction behind WI-210. The whole failure of that positive moment argument after admitting off-line pairs is therefore measured explicitly by the departures `cosh(ka)-1`.

## 3. Full local packets force macroscopic radial defect

Let

\[
r_T:=\max\{k\in\mathbb N:k<d_T\}.
\]

Take a bounded-spacing subsequence with `d_T->d>=2` and constant `r_T=r`, so

\[
r<d\le r+1.
\tag{17}
\]

For the full Maynard--Pratt bow, `M=m-O(1)`. WI-184 gives the entire local excess count beyond the selected bow and compulsory mirrors as

\[
E_I=(d_T-2+o(1))m.
\tag{18}
\]

If the whole screen in (8) lies in that same bow interval, then generously

\[
R\le E_I+O(1).
\tag{19}
\]

Take `s=r` and `eta=o(1)` in (16). Equations (17)--(19) give

\[
\begin{aligned}
\sum_j\mu_j\mathcal C_r(a_j)
&\ge
\left[
\frac{r+1}{2}(2r-d+2)+o(1)
\right]m\\
&\ge
\boxed{
\left(\frac{(r+1)^2}{2}+o(1)\right)m
},
\end{aligned}
\tag{20}
\]

because `d<=r+1`.

This is the quantitative version of WI-210's defect-to-defect alternative. The local excess population may contain critical-line zeros, repeated zeros, and additional off-line pairs in any mixture, but if it actually cancels all interior reciprocal harmonics then the **additional off-line pairs alone** must carry order-`m` radial Fejer cost.

In particular, if every additional off-line pair has

\[
a_j\le A
\]

for one fixed `A`, then

\[
\mathcal C_r(a_j)\le\mathcal C_r(A)=O_{r,A}(1),
\]

so (20) forces

\[
\boxed{
P=\sum_j\mu_j\gg_{r,A}m.
}
\tag{21}
\]

A bounded-depth local screen therefore requires a positive-density population of fresh off-line pair multiplicity. A screen with `P=o(m)` can survive only by sending some radial depths to infinity. This is precisely the shallow-defect-versus-depth-escalation split that remained qualitative after WI-210--WI-212.

The conclusion is about pair multiplicity, not automatically about distinct ordinates. WI-230 independently constrains repeated off-line mass in the near-extremal Lamzouri-v2 regime, but that extra input is not needed for (20)--(21) and is not silently folded into this finding.

## 4. The first harmonic gives a sharp sparse-screen law

For `s=1`,

\[
\mathcal C_1(a)=2(\cosh a-1),
\]

so (16) becomes

\[
\boxed{
\sum_j\mu_j(\cosh a_j-1)
\ge
M-\frac R2-\frac{\eta M}{2}.
}
\tag{22}
\]

This can also be read directly from the triangle inequality: the selected first-harmonic amplitude is at least `2M`; critical-line labels contribute modulus at most one per label; an off-line pair of multiplicity `mu` contributes modulus at most `2 mu cosh a`.

Let `a_max` be the largest depth among the off-line screening pairs. Whenever the right side of (22) is positive, `P<=R/2` gives

\[
\frac R2(\cosh a_{\max}-1)
\ge
M-\frac R2-\frac{\eta M}{2},
\]

hence the exact count--depth law

\[
\boxed{
\cosh a_{\max}
\ge
(2-\eta)\frac{M}{R}.
}
\tag{23}
\]

Several consequences are immediate.

If `R=o(M)` and `eta=o(1)`, then `a_max->infinity`. More quantitatively, if `R=O(1)`,

\[
a_{\max}\ge\log M+O(1).
\tag{24}
\]

Thus no fixed-size local screen can improve the `log M` radial-depth scale of WI-211--WI-212 to `o(log M)`. Their deep-screen scale is forced already before using the higher reciprocal moments.

For every nontrivial zeta zero, `beta<1`; therefore a right-half screening pair obeys

\[
a_j
=\frac{(\beta_j-\tfrac12)L_T}{d_T}
<\frac{L_T}{2d_T}.
\tag{25}
\]

Combining (23) and (25) gives the necessary local screen-count condition

\[
\boxed{
\frac RM
>
\frac{2-\eta}{\cosh(L_T/(2d_T))}.
}
\tag{26}
\]

If `d_T->d` and `eta=o(1)`, then

\[
\frac RM
\ge
(4+o(1))T^{-1/(2d)}.
\tag{27}
\]

Consequently, if

\[
M=T^{\vartheta+o(1)},
\qquad
R=T^{\psi+o(1)},
\qquad
0\le\psi<\vartheta,
\]

then every such local screen must satisfy

\[
\boxed{
\psi\ge\vartheta-\frac1{2d}.
}
\tag{28}
\]

For an `O(1)` screen this is the necessary condition

\[
\boxed{d\vartheta\le\frac12.}
\tag{29}
\]

WI-212 constructs an `O_d(1)` screen with `a=log M+O(1)` that stays inside the critical strip whenever `d\vartheta<1/2`. Thus (24) and (29) show that both the logarithmic radial scale and the critical-strip exponent threshold of that sparse-screen construction are sharp at the level of order/exponent. The endpoint equality is not claimed.

At the source-compatible count-saturating spacing `d=2`, (28) reads

\[
\boxed{
\psi\ge\vartheta-\frac14.
}
\tag{30}
\]

So for any fixed-power bow with `vartheta>1/4`, same-interval first-harmonic cancellation cannot be supplied by `O(1)` or even `T^{vartheta-1/4-o(1)}` complementary labels. It must use a polynomially growing local screen, leave the bow interval, or involve a nonzero/source-side term outside the zero-screen model.

## 5. Relation to the WI-227 localization frontier

WI-227 proves a different but complementary statement. For one fixed reciprocal harmonic, a cancelling dyadic screen either pays order-`M` radial-weighted mass beyond a chosen depth threshold or its shallow radial mass localizes within physical radius

\[
O((A+1)M/L_T).
\]

Equation (20) now identifies what would happen if a full reciprocal packet could be localized into a window whose zero-count excess is genuinely comparable with the original WI-184 bow budget: the shallow branch cannot be populated mostly for free. At bounded depth it creates `Omega(M)` additional off-line pair multiplicity; if that amplification is avoided, the radial depth must escalate.

This is not yet an iteration theorem. The current WI-227 localization radius carries an unspecified fixed collar constant, and Riemann--von Mangoldt only gives `O(M)` total labels in a generic bow-scale collar. Equation (19) is therefore an additional localization/count hypothesis when applying (20) to the exact WI-184 excess budget; WI-227 by itself does not supply it. Nor does (16) prevent the same deep pair from contributing to several harmonic or depth tests.

The remaining RH-facing target is now sharper: obtain source-fixed localization strong enough that the screen entering (16) inherits a sufficiently small local count budget, or prove that the deep radial charge forced by (16)/(23) cannot be recycled indefinitely. Either would turn the present exact local tariff into a genuine defect bootstrap.

## 6. Prior-art and novelty audit

The ingredients are classical. Fejer positivity and the positive truncated trigonometric moment problem underlie WI-210. Functional-equation symmetry supplies the reciprocal same-ordinate pairs and the `cosh(ka)` radial weights. Riemann--von Mangoldt supplies the local excess count in WI-184. The general literature on indefinite truncated trigonometric moments and Pontryagin-space interpolation explains qualitatively why admitting negative directions destroys positive-unit-circle moment rigidity; the line already records Derkach--Hassi--de Snoo and Derkach--Dym as neighboring prior art for that phenomenon.

A targeted search around Fejer kernels with radially deformed/reciprocal pairs, indefinite truncated trigonometric moments, Maynard--Pratt bow configurations, and zeta horizontal-depth pair contributions found those classical frameworks and the existing recent zeta proportion literature, but no source stating (16), the screen law (23), or the exponent necessity (28) for the symmetrized bow. Absence from that search is not used as a priority claim, and no priority claim is made.

The durable delta relative to the local Mathia corpus is narrower and exact. WI-210 says an all-critical local screen is impossible; WI-212 says a sparse off-line screen exists at depth `log M+O(1)`; WI-227 says shallow screens localize. Equations (16)--(30) prove that **radial depth is exactly the currency by which the off-line screen evades the positive Fejer count obstruction**, and that a sparse screen cannot pay less than logarithmic depth. This closes the route of seeking an `o(log M)` fixed-size finite-harmonic screen and supplies an explicit count--depth quantity for future bootstrap attempts.

## 7. Boundaries and falsification controls

The following restrictions are load-bearing.

First, (8) is a local zero-screen hypothesis. Remote zeros, the structured `Lambda^sharp` component in the WI-195 source representation, or another source-side term can cancel before the amplitude is represented by the local population above. No statement here proves that they do not.

Second, the selected bow must retain the reciprocal phase coherence of WI-184/WI-210 so that `B_k>=2M`. Arbitrary off-line populations without that coherent selected component are not covered.

Third, multiplicity is explicit. `R`, `C`, and `P` count labels/pair multiplicity, not only distinct ordinates. Critical-line multiple zeros remain positive-unit-circle mass; repeated off-line zeros multiply both their count and radial contribution. No conversion to distinct-zero density is made without an additional theorem such as the separate rigidity studied in WI-230.

Fourth, the complete-packet consequence (20) requires the screen to fit inside a region to which the WI-184 excess count applies. Enlarging the localization window can add `Theta(M)` labels and weaken or erase that particular count comparison. The algebraic tariff (16) itself remains exact for whatever actual screen count `R` is used.

Finally, the result changes no established global simple-critical proportion and does not rule out the WI-212 sparse deep screens. Instead it proves their depth scale is the necessary escape. A falsification would therefore have to exhibit a screen satisfying (4)--(8) for which (16) fails, or identify a normalization/counting mismatch in the reciprocal-pair contribution (6). Both reduce to finite exact inequalities; no unproved zeta statistics enter the derivation.