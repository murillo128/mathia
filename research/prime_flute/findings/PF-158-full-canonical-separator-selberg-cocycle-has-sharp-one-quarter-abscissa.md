# PF-158 — full canonical-separator Selberg cocycle has sharp positive-real abscissa `1/4`

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + DECISIVE-NEGATIVE/BOUNDARY` for the complete PF-004 canonical consecutive-block separator sector. PF-157 proves that the source Margulis-short Selberg sector becomes a holomorphic zero-free relative cocycle on `Re s>0` after the exact all-composite shift subtraction. The present finding removes the shortness restriction for the entire explicit multi-gap separator family. The normalized relative product over **all** PF-004 canonical separators converges locally normally and is zero-free on

\[
\boxed{\operatorname{Re}s>\frac14.}
\]

The threshold is sharp for this natural matched series on the positive real axis: after fixing any one left exterior prime gap, the corresponding right-endpoint subseries of the relative Selberg logarithmic derivative diverges with one eventual sign for every real `0<s<=1/4`.

In particular, the whole canonical multi-gap sector — including the PF-069 positive interval of primitive-length accumulation, the zero-systole subsequences, and arbitrarily long consecutive-block separators — cannot generate a critical-line zero divisor after exact prime/shift matching. The critical line `Re s=1/2` lies strictly inside the proved zero-free half-plane.

This is **not** a full relative Selberg zeta function for the infinite flute. Primitive word classes outside the PF-004 canonical separator family remain uncontrolled.

## Claim

Let

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
W(x)=V(x+1)-1,
\tag{1}
\]

and let `C` denote the complete PF-004 family of primitive simple separators of finite consecutive cusp blocks. Write a member of `C` by its two exterior consecutive-prime intervals

\[
a<b<c<d,
\tag{2}
\]

where `b` is the prime after `a` and `d` is the prime after `c`. Put

\[
X=V(b)-V(a),\qquad
Y=V(c)-V(b),\qquad
Z=V(d)-V(c),
\tag{3}
\]

so that PF-004 gives

\[
\chi=\frac{Y(X+Y+Z)}{XZ},
\qquad
L=4\operatorname{arsinh}\sqrt\chi.
\tag{4}
\]

Let `L^+` be the length of the same marked separator on the exact all-composite shift clone obtained from the endpoints `W(p)`. PF-106 and PF-109 give, uniformly over arbitrary block span,

\[
\boxed{
|L^+-L|\le C a^{-3},
\qquad
\left|\log\frac{L^+}{L}\right|\le C a^{-3}.
}
\tag{5}
\]

For one primitive length `L>0`, use the standard local Selberg factor

\[
Z_L(s)
:=
\prod_{m=0}^{\infty}
\left(1-e^{-(s+m)L}\right),
\qquad \operatorname{Re}s>0,
\tag{6}
\]

and write

\[
Q_s(L)
:=
\frac{d}{ds}\log Z_L(s)
=
\sum_{k\ge1}
\frac{L e^{-skL}}{1-e^{-kL}}.
\tag{7}
\]

Define the canonical-separator relative logarithmic derivative formally by

\[
G_{\rm can}(s)
:=
\sum_{\eta\in\mathcal C}
\left[
Q_s(L_\eta^+)-Q_s(L_\eta)
\right].
\tag{8}
\]

Then:

1. the series in (8) converges **absolutely and locally uniformly** on
   \[
   \mathbb H_{1/4}
   :=
   \left\{s\in\mathbb C:\operatorname{Re}s>\frac14\right\};
   \tag{9}
   \]
2. hence `G_can` is holomorphic on `H_{1/4}`;
3. for any `s_0 in H_{1/4}`, the finite normalized products
   \[
   D_E(s;s_0)
   :=
   \prod_{\eta\in E}
   \frac{Z_{L_\eta^+}(s)}{Z_{L_\eta}(s)}
   \frac{Z_{L_\eta}(s_0)}{Z_{L_\eta^+}(s_0)},
   \tag{10}
   \]
   indexed by finite subsets `E subset C`, converge locally uniformly to
   \[
   \boxed{
   D_{\rm can}(s;s_0)
   =
   \exp\!\left(
   \int_{s_0}^{s}G_{\rm can}(w)\,dw
   \right);
   }
   \tag{11}
   \]
4. therefore
   \[
   \boxed{
   D_{\rm can}(s;s_0)\ne0
   \qquad
   \left(\operatorname{Re}s>\frac14\right).
   }
   \tag{12}
   \]

Moreover the positive-real boundary is sharp for the series (8). Fix any one left exterior consecutive-prime pair `a<b`. If the right exterior pair `c<d` runs to infinity through consecutive primes, then for every real

\[
0<\sigma\le\frac14
\tag{13}
\]

the terms

\[
Q_\sigma(L_{a,c}^+)-Q_\sigma(L_{a,c})
\tag{14}
\]

are eventually negative and their sum diverges to `-infinity`.

Thus `1/4` is not an artifact of the upper-bound proof: it is the actual positive-real abscissa of convergence for the naturally paired canonical-separator logarithmic derivative. No meromorphic-continuation statement across that boundary is made.

## 1. Selberg sensitivity is bounded at short length and exponentially damped at long length

PF-157 rewrites (7) as

\[
Q_s(L)
=
\sum_{k\ge1}\frac1k H_s(kL),
\qquad
H_s(x):=
\frac{x e^{-sx}}{1-e^{-x}}.
\tag{15}
\]

Fix a compact set `K subset {Re s>0}` and put

\[
\sigma_K:=\inf_{s\in K}\operatorname{Re}s>0.
\tag{16}
\]

PF-156/PF-157 already prove the uniform small-length logarithmic estimate: for every fixed finite `L_*`,

\[
\boxed{
\sup_{s\in K}
|Q_s(L')-Q_s(L)|
\le C_{K,L_*}
\left|\log\frac{L'}L\right|
}
\tag{17}
\]

whenever `0<L,L'<=L_*`.

