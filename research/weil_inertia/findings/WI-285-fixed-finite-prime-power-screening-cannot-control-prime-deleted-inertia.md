# WI-285 — fixed finite prime-power screening cannot control prime-deleted inertia

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the support-sensitive prime-deleted spectral target opened by `WI-284`. This finding tests whether the `WI-281` packing information, strengthened from the powers of `2` to the powers of any prescribed **fixed finite set of primes**, can force the restricted gamma-plus-pole form toward nonnegativity.
- **Result:** it cannot. For every fixed finite prime set, arbitrarily small support measure, and arbitrarily large requested negative Rayleigh quotient, there are arbitrarily large apertures carrying a full-span support that screens every power of those primes while the prime-deleted form has a supported odd vector with Rayleigh quotient below the requested negative level. In fact the supported quotient tends to `-infinity` along the construction.
- **What it does not claim:** this does not construct a Suzuki null mode, does not satisfy complete screening for **all** active prime powers as the aperture grows, does not refute `WI-284`, and does not show that the actual first-crossing support can have this geometry. It rules out any argument that tries to close `WI-284` using only a fixed finite collection of prime-base power lattices, support measure, span, or their associated packing constraints.
- **Novelty boundary:** Suzuki supplies the exact localized Weil form and `WI-240` records its odd pole factorization. Avoiding finitely many arithmetic lattices by a measure count is elementary. The line-local content is their combination into a support-sensitive obstruction: fixed finite prime-power screening is compatible with arbitrarily negative **restricted** prime-deleted energy even on arbitrarily sparse full-span supports. No historical priority claim is made.

## Claim

Let

\[
\mathcal P=\{p_1,\ldots,p_J\}
\tag{1}
\]

be any nonempty finite set of primes, and put

\[
L_j:=\log p_j.
\tag{2}
\]

Let `q_arch^a` denote the exact prime-deleted gamma-plus-pole form used in `WI-240` and `WI-284`. Then for every

\[
\varepsilon>0,
\qquad
M>0,
\tag{3}
\]

there exist arbitrarily large apertures `a` and open sets

\[
E\subset(-a,a)
\tag{4}
\]

such that

\[
|E|<\varepsilon,
\tag{5}
\]

\[
\operatorname*{ess\,inf}E=-a,
\qquad
\operatorname*{ess\,sup}E=a,
\tag{6}
\]

and

\[
\boxed{
|E\cap(E-k\log p)|=0
\quad
(p\in\mathcal P,\ k\ge1).
}
\tag{7}
\]

Nevertheless there is a real odd nonzero

\[
u\in\mathfrak D(q_{\rm arch}^a),
\qquad
u=0\ \text{a.e. on }E^c,
\tag{8}
\]

for which

\[
\boxed{
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}<-M.
}
\tag{9}
\]

Equivalently, if

\[
\mathfrak D_E:=\mathfrak D(q_{\rm arch}^a)\cap L^2(E),
\tag{10}
\]

then the restricted bottom obeys

\[
\inf_{0\ne u\in\mathfrak D_E}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}<-M.
\tag{11}
\]

Moreover `E` can be the positivity set of a normalized nonnegative smooth form-domain profile `v`; for that profile

\[
C_v(k\log p)=0
\quad
(p\in\mathcal P,\ k\ge1).
\tag{12}
\]

Thus even **exact screening of all powers of every prime in an arbitrary fixed finite prime family** does not give a lower bound, let alone the zero lower bound required by `WI-284`, for the prime-deleted form on the selected support.

## 1. A sparse two-component support can avoid every fixed prime-power lattice

Write

\[
S_{\mathcal P}:=\sum_{j=1}^J\frac1{L_j}.
\tag{13}
\]

Choose `b>0` so small that

\[
4b<\varepsilon,
\qquad
b<\frac14\min_jL_j,
\qquad
4bS_{\mathcal P}<1.
\tag{14}
\]

For `T>0`, consider the forbidden set of possible component separations

\[
\mathcal F_T
:=[T,2T]\cap
\bigcup_{j=1}^J\bigcup_{k\ge1}
(kL_j-2b,kL_j+2b).
\tag{15}
\]

