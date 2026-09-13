# RE-096 — depth-two bad hosts reduce to a phase-stable deformed quadratic sequence

**Status:** `EXACT-DERIVED + MIXED-FIRST/SECOND-LAYER-CHAMBERS + INTEGER-HOST-ENLARGEMENT + LOGARITHMIC-QUADRATIC-DRIFT + PHASE-DERIVATIVE-STABILITY + FIXED-POWER-PRIOR-ART-BOUNDARY + SOURCE-CONDITIONED-TARGET-REFINEMENT + PRIOR-ART-AUDITED`.

`RE-095` isolates a concrete target for the residual mixed first/depth-two channel. If, at physical scale `X` and interval length `H=X^vartheta`, the number of **prime** hosts `q asymp X^(1/2)` for which the deterministic sample

\[
x_q:=\eta_1^{-1}(\eta_2(q))
\]

has a prime-free one-sided `2H` neighborhood is `X^(kappa(vartheta)+o(1))`, then any `kappa(vartheta)<1/2` creates a genuine improvement over the `173/200` second-moment frontier. This made the missing input look intrinsically prime-indexed.

The host primality is not actually needed for that analytic input. The map `x_q` extends canonically to every large real, hence every integer, host. Enlarging from prime hosts to all integer hosts can only increase the bad set. The resulting integer sample is not an ordinary quadratic lattice, but it is an exceptionally rigid logarithmic deformation of one:

\[
\boxed{
 x(t)
 =\frac{t^2}{2}
 \left(
 1+\frac{\log 2}{2\log t}
 +\frac{\log 2\,(\log 2-1)}{4(\log t)^2}
 +O\!\left(\frac1{(\log t)^3}\right)
 \right).
}
\tag{1}
\]

Consequently

\[
\boxed{
 x(t)-\frac{t^2}{2}
 \sim
 \frac{\log 2}{4}\frac{t^2}{\log t},
}
\tag{2}
\]

so the CA sample is **not** close enough to the fixed quadratic lattice for a short-interval theorem at `t^2/2` to transfer by interval inclusion at any power scale `H=X^vartheta` with `vartheta<1`. On the other hand its logarithmic phase is much more stable than its physical position:

\[
\boxed{
 \frac{d}{dt}\log x(t)
 =\frac2t-\frac{\log 2}{2t(\log t)^2}
 +O\!\left(\frac1{t(\log t)^3}\right),
}
\tag{3}
\]

\[
\boxed{
 \frac{d^2}{dt^2}\log x(t)
 =-\frac2{t^2}
 +O\!\left(\frac1{t^2(\log t)^2}\right).
}
\tag{4}
\]

Thus zero-sum phases `gamma log x(n)` have the same first- and second-derivative geometry as the quadratic phase `2 gamma log n`, up to logarithmically smaller derivative errors. This changes the most natural next target: rather than first seeking a theorem conditioned on `q` being prime, it is enough to prove the required bad-host saving for the **all-integer deformed-quadratic sequence** `x(n)`. That target is structurally closer to the fixed-power sparse-sequence literature, while still requiring a genuine adaptation because the physical displacement (2) is much larger than the short interval being tested.

## 1. The prime-host target embeds in an integer-host target

For real `t>1`, use the exact CA event maps

\[
\lambda_j(t)
=\log\!\left(1+\frac1{t+t^2+\cdots+t^j}\right),
\qquad
\eta_j(t)\log\eta_j(t)=\frac{\log t}{\lambda_j(t)}.
\tag{5}
\]

The functions are smooth and strictly increasing for all sufficiently large `t`, so define

\[
x(t):=\eta_1^{-1}(\eta_2(t)).
\tag{6}
\]

Fix shell constants `0<c<C` as in `RE-095`, put `H=X^vartheta`, and define the enlarged bad-index set

\[
\mathcal Z_\vartheta(X)
:=
\left\{
 n\in\mathbb Z:
 cX^{1/2}\le n\le CX^{1/2},
 (x(n)-2H,x(n))\cap\mathbb P=\varnothing
 \text{ or }
 (x(n),x(n)+2H)\cap\mathbb P=\varnothing
\right\}.
\tag{7}
\]

