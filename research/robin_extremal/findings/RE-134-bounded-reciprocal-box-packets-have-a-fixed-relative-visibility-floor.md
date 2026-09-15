# RE-134 — bounded reciprocal-box packets have a fixed-relative visibility floor

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + RECIPROCAL-BOX + BOUNDED-COMPLEXITY-VISIBILITY + MACROSCOPIC-WINDOW + REAL-PACKET-OBSERVABILITY + CONCENTRATION-COMPACTNESS-DICHOTOMY + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-133` shows that a growing reciprocal-scale cluster can hide a dominant subedge atom uniformly on a fixed-relative window. Its construction uses `2^j` atoms and a scaled cluster diameter that grows with `j`, and it notes that the growing microscopic complexity is load-bearing for that particular product mechanism.

The growth is not merely an artifact of the subset-product construction. **Any packet with uniformly bounded cardinality whose offsets remain inside one fixed reciprocal-scale box has a fixed visibility floor on a fixed-relative window.** Consequently, a full packet that hides a dominant atom must lose compactness in the scaled local zero configuration: cancellation must either use unbounded local cardinality or remain order-one outside every fixed reciprocal box that has bounded occupancy.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad 0<\kappa<\frac12,
\qquad R>0,
\qquad B\in\mathbb N.
\tag{1}
\]

For a positive-ordinate subedge coordinate

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\tag{2}
\]

use the finite-order coefficient law

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{3}
\]

Let `gamma_*>0` be fixed. For every sufficiently large `U`, choose a target

\[
\rho_0=\beta_0+i\gamma_0,
\qquad
\gamma_0\ge\gamma_*,
\tag{4}
\]

and let `C_U` be a finite multiset of positive-ordinate subedge coordinates containing `rho_0`, counted with multiplicity, such that

\[
\#C_U\le B,
\qquad
|\beta-\beta_0|\le\frac RU,
\qquad
|\gamma-\gamma_0|\le\frac RU
\quad(\rho\in C_U).
\tag{5}
\]

Define its real packet

\[
\mathcal S_{C_U,K}(u)
:=2\Re\sum_{\rho\in C_U}
a_{\rho,K}(u)e^{i\gamma u}.
\tag{6}
\]

Then there are constants `c_0>0` and `U_0`, depending only on the fixed parameters in (1) and on `gamma_*`, such that

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
c_0\,|a_{\rho_0,K}(U)|
}
\tag{7}
\]

for every `U>=U_0`.

No simplicity assumption is needed for (7). Coincident coordinates only strengthen the compactness argument below because the coefficient kernel gives them the same leading orientation. The theorem is also independent of any one-level zero-density estimate.

## 1. Reciprocal boxes compactify the local coefficient law

Write

\[
d_\rho:=\frac1{\rho(1-\rho)}.
\tag{8}
\]

Uniformly for

\[
x\in I_\kappa:=[1-\kappa,1],
\qquad u=Ux,
\tag{9}
\]

the bracket in (3) satisfies

\[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
=
d_\rho\left(1+O_K(U^{-1})\right).
\tag{10}
\]

Indeed, after division by `d_rho`, the `k`th correction is

\[
\frac{(-1)^k k!\rho}{u^k(1-\rho)^k},
\tag{11}
\]

and `|rho/(1-rho)|` is uniformly bounded on the fixed right-half strip once `gamma>=gamma_*/2`. The finitely many powers in (11) are therefore uniformly `O_K(U^-1)` in total.

The reciprocal box in (5) also gives

\[
\frac{d_\rho}{d_{\rho_0}}=1+O_{R,\sigma_0,\Theta,\gamma_*}(U^{-1}),
\tag{12}
\]

because the logarithmic derivative of `1/[rho(1-rho)]` is uniformly bounded on that region.

Introduce scaled offsets

\[
\lambda_{\rho,U}
:=U\bigl((\beta-\beta_0)+i(\gamma-\gamma_0)\bigr),
\tag{13}
\]

so that

\[
|\Re\lambda_{\rho,U}|\le R,
\qquad
|\Im\lambda_{\rho,U}|\le R.
\tag{14}
\]

After demodulating by the target carrier and factoring the target edge damping, the complex positive-frequency cluster becomes

\[
\sum_{\rho\in C_U}
a_{\rho,K}(Ux)e^{i\gamma Ux}
=
 e^{-(\Theta-\beta_0)Ux}
 d_{\rho_0}e^{i\gamma_0Ux}
 \left(P_U(x)+E_U(x)\right),
\tag{15}
\]

where

\[
P_U(x)
:=
\sum_{\rho\in C_U}
c_{\rho,U}e^{\lambda_{\rho,U}x},
\qquad
c_{\rho,U}:=\frac{d_\rho}{d_{\rho_0}},
\tag{16}
\]

and

\[
\sup_{x\in I_\kappa}|E_U(x)|\ll_{B,R,K}U^{-1}.
\tag{17}
\]

For large `U`, every `c_(rho,U)` lies in a fixed small disk around `1`; in particular

\[
\Re c_{\rho,U}\ge\frac12.
\tag{18}
\]

Thus a bounded reciprocal box converts the local Robin/CA packet into a compact family of bounded-term exponential polynomials whose leading coefficients all have the same orientation.

## 2. A bounded-term local exponential polynomial has a uniform L2 floor

There exists

\[
m=m(B,R,\kappa)>0
\tag{19}
\]

such that every polynomial of the form

\[
P(x)=\sum_{j=1}^{N}c_je^{\lambda_jx},
\qquad
1\le N\le B,
\tag{20}
\]

with

\[
|\Re\lambda_j|,|\Im\lambda_j|\le R,
\qquad
|c_j-1|\le\frac12,
\tag{21}
\]

satisfies

\[
\boxed{
\int_{I_\kappa}|P(x)|^2\,dx\ge m.
}
\tag{22}
\]

This is a finite-dimensional compactness statement. If (22) failed, take a sequence with integrals tending to zero. After passing to a subsequence, `N` is fixed and every `lambda_j` and `c_j` converges. The resulting exponential polynomial `P_infty` vanishes on `I_kappa`, hence vanishes identically by analyticity.

Group equal limiting exponents. The coefficient of every resulting distinct exponential is a sum of one or more limiting `c_j` and therefore has strictly positive real part by (21). No grouped coefficient can vanish. Distinct exponentials are linearly independent: differentiating at one point gives a Vandermonde system. Hence `P_infty` cannot vanish identically, a contradiction.

This is the exact place where bounded cardinality and bounded scaled diameter enter. If either `B` or `R` grows with `U`, the compact parameter set disappears and the floor `m(B,R,kappa)` is allowed to collapse.

## 3. The real Robin packet retains the complex visibility floor

A lower bound for the complex envelope is not automatically a lower bound for its real part, so one still has to control the target carrier. Write

\[
d_{\rho_0}=|d_{\rho_0}|e^{i\theta_0},
\qquad
\omega_U:=\gamma_0U.
\tag{23}
\]

Ignoring the `O(U^-1)` error in (15) for one moment, the normalized real packet on `I_kappa` is

\[
G_U(x)
:=
\Re\left(
e^{i(\omega_Ux+\theta_0)}P_U(x)
\right).
\tag{24}
\]

The family in (20)--(21) has uniformly bounded `P_U` and `P_U'` on `I_kappa`. Therefore integration by parts gives

