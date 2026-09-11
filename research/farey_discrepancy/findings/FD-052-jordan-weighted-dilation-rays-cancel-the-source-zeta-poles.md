# FD-052 — Jordan-weighted dilation rays cancel the source zeta poles

**Status:** `EXACT-DERIVED + PHYSICAL-SOURCE-PLACEMENT + JORDAN-WEIGHTED-DILATION + ZETA-POLE-CANCELLATION + SQUAREFREE-PRESERVING-RAY + HALF-POWER-SIGNED-CEILING + FALSE-RH-SELF-CANCELLATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-037`, `FD-048`, and the current research-line frontier isolate the remaining joint-occupation problem at the physical low-row end. Generic shell smoothness is insufficient: the missing input must use the exact multiplicative placement law of the physical increments

\[
\Delta\mathcal H(n)
=
\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\]

or an equivalent divisibility coupling. There is a natural such coupling hidden directly in the Jordan weights. It is exact, but its first consequence is a warning rather than the desired coercive theorem.

Let

\[
w(n):=\frac{J_2(n)}{n^2}
=\prod_{p\mid n}(1-p^{-2}),
\qquad
\mathcal H(X)=\sum_{n\le X}c(n),
\]

with

\[
\sum_{n\ge1}\frac{c(n)}{n^s}
=\frac{\zeta(s+1)}{\zeta(s)}.
\]

For every fixed integer `q>=1`, define the signed Jordan-weighted dilation ray

\[
\mathscr R_q(X)
:=
\sum_{m\le X}
 w(qm)\,
 \mathcal H\!\left(\left\lfloor\frac Xm\right\rfloor\right).
\tag{1}
\]

Then the full zeta-zero denominator of the physical source cancels exactly against the Jordan-row dilation series. In fact

\[
\boxed{
\mathscr R_q(X)
=
\frac1{\zeta(2)}\log X+C_q+o_q(1).
}
\tag{2}
\]

The logarithmic coefficient is independent of `q`.

If `q` is squarefree, split this ray according to whether the physical output row `qm` stays squarefree:

\[
\mathscr R_q^{\rm sf}(X)
:=
\sum_{\substack{m\le X\\\mu(qm)\ne0}}
 w(qm)\,
 \mathcal H\!\left(\left\lfloor\frac Xm\right\rfloor\right),
\tag{3}
\]

\[
\mathscr R_q^{\rm ns}(X)
:=
\mathscr R_q(X)-\mathscr R_q^{\rm sf}(X).
\tag{4}
\]

For every fixed `epsilon>0`,

\[
\boxed{
\mathscr R_q^{\rm sf}(X)
=O_{q,\epsilon}(X^{1/2+\epsilon}),
\qquad
\mathscr R_q^{\rm ns}(X)
=O_{q,\epsilon}(X^{1/2+\epsilon}).
}
\tag{5}
\]

These are **signed first-moment** statements, not energy bounds. Their relevance is clearest if RH is false. Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

`FD-046` proves that the pointwise source has power frontier `Theta`. Hence if `Theta>1/2`, for every fixed squarefree `q` and every sufficiently small fixed `delta>0`, there are arbitrarily large `X` with

\[
|\mathcal H(X)|\ge X^{\Theta-\delta}
\]

and along such a subsequence

\[
\boxed{
\sum_{\substack{2\le m\le X\\\mu(qm)\ne0}}
 w(qm)\,
 \mathcal H\!\left(\left\lfloor\frac Xm\right\rfloor\right)
=
-w(q)\mathcal H(X)
+o(|\mathcal H(X)|).
}
\tag{6}
\]

At the same horizons,

\[
\boxed{
\mathscr R_q^{\rm ns}(X)=o(|\mathcal H(X)|).
}
\tag{7}
\]

Thus an off-critical `Theta`-scale spike on one fixed squarefree Jordan row has an exact multiplicative escape channel: at the level of the canonical Jordan-weighted signed dilation statistic, its leading cancellation occurs **entirely among other squarefree rows**. The nonsquarefree branch need not carry a comparable signed response.

This does not construct a vanishing sequence for `U_(H,D)/E_(H,D)`. Positive quadratic energy can be large even when a signed first moment cancels. What it does rule out is a tempting version of the remaining program: merely discovering the exact divisibility first moment and observing that a large low-row value must be balanced somewhere does not force the balance into the nonsquarefree coordinates. The Jordan weights themselves cancel the source `1/zeta(s)` pole structure before the quadratic occupation question is reached.

