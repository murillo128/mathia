# WI-158 — the BGSTB pointwise error is not uniform on singular near-extremizers

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

WI-157 closes every growing support-one scalar Lamzouri portfolio for which the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB) form-factor error can be integrated uniformly, and gives the sufficient regularity gate

\[
\|r_L\|_\infty=o(L),\qquad \|r_L\|_1=o(\sqrt L),
\qquad L=\log T,
\]

for the deweighted profile

\[
r_L(\alpha)=\phi_L(\alpha)-\frac{\phi_L''(\alpha)}{4L^2}.
\]

That finding deliberately leaves open a singular `T`-dependent family whose norms violate the gate. The present finding shows that this boundary is not an artifact of a crude Hölder estimate. The `L^1=o(\sqrt L)` condition is order-sharp relative to the **published pointwise BGSTB theorem**: there are smooth support-one Lamzouri kernels whose one-delta cost converges to the exact Montgomery--Taylor optimum, with

\[
\|r_L\|_\infty=O(\sqrt L)=o(L),
\qquad
\|r_L\|_1=\Theta(\sqrt L),
\]

and there are nonnegative model form factors satisfying the full stated BGSTB pointwise asymptotic, with the same uniform `O(L^{-1/2})` bulk error, for which the integrated error against `r_L` tends to an arbitrary prescribed negative constant.

Consequently the BGSTB Theorem 1 asymptotic, even supplemented by pointwise nonnegativity of the form factor, cannot by itself justify a singular support-one scalar improvement. Any such escape must use **new arithmetic information about the error beyond its pointwise size** — for example frequency-sensitive cancellation, regularity, an averaged error theorem, or an equivalent unweighted form-factor estimate — or leave the one-scalar/support-one architecture. This is a logical insufficiency theorem for the published arithmetic interface; it does not assert that the actual zeta form-factor error realizes the adversarial oscillations constructed below.

## 1. Build admissible Lamzouri kernels arbitrarily close to the CCLM extremizer

Use the Fourier convention

\[
\widehat f(x)=\int_{\mathbb R}f(u)e^{-2\pi i xu}\,du
\]

and put

\[
I=[-1/2,1/2].
\]

The CCLM/Montgomery--Taylor one-delta minimizer in the Paley--Wiener variable is

\[
f_*(u)=\frac{\sqrt2}{2\sin(1/\sqrt2)}\cos(\sqrt2\,u),
\qquad u\in I,
\]

normalized by `int_I f_*=1`. It is strictly positive on the whole closed interval. As in WI-157, its quadratic cost is

\[
Q_1(f_*)=m_{\rm MT}
=\frac1{\sqrt2}\cot\frac1{\sqrt2}-\frac12.
\]

Choose even nonnegative smooth cutoffs `g_L in C_c^infty((-1/2,1/2))`, normalized by

\[
\int_I g_L=1,
\]

such that

\[
g_L\to f_*
\quad\text{in }L^2(I)
\]

and `g_L` stays uniformly bounded below on `[-1/4,1/4]`. For example one may multiply `f_*` by a square smooth cutoff whose boundary layer has width `L^{-1/16}` and renormalize. This choice also has

\[
\|g_L'\|_1=O(1),
\]

and its Fourier coefficients at frequencies `asymp L^{3/2}` are `o(L^{-1/4})` by one integration by parts.

Fix once and for all a nonzero even function

\[
\psi\in C_c^\infty((-1/4,1/4)),
\qquad \psi\ge0.
\]

Write

\[
A_j:=\widehat\psi(j)
=\int\psi(u)\cos(2\pi j u)\,du,
\qquad j=0,1.
\]

Because `cos(2 pi u)` is positive and strictly below one away from the origin on the support of `psi`,

\[
\boxed{0<A_1<A_0},
\qquad
\boxed{d_\psi:=A_0^2-A_1^2>0.}
\tag{1}
\]

Let

\[
\varepsilon_L=L^{-1/4},
\qquad
n_L\sim cL^{3/2}
\]

with `n_L` an integer and `c>0` fixed. Define

\[
Z_L
:=1+\varepsilon_L\widehat\psi(n_L),
\]

and

