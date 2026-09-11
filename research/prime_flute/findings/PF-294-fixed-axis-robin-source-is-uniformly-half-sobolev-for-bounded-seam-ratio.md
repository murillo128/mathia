# PF-294 — fixed-axis Robin source is uniformly half-Sobolev for bounded seam ratio

**Status:** `EXACT-DERIVED + UNIFORM-FRACTIONAL-REGULARITY + NEGATIVE/ROUTE-NARROWING`.

PF-293 proves that, for each fixed Robin/seam parameter pair, the normalized fixed-axis source column has exactly one `K_0=A^{1/2}` derivative and no uniformly stronger fixed-parameter conclusion. Its explicit caveat is the one now relevant to PF-292: the Sobolev norm might still grow with the thin-seam parameters, so parameter variation could in principle generate the local frequency escape needed by the PF-290 shorting deficit.

That escape does **not** occur inside the bounded-ratio fixed-axis source family. PF-276's inverse-positive Robin normalization has an exact conserved positive first moment. Because PF-247's compactified operator `L` is parity-banded relative to the `A` eigenbasis, that moment gives a parameter-uniform `L^{3/4}` bound on the pre-seam vector. The exact finite-seam multiplier can then spend at most one half derivative when `w=rs`, uniformly as `s\downarrow0` provided `r` stays bounded.

More precisely, for every fixed source row and every `r_*<\infty`, the physical fixed-axis source

\[
y_{s,r}=B_{rs}^*\varphi_i
=s^{-1/2}g_{rs}(L)z_{s,r}
\]

is uniformly bounded in `H^{1/2}(\mathbb R_\tau)` under PF-247's exact complete-axis compactification, simultaneously for all `s>0` and `0<r\le r_*`. Thus shrinking the seam scale at bounded `w/s` cannot by itself produce PF-292's required loss of every positive local Sobolev bound. Any surviving frequency escape in the full normalized mixed response must enter through an ingredient not controlled by this fixed-axis column: an unbounded seam ratio, mixed/global Schur reassembly, neighboring-cell coupling, support migration/end completion, or another normalization effect.

This is a **component theorem**, not a theorem for PF-292's full `G_{n,r}`. It therefore narrows the accepted heavy-angle clue without closing it.

## Claim

Work in one parity sector and use PF-276's notation

\[
\varphi_j=e_{2j+\varepsilon},
\qquad
A\varphi_j=\kappa_j^2\varphi_j,
\qquad
D=A^{-1/4},
\tag{1}
\]

with fixed source index `i`. For `s,r>0`, put `w=rs` and

\[
R_{s,r}=s^{-1}D f_w(L)D,
\qquad
u_{s,r}:=(I+R_{s,r})^{-1}\varphi_i,
\qquad
z_{s,r}:=D\nu_{s,r},
\tag{2}
\]

where

\[
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\qquad
g_w=f_w^{1/2}.
\tag{3}
\]

Let

\[
y_{s,r}:=B_w^*\varphi_i
=s^{-1/2}g_w(L)z_{s,r}
\tag{4}
\]

be PF-276/PF-257's normalized fixed-axis source. Then:

1. there is a constant `C_i`, independent of `s,r`, such that
   \[
   \boxed{\|A^{3/4}z_{s,r}\|_2\le C_i;}
   \tag{5}
   \]
2. PF-247's exact parity-banded relation implies
   \[
   \boxed{LA^{-1}\in\mathcal B(L^2),}
   \tag{6}
   \]
   hence, for every `0\le\theta\le1`,
   \[
   \boxed{
   \operatorname{Dom}(A^\theta)\hookrightarrow\operatorname{Dom}(L^\theta),
   \qquad
   \|L^\theta x\|_2\le C_\theta\|A^\theta x\|_2;
   }
   \tag{7}
   \]
3. consequently
   \[
   \boxed{\sup_{s,r>0}\|L^{3/4}z_{s,r}\|_2<\infty;}
   \tag{8}
   \]
4. for every `r_*<\infty` and every `0\le\sigma\le1/2`,
   \[
   \boxed{
   \sup_{s>0,\ 0<r\le r_*}
   \|L^{\sigma/2}y_{s,r}\|_2<\infty.
   }
   \tag{9}
   \]

Under PF-247's exact unitary compactification

\[
L=U(1-\partial_\tau^2)U^*,
\tag{10}
\]

equation (9) is exactly

\[
\boxed{
\sup_{s>0,\ 0<r\le r_*}
\|U^*y_{s,r}\|_{H^\sigma(\mathbb R_\tau)}<\infty,
\qquad 0\le\sigma\le\frac12.
}
\tag{11}
\]