## 1. Floor transforms convert a row-ray sum into Dirichlet convolution

For arithmetic coefficients `a(n)` and a summatory function

\[
F(X)=\sum_{n\le X}f(n),
\]

one has the finite identity

\[
\sum_{m\le X}a(m)F(\lfloor X/m\rfloor)
=
\sum_{n\le X}(a*f)(n).
\tag{8}
\]

Indeed, both sides equal

\[
\sum_{mn\le X}a(m)f(n).
\]

For the physical shell source, `f=c` and

\[
C(s):=
\sum_{n\ge1}\frac{c(n)}{n^s}
=
\frac{\zeta(s+1)}{\zeta(s)}
\qquad(\Re s>1).
\tag{9}
\]

Fix `q` and set

\[
a_q(m):=w(qm).
\]

The local Euler factor of `w` is

\[
1+(1-p^{-2})\frac{p^{-s}}{1-p^{-s}}
=
\frac{1-p^{-(s+2)}}{1-p^{-s}},
\]

so

\[
\sum_{m\ge1}\frac{w(m)}{m^s}
=
\frac{\zeta(s)}{\zeta(s+2)}.
\tag{10}
\]

If `p|q`, the prime `p` is already present in `w(qm)` even when the `p`-adic exponent of `m` is zero. Correcting those finitely many local factors gives

\[
\boxed{
A_q(s)
:=
\sum_{m\ge1}\frac{w(qm)}{m^s}
=
w(q)
\frac{\zeta(s)}{\zeta(s+2)}
\prod_{p\mid q}
(1-p^{-(s+2)})^{-1}.
}
\tag{11}
\]

Multiplying (11) by the physical source series (9) cancels `zeta(s)` exactly:

\[
\boxed{
A_q(s)C(s)
=
w(q)
\frac{\zeta(s+1)}{\zeta(s+2)}
\prod_{p\mid q}
(1-p^{-(s+2)})^{-1}.
}
\tag{12}
\]

No nontrivial zero of `zeta(s)` remains in this row-ray transform.

## 2. The complete weighted ray is an explicit positive totient transform

The classical totient Dirichlet series gives

\[
\sum_{n\ge1}
\frac{\varphi(n)/n^2}{n^s}
=
\frac{\zeta(s+1)}{\zeta(s+2)}.
\tag{13}
\]

For the finite prime set dividing `q`, let `\mathcal P(q)` denote the multiplicative semigroup generated by those primes. Since

\[
\prod_{p\mid q}(1-p^{-(s+2)})^{-1}
=
\sum_{e\in\mathcal P(q)}\frac{e^{-2}}{e^s},
\tag{14}
\]

(8) and (12)--(14) give the exact coefficient identity

\[
\boxed{
\mathscr R_q(X)
=
w(q)
\sum_{\substack{e\in\mathcal P(q)\\e\le X}}
\frac1{e^2}
\sum_{n\le X/e}
\frac{\varphi(n)}{n^2}.
}
\tag{15}
\]

In particular the right side is positive, despite the oscillatory signs inside `mathcal H`.

An elementary Möbius expansion of `phi(n)/n` gives

\[
\sum_{n\le Y}\frac{\varphi(n)}{n^2}
=
\frac1{\zeta(2)}\log Y+C_\varphi+o(1).
\tag{16}
\]

For completeness,

\[
\frac{\varphi(n)}n
=
\sum_{d\mid n}\frac{\mu(d)}d,
\]

so the left side of (16) equals

\[
\sum_{d\le Y}\frac{\mu(d)}{d^2}
H_{\lfloor Y/d\rfloor},
\]

and `H_m=log m+gamma+O(1/m)` together with absolute convergence of `sum d^(-2)` gives (16) directly.

Now

\[
w(q)
\sum_{e\in\mathcal P(q)}e^{-2}
=
w(q)
\prod_{p\mid q}(1-p^{-2})^{-1}
=1,
\tag{17}
\]

while the corresponding logarithmic moment in `e` converges. Substituting (16) into (15) proves (2). The universal coefficient `1/zeta(2)` is therefore not an asymptotic coincidence: the `q`-local correction cancels exactly against `w(q)`.

A useful special case is `q=1`:

