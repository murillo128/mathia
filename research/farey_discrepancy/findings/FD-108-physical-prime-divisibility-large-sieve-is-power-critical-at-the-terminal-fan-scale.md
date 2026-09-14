# FD-108 — physical prime-divisibility large sieve is power-critical at the terminal fan scale

**Status:** `EXACT-DERIVED + PHYSICAL-COEFFICIENT-LAW + PRIME-DIVISIBILITY-PROJECTION + ADDITIVE-LARGE-SIEVE + RECIPROCAL-PRIME-SAMPLE-L2 + TERMINAL-FAN-SCALE-AUDIT + NEGATIVE/OBSTRUCTION + FALSE-RH-COMPOSITION-FRONTIER`.

`FD-107` shows that common shell coherence, one-Lipschitz regularity, sublinear growth, polynomial high mass, and the exact least-prime-factor terminal partition still permit the harmonic endpoint of `FD-106`. The synthetic countermodel deliberately omits the physical increment law

\[
a(n):=\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\tag{1}
\]

The first natural way to use (1) is to test the reciprocal prime samples `mathcal H(floor(X/p))` through the divisibility projections of the coefficient sequence. This produces a genuine source-specific restriction. For every `X>=1` and `P>=3`,

\[
\boxed{
\sum_{3\le p\le P}p
\left|
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)
+\frac{\mathcal H(X)}{p-1}
\right|^2
\ll X(X+P^2).
}
\tag{2}
\]

The sum is over primes. The implied constant is absolute. Equation (2) is obtained from the exact prime-power covariance forced by (1) and the classical additive large sieve; it is not available for the arbitrary one-Lipschitz source used in `FD-107`.

However, (2) is still **power-critical at exactly the source-rich terminal scale**. On a sharp false-RH state `H=4X` with

\[
U_H=H^{2\Theta+o(1)},
\qquad \frac12<\Theta<1,
\tag{3}
\]

the adaptive source cutoff of `FD-105` permits terminal least-prime labels only up to

\[
P_*(X)
\ll \frac{X^2\log X}{U_H}
=X^{2-2\Theta+o(1)}.
\tag{4}
\]

A harmonic endpoint profile on the prime rows,

\[
w(4p)\,
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)^2
\asymp
\frac{U_H}{S(P_*)p},
\qquad
S(P):=\sum_{3\le p\le P}\frac1p,
\tag{5}
\]

has reciprocal-sample large-sieve cost, by the prime number theorem,

\[
\ll
\frac{U_H P_*}{S(P_*)\log P_*}
\ll_\Theta
\frac{X^2}{S(P_*)}
=o(X^2).
\tag{6}
\]

The deterministic centering term in (2) is also `o(X^2)`. Thus this harmonic profile lies inside the unavoidable `X^2` term on the right of (2). The basic first-order prime-divisibility consequence of the physical coefficient law therefore does **not** remove the `epsilon` in `FD-106` for any fixed `Theta<1`.

This does not show that the physical coefficient law is insufficient. It identifies the information lost by this particular reduction. Any successful coefficient-law attack must exploit structure beyond the first-order residue-class `L^2` budget: higher-order prime incidence, the complete least-prime-factor tree, multiplicative sign coherence, or an amortized coupling to source descent/head events. The boundary case `Theta=1` is not decided by the power audit below because the terminal prime range is then only subpower and logarithmic factors become first-order.

## 1. The physical increment law has an exact prime-power covariance

Write

\[
\mathcal H(X)=\sum_{n\le X}a(n),
\qquad
\mathcal H(0)=0,
\tag{7}
\]

with `a(n)` from (1). For a prime `p` and an integer `m>=1`, the radical changes only when `p` is absent from `m`. Directly from (1),

\[
\boxed{
a(pm)=
\begin{cases}
-(1-p^{-1})a(m),&p\nmid m,\\[2mm]
p^{-1}a(m),&p\mid m.
\end{cases}}
\tag{8}
\]

Define the `p`-divisible coefficient projection

\[
D_p(X):=
\sum_{\substack{n\le X\\p\mid n}}a(n).
\tag{9}
\]

Putting `Y=floor(X/p)` and splitting the sum over `m<=Y` according to divisibility by `p`, (8) gives the exact recurrence

\[
\boxed{
D_p(X)
=D_p(Y)-(1-p^{-1})\mathcal H(Y).
}
\tag{10}
\]

Iteration terminates after finitely many steps and yields

\[
\boxed{
D_p(X)
=-(1-p^{-1})
\sum_{j\ge1}
\mathcal H\!\left(\left\lfloor\frac X{p^j}\right\rfloor\right).
}
\tag{11}
\]

This is the direct arithmetic coupling missing from the synthetic source of `FD-107`: a reciprocal sample at `X/p` is not a freely placeable tent height. It controls a genuine divisibility projection of the physical coefficient sequence, up to the deeper `p`-adic samples.

