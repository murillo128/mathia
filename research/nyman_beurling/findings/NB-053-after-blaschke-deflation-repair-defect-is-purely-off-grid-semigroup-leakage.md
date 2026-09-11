# NB-053 — after Blaschke deflation the repair defect is purely off-grid semigroup leakage

**Status:** `EXACT-DERIVED + LITERATURE-BOUNDED + DISCRETE-SEMIGROUP-INVARIANCE + TWO-GENERATOR-CONTINUOUS-HULL + LARGE-SHIFT-LEAKAGE-DECAY + NEGATIVE/METHOD-BOUNDARY`. `NB-052` removes Burnol's common Blaschke factor from the weighted-repair comparison and leaves the target defect

\[
\Delta_*=B(1)^2\delta_{\mathrm{def}}^2,
\qquad
\delta_{\mathrm{def}}
=
\operatorname{dist}(k_1,\mathcal A_{\mathrm{nat}}),
\qquad
k_1(s)=\frac1s,
\tag{1}
\]

where

\[
\mathcal A_{\mathrm{nat}}
=
\overline{\operatorname{span}}
\{\phi_{1/n}:n\ge2\}
\subset H^2(\Re s>1/2),
\tag{2}
\]

and

\[
\phi_\theta(s)
=
\frac{1}{B(s)}\widehat{\rho_\theta}(s)
=
O(s)\frac{\theta-\theta^s}{s-1},
\qquad
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}.
\tag{3}
\]

Burnol's factorization makes `O` outer. The remaining defect in (1) therefore cannot be another copy of the off-critical-zero Blaschke obstruction. The present result sharpens that statement in semigroup form.

Let

\[
(U_tF)(s)
:=
 e^{-t(s-1/2)}F(s),
\qquad t\ge0,
\tag{4}
\]

be the standard strongly continuous inner-multiplier shift semigroup on `H^2(Re s>1/2)`. Then:

1. the deflated natural closure is invariant under every **integer logarithmic shift**,

\[
\boxed{
U_{\log m}\mathcal A_{\mathrm{nat}}
\subseteq
\mathcal A_{\mathrm{nat}}
\qquad(m\ge2);
}
\tag{5}
\]

2. nevertheless its smallest closed invariant hull under the **full continuous shift semigroup** is the whole Hardy space, and in fact the two natural generators `n=2,3` already suffice:

\[
\boxed{
\overline{\operatorname{span}}
\{U_t\phi_{1/2},U_t\phi_{1/3}:t\ge0\}
=
H^2(\Re s>1/2);
}
\tag{6}
\]

3. consequently every nonzero vector in `A_nat^perp` is invisible to all integer-log shifts but must leak into `A_nat` at some off-grid shift. More strongly, this off-grid leakage always disappears uniformly at large logarithmic scale. If

\[
P=P_{\mathcal A_{\mathrm{nat}}},
\qquad
h\in\mathcal A_{\mathrm{nat}}^\perp,
\qquad
\mathcal L_h(t):=P U_t^*h,
\tag{7}
\]

then

\[
\boxed{
\mathcal L_h(\log n)=0\quad(n\ge1),
}
\tag{8}
\]

and

\[
\boxed{
\sup_{t\ge T}\|\mathcal L_h(t)\|
\longrightarrow0
\qquad(T\to\infty).
}
\tag{9}
\]

If `h!=0`, however, (6) forces

\[
\boxed{
\mathcal L_h(t)\ne0
\quad\text{for at least one }t\ge0,
}
\tag{10}
\]

and every such detecting time is necessarily off the logarithmic integer grid.

For the canonical deflated target residual

\[
h_*
:=
k_1-Pk_1,
\qquad
\|h_*\|=\delta_{\mathrm{def}},
\tag{11}
\]

this gives a precise interpretation of `NB-052`: if `Delta_*>0`, its nonzero arithmetic component is a **finite/moderate-scale off-grid co-invariance defect**. It is not a second common inner factor and it cannot be recovered by expecting a fixed nonzero leakage from larger and larger dilation scales. The finite grids of `NB-050`--`NB-051` gain exactly the kind of noninteger parameter access that the natural closure lacks.

## 1. The natural deflated space is invariant under the integer multiplicative semigroup

For `n>=2` write

