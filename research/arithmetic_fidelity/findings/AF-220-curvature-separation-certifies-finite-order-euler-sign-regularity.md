# AF-220 — curvature and coordinate separation certify finite-order Euler sign regularity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `QUANTITATIVE-FIDELITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-217 proves that the full Euler-log translation kernel cannot be totally nonnegative at all orders, while AF-218 and AF-219 prove that it is strictly totally positive through orders two and three. There is also an exact quantitative regime in which **every prescribed finite order** is certified from local curvature and coordinate separation.

Put

\[
L(x):=-\log(1-e^{-x}),\qquad
f(t):=L(e^t),\qquad
K(u,v):=f(u-v),
\tag{1}
\]

and let

\[
g(t):=\log f(t),\qquad
\kappa(t):=-g''(t)>0.
\tag{2}
\]

The strict positivity of `\kappa` is AF-218's global logarithmic-curvature theorem.

Fix a compact interval `I\subset\mathbb R` and write

\[
\kappa_I:=\min_{t\in I}\kappa(t)>0.
\tag{3}
\]

Let

\[
u_1<\cdots<u_m,\qquad v_1<\cdots<v_n
\tag{4}
\]

be finite coordinate sets such that every interaction difference `u_i-v_j` lies in `I`. Define

\[
\delta_U:=\min_i(u_{i+1}-u_i),\qquad
\delta_V:=\min_j(v_{j+1}-v_j).
\tag{5}
\]

For an integer `r` with `2\le r\le\min(m,n)`, set

\[
c_r:=4\cos^2\!\frac{\pi}{r+1}.
\tag{6}
\]

Then

\[
\boxed{
\kappa_I\,\delta_U\delta_V>\log c_r
\quad\Longrightarrow\quad
[K(u_i,v_j)]\text{ is strictly totally positive through order }r.
}
\tag{7}
\]

In other words, every square minor of size `s\le r` is strictly positive.

For the Euler matrix

\[
E_s(q):=-\log(1-q^{-s}),\qquad s>0,\ q>1,
\tag{8}
\]

let

\[
0<s_1<\cdots<s_m,\qquad 1<q_1<\cdots<q_n,
\tag{9}
\]

and define

\[
\delta_S:=\min_i\log\frac{s_{i+1}}{s_i},\qquad
\delta_Q:=\min_j\log\frac{\log q_{j+1}}{\log q_j}.
\tag{10}
\]

If all interaction coordinates

\[
\log(s_i\log q_j)
\tag{11}
\]

lie in the same compact interval `I` and

\[
\boxed{
\kappa_I\,\delta_S\delta_Q>\log c_r,
}
\tag{12}
\]

then every selected `s\times s` Euler minor with `s\le r` has the strict checkerboard sign

\[
\boxed{
(-1)^{s(s-1)/2}
\det\!\Big[E_{s_{i_a}}(q_{j_b})\Big]_{a,b=1}^{s}>0.
}
\tag{13}
\]

At the live order-four frontier,

\[
c_4=4\cos^2\frac{\pi}{5}=\frac{3+\sqrt5}{2},
\tag{14}
\]

so

\[
\boxed{
\kappa_I\,\delta_S\delta_Q>
\log\frac{3+\sqrt5}{2}
\quad\Longrightarrow\quad
\text{strict Euler sign regularity through order four.}
}
\tag{15}
\]

Thus any bad `4\times4` Euler minor allowed by AF-217 must lie outside this separated-curvature regime. AF-220 does **not** prove global order-four positivity; it localizes where a counterexample can occur.

## Derivation

### 1. Euler logarithmic curvature controls every adjacent cross ratio

Define

\[
h(u,v):=\log K(u,v)=g(u-v).
\tag{16}
\]

Then

\[
\frac{\partial^2 h}{\partial u\,\partial v}(u,v)
=-g''(u-v)=\kappa(u-v)>0.
\tag{17}
\]

For any `u<u'` and `v<v'`, the fundamental theorem of calculus in two variables gives

\[
\begin{aligned}
&\log\frac{K(u,v)K(u',v')}{K(u,v')K(u',v)}\\
&\qquad=
\int_u^{u'}\int_v^{v'}\kappa(a-b)\,db\,da.
\end{aligned}
\tag{18}
\]

If the four corner differences lie in the interval `I`, then every intermediate difference `a-b` in the integration rectangle also lies in `I`. Hence

\[
\boxed{
\frac{K(u,v)K(u',v')}{K(u,v')K(u',v)}
\ge
\exp\!\big(\kappa_I(u'-u)(v'-v)\big).
}
\tag{19}
\]

For adjacent nodes from `(4)`, this yields the uniform lower bound