## 2. Additive large sieve bounds all prime divisibility projections simultaneously

Let

\[
S_X(\alpha):=\sum_{n\le X}a(n)e(n\alpha),
\qquad e(t):=e^{2\pi it}.
\tag{12}
\]

Additive-character orthogonality gives

\[
D_p(X)-\frac{\mathcal H(X)}p
=
\frac1p
\sum_{h=1}^{p-1}S_X(h/p).
\tag{13}
\]

By Cauchy--Schwarz,

\[
p\left|D_p(X)-\frac{\mathcal H(X)}p\right|^2
\le
\sum_{h=1}^{p-1}|S_X(h/p)|^2.
\tag{14}
\]

For primes `p<=P`, all fractions `h/p` in (14) are reduced and distinct; two distinct such fractions are separated modulo one by at least `P^{-2}`. The classical additive large sieve therefore gives

\[
\sum_{3\le p\le P}
\sum_{h=1}^{p-1}|S_X(h/p)|^2
\le
(X-1+P^2)
\sum_{n\le X}|a(n)|^2.
\tag{15}
\]

The physical law (1) has `|a(n)|<=1`, so

\[
\boxed{
\sum_{3\le p\le P}
p\left|D_p(X)-\frac{\mathcal H(X)}p\right|^2
\ll X(X+P^2).
}
\tag{16}
\]

Now put

\[
T_p(X):=
\sum_{j\ge2}
\mathcal H\!\left(\left\lfloor\frac X{p^j}\right\rfloor\right).
\tag{17}
\]

Since the physical source is one-Lipschitz and starts at zero,

\[
|\mathcal H(y)|\le y,
\]

hence

\[
|T_p(X)|
\le
X\sum_{j\ge2}p^{-j}
=
\frac{X}{p(p-1)}.
\tag{18}
\]

Combining (11) with `D_p=mathcal H(X)/p + (D_p-mathcal H(X)/p)` gives the exact centered identity

\[
\boxed{
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)
+\frac{\mathcal H(X)}{p-1}
=
-\frac{p}{p-1}
\left(D_p(X)-\frac{\mathcal H(X)}p\right)
-T_p(X).
}
\tag{19}
\]

Squaring, summing with weight `p`, using `p/(p-1)<=3/2` for `p>=3`, and applying (16)--(18) proves (2). The `p`-adic tail contributes only

\[
X^2\sum_{p\ge3}\frac1{p(p-1)^2}=O(X^2),
\tag{20}
\]

which is already contained in the right side of (2).

The derivation is intentionally first-order. It uses the exact physical coefficient law to create the divisibility projections `D_p`, but after that it sees the coefficient sequence only through its `L^2` norm.

## 3. The terminal prime rows are exactly reciprocal samples seen by (2)

Take a four-adic parent horizon

\[
H=4X.
\tag{21}
\]

The prime rows `r=4p` are members of the repaired dyadic-terminal nonhead family of `FD-093`. Their exact physical energy is

\[
\boxed{
E_{4p}(H)
=w(4p)
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)^2,
\qquad
w(4p)=\frac34(1-p^{-2}).
}
\tag{22}
\]

Thus (2) is not merely a generic estimate on unrelated source samples: it directly constrains a distinguished subfamily of the terminal fan responsible for the harmonic endpoint in `FD-106`.

For a high-mass parent, the source-rich cutoff is

\[
L_H
=\left\lfloor\frac{U_H}{H\log H}\right\rfloor.
\tag{23}
\]

A retained terminal prime row has source argument `floor(X/p)>L_H`, so

\[
p\ll\frac{X}{L_H}
\ll\frac{XH\log H}{U_H}
\asymp\frac{X^2\log X}{U_H}.
\tag{24}
\]

On a sharp false-RH state (3), logarithms and fixed constants are absorbed in the `o(1)` exponent, giving

\[
\boxed{
p\le P_*(X):=X^{2-2\Theta+o(1)}.}
\tag{25}
\]

The same exponent appeared implicitly in the source-rich repairs of `FD-105`--`FD-106`; here it becomes the natural modulus range for the physical large-sieve constraint.

## 4. The harmonic matched profile fits inside the large-sieve budget

Stress-test (2) against the exact obstruction isolated by `FD-106` and realized generically by `FD-107`. Suppose, only as a capacity model, that a fixed fraction of a sharp parent mass is placed on prime terminal rows with

\[
E_{4p}(H)
\asymp
\frac{U_H}{S(P)p},
\qquad
3\le p\le P,
\tag{26}
\]

where

\[
S(P)=\sum_{3\le p\le P}\frac1p.
\tag{27}
\]

Then by (22), uniformly up to harmless fixed factors,

\[
\left|
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)
\right|^2
\asymp
\frac{U_H}{S(P)p}.
\tag{28}
\]

Hence the reciprocal-sample contribution to the left side of (2) satisfies

