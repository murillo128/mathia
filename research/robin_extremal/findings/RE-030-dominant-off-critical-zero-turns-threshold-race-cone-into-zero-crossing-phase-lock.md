# RE-030 — a dominant off-critical zero turns the threshold race cone into a zero-crossing phase lock

**Status:** `EXACT-DERIVED + SPECTRAL-MODE-CONTROL + CONDITIONAL-DOMINANT-ZERO + NEGATIVE/OBSTRUCTION + THRESHOLD-SELECTOR-PHASE-LOCK + PRIOR-ART-ALIGNED`. `RE-029` shows that hypothetical RH failure forces threshold-tangent CA parameters `Z` at which the normalized Chebyshev error is negative at the prescribed threshold scale while the normalized logarithmic Mertens-product error is positive at least at the complementary scale. A natural possible continuation is to hope that the standard/reciprocal zero coefficients themselves make this opposite-sign cone incompatible with an off-critical zeta zero. They do not.

For one off-critical conjugate zero pair
\[
\rho=\beta+i\gamma,\qquad \frac12<\beta<1,\qquad \gamma>0,
\]
the standard Chebyshev mode and the reciprocal Mertens mode are phase-shifted just enough that the `RE-029` cone is realized near one of the two zero crossings of the standard mode. More precisely, set
\[
a:=\beta-\frac12>0
\]
and define the normalized leading pair modes
\[
\Theta_\rho(x):=
-2x^a\Re\frac{x^{i\gamma}}{\rho},
\qquad
L_\rho(x):=
-2x^a\Re\frac{x^{i\gamma}}{\rho-1}.
\tag{1}
\]
The coefficient `1/rho` for a standard error and `1/(rho-1)` for a reciprocal error is classical explicit-formula structure; Bhattacharya--Martin--Simpson make this comparison explicit on RH. The exact `RE-014` tail transform gives the same `rho -> rho-1` response for an individual off-critical Chebyshev source mode, so no RH assumption is needed for the model calculation below.

Fix
\[
1-\beta<b<\frac12,\qquad c>0,
\]
and put
\[
d:=\frac12-b,\qquad
\delta:=a-d=\beta+b-1>0.
\tag{2}
\]
Then there is an unbounded sequence `x_k` on which
\[
\boxed{
\Theta_\rho(x_k)
=
-bc\,x_k^d\log x_k
}
\tag{3}
\]
while simultaneously
\[
\boxed{
L_\rho(x_k)
=
\left(
\frac{2\gamma}{|\rho|\,|\rho-1|^2}
+o(1)
\right)x_k^a>0.
}
\tag{4}
\]
Consequently
\[
\boxed{
\frac{L_\rho(x_k)}
{(1-b)c\,x_k^d\log x_k}
\longrightarrow+\infty,
\qquad
\frac{L_\rho(x_k)}{-\Theta_\rho(x_k)}
\longrightarrow+\infty.
}
\tag{5}
\]
Thus a single off-critical mode does not merely permit the standard-error cone required by `RE-029`; it lies asymptotically **deep inside** its reciprocal-positive side.

The cost is a sharp logarithmic phase condition. If
\[
\alpha:=\arg\rho\in(0,\pi/2),
\]
then the sequence in (3)--(4) satisfies
\[
\boxed{
\gamma\log x_k-\alpha
=
\frac{3\pi}{2}+2\pi k
+
\left(\frac{bc|\rho|}{2}+o(1)\right)
x_k^{-\delta}\log x_k.
}
\tag{6}
\]
The `RE-029` source cone therefore becomes, in a one-dominant-zero regime, a **zero-crossing phase-locking requirement** on the CA-selected event parameters. The unresolved arithmetic issue is not an incompatibility between the two zero coefficients; it is whether the threshold-tangent CA selector can hit the reciprocal-positive Chebyshev zero-crossing branch at the shrinking phase accuracy in (6) infinitely often.

## 1. The exact Mertens tail rotates one Chebyshev zero mode from `1/rho` to `1/(rho-1)`

`RE-014` writes the endpoint-subtracted Mertens remainder for real input as
\[
\mathcal M_*(x)
=
\int_x^\infty
\left[
\Delta(t)h'(t)-(h(t)-k(t))
\right]dt,
\tag{7}
\]
where
\[
\Delta(t)=\vartheta(t)-t,\qquad
h(t)=\frac{-\log(1-t^{-1})}{\log t},
\qquad
k(t)=\frac1{t\log t},
\]
and `RE-008` gives
\[
E(x)=\Delta(x)h(x)+\mathcal M_*(x).
\tag{8}
\]
The term `h-k` is source-independent. To measure the linear response to one complex Chebyshev source atom, insert
\[
\Delta_\rho^{\mathbb C}(t):=-\frac{t^\rho}{\rho}.
\tag{9}
\]
The source-dependent part of (8) is then exactly
\[
\begin{aligned}
E_\rho^{\mathbb C}(x)
&=
\Delta_\rho^{\mathbb C}(x)h(x)
+
\int_x^\infty
\Delta_\rho^{\mathbb C}(t)h'(t)\,dt\\
&=
-\int_x^\infty
\left(\Delta_\rho^{\mathbb C}\right)'(t)h(t)\,dt\\
&=
\int_x^\infty t^{\rho-1}h(t)\,dt.
\end{aligned}
\tag{10}
\]
Here the boundary term at infinity vanishes because `Re(rho)<1` and `h(t)=O((t log t)^(-1))`.