\[
\frac{K(u_i,v_j)K(u_{i+1},v_{j+1})}
{K(u_i,v_{j+1})K(u_{i+1},v_j)}
\ge
\exp(\kappa_I\delta_U\delta_V).
\tag{20}
\]

This is the finite-order extension of AF-218's order-two curvature modulus: the same retained mixed-log curvature now controls the local cross ratios required by a general determinant criterion.

### 2. The Katkova–Vishnyakova criterion turns the cross-ratio margin into determinant positivity

Katkova and Vishnyakova proved the following sharp sufficient criterion. If `M=(a_{ij})` is a positive `k\times k` matrix and

\[
a_{ij}a_{i+1,j+1}
>
4\cos^2\!\frac{\pi}{k+1}\,
 a_{i,j+1}a_{i+1,j}
\tag{21}
\]

for all adjacent indices, then

\[
\det M>0.
\tag{22}
\]

The constant in `(21)` is sharp for arbitrary positive matrices.

Assume `(7)`. Take any square `s\times s` submatrix of `[K(u_i,v_j)]` with `1\le s\le r`, keeping the inherited increasing row and column order. Adjacent selected coordinates can only be farther apart than the minimum gaps in `(5)`, so `(19)` gives every adjacent cross ratio in this submatrix the strict bound

\[
\frac{a_{ij}a_{i+1,j+1}}{a_{i,j+1}a_{i+1,j}}
>
c_r.
\tag{23}
\]

The constants

\[
c_s=4\cos^2\frac{\pi}{s+1}
\tag{24}
\]

increase with `s`, hence `c_s\le c_r`. Therefore `(23)` implies the Katkova–Vishnyakova hypothesis at the actual submatrix size `s`, and

\[
\det M_s>0.
\tag{25}
\]

Because the selected submatrix was arbitrary, every minor through order `r` is positive. This proves `(7)`.

For `r=2`, `c_2=1`, so `(7)` is automatic whenever the coordinates are genuinely separated; this is consistent with AF-218's global `STP_2` theorem. For `r=3`, the criterion asks for the stronger quantitative condition `\kappa_I\delta_U\delta_V>\log2`, whereas AF-219 proves `STP_3` globally without any such separation. The criterion is therefore a sufficient certificate, not a characterization of this special kernel.

### 3. Increasing generator norms produce the Euler checkerboard sign

Set

\[
u_i:=\log s_i,
\qquad
v_j:=-\log\log q_j.
\tag{26}
\]

Then

\[
K(u_i,v_j)
=f(\log(s_i\log q_j))
=-\log(1-q_j^{-s_i})
=E_{s_i}(q_j).
\tag{27}
\]

Increasing `q_j` makes `v_j` decrease. Reversing the `s` selected source columns restores increasing `v` order and contributes the determinant sign

\[
(-1)^{s(s-1)/2}.
\tag{28}
\]

The absolute gaps in the reversed `v` coordinates are exactly the log-log gaps `\delta_Q` in `(10)`. Applying `(7)` after this reversal proves `(13)`.

### 4. Order four is confined to a weak-cross-ratio region

For `r=4`, the Katkova–Vishnyakova threshold is

\[
c_4=\frac{3+\sqrt5}{2}=\varphi^2\approx2.618.
\tag{29}
\]

Thus a nonpositive corrected `4\times4` Euler determinant can occur only if the condition `(15)` fails. More locally, the contrapositive of the determinant criterion says that any nonpositive positive `4\times4` translation determinant has at least one adjacent cross ratio no larger than `\varphi^2`.

This is a real narrowing of AF-219's unresolved order-four question. A search for a first bad Euler minor need not treat the whole positive coordinate space uniformly: any counterexample must enter a region where curvature, row separation, source separation, or some combination of the three is too weak to force the sharp general positive-matrix criterion.

It also identifies a reusable finite-order fidelity resource:

\[
\boxed{
\text{retained mixed-log curvature}
\times
\text{sample separation}
\times
\text{source separation}.
}
\tag{30}
\]

The resource is quantitative and compositional in a way that bare exact injectivity is not.

### 5. Consecutive-prime tails exhaust this separation certificate

The theorem applies to arbitrary generator norms `q>1`; primality is not used in its positive direction. On actual rational-prime tails, however, the source-separation resource has an exact degeneration.

If `p<q` are consecutive primes, Bertrand's postulate gives `q<2p`, and therefore

\[
0<\log\frac{\log q}{\log p}
<
\log\!\left(1+\frac{\log2}{\log p}\right)
\longrightarrow0.
\tag{31}
\]

Consequently, for fixed-size blocks of consecutive primes tending to infinity,

\[
\delta_Q\longrightarrow0.
\tag{32}
\]

