# AF-394 — Connected curvature support completes smooth PF3 fidelity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `BOUNDARY-TOPOLOGY` · `MULTISCALE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^4`, put

\[
g=\log f,
\qquad
q=-g'',
\qquad
\Omega=\{t\in\mathbb R:q(t)>0\},
\tag{1}
\]

and let

\[
K_f(x,y)=f(x-y).
\tag{2}
\]

Then `K_f` is totally nonnegative through order three if and only if all three conditions hold:

1. `q\ge0` on `\mathbb R`;
2. `\Omega` is an interval, allowing the empty interval and unbounded intervals;
3. on `\Omega`,

\[
\boxed{(\log q)''\le2q.}
\tag{3}
\]

The empty case is exactly `q\equiv0`, when `f=e^{at+b}` and `K_f` has rank one.

Thus AF-393's positive-curvature differential criterion extends across smooth curvature zeros with one additional global datum: **the positive-curvature set must be connected**. A zero of `q` may occur at the boundary of that interval, even with infinite-order contact as in AF-391, but it cannot split two positive-curvature regions.

There is an immediate multiscale recognition consequence. Under the shrinking solid `PF_2/PF_3` hypotheses of AF-388, the sampled hierarchy already implies

\[
q\ge0,
\qquad
2q^3-qq''+(q')^2\ge0.
\tag{4}
\]

On `\Omega`, `(4)` is exactly `(3)`. Therefore, for every `C^\infty` profile satisfying those multiscale solid hypotheses,

\[
\boxed{
K_f\in TN_3
\quad\Longleftrightarrow\quad
\{q>0\}\text{ is an interval}.
}
\tag{5}
\]

So after compatible solid tests have been retained at arbitrarily fine scales, the residual obstruction is no longer another local differential or finite-window inequality. It is the **component topology of positive logarithmic curvature**.

## Fixed-gap orientation reduction

Fix positive column gaps

\[
a>0,
\qquad b>0,
\]

and, with `t=x-y_1`, write

\[
U(t)=\frac{f(t-a)}{f(t)},
\qquad
V(t)=\frac{f(t-a-b)}{f(t)}.
\tag{6}
\]

For increasing row coordinates `t_1<t_2<t_3`, the corresponding order-three translation minor has the same sign as

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}.
\tag{7}
\]

Define the adjacent curvature masses

\[
A(t)=\int_{t-a}^{t}q(s)\,ds,
\qquad
B(t)=\int_{t-a-b}^{t-a}q(s)\,ds.
\tag{8}
\]

Then

\[
(\log U)'=A,
\qquad
(\log V)'=A+B.
\tag{9}
\]

When `A>0`, `U` is a local coordinate and the tangent slope of the curve `(U,V)` is

\[
S(t):=\frac{V'}{U'}
=\frac{V}{U}\frac{A+B}{A}.
\tag{10}
\]

If also `B>0`, direct differentiation gives

\[
\frac{d}{dt}\log S
=
\frac{B}{A+B}
\left(
A+B+\frac{B'}B-\frac{A'}A
\right).
\tag{11}
\]

This is the AF-392 finite-window expression, but `(11)` itself only needs `A,B>0`; it does not require `q` to be positive globally.

## Necessity: a PF3 kernel cannot split positive curvature

If `K_f\in TN_3`, then in particular `K_f\in TN_2`. For a positive translation kernel this is equivalent to log-concavity of `f`, hence

\[
q=-g''\ge0.
\tag{12}
\]

On every open interval where `q>0`, the local argument of AF-393 applies. Shrinking positive adjacent windows in `(11)` gives

\[
(\log q)''\le2q,
\tag{13}
\]

so only connectedness of `\Omega` remains to prove.

For later use, note the elementary orientation consequence of `(7)`. Since `(12)` makes both `U` and `V` nondecreasing, if for some

\[
t_1<t_2<t_3
\]

we have

\[
U(t_1)=U(t_2)<U(t_3),
\qquad
V(t_1)<V(t_2),
\tag{14}
\]

then `(7)` equals

\[
-(U(t_3)-U(t_1))(V(t_2)-V(t_1))<0,
\tag{15}
\]

contradicting `TN_3`. Thus a vertical motion of the normalized curve cannot occur before a later increase of `U`.

### A zero interval cannot separate two positive regions

Suppose first that a nontrivial zero interval separates positive curvature on its left and right. Choose `a,b>0` and `t_1<t_2` inside that gap so that

\[
A(t)=0,
\qquad
B(t)>0
\]

throughout `[t_1,t_2]`. This is always possible by placing the right window `(t-a,t)` inside the zero gap while the immediately preceding left window still overlaps the left positive component.