For a fixed `j`, only `T/L_j+O(1)` lattice points `kL_j` have their `2b`-neighborhood meet `[T,2T]`. Therefore

\[
|\mathcal F_T|
\le
4bT\sum_{j=1}^J\frac1{L_j}
+O_{\mathcal P,b}(1)
=
4bS_{\mathcal P}T+O_{\mathcal P,b}(1).
\tag{16}
\]

Because `4bS_P<1`, the right side is strictly less than `T=|[T,2T]|` for all sufficiently large `T`. Hence there are arbitrarily large separations `Delta` satisfying

\[
\boxed{
\operatorname{dist}(\Delta,L_j\mathbb Z)\ge2b
\qquad(1\le j\le J).
}
\tag{17}
\]

For such a `Delta`, put

\[
R:=\frac\Delta2,
\qquad
a:=R+b,
\tag{18}
\]

and define

\[
E:=(-R-b,-R+b)\cup(R-b,R+b).
\tag{19}
\]

Then

\[
|E|=4b<\varepsilon,
\tag{20}
\]

and the essential span of `E` is the full aperture `(-a,a)`, giving (6).

Now fix `p_j` and `k>=1`, and set `d=kL_j`. A translate by `d` cannot overlap one component with itself because

\[
d\ge L_j>4b>2b.
\tag{21}
\]

An overlap between the two different components would require

\[
|d-\Delta|<2b,
\tag{22}
\]

which is forbidden by (17). Endpoint equality has zero measure. Hence (7) holds for every power of every prime in `P`.

Choose a standard real even bump

\[
0\le\phi\in C^\infty(\mathbb R),
\qquad
\{\phi>0\}=(-b,b),
\tag{23}
\]

flat at `+-b`, and set

\[
v_\Delta(x):=\phi(x-R)+\phi(x+R).
\tag{24}
\]

After normalization, `v_Delta>=0`, its positivity set is exactly `E`, it belongs to the localized form domain, and (7) immediately gives (12). Thus the support geometry is realized by an actual one-signed screened profile; no cancellation is being used to manufacture the vanishing autocorrelations.

## 2. The same screened support carries an odd direction with exponentially negative pole energy

On the same support define

\[
u_\Delta(x):=\phi(x-R)-\phi(x+R).
\tag{25}
\]

Because `phi` is even, `u_Delta` is real and odd. It belongs to the form domain and is supported in `E`.

`WI-240` records Suzuki's exact prime-deleted decomposition

\[
q_{\rm arch}^a(u)=G(u)+P_a(u),
\tag{26}
\]

where

\[
G(u)
=
\frac1{2\pi}\int_{\mathbb R}
 m(z)|\widehat u(z)|^2\,dz,
\qquad
m(z)=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi,
\tag{27}
\]

and, for odd real `u`, the pole term factors as

\[
\boxed{
P_a(u)=-2\left|\int_{-a}^{a}u(x)e^{x/2}\,dx\right|^2.
}
\tag{28}
\]

Set

\[
A_b:=\int_{\mathbb R}\phi(y)e^{y/2}\,dy>0.
\tag{29}
\]

Translation gives exactly

\[
\int u_\Delta(x)e^{x/2}\,dx
=
A_b\left(e^{R/2}-e^{-R/2}\right)
=2A_b\sinh(R/2).
\tag{30}
\]

Consequently

\[
\boxed{
P_a(u_\Delta)
=-8A_b^2\sinh^2(R/2)
=-8A_b^2\sinh^2(\Delta/4).
}
\tag{31}
\]

This tends to `-infinity` exponentially as the separation grows.

The gamma multiplier cannot compensate that growth. Translation only changes Fourier phases, so

\[
\widehat{u_\Delta}(z)
=
\left(e^{-izR}-e^{izR}\right)\widehat\phi(z),
\tag{32}
\]

and therefore

\[
|\widehat{u_\Delta}(z)|\le2|\widehat\phi(z)|.
\tag{33}
\]

The standard vertical-line digamma asymptotic gives

\[
|m(z)|\ll1+\log(2+|z|),
\tag{34}
\]

while `hat(phi)` is Schwartz. Hence