\[
\boxed{
f_L(u)
=Z_L^{-1}
\left[g_L(u)+\varepsilon_L\psi(u)\cos(2\pi n_Lu)\right].
}
\tag{2}
\]

Since `widehat psi(n_L)` decays faster than every power, `Z_L=1+o(1)`. The perturbation is supported where `g_L` has a fixed positive lower bound, so `f_L>=0` for all large `L`; it is even, smooth, compactly supported in `I`, and exactly normalized by

\[
\int_I f_L=1.
\tag{3}
\]

Hence it lies in the concrete Lamzouri factor class: one may take `eta_L=sqrt(f_L)` after choosing the standard flat boundary cutoff. Put

\[
\phi_L=f_L*f_L,
\qquad
H_L(x)=\widehat\phi_L(x)=\widehat f_L(x)^2.
\tag{4}
\]

Then `phi_L` is real, even, smooth and supported in `[-1,1]`, while

\[
H_L(x)\ge0\quad(x\in\mathbb R),
\qquad H_L(0)=1.
\tag{5}
\]

Moreover `f_L-f_* ->0` in `L^2(I)`, because the cutoff error tends to zero and the oscillatory perturbation has `L^2` norm `O(epsilon_L)`. The boundedness of the CCLM integral operator therefore gives

\[
Q_1(f_L)\to Q_1(f_*)=m_{\rm MT}.
\tag{6}
\]

Equivalently, the limiting scalar pair-correlation cost satisfies

\[
\boxed{C(\phi_L)\to C_{\rm MT}.}
\tag{7}
\]

Thus the construction is not made expensive by moving away from the one-delta optimum: it is an asymptotically extremizing Lamzouri family.

## 2. The deweighting operator amplifies the hidden high frequency

Define the exact Lamzouri/BGSTB deweighted profile

\[
r_L(\alpha)
=\phi_L(\alpha)-\frac{\phi_L''(\alpha)}{4L^2}.
\tag{8}
\]

Since `widehat{phi_L}=H_L`, for every real `x`

\[
\boxed{
\widehat r_L(x)
=\left(1+\frac{\pi^2x^2}{L^2}\right)H_L(x).
}
\tag{9}
\]

At the three integer frequencies `n_L+j`, `j=0,+-1`, equation (2) gives

\[
\widehat f_L(n_L+j)
=Z_L^{-1}\left[
\widehat g_L(n_L+j)
+\frac{\varepsilon_L}{2}
\bigl(\widehat\psi(j)+\widehat\psi(2n_L+j)\bigr)
\right].
\tag{10}
\]

The cutoff Fourier terms and the `2n_L+j` terms are `o(epsilon_L)`, hence

\[
H_L(n_L)
=\frac{\varepsilon_L^2}{4}A_0^2+o(\varepsilon_L^2),
\tag{11}
\]

\[
H_L(n_L+-1)
=\frac{\varepsilon_L^2}{4}A_1^2+o(\varepsilon_L^2).
\tag{12}
\]

Therefore, with

\[
S_L
:=\widehat r_L(n_L)
-\frac12\widehat r_L(n_L-1)
-\frac12\widehat r_L(n_L+1),
\]

we obtain from (1), (9)--(12), and `n_L/L -> infinity`

\[
\boxed{
S_L
=\frac{\pi^2d_\psi}{4}
\frac{\varepsilon_L^2n_L^2}{L^2}
\bigl(1+o(1)\bigr).
}
\tag{13}
\]

For the chosen scales

\[
\varepsilon_L^2=L^{-1/2},
\qquad
n_L^2\sim c^2L^3,
\]

so

\[
\boxed{
S_L
=\frac{\pi^2c^2d_\psi}{4}\sqrt L\,(1+o(1)).
}
\tag{14}
\]

This is the precise amplification scale hidden by a fixed-test limit.

## 3. A BGSTB-sized pointwise error can produce an order-one integrated shift

Set

\[
b(\alpha)=1-\cos(2\pi\alpha)
\]

and, for a fixed `a>0`, define on `[-1,1]`

\[
\boxed{
E_L(\alpha)
=-aL^{-1/2}
 b(\alpha)\cos(2\pi n_L\alpha).
}
\tag{15}
\]

