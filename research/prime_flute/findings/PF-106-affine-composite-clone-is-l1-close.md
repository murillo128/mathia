# PF-106 — an affine all-composite exact clone is `ell^1`-close at the sampled endpoints

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. This strengthens PF-105's exact all-composite control. It does **not** prove unitary equivalence, compact resolvent equivalence, trace-class relative heat kernels, or equality of any global spectral determinant. Its role is to narrow the surviving exact-geometry branch: even the full sampled endpoint sequence admits an all-composite exact clone whose canonically normalized vertex displacement is absolutely summable and whose full marked tail cross-ratio distortion is uniformly `O(P^-3)`.

## Claim

Let

\[
V(x)=\pi\cot\frac{\pi}{x},\qquad x>2,
\]

and let the exact prime-flute tail have endpoints

\[
x_n^E=V(p_n),\qquad p_n\ge3.
\]

For every odd prime `p_n`, define

\[
q_n=p_n+1.
\]

Then every `q_n` is an even composite integer. Feed the `q_n` through the **same exact endpoint law** and form the corresponding orthogonal-circle flute with vertices `V(q_n)`. Hyperbolic translation

\[
z\mapsto z-1
\]

is a Möbius isometry, so this all-composite surface is isometric to the flute with normalized endpoints

\[
\boxed{
x_n^+=W(p_n),\qquad W(x):=V(x+1)-1.}
\tag{1}
\]

The normalization (1) keeps the common projective gap geometry fixed: before applying `V`, the composite labels `p_n+1` differ from the primes by one global translation, so every projective gap and every projective tangent is exactly unchanged.

The exact cotangent deformation is much smaller than in the dilation clone of PF-105. Define the sampled endpoint displacement

\[
d(x):=W(x)-V(x).
\]

Then

\[
\boxed{
d(x)>0,\qquad d'(x)<0,\qquad
 d(x)=\frac{\pi^2}{3x^2}+O(x^{-3}),}
\tag{2}
\]

and therefore

\[
\boxed{
\sum_{p_n\ge3}|x_n^+-x_n^E|
=\sum_{p_n\ge3}d(p_n)<\infty.}
\tag{3}
\]

Moreover, for every `P>=3` and every real interval `P<=a<b`, with no restriction on `b-a`, the exact secant ratio

\[
R_+(a,b)
:=
\frac{V(b)-V(a)}{W(b)-W(a)}
\]

satisfies

\[
\boxed{
1\le R_+(a,b)\le 1+\frac{C}{P^3}}
\tag{4}
\]

for an absolute constant `C`. Consequently, for **any** four prime labels

\[
P\le a<b<c<d,
\]

if `chi_E` and `chi_+` are the exact PF-004 cross-ratios of the matched prime and all-composite endpoints, then

\[
\boxed{
\left|\log\frac{\chi_E}{\chi_+}\right|
=O(P^{-3})}
\tag{5}
\]

uniformly over arbitrary gap sizes and arbitrary block span. The corresponding canonical separating lengths

\[
L=4\operatorname{arsinh}\sqrt\chi
\]

therefore obey

\[
\boxed{|L_E-L_+|=O(P^{-3})}
\tag{6}
\]

with the same all-span uniformity.

The adjacent fan-shear defect is also absolutely summable, now with the stronger one-interval estimate

\[
\boxed{
r_n:=\log\frac{V(p_{n+1})-V(p_n)}{W(p_{n+1})-W(p_n)}
=O(p_n^{-3}),
\qquad
\sum_n r_n<\infty.}
\tag{7}
\]

Thus PF-105's conclusion is not an artifact of the dilation control `Kp_n`, whose normalized vertices differ from `V(p_n)` at order `p_n^-1`. There is an exact all-composite control with **summable vertex displacement** and a uniformly smaller `O(P^-3)` marked tail distortion.

## 1. Exact `ell^1` sampled-vertex displacement

From PF-105,

\[
V'(x)
=
\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2>1
\]

and `V'` is strictly decreasing to `1` for `x>2`. Hence

