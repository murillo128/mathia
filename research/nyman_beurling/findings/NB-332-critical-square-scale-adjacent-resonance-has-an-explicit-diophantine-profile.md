# NB-332 — Critical square-scale adjacent resonance has an explicit Diophantine profile

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-330, NB-331
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + CRITICAL-SQUARE-SCALE + ADJACENT-WITNESS + DIOPHANTINE-PROFILE + RANK-ONE-ERROR + LOGARITHMIC-RESONANCE + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let `R_n` be the rank-one comparison operator from `NB-314`. For

\[
8\le q\le n,
\qquad
\nu_q:=g_q-\frac{q-1}{q}g_{q-1},
\tag{1}
\]

consider the exact critical lattice

\[
m=dq,
\qquad
d=d_q\in\mathbb N,
\qquad
\frac dq\longrightarrow\delta\in(0,\infty).
\tag{2}
\]

Define

\[
\mathcal F_{n;q,d}
:=
\left\langle
(\sqrt{dq}\,T_{n,dq}-R_n)g_2,\nu_q
\right\rangle.
\tag{3}
\]

Then the critical-scale adjacent coefficient has the explicit limit

\[
\boxed{
q\,\mathcal F_{n;q,d}
\longrightarrow
\Phi(\delta),
}
\tag{4}
\]

where

\[
\boxed{
\Phi(\delta)
=
-\frac1{4\delta}
\sum_{k=1}^{\infty}
\frac{\|k\delta\|_{\mathbb Z}^{\,2}}{k^2}.
}
\tag{5}
\]

Here `||x||_Z` denotes the distance from `x` to the nearest integer. The series is absolutely convergent. In particular,

\[
\boxed{
\Phi(\delta)<0
\quad\Longleftrightarrow\quad
\delta\notin\mathbb N,
}
\tag{6}
\]

while

\[
\Phi(\delta)=0
\qquad(\delta\in\mathbb N).
\tag{7}
\]

Thus the adjacent resonance of `NB-331` does not simply disappear when `d/q` reaches order one. On the exact lattice `m=dq`, it survives at the critical square scale with a deterministic Diophantine amplitude for every nonintegral aspect ratio. Integer aspect ratios are genuine zeros of this **particular adjacent channel**.

Using the physical norm estimate of `NB-304`, every nonintegral `delta` therefore gives

\[
\boxed{
\liminf_{q\to\infty}
\sqrt{\log q}\,
\|\sqrt{dq}\,T_{n,dq}-R_n\|
\ge
\frac{\sqrt2\,|\Phi(\delta)|}{\sqrt{\log2}}.
}
\tag{8}
\]

If additionally `q/n -> c in (0,1]`, then `dq/n^2 -> delta c^2`, so (8) is a genuine `m asymp n^2` obstruction. This extends the subquadratic routing picture to a nontrivial family on the quadratic boundary, but it is not a uniform theorem over all critical dilations.

## 1. Exact-lattice reduction

The bilinear identity used in `NB-331` remains valid for every `q<=n`. The centered reciprocal profile of the adjacent target is

\[
\widetilde F_q(z)
=
\left\{\frac zq\right\}
-\frac{q-1}{q}
\left\{\frac z{q-1}\right\}
-\frac1{2q}.
\tag{9}
\]

For the exact lattice `m=dq`, scale by the integer `d` and put

\[
\phi(t):=\{t\}-\frac12,
\qquad
h_q(y):=\widetilde F_q(qy).
\tag{10}
\]

Since the constants cancel,

\[
\boxed{
h_q(y)
=
\phi(y)
-\frac{q-1}{q}\,
\phi\!\left(\frac q{q-1}y\right).
}
\tag{11}
\]

As in `NB-327`--`NB-331`,

\[
\mathcal F_{n;q,d}
=
d\int_0^\infty
s_d(y)h_q(y)\frac{dy}{y^2},
\qquad
s_d(y):=F_{g_2}(y/d).
\tag{12}
\]

