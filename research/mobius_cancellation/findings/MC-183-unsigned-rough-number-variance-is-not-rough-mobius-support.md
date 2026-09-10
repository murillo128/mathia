# MC-183 — Unsigned rough-number variance controls a periodic eligibility envelope, not the rough Möbius support

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The closest classical unsigned short-interval object to the live rough Möbius factor of `MC-180`--`MC-181` is **not** its support. It is a strictly larger periodic eligibility envelope, and in the current logarithmic-cutoff regime that envelope already has much stronger variance control than the signed target. Consequently the modern variance theory of rough numbers cannot be imported as a black-box approximation to the required rough Möbius variance: a valid transfer must separately recover square-free support and Möbius orientation.

Keep

\[
H=X^\theta,
\qquad
0<\theta<1,
\qquad
y=c\log X,
\qquad
0<c<\min(\theta,1-\theta),
\tag{1}
\]

and define

\[
q=Q_y:=\prod_{p\le y}p,
\qquad
P_y:=\frac{\varphi(q)}q.
\tag{2}
\]

The live signed coefficient is

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}.
\tag{3}
\]

By contrast, the standard rough-number indicator is

\[
\alpha_y(n):=\mathbf 1_{P^-(n)>y}
=\mathbf 1_{(n,q)=1}.
\tag{4}
\]

The exact relationships are therefore

\[
\boxed{g_y=\mu\,\alpha_y,}
\qquad
\boxed{|g_y|=\mu^2\alpha_y.}
\tag{5}
\]

In particular,

\[
\boxed{\alpha_y\ne |g_y|.}
\tag{6}
\]

For every prime `p>y`,

\[
\alpha_y(p^2)=1,
\qquad
|g_y(p^2)|=0.
\tag{7}
\]

Thus forgetting the Möbius sign in `(3)` does **not** produce the usual rough-number indicator. It produces the indicator of **square-free rough numbers**. The square-free projector is an additional arithmetic layer that standard unsigned rough-number variance does not retain.

This distinction is especially sharp at the present cutoff. The envelope `alpha_y` is exactly `q`-periodic. For integer `H=kq+r`, `0<=r<q`, set

\[
D_y(x,H)
:=
\sum_{x<n\le x+H}\alpha_y(n)-HP_y.
\tag{8}
\]

Every block of `q` consecutive integers contains exactly `phi(q)` integers coprime to `q`, so pointwise for every real `x`,

\[
\boxed{D_y(x,H)=D_y(x,r).}
\tag{9}
\]

Let

\[
W_y(X,H)=\int_X^{2X}|D_y(x,H)|^2\,dx.
\tag{10}
\]

The classical reduced-residue variance of Hausman--Shapiro and Montgomery--Vaughan gives, in the normalization

\[
V_q(r)
=
\frac1q\sum_{a\bmod q}
\left(
\sum_{1\le h\le r}\mathbf 1_{(a+h,q)=1}-rP_y
\right)^2,
\tag{11}
\]

the upper bound

\[
\boxed{V_q(r)\le rP_y.}
\tag{12}
\]

Because `D_y(x,r)^2` is `q`-periodic and constant between consecutive integers,

\[
\int_0^q|D_y(x,r)|^2dx=qV_q(r).
\tag{13}
\]

Partitioning an interval of length `X` into complete periods plus one remainder yields

\[
\boxed{
W_y(X,H)
\le
(X+q)V_q(r)
\le
(X+q)qP_y.
}
\tag{14}
\]

The prime number theorem gives

\[
q=\exp((1+o(1))y)=X^{c+o(1)},
\tag{15}
\]

so, since `c<theta` and `q=o(X)`, the periodic envelope satisfies

\[
\boxed{W_y(X,H)\le X^{1+c+o(1)}.}
\tag{16}
\]

Compare `(16)` with the actual signed target from `MC-180`,

\[
V_y(X,H)
:=
\int_X^{2X}
\left|\sum_{x<n\le x+H}g_y(n)\right|^2dx
\le
X^{1+o(1)}H^{2-\eta},
\qquad 0<\eta\le1.
\tag{17}
\]

For every such fixed `eta`,

\[
\frac{W_y(X,H)}{XH^{2-\eta}}
\le
X^{c-\theta(2-\eta)+o(1)}
\le
X^{-(\theta-c)+o(1)}.
\tag{18}
\]

