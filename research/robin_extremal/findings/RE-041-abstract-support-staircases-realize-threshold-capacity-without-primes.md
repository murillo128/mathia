# RE-041 — abstract support staircases realize the threshold-capacity budget without primes

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SYNTHETIC-CONTROL + SUPPORT-GEOMETRY-UNIVERSALITY + EVENT-QUANTIZATION-BOUNDARY + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-040` proves two genuinely stronger facts about the compact false-RH threshold fan: the adaptive maximizers are simultaneously regular on the same late counterexample blocks, and the translated standard/reciprocal prime-race law holds uniformly across the fan. It also derives the threshold-capacity inequality

\[
|I_C|
\le
\frac{Y_C\bigl(\varepsilon_-(C)-\varepsilon_+(C)\bigr)}
{1-e^{-h(C)}}.
\tag{1}
\]

The first two facts retain arithmetic content. The **capacity inequality by itself does not**. Every prescribed compact threshold fan can be embedded, in the same small-height and logarithmic-spacing regime used by `RE-039`--`RE-040`, into a strictly concave abstract support chain whose adjacent slopes satisfy the full `RE-040` chamber inequalities. The associated positive atomic event staircase can moreover be chosen so that the exact selector equation

\[
Y_i=\Phi_{\rm syn}(Z_i(b))
\tag{2}
\]

holds throughout every threshold cell.

Thus neither a support-capacity budget nor the bare existence of an exact event staircase distinguishes the physical colossally abundant system. The surviving arithmetic datum is narrower: for the real CA staircase each atom is a **prime-power layer**, so its jump mass and supporting slope are tied to the same pair `(p,j)`,

\[
\Delta Y=\log p,
\qquad
m_{p,j}
=
\frac1{\log p}
\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\tag{3}
\]

with tied transitions formed only by collisions among these special values. In addition, the same primes must generate the standard/reciprocal race coordinates in the uniform relation of `RE-040`. A closing argument must use that quantization/common-source coupling, not abstract support capacity alone.

## 1. A guarded synthetic fan with the exact Robin amplitude

Fix

\[
0<b_0<b_1<\frac12,
\qquad
J=[b_0,b_1],
\qquad
c_0>0.
\tag{4}
\]

Choose an integer `m>=2` and a strictly increasing transition mesh

\[
b_0=\beta_1<\beta_2<\cdots<\beta_m=b_1.
\tag{5}
\]

Choose increasing intrinsic coordinates

\[
Y_0<Y_1<\cdots<Y_m
\tag{6}
\]

and define positive synthetic excesses by

\[
R_0:=c_0Y_0^{-b_0},
\qquad
R_i:=R_{i-1}
\left(\frac{Y_{i-1}}{Y_i}\right)^{\beta_i}
\quad(1\le i\le m).
\tag{7}
\]

As in `RE-039`, put

\[
A_b(i):=Y_i^bR_i.
\tag{8}
\]

The adjacent logarithmic score difference is exact:

\[
\boxed{
\log A_b(i)-\log A_b(i-1)
=
(b-\beta_i)\log\frac{Y_i}{Y_{i-1}}.
}
\tag{9}
\]

Consequently, for

\[
\beta_i\le b<\beta_{i+1},
\qquad 1\le i\le m-1,
\tag{10}
\]

the rightmost maximizer of the whole finite family is exactly state `i`. States `0` and `m` are guards tied only at the two endpoints of `J`; endpoint choices have zero effect on the threshold-cell budget. At `b=b_0`, equation (7) gives

\[
A_{b_0}(0)=A_{b_0}(1)=c_0,
\tag{11}
\]

so the construction retains the quantitative left-endpoint normalization used in `RE-038`--`RE-040`.

For the asymptotic control below take

\[
Y_i=T+i\log T,
\tag{12}
\]

allowing `m=m(T)` subject initially only to `m\log T=o(T)`. Then uniformly in `i`,

\[
R_i=(c_0+o(1))T^{-b_0},
\qquad
h_i:=\log(1+R_i),
\qquad
a_i:=1-e^{-h_i}=\frac{R_i}{1+R_i},
\tag{13}
\]

and hence

\[
h_i\log Y_i\longrightarrow0.
\tag{14}
\]

This is exactly the asymptotically small positive-height regime in which the adaptive barriers of `RE-034` and `RE-040` are strictly concave.

## 2. The synthetic heights determine their own compatible support chain

Discarding the irrelevant additive Euler constant, define the synthetic abundance ordinate

\[
F_i:=\log\log Y_i+h_i.
\tag{15}
\]

For each transition set

\[
s_i:=
\frac{F_i-F_{i-1}}{Y_i-Y_{i-1}}
\qquad(1\le i\le m).
\tag{16}
\]

At the switch `beta_i`, equation (7) gives the common amplitude

\[
c_i:=R_{i-1}Y_{i-1}^{\beta_i}
=R_iY_i^{\beta_i}.
\tag{17}
\]

Therefore both endpoints `(Y_{i-1},F_{i-1})` and `(Y_i,F_i)` lie on the same adaptive barrier

\[
H_i(x)
:=
\log\log x+\log(1+c_ix^{-\beta_i}).
\tag{18}
\]

Its derivative at state `i` is

\[
H_i'(Y_i)
=
g(Y_i)-\frac{\beta_i a_i}{Y_i},
\qquad
g(x):=\frac1{x\log x}.
\tag{19}
\]

Write more generally

\[
t_i(b):=
g(Y_i)-\frac{ba_i}{Y_i}.
\tag{20}
\]

The positive curvature of the second term in (18) is

\[
\frac{\beta_i c_i\bigl((\beta_i+1)x^{\beta_i}+c_i\bigr)}
{x^2(x^{\beta_i}+c_i)^2}.
\tag{21}
\]

On every interval `[Y_{i-1},Y_i]`, equations (13)--(14) give uniformly

\[
\frac{
\bigl(\log(1+c_ix^{-\beta_i})\bigr)''
}{
|(\log\log x)''|
}
=
O_J(R_i\log T)
=o(1).
\tag{22}
\]

Hence every `H_i` is strictly concave for sufficiently large `T`. Applying the backward and forward secant inequalities at the common state `i` gives, for `1<=i<=m-1`,

\[
\boxed{
s_i
>
t_i(\beta_i)
>
t_i(\beta_{i+1})
>
s_{i+1}.
}
\tag{23}
\]

The middle inequality is exact because `a_i>0` and `beta_i<beta_{i+1}`.

Equation (23) has two consequences. First,

\[
s_1>s_2>\cdots>s_m,
\tag{24}
\]

so the points `(Y_i,F_i)` are the vertices of a strictly concave support polygon: state `i` uniquely maximizes

\[
F_j-\varepsilon Y_j
\tag{25}
\]

whenever

\[
s_{i+1}<\varepsilon<s_i.
\tag{26}
\]

Thus the synthetic Robin heights do not need independently assigned supporting intervals; the required support chain is already forced by their own secants.

Second, for every threshold in the amplitude cell,

\[
\beta_i\le b\le\beta_{i+1},
\tag{27}
\]

monotonicity of `t_i(b)` and (23) give

\[
\boxed{
s_{i+1}
<
g(Y_i)-\frac{ba_i}{Y_i}
<
s_i.
}
\tag{28}
\]

This is exactly the `RE-040` regularity inequality, with the abstract adjacent supporting slopes

\[
\varepsilon_-(i)=s_i,
\qquad
\varepsilon_+(i)=s_{i+1}.
\tag{29}
\]

No primes have entered the construction.

## 3. The RE-040 capacity budget is automatic, with an exact curvature-slack decomposition

Solving (28) for `b` defines the synthetic support-capacity interval

\[
K_i:=
\left(
\frac{Y_i(g(Y_i)-s_i)}{a_i},
\frac{Y_i(g(Y_i)-s_{i+1})}{a_i}
\right).
\tag{30}
\]

Equation (23) gives the strict containment

\[
\boxed{
[\beta_i,\beta_{i+1}]
\subset K_i.
}
\tag{31}
\]

In particular,

\[
\boxed{
\beta_{i+1}-\beta_i
<
\frac{Y_i(s_i-s_{i+1})}{a_i},
}
\tag{32}
\]

which is the exact analog of the single-state capacity estimate (1). Summing the cells yields

\[
\boxed{
b_1-b_0
<
\sum_{i=1}^{m-1}
\frac{Y_i(s_i-s_{i+1})}{a_i}.
}
\tag{33}
\]

More importantly, the amount by which capacity exceeds the threshold cell has an exact elementary decomposition. Since

\[
t_i(\beta_i)-t_i(\beta_{i+1})
=
(\beta_{i+1}-\beta_i)\frac{a_i}{Y_i},
\tag{34}
\]

we have

\[
\boxed{
\frac{Y_i(s_i-s_{i+1})}{a_i}
=
(\beta_{i+1}-\beta_i)
+\kappa_i^-+\kappa_i^+,
}
\tag{35}
\]

where

\[
\kappa_i^-:=
\frac{Y_i\bigl(s_i-t_i(\beta_i)\bigr)}{a_i}>0,
\qquad
\kappa_i^+:=
\frac{Y_i\bigl(t_i(\beta_{i+1})-s_{i+1}\bigr)}{a_i}>0.
\tag{36}
\]

Thus the capacity budget is literally the amplitude-cell partition plus the two secant-versus-tangent curvature slacks. It contains no additional source datum at the abstract support level.

The control can even make the total budget asymptotically tight while the fan becomes arbitrarily dense. Under (12),

\[
\sup |H_i''(x)|
=
O\!\left(\frac1{T^2\log T}\right),
\tag{37}
\]

so the tangent-secant theorem and `Y_i-Y_{i-1}=\log T` give

\[
\kappa_i^\pm
=
O_J(T^{b_0-1})
\tag{38}
\]

uniformly. Choose, for example,

\[
m(T)=\left\lfloor T^{(1-b_0)/2}\right\rfloor
\tag{39}
\]

and an evenly spaced `beta` mesh. Then `m(T)->infinity`, the largest threshold cell tends to zero, the whole synthetic block still has relative stretch `o(T)`, and

\[
\boxed{
\sum_{i=1}^{m-1}
\frac{Y_i(s_i-s_{i+1})}{a_i}
=
b_1-b_0+o(1).
}
\tag{40}
\]

Therefore neither a divergent number of cells nor near-saturation of the total support-capacity budget can distinguish the physical CA fan from a source-free control.

## 4. Even the exact selector staircase can be reproduced abstractly

Because the support slopes in (24) are positive and strictly decreasing for large `T`, let

\[
\eta_i:=g^{-1}(s_i).
\tag{41}
\]

Since `g` is strictly decreasing,

\[
\eta_1<\eta_2<\cdots<\eta_m.
\tag{42}
\]

Define on this local block the positive atomic staircase

\[
\Phi_{\rm syn}(Z)
:=
Y_0+
\sum_{\eta_j\le Z}(Y_j-Y_{j-1}).
\tag{43}
\]

At every atom,

\[
F_j-F_{j-1}
=
s_j(Y_j-Y_{j-1})
=
g(\eta_j)(Y_j-Y_{j-1}),
\tag{44}
\]

so this has exactly the generic event bookkeeping of the CA variational system: event mass is the increment in intrinsic log-size, and abundance gain is supporting slope times that mass.

For a selected state `i` and any `b` in its threshold cell define the same adaptive tangent parameter as in `RE-039`--`RE-040`,

\[
g(Z_i(b))
=
t_i(b)
=
g(Y_i)-\frac{ba_i}{Y_i}.
\tag{45}
\]

Equation (28) and monotonicity of `g^{-1}` imply

\[
\eta_i<Z_i(b)<\eta_{i+1}.
\tag{46}
\]

Hence, exactly,

\[
\boxed{
\Phi_{\rm syn}(Z_i(b))=Y_i.
}
\tag{47}
\]

So the matched control now reproduces not only the affine threshold fan and tangent displacement of `RE-039`, but also the abstract version of the selector equation that `RE-040` writes as `Y=Phi(Z)`. What it does **not** reproduce is the special prime-generated measure `Phi`.

This distinction is load-bearing. An argument using only positivity of the event masses, monotone event locations, support concavity, the exact event gain relation (44), and the equality (47) is still vulnerable to this control.

## 5. Where the actual arithmetic survives

For the physical CA process, `RE-001` identifies every individual event with a prime-power layer:

\[
\Delta Y_{p,j}=\log p,
\qquad
\lambda_{p,j}
=
\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\qquad
m_{p,j}=\frac{\lambda_{p,j}}{\log p},
\tag{48}
\]

and its event location satisfies

\[
g(\eta_{p,j})=m_{p,j}.
\tag{49}
\]

The synthetic staircase has no analog of this **joint quantization of mass and slope by one prime-power label**. Its atom masses `Y_j-Y_{j-1}` and slopes `s_j` are free positive geometric data subject only to concavity. It also does not generate

\[
\vartheta(Z)-Z
\tag{50}
\]

and the logarithmic Mertens-product error from the same primes, so it does not reproduce the uniform translated nonlinear race identity of `RE-040`.

Accordingly, this finding does not refute simultaneous regularity, the real CA selector, or the uniform prime-race conclusion of `RE-040`. It removes only an overinterpretation of the capacity side: **capacity is generic support geometry until the allowed support atoms are restricted to the prime-power event lattice.**

The most direct remaining targets are therefore source-specific. One may try to show that the prime-power pairs `(log p,m_{p,j})` cannot supply enough consecutive chamber capacity for a whole quantitative false-RH fan, or combine their quantization with the uniform race calibration so that the same prime source is overconstrained. Merely proving an upper or lower bound for an abstract sum of chamber widths cannot close the route unless that bound uses the special event lattice.

## 6. Stress tests, prior-art boundary, and consequence

The construction is deliberately not an integer model. The synthetic states are not claimed to be colossally abundant numbers, and the atoms in (43) are not claimed to be primes or prime powers. That is precisely the matched-control boundary: it tests which parts of `RE-040` follow from support geometry before prime arithmetic is imposed.

The guards at `beta_1=b_0` and `beta_m=b_1` avoid endpoint artifacts; only states `1,...,m-1` carry positive-length cells. Strict inequalities in (23) show that breakpoint ties in the amplitude envelope do not create tied support parameters: each tied amplitude state has its own interior adaptive supporting slope, just as in `RE-040`.

The curvature estimate uses no prime-number theorem and no zeta input. It is the same elementary strict-concavity mechanism already present in `RE-001`, `RE-034`, and `RE-040`. Convex/support-envelope organization of divisor-sum extremizers is classical in spirit, with Alaoglu--Erdos supplying the actual CA prime-exponent thresholds and Musin providing a nearby convex-envelope prior-art boundary. Mantovanelli's prime-layer event sweep is the closest recent source-side representation. A targeted current search found no source turning the `RE-038` scale-invariant threshold fan into this particular matched abstract-event control; no new external theorem is load-bearing, so `SOURCES.md` requires no change.

The novelty claim is therefore narrow. It is not a new theorem about convex polygons. The line-specific result is the negative control: **the full threshold-capacity inequality and even an exact abstract selector staircase can be manufactured from the same synthetic heights that already realize arbitrary threshold fans.** This identifies the first genuinely arithmetic interface more sharply than `RE-039`: not `Y=Phi(Z)` in isolation, but `Phi` being the prime-power event measure and simultaneously feeding the standard/reciprocal prime races.

For the live false-RH strategy, the practical consequence is that a future contradiction must spend prime-specific information. The promising object is no longer total chamber capacity as an abstract resource, but the compatibility of a dense compact threshold fan with the quantized event pairs (48)--(49) **and** the vanishing-width common-source race calibration of `RE-040`.
