# ANF-121 — triangular-notch fatal slope stays uniformly below pointwise source efficiency

**Status:** `EXACT-DERIVED + FIXED-NOTCH + UNIFORM-EFFICIENCY-GAP + NEGATIVE/OBSTRUCTION + HILBERT-ONLY-BOUNDARY`. `ANF-120` reduces every bounded-mass off-notch companion to a corridor controlled by the pointwise source efficiency

\[
\chi_\eta
=\operatorname*{ess\,sup}_{|\alpha|\le1}
\frac{\phi_\eta(\alpha)}{J_0(\alpha)}
\]

of the frozen central notch. Its easy positive branch would close the ray immediately if `chi_eta < B_eta`, where `B_eta` is the fatal affine slope from `ANF-099`; near equality `B_eta \approx chi_eta` would also force strong saddle mirroring. For the canonical triangular notch family this mechanism has a uniform obstruction: **the fatal slope is always strictly below the pointwise source efficiency, for every width `0<eta<1`, with a width-independent gap.**

Retain

\[
J_0=J_{\rm MT},
\qquad
\phi_\eta(\alpha)
=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad
b_\eta
=\min\left\{1,\min_{|\alpha|\le\eta}J_0(\alpha)\right\}>0,
\tag{1}
\]

and write

\[
C_0=C(J_0),
\qquad
B_\eta
=\frac{C(\phi_\eta)}{C_0}
=\frac{b_\eta(1+\eta^2/3)}{C_0}.
\tag{2}
\]

Then, for every `0<eta<1`,

\[
\boxed{
\frac{\chi_\eta}{B_\eta}
>
\frac{13125}{13072}
>1.
}
\tag{3}
\]

Equivalently,

\[
\boxed{
1-\frac{B_\eta}{\chi_\eta}
>
\frac{53}{13125}.
}
\tag{4}
\]

Thus the `chi_eta < B_eta` branch of `ANF-120` is impossible for the entire canonical triangular-notch family, not merely for the sufficiently narrow notches already screened abstractly in `ANF-099`. More importantly, the actual fatal threshold remains uniformly separated from pointwise efficiency saturation. Consequently the Hilbert-space corridor of `ANF-120`, even together with the exact Montgomery--Taylor profile, cannot force bounded-mass mirroring merely from exposure at the fatal level `B_eta`; the remaining step is genuinely physical realizability of source-generated exponential sums.

## 1. The Montgomery--Taylor source has an elementary closed form on the band

Use the exact factorization from `ANF-030`. Put

\[
\theta=2^{-1/2},
\qquad
g(u)=
\frac{\cos(\sqrt2\,u)}{\sqrt2\sin\theta}
\mathbf 1_{[-1/2,1/2]}(u),
\qquad
J_0=g*g.
\tag{5}
\]

For `0<=x<=1`, the overlap of the two supports is `u in [x-1/2,1/2]`. Product-to-sum therefore gives directly

\[
\boxed{
J_0(x)
=
\frac{
\sin(\sqrt2(1-x))/\sqrt2
+(1-x)\cos(\sqrt2 x)
}{4\sin^2\theta}.
}
\tag{6}
\]

Let

\[
t:=\theta\cot\theta.
\tag{7}
\]

The exact Montgomery--Taylor cost from `ANF-030` is

\[
C_0=\frac12+t.
\tag{8}
\]

At the center, (6) simplifies to

\[
J_0(0)
=
\frac{1+2t+2t^2}{4},
\tag{9}
\]

because `theta^2=1/2`. Hence

\[
\boxed{
\frac{C_0}{J_0(0)}
=
R(t)
:=
\frac{2(1+2t)}{1+2t+2t^2},
\qquad
R'(t)
=-\frac{8t(t+1)}{(1+2t+2t^2)^2}<0.
}
\tag{10}
\]

Only two elementary point evaluations of `phi_eta/J_0` will be needed. Since `J_0` is strictly positive on `(-1,1)`, that ratio is continuous at both points used below; therefore the point values are legitimate lower bounds for the **essential** supremum `chi_eta`.

