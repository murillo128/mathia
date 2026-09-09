# AF-219 — full Euler log is strictly sign-regular of order three

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `SOURCE-COMPLEXITY-GATE`, `EXACT-FIDELITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-218 proves that the full Euler-log translation kernel is strictly totally positive through order two, while AF-217 proves that it cannot be totally nonnegative at every order. The next finite order also survives exactly.

Put

\[
L(x):=-\log(1-e^{-x}),\qquad x>0,
\tag{1}
\]

and

\[
f(t):=L(e^t),\qquad
K(u,v):=f(u-v)=L(e^{u-v}).
\tag{2}
\]

Then `K` is **strictly totally positive of order three**. In particular, for every

\[
u_1<u_2<u_3,
\qquad
v_1<v_2<v_3,
\tag{3}
\]

one has

\[
\boxed{
\det[K(u_i,v_j)]_{i,j=1}^3>0.
}
\tag{4}
\]

Together with AF-218, all minors of orders `1`, `2`, and `3` have the strict total-positivity signs.

Returning to the Euler variables

\[
E_s(q):=-\log(1-q^{-s}),
\qquad s>0,\ q>1,
\tag{5}
\]

one has for every

\[
0<s_1<s_2<s_3,
\qquad
1<q_1<q_2<q_3,
\tag{6}
\]

\[
\boxed{
\det[E_{s_i}(q_j)]_{i,j=1}^3<0.
}
\tag{7}
\]

The minus sign is the same checkerboard sign already visible in AF-217/AF-218: increasing generator norm reverses the translation-kernel source coordinate, and reversing three columns has parity `(-1)^3=-1`.

Consequently, the first bad finite order whose existence is guaranteed by AF-217 is **at least four**. The complete Euler logarithm therefore preserves the classical ordered-sign / Chebyshev mechanism one order farther than AF-218 established.

The proof is not numerical. It reduces the order-three problem to a curvature inequality for the Euler-log profile, proves that inequality exactly by elementary exponential/logarithmic estimates, and then invokes the classical Wronskian criterion for extended complete Chebyshev systems.

## Derivation

### 1. Order two supplies the monotone first coordinate

Write

\[
g(t):=\log f(t),
\qquad
a(t):=g'(t).
\tag{8}
\]

AF-218 proves

\[
g''(t)<0
\qquad(t\in\mathbb R),
\tag{9}
\]

so `a` is strictly decreasing. Define also

\[
c(t):=\frac{f''(t)}{f(t)}
=g''(t)+g'(t)^2.
\tag{10}
\]

Because `a` is strictly monotone, `c(t)` may be regarded as a function of `a(t)`. A direct differentiation gives

\[
\frac{d^2c}{da^2}
=
2+\frac{g''''}{(g'')^2}
-\frac{(g''')^2}{(g'')^3}.
\tag{11}
\]

Introduce

\[
Q(t)
:=(g'''(t))^2-g''(t)g''''(t)-2(g''(t))^3.
\tag{12}
\]

Then

\[
\frac{d^2c}{da^2}
=-\frac{Q(t)}{(g''(t))^3}.
\tag{13}
\]

Since `g''<0`, strict positivity of `Q` is exactly strict convexity of `c` as a function of `a`.

Thus the order-three problem has an intrinsic local differential gate:

\[
\boxed{Q(t)>0\quad\text{for all }t.}
\tag{14}
\]

### 2. The differential gate is a confluent order-three determinant

The quantity `Q` has a convenient determinant form. Standard logarithmic-derivative algebra gives

\[
\boxed{
 f(t)^3Q(t)
=
\det\!\begin{pmatrix}
 f & -f' & f''\\
 f'&-f''&f'''\\
 f''&-f'''&f''''
\end{pmatrix}(t).
}
\tag{15}
\]

This is the fully confluent order-three translation determinant. Its positivity is stronger than the numerical observation that nearby `3 x 3` minors have the expected sign: it will supply a global convexity statement from which arbitrary separated minors follow.

Set

\[
x=e^t>0,
\qquad
y=e^{-x}\in(0,1),
\qquad
\ell=L(x)=-\log(1-y).
\tag{16}
\]

The first four ordinary `x`-derivatives needed below are

\[
L'(x)=-\frac{y}{1-y},
\qquad
L''(x)=\frac{y}{(1-y)^2},
\tag{17}
\]

\[
L'''(x)=-\frac{y(1+y)}{(1-y)^3},
\qquad
L''''(x)=\frac{y(1+4y+y^2)}{(1-y)^4}.
\tag{18}
\]

Using `d/dt=x d/dx` in `(15)` and simplifying gives the exact factorization

\[
f(t)^3Q(t)
=
\frac{x^3y^2}{(1-y)^6}
\big(C_0(x,y)+\ell C_1(x,y)\big),
\tag{19}
\]

where

\[
\begin{aligned}
C_0(x,y)
={}&xy\big(
 x^2y^2+2x^2y+4xy^2-3xy-x\\
&\hspace{35mm}+2y^2-4y+2
\big),
\end{aligned}
\tag{20}
\]

and

\[
\begin{aligned}
C_1(x,y)
={}&x^2-2x+2
+(-2x^3+3x^2-6)y\\
&+(-3x^2+6x+6)y^2
-(x^2+4x+2)y^3.
\end{aligned}
\tag{21}
\]

All prefactors in `(19)` are positive. It remains to prove

\[
C_0+\ell C_1>0.
\tag{22}
\]

### 3. The coefficient of the logarithm is strictly positive

First prove

\[
C_1(x,e^{-x})>0
\qquad(x>0).
\tag{23}
\]

Define

\[
R(x):=e^{3x}C_1(x,e^{-x}).
\tag{24}
\]

Direct differentiation gives

\[
R^{(k)}(0)=0,
\qquad 0\le k\le5,
\tag{25}
\]

and

\[
\begin{aligned}
R^{(6)}(x)
={}&(729x^2+1458x+972)e^{3x}\\
&-(128x^3+960x^2+1728x+864)e^{2x}\\
&-(3x^2+30x+48)e^x.
\end{aligned}
\tag{26}
\]

Factor one `e^x` and write

\[
A:=729x^2+1458x+972,
\tag{27}
\]

\[
B:=128x^3+960x^2+1728x+864,
\qquad
C:=3x^2+30x+48.
\tag{28}
\]

Then

\[
e^{-x}R^{(6)}(x)
=e^x(Ae^x-B)-C.
\tag{29}
\]

For `x>=0`, `e^x>=1+x`, hence

\[
Ae^x-B
\ge A(1+x)-B
=601x^3+1227x^2+702x+108>0.
\tag{30}
\]

Using `e^x>=1` once more in `(29)` yields

\[
\begin{aligned}
e^{-x}R^{(6)}(x)
&\ge
601x^3+1224x^2+672x+60\\
&>0.
\end{aligned}
\tag{31}
\]

Therefore `R^(6)>0` on `(0,infinity)`. Together with the six zero initial data `(25)`, repeated integration gives

\[
R(x)>0
\qquad(x>0),
\tag{32}
\]

which proves `(23)`.

### 4. The elementary logarithmic lower bound closes the determinant

Since `0<y<1`,

\[
\ell=-\log(1-y)>y.
\tag{33}
\]

By `(23)`, it therefore suffices to prove

\[
C_0+yC_1>0.
\tag{34}
\]

A direct simplification gives

\[
C_0(x,y)+yC_1(x,y)=yP(x,y),
\tag{35}
\]

with

\[
\begin{aligned}
P(x,y)
={}&2-(4x+6)y\\
&+(x^3+x^2+8x+6)y^2\\
&-(x^2+4x+2)y^3.
\end{aligned}
\tag{36}
\]

Set `y=e^{-x}` and remove the positive factor `e^{-3x}`:

\[
\begin{aligned}
S(x)
:=e^{3x}P(x,e^{-x})
={}&2e^{3x}-(4x+6)e^{2x}\\
&+(x^3+x^2+8x+6)e^x\\
&-(x^2+4x+2).
\end{aligned}
\tag{37}
\]

The Taylor coefficients through degree three vanish. For `n>=3`, the numerator of the coefficient of `x^n/n!` is

\[
A_n
=2\,3^n-(2n+6)2^n+n(n-1)^2+8n+6.
\tag{38}
\]

One has `A_3=0`, while

\[
A_4=12,
\qquad
A_5=100.
\tag{39}
\]

For every `n>=6`,

\[
\left(\frac32\right)^n>n+3.
\tag{40}
\]

Indeed `(40)` holds at `n=6`, and multiplication by `3/2` preserves it inductively because `3(n+3)/2>n+4`. Hence

\[
2\,3^n-(2n+6)2^n
=2^{n+1}\left[\left(\frac32\right)^n-(n+3)\right]>0,
\tag{41}
\]

and the remaining polynomial term in `(38)` is also positive. Thus

\[
A_n>0
\qquad(n\ge4).
\tag{42}
\]

Consequently

\[
S(x)=\sum_{n\ge4}A_n\frac{x^n}{n!}>0
\qquad(x>0).
\tag{43}
\]

Equations `(35)`--`(43)` prove `C_0+yC_1>0`. Using `(33)` and `(23)`,

\[
C_0+\ell C_1
>
C_0+yC_1
>0.
\tag{44}
\]

By `(19)`,

\[
\boxed{Q(t)>0\qquad(t\in\mathbb R).}
\tag{45}
\]

### 5. The curvature inequality gives arbitrary separated `3 x 3` minors

Combining `(13)`, `(9)`, and `(45)` shows that `c` is a strictly convex function of `a`.

Fix now arbitrary

\[
v_1<v_2<v_3
\tag{46}
\]

and define three translated functions

\[
\phi_j(u):=f(u-v_j).
\tag{47}
\]

At a fixed `u`, put `t_j=u-v_j`. Then

\[
t_1>t_2>t_3.
\tag{48}
\]

Because `a(t)=g'(t)` is strictly decreasing,

