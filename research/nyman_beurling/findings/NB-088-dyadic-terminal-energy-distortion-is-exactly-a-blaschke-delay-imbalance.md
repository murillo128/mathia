# NB-088 — dyadic terminal energy distortion is exactly a Blaschke-delay imbalance

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + BLASCHKE-DELAY-IDENTITY + DYADIC-VISIBLE-ENERGY + FINITE-BLASCHKE-SILENCE + NEGATIVE-METHOD-BOUNDARY + METHOD-ADVANCE`.

`NB-087` reduces a compulsory part of the fixed-`q` radial entropy charge to the scalar terminal sibling distortion

\[
\eta_{j,R}^{(q)}
=
\frac{q\,\|J_{R/q}D_j\|^2}
{\sum_{k=qj}^{q(j+1)-1}\|J_RD_k\|^2}-1.
\]

The live source question was therefore to estimate these truncated innovation norms for `j asymp R`. In the dyadic case this can be sharpened substantially. After restoring the common off-critical Blaschke factor, the visible norm is elementary and independent of `j`; all arithmetic deformation of `eta` is carried by one nonnegative **causal Blaschke-delay energy**. Moreover every fixed finite Blaschke divisor produces only `O(R^-1)` distortion per terminal sibling block, so its total squared contribution in the `NB-087` lower bound tends to zero.

This is both a source reduction and a negative method result. The scalar average-direction channel isolated by `NB-087` cannot by itself distinguish RH from a hypothetical source with only finitely many right-half off-critical zeros. Any divergent scalar obstruction for the actual source must be a genuinely collective effect of an unbounded Blaschke product, not the local footprint of one or finitely many off-critical zeros.

## 1. Restoring the Blaschke factor gives an explicit raw innovation

Use the notation of `NB-062` and `NB-084`. The actual Blaschke-deflated innovation is

\[
D_j(s)
=
\frac{\zeta(s)}{sB(s)}
\bigl(j^{1-s}-(j+1)^{1-s}\bigr),
\tag{1}
\]

where `B` is Burnol's inner Blaschke product over the zeta zeros with real part greater than `1/2`. Restore that common inner factor and write

\[
\widetilde D_j:=BD_j
=
\frac{\zeta(s)}s
\bigl(j^{1-s}-(j+1)^{1-s}\bigr).
\tag{2}
\]

Under the Paley--Wiener normalization already used in this line, `1/s` corresponds to `e^{-t/2}` and multiplication by `n^{-s}` gives the appropriately weighted right shift by `log n`. For `Re s>1`, termwise inversion of the Dirichlet series for `zeta` therefore gives the time representative

\[
\boxed{
\widetilde d_j(t)
=
e^{-t/2}
\left[
 j\left\lfloor\frac{e^t}{j}\right\rfloor
-(j+1)\left\lfloor\frac{e^t}{j+1}\right\rfloor
\right].
}
\tag{3}
\]

The bracket is `O(j)` for large `t`, so the difference in (3) is square-integrable even though the two unrecombined `zeta(s)/s` terms are not separately Hardy vectors. Thus the identity extends from the absolutely convergent half-plane to the Hardy boundary representative of (2).

Now fix a physical cutoff `X` with

\[
j+1\le X\le2j.
\tag{4}
\]

On `log j <= t < log(j+1)` the two floors in (3) are `1` and `0`; on `log(j+1) <= t <= log X` they are both `1`. Hence

\[
\widetilde d_j(t)
=
\begin{cases}
 j e^{-t/2},&\log j\le t<\log(j+1),\\[2mm]
 -e^{-t/2},&\log(j+1)\le t\le\log X.
\end{cases}
\tag{5}
\]

The visible raw norm is therefore exact:

\[
\begin{aligned}
\|J_X\widetilde D_j\|^2
&=
 j^2\int_j^{j+1}\frac{dx}{x^2}
+
\int_{j+1}^{X}\frac{dx}{x^2}\\
&=
\boxed{1-\frac1X}.
\end{aligned}
\tag{6}
\]

This equality is independent of the location of the parent inside the terminal window. The raw zeta source already has essentially perfect visible energy balance; its only dyadic mismatch comes from observing the parent at `R/2` and the children at `R`.

## 2. The full source differs from the raw norm by one nonnegative causal-delay term

Let `M_B` denote multiplication by the inner function `B`. In Paley--Wiener coordinates it is a causal isometry. Causality gives

\[
J_XM_B(I-J_X)=0,
\tag{7}
\]

while `M_BD_j=\widetilde D_j`. Define the finite-prefix Blaschke-delay energy

\[
\boxed{
\Lambda_{j,X}(B)
:=
\|(I-J_X)M_BJ_XD_j\|^2
\ge0.
}
\tag{8}
\]

Since `M_B` is an isometry,

\[
\begin{aligned}
\|J_XD_j\|^2
&=\|M_BJ_XD_j\|^2\\
&=\|J_XM_BJ_XD_j\|^2
 +\|(I-J_X)M_BJ_XD_j\|^2\\
&=\|J_X\widetilde D_j\|^2+\Lambda_{j,X}(B).
\end{aligned}
\tag{9}
\]

Combining (6) and (9), for every terminal cutoff satisfying (4),

\[
\boxed{
\|J_XD_j\|^2
=
1-\frac1X+\Lambda_{j,X}(B).
}
\tag{10}
\]

Thus the source-facing norm problem left by `NB-087` is not an unrestricted truncated-Gram asymptotic. It is exactly the problem of estimating how much energy multiplication by the off-critical inner factor pushes **past the same physical cutoff** when acting on the finite prefix of the deflated innovation.

The sign is important. The Blaschke factor can only increase the norm required on the deflated side to produce the same visible raw prefix; there is no hidden signed cancellation inside (10). What can cancel in the sibling ratio is only the *difference* of these nonnegative delay energies between parent and children.

## 3. Dyadic terminal distortion is an exact three-delay imbalance

Take `q=2` and the complete terminal parent set of `NB-087`,

\[
\mathcal P_{R,2}
=
\left\{
\left\lceil\frac R4\right\rceil
\le j\le
\left\lfloor\frac R2\right\rfloor-1
\right\}.
\tag{11}
\]

For every `j` in this set, the parent pair `(j,R/2)` and both child pairs `(2j,R)`, `(2j+1,R)` satisfy the terminal condition (4). Equation (10) therefore gives

\[
\|J_{R/2}D_j\|^2
=1-\frac2R+\Lambda_{j,R/2}(B),
\tag{12}
\]

and

\[
\|J_RD_{2j}\|^2
=1-\frac1R+\Lambda_{2j,R}(B),
\qquad
\|J_RD_{2j+1}\|^2
=1-\frac1R+\Lambda_{2j+1,R}(B).
\tag{13}
\]

Substitution into the scalar distortion from `NB-087` yields the exact identity

\[
\boxed{
\eta_{j,R}^{(2)}
=
\frac{
2\Lambda_{j,R/2}(B)
-\Lambda_{2j,R}(B)
-\Lambda_{2j+1,R}(B)
-2/R
}{
2(1-1/R)
+\Lambda_{2j,R}(B)
+\Lambda_{2j+1,R}(B)
}.
}
\tag{14}
\]

This isolates the complete arithmetic content of the dyadic average-direction obstruction. The universal raw term is only `-2/R` in the numerator. If `B=1`, as on the RH branch, all three delay energies vanish and

\[
\boxed{
\eta_{j,R}^{(2)}=-\frac1{R-1}
}
\tag{15}
\]

for every complete terminal sibling pair, independently of `j`. Consequently

\[
\sum_{j\in\mathcal P_{R,2}}|\eta_{j,R}^{(2)}|^2
=O(R^{-1})\longrightarrow0
\tag{16}
\]

on that branch. This is the correct source calibration for the scalar test; the unit-outer control of `NB-087`, where `eta=0` exactly, was a memory-free model rather than the `B=1` zeta source.

Equation (14) also specifies what a successful negative result must prove under false RH: not merely that `B` is nontrivial, but that its parent-versus-children **finite-prefix delay imbalance** has nonsummable squared mass across terminal sibling blocks.

## 4. Every fixed finite Blaschke divisor is asymptotically silent in this scalar channel

The requirement in the previous paragraph is genuinely collective. Let `B_F` be any finite Blaschke divisor formed from a fixed finite multiset `F` of actual zeta zeros with `Re rho>1/2`, respecting multiplicity, and define the matched partially deflated innovations

\[
D_j^{[F]}(s)
:=
\frac{\zeta(s)}{sB_F(s)}
\bigl(j^{1-s}-(j+1)^{1-s}\bigr).
\tag{17}
\]

Because `B_F` divides the full Burnol product, `D_j^[F]=(B/B_F)D_j` is a legitimate Hardy vector even when the full product is infinite. It obeys the same exact integer-branching law as the actual innovations.

Write a single half-plane Blaschke factor in the shifted coordinate `z=s-1/2` as

\[
b_\lambda(z)=\frac{z-\lambda}{z+\overline\lambda},
\qquad
\lambda=\rho-\frac12,
\qquad
0<\Re\lambda<\frac12,
\tag{18}
\]

up to an irrelevant unimodular constant. If `Y=b_lambda X`, then

\[
X(z)
=Y(z)
+(\lambda+\overline\lambda)\frac{Y(z)}{z-\lambda}.
\tag{19}
\]

On any finite Paley--Wiener horizon this is the causal Volterra inversion

\[
x(u)
=y(u)
+2\Re\lambda
\int_0^u e^{\lambda(u-v)}y(v)\,dv.
\tag{20}
\]

For the raw innovation, shift the support origin to `log j`, put `delta_j=log(1+1/j)`, and restrict to `0<=u<=log 2`. Equation (5) becomes

\[
y_j(u)
=
\begin{cases}
\sqrt j\,e^{-u/2},&0\le u<\delta_j,\\[1mm]
-j^{-1/2}e^{-u/2},&\delta_j\le u\le\log2.
\end{cases}
\tag{21}
\]

The large piece has height `sqrt j` but width `delta_j=O(1/j)`. Therefore the Volterra correction generated by (20) is uniformly `O(j^-1/2)` on the whole relative horizon. Since `2 Re lambda <=1` and `|e^{lambda u}|<=sqrt 2` there, the constant is independent of the height `Im rho`; iterating through a fixed number `m=deg B_F` of factors gives

\[
D_j^{[F]}(\log j+u)
=
y_j(u)+r_{j,F}(u),
\qquad
\sup_{0\le u\le\log2}|r_{j,F}(u)|
\ll_m j^{-1/2}.
\tag{22}
\]

Splitting the norm integral at `delta_j`, the cross term on the spike is `O_m(1/j)` because its width is `O(1/j)`; the tail cross term and the correction square are also `O_m(1/j)`. Hence, uniformly for `j+1<=X<=2j`,

\[
\boxed{
\|J_XD_j^{[F]}\|^2
=
1-\frac1X+O_m(j^{-1}).
}
\tag{23}
\]

Equivalently, the finite-product delay energy in (10) satisfies

\[
\Lambda_{j,X}(B_F)=O_m(j^{-1}).
\tag{24}
\]

For terminal dyadic blocks `j asymp R`, equations (14) and (24) now give the uniform estimate

\[
\boxed{
\eta_{j,R}^{[F],(2)}=O_m(R^{-1}).
}
\tag{25}
\]

Since `|P_(R,2)|=R/4+O(1)`,

\[
\boxed{
\sum_{j\in\mathcal P_{R,2}}
|\eta_{j,R}^{[F],(2)}|^2
=O_m(R^{-1})\longrightarrow0.
}
\tag{26}
\]

Thus **any fixed finite collection of right-half zeros is invisible to the compulsory scalar entropy channel isolated by `NB-087`**. In particular, if the full off-critical Blaschke product were finite, the actual Nyman source itself would satisfy (25)--(26) despite false RH.

## 5. Consequence for the radial strategy

`NB-087` proves only a lower bound

\[
\mathfrak S_{R,2}
\ge
\sum_{j\in\mathcal P_{R,2}}|\eta_{j,R}^{(2)}|^2.
\tag{27}
\]

Therefore (26) does **not** imply bounded radial Szego charge, successful screening, or vanishing stable tail for the finite-Blaschke controls. The entropy may still live in sibling contrast directions, cross-block correlations, earlier indices, or the positive radial prediction floors of `NB-085`. This finding removes only the scalar average-direction route as a finite-zero detector.

The falsification boundary is correspondingly sharp. To make the `NB-087` channel itself decisive, one must prove that the full actual Blaschke product creates a delay imbalance satisfying

\[
\sum_{j\in\mathcal P_{R,2}}
\left|
2\Lambda_{j,R/2}(B)
-\Lambda_{2j,R}(B)
-\Lambda_{2j+1,R}(B)
\right|^2
\not=O(1)
\tag{28}
\]

at the denominator scale of (14), or an equivalent lower bound that survives the universal `2/R` term. No argument based on a single fixed zero, or on any fixed finite subset of zeros, can establish such divergence: equations (24)--(26) rule that out.

This redirects the live source question. The useful object is now the **nonuniform tail of the Blaschke product across shrinking terminal cells**. A positive continuation would need a collective estimate in which the number or effective strength of relevant off-critical factors grows with `R`; alternatively, one should move to the contrast/cross-block components of the terminal correlation matrix that `NB-087` deliberately discarded.

## 6. Prior-art and adversarial boundary

The Blaschke factor itself is classical in this line and already anchored to Burnol in `SOURCES.md`; no novelty is claimed for extracting the common off-critical inner factor or for the elementary half-plane Blaschke/Volterra algebra. The closest recent line-level prior art located in the audit is Ziad's 2026 Gram-spectral decomposition, which explicitly separates a finite Blaschke skeleton from an arithmetic Gram projection defect, and Carvill's 2025 multiscale Gram/block-compressibility analysis after Mellin smoothing. Neither supplies the terminal-window identity (10), the exact dyadic delay balance (14), or the finite-product suppression (25)--(26). No priority claim is made.

The main adversarial checks are built into the statement. First, the result does not infer small entropy from small `eta`; (27) has the wrong direction for that. Second, it does not replace the full Burnol product by a finite one: finite products are used only as matched controls and as the exact actual source in the logically possible finite-off-critical-zero case. Third, the Volterra estimate is restricted to the relative horizon `log 2`, where inversion of each unstable Blaschke factor is uniformly bounded; no global inverse bound for `B` is assumed. Fourth, multiplicity is allowed, but the degree of the finite divisor is fixed before `R` tends to infinity.

No new specialized external estimate is load-bearing, so `SOURCES.md` remains unchanged.

The durable delta after `NB-087` is therefore twofold: **the dyadic scalar distortion is exactly a three-term Blaschke-delay imbalance, and every fixed finite off-critical Blaschke defect is asymptotically too small to make its squared terminal mass diverge**. The next useful theorem must either make the infinite-product tail visible quantitatively or leave the scalar average sibling direction and exploit the remaining terminal correlation geometry.