# MC-112 — Off-center proportional shells close every fixed local parity filter

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact Hamming-shell deformation and fixed local filter from `MC-107` and `MC-111`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
L:=\log\log N,
\tag{1}
\]

and

\[
A(z)=\sum_{j=0}^{r}a_jz^j,
\qquad
T^A_{k,N}:=\sum_{j=0}^{r}a_jC_{k+j,N},
\tag{2}
\]

where `A` is a fixed nonzero real polynomial, independent of `N`, and the shell sequence is extended by zero outside its finite support. The exact parity transfer remains

\[
\sum_{k\in\mathbb Z}(-1)^kT^A_{k,N}
=A(-1)\mathcal Q_N(1).
\tag{3}
\]

Thus a lossless local parity carrier must satisfy `A(-1)\ne0`.

`MC-111` classified filters with `A(1)\ne0` and filters having a simple zero at `1`, leaving a possible escape when `A` has a double or higher-order zero there. That escape disappears once the filter is tested away from the exactly flat central saddle.

Let `\beta>0` be fixed and choose integers `k=k_N` with

\[
\frac{k-2}{2L}\longrightarrow\beta.
\tag{4}
\]

The proportional Sathe--Selberg shell law of `MC-107` gives, uniformly on compact positive `\beta`-ranges,

\[
\frac{C_{k+1,N}}{C_{k,N}}
=\left(1+o(1)\right)\frac{2L}{k-1}.
\tag{5}
\]

Therefore for every fixed `j\ge0`,

\[
\boxed{
\frac{C_{k+j,N}}{C_{k,N}}\longrightarrow\beta^{-j}.
}
\tag{6}
\]

Substitution into the finite filter gives the exact transfer-function limit

\[
\boxed{
\frac{T^A_{k,N}}{C_{k,N}}
\longrightarrow A(\beta^{-1}).
}
\tag{7}
\]

Because a nonzero fixed polynomial has only finitely many positive real roots, one can choose a fixed `\beta>0`, as close to `1` as desired but avoiding those finitely many reciprocal roots, such that

\[
A(\beta^{-1})\ne0.
\tag{8}
\]

For such a `\beta`, equation `(7)` yields

\[
|T^A_{k,N}|\sim |A(\beta^{-1})|\,C_{k,N}.
\tag{9}
\]

The same `MC-107` asymptotic, with Stirling applied at `k-2\sim2\beta L`, gives

\[
\boxed{
C_{k,N}
\sim
\frac{J\,\mathcal A(\beta)}{\sqrt{4\pi\beta L}}
\,N^2(\log N)^{-2I(\beta)},
}
\tag{10}
\]

where

\[
I(\beta):=1-\beta+\beta\log\beta\ge0
\tag{11}
\]

and the positive arithmetic factor `\mathcal A(\beta)` is the one in `MC-107`. Consequently

\[
\boxed{
|T^A_{k,N}|
\asymp_{A,\beta}
\frac{N^2}{(\log N)^{2I(\beta)}\sqrt{\log\log N}}
=N^{2-o(1)}.
}
\tag{12}
\]

This holds for **every fixed nonzero finite local filter** after choosing one fixed off-center proportional shell on which its transfer function does not vanish. In particular, the multiplicity of the zero of `A` at `z=1` is irrelevant to the existence of an almost-square filtered coefficient.

If `A(-1)\ne0`, the exact reconstruction `(3)` and any positive diagonal Hölder weights `w_{k,N}` give, for conjugate exponents `1\le p,q\le\infty`,

\[
|\mathcal Q_N(1)|
\le
\frac1{|A(-1)|}
\left\|(w_{k,N}T^A_{k,N})_k\right\|_p
\left\|(w_{k,N}^{-1})_k\right\|_q.
\tag{13}
\]

For every coordinate `K`,

\[
\left\|wT^A\right\|_p
\left\|w^{-1}\right\|_q
\ge |T^A_K|.
\tag{14}
\]

Choosing the proportional shell from `(8)`--`(12)` therefore forces