\[
\left|
\int_{I_\kappa}
e^{2i\omega_Ux}P_U(x)^2\,dx
\right|
\ll_{B,R,\kappa}
\frac1{\omega_U}
\ll
\frac1U,
\tag{25}
\]

because `gamma_0>=gamma_*`.

Using `Re(z)^2=(|z|^2+Re(z^2))/2`, (22) and (25) yield

\[
\int_{I_\kappa}|G_U(x)|^2\,dx
=
\frac12\int_{I_\kappa}|P_U(x)|^2\,dx
+O_{B,R,\kappa}(U^{-1})
\ge
\frac m3
\tag{26}
\]

for large enough `U`. Restoring `E_U` from (17) changes the `L^2` norm by `o(1)`, so after another harmless weakening there is `g_0>0` with

\[
\sup_{x\in I_\kappa}
\left|
\Re\left(
e^{i(\omega_Ux+\theta_0)}(P_U(x)+E_U(x))
\right)
\right|
\ge g_0.
\tag{27}
\]

This carrier averaging is why (7) is a statement about the actual real packet rather than only its positive-frequency analytic half.

Finally, because `x<=1`,

\[
e^{-(\Theta-\beta_0)Ux}
\ge
e^{-(\Theta-\beta_0)U},
\tag{28}
\]