## 2. Widths up to `24/25` are already separated at the center

The alternating Taylor bounds at `theta=1/sqrt2` give

\[
\cos\theta
<1-\frac{\theta^2}{2}+\frac{\theta^4}{24}
=\frac{73}{96},
\qquad
\sin\theta
>\theta-\frac{\theta^3}{6}
=\frac{11}{12}\theta.
\tag{11}
\]

Thus

\[
t=\theta\frac{\cos\theta}{\sin\theta}
<\frac{73}{88}
<\frac56.
\tag{12}
\]

By the monotonicity in (10),

\[
\frac{C_0}{J_0(0)}
>R(5/6)
=\frac{96}{73}.
\tag{13}
\]

At `alpha=0`, equation (1) gives `phi_eta(0)=b_eta`, so continuity yields

\[
\frac{\chi_\eta}{B_\eta}
\ge
\frac{C_0}{J_0(0)(1+\eta^2/3)}.
\tag{14}
\]

If `0<eta<=24/25`, then

\[
1+\frac{\eta^2}{3}
\le
1+\frac1{3}\left(\frac{24}{25}\right)^2
=\frac{817}{625},
\tag{15}
\]

and hence

\[
\boxed{
\frac{\chi_\eta}{B_\eta}
>
\frac{96}{73}\frac{625}{817}
=
\frac{60000}{59641}
>1.
}
\tag{16}
\]

This extends the small-`eta` control already implicit in the abstract Fejer stress test of `ANF-099` to an explicit large interval of notch widths, with no asymptotics.

## 3. Wider notches are separated by one fixed interior frequency

For the complementary range we use the fixed point `x=3/4`. First obtain a lower bound for `C_0`. Alternating Taylor bounds give

\[
\cos\theta
>
1-\frac{\theta^2}{2}
+\frac{\theta^4}{24}
-\frac{\theta^6}{720}
=\frac{4379}{5760},
\tag{17}
\]

and

\[
\sin\theta
<
\theta-\frac{\theta^3}{6}
+\frac{\theta^5}{120}
=\frac{147}{160}\theta.
\tag{18}
\]

Therefore

\[
t
>\frac{4379}{5292}
>\frac{41}{50},
\qquad
\boxed{C_0>\frac{33}{25}.}
\tag{19}
\]

Equation (6) at `x=3/4` is

\[
J_0(3/4)
=
\frac{
\sin(\theta/2)/(2\theta)
+\frac14\cos(3\theta/2)
}{4\sin^2\theta}.
\tag{20}
\]

Let `y=theta/2`, so `y^2=1/8`. Since

\[
\frac{\sin y}{2\theta}
=\frac14\frac{\sin y}{y}
<
\frac14\left(1-\frac{y^2}{6}+\frac{y^4}{120}\right)
=\frac{2507}{10240},
\tag{21}
\]

while `(3theta/2)^2=9/8` gives

\[
\cos(3\theta/2)
<1-\frac{9}{16}+\frac{81}{1536}
=\frac{251}{512},
\tag{22}
\]

the numerator in (20) is strictly below `1881/5120`. Also (11) yields

\[
4\sin^2\theta
>\frac{121}{72}.
\tag{23}
\]

Consequently

\[
J_0(3/4)
<
\frac{1539}{7040}
<\frac{11}{50}.
\tag{24}
\]

Combining (19) and (24),

\[
\boxed{
\frac{J_0(3/4)}{C_0}<\frac16.
}
\tag{25}
\]

Now suppose `24/25<=eta<1`. Since `3/4<eta`, continuity at `alpha=3/4` gives

\[
\frac{\chi_\eta}{B_\eta}
\ge
\frac{
C_0(1-3/(4\eta))
}{
J_0(3/4)(1+\eta^2/3)
}
>
F(\eta),
\tag{26}
\]

where

\[
F(\eta)
:=
\frac{6(1-3/(4\eta))}{1+\eta^2/3}
=
\frac92\frac{4\eta-3}{\eta(3+\eta^2)}.
\tag{27}
\]

A direct derivative gives