It is real and even and obeys

\[
\|E_L\|_\infty\le2aL^{-1/2}.
\tag{16}
\]

The elementary identity

\[
b(\alpha)\cos(2\pi n\alpha)
=\cos(2\pi n\alpha)
-\frac12\cos(2\pi(n-1)\alpha)
-\frac12\cos(2\pi(n+1)\alpha)
\tag{17}
\]

and the support/evenness of `r_L` give the exact pairing

\[
\begin{aligned}
2\int_0^1E_L(\alpha)r_L(\alpha)\,d\alpha
&=\int_{-1}^1E_L(\alpha)r_L(\alpha)\,d\alpha\\
&=-aL^{-1/2}S_L.
\end{aligned}
\tag{18}
\]

Using (14),

\[
\boxed{
2\int_0^1E_Lr_L
\longrightarrow
-\frac{a\pi^2c^2d_\psi}{4}.
}
\tag{19}
\]

The limiting negative constant can be made arbitrarily large in magnitude by increasing `c`, even though the pointwise error remains `O(L^{-1/2})` with exactly the same constant `2a`.

This adversarial error can also be made compatible with the elementary positivity enjoyed by the actual form factor. Define the model

\[
\widetilde F_L(\alpha)
=Le^{-2L\alpha}+\alpha+E_L(\alpha),
\qquad 0\le\alpha\le1.
\tag{20}
\]

Since

\[
0\le b(\alpha)\le2\pi\alpha
\qquad(0\le\alpha\le1),
\tag{21}
\]

for `L>(2 pi a)^2` we have

\[
|E_L(\alpha)|
\le2\pi aL^{-1/2}\alpha
\le\alpha.
\tag{22}
\]

Consequently

\[
\boxed{\widetilde F_L(\alpha)\ge0}
\tag{23}
\]

throughout `[0,1]`, while (20) satisfies exactly the published BGSTB Theorem 1 shape

\[
\boxed{
\widetilde F_L(\alpha)
=e^{-2L\alpha}(L+O(1))
+\alpha+O(L^{-1/2})
}
\tag{24}
\]

uniformly on `[0,1]`.

Thus neither the pointwise error envelope nor pointwise nonnegativity prevents the order-one shift (19).

## 4. The `sqrt(L)` norm gate from WI-157 is saturated, not merely violated

The same construction lands exactly at the scale where WI-157's integrated BGSTB error ceases to be `o(1)`. From (17)--(18) with `E_L` stripped of its prefactor,

\[
|S_L|
\le2\|r_L\|_1,
\]

so (14) implies

\[
\|r_L\|_1\gg\sqrt L.
\tag{25}
\]

For the converse bound, write `phi_L=f_L*f_L`. Because the factors vanish smoothly at their support boundary,

\[
\phi_L''=f_L'*f_L'.
\]

The construction has

\[
\|f_L'\|_1=O(1+\varepsilon_Ln_L),
\]

and hence Young's inequality gives

\[
\|\phi_L''\|_1
\le\|f_L'\|_1^2
=O(\varepsilon_L^2n_L^2).
\]

Since `||phi_L||_1=1`, equations (8) and the chosen scales yield

\[
\boxed{\|r_L\|_1=\Theta(\sqrt L).}
\tag{26}
\]

Similarly

\[
\|\phi_L''\|_\infty
\le\|f_L'\|_2^2
=O(\varepsilon_L^2n_L^2)
\]

(up to the slower cutoff contribution), so

\[
\boxed{\|r_L\|_\infty=O(\sqrt L)=o(L).}
\tag{27}
\]

The exponential `O(1)e^{-2L alpha}` error in BGSTB therefore remains harmless under WI-157's first norm gate. The obstruction is specifically the uniform bulk remainder `O(L^{-1/2})`: its natural dual threshold is exactly `||r_L||_1=o(sqrt L)`, and (26) shows that threshold can be saturated by asymptotically one-delta-optimal admissible kernels.

More generally, if a high-frequency perturbation has amplitude `epsilon_L` and frequency `n_L`, the dangerous scale is

