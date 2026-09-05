# MC-089 — Common-prime omission is power-cheap on arbitrary scales; floor mismatch costs only boundary size

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `BOUNDARY/CONDITIONAL-GAIN`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-088` exhibited the first supercritical physical-space omission whose signed contribution is recursively cheaper than the ambient square-scale Mertens target. Its only structural defect was scale sparsity: the proof imposed `N=p^(L+1)` so that every p-adic cutoff aligned exactly with the Huxley--Watt numerator.

That alignment is not necessary. The resulting floor mismatch is only a divisor-boundary term of size `X^(1+o(1))`, uniformly in the deleted prime.

Let `N>=2` be an integer, let `p<=N` be any prime, and put

\[
X:=\frac Np.
\tag{1}
\]

For the Huxley--Watt annulus

\[
\mathcal A_N=\{(m,n):m,n\le N,\ mn>N\},
\tag{2}
\]

omit the common-`p` block

\[
E_{N,p}
:=
\{(m,n)\in\mathcal A_N:p\mid m,\ p\mid n\}
\tag{3}
\]

and write

\[
T_{N,p}
:=
\sum_{(m,n)\in E_{N,p}}
\mu(m)\mu(n)
 z\!\left(\frac{N^2}{mn}\right),
\qquad
z(x)=\lfloor x\rfloor+\frac12-x.
\tag{4}
\]

Then for every fixed

\[
\frac12<\beta<1,
\tag{5}
\]

the prior hypothesis

\[
M(y)=O(y^\beta)
\tag{6}
\]

implies, **uniformly for every prime `p<=N`**, 

\[
\boxed{
T_{N,p}
=O_\beta\!\left((1+N/p)^{2\beta}\right).
}
\tag{7}
\]

The proof uses only the elementary deletion of one Euler prime, the arbitrary-cutoff Huxley--Watt identity already recorded in `MC-S24`, and the standard divisor bound `d_3(n)=n^{o(1)}`. No continuation of `1/zeta(s)` is used.

Consequently fix any

\[
0<\delta<\frac12.
\tag{8}
\]

For all sufficiently large `N`, choose by Bertrand's postulate a prime

\[
N^\delta\le p_N\le 2N^\delta.
\tag{9}
\]

Then

\[
\boxed{
\#E_{N,p_N}
=N^{2(1-\delta)+o(1)},
}
\tag{10}
\]

so the omitted support is still supercritical at the square-root Mertens resolution, while (7) gives

\[
\boxed{
T_{N,p_N}
=O_\beta\!\left(N^{2\beta(1-\delta)}\right).
}
\tag{11}
\]

Thus the common-prime complement reduction from `MC-088` now holds on **every sufficiently large ambient scale**, not merely prime powers.

More strongly, because `beta<1`, the interval

\[
1-\frac1{2\beta}<\delta<\frac12
\tag{12}
\]

is nonempty. Choosing `delta` there makes

\[
2\beta(1-\delta)<1,
\tag{13}
\]

so a support-supercritical omitted block has signed contribution below the existing `O(N log N)` interior scale under the old exponent hypothesis.

For the retained source-coupled statistic `P_N(E)` of `MC-087`, the exact identity

\[
P_N(E_{N,p})
=
2M(N)-M(N^2)-I_N-T_{N,p},
\qquad
I_N=O(N\log N),
\tag{14}
\]

therefore has the following scale-complete contraction ledger. If in addition one proves uniformly for the chosen moving prime family

\[
P_N(E_{N,p_N})=O(N^{2\alpha}),
\qquad
\frac12<\alpha<\beta,
\tag{15}
\]

then

\[
\boxed{
M(N^2)
=O\!\left(N^{2\gamma}\right),
\qquad
\gamma=
\max\{\alpha,\beta(1-\delta)\}<\beta.
}
\tag{16}
\]

In particular, choosing

\[
\delta>1-\frac\alpha\beta
\tag{17}
\]

while keeping `delta<1/2` makes the complement subordinate to the retained estimate and yields `gamma=alpha`.

The scale-coverage problem for the **omitted common-prime block** is therefore closed. The remaining missing theorem is sharper and genuinely arithmetic: obtain a uniform sub-old-exponent estimate for the retained statistic as the deleted prime moves with `N`.

## 1. Arbitrary-scale reduction to a p-sifted quadratic form

Only square-free multiples of `p` contribute to (4). Define

\[
\nu_p(a):=\mu(a)\mathbf 1_{p\nmid a}.
\tag{18}
\]

Writing `m=pa`, `n=pb` gives `a,b<=X`, and

\[
p^2ab>N
\quad\Longleftrightarrow\quad
ab>\frac Xp.
\tag{19}
\]

Because the two common factors `mu(p)=-1` cancel,

\[
T_{N,p}
=
\sum_{\substack{a,b\le X\\ab>X/p}}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right).
\tag{20}
\]

Let

\[
Q_p(X)
:=
\sum_{a,b\le X}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right)
\tag{21}
\]

and

\[
J_p(X)
:=
\sum_{\substack{a,b\le X\\ab\le X/p}}
\nu_p(a)\nu_p(b)
 z\!\left(\frac{X^2}{ab}\right).
\tag{22}
\]

Then exactly

\[
T_{N,p}=Q_p(X)-J_p(X).
\tag{23}
\]

Since `|z|<=1/2`, the elementary divisor-hyperbola bound gives

\[
\boxed{
J_p(X)
=O\!\left(1+\frac Xp\log(2X)\right).
}
\tag{24}
\]

The exact Euler-factor deletion identity from `MC-088` remains

\[
\boxed{
\nu_p(n)
=
\sum_{\substack{i\ge0\\p^i\mid n}}
\mu\!\left(\frac n{p^i}\right).
}
\tag{25}
\]

No divisibility relation between `X` and `p` is needed for (25).

Put

\[
J:=\lfloor\log_p X\rfloor,
\qquad
x_i:=\frac{X}{p^i},
\qquad
A_i:=\lfloor x_i\rfloor
\quad(0\le i\le J).
\tag{26}
\]

Substituting (25) into (21) gives the exact finite expansion

\[
Q_p(X)
=
\sum_{i,j=0}^{J}
\sum_{u\le A_i}\sum_{v\le A_j}
\mu(u)\mu(v)
 z\!\left(\frac{x_i x_j}{uv}\right).
\tag{27}
\]

The only difference from `MC-088` is that generally `x_i x_j != A_iA_j`.

## 2. The floor mismatch is only a thin integer boundary

For positive integers `A,B` define the aligned Huxley--Watt sawtooth form

\[
Z(A,B)
:=
\sum_{u\le A}\sum_{v\le B}
\mu(u)\mu(v)
 z\!\left(\frac{AB}{uv}\right).
\tag{28}
\]

For each pair `(i,j)`, let

\[
K_{ij}:=x_ix_j,
\qquad
\Delta_{ij}:=K_{ij}-A_iA_j.
\tag{29}
\]

Since `A_i<=x_i<A_i+1`, one has

\[
0\le\Delta_{ij}<A_i+A_j+1.
\tag{30}
\]

The mismatch term is

\[
E_{ij}
:=
\sum_{u\le A_i}\sum_{v\le A_j}
\mu(u)\mu(v)
\left[
 z\!\left(\frac{K_{ij}}{uv}\right)
-z\!\left(\frac{A_iA_j}{uv}\right)
\right].
\tag{31}
\]

Using `z(t)=floor(t)+1/2-t`, write

\[
E_{ij}=F_{ij}-\Delta_{ij}H(A_i)H(A_j),
\tag{32}
\]

where

\[
F_{ij}
=
\sum_{u\le A_i}\sum_{v\le A_j}
\mu(u)\mu(v)
\left(
\left\lfloor\frac{K_{ij}}{uv}\right\rfloor
-
\left\lfloor\frac{A_iA_j}{uv}\right\rfloor
\right).
\tag{33}
\]

The difference of floors counts integer multiples of `uv` lying in the interval `(A_iA_j,K_ij]`. Hence

\[
F_{ij}
=
\sum_{A_iA_j<r\le K_{ij}}
\sum_{\substack{u\le A_i,\ v\le A_j\\uv\mid r}}
\mu(u)\mu(v).
\tag{34}
\]

The inner sum has at most `d_3(r)` terms, because every admissible pair `(u,v)` extends to an ordered factorization `r=uvk`. Therefore, for every fixed `eta>0`, the standard divisor bound gives

\[
|F_{ij}|
\ll_\eta
(\Delta_{ij}+1)X^\eta.
\tag{35}
\]

Also the trivial bound `|H(A)|<=1+log A` gives

\[
|\Delta_{ij}H(A_i)H(A_j)|
\ll
\Delta_{ij}\log^2(2X).
\tag{36}
\]

Now

\[
J+1=O(\log(2X)),
\qquad
\sum_{i=0}^{J}A_i=O(X),
\tag{37}
\]

uniformly in `p>=2`. Summing (30), (35), and (36) over `(i,j)` yields

\[
\boxed{
Q_p(X)
=
\sum_{i,j=0}^{J} Z(A_i,A_j)
+O_\eta(X^{1+\eta})
}
\tag{38}
\]

for every fixed `eta>0`, uniformly in the deleted prime. This is the floor-mismatch repair absent from `MC-088`.

The important point is structural: misalignment does **not** create another square-scale quadratic term. It creates only a thin set of integer levels between two nearby product cutoffs.

## 3. Huxley--Watt evaluates the aligned layers

The arbitrary-independent-cutoff identity of Huxley and Watt (`MC-S24`) gives exactly, for positive integers `A,B`,

\[
\boxed{
Z(A,B)
=
M(A)+M(B)-M(AB)
-ABH(A)H(B)
+\frac12M(A)M(B).
}
\tag{39}
\]

This is the same identity used in `MC-088`; only the treatment of the nonintegral p-adic scales is new here.

Assume (6). As already audited in `MC-088`, partial summation plus convergence of `sum mu(n)/n` gives

\[
H(y)=O_\beta(y^{\beta-1}).
\tag{40}
\]

Hence

\[
Z(A,B)
=
O_\beta\!\left(
(AB)^\beta+A^\beta+B^\beta
\right).
\tag{41}
\]

The p-adic cutoffs satisfy

\[
\sum_{i=0}^{J}A_i^\beta
\ll_\beta X^\beta,
\tag{42}
\]

uniformly in `p`, while `J+1=O(log(2X))`. Therefore

\[
\sum_{i,j=0}^{J}Z(A_i,A_j)
=
O_\beta\!\left(X^{2\beta}+X^\beta\log(2X)\right)
=
O_\beta(X^{2\beta}).
\tag{43}
\]

Choose `eta` in (38) with `1+eta<2beta`. Then (38), (43), and (24) prove (7).

This deduction is uniform in `p`. In particular, the number of p-adic layers may grow logarithmically for small `p` without changing the power exponent, while for `p=N^(delta+o(1))` the layer count is actually bounded in terms of `delta`.

## 4. Polynomially moving primes remove the scale-sparsity defect

Fix `0<delta<1/2` and choose `p_N` as in (9). Then

\[
X=\frac N{p_N}=N^{1-\delta+o(1)}.
\tag{44}
\]

The omitted support is the set of integer pairs `a,b<=X` with `ab>X/p_N`. Thus

\[
\#E_{N,p_N}
=
\lfloor X\rfloor^2
-
O\!\left(1+\frac X{p_N}\log(2X)\right),
\tag{45}
\]

which proves (10). Because `delta<1/2`, its support exponent `2(1-delta)` is strictly larger than `1`; the family remains outside the generic RH-scale support-restoration regime of `MC-087`.

At the same time, (7) gives (11). The complement saving is now present for every sufficiently large `N`, with no interpolation between prime-power scales.

If `delta` additionally satisfies (12), then the signed common-prime block is `O(N^(1-kappa))` for some `kappa>0` determined by `beta,delta`. Thus under the old exponent hypothesis the deliberately omitted supercritical block is cheaper than the already-known interior term `I_N=O(N log N)`.

This is the strongest form of the complement reduction: support cardinality alone says the block is far too large to restore, while its source-compatible signed arithmetic structure makes it lower-order at the square-root scale.

## 5. The remaining contraction problem is now purely the retained carrier

Insert (11) into (14). Under (6),

\[
M(N)=O(N^\beta),
\tag{46}
\]

which is smaller than `N^(2alpha)` whenever `alpha>1/2`; the same is true of `I_N=O(N log N)`. Therefore (15) implies (16).

For any fixed `alpha<beta`, one may choose `delta` satisfying both

\[
1-\frac\alpha\beta<\delta<\frac12,
\tag{47}
\]

because `alpha/beta>1/2`. Then

\[
\beta(1-\delta)<\alpha,
\tag{48}
\]

so the complement no longer limits the bootstrap and the new exponent is exactly `alpha`.

This does not prove (15). The retained statistic contains almost the entire annulus and depends on a prime that changes with scale. Any useful theorem must therefore be **uniform in a polynomially moving prime family** and must arise from arithmetic information genuinely weaker than the Mertens exponent it is intended to improve.

The result removes two previous escape ambiguities at once. A positive continuation no longer needs to search for another recursively cheap supercritical complement, and it no longer needs to solve prime-power interpolation for this common-prime construction. It must attack the retained source-coupled statistic itself.

## 6. Falsification controls and boundaries

The proof has four load-bearing points.

First, the coefficient identity (25) must be used with every p-adic power dividing the integer coefficient; truncation at `J=floor(log_p X)` is justified only because larger powers cannot divide any `a<=X`.

Second, the mismatch estimate must retain the floor jumps. Replacing `z(K/(uv))` by a smooth Lipschitz approximation would miss the only delicate term. Equation (34) handles those jumps exactly as a thin interval of integer product levels.

Third, the divisor-bound estimate is an **absolute** boundary estimate, not Möbius cancellation. If the interval `(A_iA_j,K_ij]` had square-scale length, the argument would fail. Its length is small only because independent flooring changes a product cutoff by `O(A_i+A_j)`.

Fourth, (7) remains conditional on the old Mertens exponent. The result does not supply an unconditional fixed power saving for `M`, and the retained estimate (15) is not inferred from deleting the common-prime block.

The moving-prime choice is also not arithmetic specificity by itself. Bertrand's postulate merely guarantees a prime of the required size. A matched system with the same one-prime Euler-factor deletion algebra and the same source identity would inherit the same complement reduction. Rational-prime specificity must enter, if at all, through a bound for the retained carrier.

Finally, the choice `delta<1/2` is not needed for (7); it is imposed only to ensure that the omission remains genuinely supercritical relative to the support-only barrier. For `delta>=1/2`, generic support restoration is already sufficient and this mechanism adds no information advantage.

## 7. Prior art and novelty boundary

The aligned identity (39) is prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20--34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`, recorded as `MC-S24`. Their theorem already allows arbitrary independent integer cutoffs.

