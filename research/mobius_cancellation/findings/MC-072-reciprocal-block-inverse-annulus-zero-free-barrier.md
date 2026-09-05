# MC-072 — The first reciprocal block of the signed inverse already carries the full zero-free burden

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic signed-inverse architecture of `MC-071`. For a fixed odd prime `q`, let

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
f_\chi(n)=\mu(n)^2\chi(n),
\qquad
F_\chi(x)=\sum_{n\le x}f_\chi(n),
\]

and let `k_chi` be the Dirichlet inverse of `h_chi=1*f_chi`. Write

\[
K_\chi(x):=\sum_{n\le x}k_\chi(n).
\]

`MC-071` gives the exact recovery formula

\[
M(X)=\sum_{d\le X}k_\chi(d)F_\chi(X/d).
\tag{1}
\]

Grouping the divisor variable by the reciprocal block

\[
m=\left\lfloor\frac Xd\right\rfloor
\]

gives the exact finite identity

\[
\boxed{
M(X)
=
\sum_{m=1}^{X}
F_\chi(m)
\left(
K_\chi\!\left(\left\lfloor\frac Xm\right\rfloor\right)
-
K_\chi\!\left(\left\lfloor\frac X{m+1}\right\rfloor\right)
\right).
}
\tag{2}
\]

The first reciprocal block is special and unavoidable in any termwise treatment: since

\[
F_\chi(1)=1,
\]

the `m=1` contribution is exactly

\[
\boxed{
K_\chi(X)-K_\chi(\lfloor X/2\rfloor).
}
\tag{3}
\]

This apparently local dyadic-annulus quantity is already globally zero-sensitive. For every fixed `alpha>0`, if

\[
\boxed{
K_\chi(x)-K_\chi(\lfloor x/2\rfloor)=O(x^\alpha)
}
\tag{4}
\]

for all sufficiently large integers `x`, then

\[
\boxed{K_\chi(x)=O(x^\alpha).}
\tag{5}
\]

Indeed, dyadic telescoping reconstructs the full partial sum from these annular increments. Therefore, for every fixed

\[
\frac12\le\alpha<1,
\]

the block estimate `(4)` forces, by `MC-071`,

\[
\boxed{
\zeta(s)\ne0
\quad\text{and}\quad
L(s,\chi)\ne0
\qquad(\operatorname{Re}s>\alpha).
}
\tag{6}
\]

In particular, if for every `epsilon>0`

\[
K_\chi(x)-K_\chi(\lfloor x/2\rfloor)
=O_\varepsilon(x^{1/2+\varepsilon}),
\tag{7}
\]

then RH holds for `zeta` and GRH holds for this primitive quadratic Dirichlet `L`-function.

Thus the obvious attempt to make `(1)` more local by reciprocal-block decomposition does **not** create a cheap independent estimate for the inverse kernel. At the critical power scale, controlling even the first dyadic inverse annulus as a standalone term already imports the same two zero-free problems as controlling the full inverse partial sum.

This does **not** rule out the coupled identity `(2)`. The surviving possibility is cancellation **between reciprocal blocks**, or an equivalent argument that controls the complete weighted sum without first assigning an RH-scale bound to the `m=1` inverse annulus itself.

No improved bound for `M(X)` is claimed.

## 1. Exact reciprocal-block decomposition

For an integer `X>=1`, the condition

\[
\left\lfloor\frac Xd\right\rfloor=m
\]

is equivalent to

\[
\frac X{m+1}<d\le\frac Xm.
\]

Since `F_chi(X/d)` is a summatory step function,

\[
F_\chi(X/d)=F_\chi(m)
\]

throughout that block. Hence

\[
\begin{aligned}
M(X)
&=\sum_{m=1}^{X}F_\chi(m)
\sum_{X/(m+1)<d\le X/m} k_\chi(d)\\
&=\sum_{m=1}^{X}F_\chi(m)
\left(
K_\chi\!\left(\left\lfloor\frac Xm\right\rfloor\right)
-
K_\chi\!\left(\left\lfloor\frac X{m+1}\right\rfloor\right)
\right),
\end{aligned}
\]

which is `(2)`.

For `m=1`, the interval is `(X/2,X]`. Because `f_chi(1)=1`, one has `F_chi(1)=1`, so its coefficient cannot be made small by choosing the character. This proves `(3)`.

The identity is just exact divisor switching inside the finite Dirichlet convolution. No analytic continuation, asymptotic estimate, or zero-free hypothesis is used.

## 2. A dyadic inverse-annulus bound reconstructs the full inverse partial sum

Assume `(4)`. Let

\[
x_j=\left\lfloor\frac{x}{2^j}\right\rfloor.
\]

Choose `J` so that `x_J` lies below the fixed threshold from which `(4)` is valid. Since

\[
\left\lfloor\frac{x_j}{2}\right\rfloor=x_{j+1},
\]

one has the exact telescoping identity

\[
K_\chi(x)
=
K_\chi(x_J)
+
\sum_{j=0}^{J-1}
\bigl(K_\chi(x_j)-K_\chi(x_{j+1})\bigr).
\tag{8}
\]

The terminal term is bounded because only finitely many arguments occur below the threshold. For the remaining terms,

\[
|K_\chi(x_j)-K_\chi(x_{j+1})|
\ll x_j^\alpha
\le x^\alpha 2^{-j\alpha}.
\]

Since `alpha>0`, the geometric series converges, giving

\[
|K_\chi(x)|
\ll
1+x^\alpha\sum_{j\ge0}2^{-j\alpha}
\ll_\alpha x^\alpha,
\]

which proves `(5)`.

The same argument works for any fixed ratio `lambda in (0,1)`: a uniform power bound for `K_chi(x)-K_chi(floor(lambda x))` reconstructs the corresponding global power bound. The dyadic case is singled out because it occurs exactly as the first reciprocal block of `(2)`.

