# PF-177 — collar Jacobian defect can be expelled from the collapsing core

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-176 shows that equal-area truncated pants admit boundary-fixed area-preserving corrections, but leaves a quantitative concern: a Moser/Jacobian correction might have to act inside arbitrarily collapsed short collars, where uniform derivative estimates are delicate. The exact PF-128 area coordinate removes that local concern. For matched standard collars with core lengths `L` and `L'=e^tL`, one can choose a smooth boundary-to-boundary comparison that is **exactly area preserving on the entire potentially collapsing region** `sqrt(L^2+x^2)<=1`; all Jacobian defect is pushed into a uniformly thick outer rim, where its metric and density size is only `O(|t|L^2)`. The unavoidable total collar-area mismatch is also `O(|t|L^2)`. For the complete PF-138 Margulis-short prime/shift family these thick-rim density budgets are summable. Thus a future global `rho=1` correction does not need to solve a prescribed-Jacobian problem inside the collapsed collar cores. What remains is a genuinely global thick-region redistribution/gluing problem: the source and target full standard collars have slightly different total areas, so no collar-by-collar area-preserving boundary-to-boundary map can exist unless `L=L'`. No global smooth area-preserving prime/shift marking, weighted body/interface estimate, density-unitary `S_r` result, wave/scattering equivalence, or RH consequence is claimed.

## Claim

For `0<L<L_0`, let