By `(9)`, `U` is constant and `V` is strictly increasing on `[t_1,t_2]`. After moving `t` far enough for the right window to enter the positive component on the other side of the gap, `U` increases. Hence a triple satisfying `(14)` exists, contradicting `(15)`.

So no positive-length zero gap can separate two components of `\Omega`.

### A single zero cannot separate two positive regions either

It remains to rule out a point `c` with

\[
q(c)=0
\tag{16}
\]

and positive-curvature points arbitrarily close on both sides.

Choose `a,b>0` such that

\[
A=\int_c^{c+a}q(s)\,ds>0,
\qquad
B=\int_{c-b}^{c}q(s)\,ds>0,
\tag{17}
\]

and evaluate `(11)` at `t=c+a`. Because `TN_3` makes the differentiable graph `V(U)` locally convex whenever `A>0`, its tangent slope is nondecreasing and `(11)` must be nonnegative. Since `q(c)=0`, this gives

\[
A+B
-\frac{q(c-b)}B
-\frac{q(c+a)}A
\ge0.
\tag{18}
\]

Now take a sequence `\varepsilon_n\downarrow0`. On the right choose

\[
a_n\in(0,\varepsilon_n]
\]

at which `q(c+a_n)` is the maximum of `q` on `[c,c+\varepsilon_n]`; then it is also a maximum on `[c,c+a_n]`, and

\[
\frac{q(c+a_n)}{\int_c^{c+a_n}q}
\ge\frac1{a_n}.
\tag{19}
\]

Choose `b_n` analogously on the left, obtaining

\[
\frac{q(c-b_n)}{\int_{c-b_n}^{c}q}
\ge\frac1{b_n}.
\tag{20}
\]

The two masses in `(17)` tend to zero by continuity, while the last two terms in `(18)` are at least `1/a_n` and `1/b_n`. For large `n`, `(18)` is impossible. Thus no zero of `q` can have positive-curvature points approaching from both sides.

If an open set in `\mathbb R` is disconnected, two of its positive regions are separated either by a zero interval or by a zero boundary point approached from both sides. The two arguments above therefore show that `\Omega` must be an interval. This proves necessity of all three conditions.

## Sufficiency: connected curvature turns the local inequality into global convexity

Assume now that

\[
q\ge0,
\qquad
\Omega=\{q>0\}\text{ is an interval},
\qquad
(\log q)''\le2q\text{ on }\Omega.
\tag{21}
\]

If `\Omega` is empty then `q\equiv0`, `g` is affine, and `K_f` has rank one, so suppose `\Omega` is nonempty.

Fix `a,b>0` and use `(6)`--`(10)`. The set

\[
J=\{t:A(t)>0\}
\tag{22}
\]

is itself an interval because `\Omega` is an interval. Hence `U` is strictly increasing on `J`, constant before `J`, and constant after `J`.

Where `A>0` but `B=0`, equation `(9)` gives

\[
\frac{d}{dt}\log\frac{V}{U}=B=0,
\]

and `(10)` reduces to

\[
S=\frac VU.
\tag{23}
\]

Thus the initial finite slope is constant.

Where `A,B>0`, the common boundary `t-a` lies inside `\Omega`. Put

\[
r=(\log q)'.
\tag{24}
\]

Condition `(21)` says

\[
r'(s)\le2q(s)
\qquad(s\in\Omega).
\tag{25}
\]

For every positive-curvature point `x` in the left window and `y` in the right window,

\[
r(y)-r(x)
\le2\int_x^yq(s)\,ds.
\tag{26}
\]

Average `(26)` against the normalized curvature measures

\[
\frac{q(x)\,dx}{B},
\qquad
\frac{q(y)\,dy}{A}.
\tag{27}
\]

With curvature-mass coordinate

\[
Q(z)=\int_{t-a}^{z}q(s)\,ds,
\tag{28}
\]

these measures push forward to uniform Lebesgue measure on `[-B,0]` and `[0,A]`. Consequently

\[
\frac{A'}A-\frac{B'}B
\le A+B,
\tag{29}
\]

or equivalently

\[
A+B+\frac{B'}B-\frac{A'}A\ge0.
\tag{30}
\]

By `(11)`, `S=V'/U'` is therefore nondecreasing wherever both masses are positive. Together with the constant initial slope `(23)`, the curve `V` as a function of `U` is convex throughout the nonvertical part of `J`.

The only possible region with

\[
A=0,
\qquad
B>0
\tag{31}
\]

occurs **after** the positive-curvature interval has passed through the right window. There `U` is already at its final value while `V` may still increase, so `(31)` contributes only a terminal vertical segment. A terminal vertical segment preserves nonnegative orientation: if `U(t_2)=U(t_3)>U(t_1)`, then `(7)` is