\[
\boxed{
\frac1{|A(-1)|}
\left\|wT^A\right\|_p
\left\|w^{-1}\right\|_q
=N^{2-o(1)}\ \text{or larger}.
}
\tag{15}
\]

Hence **no fixed finite local parity-preserving filter followed by positive diagonal absolute-value/Hölder control can yield any fixed polynomial saving over the source scale**. Higher-order finite differences do not evade the shell obstruction; they only suppress the exactly central local-ratio frequency.

No estimate for `M(x)` is improved here. The result classifies one radial certificate family and leaves genuinely signed nonlocal reconstruction, `N`-dependent/growing-range filters, and finer source-coupled/non-radial information open.

## 1. Fixed shifts sample the transfer polynomial at a proportional-shell frequency

For `j>0`, telescope the consecutive ratios:

\[
\frac{C_{k+j,N}}{C_{k,N}}
=\prod_{m=0}^{j-1}
\frac{C_{k+m+1,N}}{C_{k+m,N}}.
\tag{16}
\]

For each fixed `m`, `(k+m-2)/(2L)\to\beta`, so `MC-107` gives

\[
\frac{C_{k+m+1,N}}{C_{k+m,N}}
\longrightarrow\frac1\beta.
\tag{17}
\]

The product is finite because the filter degree is fixed, proving `(6)`. Equation `(7)` then follows directly:

\[
\frac{T^A_{k,N}}{C_{k,N}}
=\sum_{j=0}^{r}a_j\frac{C_{k+j,N}}{C_{k,N}}
\longrightarrow
\sum_{j=0}^{r}a_j\beta^{-j}
=A(\beta^{-1}).
\tag{18}
\]

This gives a simpler classification than expanding higher derivatives at the central mode. The local shell ratio varies through the continuum `\beta^{-1}\in(0,\infty)` as the proportional scale varies. A fixed nonzero polynomial can annihilate only finitely many of those frequencies.

The condition `A(-1)\ne0` enters only when the filtered sequence is required to retain the target parity endpoint. The off-center floor `(12)` already holds for every fixed nonzero `A`; a filter with `A(-1)=0` simply cannot reconstruct `\mathcal Q_N(1)` through `(3)`.

## 2. Every proportional shell is still almost square on the `N` scale

`MC-107` gives

\[
C_{k,N}
\sim
J\mathcal A(\beta)
\frac{N^2}{(\log N)^2}
\frac{(2L)^{k-2}}{(k-2)!}.
\tag{19}
\]

Put `n=k-2=2\beta L+o(L)`. Stirling's formula yields

\[
\frac{(2L)^n}{n!}
=
\frac{1+o(1)}{\sqrt{4\pi\beta L}}
\exp\!\left(2\beta L(1-\log\beta)+o(L)\right).
\tag{20}
\]

Since `e^L=\log N`, equations `(19)`--`(20)` become `(10)` with

\[
-2+2\beta(1-\log\beta)
=-2I(\beta).
\tag{21}
\]

The convex function `I` is nonnegative and vanishes only at `\beta=1`. For any fixed `\beta>0`, `(10)` differs from `N^2` only by powers of `\log N` and `\log\log N`, proving the `N^{2-o(1)}` statement. Moreover, because the roots excluded in `(8)` are finite, `\beta` can be chosen arbitrarily close to `1`, so even the fixed logarithmic penalty `2I(\beta)` can be made arbitrarily small for each fixed filter.

This is the key point missed by a purely central Taylor analysis: a high-order zero at `1` can make many central derivatives vanish, but moving a fixed proportional distance in shell degree changes the local geometric ratio to a nearby value where the same fixed polynomial is nonzero while the shell magnitude remains almost square.

## 3. Absoluteizing after any fixed local filter still loses the decisive cancellation

Equation `(3)` says that a parity-preserving filter does not remove the endpoint; it rewrites it as signed cancellation among the filtered degrees. A diagonal norm certificate discards those signs.