The prime-host bad set of `RE-095` is literally a subset:

\[
\boxed{
\mathcal B_\vartheta(X)\subseteq\mathcal Z_\vartheta(X).
}
\tag{8}
\]

Therefore any estimate

\[
\#\mathcal Z_\vartheta(X)
\ll X^{\kappa(\vartheta)+o(1)}
\tag{9}
\]

immediately supplies the hypothesis of `RE-095` with the same `kappa(vartheta)`. In particular, if for some

\[
\vartheta<\frac{73}{200}
\]

one proves

\[
\#\mathcal Z_\vartheta(X)
\ll X^{1/2-\delta+o(1)},
\qquad \delta>0,
\tag{10}
\]

then the moment contribution to the false-RH frontier drops from `173/200` to

\[
\frac{173}{200}-\frac\delta2.
\tag{11}
\]

The primality of the host `q` is still essential in the CA staircase that creates the actual mixed cell, but it need not be used by the **upper-bound theorem** that eliminates bad hosts. This is a useful relaxation of the source-conditioned target.

## 2. Exact reduction to one scalar implicit equation

The equality `eta_1(x(t))=eta_2(t)` can be stripped of the common Lambert inversion. If

\[
R_j(u):=\frac{\log u}{\lambda_j(u)},
\tag{12}
\]

then the defining relation is exactly

\[
\boxed{R_1(x(t))=R_2(t).}
\tag{13}
\]

For `j=1,2`,

\[
\lambda_1(x)=\log\!\left(1+\frac1x\right),
\qquad
\lambda_2(t)=\log\!\left(1+\frac1{t+t^2}\right).
\tag{14}
\]

Using

\[
\frac1{\log(1+z)}
=\frac1z+\frac12-\frac z{12}+O(z^2)
\qquad(z\to0),
\tag{15}
\]

gives

\[
R_1(x)
=\log x\left(x+\frac12+O(x^{-1})\right),
\tag{16}
\]

and

\[
R_2(t)
=\log t\left(t^2+t+\frac12+O(t^{-2})\right).
\tag{17}
\]

Since `RE-093` already gives `x(t)=t^2/2(1+O(1/log t))`, write

\[
L:=\log t,
\qquad c:=\log2,
\]

and seek

\[
x(t)=\frac{t^2}{2}
\left(1+\frac aL+\frac b{L^2}+O(L^{-3})\right).
\tag{18}
\]

The terms of size `tL` and smaller in (17) are negligible compared with `t^2/L^2`, so (13) reduces to matching the logarithmic expansion of `x log x` through relative order `L^(-2)`. Substitution gives

\[
\frac{x\log x}{t^2}
=
L+\left(a-\frac c2\right)
+\frac{b+\frac a2(1-c)}{L}
+O(L^{-2}).
\tag{19}
\]

Matching (17) yields

\[
a=\frac c2,
\qquad
b=\frac{c(c-1)}4,
\tag{20}
\]

which proves (1). In particular the leading correction has a nonzero positive coefficient, so the previous `O(1/log t)` displacement from `RE-093` is a genuine drift rather than a removable error term. Equation (2) follows immediately.

At the relevant physical scale `X asymp x(t) asymp t^2`, equation (2) becomes

\[
\left|x(t)-\frac{t^2}{2}\right|
\asymp \frac X{\log X}.
\tag{21}
\]

For every fixed `vartheta<1`,

\[
\frac{X/\log X}{X^\vartheta}\to\infty.
\tag{22}
\]

Hence a theorem saying that `[t^2/2,t^2/2+X^vartheta]` contains primes gives no pointwise information about the interval of the same length adjacent to `x(t)`. In particular this obstruction applies throughout the `RE-095` window `vartheta<73/200`.

## 3. The logarithmic phase nevertheless stays quadratic

The physical drift is large, but the analytic phases occurring in explicit-formula approaches depend on `log x(t)`, not directly on `x(t)-t^2/2`. Taking logs in (1) gives

\[
\log x(t)
=2L-c+\frac c{2L}
+\frac{c(c-2)}{8L^2}
+O(L^{-3}).
\tag{23}
\]