\[
a(t_1)<a(t_2)<a(t_3).
\tag{49}
\]

The first Wronskian is positive because `f>0`. The order-two Wronskian is

\[
W(\phi_1,\phi_2)
=f(t_1)f(t_2)\big(a(t_2)-a(t_1)\big)>0.
\tag{50}
\]

For order three, factor `f(t_j)` from column `j`:

\[
\begin{aligned}
W(\phi_1,\phi_2,\phi_3)
={}&\prod_{j=1}^3 f(t_j)\\
&\times
\det\!\begin{pmatrix}
1&1&1\\
a(t_1)&a(t_2)&a(t_3)\\
c(t_1)&c(t_2)&c(t_3)
\end{pmatrix}.
\end{aligned}
\tag{51}
\]

The determinant in `(51)` is strictly positive because the `a(t_j)` are strictly increasing in column order and `c` is strictly convex as a function of `a`. Hence

\[
W(\phi_1,\phi_2,\phi_3)>0
\qquad(u\in\mathbb R).
\tag{52}
\]

Thus every ordered triple of translates is an extended complete Chebyshev system on `R`: its leading Wronskians of orders one, two, and three never vanish and have the positive orientation.

The classical Wronskian criterion for ECT systems then implies that for every `u_1<u_2<u_3`,