\[
q_n(s)
:=
\frac{n^{-1}-n^{-s}}{s-1},
\qquad
\phi_{1/n}=Oq_n.
\tag{12}
\]

The apparent singularity of `q_n` at `s=1` is removable, with

\[
q_n(1)=\frac{\log n}{n}.
\tag{13}
\]

For integers `m,n>=2` there is the exact cocycle identity

\[
\begin{aligned}
q_{mn}(s)
&=
\frac{(mn)^{-1}-(mn)^{-s}}{s-1}\\
&=
n^{-1}q_m(s)+m^{-s}q_n(s).
\end{aligned}
\tag{14}
\]

Multiplying by the common outer factor `O` gives

\[
\boxed{
\phi_{1/(mn)}
=
n^{-1}\phi_{1/m}+m^{-s}\phi_{1/n}.
}
\tag{15}
\]

Since

\[
U_{\log m}F
=m^{1/2-s}F,
\tag{16}
\]

(15) rearranges to

\[
\boxed{
U_{\log m}\phi_{1/n}
=
\sqrt m\left(
\phi_{1/(mn)}-n^{-1}\phi_{1/m}
\right).
}
\tag{17}
\]

The right side belongs to the algebraic natural span. By density and boundedness of `U_(log m)`, (17) proves (5).

This invariance is not claimed as a new Nyman mechanism. It is the Mellin/deflated form of the classical dilation-semigroup covariance already used by Nyman, Burnol, Bagchi and earlier findings in this line. What matters here is what remains after combining it with the exact de-Blaschke repair defect of `NB-052`.

## 2. Two multiplicatively independent natural generators have full continuous shift hull

The full continuous semigroup behaves very differently from its logarithmic integer sampling. By Beurling--Lax, the smallest closed `U_t`-invariant subspace containing a family of Hardy functions is the common-inner-factor subspace associated with their greatest common inner divisor.

Because `O` is outer, the inner factor of `phi_(1/n)=Oq_n` is exactly the inner factor of `q_n`. The latter has a completely explicit zero set. From (12), away from the removable point `s=1`,

\[
q_n(s)=0
\iff
n^{-(s-1)}=1,
\tag{18}
\]

so

\[
\boxed{
Z(q_n)
=
\left\{
1+\frac{2\pi i k}{\log n}:k\in\mathbb Z\setminus\{0\}
\right\},
}
\tag{19}
\]

up to the immaterial sign convention for `k`.

There is no singular boundary inner factor: `q_n` extends holomorphically through the critical boundary. There is also no nontrivial special exponential inner factor. Indeed on the positive real axis

\[
q_n(\sigma)
=
\frac{n^{-1}+o(1)}{\sigma-1}
\qquad(\sigma\to+\infty),
\tag{20}
\]

so it has only polynomial decay there; a factor `exp(-c(s-1/2))` with `c>0` would force exponential decay of the inner component and exponential growth of the remaining Hardy factor. This is the same standard factorization boundary used by Burnol when excluding a special inner factor from the continuous Nyman family.

Now `q_2` and `q_3` have no common zero. A common nonzero zero would give integers `k,l!=0` with

\[
\frac{k}{\log2}
=
\frac{l}{\log3},
\tag{21}
\]

hence `log 2/log 3` rational, equivalently `2^l=3^k`, impossible. Thus their greatest common inner divisor is constant. Beurling--Lax therefore gives (6).

The same statement can be read before deflation. Since multiplication by `B` is inner and isometric,

\[
\overline{\operatorname{span}}
\{U_t\widehat{\rho_{1/2}},
  U_t\widehat{\rho_{1/3}}:t\ge0\}
=
B H^2,
\tag{22}
\]

which is Burnol's complete continuous Nyman closure. Thus, after the common zeta-zero obstruction is removed, **there is no further common inner obstruction even in the two-generator pair `1/2,1/3`**.

This is stronger than merely restating that the full continuous family has deflated closure `H^2`: the full continuous invariant hull is already forced by two natural generators. The difference between the natural closure and the continuous closure therefore cannot be blamed on missing spectral/inner factors shared by the natural generators. It lies in the restriction of the available shift times.

## 3. Every natural orthogonal defect is exactly blind on `log N` and asymptotically blind off-grid

Let `h in A_nat^perp`. From (5), for every integer `n>=1` and every `f in A_nat`,

