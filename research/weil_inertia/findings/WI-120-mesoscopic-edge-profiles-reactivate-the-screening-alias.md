# WI-120 — mesoscopic edge profiles reactivate a finite-block support-one alias

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It sharpens the falsification boundary of WI-118/WI-119: the fixed-test support-one screening obstruction is not uniform over test families that move toward the support edge on the reciprocal block scale. Using only the published unconditional Montgomery form-factor theorem, one can choose a smooth nonnegative profile whose Fourier support stays strictly inside `[-1,1]` for every `T`, but lies within `Theta(1/M)` of the endpoints. On an `M`-site WI critical screening block, this profile distinguishes an off-line mirror-pair block from an on-line-double block by `Theta(M^2)`, and the exact Montgomery weight preserves that leading term whenever `M -> infinity` and `M=o(log T)`.

The arithmetic side is genuinely available: Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh prove their unconditional form factor uniformly for every `0<=alpha<=1`. Their exact transform identity therefore evaluates these `T`-dependent edge profiles with an error controlled by their bounded `L^1` norm, even though their derivatives grow with `M`. The unresolved step is extraction, not evaluation. The resulting real-axis kernel changes sign, so the known total all-pairs quadratic form does not by itself lower-bound the positive contribution of a selected screening block; external cross-height terms may cancel it. Thus this is a precise live information carrier, not yet a defect-to-zero theorem.

## 1. The uniform arithmetic interface is stronger than a fixed-test lemma

Let

\[
L:=\log T,
\qquad
\mathcal N_T:=\frac{T}{2\pi}L.
\]

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh define