\[
F'(\eta)
=
\frac{9(9+9\eta^2-8\eta^3)}
{2\eta^2(3+\eta^2)^2}
>0
\qquad(0<\eta\le1),
\tag{28}
\]

because `8 eta^3<=8 eta^2`. Hence

\[
\boxed{
\frac{\chi_\eta}{B_\eta}
>
F(24/25)
=
\frac{13125}{13072}
>1.
}
\tag{29}
\]

Since

\[
\frac{60000}{59641}
>
\frac{13125}{13072},
\tag{30}
\]

equations (16) and (29) prove the uniform statement (3).

## 4. Fatal exposure remains uniformly below the mirroring regime

Taking reciprocals in (3) gives

\[
\frac{B_\eta}{\chi_\eta}
<
\frac{13072}{13125}
=1-\frac{53}{13125},
\tag{31}
\]

which proves (4). Thus even a sequence sitting exactly at the fatal exposure threshold of `ANF-099`, `h_eta -> B_eta`, stays a fixed positive distance from the efficiency-saturation regime `h_eta/chi_eta ->1` that forces bounded-mass mirroring in `ANF-120`.

This is not merely a loose constant in the proof. The two-band Hilbert model of `ANF-120` converts the gap into an explicit adversarial control. Put

\[
\varepsilon_*:=\frac{53}{13125},
\qquad
\delta_*:=\frac{\varepsilon_*}{2}
=\frac{53}{26250},
\tag{32}
\]

and in that model choose

\[
M=1,
\qquad
X=1-2\sqrt{\delta_*}.
\tag{33}
\]

Then the corridor mismatch tax is nonzero,

\[
\frac{(M-X)^2}{4M}=\delta_*,
\tag{34}
\]

while the saturating notch exposure is

\[
h=\chi_\eta(1-\delta_*).
\tag{35}
\]

Equation (31) implies

\[
1-\delta_*
>
1-\varepsilon_*
>
\frac{B_\eta}{\chi_\eta},
\]

so

\[
\boxed{h>B_\eta}
\tag{36}
\]

for **every** `0<eta<1`, despite the fixed nonzero mismatch (34). Hence no argument using only the affine defect identity, Hilbert-space polarization, and pointwise domination `phi_eta<=chi_eta J_0` can turn the fatal threshold into profile mirroring. `ANF-120` was already sharp abstractly; the present result shows that its sharpness is relevant at the actual triangular-notch decision slope, uniformly over all notch widths.

The model in (32)--(36) is deliberately abstract. It is not asserted to arise from a physical conjugation-invariant multiset, and therefore does **not** prove `beta_eta>=B_eta` or kill the fixed notch ray. Its role is to remove the remaining scalar/Hilbert shortcut. The live question is now exactly the one anticipated by `ANF-120`: whether the physical exponential-sum class can realize enough simultaneous off-notch anti-alignment and central-notch-efficient mass, or whether source-generated structure forces a stronger inequality than the pointwise efficiency ceiling.

## 5. Prior-art boundary and evidence limit

The Montgomery--Taylor extremal profile and its cost are classical inputs already anchored through Carneiro--Chandee--Littmann--Milinovich in `SOURCES.md`. The convolution formula (6), the rational Taylor bounds, and the one-variable comparison above are elementary consequences of that profile. A targeted literature audit around the Montgomery--Taylor extremizer, pair-correlation extremal functions, and triangular/central spectral perturbations did not locate the specific all-width comparison (3); no external theorem is needed for it, so this finding adds no new `SOURCES.md` dependency and makes no absolute novelty claim.

This result does not estimate the physical near-extremizer envelope `beta_eta`, construct a fatal configuration, improve the unconditional zeta-zero proportion, or prove RH. It establishes a sharper boundary: for the canonical triangular notch, **pointwise source efficiency is uniformly too permissive to decide the frozen ray**. Any closure of `beta_eta<B_eta` must use information lost by the scalar domination `phi_eta<=chi_eta J_0`, such as the realizability and coupled-frequency structure of the actual Montgomery--Taylor exponential sums.