\[
|G(u_\Delta)|
\le
\frac4{2\pi}
\int_{\mathbb R}|m(z)|\,|\widehat\phi(z)|^2\,dz
=:C_\phi<\infty,
\tag{35}
\]

uniformly in `Delta`. Combining (31) and (35),

\[
q_{\rm arch}^a(u_\Delta)
\le
C_\phi-8A_b^2\sinh^2(\Delta/4)
\longrightarrow-\infty.
\tag{36}
\]

For large `Delta` the two translated bumps are disjoint, so

\[
\|u_\Delta\|_2^2=2\|\phi\|_2^2.
\tag{37}
\]

The norm is constant while (36) diverges negatively. Therefore the Rayleigh quotient tends to `-infinity`, proving (9)--(11) for any prescribed `M`.

This is stronger than merely importing the full-space negative index of `WI-240`: the negative direction has been exhibited **inside the same sparse support that realizes the prescribed prime-power screening**.

## 3. Why the aperture boundary causes no hidden domain problem

The choice `a=R+b` makes the positivity set have full essential span while the bump is flat at the two aperture endpoints. Thus `u_Delta` and `v_Delta` lie in the natural `H_0^1(-a,a)` form-domain class used in Suzuki's localized realization, even though their closed supports touch the boundary.

The pole factorization remains exact. Every difference `x-y` of points in the open aperture lies in `(-2a,2a)`; possible equality at an endpoint is null. Hence the truncation of Suzuki's pole kernel at `+-2a` does not change (28) for these functions. The finite prime translation perturbation is bounded at fixed `a`, so the full and prime-deleted forms have the same form domain, as already used in `WI-284`.

## 4. Consequence for the `WI-284` support-sensitive program

`WI-284` shows that a genuinely completely screened one-signed first-crossing support `E` would have to satisfy

\[
q_{\rm arch}^a\big|_{\mathfrak D_E}\ge0
\qquad\text{and}\qquad
\inf_{0\ne u\in\mathfrak D_E}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}=0.
\tag{38}
\]

The present construction proves that the strongest elementary packing information obtainable from **any fixed finite set of prime bases**, even when every positive power of every chosen prime is screened exactly, does not move in that direction. The compatible restricted bottom can instead be made arbitrarily negative.

Taking `P={2}` is already instructive. The support is a valid `log 2`-lattice selector of the kind forced by `WI-281`, its measure can be arbitrarily smaller than `log 2`, and yet

\[
\inf q_{\rm arch}^a|_{E}\to-\infty
\tag{39}
\]

along the separated two-bump family. Therefore there is no Faber--Krahn-type implication of the form

\[
|E|\le\log2
\quad\Longrightarrow\quad
q_{\rm arch}^a|_E\ge0
\tag{40}
\]

for the exact gamma-plus-pole form. Small **measure** is not a substitute for the small **diameter/window** that appears in classical compact-support positivity results; the polar cross-interaction detects the separation and has the opposite sign on the odd channel.

The same point persists for every fixed `J`. What changes in the actual `WI-284` hypothesis is that the active prime set grows with `a`. The counting argument (16) deliberately has coefficient

\[
4b\sum_{p\in\mathcal P}\frac1{\log p},
\tag{41}
\]

and supplies no uniform avoidance as the number of prime bases tends to infinity. Thus the full arithmetic diversity is precisely where the present obstruction stops.

A successful support-sensitive contradiction must therefore use at least one ingredient absent from this construction: the aperture-growing family of distinct prime bases, quantitative amplitudes from the actual null equation rather than zero-overlap topology alone, or another source-specific constraint tying the selected support to the exact first-crossing operator.

## 5. Optional maximal-support strengthening for a fixed finite lag family

At any one constructed aperture, only finitely many powers `k log p` with `p in P` lie below `2a`. Starting from the open set `E` above, the finite forbidden-distance saturation lemma used in `WI-283` may be applied to those lags. It gives a maximal open distance-avoiding extension `E_max` satisfying the corresponding fixed-family support-domination condition.

Because

\[
E\subset E_{\max},
\tag{42}
\]