Since
\[
h(t)
=
\frac1{t\log t}
+
O\!\left(\frac1{t^2\log t}\right),
\tag{11}
\]
one integration by parts after the substitution `u=log t` gives
\[
\boxed{
E_\rho^{\mathbb C}(x)
=
-\frac{x^{\rho-1}}{(\rho-1)\log x}
+
O_\rho\!\left(
\frac{x^{\beta-1}}{(\log x)^2}
\right).
}
\tag{12}
\]
Adding the conjugate mode and multiplying by the reciprocal normalization `sqrt(x) log x` gives
\[
\boxed{
\sqrt x\log x\,E_\rho(x)
=
L_\rho(x)
+
O_\rho\!\left(\frac{x^a}{\log x}\right),
}
\tag{13}
\]
with `L_rho` as in (1).

Equation (12) is the local source-response version of the standard/reciprocal coefficient shift already present in the explicit-formula literature. It is included here to make the off-critical model independent of applying an RH-only normalized formula outside its hypotheses. No novelty is claimed for the coefficient `1/(rho-1)` itself.

## 2. One standard zero crossing has the reciprocal sign required by `RE-029`

Write
\[
\rho=|\rho|e^{i\alpha}.
\tag{14}
\]
The standard mode in (1) becomes
\[
\Theta_\rho(x)
=
-\frac{2x^a}{|\rho|}
\cos(\gamma\log x-\alpha).
\tag{15}
\]
Its zero crossings occur at
\[
\gamma\log x-\alpha
=
\frac\pi2+\pi m.
\tag{16}
\]

Consider the branch
\[
\gamma\log x-\alpha
=
\frac{3\pi}{2}+2\pi k.
\tag{17}
\]
At an exact crossing, a direct calculation gives
\[
\Re\left(
\frac{e^{i(\alpha+3\pi/2)}}{\rho-1}
\right)
=
-\frac{\gamma}{|\rho|\,|\rho-1|^2}.
\tag{18}
\]
Therefore
\[
\boxed{
L_\rho(x)
=
\frac{2\gamma}{|\rho|\,|\rho-1|^2}x^a
>0
}
\tag{19}
\]
on this branch. At the alternating branch `pi/2+2 pi k`, the sign is negative. Hence the reciprocal-positive half of the `RE-029` cone selects the `3pi/2` branch if one pair dominates.

This sign check is load-bearing. The result is not the vague statement that standard and reciprocal races have different phases; the relevant branch is fixed by the sign forced by the threshold-tangent Robin witness.

## 3. The `RE-029` Chebyshev scale forces polynomially shrinking phase error

Let
\[
x_k^{(0)}
:=
\exp\left(
\frac{\alpha+3\pi/2+2\pi k}{\gamma}
\right)
\tag{20}
\]
be the positive-reciprocal zero crossings. Seek a nearby point
\[
x=x_k^{(0)}e^{t/\gamma},
\qquad t=o(1).
\tag{21}
\]
Then (15) gives exactly
\[
\Theta_\rho(x)
=
-\frac{2x^a}{|\rho|}\sin t.
\tag{22}
\]
To impose the threshold scale in (3), `t` must solve
\[
\sin t
=
\frac{bc|\rho|}{2}
x^{-\delta}\log x.
\tag{23}
\]
Because `delta>0`, the right-hand side tends to zero. For every sufficiently large `k` there is a unique small positive solution near the crossing, and
\[
\boxed{
t
=
\left(\frac{bc|\rho|}{2}+o(1)\right)
x^{-\delta}\log x.
}
\tag{24}
\]
Equations (21) and (24) prove the phase law (6).

The reciprocal mode varies smoothly with `t`, so (18)--(19) give
\[
L_\rho(x_k)
=
\left(
\frac{2\gamma}{|\rho|\,|\rho-1|^2}+o(1)
\right)x_k^a,
\]
which is (4). Since
\[
a-d=\delta>0,
\]
division by either threshold-scale quantity proves (5).

Thus the standard coordinate can be tuned down from its natural off-critical scale `x^a` to the much smaller `x^d log x` scale required by `RE-029` while the reciprocal coordinate remains at full off-critical power scale and positive. There is no coefficient-level contradiction to exploit.

## 4. Conditional implication for an actual dominant-zero regime

