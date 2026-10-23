# NB-299 — large off-critical dilations make projected escape sample-null

- **Date:** 2026-09-23
- **Status:** proved (author derivation; strengthened estimates pending independent adversarial review)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-292, NB-294, NB-297, NB-298
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + FIRST-FREE-SAMPLING + PROJECTED-DILATION-ESCAPE + SHIFT-COMPRESSION-DECAY + OFF-CRITICAL-SAMPLE-CONTRACTION + BASELINE-FREE-NO-GO + SHARP-TARGET-DECAY + JOINT-FIXED-PACKET-NULL + MOVING-PACKET-GATE + PRIOR-ART-AUDITED`

## Claim

`NB-297` isolates the baseline-free projected dilation escape

\[
R_{m,n,Z}=(U+S_mU)\ominus U,
\qquad
U:=V_{n-1,Z},
\]

and its first-free sampling Gram

\[
\Xi_{m,n,Z}=L_ZP_{R_{m,n,Z}}L_Z^*.
\]

`NB-298` then shows that this block is only a subblock of the pre-existing future representer tail. In particular, for a fixed zero packet, going sufficiently deep in the ordinary section kills `Xi` uniformly in the dilation factor `m`.

There is a complementary no-go in the **other** large parameter. Fix a finite off-critical zero packet

\[
Z=\{\rho_1,\ldots,\rho_N\}\subset\{1/2<\Re s<1\},
\]

fix `n>=3`, and assume the first-free sampler is onto on

\[
U=V_{n-1,Z}.
\]

Then, as the integer dilation `m->infinity`, the projected source escape becomes asymptotically orthogonal to the old section **but simultaneously becomes first-free-sample-null**:

\[
\boxed{
\|P_US_m|_U\|\longrightarrow0,
\qquad
\|\Xi_{m,n,Z}\|\longrightarrow0.
}
\tag{1}
\]

The two limits express opposite effects. Large dilation maximizes the source-space principal-angle escape from `U`, but off-critical evaluation contracts every transported sample by

\[
D_Z(m)=\operatorname{diag}(m^{1/2-\rho_1},\ldots,m^{1/2-\rho_N}),
\qquad
\|D_Z(m)\|=m^{-\delta_Z},
\]

where

\[
\delta_Z:=\min_j(\Re\rho_j-1/2)>0.
\tag{2}
\]

The exact factorization from `NB-297` makes this quantitative. Let

\[
E_U:\mathbb C^d\to U,
\qquad d=n-2,
\]

be any isometric synthesis map, and put

\[
X:=L_ZE_U,
\qquad
T_m:=E_U^*S_mE_U,
\qquad
Q_m:=I-T_m^*T_m,
\]

\[
Y_m:=D_Z(m)X-XT_m.
\tag{3}
\]

Then

\[
\Xi_{m,n,Z}=Y_mQ_m^+Y_m^*.
\tag{4}
\]

Define the old-section source overlap

\[
\beta_n(m):=\|T_m\|.
\tag{5}
\]

For the actual canonical Nyman source,

\[
\boxed{
\beta_n(m)\le \frac{C_n}{\sqrt m}
}
\tag{6}
\]

with an explicit finite constant `C_n` depending only on the source section `V_(n-1)`, not on the zero packet `Z`. Consequently, whenever `C_n^2<m`,

\[
\boxed{
\|\Xi_{m,n,Z}\|
\le
\|K_{n-1,Z}\|
\frac{
\bigl(m^{-\delta_Z}+C_nm^{-1/2}\bigr)^2
}{
1-C_n^2/m
}.
}
\tag{7}
\]

Since every nontrivial zeta zero satisfies `Re rho<1`, one has `0<delta_Z<1/2`; for fixed `n,Z`, `(7)` therefore gives

\[
\boxed{
\|\Xi_{m,n,Z}\|=O_{n,Z}(m^{-2\delta_Z}).
}
\tag{8}
\]

The target consequence is equally direct. Let

\[
K:=K_{n-1,Z}\succ0,
\qquad
\mathcal C_U(y):=y^*K^{-1}y,
\]

and let

\[
\mathcal G_{m,n,Z}(y)
:=
\mathcal C_U(y)-\mathcal C_{U+R_{m,n,Z}}(y)
\]

be the baseline-free gain supplied by the projected dilation block. Then

\[
\boxed{
0\le
\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_U(y)}
\le
\min\left\{
1,
\kappa(K)
\frac{
\bigl(m^{-\delta_Z}+C_nm^{-1/2}\bigr)^2
}{
1-C_n^2/m
}
\right\}.
}
\tag{9}
\]

Thus for every fixed first-free datum `y!=0`, fixed packet `Z`, and fixed surjective old section,

\[
\boxed{
\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_U(y)}\longrightarrow0.
}
\tag{10}
\]

If the full finite-section excess from `NB-298` is nonzero, its projected-dilation occupation ratio also vanishes:

\[
\boxed{
\eta_{m,n,Z}(y)
=
\frac{\mathcal G_{m,n,Z}(y)}{\mathfrak A_U(y)}
\longrightarrow0.
}
\tag{11}
\]

This is not in conflict with `NB-294`. There the multiplicative quotient band becomes coercive **relative to the dilated old baseline**, whose sample Gram itself contracts like `D_Z(m)KD_Z(m)^*`. Here the old baseline is the ordinary undilated section `U`. Large off-critical dilation can therefore make the transported-baseline repair almost complete while making the canonical projected copy contribute asymptotically nothing to the ordinary finite-section improvement.

Combined with `NB-298`, there are now two boundary no-go results for the same baseline-free block:

\[
\sup_{m\ge2}\|\Xi_{m,n,Z}\|\to0
\quad(n\to\infty,\ Z\text{ fixed}),
\tag{12}
\]

while

\[
\|\Xi_{m,n,Z}\|\to0
\quad(m\to\infty,\ n,Z\text{ fixed}).
\tag{13}
\]

A surviving Ford-scale occupation theorem must therefore be genuinely **joint-scale**. It cannot be obtained merely by taking the ordinary section deep, nor merely by pushing the multiplicative dilation far out. The moving packet, cutoff, source concentration constant, sampling conditioning, and off-critical displacement must remain coupled.

More precisely, Sections 3a and 4a give a two-sided relative Gram estimate and the sharp fixed-datum rate. If `h=K^{-1}y!=0` and
\[
\delta(y):=\min_{j:h_j\ne0}(\Re\rho_j-1/2),
\]
then at fixed `n,Z,y`,
\[
\boxed{\mathcal G_{m,n,Z}(y)=\Theta_{n,Z,y}(m^{-2\delta(y)}).}
\tag{13a}
\]
The exponent is selected by the inverse-Gram-transformed datum, not by its raw coordinates. The leading coefficient can retain bounded oscillations in `log m`. Section 7 also combines the **uniform-in-dilation** deep-section bound with the fixed-section far-dilation limit: for fixed `Z`, the sample Gram and the target gain relative to the old cost vanish uniformly outside finite rectangles in `(n,m)`. Thus a moving cutoff and dilation cannot retain a nonzero such gain while the packet remains fixed. None of these conditional statements asserts that an off-critical zeta packet exists.

---

## 1. Source compression of a large dilation tends to zero

The source statement is independent of the selected zero packet. It is easiest to verify first in the canonical real-variable Nyman space.

Recall the canonical atoms from `NB-290`,

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\},
\qquad
2\le j,
\tag{14}
\]

and the isometric dilation

\[
(A_mf)(x)
=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{15}
\]

For fixed `n`, let

\[
U_n^{\rm can}:=\operatorname{span}\{g_2,\ldots,g_{n-1}\}.
\tag{16}
\]

Every vector in `A_mU_n^(can)` is supported in `(0,1/m]`. Hence for unit vectors `u,v in U_n^(can)`,

\[
|\langle u,A_mv\rangle|
\le
\|1_{(0,1/m]}u\|_2\,\|A_mv\|_2
=
\|1_{(0,1/m]}u\|_2.
\tag{17}
\]

Because `U_n^(can)` is finite-dimensional, its unit sphere is compact. The multiplication operators

\[
f\mapsto1_{(0,1/m]}f
\]

converge strongly to zero on `L^2(0,1)`, hence uniformly on that compact unit sphere. Therefore

\[
\sup_{\substack{u\in U_n^{\rm can}\\\|u\|=1}}
\|1_{(0,1/m]}u\|_2
\longrightarrow0.
\tag{18}
\]

It follows from `(17)` that

\[
\boxed{
\|P_{U_n^{\rm can}}A_m|_{U_n^{\rm can}}\|\to0.
}
\tag{19}
\]

So a far-out multiplicative dilation of a fixed finite Nyman section becomes asymptotically orthogonal to that section.

This qualitative argument is already enough for `(1)`. For the actual canonical atoms one also gets the elementary rate used in `(6)`.

Since each fractional part belongs to `[0,1)`,

\[
|g_j(x)|\le1+\frac1j.
\tag{20}
\]

Let

\[
G_{n-1}^{\rm src}
=
\bigl(\langle g_j,g_k\rangle\bigr)_{2\le j,k\le n-1},
\qquad
\lambda_n:=\lambda_{\min}(G_{n-1}^{\rm src})>0,
\tag{21}
\]

where positivity follows from the finite independence already proved in `NB-014`. Put

\[
B_n^2
:=
\sum_{j=2}^{n-1}\left(1+\frac1j\right)^2,
\qquad
C_n:=\frac{B_n}{\sqrt{\lambda_n}}.
\tag{22}
\]

If

\[
u=\sum_{j=2}^{n-1}a_jg_j,
\]

then Cauchy--Schwarz and `(20)` give

\[
\|u\|_\infty
\le B_n\|a\|_2.
\tag{23}
\]

At the same time,

\[
\|u\|_2^2
=a^*G_{n-1}^{\rm src}a
\ge\lambda_n\|a\|_2^2.
\tag{24}
\]

Therefore

\[
\boxed{
\|u\|_\infty\le C_n\|u\|_2
\qquad(u\in U_n^{\rm can}).
}
\tag{25}
\]

Combining `(17)` and `(25)`,

\[
|\langle u,A_mv\rangle|
\le
\frac{C_n}{\sqrt m}
\|u\|_2\|v\|_2.
\tag{26}
\]

Hence

\[
\boxed{
\|P_{U_n^{\rm can}}A_m|_{U_n^{\rm can}}\|
\le
C_nm^{-1/2}.
}
\tag{27}
\]

The constant is deliberately source-side. It can be very poor as `n` grows because `lambda_n` may become small. No uniform-in-`n` claim is being made.

---

## 2. Blaschke deflation preserves the source compression

The first-free quotient sections used in `NB-292`--`NB-298` are obtained by dividing the canonical Hardy atoms by the finite packet Blaschke product `B_Z`. Multiplication by `B_Z` is an isometry from the quotient-source section onto the canonical section, and the dilation multiplier

\[
S_mh(s)=m^{1/2-s}h(s)
\tag{28}
\]

commutes with multiplication by `B_Z`.

Consequently the compression of `S_m` to

\[
U=V_{n-1,Z}
\]

is unitarily equivalent to the compression of the canonical dilation `A_m` to `U_n^(can)`. In the isometric coordinates `E_U` from the claim,

\[
T_m=E_U^*S_mE_U
\tag{29}
\]

therefore satisfies

\[
\boxed{
\beta_n(m):=\|T_m\|
\le C_nm^{-1/2}.
}
\tag{30}
\]

In particular,

\[
T_m\to0
\tag{31}
\]

in operator norm for every fixed `n`, uniformly over the choice of finite zero packet.

The principal-angle defect from `NB-297` is

\[
Q_m=I-T_m^*T_m.
\tag{32}
\]

Thus

\[
\boxed{
Q_m\succeq(1-\beta_n(m)^2)I.
}
\tag{33}
\]

For `m>C_n^2`, the right side is positive definite, so `Q_m` is invertible and

\[
\boxed{
\|Q_m^{-1}\|
\le
\frac1{1-C_n^2/m}.
}
\tag{34}
\]

This is worth interpreting carefully. Large `m` does **not** suppress the source escape. It does the opposite:

\[
Q_m\to I.
\tag{35}
\]

All principal angles between the old section and its far-out dilated copy tend to `pi/2`. The source escape becomes asymptotically maximal.

The no-go below therefore cannot be blamed on failure of source separation.

---

## 3. Off-critical sample contraction kills the normalized escape block

The first-free sample covariance is

\[
L_ZS_m=D_Z(m)L_Z,
\tag{36}
\]

with

\[
D_Z(m)
=
\operatorname{diag}
\bigl(m^{1/2-\rho_1},\ldots,m^{1/2-\rho_N}\bigr).
\tag{37}
\]

For the off-critical packet in the claim,

\[
\|D_Z(m)\|
=m^{-\delta_Z}.
\tag{38}
\]

Let

\[
X=L_ZE_U.
\]

Since `E_U` is isometric onto `U`,

\[
XX^*=L_ZP_UL_Z^*=K_{n-1,Z}=K,
\tag{39}
\]

and therefore

\[
\|X\|=\sqrt{\|K\|}.
\tag{40}
\]

The exact source/sample intertwining defect from `NB-297` is

\[
Y_m=D_Z(m)X-XT_m.
\tag{41}
\]

Using `(30)`, `(38)`, and `(40)`,

\[
\begin{aligned}
\|Y_m\|
&\le
\|D_Z(m)\|\,\|X\|
+
\|X\|\,\|T_m\|\\
&\le
\sqrt{\|K\|}
\left(
m^{-\delta_Z}+C_nm^{-1/2}
\right).
\end{aligned}
\tag{42}
\]

For `m>C_n^2`, `Q_m` is invertible, so the `NB-297` factorization becomes

\[
\Xi_{m,n,Z}
=Y_mQ_m^{-1}Y_m^*.
\tag{43}
\]

Consequently

\[
\begin{aligned}
\|\Xi_{m,n,Z}\|
&\le
\|Y_m\|^2\,\|Q_m^{-1}\|\\
&\le
\|K\|
\frac{
\bigl(m^{-\delta_Z}+C_nm^{-1/2}\bigr)^2
}{
1-C_n^2/m
},
\end{aligned}
\tag{44}
\]

which proves `(7)`.

For nontrivial zeta zeros,

\[
0<\Re\rho_j<1.
\tag{45}
\]

Hence a packet strictly to the right of the critical line satisfies

\[
0<\delta_Z<1/2.
\tag{46}
\]

At fixed `n,Z`, the `m^(-delta_Z)` term therefore decays more slowly than the source-compression term `m^(-1/2)`. Equation `(44)` then gives the simpler asymptotic

\[
\|\Xi_{m,n,Z}\|
=O_{n,Z}(m^{-2\delta_Z}),
\tag{47}
\]

proving `(8)`.

This exposes the geometry hidden by source rank. For large `m`, `NB-297` gives full or nearly full source escape rank and `(35)` says the normalized source escape becomes almost orthogonal to the old section. Yet `(47)` says its complete first-free sampling Gram collapses to zero. The escaping directions are becoming asymptotically **sample-null**.

---

## 3a. Relative sampling asymptotics retain the transported Gram

The source-compression error is smaller than **every** transported sample amplitude at a fixed off-critical packet. Put
\[
\delta_j=\Re\rho_j-1/2,\quad
\delta_+=\max_j\delta_j<1/2,\quad
A_m=D_Z(m)KD_Z(m)^*,\quad \beta=\|T_m\|,
\]
\[
\varepsilon_m=\sqrt{\kappa(K)}\,m^{\delta_+}\beta,
\qquad
\ell_m=(1-\varepsilon_m)^2,\qquad
u_m=\frac{(1+\varepsilon_m)^2}{1-\beta^2}.
\]
Whenever `beta<1` and `epsilon_m<1`, there is the finite, target-independent Loewner comparison
\[
\boxed{\ell_m A_m\preceq\Xi_{m,n,Z}\preceq u_m A_m.}
\tag{47a}
\]

To prove it without commuting `K` and `D=D_Z(m)`, define
\[
W=K^{-1/2}X,\qquad F=K^{-1/2}D^{-1}XT_m.
\]
Then `WW^*=I`, `||F||<=epsilon_m`, and exactly
\[
Y_m=DK^{1/2}(W-F).
\]
For every sample vector `z`, the triangle and reverse-triangle inequalities give
\[
(1-\varepsilon_m)\|z\|
\le\|(W-F)^*z\|
\le(1+\varepsilon_m)\|z\|.
\]
Also `I<=Q_m^{-1}<=(1-beta^2)^{-1}I`. Apply these inequalities to `(43)` and take congruence by `DK^{1/2}` to obtain `(47a)`. No pointwise sample phase, source rank heuristic, or inverse of a singular `Q_m` is used.

At fixed `n,Z`, `(30)` gives
\[
\varepsilon_m=O_{n,Z}(m^{\delta_+-1/2})\to0.
\]
Consequently `(47a)` is a **relative**, not just absolute, asymptotic: for every nonzero sample vector `z`, uniformly in that vector,
\[
\frac{z^*\Xi_{m,n,Z}z}{z^*A_mz}
=1+O_{n,Z}(m^{\delta_+-1/2}).
\tag{47b}
\]
In particular `(47)` is sharp at matrix-norm level:
`||Xi||=Theta_{n,Z}(m^{-2 delta_Z})`. Indeed an index attaining `delta_Z` gives `||A_m||>=K_{jj}m^{-2 delta_Z}`, while `(62)` gives the matching upper bound. At sufficiently large `m`, the escaping block has full **sample** rank even as its entire sample Gram tends to zero.

For moving packets the finite estimate `(47a)` remains valid when its displayed hypotheses hold. The sufficient relative-asymptotic gate is `sqrt(kappa(K)) m^{delta_+} beta -> 0`; this is an extra quantitative requirement for this estimate, not a consequence of source overlap merely tending to zero or a necessary condition for relative convergence itself.

---

## 4. The baseline-free target gain vanishes

Assume `L_Z|_U` is onto, so

\[
K=K_{n-1,Z}\succ0.
\tag{48}
\]

The section `U+R_(m,n,Z)` is the orthogonal sum `U\oplus R_(m,n,Z)`, so its sampling Gram is

\[
K+\Xi_{m,n,Z}.
\tag{49}
\]

For datum `y`, define

\[
x:=K^{-1/2}y,
\qquad
M_{\rm esc}:=K^{-1/2}\Xi_{m,n,Z}K^{-1/2}.
\tag{50}
\]

Then

\[
\mathcal C_U(y)=\|x\|^2
\tag{51}
\]

and

\[
\mathcal G_{m,n,Z}(y)
=
x^*M_{\rm esc}(I+M_{\rm esc})^{-1}x.
\tag{52}
\]

Because `M_esc` is positive semidefinite,

\[
0\preceq
M_{\rm esc}(I+M_{\rm esc})^{-1}
\preceq
\min\{I,\|M_{\rm esc}\|I\}.
\tag{53}
\]

Moreover,

\[
\|M_{\rm esc}\|
\le
\|K^{-1}\|\,\|\Xi_{m,n,Z}\|.
\tag{54}
\]

Combining `(44)` and `(54)`,

\[
\boxed{
\|M_{\rm esc}\|
\le
\kappa(K)
\frac{
\bigl(m^{-\delta_Z}+C_nm^{-1/2}\bigr)^2
}{
1-C_n^2/m
}.
}
\tag{55}
\]

Dividing `(52)` by `(51)` proves `(9)`. In particular, for fixed `n,Z`,

\[
\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_U(y)}
=O_{n,Z}(m^{-2\delta_Z})
\tag{56}
\]

uniformly over all nonzero data `y`.

This is stronger than saying that some particular target misses the escaping subspace. **Every** first-free target misses it asymptotically after normalization by its old-section cost.

Now suppose the full finite-section excess from `NB-298`,

\[
\mathfrak A_U(y)
=
\mathcal C_U(y)-\mathcal C_\infty(y),
\tag{57}
\]

is positive. That quantity is independent of `m`, while `mathcal G_(m,n,Z)(y)->0`. The exact occupation identity from `NB-298`,

\[
\mathcal G_{m,n,Z}(y)
=
\eta_{m,n,Z}(y)\,\mathfrak A_U(y),
\tag{58}
\]

therefore gives

\[
\eta_{m,n,Z}(y)\to0.
\tag{59}
\]

So a fixed future tail can remain nonzero while the far-out projected dilation block occupies asymptotically none of its target-relevant Parseval mass.

---

## 4a. The fixed target selects the exact decay exponent

Let `y!=0`, `h=K^{-1}y`, and put
\[
J_m(y)=h^*A_mh=(D_Z(m)^*h)^*K(D_Z(m)^*h)>0,
\qquad
\gamma_m=\|K^{-1/2}A_mK^{-1/2}\|
\le\kappa(K)m^{-2\delta_Z}.
\]
Under the finite hypotheses of `(47a)`, `(52)` yields the two-sided target certificate
\[
\boxed{
\frac{\ell_m}{1+u_m\gamma_m}J_m(y)
\le\mathcal G_{m,n,Z}(y)
\le u_m J_m(y).
}
\tag{59a}
\]
For the proof use
`M_esc/(1+||M_esc||)<=M_esc(I+M_esc)^{-1}<=M_esc`,
`||M_esc||<=u_m gamma_m`, and
`ell_m J_m(y)<=x^*M_esc x<=u_m J_m(y)`.
Thus for fixed `n,Z`, uniformly over all nonzero `y`,
\[
\boxed{
\mathcal G_{m,n,Z}(y)
=J_m(y)\left[1+O_{n,Z}\left(
m^{\delta_+-1/2}+m^{-2\delta_Z}\right)\right].
}
\tag{59b}
\]

For a fixed datum write `rho_j=1/2+delta_j+i t_j`, let
`delta(y)=min_{h_j!=0} delta_j`, and define the nonzero vector
\[
v_j(m)=
\begin{cases}
e^{it_j\log m}h_j,&\delta_j=\delta(y),\\
0,&\delta_j\ne\delta(y).
\end{cases}
\]
There are only finitely many indices, so
\[
m^{2\delta(y)}J_m(y)=v(m)^*Kv(m)+o(1),
\]
and hence
\[
\boxed{m^{2\delta(y)}\mathcal G_{m,n,Z}(y)
=v(m)^*Kv(m)+o(1).}
\tag{59c}
\]
The norm of `v(m)` is a fixed positive number. Its quadratic form lies between `lambda_min(K)||v||^2` and `lambda_max(K)||v||^2`, proving `(13a)`. This also prevents equal-depth phase cancellation from improving the decay exponent. It does **not** force a scalar limiting constant: the cross terms of `v(m)^*Kv(m)` can oscillate with `log m`. If exactly one coordinate `j` survives at the least occupied depth, the limit is `K_{jj}|h_j|^2`.

Raw nonzero entries of `y` do not identify the exponent. In a two-sample algebraic control with `delta_1<delta_2` and `K_{12}!=0`, choosing `y=K e_2` gives `h=e_2`, so the exponent is `2 delta_2` although `y_1!=0`. This is a finite linear-algebra control, not an assertion about the actual Ford datum. Conversely, any nonzero `h` coordinate at depth `delta_Z` makes the upper rate `(56)` sharp for that datum. The actual canonical datum has to be inserted before either conclusion applies to it.

The gain here is still only the projected-dilation contribution inside the ordinary enlarged section. A positive but vanishing two-sided rate neither controls the rest of that increment nor estimates the Nyman target distance.

---

## 5. Why this does not contradict the strong band coercivity of NB-294

At first sight `(56)` appears to point in the opposite direction from `NB-294`, where large off-critical dilation produces

\[
M_{\rm band}
\succeq
\left(
\frac{m^{2\delta_Z}}{\kappa(K)}-1
\right)_+I
\tag{60}
\]

for the multiplicative quotient band relative to the dilated old section.

The baselines are different.

`NB-294` compares the enlarged canonical section with

\[
S_mU,
\]

whose sampling Gram is

\[
A_m
=D_Z(m)KD_Z(m)^*.
\tag{61}
\]

Off criticality forces this baseline itself to collapse:

\[
\|A_m\|
\le
m^{-2\delta_Z}\|K\|.
\tag{62}
\]

A fixed-size ordinary sampling Gram can therefore look enormously coercive when whitened against `A_m`.

`NB-299` instead compares against the undilated old section `U`, whose Gram is the fixed matrix `K`. The component of the dilated copy that actually escapes `U` has Gram `Xi_(m,n,Z)`, and `(47)` shows that this Gram collapses at the same off-critical scale after source overlap has died away.

Thus large `m` simultaneously produces

\[
\text{strong repair relative to a shrinking transported baseline}
\]

and

\[
\text{vanishing new information relative to the ordinary baseline}.
\]

There is no contradiction. The two statements quantify different denominators, and together they make the baseline obstruction of `NB-296` explicit in the actual canonical source.

For fixed `n,Z`, the `NB-294` uniform gate

\[
2\delta_Z\log m-\log\kappa(K)\to+\infty
\tag{63}
\]

is automatic as `m->infinity`. In exactly the same regime, `(56)` says the baseline-free projected gain tends to zero. Thus pushing `m` ever larger is not a way to convert transported-band coercivity into ordinary finite-section coercivity.

---

## 6. A moving-scale upper gate

The fixed-parameter result is a no-go, but `(55)` also gives a quantitative moving-family test.

Let

\[
(Z_X,n_X,m_X)
\]

be any family for which `L_(Z_X)` is onto on `U_X=V_(n_X-1,Z_X)`. Put

\[
K_X:=K_{n_X-1,Z_X},
\qquad
\delta_X:=\min_{\rho\in Z_X}(\Re\rho-1/2),
\qquad
C_X:=C_{n_X}.
\tag{64}
\]

Assume eventually

\[
m_X>C_X^2.
\tag{65}
\]

Then `(55)` gives

\[
\boxed{
\|M_{{\rm esc},X}\|
\le
\kappa(K_X)
\frac{
\bigl(m_X^{-\delta_X}+C_Xm_X^{-1/2}\bigr)^2
}{
1-C_X^2/m_X
}.
}
\tag{66}
\]

Therefore the sufficient large-dilation **sample-null gate** is

\[
\boxed{
\kappa(K_X)
\frac{
\bigl(m_X^{-\delta_X}+C_Xm_X^{-1/2}\bigr)^2
}{
1-C_X^2/m_X
}
\longrightarrow0.
}
\tag{67}
\]

Whenever `(67)` holds,

\[
\sup_{y\ne0}
\frac{
\mathcal C_{U_X}(y)-\mathcal C_{U_X+R_X}(y)
}{
\mathcal C_{U_X}(y)
}
\longrightarrow0.
\tag{68}
\]

This is an upper gate, complementary to the lower gates of `NB-294`--`NB-295` for the transported band.

The constant `C_X` is intentionally not hidden. Its dependence on the smallest eigenvalue of the **source** Gram records the price of controlling how fast the dilated old section loses overlap with the undilated one. In a moving packet/cutoff regime, neither `C_X`, `kappa(K_X)`, nor `delta_X` is presently controlled at the required scale.

If these quantities were uniformly tame and `delta_X` stayed positive, large `m_X` would force the ordinary projected block to vanish. A surviving Ford mechanism must therefore exploit a coupled regime in which at least one of the following prevents `(67)` from becoming small: the packet approaches the critical line, the first-free sampling Gram becomes badly conditioned, the source-section concentration constant grows, or the dilation is not yet in the asymptotic far-shift regime.

This is a significantly narrower destination than merely proving that `R_X` has large rank or that its principal angles from `U_X` are large. Indeed `(35)` already shows that large dilation makes those principal angles as favorable as possible while the sample-visible block still vanishes.

---

## 7. Joint fixed-packet vanishing and the remaining moving-packet window

`NB-298` proves, for every fixed packet `Z`,

\[
\sup_{m\ge2}\|\Xi_{m,n,Z}\|
\le
\|E_{n-1,Z}\|
\longrightarrow0
\qquad(n\to\infty).
\tag{69}
\]

The present finding proves, for every fixed `n,Z`,

\[
\|\Xi_{m,n,Z}\|
\longrightarrow0
\qquad(m\to\infty).
\tag{70}
\]

The supremum over `m` in `(69)` is essential: together these limits **do** imply joint vanishing at fixed packet. Fix `Z` and an index `n_0` for which the sampler is onto. Then
\[
\boxed{
\lim_{R\to\infty}
\sup_{\substack{n\ge n_0,\ m\ge2\\\max\{n,m\}\ge R}}
\|\Xi_{m,n,Z}\|=0.
}
\tag{70a}
\]
Given `epsilon>0`, `(69)` first supplies `N` so that all `n>=N` and every `m>=2` have norm below `epsilon`. There are only finitely many remaining indices `n_0<=n<N`; `(70)` supplies one common threshold `M` for these. Outside the rectangle `n<N, m<M`, the norm is therefore below `epsilon`. This proves `(70a)` without interchanging nonuniform limits.

The target consequence is also uniform over data. Nestedness gives
`K_{n-1,Z}>=K_{n_0-1,Z}>0`, so `(53)`--`(54)` imply
\[
0\le\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_{V_{n-1,Z}}(y)}
\le\|K_{n_0-1,Z}^{-1}\|\,\|\Xi_{m,n,Z}\|.
\]
Thus
\[
\boxed{
\lim_{R\to\infty}
\sup_{\substack{n\ge n_0,\ m\ge2\\\max\{n,m\}\ge R}}
\sup_{y\ne0}
\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_{V_{n-1,Z}}(y)}=0.
}
\tag{70b}
\]
This does not give a joint bound on `G/A_U` when the full excess `A_U` itself vanishes: that is a different denominator.

Accordingly, a surviving nonvanishing absolute sample block or relative-to-old-cost target gain must vary the **zero packet**, not just the cutoff and dilation. The uniform thresholds in `(70a)`--`(70b)` depend on the fixed packet. No uniformity over `Z` is asserted. A Ford-scale theorem must control that moving-packet dependence, avoid the quantitative collapse gate `(67)`, and separately establish the needed target occupation and full excess. Dilation alone supplies no free amplification parameter.

---

## 8. Prior-art boundary and adversarial audit

The literature audit rechecked the classical Nyman--Beurling/Báez-Duarte dilation framework and Bagchi's Hilbert-space/semigroup exposition. Those sources establish the discrete dilation setting and its relation to the criterion, but the present proof does not require a new external theorem. The key analytic fact is elementary: an isometric dilation whose range is supported in `(0,1/m]` converges weakly to zero, and on a fixed finite-dimensional source section its compression therefore converges to zero in operator norm. The quantitative `m^(-1/2)` estimate is proved directly from the bounded canonical atoms and the finite source Gram.

No novelty is claimed for weak convergence of shifts, finite-dimensional compactness, or the matrix inequality behind `(44)`. The research-specific point is their combination with the exact `NB-297` factorization `Xi=YQ^+Y^*` and the off-critical first-free covariance `L_ZS_m=D_Z(m)L_Z`. The audit did not reveal a Nyman--Beurling source stating this projected-escape sample-null consequence. The already recorded Bagchi and Báez-Duarte anchors remain sufficient, so `SOURCES.md` needs no new durable dependency.

The relative comparison `(47a)` is an elementary singular-value perturbation bound for a coisometry; see G. W. Stewart, *Perturbation Theory for the Singular Value Decomposition*, UMIACS-TR-90-124 (1990), Section 2, [author report](https://users.math.msu.edu/users/iwenmark/Teaching/MTH995/Papers/SVD_Stewart.pdf), for the classical perturbation boundary. The proof above uses only triangle inequalities and proves the needed version directly. Bagchi's [semigroup construction](https://arxiv.org/abs/math/0607733), Theorem 7, supplies the established dilation setting; Werner Ehm's [Gram-kernel study](https://arxiv.org/abs/2405.06349) concerns explicit kernels and quadratic-form decompositions, rather than this finite first-free projected-escape asymptotic. No priority claim is made for the matrix perturbation, inverse-cost identity, or finite-rectangle argument. The added line-specific content is the relative transported-Gram comparison, the inverse-Gram-selected decay exponent for the actual interpolation datum, and the fixed-packet quantifier consequence. All are derived from existing canonical identities, with no new specialized external estimate.

The adversarial checks are as follows.

First, the proof does **not** infer small `Xi` from large source principal angles. It proves the opposite source behavior `Q_m->I` and obtains smallness only from the intertwining defect `Y_m=D_Z(m)X-XT_m`, where both terms vanish off criticality.

Second, Blaschke deflation does not invalidate the source-compression estimate. Multiplication by the finite packet inner factor is isometric and commutes with the dilation multiplier, so the compression norm is exactly the canonical one.

Third, no inverse of `Q_m` is used until `beta_n(m)<1`. For sufficiently large `m`, `(30)` guarantees this. Before that threshold the Moore--Penrose formula from `NB-297` remains valid, but no bound of the form `(44)` is asserted.

Fourth, the result genuinely requires an off-critical packet. If `Re rho=1/2`, then `|m^(1/2-rho)|=1`, so `D_Z(m)` does not decay. In that case `T_m->0` would make `Y_m` approach `D_Z(m)X`, not zero; the sample-null conclusion fails exactly where it should.

Fifth, `(67)` is only a sufficient upper gate in a moving family. Failure of `(67)` does not imply nonvanishing occupation. Likewise, the fixed-parameter estimates do not supply a uniform Ford-scale rate because `delta_X` may tend to zero and both source and sample conditioning may deteriorate.

The relative estimate also uses `delta_+<1/2`, not only `delta_Z>0`: it is what makes the source-compression error small after undoing **all** diagonal sample contractions. Neither `K` nor its square root is commuted through `D_Z(m)`. The finite comparison was additionally checked in exact rational arithmetic for `X=((1,1,0),(0,1,1))`, `D=diag(1/3,-1/5)`, and the nonnormal `T` with entries `T_12=1/100`, `T_23=1/200`, `T_31=1/300` and all others zero. Here `K=XX^*`, `beta=1/100`, and `epsilon<=sqrt(3)/20<1/10`; both Gram and target-gain Loewner bounds pass with the conservative `epsilon=1/10` and `gamma<=1/3`. This checks a noncommuting signed control, not realizability by a zeta packet or the general proof. No target coefficient support is assumed from that control.

Finally, the target gain in `(9)` concerns `U+R_(m,n,Z)`, the canonical projected-dilation subspace inside the ordinary enlarged section. It is a lower-dimensional certificate for ordinary enrichment, not the full gain from `U` to `V_(mn-1,Z)`. Showing that this certificate vanishes does not show that every other part of the ordinary increment is useless.

---

## Consequence for the research line

`NB-294`--`NB-295` showed that off-critical dilation creates strong transported-band capacity. `NB-296` warned that this may be only baseline repair. `NB-297` extracted the canonical baseline-free projected copy, and `NB-298` identified it as a Parseval subblock of the existing finite-section tail.

`NB-299` closes the simplest remaining amplification idea: **for a fixed source section and fixed off-critical packet, sending the dilation to infinity makes that baseline-free projected block sample-null even though its source-space escape becomes asymptotically maximal**.

The far-dilation loss is quantitatively sharp: the inverse-Gram-transformed datum determines its decay exponent, with the two-sided certificate `(59a)` and asymptotic `(59c)`. Deep ordinary sections kill the future tail uniformly in `m`; together with far-dilation decay this excludes every joint escape in `(n,m)` at a **fixed** packet. A surviving Ford-scale argument must vary and control the packet itself, couple its horizontal displacements to source and sample conditioning, and still prove the needed finite-section excess and occupation. The fixed-packet classification supplies no Nyman-distance rate or RH implication.