Hence the **pre-sieve rough eligibility envelope** is already power-more-regular than the entire signed variance family being sought. But this does not solve even the unsigned support problem `|g_y|=mu^2 alpha_y`, and it certainly does not solve the signed problem. The gap from established rough-number variance to `(17)` contains two distinct operations:

\[
\alpha_y
\longrightarrow
\mu^2\alpha_y=|g_y|
\longrightarrow
\mu\alpha_y=g_y.
\tag{19}
\]

The first restores square-free support; the second restores prime-factor-parity orientation. Neither operation is encoded by the periodic reduced-residue statistic `(10)`.

The practical conclusion is a no-shortcut statement: **a theorem about the variance of integers without small prime factors is not a theorem about the absolute support of the rough Möbius coefficient, even before the sign problem is addressed.** Any proposed transfer must expose and price both missing layers rather than calling `alpha_y` the support of `g_y`.

## 1. Why the rough-number object becomes elementary at this cutoff

Ofir Gorodetsky, *The variance of integers without small prime factors in short intervals*, Math. Z. 308, 59 (2024), DOI `10.1007/s00209-024-03601-w`, defines exactly the indicator `(4)`. He records that for fixed `y` it is periodic with primorial period

\[
q_y=\prod_{p\le y}p
\tag{20}
\]

and mean

\[
P_y=\prod_{p\le y}(1-1/p),
\tag{21}
\]

and notes the exact variance reduction under `H -> H-q_y` when `H>q_y`.

The current Möbius decomposition chooses `y=c log X` for a different reason: `MC-180` needs the small-prime Möbius factor to have only subpower many states and to lie below both the interval and complementary scales. That same choice makes

\[
q_y=X^{c+o(1)}=o(H)
\tag{22}
\]

by the already-required inequality `c<theta`. Thus a polynomial window contains many complete periods of `alpha_y`.

Equation `(9)` is consequently exact, not an almost-all statement. All full primorial blocks contribute precisely their deterministic mean; only the residual interval of length `r<q` fluctuates. The reduced-residue variance `(11)` prices that residual.

Gorodetsky reviews the one-period formulas of Miriam Hausman and Harold Shapiro, *On the mean square distribution of primitive roots of unity*, Comm. Pure Appl. Math. 26 (1973), 539--547, DOI `10.1002/cpa.3160260407`, and the bounds of Hugh Montgomery and Robert Vaughan, *On the distribution of reduced residues*, Ann. of Math. 123 (1986), 311--333, DOI `10.2307/1971274`. The latter supplies `(12)`.

No asymptotic formula from the modern rough-number variance theory is needed for `(16)`. The elementary period reduction plus the classical reduced-residue upper bound already puts the envelope below the live fixed-power variance scale.

## 2. The actual unsigned support contains a square-free projector

The terminology is easy to blur because both objects exclude all primes at most `y`. The difference is prime powers above the cutoff.

The rough indicator `alpha_y` allows

\[
p^2,
p^3,
p^aq^b,\ldots
\qquad(p,q>y),
\]

whereas Möbius vanishes as soon as any prime occurs twice. Therefore

\[
\operatorname{supp}(g_y)
=
\{n:P^-(n)>y,\ n\text{ square-free}\},
\tag{23}
\]

and its indicator is `mu^2 alpha_y`, not `alpha_y`.

This is not a cosmetic distinction that can be erased at fixed-power cost by the most naive estimate. If

\[
E_y(x,H)
:=
\sum_{x<n\le x+H}\alpha_y(n)(1-\mu^2(n)),
\tag{24}
\]

then every counted integer is divisible by `p^2` for some prime `p>y`. Absolute union bounding gives only

\[
E_y(x,H)
\le
\sum_{y<p\le\sqrt{x+H}}
\left(\frac{H}{p^2}+1\right).
\tag{25}
\]

Even discarding the endpoint `+1` issue, the density term from `(25)` saves only inverse powers of `y` (hence only logarithms when `y=c log X`), not a fixed power of `H`. So a fixed-power transfer from `alpha_y` to `|g_y|` cannot be justified merely by saying nonsquarefree rough integers are sparse.

Equation `(25)` is deliberately only a diagnostic bound. Sharper square-free short-interval methods may exploit cancellation or averaging unavailable to this absolute estimate. The point is that **such a theorem would be an additional input**, not something contained in the rough-number variance `(16)`.

## 3. Restoring sign is a second, independent parity step