The pure-mode calculation is a matched spectral control, not a theorem that the zeta errors are eventually governed by one zero. To state exactly what would follow under such a regime, suppose an actual threshold-selected sequence `Z_j` from `RE-029` and one pair `rho, conjugate(rho)` satisfy, with the same `a,d,delta`,
\[
\mathcal E_\vartheta(Z_j)
=
\Theta_\rho(Z_j)
+
o(Z_j^d\log Z_j),
\tag{25}
\]
and
\[
\mathcal E_{\pi_\ell}(Z_j)
=
L_\rho(Z_j)
+
o(Z_j^a).
\tag{26}
\]
These are explicit **spectral-dominance hypotheses** at the two resolutions needed by the argument; they are not asserted unconditionally and are stronger than merely saying that `rho` has maximal real part.

`RE-029` gives on the same selected points
\[
\mathcal E_\vartheta(Z_j)
=
-(bc_b+o(1))Z_j^d\log Z_j
\tag{27}
\]
and
\[
\mathcal E_{\pi_\ell}(Z_j)
\ge
((1-b)c_b+o(1))Z_j^d\log Z_j.
\tag{28}
\]
Under (25), equation (27) puts the phase within `O(Z_j^(-delta) log Z_j)` of one of the two standard zero-crossing branches. Under (26), the positive lower bound (28) eliminates the reciprocal-negative `pi/2` branch. Therefore
\[
\boxed{
\gamma\log Z_j-\alpha
=
\frac{3\pi}{2}+2\pi m_j
+
\left(\frac{bc_b|\rho|}{2}+o(1)\right)
Z_j^{-\delta}\log Z_j.
}
\tag{29}
\]
Moreover,
\[
\boxed{
\mathcal E_{\pi_\ell}(Z_j)
=
\left(
\frac{2\gamma}{|\rho|\,|\rho-1|^2}
+o(1)
\right)Z_j^a,
}
\tag{30}
\]
so its ratio to the lower bound in (28) diverges.

This is a useful diagnostic boundary. If a future argument assumes or derives one-zero dominance and then tries to contradict `RE-029` only from the algebraic relation between standard and reciprocal explicit-formula coefficients, it cannot work: under precisely that simplification the cone has an explicit compatible phase realization. A contradiction would have to come from the CA selector refusing the phase lock (29), from multi-frequency interference that destroys the one-mode picture, or from additional event-ladder information not contained in the two error coordinates.

## 5. Prior-art and novelty boundary

Bhattacharya--Martin--Simpson are direct prior art for the standard/reciprocal coefficient comparison: their normalized RH formulas use `1/rho` for standard errors and `1/(rho-1)` for reciprocal errors, and their Remark 4.6 explains how the closeness but inequality of those coefficients produces high but imperfect correlation. Their Theorem 1.6, already used in `RE-009`, also shows why global one-sided control of the mixed difference is not a weaker route.

The wider Mertens-error literature likewise derives zero sums with `rho(rho-1)` kernels after averaging or tail integration. A targeted current search found no CA threshold-tangent use of those phase relations that yields (6) or (29). No novelty is claimed for explicit formulas, the coefficient rotation, or one-zero trigonometry. The repository-level delta is narrower: **when the exact `RE-029` threshold exponent is imposed, a one-zero source model converts the apparent opposite-sign race obstruction into a quantitatively shrinking CA-selector phase-lock, and simultaneously shows that the reciprocal lower bound becomes non-coercive.**

No new source anchor is required. The load-bearing literature boundary is already recorded in `SOURCES.md`; equation (12) is also derived directly from the line's exact tail identity rather than imported from a new theorem.

## 6. Falsification boundaries and research consequence

Several limitations are essential. The construction in Sections 1--3 is a spectral source-mode control, not an admissible prime sequence, not a CA event measure, and not evidence that RH is false. It preserves exactly the zero-mode coefficient relationship relevant to a proposed source-correlation contradiction and nothing more.

The conditional statement in Section 4 does not follow merely from the existence of an off-critical zero or even from attainment of `Theta`. Other zeros with comparable real part can interfere at the threshold resolution `Z^d log Z`; if `Theta` is not isolated, if several phases contribute, or if the needed remainders in (25)--(26) are not small, the one-mode phase law need not describe the actual selected sequence.

Conversely, (29) is not yet an impossibly narrow set for CA events. Its phase width shrinks polynomially, but in the original `Z` coordinate the corresponding displacement can still be much larger than an individual prime-layer event spacing. No sparsity contradiction is claimed.

The useful narrowing is therefore strategic. `RE-029` should not be pursued as though the sign cone itself were surprising from the explicit-formula viewpoint. In the simplest off-critical spectral control, the cone is the expected geometry near one reciprocal-positive zero crossing. The genuinely new source-side target is to prove that the **threshold-tangent CA event selector cannot phase-lock to those crossings with the accuracy forced by `delta=beta+b-1>0`**, or to show that unavoidable multi-zero interference makes such simultaneous locking impossible. That is a stricter and more falsifiable target than seeking a generic inequality between the Chebyshev and Mertens errors.
