# WI-161 — prefix subtraction restores the split dyadic BGSTB spike error

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

This finding replaces and corrects withdrawn WI-160. WI-160 correctly identified that the current author correction to Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB) contains a stronger **prefix** estimate than the deliberately degraded displayed Montgomery theorem, but it incorrectly concluded that the same split first-term error was unavailable for the dyadic sum `T < gamma,gamma' <= 2T`.

Keeping the first line of corrected equation (3.5) at heights `2T` and `T` before subtracting the prefixes gives the same split error for the dyadic form factor. The cross-boundary term already bounded in the authors' dyadic proof is only `O(T)` uniformly for `1 <= x <= T`, so it is absorbed by the existing `O(T sqrt(log T))` bulk error. Consequently the stronger dyadic estimate is

\[
\boxed{
\mathcal F_{(T,2T]}(x)
=
\frac{T}{2\pi x^2}\bigl((\log T)^2+O(\log T)\bigr)
+
\frac{T}{2\pi}\log x
+O\!\bigl(T\sqrt{\log T}\bigr)
}
\qquad (1\le x\le T).
\]

After normalization this restores exactly the changing-test norm gate used in WI-157 on the dyadic window. No new zero proportion follows, but a source-level obstacle recorded in WI-160 disappears.

## 1. Corrected prefix input

Let

\[
L:=\log T,
\qquad c:=\log 2.
\]

In `arXiv:2501.14545v3`, Section 3, the authors correct the proof of their earlier unconditional Montgomery theorem. Before deliberately degrading the first error term, their equation (3.5) proves, for a prefix of arbitrary height `U`,

\[
\mathcal F_{(0,U]}(x)
=
\frac{U}{2\pi x^2}
\bigl((\log U)^2+O(\log U)\bigr)
+
\frac{U}{2\pi}\log x
+O\!\bigl(U\sqrt{\log U}\bigr),
\tag{1}
\]

uniformly for `1 <= x <= U`.

The first error in (1) comes from the elementary `M_1` calculation and is genuinely `O(U log U/x^2)`. The authors then replace it by the weaker relative `O((log U)^-1/2)` form only to simplify subsequent fixed-test applications.

## 2. Retaining the first line through dyadic subtraction

The dyadic proof in the same section starts from

\[
\mathcal F_{(T,2T]}(x)
=
\mathcal F_{(0,2T]}(x)
-
\mathcal F_{(0,T]}(x)
+O(E_1(x,T)),
\tag{2}
\]

where the cross-boundary contribution `E_1` is estimated in the paper using the zero-free region. Their argument gives uniformly for `1 <= x <= T`

\[
E_1(x,T)\ll T^{1/2}+x\ll T.
\tag{3}
\]

Apply the **first line** (1), rather than its degraded reformulation, at heights `2T` and `T`. Since `x <= T`, both applications are inside their uniform ranges. The spike terms subtract as

\[
\begin{aligned}
&\frac{2T}{2\pi x^2}
\bigl((L+c)^2+O(L)\bigr)
-
\frac{T}{2\pi x^2}
\bigl(L^2+O(L)\bigr)\\
&\qquad=
\frac{T}{2\pi x^2}
\left(2(L+c)^2-L^2+O(L)\right)\\
&\qquad=
\boxed{
\frac{T}{2\pi x^2}\bigl(L^2+O(L)\bigr)
},
\end{aligned}
\tag{4}
\]

because

\[
2(L+c)^2-L^2=L^2+4cL+2c^2=L^2+O(L).
\tag{5}
\]

The prime-side main terms subtract exactly:

\[
\frac{2T}{2\pi}\log x-
\frac{T}{2\pi}\log x
=
\frac{T}{2\pi}\log x.
\tag{6}
\]

The two bulk errors from (1) contribute `O(T sqrt L)`, and (3) is smaller. Substitution into (2) therefore proves

\[
\boxed{
\mathcal F_{(T,2T]}(x)
=
\frac{T}{2\pi x^2}\bigl(L^2+O(L)\bigr)
+
\frac{T}{2\pi}\log x
+O(T\sqrt L)
}
\tag{7}
\]

uniformly throughout `1 <= x <= T`.

The published displayed dyadic Montgomery theorem in that paper is weaker because the authors insert the already degraded second line of (3.5) into (2). Equation (7) is instead an exact consequence of the stronger first line that their corrected proof has already established.