\[
\langle U_{\log n}^*h,f\rangle
=
\langle h,U_{\log n}f\rangle
=0.
\tag{23}
\]

Hence

\[
U_{\log n}^*h
\in
\mathcal A_{\mathrm{nat}}^\perp,
\tag{24}
\]

which proves (8).

The shrinking mesh of the logarithmic integer grid then gives more than exact blindness at the sampled times. Fix `t` large and put

\[
n=\lfloor e^t\rfloor,
\qquad
a=\log n,
\qquad
\delta=t-a.
\tag{25}
\]

Then

\[
0\le\delta
<
\log\left(1+\frac1n\right).
\tag{26}
\]

The shift semigroup and its adjoint commute with themselves, so

\[
U_t^*h-U_a^*h
=
U_a^*(U_\delta^*h-h).
\tag{27}
\]

Since `P U_a^*h=0` by (8), and both `P` and `U_a^*` are contractions,

\[
\boxed{
\|\mathcal L_h(t)\|
\le
\|U_\delta^*h-h\|.
}
\tag{28}
\]

Define the fixed-vector continuity modulus

\[
\omega_h(r)
:=
\sup_{0\le u\le r}
\|U_u^*h-h\|.
\tag{29}
\]

Strong continuity gives `omega_h(r)->0` as `r->0`. For `t>=T`, (26) yields

\[
\delta
\le
\varepsilon_T
:=
\log\left(
1+\frac1{\lfloor e^T\rfloor}
\right),
\qquad
\varepsilon_T\to0.
\tag{30}
\]

Therefore

\[
\boxed{
\sup_{t\ge T}
\|\mathcal L_h(t)\|
\le
\omega_h(\varepsilon_T)
\longrightarrow0,
}
\tag{31}
\]

which proves (9).

The conclusion is deliberately **vectorwise**, not operator-norm uniform. The right-shift semigroup is strongly continuous but not norm-continuous at zero, so (31) does not imply

\[
\|P U_t^*P_{\mathcal A_{\mathrm{nat}}^\perp}\|
\to0.
\tag{32}
\]

No such uniform claim is made. This distinction is load-bearing for finite-section applications where the relevant residual may itself move with the scale.

## 4. Nonzero defects must be exposed at a finite off-grid shift

Suppose `h in A_nat^perp` also satisfies

\[
P U_t^*h=0
\qquad\text{for every }t\ge0.
\tag{33}
\]

Then for every `f in A_nat`,

\[
\langle h,U_tf\rangle
=
\langle U_t^*h,f\rangle
=0.
\tag{34}
\]

Thus `h` is orthogonal to the full continuous invariant hull of `A_nat`. Equation (6) says that hull is all of `H^2`, so `h=0`. Contrapositively,

\[
\boxed{
h\ne0
\Longrightarrow
\exists t\ge0:
P U_t^*h\ne0.
}
\tag{35}
\]

Combining (8), (31), and (35), every nonzero natural orthogonal defect has the same qualitative profile:

\[
\text{exactly blind on }\{\log n:n\in\mathbb N\},
\quad
\text{visible somewhere off-grid},
\quad
\text{and asymptotically invisible as }t\to\infty.
\tag{36}
\]

Apply this to the canonical target residual `h_*` from (11). If `delta_def>0`, then the `NB-052` repair limit

\[
\Delta_*
=
B(1)^2\|h_*\|^2
\tag{37}
\]

is attached to a fixed vector with precisely the leakage profile (36). Hence a strategy that tries to control `Delta_*` merely by probing larger and larger dilation parameters against this fixed infinite-section defect is pointed in the wrong direction: every such off-grid leakage tends to zero, while the exact integer-grid leakage is identically zero.

This does **not** rule out scale-coupled finite-section probes. Their residuals vary with `N`, and the modulus `omega_h` in (31) is not uniform over the unit sphere. A successful finite argument could still exploit quantitative regularity of the actual moving residuals, a bounded family of off-grid times, or a source-specific relation unavailable for arbitrary vectors in `A_nat^perp`.

## 5. The finite continuous grid injects the missing off-grid operation

The `NB-050` space

\[
\mathcal D_{M,N}
=
\operatorname{span}
\{\phi_{M/n}:M<n\le N\}
\tag{38}
\]

uses logarithmic parameters

