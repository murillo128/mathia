# NB-037 — the early-shell Gram oracle has an unavoidable Burnol-scale defect

**Status:** `EXACT-DERIVED + TARGET-CORRELATION-DEFECT-LOWER-BOUND + RELATIVE-GRAM-DEFECT-LOWER-BOUND + BURNOL-SCALE-OBSTRUCTION + NEGATIVE/BOUNDARY`. `NB-034` constructs the weighted-tail skeleton with an explicit early-shell lower Gram matrix `B_M`, while `NB-036` localizes all upper-section dependence to the positive defect matrix `Z_{M,N}` and target-correlation defect `eta_{M,N}`. Those defects are not merely bookkeeping terms that might both be negligible at the accuracy requested by the accepted weighted-skeleton target-data clue. The early-shell model itself forces them to be visible at least at the finite Nyman-distance scale.

Use the notation of `NB-034` and `NB-036`. Thus, for `2 <= M <= N`, let

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

and put

\[
d:=d_N=\operatorname{dist}(e,V_N),
\qquad
\kappa:=\widehat\kappa_{M,N}
=\operatorname{dist}(e,\widehat K_{M,N}).
\tag{1}
\]

Then the explicit source vector

\[
u=
\bigl(-\mu(2),\ldots,-\mu(M-1),\,M m(M-1)\bigr)^T
\tag{2}
\]

satisfies the exact early-shell identity

