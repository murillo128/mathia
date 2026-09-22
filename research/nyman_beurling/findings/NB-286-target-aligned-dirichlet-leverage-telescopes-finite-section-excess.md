# NB-286 — target-aligned Dirichlet leverage telescopes finite-section excess

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-284, NB-285
- **Classification:** `EXACT-DERIVED + FIRST-FREE-JET-COST + FINITE-SECTION-GRAM + RANK-ONE-UPDATE + TARGET-AWARE-LEVERAGE + MOVING-PACKET-CONDITIONING + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-285` writes the genuine finite-section penalty

\[
\mathfrak A_M
=
\mathcal C_M-\mathcal C_\infty
\]

as representer tail plus optimal sample repair and identifies the missing sampling Gram as a sum of rank-one increments contributed by future orthogonalized Dirichlet atoms. Those increments can be followed one at a time, and the constrained synthesis cost then admits an exact telescoping law.

Fix a zero packet `Z` and use the closed quotient-source space, first-free sampling map and nested finite sections from `NB-285`:

\[
L:\mathcal H_Z^\infty\to\mathbb C^N,
\qquad
V_M\subset V_{M+1},
\qquad
K_M=LP_ML^*.
\]

Work beyond the eventual-surjectivity threshold supplied by `NB-282`, so `K_M` is positive definite. Whenever `V_{M+1}` gains one new direction, choose the normalized orthogonalized source atom

\[
\psi_{M+1}\in V_{M+1}\ominus V_M
\]

and put

\[
v_{M+1}:=L\psi_{M+1}\in\mathbb C^N.
\]

If no new direction is added, set `v_(M+1)=0`. Then

\[
\boxed{
K_{M+1}=K_M+v_{M+1}v_{M+1}^*.
}
\tag{1}
\]

For the prescribed first-free datum `y`, define

\[
\mathcal C_M:=y^*K_M^{-1}y.
\tag{2}
\]

The exact one-step gain from admitting the next Dirichlet direction is

\[
\boxed{
\mathcal C_M-\mathcal C_{M+1}
=
\frac{
|v_{M+1}^*K_M^{-1}y|^2
}{
1+v_{M+1}^*K_M^{-1}v_{M+1}
}.
}
\tag{3}
\]

Consequently, because `NB-284` proves `C_R -> C_infty` for every fixed packet,

\[
\boxed{
\mathfrak A_M
=
\sum_{r\ge M}
\frac{
|v_{r+1}^*K_r^{-1}y|^2
}{
1+v_{r+1}^*K_r^{-1}v_{r+1}
}.
}
\tag{4}
\]

Thus the finite-section excess is not controlled by the future Dirichlet leverage alone. Only the component of each future sample vector aligned with the **current constrained target direction** can reduce the synthesis cost.

More precisely, with

\[
z_r:=K_r^{-1/2}y,
\qquad
w_r:=K_r^{-1/2}v_{r+1},
\]

let

\[
\ell_r:=\|w_r\|^2
=v_{r+1}^*K_r^{-1}v_{r+1}
\tag{5}
\]

and, when `w_r` is nonzero,

\[
\cos^2\theta_r
:=
\frac{|w_r^*z_r|^2}{\|w_r\|^2\|z_r\|^2}.
\tag{6}
\]

Set the angle factor to zero when `w_r=0`. Then

\[
\boxed{
\alpha_r
:=
\frac{\mathcal C_r-\mathcal C_{r+1}}{\mathcal C_r}
=
\cos^2\theta_r\,
\frac{\ell_r}{1+\ell_r}.
}
\tag{7}
\]

Hence

\[
\boxed{
\mathcal C_{r+1}=\mathcal C_r(1-\alpha_r),
}
\tag{8}
\]

and the whole finite-section penalty has the exact product form

\[
\boxed{
\frac{\mathcal C_\infty}{\mathcal C_M}
=
\prod_{r\ge M}(1-\alpha_r),
\qquad
\frac{\mathfrak A_M}{\mathcal C_M}
=
1-
\prod_{r\ge M}(1-\alpha_r).
}
\tag{9}
\]

For nonzero datum `y`, `C_infty>0`, so equivalently

\[
\boxed{
-\log\left(1-\frac{\mathfrak A_M}{\mathcal C_M}\right)
=
\sum_{r\ge M}-\log(1-\alpha_r).
}
\tag{10}
\]

This is an exact target-aware criterion. A persistent **relative** finite-section excess requires a persistent tail budget of target-aligned leverage after the legal cutoff. Large future Gram increments, large determinant growth, or poor conditioning in directions orthogonal to the constrained datum are not enough.

---

## 1. The next Dirichlet atom gives a rank-one sampling update