\[
(U(t_2)-U(t_1))(V(t_3)-V(t_2))\ge0.
\tag{32}
\]

Before `J`, both masses vanish and the normalized curve is constant. Hence every increasing triple has nonnegative determinant `(7)`.

Because `a,b>0` were arbitrary, every order-three translation minor is nonnegative. Condition `q\ge0` already gives all order-two minors, and order one is positive. Thus

\[
K_f\in TN_3,
\tag{33}
\]

proving sufficiency.

## Exact residual resource under multiscale solid sampling

Now impose the AF-388 hypotheses: for a sequence `h_\nu\to0`, every solid order-two and order-three Toeplitz minor of the sampled profile is nonnegative.

AF-388 derives exactly

\[
q\ge0
\tag{34}
\]

and

\[
R:=2q^3-qq''+(q')^2\ge0.
\tag{35}
\]

On `\Omega`, divide `(35)` by `q^2` to obtain

\[
(\log q)''\le2q.
\tag{36}
\]

Thus the multiscale solid certificate already supplies every analytic condition in the characterization above. It may also force stronger boundary flatness, as AF-389 shows, but that extra jet information is not what remains missing for the `TN_3` decision.

Combining `(34)`--`(36)` with the main theorem gives `(5)`: **connectedness of the positive-curvature set is the exact remaining global resource**.

This clarifies the information-loss mechanism behind AF-387--AF-393. A fixed lattice can lose placement information through lower-order degeneracy. Vanishing-mesh compatibility recovers the local differential cone and forces exceptional zeros onto increasingly rigid strata. But arbitrarily fine local sampling does not, by itself, encode whether the positive-curvature region consists of one component or several. The final missing bit of structure is topological rather than another infinitesimal coefficient.

## Prior art and novelty audit

The unrestricted `PF_3` classification problem is classical. H. F. Weinberger's 1983 paper is explicitly a characterization of Pólya-frequency functions of order three, while Schoenberg and Karlin provide the surrounding translation-kernel and total-positivity theory. The accessible publisher and institutional metadata confirm Weinberger's bibliographic identity and scope, but the primary article text was not accessible in this literature pass.

Accordingly **no novelty claim is made** for the characterization `(1)`--`(3)`. It may be a smooth reformulation, specialization, or direct consequence of Weinberger's classical theorem. The durable Arithmetic Fidelity result is the internal identification of the exact resource left by the AF-388 multiscale compression: after the local differential condition has already been recovered, continuum order-three fidelity is equivalent to retaining the component topology of `\{-(\log f)''>0\}`.

Primary neighboring sources:

- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* 15(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`.
- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968).
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* 1 (1951), 331--374, DOI `10.1007/BF02790092`.

A targeted search of the available literature metadata did not expose this exact curvature-support formulation. That absence is not evidence of novelty and is not used as such.

## Boundaries and falsification checks

- Positivity of `f` is load-bearing because `g=\log f` and the row normalizations in `(6)` must be globally defined.
- `C^4` is a convenient sufficient regularity level. It makes `q\in C^2` and `(\log q)''` classical on `\Omega`. Weaker absolutely-continuous formulations are plausible but are not claimed.
- The theorem concerns order three only. It does not assert that one support-topology condition plus one local differential inequality characterizes higher `PF_k` classes.
- Connectedness is imposed on the **positive set of logarithmic curvature**, not on the positive support of `f`; here `f` is positive everywhere.
- Boundary zeros are allowed. AF-391's nonquasianalytic flat-zero example is consistent with the theorem because its positive-curvature set is one half-line.
- A two-sided infinitely-flat zero is not harmless: even if `(3)` holds separately on both sides, `(18)` shows that the missing cross-boundary placement data force a negative order-three minor.
- The multiscale corollary does not say that solid tests automatically prove connectedness. It identifies connectedness as the exact extra global fact required after the AF-388 local consequences are known.
- No arithmetic source and no RH consequence are asserted.

## Riemann-facing boundary

The result is a recognition theorem for a compression mechanism, not evidence that a prime-derived kernel with the required signs exists.

Its reusable lesson is sharper than a generic warning about information loss. A hierarchy of increasingly fine local certificates can recover every pointwise differential constraint relevant to the target and still omit one global discriminator: **which local positive regions belong to the same connected component**. If an RH-facing construction compresses a prime-derived object to local or multiscale determinant data, a proof must either retain that topology explicitly or derive it from the arithmetic source. The downstream positivity machinery cannot manufacture it after the component information has been discarded.