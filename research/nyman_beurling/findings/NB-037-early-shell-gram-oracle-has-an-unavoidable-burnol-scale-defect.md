# NB-037 — the early-shell Gram oracle has an unavoidable Burnol-scale defect

**Status:** `EXACT-DERIVED + TARGET-CORRELATION-DEFECT-LOWER-BOUND + RELATIVE-GRAM-DEFECT-LOWER-BOUND + BURNOL-SCALE-OBSTRUCTION + NEGATIVE/BOUNDARY`. `NB-034` gives the weighted-tail skeleton and its explicit early-shell lower Gram matrix `B_M`; `NB-036` localizes every remaining upper-section dependence to the positive defect matrix `Z_{M,N}` and target-correlation defect `eta_{M,N}`. Those defects cannot both be treated as asymptotically negligible at the accuracy requested by the accepted weighted-skeleton target-data clue.

For `2 <= M <= N`, abbreviate

\[
B:=B_M,
\qquad
H:=\widehat H_{M,N},
\qquad
u:=u_M,
\qquad
\eta:=\eta_{M,N},
\qquad
Z:=Z_{M,N},
\]

and

\[
d:=d_N=\operatorname{dist}(e,V_N),
\qquad
\kappa:=\widehat\kappa_{M,N}
=\operatorname{dist}(e,\widehat K_{M,N}).
\tag{1}
\]

Here the source vector is

\[
u=
\bigl(-\mu(2),\ldots,-\mu(M-1),\,M m(M-1)\bigr)^T.
\tag{2}
\]

Then

\[
\boxed{u^*Bu=1-\frac1M.}
\tag{3}
\]

Define

\[
\Delta_{M,N}:=
\left[
\sqrt{1-\frac1M}-\sqrt{1-d^2}
\right]_+.
\tag{4}
\]

The target-correlation defect necessarily satisfies

\[
\boxed{
\|B^{1/2}\eta\|_2
\ge \Delta_{M,N}
\ge \frac{(d^2-1/M)_+}{2}.
}
\tag{5}
\]

If

\[
S_{M,N}:=B^{1/2}ZB^{1/2}\succeq0,
\tag{6}
\]

then, for `d>0`,

\[
\boxed{
\|S_{M,N}\|_{\mathrm{op}}
\ge
\frac{\Delta_{M,N}^2}{d^2}
\ge
\frac{(d^2-1/M)_+^2}{4d^2}.
}
\tag{7}
\]

Moreover `S_{M,N}` is exactly the relative Gram error made by replacing the true retained Gram matrix by the explicit early-shell matrix:

\[
\boxed{
\left\|
H^{-1/2}(B-H)H^{-1/2}
\right\|_{\mathrm{op}}
=
\|S_{M,N}\|_{\mathrm{op}}.
}
\tag{8}
\]

Hence, for any predeclared cutoff with

\[
\frac{M}{\log N}\longrightarrow\infty,
\tag{9}
\]

Burnol's unconditional lower bound `d_N^2 \gg 1/log N` gives `1/M=o(d_N^2)`, so

\[
\boxed{
\|B_M^{1/2}\eta_{M,N}\|_2
\ge\left(\frac12-o(1)\right)d_N^2
\gg\frac1{\log N},
}
\tag{10}
\]

and

\[
\boxed{
\left\|
\widehat H_{M,N}^{-1/2}
(B_M-\widehat H_{M,N})
\widehat H_{M,N}^{-1/2}
\right\|_{\mathrm{op}}
\ge\left(\frac14-o(1)\right)d_N^2
\gg\frac1{\log N}.
}
\tag{11}
\]

Thus `B_M` is a useful conditioning certificate but cannot itself be an `o(1/log N)` target-data oracle in the moving-cutoff regime where `NB-034` preserves relative Nyman distance.

## 1. Exact early-shell target norm

Let

\[
E_M:=\operatorname{span}\{\mathbf 1_{I_t}:1\le t<M\},
\qquad
I_t=\left(\frac1{t+1},\frac1t\right].
\tag{12}
\]

`NB-034` proves that the restrictions of `g_2,...,g_M` to the first `M-1` shells form a basis of `E_M`. `NB-036` gives the corresponding dual basis

\[
\lambda_j^{(M)}=\xi_j\quad(j<M),
\qquad
\lambda_M^{(M)}=M\Psi_{M-1},
\tag{13}
\]

with

\[
\langle g_i,\lambda_j^{(M)}\rangle=\delta_{ij},
\qquad
\bigl(\langle e,\lambda_j^{(M)}\rangle\bigr)_{j=2}^M=u.
\tag{14}
\]

Because the dual vectors are supported on those early shells, `u` is exactly the coefficient vector of `P_{E_M}e` in the restricted generator basis. Since `B_M` is the Gram matrix of those restrictions,

\[
u^*Bu
=\|P_{E_M}e\|^2
=\sum_{t=1}^{M-1}|I_t|
=\sum_{t=1}^{M-1}\frac1{t(t+1)}
=1-\frac1M,
\tag{15}
\]

proving (3). Equivalently, the Möbius/Vasyunin coordinates reconstruct the constant target exactly on every shell `I_t`, `t<M`.

If one formally sets `Z=0` and `eta=0` in the `NB-036` certificate, then `H=B` and this zero-defect model predicts

\[
\kappa_0^2=1-u^*Bu=\frac1M.
\tag{16}
\]

