# NB-294 — off-critical dilation uniformly coerces multiplicative-band sampling

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-284, NB-292, NB-293
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + FIRST-FREE-SAMPLING + OFF-CRITICAL-DILATION + MULTIPLICATIVE-QUOTIENT-BAND + LOEWNER-COERCIVITY + TARGET-UNIFORM-SATURATION + MOVING-PACKET-GATE + RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-293` reduces the target-aware gain from the canonical multiplicative band to the whitened positive matrix

\[
M_{m,n,Z}
=
A_{m,n,Z}^{-1/2}\Gamma_{m,n,Z}A_{m,n,Z}^{-1/2},
\]

where

\[
A_{m,n,Z}
=
D_Z(m)K_{n-1,Z}D_Z(m)^*,
\qquad
\Gamma_{m,n,Z}
=
K_{mn-1,Z}-A_{m,n,Z},
\]

and

\[
D_Z(m)
=
\operatorname{diag}
\bigl(m^{1/2-\rho_1},\ldots,m^{1/2-\rho_N}\bigr).
\]

The open question after `NB-293` is whether the actual transformed datum can miss the positive spectrum of `M`. For a **fixed finite packet strictly inside the Hardy half-plane**, it cannot once the multiplicative dilation is large enough. The off-critical displacement itself forces a uniform spectral floor.

Fix

\[
Z=\{\rho_1,\ldots,\rho_N\}
\subset\{\Re s>1/2\}
\]

and a section `n` beyond the first-free surjective cutoff, so

\[
K:=K_{n-1,Z}\succ0.
\]

Put

\[
\delta_Z
:=
\min_j\left(\Re\rho_j-\frac12\right)>0,
\qquad
\kappa_Z(n)
:=
\frac{\lambda_{\max}(K)}{\lambda_{\min}(K)},
\]

and define the dimensionless dilation-to-conditioning ratio

\[
\boxed{
R_{m,n,Z}
:=
\frac{m^{2\delta_Z}}{\kappa_Z(n)}.
}
\tag{1}
\]

Then the actual canonical band satisfies the Loewner lower bound

\[
\boxed{
K_{mn-1,Z}
\succeq
R_{m,n,Z}\,A_{m,n,Z}.
}
\tag{2}
\]

Equivalently,

\[
\boxed{
\Gamma_{m,n,Z}
\succeq
\bigl(R_{m,n,Z}-1\bigr)A_{m,n,Z}.
}
\tag{3}
\]

Since `Gamma` is independently positive semidefinite by `NB-292`, the useful form is

\[
\boxed{
M_{m,n,Z}
\succeq
\bigl(R_{m,n,Z}-1\bigr)_+ I.
}
\tag{4}
\]

Thus every generalized band eigenvalue diverges for fixed `Z,n` as `m -> infinity`.

For any nonzero first-free datum `y`, let

\[
\mathcal C_U(m;y)
:=
y^*A_{m,n,Z}^{-1}y
\]

be the minimum synthesis cost in the dilated old section `S_mV_(n-1,Z)`, and

\[
\mathcal C_V(m;y)
:=
y^*K_{mn-1,Z}^{-1}y
\]

be the minimum cost in the enlarged canonical section. Then

\[
\Delta_{m,n,Z}(y)
=
\mathcal C_U(m;y)-\mathcal C_V(m;y)
\]

from `NB-293`, and `(2)` gives the target-uniform estimate

\[
\boxed{
\frac{\mathcal C_V(m;y)}{\mathcal C_U(m;y)}
\le
\min\left\{1,\frac1{R_{m,n,Z}}\right\}.
}
\tag{5}
\]

Therefore

\[
\boxed{
\frac{\Delta_{m,n,Z}(y)}{\mathcal C_U(m;y)}
\ge
\left(1-\frac1{R_{m,n,Z}}\right)_+
=
\left(1-\kappa_Z(n)m^{-2\delta_Z}\right)_+.
}
\tag{6}
\]

In particular, for every fixed off-critical packet and every fixed surjective lower section,

\[
\boxed{
\inf_{y\ne0}
\frac{\Delta_{m,n,Z}(y)}{\mathcal C_U(m;y)}
\longrightarrow1
\qquad(m\to\infty).
}
\tag{7}
\]

This is stronger than a lower bound on one canonical defect pairing: asymptotically **no target direction can avoid the multiplicative quotient band**.

The moving-packet version isolates the remaining quantitative gate. For a family `(Z_X,n_X,m_X)`, define

\[
\delta_X
=
\min_{\rho\in Z_X}
\left(\Re\rho-\frac12\right),
\qquad
\kappa_X
=
\kappa\bigl(K_{n_X-1,Z_X}\bigr).
\]

If

\[
\boxed{
2\delta_X\log m_X-\log\kappa_X
\longrightarrow+\infty,
}
\tag{8}
\]

then `R_X -> infinity`, and the gain saturates uniformly over **all** nonzero first-free data:

\[
\boxed{
\sup_{y\ne0}
\frac{\mathcal C_V(m_X;y)}{\mathcal C_U(m_X;y)}
\longrightarrow0.
}
\tag{9}
\]

Thus the target-occupation problem from `NB-293` is automatic whenever off-critical dilation amplification beats the conditioning of the lower first-free sampling Gram. What remains open at Ford scales is precisely whether this gate survives when the packet moves, its minimum horizontal displacement may shrink, the packet rank grows, and the relevant lower-section conditioning may deteriorate.

---

## 1. Off-critical evaluation contracts the dilated old sampling Gram

Write

\[
\beta_j:=\Re\rho_j,
\qquad
\delta_j:=\beta_j-\frac12>0.
\]

The diagonal covariance satisfies

\[
|D_Z(m)_{jj}|
=
m^{-\delta_j},
\]

so

\[
\boxed{
\|D_Z(m)\|=m^{-\delta_Z}.
}
\tag{10}
\]

For every `u in C^N`,

\[
\begin{aligned}
u^*A_{m,n,Z}u
&=(D_Z(m)^*u)^*K(D_Z(m)^*u)\\
&\le
\lambda_{\max}(K)\|D_Z(m)^*u\|^2\\
&\le
\lambda_{\max}(K)m^{-2\delta_Z}\|u\|^2.
\end{aligned}
\]

Hence

\[
\boxed{
A_{m,n,Z}
\preceq
\lambda_{\max}(K)m^{-2\delta_Z}I.
}
\tag{11}
\]

This is the source of coercivity: the same fixed first-free sample coordinates are exponentially contracted in `log m` when transported by the Hardy dilation through a point with `Re rho>1/2`.

---

## 2. Canonical nestedness supplies a noncontracting floor

The quotient sections are nested in their ordinary cutoff:

\[
V_{n-1,Z}\subseteq V_{mn-1,Z}.
\]

Therefore their sampling Grams satisfy

\[
K_{mn-1,Z}\succeq K.
\tag{12}
\]

Since

\[
K\succeq\lambda_{\min}(K)I,
\]

combine `(11)` and `(12)` to obtain

\[
\begin{aligned}
R_{m,n,Z}A_{m,n,Z}
&\preceq
\frac{m^{2\delta_Z}}{\kappa_Z(n)}
\lambda_{\max}(K)m^{-2\delta_Z}I\\
&=
\lambda_{\min}(K)I\\
&\preceq K\\
&\preceq K_{mn-1,Z}.
\end{aligned}
\]

This proves `(2)`. Subtracting `A` gives `(3)`, and conjugating by `A^(-1/2)` gives

\[
M_{m,n,Z}\succeq(R_{m,n,Z}-1)I.
\]

Together with `M >= 0`, this proves `(4)`.

The argument uses both structures isolated in `NB-292`: the exact diagonal covariance of first-free samples under the **same** Hardy dilation and the inclusion of the dilated old section inside the larger canonical section. A synthetic model that only reproduces the raw zero-sample table or the scalar pivot profile need not satisfy this comparison.

---

## 3. The whole target spectrum becomes occupied

Because

\[
K_{mn-1,Z}=A_{m,n,Z}+\Gamma_{m,n,Z},
\]

`NB-293` writes

\[
\mathcal C_U(m;y)
=
\|x\|^2,
\qquad
x=A_{m,n,Z}^{-1/2}y,
\]

and

\[
\Delta_{m,n,Z}(y)
=
x^*M(I+M)^{-1}x.
\tag{13}
\]

If `R>=1`, `(4)` implies

\[
I+M\succeq RI,
\]

hence

\[
(I+M)^{-1}\preceq R^{-1}I.
\]

Using

\[
M(I+M)^{-1}=I-(I+M)^{-1},
\]

we obtain

\[
\Delta_{m,n,Z}(y)
\ge
(1-R^{-1})\|x\|^2.
\]

For `R<1`, positivity gives the trivial lower bound zero. This proves `(6)`.

Equivalently, inversion of `(2)` gives directly

\[
K_{mn-1,Z}^{-1}
\preceq
R^{-1}A_{m,n,Z}^{-1}
\]

when `R>0`; together with `K_(mn-1,Z)>=A` from `Gamma>=0`, this yields `(5)`.

The important point is that this is **uniform in `y`**. The target-miss stress test in `NB-293` — a large positive band whose spectrum sits orthogonal to the datum — remains valid for arbitrary positive matrices, but cannot persist at fixed off-critical `Z,n` once the actual dilation covariance makes `A` small compared with the nested canonical Gram floor.

---

## 4. Fixed packets and moving packets are qualitatively different

For fixed `Z` and fixed surjective `n`, both `delta_Z>0` and `kappa_Z(n)<infinity` are constants. Therefore

\[
R_{m,n,Z}
=
\frac{m^{2\delta_Z}}{\kappa_Z(n)}
\longrightarrow\infty,
\]

which proves `(7)`.

At a moving packet the same argument exposes rather than removes the hard part. Writing

\[
R_X
=
\exp\bigl(
2\delta_X\log m_X-\log\kappa_X
\bigr),
\]

shows exactly what must be paid. A displacement `delta_X` approaching zero can neutralize polynomial or even larger multiplicative growth, and a growing sampling condition number can erase the same gain. The sufficient condition `(8)` is therefore a true scale-coupled gate, not a fixed-packet compactness statement.

For a desired relative gain `eta in (0,1)`, `(6)` gives the explicit sufficient threshold

\[
\boxed{
R_{m,n,Z}\ge\frac1{1-\eta}
\quad\Longrightarrow\quad
\Delta_{m,n,Z}(y)
\ge
\eta\,\mathcal C_U(m;y)
\quad\text{for every }y.
}
\tag{14}
\]

No target alignment estimate is then needed. Conversely, failure of `(8)` does **not** prove the gain is small; it only says this uniform Loewner route no longer forces it. Target-specific spectral occupation or the canonical pairing from `NB-293` can still succeed below the uniform threshold.

---

## 5. Adversarial checks and scope boundaries

### This is not a Nyman-distance decrement from `V_(n-1)` to `V_(mn-1)`

The baseline cost in `(6)` is the cost of realizing the **same** first-free datum inside the dilated subspace

\[
S_mV_{n-1,Z},
\]

not inside the ordinary old section `V_(n-1,Z)`. For an off-critical packet this dilated realization becomes expensive precisely because point evaluation contracts by `m^(1/2-rho)`. The theorem says that the canonical multiplicative band repairs almost all of that dilation-induced cost. It does not by itself bound the original Nyman approximation distance or the finite-section excess `mathfrak A_(n-1)`.

### Critical-line points correctly remove the mechanism

If one formally allows `delta_Z=0`, then

\[
R_{m,n,Z}=\kappa_Z(n)^{-1}\le1,
\]

and `(6)` supplies no positive fraction. This is expected: `|m^(1/2-rho)|=1` on the critical line, so the diagonal sample contraction used in `(11)` disappears.

### Bad lower-section conditioning is paid explicitly

No hidden uniform conditioning is assumed. If `kappa_Z(n)` grows as fast as, or faster than, `m^(2 delta_Z)`, the bound can be vacuous. This is exactly the moving-packet failure mode left open by `NB-288`--`NB-293`.

### The canonical one-vector defect need not carry the gain

`NB-293` gives the sufficient certificate based on

\[
|d_{m,n,Z}^*A^{-1}y|.
\]

The present theorem does not lower-bound that particular pairing. It lower-bounds the **entire** whitened band. The gain can be distributed among other directions in the null block `Q_(m,n,Z)` even if the singled-out canonical defect direction is nearly target-orthogonal.

### No contradiction follows from a fixed hypothetical off-critical zero

A fixed off-critical packet makes the relative band gain tend to one, but the old dilated synthesis cost itself grows. There is no conservation law here forcing the canonical cost negative or forcing the Nyman distance to vanish. The statement is a coercivity theorem for the multiplicative interpolation enrichment, not a proof or disproof of RH.

---

## 6. Prior-art audit and research disposition

A fresh search checked the classical Hardy/Nyman semigroup background represented by Bagchi's 2006 survey and the recent multiplicative-ladder Gram work of Carvill (2025), as well as modern generalized Nyman approximation work. The surfaced literature treats the Hilbert-space criterion, dilation structure, and multiplicative Gram decay, but did not surface this line-local finite-section Loewner comparison between the contracted first-free Gram `D K D^*` and the nested canonical Gram `K_(mn-1)`.

No external theorem is load-bearing. Equations `(2)`--`(9)` follow from the exact covariance and band identities already proved in `NB-292`--`NB-293`, nestedness of the canonical sections, and elementary spectral order. Therefore `SOURCES.md` needs no update.

The result changes the immediate diagnostic but not the durable moving-packet frontier enough to rewrite `mind/**`: target occupation is now automatic above the explicit gate `(8)`, while the unresolved Ford-scale question remains whether actual packet displacement and source conditioning cross that gate, or whether a target-specific estimate survives when they do not.

The next decisive calculation should therefore track

\[
\boxed{
\mathcal R_X
:=
2\delta_X\log m_X-
\log\kappa\bigl(K_{n_X-1,Z_X}\bigr).
}
\tag{15}
\]

If `mathcal R_X -> +infinity`, the multiplicative-band target problem is closed uniformly by `(9)`. If it stays bounded above, further progress must use finer packet-dependent spectral occupation, the canonical defect pairing from `NB-293`, or a stronger source-metric estimate than the condition-number comparison used here.