\[
\det[\phi_j(u_i)]_{i,j=1}^3>0.
\tag{53}
\]

This is exactly `(4)`.

### 6. Return to the full Euler-factor coordinates

For every `q>1`, set

\[
v_q:=-\log\log q.
\tag{54}
\]

Then

\[
K(\log s,v_q)
=L(s\log q)
=-\log(1-q^{-s})
=E_s(q).
\tag{55}
\]

If `q_1<q_2<q_3`, then

\[
v_{q_1}>v_{q_2}>v_{q_3}.
\tag{56}
\]

Applying `(4)` in increasing `v` order and reversing the three columns gives `(7)`.

Combining AF-218 with the present result therefore gives the uniform checkerboard statement

\[
\boxed{
(-1)^{r(r-1)/2}
\det[E_{s_i}(q_j)]_{i,j=1}^r>0,
\qquad r=1,2,3,
}
\tag{57}
\]

whenever both the sample sequence `s_i` and the generator-norm sequence `q_j` are strictly increasing.

By the standard finite-order variation-diminishing/Chebyshev consequence, a nonzero finite signed source whose ordered coefficients have at most two sign changes cannot annihilate three distinct positive real Euler samples. As in AF-216/AF-218, this is an **exact** source-complexity gate; it is not by itself a uniform conditioning theorem.

## Relation to AF-216, AF-217, and AF-218

AF-216 gives an all-order Chebyshev theorem for the **first Dirichlet harmonic**. AF-217 proves that the complete Euler logarithm cannot satisfy the corresponding all-order total-positivity law: its Mellin/Laplace transform contains the nontrivial zeta zeros, which are incompatible with `PF_infinity`.

AF-218 proves that the first nontrivial finite order nevertheless survives. AF-219 now advances the exact boundary once more:

\[
\boxed{
\text{full Euler log is strictly sign-regular through order }3,
\quad
\text{but not through all orders.}
}
\tag{58}
\]

The all-order obstruction is therefore not visible at order three. The smallest failing order is at least four.

The mechanism is also more structured than an isolated determinant calculation. AF-218 supplies strict concavity of `g=log f`; AF-219 shows that the next normalized derivative coordinate

\[
c=\frac{f''}{f}
\tag{59}
\]

is strictly convex when parameterized by

