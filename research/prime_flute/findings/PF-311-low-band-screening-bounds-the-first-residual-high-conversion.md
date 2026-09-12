# PF-311 — low-band screening bounds the first residual physical-high conversion

**Status:** `EXACT-DERIVED + POSITIVE/ROUTE-NARROWING + SHARP-BOUNDARY`.

PF-310 shows that the near-singular constant/nonconstant Schur reservoir already exists inside one fixed physical low band. That leaves an immediate question: after the physical-low modes have done the screening, can the same trace couple strongly and directly into the remaining physical-high sector?

At the level of the positive boundary form there is an exact answer. Split a finite canonical PF-205 boundary section into cuff constants `C`, retained nonconstant physical-low modes `L`, and retained physical-high modes `H`. Short the `L` variables first. The resulting constant/high form has blocks

\[
\begin{pmatrix}
S_L&E_{LH}\\
E_{LH}^*&R_H
\end{pmatrix}>0,
\]

where `S_L` is the constant form after optimal physical-low relaxation and `E_{LH}` is the **residual** constant-to-high coupling after that same relaxation. Positivity then forces

\[
\boxed{
\|R_H^{-1/2}E_{LH}^*x\|^2
<\langle x,S_Lx\rangle
}
\tag{1}
\]

for every nonzero constant trace `x`. Equivalently, the energy of the optimal physical-high correction available *after* low screening can never exceed the low-shorted energy still left to remove.

Applying (1) to PF-310's exact fixed-low-band witnesses gives

\[
\boxed{
\frac{\|R_H^{-1/2}E_{LH}^*x^{(M)}\|^2}
{\mathfrak m_0[x^{(M)}]}
\longrightarrow0
}
\tag{2}
\]

uniformly over finite physical-high Galerkin sections. Thus the explicit PF-310 screened family cannot carry a macroscopic **direct residual high-conversion energy** in the natural high-sector metric: once its fixed-low-band relaxation has reduced the constant energy to `o(\mathfrak m_0)`, positivity forces the first remaining high correction to be `o(\mathfrak m_0)` as well.

This is useful but deliberately not the final `P/H` estimate. The bound is sharp: the high sector may still remove an arbitrary fixed fraction of the already tiny low-shorted energy. Moreover the actual Green response contains the inverse of the twice-shorted constant form. A small residual coupling can therefore still be amplified after inversion. The next live quantity is no longer the raw low-to-high block; it is the **post-low-screening normalized angle and its source/reassembly overlap**.

## Claim

Fix the PF-212 physical cutoff `\kappa>0` and a finite PF-205 boundary-response section containing all cuff constants on the chosen geometric block. Decompose the retained boundary space as

\[
\mathcal C\oplus\mathcal L_\kappa\oplus\mathcal H_\kappa,
\]

where `\mathcal L_\kappa` contains the retained nonconstant modes with physical tangential frequency `|\xi|\le\kappa`, and `\mathcal H_\kappa` contains the retained modes with `|\xi|>\kappa`. In the canonical positive boundary normalization write

\[
\mathcal A=
\begin{pmatrix}
H&B_L&B_H\\
B_L^*&J_{LL}&J_{LH}\\
B_H^*&J_{HL}&J_{HH}
\end{pmatrix}>0.
\tag{3}
\]

All diagonal blocks are strictly positive on the finite section. Shorting the physical-low variables gives

\[
\boxed{
S_L:=H-B_LJ_{LL}^{-1}B_L^*,
}
\tag{4}
\]

\[
\boxed{
E_{LH}:=B_H-B_LJ_{LL}^{-1}J_{LH},
}
\tag{5}
\]

and

\[
\boxed{
R_H:=J_{HH}-J_{HL}J_{LL}^{-1}J_{LH}.
}
\tag{6}
\]

Then:

1. the once-shorted form is exactly
   \[
   \boxed{
   \mathcal A/\mathcal L_\kappa
   =
   \begin{pmatrix}
   S_L&E_{LH}\\
   E_{LH}^*&R_H
   \end{pmatrix}>0;
   }
   \tag{7}
   \]