\[
C_L=(-w(L),w(L))\times\mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

with standard hyperbolic collar metric

\[
g_L=dr^2+L^2\cosh^2r\,d\theta^2.
\tag{2}
\]

Use PF-128's exact area coordinate

\[
\boxed{x=L\sinh r,}
\tag{3}
\]

so

\[
\boxed{
g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2,
\qquad d\mu_L=dx\,d\theta,}
\tag{4}
\]

and

\[
C_L\cong(-A(L),A(L))\times\mathbb S^1,
\qquad
A(L):=\frac{L}{\sinh(L/2)}=2+O(L^2).
\tag{5}
\]

Let

\[
L'=e^tL,
\qquad |t|\le t_0,
\tag{6}
\]

and put `A=A(L)`, `A'=A(L')`. For sufficiently small `L`, both `A,A'` exceed `3/2`.

Fix a smooth cutoff `eta:[0,1]->[0,1]` with `eta=0` near `0`, `eta=1` near `1`, and bounded derivatives. Define an odd smooth function `phi:[-A,A]->[-A',A']` by

\[
\phi(x)=x
\qquad(|x|\le1),
\tag{7}
\]

and, for `1<=x<=A`,

\[
\boxed{
\phi(x)
=x+(A'-A)\,
\eta\!\left(\frac{x-1}{A-1}\right),
}
\tag{8}
\]

with `phi(-x)=-phi(x)`. After shrinking `L_0` if necessary, `phi'>0`, and

\[
\Phi_{L,L'}(x,\theta):=(\phi(x),\theta)
\tag{9}
\]

is a smooth reflection-equivariant boundary-to-boundary diffeomorphism of the two standard collars.

Let

\[
h:=\Phi_{L,L'}^*g_{L'},
\qquad
\rho:=\frac{d\mu_h}{d\mu_L}.
\tag{10}
\]

Then:

1. on the complete central region `|x|<=1`,
   \[
   \boxed{\rho\equiv1;}
   \tag{11}
   \]
2. for the Güneysu--Thalmaier metric-deviation scalar, uniformly for bounded `t`,
   \[
   \boxed{
   \delta_{g_L,h}(x)
   \le C|t|\frac{L^2}{x^2+L^2}
   \qquad(|x|\le1);
   }
   \tag{12}
   \]
3. on the outer rim `1<=|x|<=A`,
   \[
   \boxed{
   \delta_{g_L,h}(x)+|\rho(x)-1|
   \le C|t|L^2;
   }
   \tag{13}
   \]
4. if
   \[
   W_L(z):=\mu_L(B_{g_L}(z,1))^{-1},
   \tag{14}
   \]
   then for every `r>=1`,
   \[
   \boxed{
   \int_{C_L}W_L\,\delta_{g_L,h}^{\,r}\,d\mu_L
   \le C_r|t|^r,
   }
   \tag{15}
   \]
   while the entire density-identification defect satisfies the strictly smaller thick-rim estimate
   \[
   \boxed{
   \int_{C_L}W_L\,|\rho-1|^r\,d\mu_L
   \le C_r|t|^rL^{2r}.
   }
   \tag{16}
   \]
   The analogous target-weighted estimates follow from the inverse map with `t` replaced by `-t`.

Finally, the total signed density defect is fixed by area conservation:

\[
\boxed{
\int_{C_L}(\rho-1)d\mu_L
=2\bigl(A(L')-A(L)\bigr)
=O(|t|L^2).
}
\tag{17}
\]

Since `A(L)` is strictly decreasing for small positive `L`, the two full standard collars have unequal area whenever `L\ne L'`. Therefore there is **no** area-preserving diffeomorphism from the source full standard collar onto the target full standard collar. Any global `rho=1` construction must compensate this small area discrepancy in the complementary geometry or move the chosen collar interface.

For the complete PF-138 family of Margulis-short prime/shift separators, with `t_eta=O(P^{-3})` and multiplicity `O(P^{0.525})` on prime scale `P`, equations (15)--(16) give for every `r>=1`

\[
\boxed{
\sum_{\eta}
\int_{C_\eta}W_\eta\,\delta_\eta^{\,r}d\mu_\eta
<\infty,
\qquad
\sum_{\eta}
\int_{C_\eta}W_\eta\,|\rho_\eta-1|^r d\mu_\eta
<\infty.
}
\tag{18}
\]

More importantly for PF-176, every `rho_eta-1` in this gauge is supported where the source unit-ball volume has a uniform positive lower bound. The collapsing cores themselves require no volume correction.

## 1. The collar area coordinate exposes the right gauge freedom

PF-128 already observed that (3) makes the hyperbolic area form exactly Lebesgue:

\[
d\mu_L=dx\,d\theta.
\tag{19}
\]

It used the uniform scaling `x->alpha x`, with `alpha=A'/A`, to map the full collar boundary to boundary. That is optimal for its local scattering estimate, but its pulled-back area ratio is the nontrivial constant `alpha` throughout the collar.

For the volume-gauge problem there is a better choice. The dangerous region for the inverse-unit-ball weight is characterized by

\[
s(x):=\sqrt{L^2+x^2}\lesssim1.
\tag{20}
\]

The fixed subcollar `|x|<=1` contains this entire potentially collapsing sector for small `L`. Because the area coordinate itself does not depend on `L`, simply keeping `x` fixed there gives an exact Jacobian-one comparison. The tiny adjustment needed to hit the target outer standard-collar boundary can be postponed until `|x|>=1`, where the geometry is uniformly thick.

This is not a Moser argument; it is an explicit gauge choice in the exact collar coordinates.

## 2. The outer boundary displacement is only `O(|t|L^2)`

PF-128 computes

\[
\frac{d}{d\log L}\log A(L)
=1-\frac L2\coth\frac L2
=O(L^2).
\tag{21}
\]

Integrating from `L` to `L'=e^tL` gives

\[
\boxed{
|A'-A|\le C_{t_0}|t|L^2.
}
\tag{22}
\]

Since `A-1` stays bounded above and below on the short-collar regime, differentiating (8) yields

\[
\boxed{
|\phi(x)-x|+|\phi'(x)-1|
\le C|t|L^2
\qquad(1\le|x|\le A).
}
\tag{23}
\]

The cutoff is constant near both ends, so `phi=x` in a neighborhood of the inner interface `|x|=1`, while near the outer boundary `phi(x)=x+(A'-A)\operatorname{sgn}(x)` with `phi'=1`. Thus no derivative kink is introduced at the interface or at the standard-collar boundary.

Equation (23) also makes `phi` strictly monotone for small enough `L`, proving that (9) is a diffeomorphism.

## 3. The volume ratio is exactly one where collapse matters

Pulling back the target metric gives

\[
\boxed{
h
=\frac{\phi'(x)^2dx^2}{L'^2+\phi(x)^2}
+\bigl(L'^2+\phi(x)^2\bigr)d\theta^2.}
\tag{24}
\]

Relative to `g_L`, the two metric eigenvalues are

\[
\lambda_x
=\phi'(x)^2\frac{L^2+x^2}{L'^2+\phi(x)^2},
\qquad
\lambda_\theta
=\frac{L'^2+\phi(x)^2}{L^2+x^2}.
\tag{25}
\]

Their product is `phi'(x)^2`, so orientation preservation gives the exact area ratio

\[
\boxed{\rho(x)=\phi'(x).}
\tag{26}
\]

On `|x|<=1`, `phi=x` and therefore (11) is exact. There the eigenvalues are reciprocal:

\[
\lambda_x
=\frac{L^2+x^2}{L'^2+x^2},
\qquad
\lambda_\theta=\lambda_x^{-1}.
\tag{27}
\]

For bounded `t`,

\[
|L'^2-L^2|\le C|t|L^2,
\tag{28}
\]

so

\[
|\log\lambda_x|+|\log\lambda_\theta|
\le C|t|\frac{L^2}{x^2+L^2}.
\tag{29}
\]

The finite-dimensional comparison between these logarithmic metric eigenvalues and the Güneysu--Thalmaier deviation gives (12).

On the outer rim, `x^2+L^2>=1`, while (23) and (28) make every entry of the relative metric matrix `I+O(|t|L^2)`. Equation (26) gives the density estimate simultaneously, proving (13).

The important distinction is therefore

\[
\boxed{
\text{thin core: }\rho-1=0\text{ exactly, metric strain allowed};
\qquad
\text{thick rim: }\rho-1=O(|t|L^2).
}
\tag{30}
\]

Area preservation removes the identification defect without pretending that the two collar metrics are isometric.

## 4. Weighted estimates retain the full PF-174 scale

PF-128 proves the ambient unit-ball lower bound

\[
\mu_L(B_{g_L}(z,1))
\ge c\min\{1,\sqrt{L^2+x^2}\}.
\tag{31}
\]

On `|x|<=1`, combine (12) with (31):

\[
\begin{aligned}
\int_{|x|\le1}W_L\,\delta^r\,d\mu_L
&\le
C_r|t|^rL^{2r}
\int_{-1}^{1}(x^2+L^2)^{-r-1/2}dx\\
&\le
C_r|t|^r
\int_{\mathbb R}(1+u^2)^{-r-1/2}du\\
&\le C_r'|t|^r.
\end{aligned}
\tag{32}
\]

For `|x|>=1`, the unit-ball weight is uniformly bounded and (13) gives an `O(|t|^rL^{2r})` contribution. This proves (15).

The density term is even simpler. It vanishes identically on `|x|<=1`, and its support lies in the uniformly thick rim. Therefore

\[
\int W_L|\rho-1|^r d\mu_L
\le C_r|t|^rL^{2r},
\tag{33}
\]

which is (16). Applying the same argument to the inverse map proves the target-weighted version required by PF-175's two-sided hypothesis whenever the surrounding body/interface comparison is controlled.

Thus PF-177 does not improve PF-174's already-sharp short-collar metric exponent. Its new content is **where the Jacobian defect can be placed**: entirely outside the collapsing core.

## 5. Full-collar area conservation is the residual coupling

Because `Phi` maps the complete source standard collar onto the complete target standard collar,

\[
\int_{C_L}\rho\,d\mu_L
=\operatorname{Area}(C_{L'})
=2A'.
\tag{34}
\]

Subtracting `Area(C_L)=2A` gives (17). Equation (21) shows `A` is strictly decreasing for positive `L`, so `A'\ne A` whenever `L'\ne L`.

This gives a small but exact no-go:

\[
\boxed{
L\ne L'
\Longrightarrow
\text{no full-standard-collar boundary-to-boundary map can have }\rho\equiv1.
}
\tag{35}
\]

The qualitative pant-level Moser theorem in PF-176 is therefore not replaceable by independent volume corrections on every standard short collar. Equal area holds only after the collar discrepancy is allowed to exchange with complementary pant/body area.

But the coupling is now quantitatively mild. Equation (22) gives only `O(|t|L^2)` signed area to redistribute, and (13) places the corresponding density forcing in a uniformly thick region. The zero-injectivity-radius core need not participate in that redistribution.

## 6. The complete short-collar family has summable thick-rim forcing

PF-138 proves that every sufficiently far Margulis-short closed geodesic is a canonical consecutive-block separator. On a prime scale `P`, their multiplicity is `O(P^{0.525})`, while PF-109 gives

\[
|t_\eta|
=\left|\log\frac{L_\eta^+}{L_\eta}\right|
=O(P^{-3}).
\tag{36}
\]

Equations (15)--(16) imply

\[
\sum_\eta\int W\delta^r d\mu
\ll
\sum_P P^{0.525-3r}<\infty
\qquad(r\ge1),
\tag{37}
\]

recovering the PF-174 weighted metric scale in the new gauge. Since every Margulis-short `L_eta` is uniformly bounded,

\[
\sum_\eta\int W|\rho_\eta-1|^r d\mu
\ll
\sum_P P^{0.525-3r}L_\eta^{2r}<\infty.
\tag{38}
\]

At `r=1`, the total signed collar-area displacement is absolutely summable as well:

\[
\sum_\eta|A(L_\eta^+)-A(L_\eta)|
\le C\sum_\eta |t_\eta|L_\eta^2
<\infty.
\tag{39}
\]

Thus an eventual global volume correction sees the complete collapsed short-collar family only through an absolutely summable collection of **thick-rim** area imbalances.

PF-177 still does not show that these local imbalances can be redistributed by one globally coherent correction while preserving the PF-125/PF-139/PF-140 body traces and the PF-145 collar interfaces. That is now the remaining volume-gauge assembly question.

## 7. Prior art and novelty audit

No general theorem novelty is claimed. The standard collar coordinates, collar lemma, and inverse-unit-ball estimate are already audited in PF-128/PF-138/PF-174. Moser's volume-form theorem, Banyaga's boundary version, and Dacorogna--Moser prescribed-Jacobian theory are classical and were already separated from project-specific content in PF-176.

A directed search of the prescribed-Jacobian literature also finds Pedro Teixeira, *Dacorogna--Moser theorem on the Jacobian determinant equation with control of support*, Discrete Contin. Dyn. Syst. 37 (2017), 4071--4089, DOI `10.3934/dcds.2017173`, and his addendum `arXiv:1705.01416`. These results show, in their bounded-domain/pullback settings, that support control can be retained when the density discrepancy is supported away from a protected region. They do **not** provide the degeneration-uniform global derivative estimates or infinite-flute assembly still missing here.

The durable project-specific statement is the exact gauge decomposition

\[
\boxed{
\text{matched collapsing collar}
\Longrightarrow
\begin{cases}
\rho=1 & \text{on the entire collapsing core},\\
\rho-1=O(|t|L^2) & \text{on a uniformly thick rim},\\
\int(\rho-1)=2(A'-A) & \text{unavoidable but summable}.
\end{cases}}
\tag{40}
\]

No claim is made that this elementary collar gauge is itself new in hyperbolic geometry. Its value here is to remove one specific false source of difficulty from PF-176/PF-175: **Jacobian correction need not penetrate the short-collar collapse**.

## 8. Audit / falsification core

A later adversary can check PF-177 through a finite chain:

1. verify PF-128's exact area coordinate (3)--(5) and the derivative formula (21);
2. check that (8) maps `A` to `A'`, is identity on `|x|<=1`, and has `phi'=1+O(|t|L^2)`;
3. pull back the target metric and verify (24)--(26), especially `rho=phi'`;
4. on `|x|<=1`, verify the reciprocal eigenvalues (27) and the pointwise bound (29);
5. on the outer rim, use `|x|>=1` and (22)--(23) to obtain (13);
6. insert PF-128's unit-ball bound and rescale `x=Lu` to prove (32)--(33);
7. integrate `rho` over the complete collar to verify the exact area obstruction (34)--(35);
8. insert PF-138/PF-109's multiplicity and `O(P^{-3})` length-ratio defect to verify (37)--(39).

A failure of the global Moser/body/interface construction would **not** refute PF-177. It would show that the remaining obstruction lives in thick-region redistribution, boundary coherence, or global assembly rather than in the collapsing collar's local volume gauge.

## Consequence

PF-176's area-preserving route can now be narrowed once more. It is unnecessary to seek degeneration-uniform prescribed-Jacobian estimates inside every short collar. The local comparison may be frozen with `rho=1` throughout the whole potentially collapsing area-coordinate core, while its unavoidable `O(|t|L^2)` volume mismatch is exported to a uniformly thick rim with a summable family budget.

The live geometric task is therefore:

\[
\boxed{
\text{assemble the already-controlled thin gauges}
+\text{ redistribute their summable thick-rim area mismatch}
+\text{ preserve smooth body/interface coherence and weighted metric control}.
}
\tag{41}
\]

Only after that global thick-region step can PF-175's identity coincidence `J^\vee=I=U` be invoked to obtain the canonical density-unitary first-resolvent `S_r` conclusion for every `r>1`.