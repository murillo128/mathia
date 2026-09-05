# XF-046 — source counting makes remote memory-scale forcing little-o at the critical R^-2 scale

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC-REFINEMENT` + `STRUCTURAL/THRESHOLD`. XF-045 showed that after centering the exact far-tail gap velocity and retaining its positive diagonal sink, a memory-scale core separated from the remote zeros by a physical buffer `D=R(T) log T` has a normalized remote forcing floor `O(R(T)^-2)`. That landed exactly at, but not below, the slow-mode triple-flux threshold isolated in XF-044.

The `O(R^-2)` bound is still not sharp for the actual Xi source package. On the full memory scale, Rodgers--Tao supply two additional pieces of information that XF-045 did not use in its final estimate: the core mean gap is asymptotic to the source spacing, and the global zero-counting discrepancy is only `O(log^2 T)`. If the far-tail field is compared with the smooth source density **before** its oscillation across the core is estimated, the counting discrepancy pays one extra spatial derivative of the inverse-square kernel. The result is

\[
\boxed{
\operatorname{osc}_{i\in I}
\bigl(E_i-\bar g_I W_i\bigr)
=o\!\left(\frac{S_I}{D^2}\right)
}
\tag{1}
\]

for a full memory-scale core `N asymp log^2 T`, `N<=log^2 T`, with source-scale upper gap envelope and a super-mesoscopic cutoff `D=R(T)log T`, `R(T)->infinity`, `D=o(T)`. Here `E_i` and `W_i` are the exact endpoint and positive tail-mass fields of XF-045, and `S_I=N\bar g_I` is the core span.

Consequently the exact remote contribution to the centered shape energy satisfies

\[
\boxed{
\mathcal R_{\rm far}
\le
 o\!\left(
 \frac{r_I\sqrt N\,S_I}{D^2}
 \right),
}
\tag{2}
\]

and the normalized stationary floor improves from XF-045's borderline estimate to

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
=o\!\left(
\left(\frac{Ns_T}{D}\right)^2
\right)
=o(R(T)^{-2}).
}
\tag{3}
\]

Thus the genuinely remote tail is not merely of the same power as the positive triple-flux gate: **the established Xi counting laws already push it into the required little-`o` regime.** The remaining precision obstruction is entirely local to the near buffer (together with the independent need to propagate the core upper envelope in time).

## 1. Setup and the exact centered far-tail decomposition

Work in the hypothetical real-simple regime `Lambda<t<=0`, at height `T->infinity`. Let

\[
I=\{a,\ldots,a+N-1\},
\qquad
\bar g=\frac1N\sum_{i\in I}g_i,
\qquad
\nu_i=g_i-\bar g,
\qquad
r_I^2=\sum_{i\in I}\nu_i^2,
\tag{4}
\]

and write

\[
S_I=x_{a+N}-x_a=N\bar g.
\tag{5}
\]

Assume

\[
N\asymp\log^2T,
\qquad N\le\log^2T,
\qquad
0<g_i\le b_*\le C s_T
\quad(i\in I),
\tag{6}
\]

where

\[
s_T:=\frac{4\pi}{\log T}.
\tag{7}
\]

Choose the fixed far-tail cutoffs of XF-045 at physical distance at least

\[
D=R(T)\log T,
\qquad R(T)\to\infty,
\qquad D=o(T)
\tag{8}
\]

from the core. For the right tail, XF-045 gives exactly

\[
A_i^+=E_i^+-g_iW_i^+,
\tag{9}
\]

where, if the first far gap is indexed by `K`,

\[
E_i^+=\frac1{x_K-x_i},
\qquad
W_i^+=\sum_{\ell\ge K+1}
\frac1{(x_\ell-x_i)(x_\ell-x_{i+1})}>0.
\tag{10}
\]

The left tail has the analogous representation. With `E_i=E_i^++E_i^-` and `W_i=W_i^++W_i^-`, the centered shape-energy contribution is

\[
\boxed{
\mathcal R_{\rm far}
=2\sum_{i\in I}\nu_i(E_i-\bar gW_i)
-2\sum_{i\in I}W_i\nu_i^2.
}
\tag{11}
\]

The second term is favorable. Since `sum_i nu_i=0`, only the oscillation of

\[
C_i:=E_i-\bar gW_i
\tag{12}
\]

can feed shape. XF-045 bounded that oscillation by `O(S_I/D^2)`. The purpose of this finding is to use the actual source density to gain little-`o` over that estimate.

## 2. The full memory core has the correct source mean spacing

Rodgers--Tao's Corollary 3.3 gives, uniformly in the real-rooted regime,

\[
x_k(t)-x_j(t)
=
\frac{4\pi(k-j)}{\log\xi_j}
+o_{j\to\infty}(\log\xi_j)
\tag{13}
\]

whenever

\[
1\le j<k\le j+\log^2\xi_j.
\tag{14}
\]

For a core satisfying (6), `x_a asymp T` and `N asymp log^2 T`; therefore (13) gives

\[
S_I
=N s_T(1+o(1)),
\qquad
\boxed{\bar g=s_T(1+o(1)).}
\tag{15}
\]

The same source statement with `k=j+1` gives the deliberately coarse but useful individual bound

\[
\boxed{g_j=o(\log T)}
\tag{16}
\]

for every gap whose endpoints remain at height comparable with `T`. In particular the single cutoff gap between `x_K` and `x_{K+1}` is `o(log T)`. This fact is far weaker than a source-scale pointwise gap bound, but because `D/log T->infinity` it is already enough to make the cutoff phase error lower order after centering.

Equation (15) is the first source-specific gain over XF-045. It allows `\bar g W_i` to be compared with the smooth density scale `s_T W_i` with only a relative `o(1)` error.

## 3. Weighted global counting gains one derivative after taking core oscillation

Consider the right tail and put

\[
u:=x_{K+1},
\qquad
f_i(y):=\frac1{(y-x_i)(y-x_{i+1})}
\qquad(y\ge u).
\tag{17}
\]

Thus `W_i^+=sum_{x_ell>=u} f_i(x_ell)` up to an irrelevant endpoint convention. If `i,j in I`, the two kernels see source points whose coordinates differ by at most `S_I`. Because every tail point is at distance `gtrsim D` from the core, the mean-value theorem gives

\[
|f_i(y)-f_j(y)|
\ll
\frac{S_I}{(D+y-u)^3},
\tag{18}
\]

and

\[
|\partial_y(f_i-f_j)(y)|
\ll
\frac{S_I}{(D+y-u)^4}.
\tag{19}
\]

Rodgers--Tao's global Riemann--von Mangoldt law is

\[
N_t([0,Y])=\Psi(Y)+O(\log^2Y),
\qquad
\Psi(Y):=\frac{Y}{4\pi}\log\frac{Y}{4\pi}-\frac{Y}{4\pi},
\qquad
\Psi'(Y)=\frac1{4\pi}\log\frac{Y}{4\pi}.
\tag{20}
\]

Apply Stieltjes summation to the **difference kernel** `f_i-f_j`, not to `f_i` and `f_j` separately. Equations (18)--(20) give

\[
\begin{aligned}
&(W_i^+-W_j^+)
-
\int_u^\infty(f_i-f_j)(y)\Psi'(y)\,dy\\
&\qquad
=O\!\left(\frac{S_I\log^2T}{D^3}\right)
+o\!\left(\frac{S_I\log T}{D^2}\right),
\end{aligned}
\tag{21}
\]

where the second term covers the remote `y`-range outside height comparable with `T`; its contribution is smaller because `D=o(T)` and the kernel difference decays cubically. The important feature is the power `D^-3`: the `O(log^2 T)` counting discrepancy is multiplied by the **oscillation kernel**, which has already gained one derivative relative to the raw `D^-2` tail kernel.

Multiplying (21) by `s_T` yields

\[
\boxed{
 s_T\operatorname{osc}_I
 \left(
 W^+-\int_u^\infty f_i(y)\Psi'(y)\,dy
 \right)
\ll
\frac{S_I\log T}{D^3}
+o\!\left(\frac{S_I}{D^2}\right)
=o\!\left(\frac{S_I}{D^2}\right),
}
\tag{22}
\]

because `D/(log T)=R(T)->infinity`.

This is the second source-specific gain. The global counting error was only sufficient for an `O(1/R)` relative density statement in XF-020, but after centering has removed the constant mode its contribution to the shape field receives another factor `core span / D`.

## 4. The smooth source density agrees with the endpoint field to little-o oscillation

Write

\[
I_i:=\int_u^\infty f_i(y)\,dy
=\frac1{g_i}
\log\frac{u-x_i}{u-x_{i+1}}.
\tag{23}
\]

First replace the slowly varying source density in (21) by the constant density `1/s_T`. With `s_T=4\pi/\log T` and the corrected source density in (20), the mismatch is exactly

\[
 s_T\Psi'(y)-1
=\frac{\log(y/T)-\log(4\pi)}{\log T}.
\tag{24}
\]

Hence on the comparable-height range `u<=y<=2T`,

\[
|s_T\Psi'(y)-1|
\ll
\frac1{\log T}
+
\frac{|y-T|}{T\log T}.
\]

For `i,j\in I`, integrating (18) gives

\[
\int_u^\infty |f_i-f_j|(y)\,dy
\ll
\frac{S_I}{D^2}.
\]

The constant `O(1/\log T)` density mismatch therefore contributes explicitly

\[
O\!\left(\frac1{\log T}
\int_u^\infty |f_i-f_j|(y)\,dy\right)
=O\!\left(\frac{S_I}{D^2\log T}\right)
=o\!\left(\frac{S_I}{D^2}\right).
\]

On the comparable-height range the `|y-T|/(T\log T)` part is likewise `O(1/\log T)` against the same integrable difference kernel, while beyond `2T` the cubic decay from (18) controls the remaining tail with room to spare. Thus

\[
\boxed{
\operatorname{osc}_I
\left(
 s_T\int_u^\infty f_i(y)\Psi'(y)\,dy-I_i
\right)
=o\!\left(\frac{S_I}{D^2}\right).
}
\tag{25}
\]

It remains to compare the constant-density integral with the exact endpoint `E_i^+`. Let

\[
G:=x_{K+1}-x_K.
\tag{26}
\]

By (16), `G=o(log T)=o(D)`. If `p_i=u-x_i`, then

\[
I_i
=\frac1{p_i}+O\!\left(\frac{g_i}{D^2}\right),
\qquad
E_i^+
=\frac1{p_i-G}.
\tag{27}
\]

The large-looking boundary phase `G/D^2` is essentially constant across the core and therefore disappears from the centered shape. More precisely,

\[
\operatorname{osc}_I
\left(E_i^+-\frac1{p_i}\right)
\ll
\frac{G S_I}{D^3},
\tag{28}
\]

while (6) gives

\[
\operatorname{osc}_I
\left(I_i-\frac1{p_i}\right)
\ll
\frac{b_*}{D^2}
+\frac{b_*S_I}{D^3}.
\tag{29}
\]

Since `G=o(log T)`, `b_*=O(s_T)`, `S_I asymp log T`, and `D=R log T`, equations (28)--(29) imply

\[
\boxed{
\operatorname{osc}_I(E^+-I)
=o\!\left(\frac{S_I}{D^2}\right).
}
\tag{30}
\]

Combining (22), (25), and (30) yields

\[
\boxed{
\operatorname{osc}_I(E^+-s_TW^+)
=o\!\left(\frac{S_I}{D^2}\right).
}
\tag{31}
\]

The left tail is identical after reflection; the part passing through bounded height is even farther from a high positive core and contributes below the displayed scale. Hence

\[
\boxed{
\operatorname{osc}_I(E-s_TW)
=o\!\left(\frac{S_I}{D^2}\right).
}
\tag{32}
\]

## 5. Replacing the source spacing by the evolving core mean costs only o(1)

From (12), add and subtract `s_TW_i`:

\[
C_i
=(E_i-s_TW_i)
+(s_T-\bar g)W_i.
\tag{33}
\]

The same difference-kernel estimate used above, now without subtracting the smooth main term, gives

\[
 s_T\operatorname{osc}_I W
=O\!\left(\frac{S_I}{D^2}\right).
\tag{34}
\]

Equation (15) therefore implies

\[
|s_T-\bar g|\operatorname{osc}_I W
=o\!\left(\frac{S_I}{D^2}\right).
\tag{35}
\]

Together with (32), this proves the central estimate (1):

\[
\boxed{
\operatorname{osc}_I C
=o\!\left(\frac{S_I}{D^2}\right).
}
\tag{36}
\]

This is precisely where both Rodgers--Tao scales are needed. The global `O(log^2 T)` counting error controls the weighted remote measure after one derivative is gained, while the bounded-`alpha`/macroscopic spacing result makes the core mean agree with `s_T` to relative `o(1)` at the `N asymp log^2 T` memory scale.

## 6. The remote forcing floor is now below the XF-044/XF-035 threshold

Insert (36) into the exact energy decomposition (11). Dropping the favorable sink and using Cauchy--Schwarz gives

\[
\boxed{
\mathcal R_{\rm far}
\le
 o\!\left(
 \frac{r_I\sqrt N\,S_I}{D^2}
 \right),
}
\tag{37}
\]

which is (2). Combining this with the finite-window coercivity of XF-042 yields

\[
D^+r_I
\le
-\lambda_I r_I
+F_I^{\rm near}
+o\!\left(\frac{\sqrt N\,S_I}{D^2}\right),
\qquad
\lambda_I=\frac{2N}{b_*^2(N-1)^2}.
\tag{38}
\]

Normalize by

\[
A_I=\frac{r_I}{s_T\sqrt N}.
\tag{39}
\]

If the near forcing is suppressed, the stationary scale contributed by the remote tail is bounded by

\[
A_{I,{\rm far}\text{-}{\rm floor}}
=o\!\left(
\frac{S_I}{s_TD^2\lambda_I}
\right).
\tag{40}
\]

Using `S_I=N s_T(1+o(1))`, `b_*<=Cs_T`, and the formula for `lambda_I`,

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
=o\!\left(
\frac{N^2s_T^2}{D^2}
\right)
=o\!\left(
\left(\frac{S_I}{D}\right)^2
\right).
}
\tag{41}
\]

At the memory scale `S_I asymp log T` and `D=R(T)log T`, this is exactly

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
=o(R(T)^{-2}).
}
\tag{42}
\]

XF-044 showed that a memory-wavelength slow mode repeated across the `M=R(T)log^2T` source buffer reaches the borderline triple-flux scale at amplitude `Theta(R^-2)`, while the positive XF-035 gate asks for little-`o(R^-2)`. Equation (42) therefore crosses the power-and-little-`o` precision barrier for the genuinely remote tail. No additional logarithmic Cauchy relaxation time is needed to suppress that component.

## 7. Stress tests and hard boundary

The improvement is **source-specific**. If one discards Rodgers--Tao's counting law and only assumes the core upper envelope, the comparison of `W_i` with the smooth density is unavailable and XF-045's `O(S_I/D^2)` oscillation bound is the correct safe statement. Generic ordered logarithmic-repulsion systems need not inherit (36).

The result is also restricted to the full memory scale where (15) follows from the source macroscopic spacing law with a relative `o(1)` error. It is not asserted for an arbitrary short block `N=o(log^2T)`: dividing the `o(log T)` source span error by a much shorter core could lose the relative mean-gap control used in (35).

The upper envelope `g_i<=Cs_T` on the core remains substantive. It is needed both for the nonlinear Cauchy coercivity and for the integral-to-endpoint estimate (29). No lower core-gap bound and no pointwise remote-gap bound are used. In particular, the remote zeros may contain very irregular individual gaps; their aggregate effect enters through the source counting discrepancy.

Equation (42) does **not** control `F_I^{near}`. Zeros inside the super-mesoscopic buffer are not separated from the core by `D`, so the difference-kernel derivative gain cannot simply be applied to them at the critical scale. Nor does the result propagate the upper envelope through a backward-time interval. Those are now the two explicit source-facing burdens.

Finally, this is not an upper bound for `Lambda` and does not assert that the actual Xi flow realizes the XF-044 slow mode. It removes the genuinely remote part of one candidate obstruction under the hypothetical real-simple dynamics; the contradiction mechanism still needs a near-buffer organization strong enough to transmit the new little-`o` precision to the local triple-flux gate.

## 8. Prior-art and novelty boundary

Stieltjes/partial summation against a counting function and the gain obtained by applying a mean-zero or difference kernel to a distant field are classical analytic devices. No novelty is claimed for either principle in isolation. A targeted search around weighted Riemann--von Mangoldt sums, far-field Cauchy kernels, and nonlocal mean-zero localization did not identify an external theorem that directly states the source-specific estimate (36); absence from that search is not used as evidence of novelty.

Rodgers and Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, are the load-bearing external source for both (13) and (20). Their published/corrected treatment also emphasizes that boundary contributions in the energy argument require explicit control. The paper is already anchored in `research/xi_flow/SOURCES.md`, and no additional external theorem is used here, so `SOURCES.md` is unchanged.

The Mathia-local content is the combination of their two counting scales with the exact endpoint-minus-sink decomposition of XF-045: taking the **core oscillation before estimating the counting discrepancy** converts the global `O(log^2T)` error into a `D^-3` term, while the memory-scale source law replaces the evolving core mean by `s_T` at relative `o(1)` cost. That combination is what upgrades the remote floor from `O(R^-2)` to `o(R^-2)`.

## 9. Consequence for `xi_flow`

The remote-tail precision branch is now closed at the threshold required by the current triple-flux program: source counting plus exact centered gap algebra already make genuinely remote memory-scale replenishment `o(R^-2)`. Further work should not spend effort extracting another power from the infinite tail.

The highest-value continuation is the **near buffer**. One now needs either a nested centering / summation-by-parts mechanism that converts the interactions inside the `R(T)log T` buffer into the same source-density cancellation, or a source-specific argument showing that the near-buffer memory-scale projection is already `o(R^-2)`. The accepted overlap-discriminant clue remains relevant to that local problem, but XF-046 does not resolve it.