2. for every constant trace `x`,
   \[
   \boxed{
   \|R_H^{-1/2}E_{LH}^*x\|^2
   \le \langle x,S_Lx\rangle;
   }
   \tag{8}
   \]
3. the exact additional fraction of the low-shorted constant energy removable by the retained high sector is
   \[
   \boxed{
   \rho_H(x)
   :=
   \frac{\|R_H^{-1/2}E_{LH}^*x\|^2}
   {\langle x,S_Lx\rangle}
   \in[0,1)
   }
   \tag{9}
   \]
   whenever `x\ne0`;
4. with
   \[
   T_H:=S_L^{-1/2}E_{LH}R_H^{-1/2},
   \tag{10}
   \]
   one has `\|T_H\|<1` in every finite section and
   \[
   \boxed{
   \rho_H(x)=
   \frac{\|T_H^*S_L^{1/2}x\|^2}
   {\|S_L^{1/2}x\|^2};
   }
   \tag{11}
   \]
5. shorting the high sector as well gives
   \[
   \boxed{
   S_{L,H}
   =S_L-E_{LH}R_H^{-1}E_{LH}^*
   =S_L^{1/2}(I-T_HT_H^*)S_L^{1/2};
   }
   \tag{12}
   \]
6. the constant/high block of the inverse after the low variables are eliminated is
   \[
   \boxed{
   [\mathcal A^{-1}]_{\mathcal C\mathcal H}
   =-S_L^{-1/2}
   (I-T_HT_H^*)^{-1}
   T_HR_H^{-1/2},
   }
   \tag{13}
   \]
   with the understood embedding back through the eliminated low variables.

For the PF-310 witnesses `x^{(M)}` and fixed `\kappa\ge\kappa_0`, the low-shorted form satisfies

\[
\frac{\langle x^{(M)},S_Lx^{(M)}\rangle}
{\mathfrak m_0[x^{(M)}]}
\longrightarrow0.
\tag{14}
\]

Therefore every finite retained physical-high section satisfies

\[
\boxed{
\frac{
\|R_H^{-1/2}E_{LH}^*x^{(M)}\|^2
}{
\mathfrak m_0[x^{(M)}]
}
\le
\frac{
\langle x^{(M)},S_Lx^{(M)}\rangle
}{
\mathfrak m_0[x^{(M)}]
}
\longrightarrow0.
}
\tag{15}
\]

The bound is uniform in the finite high cutoff because its right-hand side depends only on the already-shortened low problem. Along any nested high Galerkin exhaustion, (15) therefore controls the corresponding increasing family of high dual energies whenever the closed-form limit is taken.

## 1. First representation: sequential Schur elimination

Starting from (3), complete the square in the low variable `\ell`. For fixed `(x,h)`,

\[
\ell_*(x,h)
=-J_{LL}^{-1}(B_L^*x+J_{LH}h).
\tag{16}
\]

Substituting (16) into the quadratic form gives

\[
\begin{aligned}
\inf_{\ell}
\langle(x,\ell,h),\mathcal A(x,\ell,h)\rangle
&=
\langle x,S_Lx\rangle
+2\operatorname{Re}\langle E_{LH}^*x,h\rangle
+\langle h,R_Hh\rangle,
\end{aligned}
\tag{17}
\]

with exactly the blocks (4)--(6). This proves (7). Since shorting a positive finite form remains positive, `R_H>0` and its Schur complement is positive:

\[
S_L-E_{LH}R_H^{-1}E_{LH}^*>0.
\tag{18}
\]

Taking the quadratic form of (18) on `x` yields (8). Factoring (18) by `S_L^{1/2}` gives

\[
I-T_HT_H^*>0,
\tag{19}
\]

hence `\|T_H\|<1`, (11), and (12). The standard two-block inverse formula then gives (13).

The important point is the order of elimination. `E_{LH}` is **not** the raw constant/high block `B_H`. It includes the indirect path