For long lengths one should instead use the additive coordinate. Differentiating (15) gives

\[
\frac{\partial}{\partial L}Q_s(L)
=
\sum_{k\ge1}H_s'(kL).
\tag{18}
\]

For `x>=1`, uniformly for `s in K`,

\[
|H_s'(x)|
\le C_K(1+x)e^{-\sigma_Kx}.
\tag{19}
\]

Consequently, for `L>=1`,

\[
\boxed{
\sup_{s\in K}
\left|\frac{\partial}{\partial L}Q_s(L)\right|
\le
C_K(1+L)e^{-\sigma_KL}.
}
\tag{20}
\]

The estimate follows by summing the geometric series and its first moment. It is the key extra input beyond PF-157: long primitive classes are exponentially cheaper at Selberg-factor level even though there are infinitely many of them for each fixed left exterior gap.

Combining (17), (20), PF-106's additive estimate and PF-109's multiplicative estimate gives the following uniform hybrid bound. If `K subset H_{1/4}` is compact, choose

\[
\frac14<\rho<\min\!\left(\sigma_K,\frac12\right).
\tag{21}
\]

Then, after discarding finitely many left labels `a`,

\[
\boxed{
\sup_{s\in K}|Q_s(L^+)-Q_s(L)|
\le
\begin{cases}
C_K a^{-3}, & L\le2,\\[2mm]
C_K a^{-3}(1+L)e^{-\rho L}, & L>2.
\end{cases}}
\tag{22}
\]

Indeed, in the short regime PF-109 keeps the entire multiplicative interpolation inside a fixed bounded length interval and (17) applies. In the long regime PF-106 gives an additive interpolation of width `O(a^-3)`; because that width tends to zero, `Re(s)` times every interpolating length is eventually at least `rho L`, and (20) applies.

The finitely many discarded left labels cause no convergence problem. For each such fixed `a`, PF-106 still gives one finite additive interpolation width. Once `L` is large, shifting `L` by a fixed bounded amount changes only the constant in (20); the finitely many remaining bounded-length terms are harmless.

In particular, without any restriction on the separator length,

\[
\boxed{
\sup_{s\in K}|Q_s(L^+)-Q_s(L)|
\le C_K a^{-3}}
\tag{23}
\]

for all sufficiently large `a`.

## 2. Near-span canonical separators are already summable

Call a separator **near-span** when

\[
c<4a.
\tag{24}
\]

For each fixed left prime `a`, there are at most `4a` possible integer values of `c`, hence certainly at most `4a` right exterior prime gaps. Equation (23) therefore gives

\[
\sum_{\substack{c<4a\\ c\ {m prime}}}
\sup_{s\in K}|Q_s(L_{a,c}^+)-Q_s(L_{a,c})|
\le C_K a^{-2}.
\tag{25}
\]

Thus