Suppose such a family is normalized so that all interaction coordinates `(11)` remain in one fixed compact interval `I`. Then `\kappa_I` is fixed and positive, while every row-coordinate gap is bounded by the diameter of `I`. Hence

\[
\kappa_I\delta_S\delta_Q\longrightarrow0.
\tag{33}
\]

For every fixed `r\ge3`, the separation certificate `(12)` must therefore eventually fail on consecutive-prime tails.

This is **not** a theorem that the corresponding Euler minors become bad. AF-219 already gives the decisive warning: order three remains globally positive even though the present sufficient certificate degenerates. Equation `(33)` says only that curvature plus pairwise coordinate separation cannot by itself provide a uniform tail certificate. A genuinely prime-facing theorem needs a stronger retained relation or a source law not reducible to minimum log-log spacing.

## Relation to the current Arithmetic Fidelity frontier

AF-216 shows that bounded ordered sign complexity limits cancellation for polynomial moments and the first Dirichlet harmonic. AF-217 proves that the full Euler logarithm cannot transport that mechanism by all-order total positivity. AF-218 and AF-219 then recover exact full-Euler sign regularity through orders two and three.

AF-220 supplies the missing quantitative bridge between those low-order successes and the all-order obstruction. **Any finite target order is guaranteed on sufficiently curved and separated compact configurations**, with an explicit sharp-for-general-matrices threshold. In particular, order-four failure is forced into a geometrically degenerate region rather than being free to occur everywhere.

The result does not resolve the more important source-side question identified by AF-216--AF-219. Rational primality alone does not bound cancellation complexity, and minimum prime spacing degenerates in the tail. A useful RH-facing application still requires an independently derived arithmetic restriction on the signed discrepancy, together with an observation theorem that transports that restriction at the required scale.

## Exact controls and boundaries

### This is sufficient, not necessary

Katkova–Vishnyakova's constant is sharp over arbitrary positive matrices, but the Euler-log matrices form a highly constrained translation-kernel family. Sharpness of the general matrix theorem does not imply sharpness of `(7)` or `(15)` for this family. AF-219 already proves substantial non-sharpness at order three.

### This does not establish global `STP_4`

Equation `(15)` proves order four only in a declared compact separated regime. Configurations failing the inequality remain undecided. No numerical search, confluent determinant sign, or local Taylor calculation is promoted here to a global theorem.

### Compact interaction control is essential to this curvature bound

AF-218 proves `\kappa(t)>0` everywhere but also shows `\kappa(t)\to0` in the small-`e^t` tail. A global positive lower curvature modulus does not exist, so `(7)` cannot be made scale-free by replacing `\kappa_I` with a universal constant.

### Criterion failure is not determinant failure

The prime-tail conclusion `(33)` kills this particular separation certificate only. It does not produce a bad prime minor and does not weaken AF-218 or AF-219.

### Primality supplies no positive input to the theorem

The proof works unchanged for arbitrary `q_j>1`. Prime support is therefore an admissible specialization, not the source of the sign regularity. A prime-specific gain must come from a non-hereditary relation among the natural coefficients, supports, or both.

### No RH consequence is claimed

The theorem concerns fidelity of finite Euler-factor observations. It neither locates zeta zeros nor excludes off-critical zeros. Its role is to identify an exact finite-order survival regime and a quantitative resource that a later arithmetic mechanism could potentially exploit.

## Prior art and novelty assessment

The determinant step is classical and no novelty is claimed for the finite-order matrix criterion.

- Olga M. Katkova and Anna M. Vishnyakova, **“On sufficient conditions for the total positivity and for the multiple positivity of matrices,”** *Linear Algebra and its Applications* **416** (2006), 1083–1097, DOI `10.1016/j.laa.2006.01.009`, arXiv:`math/0504183`. Their theorem gives exactly the sharp positive-matrix determinant criterion `(21)` used above.
- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968). Classical background for total positivity, sign regularity, and variation-diminishing kernels.
- Olga M. Katkova, **“Multiple positivity and the Riemann zeta-function,”** *Computational Methods and Function Theory* **7** (2007), 13–31, arXiv:`math/0505174`. This is direct prior art that finite-order Pólya-frequency/multiple-positivity conditions are already an established language around the Riemann zeta function. Its Toeplitz/coefficient setting is different from the Euler-log translation kernel studied here.

AF-218 supplies the Euler-specific strict curvature `\kappa=-g''>0`; AF-219 supplies the stronger global order-three theorem. AF-220 is the direct specialization of the classical Katkova–Vishnyakova local-ratio criterion to that exact Euler-log curvature. The value here is the resulting **explicit finite-order fidelity gate and localization of the order-four frontier**, not a claim that the underlying determinant criterion or finite multiple positivity is new.