In particular the bounded-ratio source family has a uniform positive Sobolev margin. No uniform `H^1`, uniform `K_0`-derivative bound, or result for unbounded `r` is asserted.

## 1. PF-276's conserved positive mass gives a uniform `A^{3/4}` bound

PF-276 proves coefficientwise positivity

\[
\nu_{s,r,j}>0
\tag{12}
\]

and the exact weighted conservation law

\[
\sum_{j\ge0}q_j\nu_{s,r,j}=q_i,
\qquad
q_j=\kappa_j^{1/2}c_j,
\qquad
q_j\asymp\kappa_j.
\tag{13}
\]

The sequence `q_j/\kappa_j` is fixed by the parity chain, strictly positive, and tends to a positive constant. Hence there is `c>0`, independent of `s,r`, such that

\[
q_j\ge c\kappa_j
\qquad(j\ge0).
\tag{14}
\]

Using positivity in (13),

\[
\sum_j\kappa_j\nu_{s,r,j}
\le c^{-1}q_i.
\tag{15}
\]

Since `z_j=\kappa_j^{-1/2}\nu_j`,

\[
\begin{aligned}
\|A^{3/4}z_{s,r}\|_2^2
&=\sum_j\kappa_j^3|z_{s,r,j}|^2\\
&=\sum_j\kappa_j^2\nu_{s,r,j}^2\\
&\le\left(\sum_j\kappa_j\nu_{s,r,j}\right)^2.
\end{aligned}
\tag{16}
\]

Equations (15)--(16) prove (5). This is the parameter-uniform information that PF-293's fixed-parameter coefficient asymptotic did not spend.

The exponent `3/4` is natural for this argument: conservation controls the `\ell^1` first moment `\sum\kappa_j\nu_j`, and after the `A^{-1/4}` factor this becomes exactly the endpoint `A^{3/4}` square norm in (16). No stronger exponent follows from this moment alone.

## 2. PF-247's banded compactification transfers three-quarter graph regularity from `A` to `L`

PF-247 gives

\[
J=A^{-1/2}LA^{-1/2}
\tag{17}
\]

and proves that `J` is bounded and parity tridiagonal in the `A` eigenbasis: `J_{mn}=0` unless `m=n` or `m=n\pm2`. On the finite modal core,

\[
LA^{-1}=A^{1/2}JA^{-1/2}.
\tag{18}
\]

Its matrix entries are

\[
(LA^{-1})_{mn}
=\frac{\kappa_m}{\kappa_n}J_{mn}.
\tag{19}
\]

Because only finitely many diagonals occur and the adjacent same-parity ratios `\kappa_{n\pm2}/\kappa_n` are uniformly bounded, the Schur test gives a bounded operator on `\ell^2`. Closure of `L` then upgrades the core identity to (6), equivalently

\[
\|Lx\|_2\le C\|Ax\|_2,
\qquad x\in\operatorname{Dom}(A).
\tag{20}
\]

Both `A` and `L` are strictly positive self-adjoint operators. Applying the classical Heinz--Kato fractional-domain interpolation theorem to the identity map between their graph scales gives (7). At `\theta=3/4`, (5) therefore yields (8).

This step uses more than the form comparison `L\lesssim A`: the target exponent is an operator power `3/4`, and the required graph embedding comes from PF-247's exact finite-band structure.

## 3. The finite-seam multiplier spends at most one half derivative at bounded ratio

By spectral calculus for `L` and (3)--(4), for `0\le\sigma\le1/2`,

\[
\begin{aligned}
\|L^{\sigma/2}y_{s,r}\|_2^2
&=s^{-1}
\int_0^\infty
\lambda^\sigma g_{rs}(\lambda)^2
\,d\mu_{z_{s,r}}(\lambda)\\
&=s^{-1}
\int_0^\infty
\lambda^{\sigma+1/2}
\tanh(rs\sqrt\lambda)
\,d\mu_{z_{s,r}}(\lambda).
\end{aligned}
\tag{21}
\]

The elementary bound `\tanh x\le x` for `x\ge0` gives

\[
\begin{aligned}
\|L^{\sigma/2}y_{s,r}\|_2^2
&\le r
\int_0^\infty
\lambda^{\sigma+1}
\,d\mu_{z_{s,r}}(\lambda)\\
&=r\,
\|L^{(\sigma+1)/2}z_{s,r}\|_2^2.
\end{aligned}
\tag{22}
\]

For `\sigma\le1/2`,