\[
\boxed{
\sum_a
\sum_{c<4a}
\sup_{s\in K}|Q_s(L_{a,c}^+)-Q_s(L_{a,c})|
<\infty.
}
\tag{26}
\]

This simple count already contains the PF-069 positive-length accumulation sector. Those accumulation sequences come from neighboring normalized prime gaps at comparable arithmetic scale, so their right exterior labels remain comparable with the left labels. Although the **absolute** primitive Selberg measure has infinite mass in a positive length interval by PF-069, the prime/shift difference of this entire near-span family is summable because there are only `O(a)` candidates at scale `a` while every matched factor changes by `O(a^-3)`.

No prime-density theorem is used in this part.

## 3. A dyadic prime-gap moment controls every far-span separator

For the far-span family `c>=4a`, use the exact cross-ratio (4). The Baker--Harman--Pintz exponent recorded in S6 gives, with

\[
\theta=0.525<1,
\tag{27}
\]

\[
b-a=O(a^\theta),
\qquad
d-c=O(c^\theta).
\tag{28}
\]

On `x>=3`, the exact derivative

\[
V'(x)
=\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2
\tag{29}
\]

is bounded above and is greater than `1`. Hence

\[
X\le C a^\theta,
\qquad
Z\le C(d-c).
\tag{30}
\]

Also `b=a+o(a)`, so for all sufficiently large `a` and every `c>=4a`,

\[
Y=V(c)-V(b)
\ge c-b
\ge \frac c2.
\tag{31}
\]

Therefore

\[
\boxed{
\chi
=\frac{Y(X+Y+Z)}{XZ}
\ge
\frac{Y^2}{XZ}
\ge
C^{-1}\frac{c^2}{a^\theta Z}.}
\tag{32}
\]

There is also a crude upper bound

\[
\boxed{\chi\le Cc^2,}
\tag{33}
\]

because `X,Z` are bounded below by positive absolute constants, while `X+Y+Z=O(c)` in this regime. Hence

\[
L=4\operatorname{arsinh}\sqrt\chi
=O(1+\log c).
\tag{34}
\]

For all sufficiently far pairs, `chi>=1`, and then

\[
L
=4\operatorname{arsinh}\sqrt\chi
\ge2\log\chi.
\tag{35}
\]

Combining (32) and (35) gives

\[
\boxed{
e^{-\rho L}
\le
C_ho\,
 a^{2\rho\theta}Z^{2\rho}c^{-4\rho}.}
\tag{36}
\]

The remaining issue is to sum the fractional moment `Z^(2rho)` over all right exterior prime gaps. This needs no distributional model for prime gaps.

Put

\[
\beta:=2\rho.
\tag{37}
\]

By (21),

\[
\frac12<\beta<1.
\tag{38}
\]

For a dyadic interval `R<=c<2R`, let the sum run over primes `c` and let `d` be the following prime. Since consecutive prime intervals are disjoint and BHP makes the final overshoot `o(R)`,

\[
\sum_{R\le c<2R}(d-c)=O(R).
\tag{39}
\]

Because `V'` is bounded,

\[
\sum_{R\le c<2R}Z=O(R).
\tag{40}
\]

Concavity of `x -> x^beta` gives

\[
\begin{aligned}
\sum_{R\le c<2R}Z^\beta
&\le
N_R^{1-\beta}
\left(\sum_{R\le c<2R}Z\right)^\beta\\
&\le C R^{1-\beta}R^\beta,
\end{aligned}
\]

using only the trivial count `N_R<=R`. Thus

\[
\boxed{
\sum_{\substack{R\le c<2R\\c\ {\rm prime}}}
Z^{2\rho}
\le C_\rho R.}
\tag{41}
\]

This elementary dyadic moment is what moves the convergence boundary from the coarser pointwise-gap estimate to the exact exponent `1/4`.

## 4. Far-span summation converges exactly to the right of `1/4`

Insert (34), (36) and (41) into the long-length part of (22). For fixed left `a` and a dyadic block `R<=c<2R`, `R>=4a`,

\[
\begin{aligned}
&\sum_{R\le c<2R}
\sup_{s\in K}
|Q_s(L_{a,c}^+)-Q_s(L_{a,c})|\\
&\qquad\le
C_K
a^{-3+2\rho\theta}
R^{-4\rho}(1+\log R)
\sum_{R\le c<2R}Z^{2\rho}\\
&\qquad\le
C_K
a^{-3+2\rho\theta}
R^{1-4\rho}(1+\log R).
\end{aligned}
\tag{42}
\]