\[
\boxed{
\nu^*B\nu=1-\frac1M.
}
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

The target-correlation defect from `NB-036` necessarily obeys

\[
\boxed{
\|B^{1/2}\eta\|_2
\ge \Delta_{M,N}
\ge \frac{(d^2-1/M)_+}{2}.
}
\tag{5}
\]

Next put

\[
S_{M,N}:=B^{1/2}ZB^{1/2}\succeq0.
\tag{6}
\]

For `d>0`, the positive defect relation `eta eta^* <= d^2 Z` of `NB-036` gives

\[
\boxed{
\|S_{M,N}\|_{
\mathrm{op}}
\ge
\frac{\Delta_{M,N}^2}{d^2}
\ge
\frac{(d^2-1/M)_+^2}{4d^2}.
}
\tag{7}
\]

Moreover this is exactly the relative Gram error made by replacing the true retained Gram matrix by the explicit early-shell matrix:

\[
\boxed{
\left\|
H^{-1/2}(B-H)H^{-1/2}
\right\|_{
\mathrm{op}}
=
\|S_{M,N}\|_{
\mathrm{op}}.
}
\tag{8}
\]

Consequently the candidate `H_tilde=B_M` cannot satisfy an `o(1/log N)` relative-metric error at any predeclared cutoff with

\[
\frac{M}{\log N}\longrightarrow\infty.
\tag{9}
\]

Indeed the unconditional Burnol lower bound already anchored for this line gives `d_N^2 \gg 1/log N`. Hence (9) implies `1/M=o(d_N^2)`, and (5)--(8) yield

\[
\boxed{
\|B_M^{1/2}\eta_{M,N}\|_2
\ge \left(\frac12-o(1)\right)d_N^2
\gg \frac1{\log N},
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
\right\|_{
\mathrm{op}}
\ge
\left(\frac14-o(1)\right)d_N^2
\gg \frac1{\log N}.
}
\tag{11}
\]

Thus the explicit early-shell geometry is an excellent conditioning certificate but **not** a sufficiently accurate target-data oracle at the Burnol scale. Any successful reduced construction must capture a leading part of the upper-section defect rather than discard `(Z,eta)`.

## 1. The Möbius source vector exactly reconstructs the early-shell target

Let

\[
E_M:=\operatorname{span}\{\mathbf 1_{I_t}:1\le t<M\},
\qquad
I_t=\left(\frac1{t+1},\frac1t\right].
\tag{12}
\]

`NB-034` proves that the restrictions of `g_2,...,g_M` to the first `M-1` shells form a basis of `E_M`. `NB-036` constructs the dual basis

\[
\lambda_j^{(M)}=\xi_j\quad(j<M),
\qquad
\lambda_M^{(M)}=M\Psi_{M-1},
\tag{13}
\]

supported entirely in those same shells, and gives

\[
\langle g_i,\lambda_j^{(M)}\rangle=\delta_{ij},
\qquad
\bigl(\langle e,\lambda_j^{(M)}\rangle\bigr)_{j=2}^M=\nu.
\tag{14}
\]

Therefore `nu` is exactly the coefficient vector of the early-shell projection `P_{E_M}e` in the restricted generator basis. Since `B_M` is precisely the Gram matrix of those restrictions,

\[
\nu^*B\nu
=\|P_{E_M}e\|^2
=\sum_{t=1}^{M-1}|I_t|
=\sum_{t=1}^{M-1}\frac1{t(t+1)}
=1-\frac1M,
\tag{15}
\]

which proves (3). Equivalently, the Möbius/Vasyunin source coordinates reconstruct the constant function exactly on every shell `I_t`, `t<M`; the only early-shell target mass not seen is the geometric tail of norm squared `1/M`.

This identity also calibrates the zero-defect model sharply. If one formally set `Z=0` and `eta=0` in the `NB-036` certificate, then `H=B` and the model would predict

\[
\kappa_0^2
=1-\nu^*B\nu
=\frac1M.
\tag{16}
\]

For the near-logarithmic cutoffs relevant to the weighted-skeleton clue, the true finite distance is unconditionally much larger than this `1/M` floor. The discrepancy therefore has to re-enter through the upper-section defects.

## 2. The target defect is forced by the distance gap

`NB-036` proves that the source coordinates of `P_{\widehat K_{M,N}}e` are

\[
c=\nu-\eta,
\tag{17}
\]

and that

\[
H^{-1}=B^{-1}-Z,
\qquad Z\succeq0.
\tag{18}
\]

Since inversion reverses the positive-definite order, (18) gives `H >= B`. Therefore

\[
\|B^{1/2}(\nu-\eta)\|_2^2
=(\nu-\eta)^*B(\nu-\eta)
\le
(\nu-\eta)^*H(\nu-\eta).
\tag{19}
\]

The final quadratic form is the squared norm of the retained target projection, so

\[
(\nu-\eta)^*H(\nu-\eta)=1-\kappa^2.
\tag{20}
\]

Because `\widehat K_{M,N}\subseteq V_N`, one has `\kappa>=d`; hence

\[
\|B^{1/2}(\nu-\eta)\|_2
\le\sqrt{1-d^2}.
\tag{21}
\]

On the other hand, (3) gives

\[
\|B^{1/2}\nu\|_2=\sqrt{1-1/M}.
\tag{22}
\]

The reverse triangle inequality applied to (21)--(22) proves the first inequality in (5). When `d^2>1/M`, rationalization gives

\[
\Delta_{M,N}
=
\frac{d^2-1/M}
{\sqrt{1-1/M}+\sqrt{1-d^2}}
\ge\frac{d^2-1/M}{2},
\tag{23}
\]

and if `d^2<=1/M` the positive-part version is trivial. This proves (5) for all `M,N`.

A useful qualitative corollary is immediate: whenever `d_N^2>1/M`, the target-correlation defect `eta_{M,N}` **cannot vanish**. The explicit early-shell source vector is then too close to a perfect reconstruction of `e` to be compatible with the actual finite Nyman distance.

## 3. Target correlation forces a relative metric defect as well

The automatic PSD estimate from `NB-036` is

\[
\eta\eta^*\preceq d^2Z.
\tag{24}
\]

Conjugating by `B^{1/2}` gives

\[
(B^{1/2}\eta)(B^{1/2}\eta)^*
\preceq d^2S_{M,N}.
\tag{25}
\]

Taking operator norms and applying (5) yields (7).

The same `S_{M,N}` is the exact relative metric defect. From (18),

\[
B^{1/2}H^{-1}B^{1/2}=I-S_{M,N}.
\tag{26}
\]

The positive matrices `B^{1/2}H^{-1}B^{1/2}` and `H^{-1/2}BH^{-1/2}` have the same eigenvalues. Since (18) implies `0\prec I-S_{M,N}\preceq I`, the eigenvalues of

\[
I-H^{-1/2}BH^{-1/2}
\]

are exactly the eigenvalues of `S_{M,N}`. Therefore

\[
\left\|H^{-1/2}(B-H)H^{-1/2}\right\|_{
\mathrm{op}}
=
\left\|I-H^{-1/2}BH^{-1/2}\right\|_{
\mathrm{op}}
=\|S_{M,N}\|_{
\mathrm{op}},
\tag{27}
\]

which proves (8).

This is stronger than merely observing that `B<=H`: it quantifies the exact relative error in the same metric used by the full-matrix sufficient condition in `CLUE-weighted-skeleton-target-data-without-full-section-oracle`.

## 4. Burnol-scale obstruction for the accepted weighted-skeleton clue

Burnol's classical lower-bound theorem, already recorded in this line's `SOURCES.md` and already used in `NB-034`, implies in particular

\[
d_N^2\gg\frac1{\log N}.
\tag{28}
\]

For any predeclared `M=M_N<=N` satisfying (9),

\[
\frac{1/M}{d_N^2}
\ll\frac{\log N}{M}\longrightarrow0.
\tag{29}
\]

Equations (5) and (7) now give (10)--(11). In particular, choosing `H_tilde=B_M` in the accepted clue's proposed relative-Gram criterion produces an error bounded **below**, rather than above, at order `1/log N`. The explicit early-shell matrix can therefore never by itself supply the clue's requested `o(1/log N)` metric accuracy in the regime where the quotient also preserves relative target distance.

If RH were false and `d_N` stayed bounded away from zero, the obstruction would be stronger: (5) forces a target defect bounded away from zero and (7) forces a nonvanishing relative metric defect. Thus no assumption on `d_N->0` is used in the finite inequalities; the Burnol theorem is needed only to convert them into the unconditional asymptotic statement at the clue's moving cutoffs.

## 5. Prior-art audit, boundaries, and consequence

The external ingredients are already anchored for this line. Vasyunin's classical biorthogonal system supplies the dual coordinates used by `NB-036`; Burnol supplies the unconditional `1/log N` lower-bound scale. The identities (3), (5), and (7)--(8) are finite Hilbert-space consequences of those persisted structures. A targeted literature search across Nyman--Beurling finite-section Gram geometry, Vasyunin biorthogonality, Burnol distance bounds, and recent multiscale Gram-compressibility work did not locate this exact weighted-tail lower-bound synthesis. This is not a priority claim: the matrix-order and generalized-eigenvalue steps are standard linear algebra, and the substantive line-local point is their application to the exact `NB-036` defect normal form.

The result does **not** prove that `(Z_{M,N},eta_{M,N})` is expensive to compute, does not give a lower bound on algorithmic complexity, and does not rule out a source-defined approximation that captures their leading components without an `N`-scale projection. It also does not turn the Burnol lower bound into an upper bound or imply `d_N->0`. What it rules out is the natural zero-defect shortcut: the explicit early-shell matrix and Möbius/Vasyunin source vector cannot be promoted from a conditioning certificate to an RH-scale target-data oracle merely by arguing that the discarded upper section is asymptotically negligible.

The accepted weighted-skeleton clue is therefore narrowed to a sharper requirement. Any successful reduced oracle at `M/log N -> infinity` must recover enough of the upper-section geometry to cancel a **provably Burnol-scale** relative Gram defect, and enough target information to account for the concomitant correlation defect in (5). The next useful theorem must control or reconstruct that leading defect from arithmetic data cheaper than the full finite-section solve; further refinement of `B_M` alone cannot cross the requested accuracy threshold.