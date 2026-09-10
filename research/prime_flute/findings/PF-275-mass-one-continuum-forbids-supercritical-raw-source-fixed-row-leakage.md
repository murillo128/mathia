# PF-275 — mass-one continuum forbids every supercritical raw-source fixed-row leakage exponent

**Status:** `EXACT-DERIVED + FIXED-ROW-LOW-LEAKAGE-OBSTRUCTION + MASS-ONE-CONTINUUM + ROBIN-NORMALIZATION-BOTTLENECK`.

[[research/prime_flute/findings/PF-273-seam-square-root-is-a-complete-bernstein-green-continuum-with-mass-one-edge|PF-273]] identifies the exact positive Green continuum of the fixed-axis square-root source

\[
X_w=s^{-1/2}A^{-1/4}g_w(L),
\qquad
g_w(\lambda)=\sqrt{\sqrt\lambda\tanh(w\sqrt\lambda)},
\qquad w=rs,
\tag{1}
\]

and shows that its representing masses reach the critical edge `\mu(t)=\sqrt{1+t}\downarrow1`. PF-273 deliberately stopped short of a block exponent because integrating PF-264's two-moving-index asymptotic through the shrinking boundary layer `t\log(j/i)=O(1)` would require small-mass uniformity.

That uniform boundary-layer theorem is **not needed to decide whether the raw source can have any PF-271-compatible exponent `q>1`**. To refute a proposed `q>1`, choose a sufficiently small but fixed positive mass slice after `q` is specified. Positivity of the Green continuum and monotonicity of the negative-point resolvent then transfer PF-262's fixed-mass, fixed-source tail directly into a lower bound.

The result is sharp at the level of smoothing exponents:

\[
\boxed{
\text{for every fixed low parity row }i_0\text{ and every }q>1,
\qquad
N^q\,\|P_{i_0}X_wE_N\|\longrightarrow\infty.
}
\tag{2}
\]

Here `E_N` is a high shell in one PF-247 parity chain and `P_{i_0}` is the rank-one projection onto the fixed output mode `f_{i_0}=e_{2i_0+\varepsilon}`. Consequently every larger low-output window containing that mode — polynomial, logarithmic, or fixed — also fails every `O(N^{-q})` estimate with `q>1`.

Thus the raw square-root source itself cannot satisfy the sufficient leakage hypothesis in PF-271 for any `R>1`. The only remaining fixed-axis escape in the accepted Robin clue is genuinely the noncommuting normalization

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w.
\tag{3}
\]

If `B_w` succeeds, the left rational factor must create the entire supercritical gain; it cannot merely preserve a margin already present in `X_w`.

## Claim

Fix `r,s>0`, put `w=rs`, and fix a parity `\varepsilon\in\{0,1\}`. Write

\[
f_j=e_{2j+\varepsilon},
\qquad
E_N=\sum_{N\le j<2N}|f_j\rangle\langle f_j|,
\qquad
P_i=|f_i\rangle\langle f_i|.
\tag{4}
\]

For every fixed `i\ge0` and every `q>1`, there are `c_q>0`, `\mu_q\in(1,q)`, and `N_q` such that

\[
\boxed{
\|P_iX_wE_N\|\ge c_qN^{-\mu_q}
\qquad(N\ge N_q).
}
\tag{5}
\]

In particular,

\[
\boxed{
N^q\|P_iX_wE_N\|\to\infty
\qquad(q>1).
}
\tag{6}
\]

Therefore, if `F_N` is any family of output projections with `P_i\le F_N` for all sufficiently large `N`, then

\[
\|F_NX_wE_N\|\ne O(N^{-q})
\qquad\text{for every }q>1.
\tag{7}
\]

This applies in particular to PF-271's `N^\theta` low-output window for every `0<\theta<1`, to its logarithmic window `A\log N`, and even to a fixed nonzero low-output window.

At fixed `s`, replacing parity index shells by the fixed-axis scale `K_s^0=sA^{1/2}` changes only constants because `K_s^0f_j=s\kappa_{2j+\varepsilon}f_j\asymp s(j+1)f_j`.

## 1. A fixed positive mass slice is enough

PF-273 gives the complete-Bernstein representation

\[
g_w(L)=\int_0^\infty L(L+t)^{-1}\,\nu_w(dt),
\tag{8}
\]

with absolutely continuous positive measure whose first support interval is

\[
0<t<\left(\frac{\pi}{2w}\right)^2
\tag{9}
\]

and whose density is strictly positive there. For distinct same-parity modes,