For a fixed packet, retain all notation from `NB-285`. The finite quotient-source spaces are nested because increasing the Dirichlet cutoff only adds generators:

\[
V_M\subseteq V_{M+1}\subseteq\mathcal H.
\tag{11}
\]

The orthogonal projection difference

\[
P_{M+1}-P_M
\tag{12}
\]

has rank at most one. If the new source atom is already in `V_M`, this difference is zero. Otherwise Gram--Schmidt gives a unit vector

\[
\psi_{M+1}\in V_{M+1}\cap V_M^\perp
\tag{13}
\]

such that

\[
P_{M+1}-P_M
=
\psi_{M+1}\otimes\psi_{M+1}.
\tag{14}
\]

Applying the sample map on both sides gives

\[
\begin{aligned}
K_{M+1}-K_M
&=L(P_{M+1}-P_M)L^*\\
&=(L\psi_{M+1})(L\psi_{M+1})^*.
\end{aligned}
\tag{15}
\]

With `v_(M+1)=L psi_(M+1)`, this is exactly `(1)`. It is also the one-step version of the tail decomposition already recorded in `NB-285`:

\[
E_M
=K_\infty-K_M
=\sum_{r\ge M}v_{r+1}v_{r+1}^*.
\tag{16}
\]

The new point is to propagate the **inverse constrained cost**, rather than estimate the static tail Gram by an operator norm.

---

## 2. Sherman--Morrison gives the exact one-step cost decrease

Once `M` is beyond the finite surjectivity threshold of `NB-282`, `K_M` is positive definite. Equation `(1)` is therefore a positive rank-one update, so the Sherman--Morrison identity gives

\[
K_{M+1}^{-1}
=
K_M^{-1}
-
\frac{
K_M^{-1}v_{M+1}v_{M+1}^*K_M^{-1}
}{
1+v_{M+1}^*K_M^{-1}v_{M+1}
}.
\tag{17}
\]

Pairing `(17)` with the fixed first-free datum `y` yields

\[
\begin{aligned}
\mathcal C_{M+1}
&=y^*K_{M+1}^{-1}y\\
&=\mathcal C_M
-
\frac{|v_{M+1}^*K_M^{-1}y|^2}
{1+v_{M+1}^*K_M^{-1}v_{M+1}}.
\end{aligned}
\tag{18}
\]

This proves `(3)`.

Summing `(18)` from `r=M` to `R-1` gives

\[
\mathcal C_M-\mathcal C_R
=
\sum_{r=M}^{R-1}
\frac{|v_{r+1}^*K_r^{-1}y|^2}
{1+v_{r+1}^*K_r^{-1}v_{r+1}}.
\tag{19}
\]

For a fixed packet, `NB-284` proves

\[
\mathcal C_R\downarrow\mathcal C_\infty.
\tag{20}
\]

Taking `R -> infinity` in `(19)` proves `(4)` without any interchange of conditionally convergent signed terms: every summand is nonnegative and the finite sums are exactly bounded by `C_M-C_infty`.

Thus `A_M` is itself a sum of source-enrichment gains. There is no missing cross term between different future atoms; their interaction is already encoded dynamically through the changing inverse metric `K_r^(-1)`.

---

## 3. Whitening separates leverage from target alignment

Define the whitened target and next sample vector by

\[
z_r=K_r^{-1/2}y,
\qquad
w_r=K_r^{-1/2}v_{r+1}.
\tag{21}
\]

Then

\[
\mathcal C_r=\|z_r\|^2,
\qquad
\ell_r=\|w_r\|^2,
\tag{22}
\]

while the numerator in `(3)` is

\[
|v_{r+1}^*K_r^{-1}y|^2
=|w_r^*z_r|^2.
\tag{23}
\]

If `w_r` is nonzero, write

\[
|w_r^*z_r|^2
=\ell_r\mathcal C_r\cos^2\theta_r.
\tag{24}
\]

Substitution into `(3)` gives `(7)` and `(8)`.

The factor

\[
\frac{\ell_r}{1+\ell_r}
\tag{25}
\]

measures how strong the new direction is in the current sample metric. The factor

\[
\cos^2\theta_r
\tag{26}
\]

measures whether that strength points in the direction that actually reduces the prescribed interpolation cost. This is exactly the target/source distinction emphasized from `NB-001` onward, now at the one-Dirichlet-atom enrichment level.

There is also a target-free interpretation of `ell_r`. The matrix determinant lemma gives

\[
\boxed{
\frac{\det K_{r+1}}{\det K_r}
=1+\ell_r.
}
\tag{27}
\]