\[
-B_LJ_{LL}^{-1}J_{LH},
\]

so it already accounts for one low-sector relaxation followed by low/high recoupling. This is exactly the first post-screening conversion vertex asked for at the end of PF-310.

## 2. Second representation: residual high gradient of the low-shorted variational problem

Equation (17) gives a different interpretation that does not start from block inversion. Define, for a fixed constant trace `x`,

\[
F_x(h)
:=
\inf_{\ell}
\langle(x,\ell,h),\mathcal A(x,\ell,h)\rangle.
\tag{20}
\]

Then

\[
F_x(0)=\langle x,S_Lx\rangle,
\tag{21}
\]

and the residual physical-high linear functional at `h=0` is

\[
\frac12\,dF_x(0)[h]
=\operatorname{Re}\langle E_{LH}^*x,h\rangle.
\tag{22}
\]

Its dual norm in the intrinsic high curvature `R_H` is precisely

\[
\|R_H^{-1/2}E_{LH}^*x\|.
\tag{23}
\]

Optimizing (20) over `h` gives

\[
h_*(x)=-R_H^{-1}E_{LH}^*x
\tag{24}
\]

and

\[
F_x(0)-\inf_hF_x(h)
=
\|R_H^{-1/2}E_{LH}^*x\|^2.
\tag{25}
\]

Because the fully minimized positive energy cannot be negative, (25) immediately gives (8). Thus (8) says something stronger than “a block norm is bounded”: **the high sector cannot remove more energy than remains after the low sector has already been optimized**.

For PF-310 this is decisive at the absolute killing scale. Its exact fixed-low-band trial proves that the remaining low-shorted energy is `o(\mathfrak m_0)`. Equation (25) therefore forces the entire next-stage high relaxation gain, measured in its natural energy metric, to be `o(\mathfrak m_0)` as well. No separate geometric high-frequency estimate is needed for that conclusion.

## 3. Sharp finite model: positivity does not force the residual fraction to vanish

The conclusion must not be strengthened from absolute smallness to a vanishing **fraction** of the already screened energy. A scalar three-block family shows the distinction exactly.

Take `0<\varepsilon<1` and `|\tau|<1`, and set

\[
\mathcal A_{\varepsilon,\tau}
=
\begin{pmatrix}
1&\sqrt{1-\varepsilon}&\tau\sqrt{\varepsilon}\\
\sqrt{1-\varepsilon}&1&0\\
\tau\sqrt{\varepsilon}&0&1
\end{pmatrix}.
\tag{26}
\]

Shorting the middle, “low”, coordinate gives

\[
\mathcal A_{\varepsilon,\tau}/L
=
\begin{pmatrix}
\varepsilon&\tau\sqrt{\varepsilon}\\
\tau\sqrt{\varepsilon}&1
\end{pmatrix}>0,
\tag{27}
\]

and therefore

\[
S_L=\varepsilon,
\qquad
E_{LH}=\tau\sqrt{\varepsilon},
\qquad
R_H=1.
\tag{28}
\]

The absolute residual high-conversion energy is

\[
|E_{LH}|^2=\tau^2\varepsilon\to0,
\tag{29}
\]

but the post-screening fraction is exactly

\[
\boxed{\rho_H=\tau^2.}
\tag{30}
\]

After high shorting the remaining constant energy is

\[
\varepsilon(1-\tau^2).
\tag{31}
\]

Hence any fixed fraction in `[0,1)` of the tiny low-shorted energy is compatible with positivity. The estimate (8) is sharp, and PF-310 alone does **not** imply `\rho_H(x^{(M)})\to0`.

This scalar model is only an algebraic falsification control. It is not asserted to model prime-flute geometry. Its role is to prevent an invalid inference from (15) to a vanishing normalized second Schur angle.

## 4. Consequence for the current physical `P/H` frontier

PF-310 left two broad possibilities for the known screened reservoir: either low-to-high conversion is already large immediately after low screening, or later inversion/reassembly turns a small residual coupling into a dangerous output. Equation (15) removes the first possibility **in absolute energy currency for the explicit PF-310 family**.