Since `rho>1/4`,

\[
1-4\rho<0,
\tag{43}
\]

so the dyadic sum over `R=2^j(4a)` is geometric. Hence

\[
\boxed{
\sum_{c\ge4a}
\sup_{s\in K}
|Q_s(L_{a,c}^+)-Q_s(L_{a,c})|
\le
C_K
a^{-2-2\rho(2-\theta)}(1+\log a).}
\tag{44}
\]

The exponent on `a` is strictly below `-2`, so summing (44) over all left primes converges absolutely. Together with (26), this proves

\[
\boxed{
\sum_{\eta\in\mathcal C}
\sup_{s\in K}
|Q_s(L_\eta^+)-Q_s(L_\eta)|
<\infty.}
\tag{45}
\]

Because `K` was an arbitrary compact subset of `H_{1/4}`, (45) proves absolute local-uniform convergence of (8).

The appearance of `1/4` has a transparent geometric origin. At fixed left boundary data a far canonical separator has

\[
L\approx4\log c
\tag{46}
\]

up to prime-gap logarithms, so its local Selberg sensitivity contributes approximately `c^(-4 Re s)`. There is one possible right exterior gap at each prime scale, and the fractional gap moment in (41) costs no extra power of `R`. The dyadic convergence condition is therefore exactly `4 Re s>1`.

## 5. The normalized canonical relative factor is holomorphic and zero-free

The half-plane `H_{1/4}` is simply connected. Equation (45) makes `G_can` holomorphic there. Define `D_can` by (11).

For a finite `E subset C`, each local factor is nonzero on `Re s>0`, and the logarithmic derivative of (10) is exactly the finite partial sum

\[
G_E(s)
=
\sum_{\eta\in E}
\left[Q_s(L_\eta^+)-Q_s(L_\eta)\right].
\tag{47}
\]

The normalization gives `D_E(s_0;s_0)=1`, so

\[
D_E(s;s_0)
=
\exp\!\left(\int_{s_0}^{s}G_E(w)\,dw\right).
\tag{48}
\]

Local-uniform convergence `G_E -> G_can` therefore implies local-uniform convergence of the normalized finite products to (11), independently of the exhaustion. Since (11) is an exponential of a holomorphic primitive,

\[
D_{\rm can}(s;s_0)\ne0
\]

throughout `H_{1/4}`. Changing the base point multiplies the limit only by a nonzero constant.

In particular,

\[
\boxed{
D_{\rm can}\!\left(\frac12+it;s_0\right)\ne0
\qquad(t\in\mathbb R).}
\tag{49}
\]

Thus the complete explicit multi-gap separator family has no matched relative Selberg zero on the RH axis.

## 6. The boundary `1/4` is genuinely sharp on the positive real axis

The upper-bound proof alone could leave open the possibility that `1/4` is merely an artifact of dyadic estimates. It is not.

Fix once and for all one left consecutive-prime pair `a<b`. Put

\[
D(x):=W(x)-V(x).
\tag{50}
\]

PF-106 proves

\[
D(x)>0,
\qquad D'(x)<0,
\qquad D(x)\to0.
\tag{51}
\]

Therefore the fixed left exterior interval satisfies

\[
X^+
=W(b)-W(a)
=X+D(b)-D(a)
<X,
\tag{52}
\]

and hence

\[
R_a:=\frac{X}{X^+}>1.
\tag{53}
\]

Let the right pair `c<d` tend to infinity. From (50)--(51),

\[
Y^+
=Y+D(c)-D(b)
=Y-D(b)+o(1),
\tag{54}
\]