Because `d` is an integer, `s_d` is exactly `1/2` on the blocks

\[
(2j+1)d\le y<(2j+2)d,
\qquad j\ge0,
\tag{13}
\]

and zero on the alternating blocks. Hence, with

\[
I_{q,J}:=
\int_J^{J+1}h_q(y)\frac{dy}{y^2},
\tag{14}
\]

we have the exact cell sum

\[
\boxed{
\mathcal F_{n;q,d}
=
\frac d2
\sum_{\substack{J\ge1\\
\lfloor J/d\rfloor\ \mathrm{odd}}}
I_{q,J}.
}
\tag{15}
\]

The subquadratic proof of `NB-331` only used cells `J=o(q)`. At critical scale `d/q -> delta`, the selector starts at `J asymp q`, so the whole cell profile must instead be resolved on the macroscopic coordinate `z=J/q`.

## 2. The macroscopic cell kernel is an exact derivative

Let

\[
\varepsilon_q:=\frac1{q-1},
\qquad
c_q:=\frac{q-1}{q}=\frac1{1+\varepsilon_q}.
\tag{16}
\]

For a unit cell `[J,J+1]`, write its mean as

\[
b_{q,J}:=\int_J^{J+1}h_q(y)\,dy.
\tag{17}
\]

The first term of (11) has zero cell mean. After the change of variable in the second term, one full period cancels and only an interval of length `epsilon_q` remains. If

\[
\theta_{q,J}:=\{\varepsilon_qJ\},
\]

then exactly

\[
\boxed{
b_{q,J}
=-c_q^2
\int_{\theta_{q,J}}^{\theta_{q,J}+\varepsilon_q}
\phi(u)\,du.
}
\tag{18}
\]

Consequently, whenever `J/q -> z>0` and `z` is not an integer,

\[
q\,b_{q,J}
\longrightarrow
-\phi(z).
\tag{19}
\]

Now center inside the cell:

\[
g_{q,J}(x):=h_q(J+x)-b_{q,J},
\qquad
H_{q,J}(x):=\int_0^x g_{q,J}(s)\,ds.
\tag{20}
\]

For almost every `x in (0,1)`, if `J/q -> z` then

\[
g_{q,J}(x)
\longrightarrow
\phi(x)-\phi(x+z).
\tag{21}
\]

The functions are uniformly bounded, so the convergence is also in `L^1(0,1)` and the primitives converge uniformly. If `a={z}`, the first moment identity

\[
\int_0^1
x\bigl(\phi(x)-\phi(x+a)\bigr)\,dx
=
\frac{a(1-a)}2
\tag{22}
\]

gives

\[
\int_0^1H_{q,J}(x)\,dx
\longrightarrow
-\frac{a(1-a)}2.
\tag{23}
\]

Decomposing (14) into the mean and mean-zero pieces and integrating the latter by parts,

\[
I_{q,J}
=
\frac{b_{q,J}}{J(J+1)}
+
2\int_0^1
\frac{H_{q,J}(x)}{(J+x)^3}\,dx.
\tag{24}
\]

Therefore, for `J/q -> z>0` away from the integer discontinuities,

\[
\boxed{
q^3I_{q,J}
\longrightarrow
C(z)
:=-\frac{\phi(z)}{z^2}
-\frac{\{z\}(1-\{z\})}{z^3}.
}
\tag{25}
\]

This kernel has a useful exact primitive. Set

\[
B(z):=
\frac{\{z\}(1-\{z\})}{2z^2},
\qquad z>0.
\tag{26}
\]

On every open interval between consecutive integers,