\[
F_T(\alpha)
:=\mathcal N_T^{-1}
\sum_{\substack{\rho,\rho'\\0<\gamma,\gamma'\le T}}
T^{\alpha(\rho-\rho')}
 w(\rho-\rho'),
\qquad
w(u):=\frac4{4-u^2},
\tag{1}
\]

and prove unconditionally that `F_T(alpha)` is real, even and nonnegative, with

\[
\boxed{
F_T(\alpha)
=
T^{-2\alpha}(L+O(1))
+\alpha
+O(L^{-1/2})
}
\qquad(0\le\alpha\le1),
\tag{2}
\]

**uniformly in `alpha`**. Their exact Fourier identity says that for every integrable profile `r`,

\[
\sum_{\rho,\rho'}
\widehat r\!\left(
 i(\rho-\rho')\frac{L}{2\pi}
\right)
 w(\rho-\rho')
=
\mathcal N_T
\int_{\mathbb R}F_T(\alpha)r(\alpha)\,d\alpha,
\tag{3}
\]

where

\[
\widehat r(z)=\int_{\mathbb R}r(\alpha)e^{-2\pi i z\alpha}\,d\alpha.
\tag{4}
\]

Their published Lemma 5 is usually applied to a fixed profile. For the construction below it is better not to use the implicit constant of that fixed-profile corollary at all: equations (2)--(3) immediately permit a `T`-dependent family as long as its `L^1` norm stays bounded. This point is important because the edge family below has derivative norms growing like powers of `M`.

## 2. A smooth profile at distance `Theta(1/M)` from the first alias

Fix once and for all a nonzero

\[
\phi\in C_c^\infty((1/4,1/2)),
\qquad
\phi\ge0,
\tag{5}
\]

and let `M=M(T)` be any integer satisfying

\[
M\to\infty,
\qquad
M=o(L).
\tag{6}
\]

Define the even profile

\[
\boxed{
r_M(\alpha)
:=
M\,\phi\!\left(M(1-|\alpha|)\right).
}
\tag{7}
\]

For every `M`, this is a smooth real nonnegative function whose support is strictly inside `[-1,1]`:

\[
1-\frac1{2M}<|\alpha|<1-\frac1{4M}.
\tag{8}
\]

Put

\[
I_0:=\int_{1/4}^{1/2}\phi(s)\,ds,
\qquad
I_1:=\int_{1/4}^{1/2}s\phi(s)\,ds.
\tag{9}
\]

Then

\[
\|r_M\|_1=2I_0,
\qquad
r_M(0)=0.
\tag{10}
\]

Because the support in (8) lies in `|alpha|>=1/2`, the `T^{-2 alpha}` spike in (2) contributes only `O_phi(L/T)`. Integrating the uniform error in (2) against (7) gives

\[
\boxed{
\frac1{\mathcal N_T}
\sum_{\rho,\rho'}
\widehat r_M\!\left(
 i(\rho-\rho')\frac{L}{2\pi}
\right)
 w(\rho-\rho')
=
2I_0-\frac{2I_1}{M}
+O_\phi(L^{-1/2}+L/T).
}
\tag{11}
\]

Thus moving to an `O(1/M)` support-edge layer does **not** ask for support greater than one or for a new prime-correlation theorem. The unconditional form factor already evaluates the family uniformly.

## 3. The same family gives a quadratic response on an `M`-site screening block

Now isolate the deterministic WI-005/WI-006 screening geometry. At the `M` consecutive ordinates

\[
t_j=t_0+j\frac{2\pi}{L},
\qquad
0\le j<M,
\tag{12}
\]

compare two multiplicity-labelled configurations. The mirror configuration has

\[
\rho_{j,\sigma}
=\frac12+\sigma\frac yL+it_j,
\qquad
\sigma\in\{+1,-1\},
\tag{13}
\]

for fixed `y != 0`; the double configuration has two labels at `1/2+it_j`.

First omit the factor `w`. Summing the Fourier representation (4) over all ordered labelled pairs gives an exact identity. If

\[
S_M(\alpha):=\sum_{j=0}^{M-1}e^{2\pi i j\alpha},
\tag{14}
\]

then the mirror-minus-double difference is

\[
\boxed{
\Delta_M^{(0)}(y)
=
\int_{-1}^{1}
4\sinh^2(y\alpha)\,
 r_M(\alpha)\,
|S_M(\alpha)|^2\,d\alpha.
}
\tag{15}
\]

This quantity is positive because `r_M>=0`. At the positive support edge write `alpha=1-s/M`. Uniformly for `s in [1/4,1/2]`,

\[
\frac{|S_M(1-s/M)|^2}{M^2}
=
\left(
\frac{\sin(\pi s)}{M\sin(\pi s/M)}
\right)^2
\longrightarrow
\left(\frac{\sin(\pi s)}{\pi s}\right)^2.
\tag{16}
\]

The negative edge contributes identically. Dominated convergence in (15) therefore yields

\[
\boxed{
\frac{\Delta_M^{(0)}(y)}{M^2}
\longrightarrow
8\sinh^2(y)\,J_\phi,
\qquad
J_\phi
:=
\int_{1/4}^{1/2}
\phi(s)
\left(\frac{\sin(\pi s)}{\pi s}\right)^2ds
>0.
}
\tag{17}
\]

Hence the moving profile sees the canonical mirror-pair-versus-double replacement not merely at density scale `Theta(M)` but with a coherent `Theta(M^2)` response on the matched finite block.

## 4. The exact Montgomery weight does not destroy the response

Let `Delta_M^(w)(y)` denote the same restricted block difference with the exact factor `w(rho-rho')` retained. Every pair in either block satisfies

\[
|\rho-\rho'|
\ll_y \frac{M}{L}.
\tag{18}
\]

Since `M=o(L)`, eventually `|rho-rho'|<1`, and

\[
w(\rho-\rho')-1
=O_y\!\left(\frac{M^2}{L^2}\right).
\tag{19}
\]

Also, for every complex argument arising from (13), the bounded `L^1` norm in (10) gives

\[
\left|
\widehat r_M\!\left(
 i(\rho-\rho')\frac{L}{2\pi}
\right)
\right|
\ll_{\phi,y}1.
\tag{20}
\]

There are `O(M^2)` ordered pairs. Therefore

\[
\boxed{
\Delta_M^{(w)}(y)-\Delta_M^{(0)}(y)
=O_{\phi,y}\!\left(\frac{M^4}{L^2}\right)
=o(M^2),
}
\tag{21}
\]

and (17) remains valid with `Delta_M^(w)` in place of `Delta_M^(0)`.

This weighted stability is weaker than the `O(1)` comparison for the fixed tapered Tsang kernels in WI-115/WI-118, but it is exactly sufficient here because the revived edge signal is quadratic in `M`.

## 5. Why this does not contradict the fixed-test screening theorems

WI-118 and WI-119 take a fixed support-one profile/test and send the screening-block length to infinity. For any fixed smooth profile strictly inside the support boundary, the first nonzero dual-lattice alias is absent and the mirror-versus-double difference is `o(M)` (indeed `O(1)` for the Schwartz higher-correlation class).

The family (7) changes the order of limits. Its distance to the first alias is `Theta(1/M)`, exactly the Fourier resolution of an `M`-site Dirichlet/Fejer peak. Although every individual `r_M` has smooth Fourier support strictly below one, the family approaches the boundary at the same rate at which the finite screening block resolves it. Equation (17) is therefore a near-alias resonance, not an endpoint mass and not support greater than one.

This gives the precise falsification boundary:

\[
\boxed{
\text{fixed smooth support-one screening}
\;\not\Rightarrow\;
\text{uniform screening for }T\text{-dependent tests at distance }O(1/M)
\text{ from the edge}.
}
\tag{22}
\]

The same observation explains why the Lagarias--Rodgers fixed-test bandlimited mimicry results do not by themselves settle this moving-profile question. No contradiction is involved: convergence against every fixed bandlimited test need not be uniform over a family whose spectral resolution diverges with the observation scale.

## 6. The remaining obstruction is extraction, not arithmetic evaluation

Equation (11) controls the **complete** all-pairs sum. Equation (17), by contrast, is the contribution difference of one selected coherent block. Because the real-axis transform of the edge profile oscillates, cross-height terms outside that block have no fixed sign. The argument used by BGSTB/Tsang to discard unwanted pairs is therefore unavailable. WI-118 shows that restoring universal real-axis termwise positivity would force endpoint taper and return to the screened class.

The global nonnegativity `F_T(alpha)>=0` does not repair this by itself. In the Gram representation behind the unconditional theorem it gives a positive semidefinite all-pairs quadratic form, but positive semidefiniteness alone does not lower-bound a chosen principal/block contribution by the all-ones quadratic form: already

\[
A=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
\succeq0,
\qquad
(1,1)A(1,1)^*=0,
\qquad
\operatorname{tr}A=2.
\tag{23}
\]

Thus the new carrier does not yet imply that an actual zeta configuration with many off-line pairs must make the total quantity in (11) too large. A successful continuation needs a **localization/coercivity inequality** controlling the signed cross-height reservoir for this moving edge family, or a zeta-specific frame/spacing statement that makes coherent block energies sufficiently additive. Conversely, an explicit zeta-count-compatible cancellation model for every such edge family would close this escape.

## 7. Prior-art audit and evidence boundary

The literature-backed inputs are exact and classical/recent: BGSTB's published 2024 paper supplies (1)--(4), including the crucial uniformity through `alpha=1`; WI-115/WI-118 record the Tsang support-one cancellation and the sharp fixed-profile endpoint obstruction; WI-119 connects fixed higher correlations to the same alias geometry; and Lagarias--Rodgers show that all currently known **fixed** bandlimited higher vertical correlations are compatible with lattice-supported alternatives.

A targeted search also checked the modern Fourier-optimization literature around Montgomery pair correlation and mesoscopic zero statistics. No source was located that formulates the specific `1/M` moving-edge profile (7), its mirror-pair-versus-double finite-block asymptotic (17), or the weighted comparison (21). Absence of a located source is **not** evidence of priority, and no priority claim is made here.

The result is deliberately narrower than an unconditional improvement. It proves that a support-one pair observable can be simultaneously:

- strictly subcritical for every finite `T`;
- unconditionally evaluable with the existing uniform form-factor theorem; and
- strongly horizontally sensitive on the canonical finite screening block.

It does **not** prove that this block signal survives the complete zeta pair sum, that a positive proportion of exceptional zeros organize into such blocks, or that any new lower bound for `N_0^s/N` follows. The unresolved signed-extraction step is load-bearing.

## 8. Consequence for the horizontal-rigidity clue

The accepted `CLUE-higher-zero-correlations-horizontal-rigidity` should no longer treat “support one” and “fixed support-one test” as interchangeable barriers. A concrete live pair-level route remains inside support one: take `M=(log T)^theta` with `0<theta<1`, use a uniformly `L^1`-bounded profile concentrated `Theta(1/M)` below the first alias, and try to prove a localization inequality for the resulting signed pair form. The arithmetic evaluation is already available from (2).

The decisive next test is therefore sharp. Either prove, using established zeta information, that the complete weighted form retains a positive proportion of the `Theta(M^2)` local edge energy generated by a density of screened mirror-pair blocks, and then feed that defect into the existing Weil-inertia certificate; or construct a compatible cancellation configuration showing that the surrounding zero population can neutralize every such moving-edge family while respecting the known form-factor asymptotic. Until one of those two outcomes is obtained, WI-120 is a precise information-carrier mechanism rather than a certified defect-to-zero improvement.
