# FD-312 — Pointwise Mertens envelopes cannot close sliding variance below the source ceiling

- **Date:** 2026-09-27
- **Status:** proved a structural no-go for closing the FD-311 sliding-variance route using only global pointwise Mertens envelopes
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens source / sliding short intervals / pointwise envelope barrier / RH shell floor / balanced depth / route pruning
- **Depends on:** FD-300, FD-303, FD-304, FD-311
- **Classification:** `EXACT-DERIVED + POINTWISE-NO-GO + RH-SHELL-FLOOR + BALANCED-DEPTH-QUANTIFICATION + ROUTE-PRUNING`

## Claim

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots
\tag{1}
\]

and retain the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
x=N^{\lambda+o(1)}.
\tag{2}
\]

As in FD-300/303, let `Q<q<=2Q` be a carrying dyadic shell, put

\[
Q=x^{\rho+o(1)},
\qquad
X:=NQ,
\tag{3}
\]

and define

\[
J_\mu(X,N)
:=
\sum_{X\le y<2X}
|M(y+N)-M(y)|^2.
\tag{4}
\]

FD-303 gives

\[
\boxed{
J_\mu(X,N)
\ge
X N^{1/2+3c\lambda-o(1)}.
}
\tag{5}
\]

Suppose one tries to close this route using only a global pointwise Mertens envelope

\[
M(t)\ll t^{\kappa+o(1)}.
\tag{6}
\]

Then, uniformly for `y~X`,

\[
|M(y+N)-M(y)|
\le |M(y+N)|+|M(y)|
\ll X^{\kappa+o(1)},
\tag{7}
\]

hence

\[
\boxed{
J_\mu(X,N)
\ll
X^{1+2\kappa+o(1)}.
}
\tag{8}
\]

Comparing (5) and (8), such a pointwise strategy can contradict near-capacity only if

\[
\boxed{
\kappa
<
\kappa_{\rm pt}(\lambda,\rho)
:=
\frac{\frac14+\frac{3c}{2}\lambda}
{1+\lambda\rho}.
}
\tag{9}
\]

Under RH, FD-304 forces every carrying shell to satisfy

\[
\rho\ge 2c.
\tag{10}
\]

Inside the entire strict source-live region of FD-300,

\[
\lambda<\frac1{2c}
=
1.2047104198\ldots,
\tag{11}
\]

we then have

\[
\boxed{
\kappa_{\rm pt}(\lambda,\rho)
\le
\kappa_{\rm pt}(\lambda,2c)
<
\frac12.
}
\tag{12}
\]

Moreover,

\[
\boxed{
\frac12-
\kappa_{\rm pt}(\lambda,2c)
=
\frac{1-2c\lambda}
{4(1+2c\lambda)}.
}
\tag{13}
\]

Equality with `1/2` occurs only at the source ceiling

\[
\lambda=\frac1{2c},
\qquad
\rho=2c,
\tag{14}
\]

where FD-300 already makes the near-capacity premise impossible.

Therefore:

> **Below the FD-300 source ceiling, no argument that first bounds the two Mertens endpoints separately by a global pointwise envelope can close the FD-311 sliding-variance route.**

The required exponent is strictly below `1/2`, while a global bound `M(x)=O(x^{\kappa+o(1)})` with `\kappa<1/2` is incompatible with the known existence of zeta zeros on the critical line.

## Proof of the pointwise threshold

From (6),

\[
M(y)=O(X^{\kappa+o(1)})
\qquad
(X\le y\le 2X+N).
\tag{15}
\]

Hence

\[
|M(y+N)-M(y)|^2
\ll
X^{2\kappa+o(1)}.
\tag{16}
\]

There are `X+O(1)` summands in (4), so

\[
J_\mu(X,N)
\ll
X^{1+2\kappa+o(1)}.
\tag{17}
\]

Since

\[
X=NQ
=
N^{1+\lambda\rho+o(1)},
\tag{18}
\]

the upper bound exponent in `N` is

\[
(1+2\kappa)(1+\lambda\rho).
\tag{19}
\]

The FD-303 lower bound (5) has exponent

\[
1+\lambda\rho
+
\frac12
+
3c\lambda.
\tag{20}
\]

For the upper bound to be strictly smaller, we need

\[
(1+2\kappa)(1+\lambda\rho)
<
1+\lambda\rho
+
\frac12
+
3c\lambda,
\tag{21}
\]

equivalently

\[
2\kappa(1+\lambda\rho)
<
\frac12+3c\lambda,
\tag{22}
\]

which is exactly (9).

For fixed `lambda`, the function `kappa_pt(lambda,rho)` decreases with `rho`. Under RH, FD-304 gives `rho>=2c`, so the most favorable shell for a pointwise strategy is `rho=2c`. Substituting gives

\[
\kappa_{\rm pt}(\lambda,2c)
=
\frac{1+6c\lambda}
{4(1+2c\lambda)}.
\tag{23}
\]

Subtracting from `1/2` yields

\[
\frac12-
\kappa_{\rm pt}(\lambda,2c)
=
\frac{
2(1+2c\lambda)-(1+6c\lambda)
}{
4(1+2c\lambda)
}
=
\frac{1-2c\lambda}
{4(1+2c\lambda)},
\tag{24}
\]

which is positive exactly when `lambda<1/(2c)`.

## Balanced depth

Set

\[
\lambda=1.
\tag{25}
\]

Then