\[
\boxed{C(z)=B'(z).}
\tag{27}
\]

Moreover `B` extends continuously across every positive integer, with value zero there. Thus it is absolutely continuous on every compact subinterval of `(0,infinity)` and (27) may be integrated across integer breakpoints without an extra jump term.

For passage from cells to the infinite selector sum, no hidden compactness is needed. From (18), `|b_(q,J)| << 1/q`; after subtracting the cell mean, the primitive `H_(q,J)` is uniformly bounded. Hence

\[
\boxed{
|I_{q,J}|
\ll
\frac1{qJ^2}+\frac1{J^3}.
}
\tag{28}
\]

When `J>=Lq`, summing (28) gives `O(1/(Lq^2))`. After multiplication by the factor `qd` relevant to `q F`, this is `O(1/L)` uniformly when `d/q` stays in a compact subset of `(0,infinity)`. Thus the compact Riemann-sum limit can be followed by `L->infinity`.

## 3. The selector integral becomes a Diophantine series

Let `d/q -> delta>0`. On the scale `z=J/q`, the selected cells in (15) converge, away from endpoints, to the alternating union

\[
\mathcal S_\delta
:=
\bigcup_{j\ge0}
[(2j+1)\delta,(2j+2)\delta).
\tag{29}
\]

Equations (25) and (28) therefore yield

\[
q\mathcal F_{n;q,d}
\longrightarrow
\frac\delta2
\int_{\mathcal S_\delta}C(z)\,dz.
\tag{30}
\]

Using `C=B'` and `B(z)=O(z^(-2))`,

\[
\frac\delta2
\int_{\mathcal S_\delta}C(z)\,dz
=
\frac\delta2
\sum_{j=0}^\infty
\left(
B((2j+2)\delta)-B((2j+1)\delta)
\right).
\tag{31}
\]

Write

\[
\psi(x):=\{x\}(1-\{x\}).
\tag{32}
\]

Since

\[
B(k\delta)
=
\frac{\psi(k\delta)}{2k^2\delta^2},
\]

(31) becomes

\[
\boxed{
\Phi(\delta)
=
\frac1{4\delta}
\sum_{k=1}^\infty
(-1)^k\frac{\psi(k\delta)}{k^2}.
}
\tag{33}
\]

The alternating expression has a more revealing sign-definite form. If

\[
F(\delta):=
\sum_{k=1}^\infty
\frac{\psi(k\delta)}{k^2},
\]

then separating even and odd `k` gives

\[
\sum_{k=1}^\infty
(-1)^k\frac{\psi(k\delta)}{k^2}
=
\frac12F(2\delta)-F(\delta).
\tag{34}
\]

For every real `x`, the elementary pointwise identity

\[
\boxed{
\psi(x)-\frac12\psi(2x)
=
\|x\|_{\mathbb Z}^{\,2}
}
\tag{35}
\]

holds by splitting according to whether `{x}` is below or above `1/2`. Substitution into (34) proves the announced formula

\[
\Phi(\delta)
=
-\frac1{4\delta}
\sum_{k=1}^\infty
\frac{\|k\delta\|_{\mathbb Z}^{\,2}}{k^2}.
\]

Every term on the right is nonnegative. If `delta` is an integer all terms vanish. If `delta` is not an integer, already the `k=1` term is positive. This proves (6)--(7) without any equidistribution input and without distinguishing rational from irrational aspect ratios.

## 4. Operator consequence and the quadratic boundary

`NB-304` gives

\[
\|\nu_q\|_2^2
\le
\frac{2H_{q-2}+1+\pi^2/18}{q^2},
\tag{36}
\]

while

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2.
\tag{37}
\]

For every fixed nonintegral `delta`, (4)--(6) and Cauchy--Schwarz therefore imply

\[
\|\sqrt{dq}\,T_{n,dq}-R_n\|
\ge
\frac{|\mathcal F_{n;q,d}|}
{\|g_2\|_2\,\|\nu_q\|_2}
=
\frac{\sqrt2\,|\Phi(\delta)|+o(1)}
{\sqrt{\log2}\,\sqrt{\log q}},
\tag{38}
\]

which yields (8).