## 3. Normalized dyadic form factor and changing-test gate

Put

\[
x=T^\alpha,
\qquad 0\le\alpha\le1,
\]

and normalize (7) by `(T/(2 pi))L`. Then

\[
\boxed{
F_T^{\mathrm{dyad}}(\alpha)
=
L e^{-2L\alpha}
+\alpha
+O(e^{-2L\alpha})
+O(L^{-1/2})
}
\tag{8}
\]

uniformly for `0 <= alpha <= 1`.

Thus for any real support-one changing test `r_L`, the two arithmetic errors pair with the deterministic bounds

\[
\left|2\int_0^1O(e^{-2L\alpha})r_L(\alpha)\,d\alpha\right|
\ll \frac{\|r_L\|_\infty}{L},
\tag{9}
\]

and

\[
\left|2\int_0^1O(L^{-1/2})r_L(\alpha)\,d\alpha\right|
\ll \frac{\|r_L\|_1}{\sqrt L}.
\tag{10}
\]

Therefore the sufficient uniformity gate from WI-157 is valid on the canonical dyadic window itself:

\[
\boxed{
\|r_L\|_\infty=o(L),
\qquad
\|r_L\|_1=o(\sqrt L)
\Longrightarrow
\text{dyadic integrated arithmetic error}=o(1).
}
\tag{11}
\]

The stronger `\|r_L\|_\infty=o(\sqrt L)` condition asserted in withdrawn WI-160 was an artifact of retaining the authors' intentionally degraded displayed dyadic error rather than propagating their sharper corrected prefix line.

## 4. Consequences and stress tests

### WI-157 is now source-correct on dyadic windows

WI-157's deweighted finite-height variational calculation needs exactly the split shape in (8). The current corrected BGSTB proof supplies it not only for the prefix but, by (2)--(7), for `T < gamma,gamma' <= 2T`. No prefix-to-dyadic uniformity gap remains at this level.

### WI-158 and WI-159 remain valid barriers

Those findings construct singular near-extremizers with `||r_L||_1 = Theta(sqrt L)` and adversarial bulk errors of size `O(L^-1/2)`. Such errors still satisfy (8). Hence restoring the split spike error does not control the singular boundary; it only removes the artificial extra dyadic `L^infty` restriction introduced in WI-160. A scalar escape beyond the regular gate still requires zeta-specific information on the bulk error, or a different architecture.

### The cross-boundary term cannot recreate the spike loss

The only additional term in passing from prefix subtraction to the actual dyadic pair sum is `E_1`. The source proves `E_1 << T` uniformly for `1 <= x <= T`, including the whole small-`x` regime. After normalization this is `O(1/L)`, so it belongs to the bulk error and cannot generate an `O(sqrt L e^{-2L alpha})` spike.

### No new proportion is claimed

Equation (7) repairs an arithmetic-interface provenance issue. It does not provide the frequency-sensitive cancellation needed at the `||r_L||_1 asymp sqrt L` boundary, does not validate any retracted higher-moment claim, and does not improve the established simple-critical-zero proportion by itself.

## 5. Prior-art and novelty audit

Primary source: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, arXiv:2501.14545v3, revised 1 Sep 2026, especially equations (3.5) and the dyadic proof immediately following it. The correction of the 2024 theorem is entirely theirs. The paper states the degraded dyadic estimate; it does not state (7) in the sharper split form.

Contemporary independent context: Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, 2 Sep 2026, explicitly distinguishes fixed-test pair-correlation input from the extra uniformity needed for `T`-dependent tests.

A targeted search around the corrected equation (3.5), dyadic prefix subtraction, and split first-term errors did not locate a published statement of (7). This absence is not used as a priority claim. The Mathia contribution recorded here is the elementary but load-bearing observation that the corrected first-line prefix estimate survives the authors' own dyadic subtraction with its `O(L)` spike coefficient intact.

## Evidence boundary

Equation (1), the dyadic decomposition (2), and the cross-boundary estimate (3) are literature-backed by `arXiv:2501.14545v3`. Equations (4)--(11) are exact algebraic/analytic consequences. The result materially reverses the dyadic-error conclusion of withdrawn WI-160, which is why it receives a new stable finding ID rather than silently repurposing that claim.