\[
\frac{\sigma+1}{2}\le\frac34,
\tag{23}
\]

so (7)--(8), strict positivity of `L`, and `r\le r_*` make the right side uniformly bounded. This proves (9). Equation (11) is then immediate from (10).

The mechanism is scale-exact. The prefactor `s^{-1/2}` in the normalized source is canceled by the small-argument estimate for `\tanh(rs\sqrt L)`, leaving only the bounded ratio `r=w/s`. Thus `s\to0` by itself cannot create the required roughness.

## 4. Consequence for the PF-292 frequency-escape gate

PF-292 says that the fixed-window high projection annihilates any normalized response family with a uniform positive local Sobolev bound. PF-293 had already shown that each fixed-parameter source column is regular, but left open whether its norm could blow up as the seam parameters vary.

Equations (9)--(11) close that loophole for the fixed-axis source whenever `r=w/s` remains bounded. Restriction from `H^{1/2}(\mathbb R_\tau)` to a fixed compact window is bounded, so this source component cannot send a nonvanishing fraction of its normalized mass to arbitrarily high local frequency solely through `s\downarrow0`.

This does **not** identify `y_{s,r}` with PF-292's complete mixed-response Riesz representative `G_{n,r}`. PF-279 shows that Schur reservoirs can change the effective local response, and the simultaneous one-cusp pant also contains neighboring-cell terms, physical `P/H` restrictions, variable-corridor/hypercycle transports, and end/cusp completion. The theorem only removes one candidate origin of roughness.

Accordingly, a future proof of frequency escape must locate the escaping mass outside the bounded-ratio fixed-axis column, or prove that the relevant physical seam ratio itself becomes unbounded. Conversely, if the remaining factors preserve any fraction of the `H^{1/2}` margin uniformly, PF-292 will kill the local shorting deficit.

## 5. Prior-art and novelty audit

The functional-analysis ingredients are classical. The fractional-domain step is an instance of Tosio Kato, *A generalization of the Heinz inequality*, Proceedings of the Japan Academy 37 (1961), 305--308, DOI `10.3792/pja/1195523678`: a bounded graph map between positive/self-adjoint operators interpolates to their fractional powers for exponents in `[0,1]`. Equivalent Hilbert-scale interpolation statements are standard in the Lions--Magenes framework.

The Schur test, spectral calculus, `\tanh x\le x`, and restriction of Sobolev functions to compact intervals are also standard. No novelty is claimed for any of them.

A targeted search did not locate the project-specific combination used here: PF-276's conserved positive Robin weight, PF-247's exact parity-banded compactification, and PF-276/PF-257's normalized seam multiplier producing a uniform half-Sobolev bound over a thin-seam parameter family. The contribution is the exact route-narrowing consequence for the Prime-Flute fixed-axis response, not a new general theorem in interpolation theory.

## 6. Falsification and boundary checks

1. **Fixed source row.** The constant depends on the chosen parity/source index `i`. No uniform estimate over a growing family of source rows or arbitrary linear combinations is proved.
2. **Bounded seam ratio is essential to this estimate.** Equation (22) carries a factor `r`. The theorem does not control `r\to\infty`.
3. **No full-response identification.** `y_{s,r}` is the fixed-axis normalized Robin source column, not the complete PF-290/PF-292 Riesz representative `G_{n,r}`.
4. **No contradiction with PF-293.** PF-293's sharp fixed-parameter statement concerns the `K_0=A^{1/2}` scale and shows exactly one derivative there. The present theorem gives a weaker but parameter-uniform `L`/physical-axis half derivative.
5. **No supercritical leakage claim.** Uniform `H^{1/2}` regularity is enough for PF-292's compactness falsifier but does not resurrect the PF-271 `R>1` leakage route killed by PF-278.
6. **No hidden commuting assumption.** The only transfer from `A` to `L` uses PF-247's exact banded matrix and graph interpolation; `A` and `L` are not assumed to commute.
7. **No global spectral conclusion.** Nothing here proves compactness of the heavy extension angle, weak trace class, scattering, a determinant identity, a zeta-zero statement, the critical line, or RH.

## Decisive next test

Return to the accepted variable-corridor/reservoir clue and derive the **complete** normalized fixed-window Riesz representative `G_{n,r}`. Use the present theorem to factor out the bounded-ratio fixed-axis Robin column rather than attributing possible roughness to its shrinking seam scale. The decisive question is whether the remaining simultaneous Schur/reassembly operator preserves any positive fraction of this Sobolev margin or instead creates a quantifiable moving-frequency component that survives PF-290's exact shorting formula.