\[
\boxed{
\sum_{m\le X}
 w(m)\mathcal H(\lfloor X/m\rfloor)
=
\sum_{n\le X}\frac{\varphi(n)}{n^2}.
}
\tag{18}
\]

This is the simplest exact multiplicative-placement identity for the physical Jordan-row vector found in this route.

## 3. Squarefree-preserving output cancels the source denominator separately

Now assume `q` is squarefree. The output row `qm` is squarefree exactly when

\[
\mu(m)^2=1,
\qquad
(m,q)=1.
\tag{19}
\]

On this support `w(qm)=w(q)w(m)`. Hence the coefficient series of the squarefree-preserving ray is

\[
A_q^{\rm sf}(s)
=
w(q)
\prod_{p\nmid q}
\left(1+(1-p^{-2})p^{-s}\right).
\tag{20}
\]

`FD-044` already isolates the absolutely convergent factor

\[
A(s)
:=
\prod_p
(1-p^{-s})
\left(1+(1-p^{-2})p^{-s}\right),
\tag{21}
\]

which is analytic and represented by an absolutely convergent Dirichlet series throughout every half-plane `Re(s)>1/2`. Therefore

\[
\boxed{
A_q^{\rm sf}(s)
=
w(q)\zeta(s)A(s)
\prod_{p\mid q}
\left(1+(1-p^{-2})p^{-s}\right)^{-1}.
}
\tag{22}
\]

Multiplication by the physical source series (9) cancels the same `zeta(s)` denominator once again:

\[
\boxed{
A_q^{\rm sf}(s)C(s)
=
\zeta(s+1)B_q(s),
}
\tag{23}
\]

where

\[
B_q(s)
:=
w(q)A(s)
\prod_{p\mid q}
\left(1+(1-p^{-2})p^{-s}\right)^{-1}.
\tag{24}
\]

For every fixed `sigma>1/2`, `B_q(s)` has an absolutely convergent Dirichlet series

\[
B_q(s)=\sum_{d\ge1}\frac{b_q(d)}{d^s},
\qquad
\sum_{d\ge1}\frac{|b_q(d)|}{d^\sigma}<\infty.
\tag{25}
\]

The finite local inverse factors are harmless because for `Re(s)>0` their geometric expansions converge absolutely.

Since `zeta(s+1)` is the Dirichlet series of `n -> 1/n`, (23)--(25) turn the squarefree-preserving ray into

\[
\boxed{
\mathscr R_q^{\rm sf}(X)
=
\sum_{d\le X}
 b_q(d)H_{\lfloor X/d\rfloor}.
}
\tag{26}
\]

For fixed `sigma>1/2`,

\[
\begin{aligned}
|\mathscr R_q^{\rm sf}(X)|
&\le
(1+\log X)
\sum_{d\le X}|b_q(d)|\\
&\le
(1+\log X)X^\sigma
\sum_{d\ge1}\frac{|b_q(d)|}{d^\sigma}.
\end{aligned}
\tag{27}
\]

Given `epsilon>0`, take `sigma=1/2+epsilon/2` and absorb the logarithm into `X^(epsilon/2)`. This proves the first estimate in (5). Equation (2) then gives the same bound for the complementary nonsquarefree-output ray (4).

The half-power in (5) is a convergence boundary for this argument, not a claim of a sharp asymptotic. `FD-045` contains stronger Walfisz-type squarefree cancellation for a related centered Jordan kernel. No such strengthening is required for the present route restriction.

## 4. False RH forces a squarefree-only cancellation cascade

The previous estimates become structurally informative when compared with the pointwise source frontier. `FD-046` proves

\[
\limsup_{X\to\infty}
\frac{\log(1+|\mathcal H(X)|)}{\log X}
=\Theta.
\tag{28}
\]

Assume `Theta>1/2`. Fix a squarefree integer `q` and choose

\[
0<\delta<\frac{\Theta-1/2}{4}.
\tag{29}
\]

By (28), there are arbitrarily large `X` such that

\[
|\mathcal H(X)|\ge X^{\Theta-\delta}.
\tag{30}
\]

Use (5) with exponent `1/2+delta`. Since

\[
\Theta-\delta>\frac12+\delta,
\]

one has

\[
\mathscr R_q^{\rm sf}(X)
=o(|\mathcal H(X)|)
\tag{31}
\]

along this subsequence. But the `m=1` term of (3) is exactly

\[
w(q)\mathcal H(X).
\]