so `Y^+/Y ->1`. Also PF-106's derivative estimate `D'(x)=O(x^-3)` gives

\[
D(d)-D(c)=O((d-c)c^{-3}),
\tag{55}
\]

while `Z>=d-c`; hence

\[
\frac{Z^+}{Z}	o1.
\tag{56}
\]

Since `Y->infinity`, the same is true for the second numerator factor, and therefore the exact cross-ratios obey

\[
\boxed{
\frac{\chi^+}{\chi}
\longrightarrow
\frac{X}{X^+}
=R_a>1.}
\tag{57}
\]

BHP gives `Z=O(c^theta)` with `theta<1`, so `chi->infinity`. Using

\[
4\operatorname{arsinh}\sqrt\chi
=2\log\chi+4\log2+o(1),
\tag{58}
\]

we obtain the nonzero additive limit

\[
\boxed{
L_{a,c}^+-L_{a,c}
\longrightarrow
\delta_a:=2\log R_a>0.}
\tag{59}
\]

This is fully compatible with PF-109: the **relative** length defect tends to zero because `L_{a,c}->infinity`, while the additive defect tends to a fixed positive constant determined by the left exterior gap.

Now fix real `sigma>0`. From (7), as `L->infinity`,

\[
\boxed{
Q_\sigma(L)
=L e^{-\sigma L}(1+o(1)),}
\tag{60}
\]

because the `k=1` term dominates and `1-e^{-L}->1`. Equations (59)--(60) give

\[
\frac{Q_\sigma(L_{a,c}^+)}
{Q_\sigma(L_{a,c})}
\longrightarrow
e^{-\sigma\delta_a}<1.
\tag{61}
\]

Thus the relative terms in (14) are eventually negative, with

\[
\boxed{
|Q_\sigma(L_{a,c}^+)-Q_\sigma(L_{a,c})|
\asymp
L_{a,c}e^{-\sigma L_{a,c}}.}
\tag{62}
\]

For fixed `a`, (32)--(33) give

\[
c_1\log c
\le L_{a,c}
\le4\log c+C_a
\tag{63}
\]

for all sufficiently large right primes `c`. Therefore

\[
L_{a,c}e^{-\sigma L_{a,c}}
\ge
C_{a,\sigma}
(\log c)c^{-4\sigma}.
\tag{64}
\]

If `0<sigma<=1/4`, then

\[
(\log c)c^{-4\sigma}
\ge \frac1c
\tag{65}
\]

for all sufficiently large `c`. Euler's divergence of the reciprocal-prime sum now gives

\[
\sum_{c\ {\rm prime}}
|Q_\sigma(L_{a,c}^+)-Q_\sigma(L_{a,c})|
=\infty.
\tag{66}
\]

Because the terms have one eventual sign, the unmodulated subseries itself diverges to `-infinity`. This proves the sharpness assertion.

The statement is intentionally real-axis and series-level. It does **not** rule out an independently justified analytic or meromorphic continuation of some future regularized full object through `Re s=1/4`.

## 7. Relation to PF-069, PF-156 and PF-157

PF-069 proves that a concrete 3-gap subfamily of these same PF-004 primitive separators has a nondegenerate interval of positive length accumulation. Consequently the absolute primitive Selberg orbital measure has infinite mass on every open subinterval of that interval, even after all short geodesics are deleted. That result kills any attempt to repair the ordinary absolute Selberg product merely by factoring the pinching sector.

PF-156 and PF-157 then show the opposite phenomenon after **matched subtraction** for the complete Margulis-short source family: repeated short-orbit packets cancel distributionally, and the corresponding relative local-factor cocycle is zero-free on `Re s>0`.

PF-158 connects the two regimes. The same exact prime/shift matching controls the whole canonical separator family:

```text
near/comparable spans:
    O(a) candidate blocks at left scale a
    x O(a^-3) matched Selberg-factor defect
    -> absolute summability, including PF-069 accumulation

far spans:
    L ~ logarithmic in the right endpoint
    + exponential Selberg damping
    + dyadic fractional prime-gap moment
    -> local-normal convergence exactly for Re s > 1/4