\[
\langle f_i,g_w(L)f_j\rangle
=-\int_0^\infty t\,G_t(i,j)\,\nu_w(dt),
\qquad
G_t(i,j):=\langle f_i,(L+t)^{-1}f_j\rangle>0.
\tag{10}
\]

Fix any target exponent `q>1`. Choose a nonresonant `t_2>0` so small that

\[
\mu_2:=\sqrt{1+t_2}<q,
\qquad
2\mu_2\notin\mathbb N,
\qquad
t_2<\left(\frac{\pi}{2w}\right)^2,
\tag{11}
\]

and put `t_1=t_2/2`. Such a choice always exists because the continuum reaches `t=0` and the resonant masses are discrete. Define

\[
m_I:=\int_{t_1}^{t_2} t\,\nu_w(dt)>0.
\tag{12}
\]

No parameter in this interval will move with `N`.

## 2. Green positivity makes the slice a lower bound

For `0<t\le t_2`, the resolvent identity gives

\[
(L+t)^{-1}-(L+t_2)^{-1}
=(t_2-t)(L+t)^{-1}(L+t_2)^{-1}.
\tag{13}
\]

In the PF-247 parity Jacobi gauge the massive Green kernels are entrywise positive. Hence the matrix entries of the product on the right of (13) are nonnegative, and therefore

\[
G_t(i,j)\ge G_{t_2}(i,j).
\tag{14}
\]

Using (10)--(12), for every `j\ne i`,

\[
\boxed{
-\langle f_i,g_w(L)f_j\rangle
\ge m_I\,G_{t_2}(i,j).
}
\tag{15}
\]

This is the key quantifier change. A sharp asymptotic of the whole `t\downarrow0` continuum is unnecessary: each forbidden exponent `q>1` is witnessed by one fixed positive slice lying below the corresponding mass threshold.

## 3. PF-262 converts the slice into critical-envelope shell leakage

PF-262 applies to the fixed nonresonant mass `a=\sqrt{t_2}`. For every fixed source/output row `i`,

\[
G_{t_2}(i,j)
=C_{i,\varepsilon}(t_2)
 j^{-1/2-\mu_2}(1+O(j^{-1})),
\qquad j\to\infty.
\tag{16}
\]

The coefficient is positive: the Green kernel is positive and the nonzero resolvent column selects the recessive solution. Thus, after enlarging `N_q`,

\[
-\langle f_i,g_w(L)f_j\rangle
\ge c\,j^{-1/2-\mu_2}
\qquad(N\le j<2N).
\tag{17}
\]

The left `A^{-1/4}` factor in (1) is a **fixed constant on the fixed output row**:

\[
A^{-1/4}f_i=\kappa_{2i+\varepsilon}^{-1/2}f_i.
\tag{18}
\]

Therefore

\[
|\langle f_i,X_wf_j\rangle|
\ge c'j^{-1/2-\mu_2}.
\tag{19}
\]

Since `P_iX_wE_N` has rank-one output, its operator norm is exactly the `\ell^2` norm of that row on the shell:

\[
\begin{aligned}
\|P_iX_wE_N\|^2
&=\sum_{N\le j<2N}|\langle f_i,X_wf_j\rangle|^2\\
&\ge c'^2\sum_{N\le j<2N}j^{-1-2\mu_2}
\gtrsim N^{-2\mu_2}.
\end{aligned}
\tag{20}
\]

This proves (5). Because `q-\mu_2>0`, multiplying by `N^q` gives (6).

## 4. Consequence for the PF-271 gate

PF-271 asks the **normalized** pre-propagation conversion to obey, for some exponent strictly larger than one, a high-input to low-output block estimate. Equation (7) proves that the unnormalized source `X_w` cannot do this even on one fixed output row. Enlarging the output projector to `N^\theta` or `A\log N` cannot improve the norm.

This is stronger than the heuristic statement that the continuum has `\inf\mu=1`. It shows that the mass-one edge is operationally visible in the exact PF-271 currency without proving a uniform shrinking-mass Green asymptotic. At the same time it does **not** decide the actual gate, because PF-257 identifies the physical fixed-axis source as

\[
B_w=(I+\mathcal R^0_{s,r})^{-1}X_w,
\qquad
\mathcal R^0_{s,r}=X_wX_w^*.
\tag{21}
\]

The left factor is noncommuting in the corridor basis and may reorganize low-output transfer. The remaining question is therefore not whether the raw source has a hidden strict exponent — it does not — but whether the normalization produces a threshold cancellation absent from `X_w`.

A useful exact row reformulation is