## 3. The zero-free implication is inherited intact

`MC-071` proves that, in `Re(s)>1`,

\[
\sum_{n\ge1}\frac{k_\chi(n)}{n^s}
=
\frac{L(2s,\chi^2)}{\zeta(s)L(s,\chi)},
\tag{9}
\]

and for prime quadratic `chi`,

\[
L(2s,\chi^2)=\zeta(2s)(1-q^{-2s})
\tag{10}
\]

is holomorphic and zero-free in the open half-plane `Re(s)>1/2`.

A power bound `(5)` with `alpha>=1/2` makes the Dirichlet series of `k_chi` holomorphic in `Re(s)>alpha` by partial summation. Because the numerator in `(9)` does not vanish there, neither denominator factor can have a zero in that half-plane. Combining this established `MC-071` implication with the elementary telescoping lemma yields `(6)` and `(7)`.

The localization in `(3)` therefore does not weaken the analytic burden. The annulus `(x/2,x]` is local in multiplicative scale, but uniform control of its signed inverse mass across all scales reconstructs the entire zero-sensitive inverse sequence.

## 4. Why termwise reciprocal localization does not solve the coupling problem

Equation `(2)` is attractive because it replaces the long inverse sum by increments of `K_chi` over reciprocal intervals. But the first coefficient is exactly one, so a triangle-inequality estimate begins with

\[
|M(X)|
\le
|K_\chi(X)-K_\chi(\lfloor X/2\rfloor)|
+
\sum_{m=2}^{X}|F_\chi(m)|\,|\Delta_mK_\chi(X)|,
\tag{11}
\]

where

\[
\Delta_mK_\chi(X)
=
K_\chi\!\left(\left\lfloor\frac Xm\right\rfloor\right)
-
K_\chi\!\left(\left\lfloor\frac X{m+1}\right\rfloor\right).
\]

At an RH-scale target, independently bounding the first term in `(11)` by `O_epsilon(X^(1/2+epsilon))` for all `X` already proves RH plus the corresponding quadratic GRH. Therefore a blockwise absolute strategy cannot claim that it has reduced the hard global inverse estimate merely because each block is shorter.

The obstruction is narrower than a no-go for `(2)`. The original signed convolution may contain cancellations among different `m`, and the factors `F_chi(m)` are arithmetically linked to the same character that defines `k_chi`. A proof that exploits those dependencies before taking absolute values need not provide `(7)` as an intermediate theorem.

This identifies the exact residual obligation: a genuinely cheaper signed-feedback argument must control a **coupled reciprocal-block functional**, not a family of independently bounded inverse annuli whose first member already has full zero-free strength.

## 5. Prior art and novelty boundary

No standalone novelty is claimed for grouping a divisor convolution by values of `floor(X/d)`, for dyadic decomposition, or for the fact that uniformly bounded multiplicative-scale increments telescope to a global bound. These are elementary/classical analytic-number-theory mechanisms.

The zero-sensitive ingredient is also not new: `MC-071` already identifies the inverse Dirichlet series as `L(2s,chi^2)/(zeta(s)L(s,chi))`, and `MC-S17` supplies adjacent literature for the broader principle that analytic continuation/nonvanishing properties of auxiliary multiplicative Dirichlet series constrain zeta zeros.

The durable line-specific contribution is the **placement of that known burden inside the exact reciprocal-block decomposition of the current signed-feedback architecture**. `MC-071` ruled out a black-box global estimate for the inverse partial sums; the present finding shows that the most immediate localization escape also fails if it estimates the first inverse annulus independently at the critical power. The remaining route must preserve cross-block coupling rather than merely shortening the inverse sum.

## 6. Boundaries and falsification tests

The conclusion is deliberately specific.

- It does not say that every proof using `(2)` must establish `(4)`. Cross-block cancellation may control the total without controlling the first block separately at the target exponent.
- It does not rule out estimates for a sparse set of scales. The telescoping implication requires a uniform all-large-scale bound, or another scale set dense enough multiplicatively to reconstruct `K_chi` with comparable power control.
- It does not rule out a block estimate weaker than the target exponent that is useful only after cancellation with other terms.
- The first-block coefficient is exactly one only because `F_chi(1)=1`; this is intrinsic to the present convolution and is independent of conductor choice.
- The implication from `(4)` to `(5)` requires `alpha>0`. The critical applications here have `alpha>=1/2`, so the geometric summability is automatic.
- The zero-free conclusion is for a fixed quadratic character, exactly as in `MC-071`. A conductor moving with `X` does not define one fixed inverse Dirichlet series to which the same global continuation argument can be applied without additional uniformity.

The exact claim is falsified if the reciprocal grouping `(2)` is incorrect, if the `m=1` coefficient is not one, if the floor-compatible dyadic telescoping `(8)` fails, or if `(4)` can hold uniformly while `(5)` fails. The zero-free consequence is then independently checked against the quotient and numerator nonvanishing already established in `MC-071`.

## Consequence for the active frontier

The signed quadratic-comparator branch has progressively removed simpler escapes. `MC-070` closes the positive-kernel triangle route over the relevant conductor ranges, and `MC-071` shows that standalone square-root cancellation of the signed inverse already contains both zeta and quadratic-Dirichlet zero information.

The present result closes the next natural localization move: **the first reciprocal inverse annulus is itself zero-hard when controlled uniformly at the critical power**. A surviving signed route must therefore exploit cancellation across the weighted reciprocal blocks in `(2)`, exploit an equivalent nonlocal coupling before any annulus is bounded separately, or introduce genuinely new arithmetic information. Merely partitioning the inverse into shorter multiplicative intervals does not reduce the information burden.