The p-sifted coefficient identity (25), Bertrand's postulate, divisor-hyperbola counting, and the standard `d_3(n)=n^(o(1))` bound are classical mechanisms. A targeted literature search around p-sifted Möbius sums, deletion of one Euler factor, and Huxley--Watt arbitrary cutoffs did not expose this exact floor-mismatch annular reduction, but absence from that search is not evidence of novelty. No standalone number-theoretic novelty is claimed.

The durable contribution is narrower and frontier-specific: the exact prime-power alignment in `MC-088` was an artifact of the proof, not a mathematical barrier. The discontinuous sawtooth kernel survives arbitrary p-adic cutoff misalignment with only `X^(1+o(1))` boundary cost. That closes the common-prime complement's global scale-coverage defect and leaves a single quantitative research obligation: a uniform estimate for the retained moving-prime statistic.

## Consequence for the research line

`MC-087` showed that support-small omissions merely reconstruct Mertens. `MC-088` crossed that barrier with one supercritical common-prime block but only on prime-power scales. The present result removes that scale restriction completely.

For any old exponent `beta>1/2`, one can now choose at every large scale a polynomially moving prime so that the omitted block is still support-supercritical, yet its signed contribution is strictly lower-exponent and can even be pushed below the source interior term. If a retained estimate with any exponent `alpha<beta` can be proved uniformly for that family, the exact source identity upgrades it directly to the same improved global Mertens exponent.

The live frontier is therefore the retained statistic itself: identify a source-natural representation or arithmetic theorem that controls `P_N(E_{N,p_N})` uniformly in a moving prime `p_N=N^(delta+o(1))` without already assuming the target zero-free/Mertens bound.