Hence a new atom can make the sampling Gram much larger in determinant or improve a badly represented direction while contributing **zero** to the target cost if its whitened sample vector is orthogonal to `z_r`.

A two-dimensional matched control makes this exact. Take

\[
K_r=I_2,
\qquad
y=e_1,
\qquad
v_{r+1}=T e_2.
\tag{28}
\]

Then

\[
\ell_r=T^2,
\qquad
\frac{\det K_{r+1}}{\det K_r}=1+T^2,
\tag{29}
\]

but

\[
v_{r+1}^*K_r^{-1}y=0
\tag{30}
\]

and therefore

\[
\mathcal C_{r+1}=\mathcal C_r=1
\tag{31}
\]

for arbitrarily large `T`. By contrast, if `v_(r+1)=T e_1`, the direction is fully aligned and

\[
\mathcal C_{r+1}=\frac1{1+T^2}.
\tag{32}
\]

So raw Gram growth and target-relevant synthesis progress can be separated by an arbitrarily large factor.

---

## 4. The finite-section excess is an exact aligned-leverage tail product

From `(8)`, for every finite `R>M`,

\[
\frac{\mathcal C_R}{\mathcal C_M}
=
\prod_{r=M}^{R-1}(1-\alpha_r).
\tag{33}
\]

For nonzero `y`, all constrained costs are strictly positive, and `(7)` gives

\[
0\le\alpha_r<1.
\tag{34}
\]

Using `(20)` in `(33)` proves the first identity in `(9)`. Since

\[
\mathfrak A_M
=\mathcal C_M-\mathcal C_\infty,
\tag{35}
\]

the second follows immediately.

This gives two useful equivalent diagnostics. First,

\[
\frac{\mathfrak A_M}{\mathcal C_M}
=1-\prod_{r\ge M}(1-\alpha_r)
\le
\sum_{r\ge M}\alpha_r.
\tag{36}
\]

Therefore a sufficient moving-packet condition for the genuine finite-section excess to vanish **relative to the current constrained cost** is

\[
\sum_{r\ge M_X}\alpha_{X,r}\to0.
\tag{37}
\]

Second, `(10)` shows the converse quantitative necessity. If along a moving family

\[
\frac{\mathfrak A_{M_X}(Z_X)}
{\mathcal C_{M_X}(Z_X)}
\ge\delta>0,
\tag{38}
\]

then

\[
\boxed{
\sum_{r\ge M_X}
-\log(1-\alpha_{X,r})
\ge
-\log(1-\delta).
}
\tag{39}
\]

In particular, `(36)` already implies

\[
\sum_{r\ge M_X}\alpha_{X,r}\ge\delta.
\tag{40}
\]

Thus a persistent relative obstruction cannot be attributed merely to future source mass or future conditioning. A fixed positive budget of **target-aligned** enrichment must survive beyond the legal cutoff.

If one additionally knows that `C_(M_X)` stays uniformly bounded above, an absolute floor

\[
\mathfrak A_{M_X}\ge\eta>0
\tag{41}
\]

forces the same conclusion with `delta=eta/sup C_(M_X)`. Without such a normalization, absolute and relative excess must not be conflated.

---

## 5. Relation to NB-285 and the new arithmetic target

`NB-285` leaves two static quantities:

\[
E_M=\sum_{r\ge M}v_{r+1}v_{r+1}^*
\tag{42}
\]

and the repair metric `K_M^(-1)`. Its general bound

\[
\mathfrak A_M
\le
\mathfrak T_M
\left(1+\frac{\|E_M\|}{\lambda_{\min}(K_M)}\right)
\tag{43}
\]

is useful but deliberately worst-case. Equation `(4)` gives the corresponding target-aware exact decomposition. Future atoms are charged only by

\[
\boxed{
\frac{|v_{r+1}^*K_r^{-1}y|^2}
{1+v_{r+1}^*K_r^{-1}v_{r+1}},
}
\tag{44}
\]

not by `||v_(r+1)||`, `ell_r`, a determinant increment, or `lambda_min(K_r)` alone.

This changes the most discriminating next calculation. For a Ford-coupled packet `Z_X` and legal cutoff `M_X`, one should estimate the orthogonalized future Dirichlet sample vectors

\[
v_{X,r+1}=L_{Z_X}\psi_{X,r+1}
\tag{45}
\]

in the **evolving inverse sample metric** and, crucially, their pairing with

\[
K_{X,r}^{-1}y_X.
\tag{46}
\]

A target-free estimate showing large future leverage is not a lower bound for `A_(M_X)`. Conversely, to prove that the finite arithmetic section is already adequate, it is enough to show that the tail of the aligned factors in `(37)` vanishes, even if the full missing Gram remains large in irrelevant directions.