while (10) at `u=U` gives

\[
|a_{\rho_0,K}(U)|
=
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|
\left(1+O_K(U^{-1})\right).
\tag{29}
\]

Equations (15), (27), (28), and (29) prove (7).

## 4. Hidden full packets must export cancellation or grow local complexity

Now return to the actual attained-edge packet of `RE-131`--`RE-133`. Let `rho_0(U)` be a maximizing positive-ordinate subedge zero,

\[
M_K(U)=|a_{\rho_0,K}(U)|,
\tag{30}
\]

and let

\[
C_U(R)
:=
\left\{
\rho:
|\Re\rho-\beta_0|\le R/U,
\quad
|\Im\rho-\gamma_0|\le R/U
\right\}
\tag{31}
\]

inside the positive-ordinate subedge packet, counted with multiplicity.

Suppose along a sequence `U_j->infinity` the full packet hides on a fixed-relative window,

\[
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_K(u)|
=o(M_K(U_j)).
\tag{32}
\]

If for some fixed `R` and `B`

\[
\#C_{U_j}(R)\le B
\tag{33}
\]

along a subsequence, then (7) supplies a point

\[
u_j\in[(1-\kappa)U_j,U_j]
\tag{34}
\]

at which the reciprocal-box subpacket has size at least `c_0 M_K(U_j)`. Combining this with (32), the complement must satisfy

\[
\boxed{
\left|
\mathcal S_K(u_j)-
\mathcal S_{C_{U_j}(R),K}(u_j)
\right|
\ge
(c_0-o(1))M_K(U_j).
}
\tag{35}
\]

Hence bounded local occupancy is compatible with hiding only if **order-one cancellation is imported from outside that fixed reciprocal box**.

In particular, if the cancelling part of the packet is tight at reciprocal scale in the sense that for some fixed `R`

\[
\sup_{(1-\kappa)U_j\le u\le U_j}
\left|
\mathcal S_K(u)-
\mathcal S_{C_{U_j}(R),K}(u)
\right|
=o(M_K(U_j)),
\tag{36}
\]

then (32) forces

\[
\boxed{
\#C_{U_j}(R)\to\infty.
}
\tag{37}
\]

This is a concentration--compactness alternative for the local zero geometry. A hidden normalized packet cannot converge to a finite nonzero reciprocal-scale configuration. It must lose compactness through growing local cardinality, through cancellation mass escaping to larger scaled radii, or through both.

## 5. `RE-133` sits exactly on the noncompact side of the dichotomy

The matched control of `RE-133` is not a counterexample to (7). Its stage-`j` cluster has `2^j` atoms, while its scaled horizontal and vertical diameters are both `O(j)`. Thus neither cardinality nor scaled radius is uniformly bounded.

For a very small fixed `R`, only the target and perhaps a few companions lie in `C_(U_j)(R)`; their partial packet is visible by (7), and the remaining subset atoms import the cancellation from outside the box. Once `R` is large enough to include one or more generations of reciprocal increments, the occupancy inside the fixed box itself grows with `j`. The construction therefore realizes exactly the two escape channels exposed by (35)--(37).

The conclusion is stronger than the mechanism-specific observation in `RE-133` that a fixed number of product factors gives only fixed suppression. Here the internal geometry is arbitrary: no subset structure, geometric amplitudes, common increment, or factorization is assumed. **Some scaled local noncompactness is necessary for macroscopic hiding under the physical coefficient law.**