the same vector `u_Delta` still belongs to the supported form domain of `E_max`, and its negative Rayleigh quotient is unchanged. Therefore even adding the `WI-283` maximal-support/domination topology for a **fixed finite prime-base family** does not repair the obstruction. This does not assert domination for the omitted active primes and hence does not bypass the complete-screening hypothesis of `WI-284`.

## 6. Prior-art and novelty audit

The load-bearing source is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026). Suzuki supplies the localized closed form, its exact gamma/von-Mangoldt/pole decomposition, and the form-domain framework. `WI-240` already derived from that source the exact odd identity (28) and used low-frequency dilation to prove unbounded full-space odd negative index.

Support-restricted minimization of Weil quadratic forms is classical in the Bombieri/Yoshida lineage, as already recorded in `WI-284`. Classical compact-window positivity results constrain functions whose support is contained in a short interval. They do not imply positivity from small support **measure** when the support has arbitrarily large diameter. The construction above gives an exact reason the distinction matters for Suzuki's prime-deleted form: the gamma contribution of separated translates stays uniformly bounded while the odd polar cross-term grows like `-exp(Delta/2)`.

Targeted prior-art searches around compact-window Weil positivity, support-restricted Weil variational problems, nonlocal Faber--Krahn inequalities, and sparse forbidden-distance supports did not locate an equivalent theorem asserting or refuting (9) under finite prime-power screening. General rearrangement/Faber--Krahn theorems for positive nonlocal kernels do not black-box apply because the exact gamma-plus-pole form is not a positive-kernel energy and its pole contribution is explicitly negative on the odd test family. Search absence is not used as a priority claim.

The novelty boundary is therefore narrow: neither the lattice-avoidance count nor the pole factorization is new. The substantive deduction is that they can be satisfied simultaneously on the **same support**, producing arbitrarily negative restricted prime-deleted inertia while preserving any prescribed finite family of prime-power screening constraints.

## 7. Stress tests and boundaries

- **All powers, not only the first lag:** condition (17) excludes `Delta` from the whole lattice `L_j Z`, and `L_j>2b` excludes same-component overlaps. Thus (7) really holds for every `k>=1`.
- **One-signed screening is genuine:** the auxiliary profile `v_Delta` is nonnegative, so its autocorrelation vanishing comes from support disjointness exactly as in `WI-281`, not cancellation.
- **The negative witness need not be the screened profile:** `WI-284` requires the prime-deleted form to be nonnegative on the *entire* supported form domain. To falsify that consequence it is enough to place any negative `u` in the same support; `u_Delta` is chosen odd precisely to expose the pole sign.
- **No claim for the full active prime set:** the finite-family hypothesis is essential. As `a` grows, complete Suzuki screening introduces new prime bases, and the coefficient in (41) is not controlled by this proof.
- **No hidden compact-window contradiction:** `|E|` is small but its diameter is `2a` and tends to infinity. Results depending on short containing intervals are in a different regime.
- **No inference from unrestricted negative index alone:** the proof explicitly constructs the support and its supported negative vector. It does not use a dimension-count argument to intersect an arbitrary negative subspace with a sparse `L^2(E)` space.
- **No RH assumption in the obstruction:** the construction is an exact statement about Suzuki's prime-deleted form and prescribed screening lattices. Its relevance to RH is conditional only through the `WI-284` first-crossing consequence it rules out as a finite-base strategy.

## 8. Research consequence

The support-sensitive target after `WI-284` cannot be closed by progressively strengthening the `log 2` packing argument through a **fixed** list of additional prime-power lattices. For every such finite list, the prime-deleted operator still admits screened sparse supports with arbitrarily negative restricted energy.

The remaining arithmetic distinction is now sharper:

\[
\boxed{
\text{finite prime-base screening}
\ \not\Longrightarrow\ 
q_{\rm arch}^a|_E\ge0,
}
\tag{43}
\]

whereas a hypothetical actual counterexample would require screening over an aperture-dependent prime family large enough to force

\[
q_{\rm arch}^a|_E\ge0
\quad\text{with bottom }0.
\tag{44}
\]

Any future contradiction should therefore exploit the **growth and diversity of the active prime set with the aperture**, or reinsert the amplitudes of the exact null equation. A bounded-prime truncation of the support geometry is provably too weak.