\[
a=\frac{f'}f.
\tag{60}
\]

This converts the first two finite positivity levels into a nested geometric statement about the logarithmic-derivative curve `(a,c)`.

## Exact controls and boundaries

### This is not `TP_infinity`

AF-217 remains decisive. AF-219 proves only the finite orders through three. Some finite higher-order minor must fail. Nothing here implies that order four survives.

### The result is stronger than a confluent test

The determinant `(15)` checks the fully confluent order-three curvature gate, but the proof does not stop there. Its positivity makes `c(a)` globally strictly convex, which controls the Wronskian for **arbitrary separated source coordinates**. The ECT criterion then yields every separated `3 x 3` translation minor.

### This is exact fidelity, not stable recovery

Strict minors can approach zero under geometric degeneration. AF-218 already exhibits loss of an order-two curvature modulus in the small-`s log q` tail, and AF-219 does not restore a global scale-free lower bound.

A stable arithmetic application still needs quantitative separation/localization assumptions in addition to exact order-three sign regularity.

### Primality again adds no positive strength at this order

The proof holds for every real `q_j>1`, not just rational primes. Prime support is therefore compatible with the theorem but is not its cause.

To obtain an RH-facing discriminator, another argument must force the relevant prime-derived signed discrepancy to lie in a low-sign-complexity class that matched non-prime controls cannot reproduce.

### Ordered sign complexity is an extra source law

The order-three gate applies only after the source atoms are merged and ordered by generator norm. Rational primality alone does not bound the number of sign changes; AF-215 already shows that prime support can realize arbitrarily high cancellation order in a different moment setting.

### The next finite order is genuinely open here

AF-219 does not classify order four. The curvature/planar-convexity reduction used here is special to three functions: order four requires a higher-dimensional Chebyshev/Wronskian condition and cannot be inferred from strict convexity of `(a,c)`.

## Prior art and novelty assessment

The conceptual machinery is classical, and no novelty is claimed for finite-order total positivity, Pólya-frequency functions, Wronskian criteria, ECT systems, or variation diminution.

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), is the standard reference for totally positive kernels, Pólya-frequency functions, Chebyshev systems, and variation-diminishing transforms.
- H. F. Weinberger, **"A Characterization of the Polya Frequency Functions of Order 3,"** *Applicable Analysis* **15** (1983), 53--69, DOI `10.1080/00036818308839439`, is direct classical prior art on `PF_3` itself. The present result should therefore be read as an application/specialization of finite-order positivity mathematics, not as the invention of an order-three theory.
- Apoorva Khare, **"Multiply positive functions, critical exponent phenomena, and the Jain--Karlin--Schoenberg kernel,"** arXiv:`2008.05121`, gives modern finite-order `TN_p/PF_p` context. Its Section 7 records a small gap in Weinberger's treatment caused by discontinuous `TN_3` functions and supplies corrected modern characterizations/reduction results. The Euler profile here is positive and real analytic, so the discontinuous-function pathology is not used in the derivation above.
- Olga M. Katkova, **"Multiple Positivity and the Riemann Zeta-Function,"** *Computational Methods and Function Theory* **7** (2007), DOI `10.1007/BF03321628`, is direct prior art for studying finite/multiple positivity together with the Riemann zeta function, albeit for a different generating-function construction.
- Standard ECT literature records the criterion used in `(50)`--`(53)`: for an ordered analytic family, nonvanishing leading Wronskians characterize an extended complete Chebyshev system, which in turn fixes the sign of its sampling determinants.

A targeted literature search using the exact profiles `L(e^t)`, `-log(1-exp(-exp(t)))`, the Euler-factor kernel `-log(1-q^{-s})`, and the transform `Gamma(z) zeta(z+1)` did not locate the specific strict-`PF_3` statement proved above. That absence is not evidence of novelty. The durable contribution is conservatively the exact placement of the classical order-three gate inside the AF-216/AF-217/AF-218 fidelity chain.

## Consequence for the Arithmetic Fidelity frontier

The finite-order boundary has moved from three to **four**. The full Euler aggregation can transport two units of ordered sign complexity without exact collision: three positive real Euler observations separate every nonzero source in the declared two-sign-change class.

The next exact question is whether order four survives. That question should be attacked independently rather than extrapolated from `(58)`. In parallel, the more important arithmetic bottleneck remains source-side: derive a natural prime-specific law that actually bounds the sign/oscillation complexity of a canonical discrepancy, and pair it with a quantitative determinant margin on the relevant source/sample geometry. Without that source theorem and a stability modulus, even exact `PF_3` behavior remains a structural fidelity result rather than an RH mechanism.