Removing that term from (31) gives (6). At the same time the second estimate in (5) gives (7).

Now take `q>D` squarefree and put the physical horizon

\[
H=qX.
\tag{32}
\]

The row `q` samples exactly `mathcal H(X)`, while its squarefree-preserving dilation descendants are precisely the rows `qm` appearing in (6). Thus an off-critical large value on one fixed squarefree low row is not forced, at signed first-moment level, to spill into the nonsquarefree row union. The exact Jordan/divisibility algebra instead forces an almost equal opposite contribution from other squarefree rows.

This is a genuine source-specific statement: the cancellation is not available to an arbitrary one-Lipschitz control such as `FD-039` or `FD-048` unless that control is additionally engineered to satisfy the exact convolution (9), the Jordan Euler factors, and the squarefree-support transform (22).

## 5. What this says — and does not say — about joint occupation

The accepted occupation clue asks for a lower bound on the positive quadratic quantity

\[
U_{H,D}
=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
 w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\tag{33}
\]

Equations (2)--(7) concern instead signed first moments. Therefore they do **not** imply that `U_(H,D)` is small, nor do they construct a physical-compatible sequence with `U/E -> 0`. Large nonsquarefree values can cancel one another in (7) while contributing strongly to (33).

The durable restriction is more precise. The current research line asks whether exact multiplicative placement can remove the subpower, zero-log-density exceptional horizons left by `FD-049`--`FD-051`. A first attempt might sum the physical row values over divisor/dilation rays and hope that a large squarefree low-row spike must create comparable signed mass in nonsquarefree descendants. Equations (5)--(7) show that this is false at the canonical Jordan weight: the source pole `1/zeta(s)` cancels already in the linear ray transform, and under false RH the leading spike is balanced inside the squarefree-preserving branch itself.

Consequently a successful use of the exact placement law must retain information beyond this signed first moment. Plausible surviving carriers include a genuinely quadratic divisibility identity, a bilinear correlation between distinct dilation rays, sign-restricted information that prevents the squarefree self-cancellation in (6), or a positive lower frame bound that uses the coefficients `c(n)` before the row values are summed.

This complements `FD-048`. That finding says aggregate short-interval cancellation of the increments is too weak. The present finding says that even an **exact** source-specific multiplicative first moment has a built-in squarefree cancellation channel. The remaining theorem must therefore exploit exact placement and positivity/quadratic structure simultaneously, rather than adding more linear consistency identities.

## 6. Prior-art and falsification boundary

The ingredients of the derivation are classical. The Dirichlet series

\[
\sum \mu(n)^2n^{-s}=\frac{\zeta(s)}{\zeta(2s)},
\qquad
\sum \varphi(n)n^{-s}=\frac{\zeta(s-1)}{\zeta(s)},
\]

and the Euler product for the Jordan totient are standard; the targeted literature search found these expected identities but no result formulated as the present physical Farey/Mertens Jordan-ray split. No novelty is claimed for those Euler products or for Dirichlet-convolution algebra in isolation. The Mathia-specific content is their combination with the exact physical source `zeta(s+1)/zeta(s)` and the same row weights that define `E_(H,D)` and `U_(H,D)`, yielding (2), (5), and the false-RH squarefree cancellation consequence (6)--(7).

No new external theorem is load-bearing. `FD-044` already established the absolute convergence of the factor `A(s)` in `Re(s)>1/2`, and `FD-046` already anchors the source frontier `Theta` through Titchmarsh. `SOURCES.md` therefore requires no expansion.

The main algebraic falsification checks are local. Equation (11) must use `w(qm)`, not `w(q)w(m)`, because common prime factors occur only once in the Jordan product; the finite correction factors in (11) are exactly what repair that overlap. The factorization `w(qm)=w(q)w(m)` is used only in the squarefree-preserving branch, where `(m,q)=1`. Equation (15) was also checked directly against the finite floor sum for several composite and nonsquarefree values of `q`; the two sides agree term-for-term through the convolution identity rather than only asymptotically.

The conceptual falsification boundary is equally important. This finding must not be cited as a positive or negative resolution of `U/E>=c_D`, as a construction of a physical occupation escape, or as a new zeta zero-free estimate. It identifies an exact low-row multiplicative carrier and proves that its linear information cancels the zeta-zero pole structure too early to force nonsquarefree quadratic occupation by itself.