```

Thus neither the pinching canonical sector nor the positive-length accumulation sector supplies a relative critical-line divisor.

## 8. Prior art and novelty audit

No novelty is claimed for the local Selberg factor, its logarithmic derivative, elementary dyadic concavity, or the general principle that sufficiently fast orbit growth controls an Euler-product abscissa.

PF-157 already audits the classical finite-geometry pinching literature: Jorgenson--Lundelius, Schulze, and Avdispahić--Jorgenson--Smajlović isolate local factors for finitely many pinched geodesics in finite-volume or finite-geometry degenerating families. Those theorems do not treat one fixed infinite-type surface with infinitely many canonical primitive classes and non-locally-finite absolute orbital measure.

The standard infinite-area Selberg theory also lives in a different regime. Borthwick--Judge--Perry, *Selberg's zeta function and the spectral geometry of geometrically finite hyperbolic surfaces*, Comment. Math. Helv. 80 (2005), 483--515, DOI `10.4171/CMH/23`, develops the zeta/scattering/resonance relation for **geometrically finite / finite-geometry** surfaces. Convex-cocompact transfer-operator results, including the classical Ruelle framework and later explicit work such as Pollicott--Vytnova on symmetric infinite-area surfaces, likewise rely on a recurrent hyperbolic system with the usual discrete periodic-orbit growth. PF-069 shows that the prime flute is outside that ordinary orbit-counting setting already at the level of the explicit canonical primitive family.

Directed searches for combinations of relative Selberg zeta, infinitely generated Fuchsian groups, infinite-type hyperbolic surfaces, non-discrete length spectra, and relative length-spectrum products recovered the finite-geometry/geometrically-finite theories above but did not locate a theorem that directly supplies the matched canonical-family result (9)--(12), much less the project-specific sharpness mechanism (57)--(66).

The durable content is therefore the exact composition

\[
\boxed{
\begin{array}{c}
\text{PF-004 exact multi-gap separator geometry}\\
+\ \text{PF-106/PF-109 exact all-composite matching}\\
+\ \text{BHP sublinear consecutive-gap envelope}\\
+\ \text{standard local Selberg factor}
\end{array}
\Longrightarrow
\begin{array}{c}
\text{full canonical-sector relative cocycle}\\
\text{zero-free on }Re\,s>1/4,\\
\text{with sharp positive-real abscissa }1/4.
\end{array}}
\tag{67}
\]

This is a **prime-flute boundary result**, not a new general theorem about Selberg zeta functions.

## 9. Scope, adversarial controls, and falsification boundary

The strongest tempting overstatement is explicitly excluded:

\[
D_{\rm can}
\ne
\text{a proved full relative Selberg zeta of }(X_+,X).
\tag{68}
\]

The canonical family is natural and geometrically intrinsic, but it is still a selected primitive sector. PF-158 does not control:

- noncanonical primitive closed geodesics / general reduced words in the infinitely generated Fuchsian group;
- possible primitive families that wind through many pants without being PF-004 consecutive-block separators;
- cusp scattering or parabolic continuous-spectrum contributions;
- a full relative trace formula;
- the global squared-resolvent `S_1` gate of PF-146--PF-148;
- wave-operator completeness;
- resonances or meromorphic continuation of the full Laplace resolvent;
- equality or existence of full Selberg/Ruelle determinants;
- any correspondence with Riemann zeros.

The boundary `Re s=1/4` is likewise not an arithmetic critical line. It comes from the geometric count of arbitrarily far **canonical** right endpoints against their `L~4 log c` Selberg damping. Equation (66) says the natural matched series cannot be extended there by ordinary convergence; it says nothing about a separately motivated regularization or continuation.

A later adversary can audit the finding through the following finite chain:

1. verify PF-004's exact cross-ratio and separator length (4);
2. verify PF-106's all-span additive `O(a^-3)` length defect and PF-109's multiplicative `O(a^-3)` defect;
3. differentiate the standard local Selberg logarithmic derivative and check the long-length bound (20);
4. verify the hybrid short/long estimate (22);
5. for `c>=4a`, derive the lower cross-ratio bound (32) and upper logarithmic-length bound (34);
6. check the dyadic fractional-gap estimate (41) from disjoint consecutive-prime intervals and concavity with `2rho<1`;
7. sum (42) dyadically and confirm that the exact convergence condition is `rho>1/4`;
8. for one fixed left gap, use the monotone endpoint displacement to prove `X^+<X`, then check the cross-ratio limit (57) and additive length limit (59);
9. verify the one-term large-`L` Selberg asymptotic (60) and reduce real-axis divergence at `sigma<=1/4` to Euler's `sum_p 1/p=infinity`;
10. keep the selected-sector and no-continuation caveats in (68).

A refutation would have to break one of those explicit steps. Failure to construct a **full** relative Selberg zeta would not refute PF-158; that broader object is deliberately not claimed.

## Research consequence

PF-157 left “longer primitive classes” as one of the places where a future full relative zeta/scattering mechanism could still acquire critical-line zeros. PF-158 removes the largest explicitly computable part of that escape:

\[
\boxed{
\text{all PF-004 canonical multi-gap separators, at every length scale,}
\quad
\Longrightarrow
\quad
\text{zero-free matched relative Selberg cocycle on }Re\,s>1/4.
}
\]

Since `1/2>1/4`, **none of the exact canonical consecutive-block geometry produces a matched relative zero on the RH line**. Any surviving prime-flute Selberg/scattering mechanism must therefore come from genuinely noncanonical primitive words, global operator/scattering coupling, or an independently justified continuation that uses information absent from this entire canonical sector.