\[
B_w^*f_i
=X_w^*(I+\mathcal R^0_{s,r})^{-1}f_i
=s^{-1/2}g_w(L)A^{-1/4}(I+\mathcal R^0_{s,r})^{-1}f_i.
\tag{22}
\]

Thus any fixed-row supercritical estimate for `B_w` must come from the special normalized source vector

\[
z_i:=A^{-1/4}(I+\mathcal R^0_{s,r})^{-1}f_i,
\tag{23}
\]

not from generic smoothing of `g_w(L)`. PF-274's continuous-Hahn transform gives a natural representation in which to test whether `z_i` cancels the branch contribution at the mass-one threshold.

## 5. Prior art and novelty audit

The ingredients are classical or already audited in the preceding findings. PF-262 uses the Birkhoff--Adams/Wong--Li theory recorded in NIST DLMF §2.9(ii) and the standard Weyl/Green theory for Jacobi operators. PF-273 uses the complete-Bernstein/Stieltjes calculus of R. L. Schilling, R. Song and Z. Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed. (De Gruyter, 2012), together with positivity of the PF parity Green kernels. Equation (13) is the standard resolvent identity.

A targeted search also checked the continuous-Hahn asymptotic literature exposed by PF-274. L.-H. Cao, Y.-T. Li and Y. Lin, *Asymptotic approximations of the continuous Hahn polynomials and their zeros*, Journal of Approximation Theory 247 (2019), 32--47, DOI `10.1016/j.jat.2019.07.001`, develops large-degree continuous-Hahn asymptotics but does not supply this Prime-Flute fixed-row Stieltjes-slice lower bound or remove the normalization in (21).

No novelty is claimed for resolvent monotonicity, positive Green kernels, complete Bernstein representations, or fixed-mass Jacobi asymptotics. The project-specific contribution is the **quantifier argument** combining them: because PF-273's positive measure reaches every sufficiently small fixed mass, every candidate exponent `q>1` can be defeated by choosing one nonresonant fixed slice with `1<\sqrt{1+t_2}<q`. This converts the structural mass-one edge into an exact obstruction in PF-271's operator-block currency without any shrinking-mass interchange.

## 6. Boundaries and adversarial checks

1. **Raw source only.** The theorem applies to `X_w`, not to the normalized source `B_w`. It does not prove that the Robin route fails.
2. **No sharp critical asymptotic.** The mass slice depends on the tested exponent `q`. Equations (5)--(6) exclude every strict exponent above one but do not prove `\|P_iX_wE_N\|\asymp N^{-1}` or determine logarithmic corrections.
3. **No shrinking-mass interchange.** The proof intentionally avoids integrating PF-264 through `t\sim1/\log N`; `t_1,t_2` are fixed before `N\to\infty`.
4. **Fixed seam parameters.** Constants depend on `r,s,i,q` and parity. No corridor-index, homotopy, shear, or canonical-tail uniformity is asserted.
5. **Nonresonant witness is enough.** PF-262's displayed fixed-source theorem is nonresonant, and the continuum contains arbitrarily small nonresonant masses. Resonant masses need not be controlled for this obstruction.
6. **Parity is not a loophole.** One same-parity fixed row suffices to lower-bound the full low-output block norm; opposite-parity vanishing does not help.
7. **No global conclusion.** Nothing here proves the PF-243 weak-trace target, scattering/determinant control, prime/control separation, a zeta-zero statement, or RH.

The finding is falsified if the PF-273 Stieltjes representation fails to have positive measure on arbitrarily small positive masses, if the massive parity Green kernel is not positive/monotone in the resolvent parameter, or if PF-262's fixed-source recessive coefficient can vanish at the chosen negative resolvent point. The persisted identities and positivity statements rule out those failure modes under the stated fixed-axis hypotheses.

## Decisive next test

Do **not** spend the next pass proving a sharp raw-`X_w` boundary-layer asymptotic merely to decide whether `X_w` has `R>1` leakage; (6) has already answered that negatively. Attack the normalized row (22) directly.

Use PF-274's continuous-Hahn transform, or an equivalent Green formulation, to determine whether the special vector `z_i` in (23) forces cancellation of the `\xi=\pm i` / `\mu=1` threshold contribution. A nonzero threshold coefficient for one fixed row would propagate the present obstruction through `(I+\mathcal R^0_{s,r})^{-1}` and kill the PF-271 route. A zero of sufficient order would identify the exact mechanism by which the Robin normalization creates the otherwise absent supercritical margin. Only after that fixed-axis discriminator is settled should the route spend effort on PF-255/PF-256 transport and canonical-tail uniformity.