\[
t_{M,n}
=
\log\frac nM,
\tag{39}
\]

which are not restricted to `log N`. Thus its improvement over the natural subgrid is exactly of the type left open by (36): it samples off-grid continuous-semigroup geometry.

There is also a direct small-shift normal form. For `a>0`, put `theta=e^{-a}`. From (3),

\[
\phi_{e^{-a}}(s)
=
O(s)q_a(s),
\qquad
q_a(s)
:=
e^{-a}
\frac{1-e^{-a(s-1)}}{s-1}.
\tag{40}
\]

The integral representation

\[
\frac{q_a(s)}a
=
\frac{e^{-a}}a
\int_0^a e^{-u(s-1)}\,du
\tag{41}
\]

shows on the critical boundary `Re s=1/2` that

\[
\left|\frac{q_a(s)}a\right|
\le1,
\tag{42}
\]

while `q_a(s)/a -> 1` pointwise as `a->0`. Since `O in H^2`, dominated convergence gives

\[
\boxed{
\frac1a\phi_{e^{-a}}
\longrightarrow
O
\quad\text{in }H^2
\qquad(a\downarrow0).
}
\tag{43}
\]

In particular, the very first off-grid parameter of the finite grid,

\[
\theta_M=\frac{M}{M+1},
\qquad
 a_M=\log\left(1+\frac1M\right),
\tag{44}
\]

already gives

\[
\frac1{a_M}\phi_{M/(M+1)}
\longrightarrow O.
\tag{45}
\]

This does not by itself make `D_(M,N)` dense or estimate `delta_(M,N)`: one direction converging to the outer seed is not a full approximation theorem. It does explain structurally why the continuous finite grid can access information unavailable to the reciprocal-integer family. As `M` grows it introduces arbitrarily small logarithmic shifts, whereas the natural semigroup has its first positive shift at `log 2`.

`NB-051` proves the stronger global statement that the complete two-scale grid converges to the full continuous closure. Equations (36) and (43)--(45) identify the operator mechanism behind that enrichment without replacing the exact target-distance argument of `NB-051`.

## 6. Prior-art boundary and consequence for the live bridge

The load-bearing classical ingredients are already anchored in `SOURCES.md`. Burnol proves the Mellin formula for `rho_theta`, the Blaschke/outer factorization, the absence of extra singular or special inner factors in the continuous Nyman family, and the Beurling--Lax identification of the continuous closure with `B H^2`. Nyman's translation semigroup and Bagchi's integer-dilation formulation make semigroup covariance classical rather than a Mathia novelty.

A targeted prior-art audit also located Boqing Xue, *On a Hilbert Space Reformulation of Riemann Hypothesis* (arXiv:1911.04029), which studies a different Hardy/Bergman model of the natural Nyman space, proves invariance under a multiplicative operator monoid, and relates adjoint invariance to RH. Accordingly, neither integer-semigroup invariance nor the general idea that adjoint invariance carries missing target information is claimed new here.

The line-local delta is narrower and tied specifically to `NB-052`: after the common Blaschke obstruction is removed, (6) shows that **two** natural generators already have full continuous-shift hull, while (31) shows that every defect orthogonal to the discrete natural closure has vanishing large-shift co-invariance leakage because the exact zero-leakage grid `log n` becomes asymptotically fine. No located source stated this two-generator de-Blaschke hull together with the uniform-tail fixed-vector leakage consequence as the normal form of the `NB-050`--`NB-052` repair defect.

No new specialized theorem is imported beyond the Burnol/Beurling--Lax machinery already recorded in `SOURCES.md`, so the source anchor file does not change.

The surviving source-to-target question is therefore sharper. A theorem controlling `delta_def` cannot come from another common inner factor, and for the fixed closure-level residual it cannot rely on a persistent signal at ever larger dilations. It must instead obtain one of the following genuinely additional inputs: quantitative control at bounded/moderate off-grid shifts, a source-uniform regularity modulus for the moving finite residuals that upgrades the vectorwise estimate (31), or a direct arithmetic relation tying the finite-grid off-grid enrichment to source-visible data.

No estimate of `delta_def`, `Delta_*`, or `d_N` is proved here, and no RH implication follows. The result removes a spectral explanation and localizes the remaining defect to a precise semigroup-sampling/co-invariance mechanism.