\[
\kappa_{\rm pt}(1,\rho)
=
\frac{
\frac14+\frac{3c}{2}
}{
1+\rho
}
=
\frac{
0.8725562489\ldots
}{
1+\rho
}.
\tag{26}
\]

At the shallowest RH-compatible shell,

\[
\rho=2c,
\tag{27}
\]

we obtain

\[
\boxed{
\kappa_{\rm pt}(1,2c)
=
0.4767871533\ldots.
}
\tag{28}
\]

At the deepest shell,

\[
\rho=1,
\tag{29}
\]

we obtain

\[
\boxed{
\kappa_{\rm pt}(1,1)
=
0.4362781245\ldots.
}
\tag{30}
\]

Thus even the most favorable shell would require improving the critical-line exponent `1/2` by the fixed power

\[
\boxed{
0.5-0.4767871533\ldots
=
0.0232128467\ldots.
}
\tag{31}
\]

No logarithmic improvement of a pointwise `x^{1/2+o(1)}` envelope can cross this gap.

## Same obstruction in the FD-311 variance-saving language

FD-311 asks for a theorem on the same source-selected window of the form

\[
J_\mu(X,N)
\le
X N^{2-\eta+o(1)}.
\tag{32}
\]

It showed that near-capacity is impossible whenever

\[
\eta>
\eta_{\rm var}(\lambda)
:=
\frac32-3c\lambda.
\tag{33}
\]

At balanced depth,

\[
\eta_{\rm var}(1)
=
\frac32-3c
=
0.2548875021\ldots.
\tag{34}
\]

Now use only the RH pointwise envelope

\[
M(t)=t^{1/2+o(1)}.
\tag{35}
\]

Then

\[
|M(y+N)-M(y)|
\le
X^{1/2+o(1)},
\tag{36}
\]

so

\[
J_\mu(X,N)
\le
X^{2+o(1)}.
\tag{37}
\]

Since `X=N^{1+rho+o(1)}` at `lambda=1`, rewriting (37) as `XN^{2-eta}` gives an effective endpoint saving

\[
\eta_{\rm ep}(\rho)
=
1-\rho.
\tag{38}
\]

The best RH-compatible value occurs at `rho=2c`:

\[
\boxed{
\eta_{\rm ep}^{\max}
=
1-2c
=
0.1699250014\ldots.
}
\tag{39}
\]

The remaining deficit is

\[
\boxed{
\eta_{\rm var}(1)
-
\eta_{\rm ep}^{\max}
=
\frac12-c
=
0.0849625007\ldots.
}
\tag{40}
\]

This is a fixed power gap. Therefore a pointwise RH envelope plus arbitrary logarithmic refinements cannot deliver the FD-311 target.

## Why a global exponent below 1/2 is unavailable

The obstruction is structural, not merely a gap in current technology.

If

\[
M(x)=O(x^{\kappa+o(1)})
\qquad
\text{for some }\kappa<\frac12,
\tag{41}
\]

then partial summation of

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}
=
\frac1{\zeta(s)}
\tag{42}
\]

would continue `1/zeta(s)` analytically into a half-plane crossing `Re(s)=1/2`. This is incompatible with the known existence of nontrivial zeros of `zeta(s)` on the critical line.

Hence the exponent demanded by (12) cannot arise from a global pointwise Mertens theorem.

## Prior-art boundary

The relevant short-interval literature does not alter this no-go.

Results of Matomäki–Radziwiłł type can provide strong control for almost all short intervals and can make exceptional sets small, but converting such statements into the complete sliding second moment (4) still requires controlling the contribution of the exceptional set. If the exceptional intervals are only bounded trivially by `N`, a small exceptional density need not yield the fixed-power second-moment saving required by FD-311.

Likewise, a reported RH result attributed to Peng Gao of the form

\[
\int_1^X
(M(x+h)-M(x))^2\,dx
=
o(Xh^2)
\tag{43}
\]

for sufficiently large `h` is qualitatively a subtrivial improvement, but without a fixed-power rate it does not cross (33). It should therefore not be read as supplying `J_mu\ll Xh\,\mathrm{polylog}`.

No new external theorem is load-bearing in the present finding; the conclusion follows from the already-established FD-303/304 shell geometry plus the classical critical-line obstruction already anchored in the research sources.

## Research consequence

The FD-311 route can only progress through information that is genuinely unavailable to separate endpoint bounds. Viable mechanisms include:

1. direct cancellation in
   \[
   M(y+N)-M(y),
   \]
   not separate bounds for the two terms;

2. a true mean-square theorem over the start variable `y`;

3. a correlation estimate for the underlying Möbius blocks;

4. additional Farey-specific structure of the source-selected shell/window that lowers the required variance target.

If the remaining task reduces only to proving a new generic theorem about short differences of Möbius on arbitrary dyadic windows, ownership should migrate toward `mobius_cancellation`. For `farey_discrepancy` to contribute additional leverage, it should extract further geometry from the source-selected shell.

## Adversarial audit

- The comparison uses the **same** source-selected dyadic window `[X,2X)` as FD-303.
- The threshold in (9) is strict; equality only gives exponent tangency.
- The RH shell floor `rho>=2c` is used only when turning the general threshold into the no-go (12).
- The global `kappa<1/2` impossibility is stronger than saying current pointwise methods are insufficient.
- No claim is made that a short-interval mean-square theorem with power saving is impossible.
- No claim is made that an exceptional-set theorem automatically yields the complete second moment needed here.
- The result prunes only the route “bound both Mertens endpoints separately”.