The first residual high coupling cannot carry order-one killing-normalized mass before inversion. The exact mixed inverse (13), however, shows why this is not yet a compactness or weak-trace theorem. The physical-high output of a forced problem contains

\[
S_L^{-1/2}(I-T_HT_H^*)^{-1}T_HR_H^{-1/2}.
\tag{32}
\]

PF-310 already makes `S_L^{-1}` large on its screened directions. Therefore even an absolutely small `E_{LH}` can matter after the source is passed through the low-screened inverse. What must now be measured is source-adapted:

- the fraction `\rho_H(x)` on the actual screened/source-reached directions;
- equivalently the overlap of `T_H` with those directions;
- and the placement of the physical source and signed target reassembly around the inverse in (32).

This sharpens the accepted source-weighted-return clue. A return/reassembly representation need not explain a macroscopic raw `B_H` coupling: sequential shorting proves that the relevant first downstream object is the residual block (5), and positivity already controls its absolute dual energy by the low-screened deficit. Any obstruction must survive the subsequent inverse/source/target normalization rather than arise from a direct energy-scale violation at this vertex.

## Prior-art and novelty audit

The algebra is classical. Li and Mathias, *Extremal Characterizations of the Schur Complement and Resulting Inequalities*, SIAM Review **42** (2000), 233--246, DOI `10.1137/S0036144599337290`, gives the standard variational and operator-inequality framework for positive Schur complements. The sequential-elimination identity is an instance of the classical quotient formula for Schur complements; see, for example, F. Zhang, *A Matrix Identity on the Schur Complement*, Linear and Multilinear Algebra **52** (2004), 367--373, DOI `10.1080/03081080310001645172`, which discusses the Crabtree--Haynsworth quotient formula. No novelty is claimed for (4)--(13) as abstract matrix identities.

The Mathia-specific deduction is their placement after PF-310's exact physical-low screening theorem. The combination shows that the explicit prime-flute low-band Schur witness has asymptotically negligible **first residual physical-high conversion energy** at the killing scale, while also proving that this does not settle the normalized post-screening angle. A targeted literature audit located the expected general Schur-complement theory, not a theorem addressing this prime-flute physical-frequency placement.

## Boundaries and falsification

1. **Finite-section statement first.** Equations (3)--(13) are exact for finite positive Galerkin sections. Passage to an infinite high sector requires the standard closed-form/shorting limit; (15) is uniform in finite high cutoff and is the safe statement needed here.
2. **Residual block, not raw block.** Replacing `E_{LH}` by `B_H` is wrong whenever `J_{LH}\ne0`. The indirect term in (5) is precisely the low-to-high reassembly created by eliminating the low variables.
3. **Absolute versus relative smallness.** PF-310 plus positivity gives (15), not `\rho_H\to0`. The exact family (26)--(31) kills that stronger inference.
4. **Energy norm versus final physical output.** `R_H^{-1/2}` is the intrinsic high-sector energy dual normalization after low shorting. A later physical target map, moving support, signed reassembly, or inverse may change the relevant output currency and needs its own estimate.
5. **The low inverse is already dangerous.** Equation (13) retains `S_L^{-1/2}`. The result does not undo PF-310's divergent low-screened Green reservoir; it identifies where a physical-high output would have to couple to that reservoir.
6. **No multiplicity result.** Nothing here counts near-screened directions or proves a Schatten/weak-Schatten estimate.
7. **No RH implication.** Resonances, determinants, zeta-zero correspondence, the critical line, and RH remain outside this finding.

The decisive next test is now narrower than PF-310's final paragraph: compute or bound `\rho_H` (or the equivalent source-adapted `T_H` overlap) on the actual killing-normalized screened directions, then insert the physical source and signed target reassembly around (32). If that overlap decays faster than the low inverse grows, the known Schur obstruction is harmless for the mixed response; if it does not, equation (32) identifies the exact amplification mechanism.