\[
\begin{aligned}
d(x)
&=V(x+1)-1-V(x)\\
&=\int_x^{x+1}\bigl(V'(t)-1\bigr)\,dt.
\end{aligned}
\tag{8}
\]

Therefore `d(x)>0`. Also

\[
d'(x)=V'(x+1)-V'(x)<0,
\tag{9}
\]

so the displacement decreases monotonically to zero. Since

\[
0<d(x)\le V'(x)-1
\]

and

\[
V'(x)-1=\frac{\pi^2}{3x^2}+O(x^{-4}),
\]

we get `d(x)=O(x^-2)` and hence

\[
\sum_n d(p_n)
\le C\sum_{m\ge3}m^{-2}<\infty.
\]

Expanding `V(x+1)-1-V(x)` one order further gives the stated leading term in (2):

\[
d(x)=\frac{\pi^2}{3x^2}+O(x^{-3}).
\]

No prime-distribution theorem is used.

## 2. Uniform all-span secant control improves to `O(P^-3)`

For `P<=a<b`,

\[
V(b)-V(a)=\int_a^b V'(t)\,dt,
\]

while

\[
W(b)-W(a)=\int_a^b V'(t+1)\,dt.
\]

Because `V'` is decreasing,

\[
V'(t)\ge V'(t+1)>1,
\]

so `R_+(a,b)>=1`.

Differentiate `V'`. With `y=pi/x`, one convenient exact form is

\[
\boxed{
V''(x)
=-\frac{2}{x}V'(x)\bigl(1-y\cot y\bigr).}
\tag{10}
\]

On `x>=3`, `0<y<=pi/3`; there `V'` is bounded and

\[
0<1-y\cot y\le C_0y^2.
\]

Hence

\[
\boxed{|V''(x)|\le C_1x^{-3}.}
\tag{11}
\]

The mean-value theorem now gives, uniformly for `t>=P`,

\[
0\le V'(t)-V'(t+1)\le C_1P^{-3}.
\]

Therefore

\[
0\le
[V(b)-V(a)]-[W(b)-W(a)]
\le C_1P^{-3}(b-a).
\]

Since `W(b)-W(a)>=b-a`,

\[
0\le R_+(a,b)-1\le C_1P^{-3},
\]

which proves (4). In particular

\[
0\le\log R_+(a,b)\le C_1P^{-3}.
\tag{12}
\]

The crucial point is again the quantifier: the estimate is independent of the length of `[a,b]`.

## 3. Cross-ratios and canonical separators inherit the stronger bound

For ordered `a<b<c<d`, PF-004 uses

\[
\chi(a,b,c,d)
=
\frac{(c-b)(d-a)}{(b-a)(d-c)}.
\]

Applying the exact prime and normalized composite maps gives

\[
\frac{\chi_E}{\chi_+}
=
\frac{R_+(b,c)R_+(a,d)}{R_+(a,b)R_+(c,d)}.
\tag{13}
\]

Every logarithm on the right lies in `[0,CP^-3]`. Thus

\[
\left|\log\frac{\chi_E}{\chi_+}\right|
\le 2CP^{-3},
\]

which is (5).

As in PF-105,

\[
\frac{d}{d\log\chi}
\left(4\operatorname{arsinh}\sqrt\chi\right)
=2\sqrt{\frac{\chi}{1+\chi}}
\le2.
\]

Therefore (5) implies (6), even if `chi` tends to zero or infinity. Pinching blocks, long separators, and hierarchically spread blocks do not evade the comparison.

## 4. The canonical boundary-mesh matching is asymptotically affine with finite total variation

There is a useful stronger formulation at the discrete boundary level. Let `h` be the increasing piecewise-affine map that sends

\[
V(p_n)\mapsto W(p_n)
\]

and is affine on every interval between consecutive sampled endpoints.

At the vertices,

\[
h(V(p_n))-V(p_n)=d(p_n)=O(p_n^{-2}),
\]

so `h(x)-x->0` along the marked tail. On the `n`-th interval its slope is

\[
h'
=
\frac{W(p_{n+1})-W(p_n)}{V(p_{n+1})-V(p_n)}
=R_+(p_n,p_{n+1})^{-1}
=1+O(p_n^{-3}).
\tag{14}
\]

Because `d(p_n)` decreases to zero,

\[
\begin{aligned}
\int_{V(p_m)}^\infty |h'(x)-1|\,dx
&=\sum_{n\ge m}
\left|[W(p_{n+1})-W(p_n)]-[V(p_{n+1})-V(p_n)]\right|\\
&=\sum_{n\ge m}\bigl(d(p_n)-d(p_{n+1})\bigr)\\
&=d(p_m)<\infty.
\end{aligned}
\tag{15}
\]

Thus the most obvious marked boundary matching is not merely asymptotically close: its derivative defect has finite `L^1` mass on every tail and the total tail mass tends to zero.

Equation (15) is **not** promoted here to a quasiconformal conjugacy theorem for the Fuchsian groups. Mapping the sampled endpoints and controlling a piecewise-affine boundary interpolation is weaker than constructing a group-equivariant map of the two quotient surfaces with the metric/derivative estimates required by relative Laplacian scattering theory. That analytic bridge remains open.

## 5. Consequence for the surviving spectral branch

PF-099 killed primality specificity of the entire projective tangent process. PF-101/PF-104 ruled out finite endpoint jets and off-prime interpolation data as privileged RH mechanisms. PF-105 then showed that even the full exact sampled cotangent geometry has an all-composite clone with uniformly vanishing marked tail cross-ratio distortion and `ell^1` fan-shear defect.

PF-106 strengthens the last control in two ways:

\[
\boxed{
\text{sampled endpoint displacement itself is }\ell^1,
}
\]

and

\[
\boxed{
\sup_{a<b<c<d,\ a\ge P}
|\log\chi_E-\log\chi_+|=O(P^{-3}).
}
\]

Accordingly, a surviving exact prime-flute spectral mechanism cannot obtain its claimed arithmetic selectivity from any invariant that is continuous under this asymptotically affine, summable marked deformation. It would have to be sensitive to the **global organization of an `ell^1`-small exact defect** in a way that is not already a generic relative perturbation invariant.

This makes the remaining relative-operator question sharper rather than solving it:

\[
\boxed{
\text{Does the canonical prime/composite matching descend to a sufficiently controlled}\
\text{surface comparison to make the relative resolvent, heat kernel, or scattering}\
\text{difference compact / Schatten / trace class?}
}
\]

A positive answer would move the surviving information into a relative spectral-shift/scattering-phase type object; it would **not** by itself provide RH zeros, and PF-016 would still forbid zeros of a genuine physical relative scattering determinant on the unitary line. A negative answer would identify a genuinely nonlocal amplification mechanism despite the `ell^1` endpoint closeness.

## 6. Interior/exterior duality

The composite normalization uses the hyperbolic Möbius translation `z -> z-1`. It transports the complete orthogonal-circle configuration and its interior/exterior realization exactly. Cross-ratios and PF-004 separator lengths are Möbius invariant, so the estimates above are independent of which ambient side is drawn.

The piecewise-affine map `h` is only a comparison device after this canonical Möbius normalization; it is not an extra geometric structure added to one side.

## 7. Prior art and novelty audit

No novelty is claimed for the ingredients:

- every odd prime plus one is even and composite;
- translations are Möbius isometries of the upper half-plane;
- the derivative identities and summability estimates are elementary calculus;
- asymptotically trivial boundary distortions belong to standard asymptotic Teichmüller language.

The existing asymptotic infinite-type Teichmüller results already noted in PF-105 do not automatically turn (15) into an operator theorem for this flute: the most convenient Fenchel--Nielsen criteria in that literature are stated under upper-bounded pants hypotheses, whereas the distinguished prime-flute cuffs tend to infinity. No such theorem is invoked here.

Directed searches for prime/cotangent tight flutes, affine all-composite endpoint clones, and spectral consequences of this exact shift normalization did not locate this specialization. The durable project-specific content is the exact control experiment:

\[
\boxed{
\{p_n\}
\longrightarrow
\{p_n+1\}\ \text{(all composite)}
\longrightarrow
\text{same projective gap process}
\longrightarrow
\ell^1\text{-close exact sampled endpoints}
\longrightarrow
O(P^{-3})\text{ full-tail cross-ratio distortion}.
}
\]

This is a stronger adversarial background than the dilation clone for testing any future global relative spectral invariant, but it does not itself establish spectral equivalence.

## 8. Audit / falsification core

The finite checks are:

1. verify that `p+1` is composite for every odd prime `p`;
2. verify that `z -> z-1` is the required Möbius normalization of the exact composite endpoints;
3. derive (8)--(9) from monotonicity of `V'` and obtain `d(x)=O(x^-2)`;
4. verify (10) and the tail bound `|V''(x)|=O(x^-3)`;
5. integrate the one-step derivative defect to obtain the all-span bound (4);
6. substitute the four secant ratios into the exact PF-004 formula to obtain (5)--(6);
7. apply (4) to consecutive prime intervals for (7), and telescope the monotone vertex displacement to obtain the finite-variation identity (15).

A counterexample to the **geometric** statement would have to violate one of these explicit estimates. A counterexample to the programmatic no-go would have to exhibit an intrinsic prime-flute spectral invariant that is not continuous under this comparison and explain why that discontinuity is geometrically forced rather than an arbitrary encoding of the prime labels.