For the cutoffs in (9), the true finite Nyman distance is unconditionally larger than this scale, so the missing mass must re-enter through the upper-section defects.

## 2. The target defect is forced by the distance gap

`NB-036` gives the retained source coordinates and inverse Gram identity

\[
c=u-\eta,
\qquad
H^{-1}=B^{-1}-Z,
\qquad
Z\succeq0.
\tag{17}
\]

The last two relations imply `H\succeq B`. Therefore

\[
\|B^{1/2}(u-\eta)\|_2^2
\le
(u-\eta)^*H(u-\eta)
=1-\kappa^2
\le1-d^2,
\tag{18}
\]

where the final inequality uses `\widehat K_{M,N}\subseteq V_N`. Together with (3), the reverse triangle inequality gives

\[
\|B^{1/2}\eta\|_2
\ge
\sqrt{1-1/M}-\sqrt{1-d^2}
\tag{19}
\]

whenever the right-hand side is positive, and otherwise the positive-part formulation in (5) is trivial. If `d^2>1/M`, rationalization yields

\[
\sqrt{1-1/M}-\sqrt{1-d^2}
=
\frac{d^2-1/M}
{\sqrt{1-1/M}+\sqrt{1-d^2}}
\ge\frac{d^2-1/M}{2}.
\tag{20}
\]

This proves (5). In particular, if `d_N^2>1/M`, then `eta_{M,N}` cannot vanish: the early-shell source vector would otherwise reconstruct too much target mass to be compatible with the actual finite distance.

## 3. Target correlation forces a metric defect

The PSD estimate of `NB-036`,

\[
\eta\eta^*\preceq d^2Z,
\tag{21}
\]

becomes after conjugation by `B^{1/2}`

\[
(B^{1/2}\eta)(B^{1/2}\eta)^*
\preceq d^2S_{M,N}.
\tag{22}
\]

Taking operator norms and using (5) proves (7).

Also, from (17),

\[
B^{1/2}H^{-1}B^{1/2}=I-S_{M,N}.
\tag{23}
\]

The positive matrices `B^{1/2}H^{-1}B^{1/2}` and `H^{-1/2}BH^{-1/2}` have the same eigenvalues. Since `0\prec I-S_{M,N}\preceq I`, the eigenvalues of `I-H^{-1/2}BH^{-1/2}` are exactly those of `S_{M,N}`. Hence

\[
\left\|H^{-1/2}(B-H)H^{-1/2}\right\|_{\mathrm{op}}
=
\left\|I-H^{-1/2}BH^{-1/2}\right\|_{\mathrm{op}}
=
\|S_{M,N}\|_{\mathrm{op}},
\tag{24}
\]

which is (8). This places the lower bound in exactly the relative metric used by the full-matrix sufficient condition in `CLUE-weighted-skeleton-target-data-without-full-section-oracle`.

## 4. Burnol-scale obstruction

Burnol's classical lower-bound theorem, already anchored in `SOURCES.md` and already used in `NB-034`, implies

\[
d_N^2\gg\frac1{\log N}.
\tag{25}
\]

Under (9),

\[
\frac{1/M}{d_N^2}
\ll\frac{\log N}{M}
\longrightarrow0.
\tag{26}
\]

Substituting this into (5) and (7) gives (10)--(11). Therefore the concrete approximation `H_tilde=B_M` fails the accepted clue's proposed requirement

\[
\left\|H^{-1/2}(H_{\rm tilde}-H)H^{-1/2}\right\|=o(1/\log N).
\tag{27}
\]

The failure is not an artifact of poor conditioning: it is forced by the gap between the exact early-shell target mass `1-1/M` and the nonzero finite Nyman distance.

If RH is false and `d_N` stays bounded away from zero, the same finite inequalities force a stronger, nonvanishing target and metric defect. No assumption `d_N->0` enters (3)--(8); Burnol is used only to convert those identities into the unconditional moving-cutoff obstruction.

## 5. Prior-art and evidence boundary

The external ingredients are already anchored for this line. Vasyunin's classical biorthogonal system supplies the finite dual coordinates used in `NB-036`; Burnol supplies the unconditional `1/log N` lower-bound scale. The exact norm identity (3) and defect lower bounds (5), (7), and (8) are finite Hilbert-space consequences of those persisted structures. A targeted literature search across Nyman--Beurling finite-section Gram geometry, Vasyunin biorthogonality, Burnol distance bounds, and recent multiscale Gram-compressibility work did not locate this exact weighted-tail lower-bound synthesis. This is not a priority claim: matrix order, reverse-triangle estimates, and generalized-eigenvalue algebra are standard.

The result does **not** show that `(Z_{M,N},eta_{M,N})` is algorithmically expensive, does not rule out a source-defined approximation that captures their leading components without an `N`-scale projection, and does not imply `d_N->0`. It rules out the natural zero-defect shortcut: the explicit early-shell matrix and Möbius/Vasyunin source vector cannot be promoted from a conditioning certificate to an RH-scale target-data oracle by arguing that the upper-section defects are negligible.

Accordingly, the accepted weighted-skeleton clue remains open but is narrowed. Any successful reduced oracle with `M/log N -> infinity` must recover enough upper-section information to account for a provably Burnol-scale relative Gram defect and the concomitant target-correlation defect. Refining `B_M` only as an early-shell object cannot cross the requested accuracy threshold.