This also sharpens the source-specific target. It would now suffice to combine two facts for actual near-edge zeta zeros at the relevant dominant phases: a bounded-occupancy theorem in one fixed reciprocal box and a tightness theorem saying that the order-`M_K(U)` cancelling mass cannot continually migrate outside that box. Either ingredient alone is insufficient, but together they contradict (32).

## 6. Adversarial audit

The main possible shortcuts were tested directly.

First, the proof does not infer real-packet visibility from complex-envelope magnitude. That implication is false pointwise. Equations (23)--(27) explicitly average the rapidly rotating target carrier and show that the oscillatory square term is `O(1/U)` uniformly over the bounded exponential-polynomial family.

Second, the leading coefficient alignment is not imposed by hand. It follows from the exact Robin/CA kernel: inside an `R/U` two-dimensional box, `d_rho/d_(rho_0)=1+O(1/U)`. The finite-order correction terms remain uniformly `O_K(1/U)` relative to the leading coefficient throughout the left relative half-window.

Third, collisions do not break the compactness argument. If limiting exponents coincide, their coefficients add with positive real part. This covers multiplicity as well as simple spectra. By contrast, arbitrary freely signed exponential coefficients would invalidate the theorem; the physical kernel orientation is load-bearing.

Fourth, (7) is deliberately proved only on `[(1-kappa)U,U]`. This is enough because the hiding hypothesis used in the line controls the larger symmetric window. Restricting to the left half also makes the target edge damping no smaller than at the center, avoiding an unnecessary loss.

Fifth, (35) is a statement about a subpacket versus its complement, not a claim that bounded occupancy alone forbids full-packet hiding. Distant modes can still cancel the visible local cluster. Equation (36) states the extra tightness input required to convert bounded occupancy into a contradiction.

Sixth, the constants are not uniform as `B` or `R` grow. That failure is essential rather than technical: `RE-133` hides precisely by allowing local complexity and scaled diameter to grow. No quantitative rate for `c_0(B,R,kappa)` is claimed here.

Finally, no actual new property of zeta zeros is assumed. The theorem is a deterministic consequence of the coefficient law and bounded reciprocal geometry. Its value is to identify exactly which local compactness property a zeta-specific input would have to supply.

No unresolved objection remains after these checks, so no review sidecar is created.

## 7. Prior-art boundary and research effect

A targeted prior-art audit found the expected harmonic-analysis analogue: Turan--Nazarov/Remez inequalities give quantitative observability of exponential polynomials from sets of positive measure, with constants depending on the number of terms and spectral diameter. The compactness proof in Section 2 is a weaker self-contained version tailored to the extra coefficient alignment supplied by (3). No Turan--Nazarov theorem is used as a dependency.

On the zeta side, Maynard--Pratt's half-isolated-zero method is explicitly sensitive to vertical zero geometry, but it does not provide an unconditional bounded-occupancy theorem for shrinking two-dimensional boxes of radius `R/U`, nor a tightness theorem for the Robin/CA coefficient mass outside such boxes. Thus the result does not duplicate a known local-zero exclusion.

No external theorem is load-bearing, so `SOURCES.md` needs no update.

The line-specific advance is that the final sentence of `RE-133` is now a theorem rather than a feature of one matched control. A fixed-relative hidden packet cannot be supported by a precompact finite reciprocal-scale configuration. The remaining attained-edge problem can therefore be organized around a precise two-part source question:

\[
\boxed{
\text{local occupancy control}
\quad+\quad
\text{reciprocal-scale cancellation tightness}
\quad\Longrightarrow\quad
\text{macroscopic visibility}.
}
\tag{38}
\]

The next useful direction is quantitative rather than another formal product: estimate how the visibility floor deteriorates with `B` and `R`, then compare that tariff with the strongest zeta-specific local counting, spacing, zero-detection, or explicit-formula constraints available at the dominant-atom scale. That would measure how much cluster complexity actual zeta zeros would need in order to imitate `RE-133`, rather than merely asserting that the complexity must grow.