Differentiating the smooth implicit solution, or equivalently differentiating its asymptotic expansion, yields (3)--(4). Thus for

\[
\Phi_\tau(t):=\tau\log x(t),
\tag{24}
\]

we have

\[
\Phi_\tau'(t)
=\frac{2\tau}{t}
\left(1+O((\log t)^{-2})\right),
\tag{25}
\]

and

\[
\Phi_\tau''(t)
=-\frac{2\tau}{t^2}
\left(1+O((\log t)^{-2})\right).
\tag{26}
\]

These are exactly the derivative scales of the fixed-power phase attached to `n^2`. So the CA deformation is large in **position space** but small in the derivative geometry used by Kusmin--Landau / van der Corput type exponential-sum estimates. This does not by itself transfer any published sparse-power theorem: a proof still has to check every range of the zero sum, amplitudes, endpoints, and uniformity under the slowly varying deformation. It does, however, identify the right comparison class much more sharply than the crude asymptotic `x_q~q^2/2`.

## 4. The closest published fixed-power theorem is still outside the needed exponent window

The closest direct prior art located in the audit is Danilo Bazzanella, *Prime Numbers in Intervals Starting at a Fixed Power of the Integers*, J. Aust. Math. Soc. **87** (2009), 83--99, DOI `10.1017/S1446788709000020`. Its Theorem 1 proves an almost-all prime number theorem for intervals `[n^alpha,n^alpha+H]` once `H>=N^(c(alpha)+epsilon)`. In the range containing `alpha=2`, the published exponent is

\[
c(\alpha)=\frac58-\frac7{16\alpha},
\]

so

\[
\boxed{c(2)=\frac{13}{32}=0.40625.}
\tag{27}
\]

Even if one grants a harmless fixed-dilation analogue for starts proportional to `n^2`, this interval exponent is too long for the present Robin splice. `RE-095` requires

\[
\vartheta<\frac{73}{200}=0.365,
\tag{28}
\]

and

\[
\frac{13}{32}-\frac{73}{200}
=\frac{33}{800}
=0.04125.
\tag{29}
\]

Moreover Bazzanella's theorem is stated for the exact power lattice, while (21) shows that the actual CA sample is displaced by `asymp X/log X`, vastly more than either interval length. Thus the published theorem does not supply (10) in two independent senses: its demonstrated `alpha=2` interval threshold lies above the Robin window, and its start geometry is not the CA-deformed geometry.

This comparison is a prior-art boundary, not a load-bearing external theorem for (1)--(10) and not a claim that Bazzanella's method cannot be improved or adapted. Indeed (25)--(26) point in the opposite direction: the analytic phase geometry suggests that revisiting that sparse-sequence method with current zero-density/additive-energy technology on the exact function `x(n)` is a materially better target than trying to transfer the old theorem by physical proximity.

## 5. Research consequence

After `RE-095`, the missing theorem was naturally phrased as a prime-indexed statement at deformed quadratic sample points. The exact enlargement (8) shows that the prime-index restriction is optional for an upper bound. A sufficient theorem can instead be stated entirely on the integer sequence

\[
\boxed{
 x(n)=\eta_1^{-1}(\eta_2(n)),
 \qquad n\asymp X^{1/2}.
}
\tag{30}
\]

The new target is therefore:

\[
\boxed{
\text{find some }\vartheta<73/200\text{ and }\delta>0
\text{ such that }
\#\mathcal Z_\vartheta(X)
\ll X^{1/2-\delta+o(1)}.
}
\tag{31}
\]

This is weaker than proving a PNT asymptotic at every sample and no stronger than the prime-host target needed by `RE-095`; it simply enlarges the host set so that existing sparse-sequence analytic machinery becomes directly relevant. Equations (21) and (25)--(26) separate the two facts that must not be conflated: **physical closeness to a square is false at the needed scale, while quadratic oscillatory phase geometry survives.**

A targeted search found no published theorem stated for this CA-deformed sequence, nor a general smooth-sequence result whose hypotheses immediately imply (31). Bazzanella's fixed-power theorem is the nearest structural precedent found. No priority claim is made, and no new external theorem is load-bearing for the exact reduction above, so `SOURCES.md` is unchanged.