The one-coordinate estimate `(14)` is independent of the choice of positive weights and of `p`. Thus any actual filtered coefficient of size `N^{2-o(1)}` is already enough to prevent a fixed power saving in `(13)`. No estimate for the complete `\ell^1` variation is needed, and no global unimodality of the shell sequence is needed.

This strengthens `MC-111`: the simple-zero calculation there showed explicitly how a first derivative survives in the central `\sqrt L` window. The present off-center argument shows that **every fixed order** survives somewhere in the proportional Sathe--Selberg range. The obstruction is therefore not first-order differentiation; it is the mismatch between a fixed finite transfer polynomial and the continuum of local shell ratios.

## 4. Prior art and novelty boundary

No new analytic-number-theory input is introduced. The proportional shell asymptotic and uniform consecutive-ratio law are the `MC-107` result, whose load-bearing analytic ingredient is classical quantitative Sathe--Selberg/Landau--Selberg--Delange coefficient extraction. `MC-111` already audited Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, AMS (2019), Theorem 16.2, as an authoritative modern source for that machinery.

The finite-filter viewpoint itself is classical signal/difference algebra: a finite shift operator has polynomial transfer function, and higher-order zeros at the flat frequency correspond to higher finite differences. `MC-111` records the adjacent Charlier finite-difference/Poisson prior-art boundary through NIST DLMF §§18.21--18.22. The proof here does not need Charlier polynomials; it uses only the exact Mathia shell sequence plus the fixed-shift ratio limit.

A targeted literature search for combinations of Sathe--Selberg asymptotics with finite differences, polynomial local filters, Charlier transforms, and Möbius/Hamming shells found generic prime-factor-distribution and finite-difference material but no direct source-specific statement equivalent to `(7)`--`(15)`. **No novelty claim is made.** The durable mathematical delta is the closure of the previously explicit higher-order fixed-filter escape in the current source deformation.

## 5. Boundaries and falsification tests

- The filter degree and coefficients are fixed as `N\to\infty`. An `N`-dependent polynomial may place an increasing number of roots across the relevant ratio range, use coefficients whose condition number grows with `N`, or have growing range; none of those possibilities is classified here.
- The argument requires only one off-center proportional shell. It does not prove a useful lower bound for the signed sum `\sum_k(-1)^kT^A_{k,N}` beyond the exact identity `(3)`; strong cancellation among the large filtered coefficients remains possible and is precisely the missing endpoint mechanism.
- Positive diagonal Hölder/absolute-value certificates are closed because they cannot exploit cancellation between filtered degrees. A genuinely non-diagonal signed quadratic form, recurrence, transfer operator, or other structured cancellation estimate is outside the claim.
- `A(-1)\ne0` is necessary for the filter to carry the parity endpoint. If it fails, recovery would need additional information outside the filtered sequence.
- The proportional asymptotic is used only at a fixed positive `\beta` in its established uniform regime. No extrapolation to `\beta\to0`, `\beta\to\infty`, or a moving filter-dependent `\beta_N` is required.
- The proof does not identify a new arithmetic source of cancellation and does not transfer the `N^2` shell scale directly to an exponent for the Mertens function.

The decisive falsifier would be a fixed nonzero finite filter `A` with `A(-1)\ne0` for which every proportional-shell response is `o(C_{k,N})`. Equation `(7)` reduces that possibility to `A(\beta^{-1})=0` for every `\beta` in a positive interval, forcing `A\equiv0`; hence no such fixed filter exists.

## Consequence for the research line

The fixed finite radial-filter branch is now closed completely. Central high-order differencing is not a new escape: any fixed local parity filter that suppresses the flat central shell necessarily reappears with almost-square amplitude on an off-center proportional shell, and absoluteizing there restores the same no-power-saving obstruction.

A further radial attack must therefore change one of the hypotheses materially: use an `N`-dependent or growing-order filter, preserve signed cancellation through a genuinely nonlocal relation, or retain finer source coupling rather than reducing to one radial shell coordinate. This sharpens the current line frontier without asserting progress on RH itself.