The resulting bottleneck is therefore sharper than the generic conditioning question left by `NB-284` and `NB-285`:

> does the actual arithmetic sequence of future orthogonalized Dirichlet atoms carry a nonvanishing **target-aligned leverage tail** at Ford scale after the permitted cutoff?

This is a source-native, target-aware question. It cannot be answered from the zero-only Gram, support rank, determinant growth, or unaligned condition numbers.

---

## 6. Adversarial checks and evidence boundary

### Invertibility boundary

The inverse formulas begin only after `K_M` is positive definite. This is legitimate because `NB-282` supplies a finite surjective first-free section for every fixed packet, but no uniform bound on that threshold is claimed here. Before that point one would need Moore--Penrose update formulas and explicit range bookkeeping; `NB-286` does not use them.

### Fixed-packet versus moving-packet quantifiers

The passage from the finite telescoping sum `(19)` to the infinite identities `(4)` and `(9)` uses the fixed-packet convergence `C_R -> C_infty` proved in `NB-284`. For a moving Ford family, the identities are applied separately to each packet and then the resulting aligned-leverage tails are compared. No uniform convergence in the packet is assumed.

### Target alignment is dynamic

The angle in `(6)` is measured using `K_r`, not a frozen initial Gram or the limiting `K_infty`. Replacing it by a fixed Euclidean angle would discard the exact recursion. The update of the metric is precisely how interactions among different future atoms enter the scalar cost.

### No arithmetic estimate yet

The finding does **not** prove that the tail in `(37)` vanishes or persists for the actual Nyman/Ford packets. It converts that question into an exact sequential scalar budget. Estimating `v_(r+1)` and its evolving target pairing remains the arithmetic step.

### No novelty claim for rank-one inverse algebra

Sherman--Morrison, the matrix determinant lemma, minimum-norm interpolation and leverage-style rank-one diagnostics are classical finite-dimensional linear algebra. The line-specific contribution here is their application to the genuine finite-section penalty isolated in `NB-284/285`, producing the exact target-aware telescoping criterion `(4)`--`(10)` for successive legal Dirichlet enrichment.

A fresh prior-art search on 2026-09-22 found adjacent work on Nyman--Beurling Gram structure and compressibility, including Hugh Carvill's 2025 analysis of polynomial off-diagonal Gram decay. That work concerns generator-Gram geometry; it does not supply the constrained target-aware rank-one synthesis recursion derived here. No external result is load-bearing for the proof, so `SOURCES.md` does not require a new dependency.

---

## 7. Next decisive test

For an explicit moving packet family `Z_X`, choose the legal cutoff `M_X` and orthogonalize the quotient-source atoms beyond it. Compute or bound

\[
\ell_{X,r}
=
v_{X,r+1}^*K_{X,r}^{-1}v_{X,r+1}
\tag{47}
\]

and

\[
\beta_{X,r}
:=
\frac{|v_{X,r+1}^*K_{X,r}^{-1}y_X|^2}
{\mathcal C_{X,r}\,
 v_{X,r+1}^*K_{X,r}^{-1}v_{X,r+1}}
\in[0,1],
\tag{48}
\]

with `beta=0` when the denominator vanishes. Then

\[
\alpha_{X,r}
=
\beta_{X,r}\frac{\ell_{X,r}}{1+\ell_{X,r}}.
\tag{49}
\]

The decisive upper-route target is

\[
\sum_{r\ge M_X}\alpha_{X,r}=o(1),
\tag{50}
\]

which closes the relative finite-section obstruction. The decisive lower-route target is a packet family for which the logarithmic budget in `(39)` remains bounded below while the already-separated global-zero and infinite-source-space penalties from `NB-284` are controlled independently.

Either outcome would be stronger than another condition-number estimate: it would price exactly the future arithmetic directions that can still change the required first-free datum.

---

## Provenance

- Re-derived from the current default branch on 2026-09-22 after reading `AGENTS.md`, the Mathia Research Watch skill, its review/representation/clue companions, the current Nyman--Beurling README, research-line mind, clues, recent findings and recent commits.
- Immediate technical parents: `NB-282`, `NB-284`, `NB-285`.
- Fresh prior-art audit performed before publication; no new load-bearing source dependency identified.
- Adversarial self-review checked the positive-definite threshold, complex rank-one inverse formula, fixed-versus-moving packet quantifiers, target normalization, and the distinction between leverage and target alignment.
- Representation decision: no `mind/**` update. The result sharpens the active synthesis-cost diagnostic but does not yet change the durable research-line strategy or establish an arithmetic estimate.
- Clue decision: no clue status change. The result narrows the quantitative target-aware finite-section problem but does not resolve the surviving asymptotic question.