Even perfect knowledge of the square-free support leaves the orientation

\[
g_y(n)=(-1)^{\omega(n)}
\qquad
\text{on }\operatorname{supp}(g_y)
\tag{26}
\]

undetermined. This is exactly the kind of information separated from local divisor densities by `MC-082`.

`MC-082` used Liouville parity classes as an explicit classical sieve control and showed that extremely accurate Type-I/local-density information can coexist with opposite prime-factor parity content. The present finding adds a source-specific warning: the most adjacent modern unsigned paper does not even stop at `|g_y|`; it stops one layer earlier at the rough eligibility envelope `alpha_y`.

Thus a route from unsigned rough-number theory to the live target must cross both arrows in `(19)`. A square-free-support theorem may address the first. A genuinely parity-sensitive bilinear, Type-II, harmonic, or other signed mechanism is still required for the second. Treating one arrow as though it supplied the other would recreate the classical parity loss in a more specialized notation.

## 4. Prior-art and novelty assessment

Everything used to control `alpha_y` is classical or established prior art. The primorial period and mean are standard and stated explicitly by Gorodetsky. Reduced-residue mean squares were studied by Hausman--Shapiro and Montgomery--Vaughan, and `(12)` is a classical upper bound. The prime-number-theorem estimate `(15)` is standard.

Gorodetsky's 2024 paper is particularly important because its title and object are close enough to the current frontier to invite a false identification. Its coefficient is the indicator of **all** integers with no prime divisor at most `y`. It is not Möbius-weighted and is not square-free restricted. Its sophisticated variance asymptotics therefore constitute useful unsigned prior art but not evidence for `(17)`.

No novelty is claimed for `(4)`, periodicity, reduced-residue variance, or the square-free identity in `(5)`. The durable contribution is the combined **object-identity and rate audit** at the live cutoff: the literature object is a periodic envelope whose centered variance already beats the signed target by a fixed power, while the actual Möbius coefficient differs from it first by square-free projection and then by parity orientation.

This materially narrows the current research question. Searching for a stronger theorem about `alpha_y` itself is not a promising way to obtain `(17)` unless the theorem simultaneously retains information that distinguishes `mu^2 alpha_y` and then `mu alpha_y`.

## 5. Boundaries and falsification tests

- `alpha_y` is **not** called the support of `g_y` here. The exact support indicator is `mu^2 alpha_y`.
- The periodic reduction `(9)` applies to `alpha_y`; neither `mu^2 alpha_y` nor `g_y` is `q`-periodic in general because square divisibility and parity contributions from primes above `y` are not determined modulo `q`.
- The variance in `(10)` is centered by the deterministic rough density `HP_y`. It is not comparable to the uncentered signed sum by dropping the center term; the two coefficients are different objects.
- Equation `(25)` is an absolute diagnostic only. It is not claimed to be an optimal estimate for nonsquarefree rough integers in short intervals.
- The fixed-power gap `(18)` uses exactly the existing bootstrap condition `c<theta`; no stronger cutoff restriction is introduced.
- A future theorem that directly controls `mu^2 alpha_y` with fixed-power variance would address the first arrow in `(19)` and is not ruled out by this finding. It would still leave the signed arrow unless it also carries parity information.
- A parity-sensitive sieve or bilinear method is not ruled out. The obstruction is specifically to importing **unsigned rough-number variance** as though it were rough Möbius variance.
- No bound for `(17)`, `M(X)`, or the zeta zero set is proved.

The claim is falsified if `(5)` is incorrect, if the standard rough indicator is not primorial-periodic with mean `P_y`, if the reduced-residue upper bound `(12)` is misstated, or if `(18)` fails under `0<c<theta` and `0<eta<=1`.

## Consequence for the active frontier

`MC-180` isolates the logarithmically rough Möbius block as a viable signed source object, and `MC-181` shows that the split is subpower-reversible at fixed-power variance scale. The adjacent unsigned literature now has a precise place in that picture: it controls a **pre-sieve eligibility envelope**, not the coefficient or even its support.

The next source-side step should therefore not be another improvement to ordinary rough-number counting. It should ask which exact decomposition of `mu^2 alpha_y` or `mu alpha_y` exposes a fixed-power estimate while preserving the second arrow in `(19)`. Any candidate that never distinguishes `alpha_y`, `mu^2 alpha_y`, and `mu alpha_y` has not yet reached the live Möbius difficulty.