\[
\boxed{
\varepsilon_L^2n_L^2\asymp L^{5/2}.
}
\tag{28}
\]

The choice `epsilon_L=L^{-1/4}`, `n_L asymp L^{3/2}` is only a convenient representative. Since `epsilon_L ->0`, the scalar variational cost can converge to the MT optimum while the arithmetic susceptibility remains order one.

## 5. What this closes and what survives

The result closes a specific remaining shortcut after WI-156--WI-157. One cannot take the published uniform-in-`alpha` BGSTB pointwise theorem, insert an increasingly oscillatory `T`-dependent Lamzouri kernel, and argue that the fixed-test arithmetic evaluation remains asymptotically valid merely because the kernel stays support one, normalized, Fourier-nonnegative, close to the CCLM extremizer, or because the form factor itself is nonnegative. Equations (19)--(24) give an explicit adversarial envelope showing that those facts do not determine the needed integral.

This does **not** prove that the actual zeta form-factor error has such an oscillatory component. The model `widetilde F_L` is required only to satisfy the information supplied by the published pointwise theorem plus nonnegativity; it is not claimed to be realizable as a zeta pair sum or to satisfy every hidden positive-definiteness identity of the true form factor. Therefore the conclusion is epistemic/methodological but rigorous: a proof using a singular family must import an additional arithmetic theorem that excludes or cancels this behavior.

The missing information can be stated in several equivalent-looking ways. One may seek an integrated BGSTB remainder estimate uniform in a stronger oscillatory norm, a frequency-localized estimate for the error, a theorem for the **unweighted** form factor obtained after moving the deweighting differential operator off the test, or a genuinely joint statistic that never collapses to this scalar pairing. Any of these would be new arithmetic information, not a consequence of BGSTB Theorem 1 as currently stated.

The finding also does not cap the Gram-defect/inertia record of this research line, the Lamzouri finite-dimensional slack program of WI-126--WI-142, joint multi-profile inequalities, higher correlations, or justified support greater than one. Those routes retain information discarded before the scalar one-delta interface.

## 6. Prior-art and novelty audit

The arithmetic theorem being stress-tested is Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya and Caroline L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376, arXiv:2306.04799. Their Theorem 1 gives, uniformly for `0<=alpha<=1`, the pointwise form-factor expansion with bulk error `O((log T)^-1/2)`; their fixed-test integration does not state a uniform theorem for a `T`-dependent oscillatory family.

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, performs the exact weight removal with `Q-Q''/(4 log^2 T)` and explicitly avoids applying the fixed-test pair-correlation lemma directly to a changing test without additional uniformity. WI-157 reconstructs that deweighting and solves the resulting finite-height one-delta main variational problem exactly.

The sharp limiting scalar extremal is established prior art from Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, especially Corollary 14. Equations (2)--(7) above deliberately place the adversarial family inside an arbitrarily small neighborhood of that established extremizer.

A targeted audit around uniform pair-correlation estimates for changing/oscillatory test functions, singular support-one families, and Lamzouri weight removal located the fixed-test BGSTB/CCLM framework and Lamzouri's explicit uniformity warning, but no prior theorem giving the adversarial sharpness construction (13)--(28). This is not a claim of mathematical priority. The line-specific novelty is the exact stress test showing that WI-157's `L^1=o(sqrt L)` gate is saturated by admissible near-extremizers and cannot be removed using only the currently published pointwise arithmetic information.

## 7. Research disposition

**Decisive negative for the singular-profile shortcut.** The regular growing scalar portfolio is closed by WI-157; the first singular boundary is now known to be genuinely unstable under the available BGSTB pointwise error. The live scalar escape is no longer “choose a more singular support-one test.” It is “prove new arithmetic cancellation for the oscillatory BGSTB remainder at the critical scale (28).” Without that new input, scalar support-one optimization cannot be advanced by a `T`-dependent profile.

For the broader Weil-inertia mandate, priority should therefore remain on information carriers that do not factor through one scalar pair-sum — the exact Lamzouri slack/inertia layers, a genuinely joint multi-profile theorem, a signed cross-height controller surviving the WI-005/WI-118 screening configuration, or rigorously justified wider support/higher-order arithmetic.