\[
\sum_{p\le P}p
\left|
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)
\right|^2
\ll
\frac{U_H\pi(P)}{S(P)}.
\tag{29}
\]

Now take `P` at the full source-rich scale (24), so that

\[
P\ll\frac{X^2\log X}{U_H},
\qquad
P=X^{2-2\Theta+o(1)}.
\tag{30}
\]

For every fixed `Theta<1`, `P` tends to infinity polynomially and

\[
\log P=(2-2\Theta+o(1))\log X.
\tag{31}
\]

The prime number theorem gives `pi(P)<<P/log P`, so (29)--(31) imply

\[
\begin{aligned}
\sum_{p\le P}p
\left|
\mathcal H\!\left(\left\lfloor\frac Xp\right\rfloor\right)
\right|^2
&\ll
\frac{U_HP}{S(P)\log P}\\
&\ll_\Theta
\frac{X^2\log X}{S(P)\log P}\\
&\ll_\Theta
\boxed{\frac{X^2}{S(P)}}.
\end{aligned}
\tag{32}
\]

Euler's divergence of the reciprocal-prime sum gives `S(P)->infinity`, so the quantity in (32) is `o(X^2)`.

The deterministic centering term in (2) also fits. `FD-046` gives, for every fixed `tau>Theta`,

\[
|\mathcal H(X)|\ll_\tau X^\tau.
\tag{33}
\]

Because `Theta<1`, choose `tau` with `Theta<tau<1`. The elementary bound

\[
\sum_{p\le P}\frac{p}{(p-1)^2}
\ll\log P
\tag{34}
\]

gives

\[
|\mathcal H(X)|^2
\sum_{p\le P}\frac{p}{(p-1)^2}
\ll_\tau
X^{2\tau}\log P
=o(X^2).
\tag{35}
\]

Using `|u+v|^2<=2|u|^2+2|v|^2`, equations (32) and (35) show that the complete harmonic profile (26), including the deterministic center in (2), consumes only `o(X^2)`. The right side of (2), however, contains the unavoidable term `X^2`. Thus the prime-divisibility large sieve has enough capacity to accommodate the matched endpoint throughout the full source-rich power range.

This comparison is deliberately a **stress test of the theorem**, not a construction of a physical source with profile (26). Its conclusion is information-theoretic: inequality (2), even though it is a genuine consequence of the physical coefficient law, is compatible with the terminal harmonic allocation at the full power range that the source-rich predecessor mechanism can expose.

The special case `Theta=1` is excluded from this power audit. Then `P_*(X)=X^{o(1)}` and logarithmic factors are no longer subordinate to a fixed positive power. Equation (2) remains true, but (30)--(35) no longer classify the endpoint sharply.

## 5. Prior-art calibration and the new frontier

The load-bearing external input is the classical additive large-sieve inequality for separated rational points; a primary anchor is H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119--134, DOI `10.1112/S0025579300004708`. The prime-number-theorem upper bound used in (32) is already anchored for this line through D. J. Newman's PNT source in `SOURCES.md`. No novelty is claimed for either theorem.

Prime-denominator refinements are also a real neighboring literature. Henryk Iwaniec, *The large sieve with prime moduli*, Revista Matemática Iberoamericana **38** (2022), 2337--2354, DOI `10.4171/RMI/1381`, surveys the classical prime-modulus problem and proves sharper estimates under additional coefficient-support or `L^2` hypotheses. `FD-108` does **not** claim that (15) is the best possible prime-modulus inequality for the physical coefficients. Its durable statement is narrower: the immediate first-order divisibility projection of (1), closed only with the standard coefficient norm `sum|a(n)|^2<=X`, is power-critical at the exact terminal range (25).

The literature audit did not locate a result tying this particular coefficient sequence `mu(rad n)phi(rad n)/n`, the reciprocal samples `mathcal H(floor(X/p))`, and the Farey/Schur terminal least-prime fan into a stronger inequality. The exact recurrence (10)--(11) is elementary once (1) is known; the Mathia-specific content is its use as the first physical-law test of the `FD-106` endpoint and the scale comparison (24)--(35).

The next useful coefficient-law attack therefore has a more precise target. A first-order prime incidence estimate loses too much. One needs either a **higher-order incidence inequality** that sees simultaneous divisibility by `pq`, `pqr`, ... and hence the complete least-prime-factor tree, or a signed/multiplicative constraint that couples those levels before squaring. The other live route remains the global one from `FD-102`/`FD-106`: make repeated source descent or head events pay the selection tax that terminal prime entropy can otherwise sustain.

**Boundary.** `FD-108` is a negative result about a specific reduction of the physical coefficient law, not about the full law. It rules out the strategy “apply prime-divisibility orthogonality plus a standard large sieve and remove the terminal epsilon” at power scale for every fixed `1/2<Theta<1`. It does not rule out stronger prime-modulus estimates tailored to these coefficients, higher-order multiplicative incidence, logarithmically sharp information, or a separate treatment of `Theta=1`.