This sharpens the method boundary left by `NB-331`. There, `d/q -> 0` made the selected source blocks microscopic on the macroscopic adjacent scale and produced the universal coefficient `-log 2/4`. At `d/q -> delta>0`, the blocks have finite macroscopic width and the coefficient remembers their arithmetic placement through the fractional parts `{k delta}`. The quadratic boundary is therefore not a featureless transition: on the exact lattice it carries an explicit Diophantine profile.

The integer zeros are equally informative. At `delta in N`, the leading `1/q` coefficient of this adjacent channel cancels. This does **not** imply

\[
\|\sqrt{dq}\,T_{n,dq}-R_n\|\to0.
\]

Another adjacent index, a nonzero remainder phase `m=dq+r`, or a different source/target pair may route around those zeros, just as `NB-330` routed around the half-cell zero of `NB-329`. The next source-side discriminator is therefore narrower than the question left by `NB-331`: resolve the full critical profile when `d/q asymp 1` and `r/d` is nonzero, and test whether the integer nodes of (5) survive optimization over admissible witnesses.

The result remains entirely source-side. It says nothing about occupation by the first-free Ford datum, finite-section target gain, or RH.

## 5. Adversarial checks and prior-art boundary

The proof was pressure-tested at the points where the square-scale passage could lose a factor or silently assume equidistribution.

- The factor in (30) is `delta/2`, not `1/2`: there are order `q` cells per bounded `z` interval, each cell integral is order `q^(-3)`, and the prefactor in (15) is `d/2 asymp delta q/2`.
- The first selected macroscopic block begins at `z=delta>0`, so the apparent singularity of `B(z)` at the origin is never sampled.
- Integer discontinuities of `phi` affect only a null set in the Riemann limit. The primitive `B` is continuous at positive integers, so no distributional jump term is missing in (31).
- The tail estimate (28) is summable uniformly after the critical prefactor. It justifies taking the infinite selector union only after a compact Riemann-sum limit.
- Formula (35) shows directly that no rational/irrational case split or equidistribution theorem is being imported. The sign and zero set of `Phi` are elementary.
- The zero set in (7) belongs only to the chosen channel `g_2 -> nu_q`. It is not an operator-norm upper bound and is not evidence of rank-one mixing by itself.
- The ambient section remains `U_n`; only the witness index is `q<=n`. No replacement of `T_(n,m)` or `R_n` by an operator on `U_q` occurs.

As an additional numerical audit, exact piecewise-constant cell integration for growing `q` was checked against (5) at several rational and nonintegral aspect ratios; the scaled coefficients converge to the predicted negative profile and vanish at integral aspect ratios. These checks are diagnostic only and are not used in the proof.

A fresh prior-art audit covered the nearby literature on multiplicative autocorrelation of the fractional-part function and classical Davenport/Bernoulli fractional-part series. Those sources make the appearance of periodic quadratic fractional-part functions unsurprising, but no external theorem is load-bearing here: the critical finite-section profile, the reduction (33), and the nearest-integer-square identity (35) are derived directly above. No claim of bibliographic novelty is made, and `SOURCES.md` needs no new durable dependency.

## Research implication

The source-side transition is now split more finely:

- `NB-331` proves a universal logarithmic obstruction for every `n<=m=o(n^2)` by adaptive adjacent routing.
- This finding shows that on the exact critical lattice `m=dq` with `d/q->delta`, the same adjacent mechanism survives at order `1/sqrt(log q)` for every nonintegral `delta`, with amplitude (5).
- Integral `delta` are exact zeros of the leading adjacent profile and therefore become the first genuinely arithmetic candidate points where critical-scale mixing could improve, but only after optimization over the remaining witnesses and remainder phases.

The immediate next question is whether those integer nodes are stable under critical off-lattice drift `m=dq+r` with `r/d -> rho`, or whether another adjacent mode routes around them and restores a nonzero `1/sqrt(log n)` obstruction.