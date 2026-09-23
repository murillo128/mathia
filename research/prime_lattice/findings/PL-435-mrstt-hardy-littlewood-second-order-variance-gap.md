# PL-435 — MRSTT almost-all Hardy–Littlewood remains first-order at the Selberg covariance gate

**Evidence/status:** `LITERATURE+EXACT-DERIVED + QUANTITATIVE-OBSTRUCTION + CURRENT-LITERATURE-BOUNDARY`.

**Parent findings:** `PL-421`, `PL-425`, `PL-432`, `PL-434`.

## Claim

The 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen (MRSTT) theorem on Hardy--Littlewood correlations with one averaging variable is genuinely quadratic and therefore much closer to the covariance target than the linear short-interval estimate audited in `PL-434`. Nevertheless, the published theorem still stops at a first-order correlation scale and does **not** supply the second-order aggregate precision required by the `PL-421`/`PL-432` covariance gate.

For `ell=2`, MRSTT Theorem 1.5 states that, whenever

\[
X^{1/3+\varepsilon}\le H\le X^{1-\varepsilon},
\]

one has

\[
\sum_{n\le X}\Lambda(n)\Lambda(n+h)
=(1+o(1))\,\mathfrak S(0,h)X
\tag{1}
\]

for a proportion `1-o(1)` of the shifts `1<=h<=H`. Thus current unconditional technology already reaches the two-point prime correlation itself for almost all shifts in precisely the polynomial short-shift regime relevant to the direct-prime route.

However, a moving-window variance is not a generic average of these correlations. It is a **triangularly weighted residual after cancellation of leading terms of order `XH^2`**. If

\[
E(h):=
\sum_{n\sim X}\Lambda(n)\Lambda(n+h)-X\mathfrak S(h)
\tag{2}
\]

schematically denotes the pair-correlation error, then the unresolved contribution to a length-`H` Selberg-type variance has the form

\[
R_H
=2\sum_{1\le h<H}(H-h)E(h)
\tag{3}
\]

up to the usual diagonal, endpoint, centering, and smoothing conventions. The natural principal-channel scale used by `PL-432` is

\[
XH L_X,
\qquad L_X\asymp \log(X/H)
\tag{4}
\]

in the classical mesoscopic prime model. Therefore a route that transfers the desired covariance through pair correlations needs a second-order estimate of the schematic strength

\[
R_H=o(XH L_X)
\tag{5}
\]

(or a sufficiently small fixed fraction of this scale if only a fixed spectral margin is required).

MRSTT's proof of Theorem 1.5 contains a key error term `mathcal E_I(h)` for which equation (8.14) is reduced, uniformly over unimodular sequences `c(h)`, to

\[
\sum_{h\le H}c(h)\mathcal E_I(h)=o_{w\to\infty}(HX)
\tag{6}
\]

in the von-Mangoldt case. Choosing phases gives an `l^1` control at the same `o(HX)` scale for that decomposition error. Even granting an analogous `o(HX)` aggregate for the total correlation error in (2), the triangular weight only yields

\[
|R_H|
\le 2H\sum_{h<H}|E(h)|
=o(XH^2),
\tag{7}
\]

whereas (5) asks for `o(XH L_X)`. The missing aggregate precision is therefore a factor of order

\[
\boxed{\frac{H}{L_X}}
\tag{8}
\]

(up to logarithms, constants, and the exact channel normalization). On every polynomial scale `H=X^{theta+o(1)}` with fixed `theta>0`, this is a polynomial gap.

The conclusion is deliberately theorem-strength only: **MRSTT Theorem 1.5 does not close the covariance gate, and its published qualitative/first-order error architecture does not by itself provide the second-order triangular residual needed here.** This does not show that MRSTT's methods cannot be sharpened, nor that the true residual (3) is large.

## 1. Exact triangular identity behind the gate

For any finitely supported complex sequence `a_n`, define the moving sum

\[
S_H(y)=\sum_{1\le r\le H}a_{y+r}
\]

and correlation

\[
C_a(d)=\sum_n a_{n+d}\overline{a_n}.
\]

Expanding the square and counting pairs with difference `d` gives the exact Fejér/triangular identity

\[
\boxed{
\sum_y |S_H(y)|^2
=
\sum_{|d|<H}(H-|d|)C_a(d).
}
\tag{9}
\]

The same identity applies entrywise to cross-covariances between residue or character channels. Hence pair-correlation information can in principle feed the `PL-421` matrix gate directly, without first proving the source-replacement estimate considered in `PL-434`.

But (9) also exposes the conditioning problem. For prime-type sources, each uncentered off-diagonal correlation is of size about `X`, so the triangular sum contains a leading mass of order `XH^2`. After centering and singular-series cancellation, the variance of interest is only of order `XH L_X`. The desired object is therefore a lower-order residual of a much larger pair-correlation aggregate.

This is why an almost-all relative asymptotic such as (1), despite being a major quadratic theorem, is not automatically a variance theorem.

## 2. What MRSTT proves, and what it does not

MRSTT Theorem 1.5 proves for fixed `ell` that

\[
\sum_{n\le X}
\Lambda(n)\Lambda(n+h)\cdots\Lambda(n+(\ell-1)h)
=(1+o(1))\mathfrak S(0,h,\ldots,(\ell-1)h)X
\]

for proportion `1-o(1)` of `h<=H` when `H>=X^{1/3+epsilon}`. For `ell=2` this is the Hardy--Littlewood prime-pair asymptotic for almost all shifts in the short averaging range.

The statement provides a leading relative asymptotic on almost all shifts. It does not state a weighted second-order estimate of the form (5), nor does it quantify the exceptional shifts strongly enough to infer such an estimate merely by summation.

In the proof, their equation (8.14) concerns a particular model-decomposition error `mathcal E_I(h)`. They reduce its control to the uniform estimate (6) for all unimodular `c(h)`. This is useful evidence for the available quantitative scale, but **`mathcal E_I(h)` must not be identified with the entire Hardy--Littlewood error `E(h)` in (2)**: the proof also contains main-term/model comparisons and sieve-theoretic steps. The present obstruction therefore uses (6) only as an audit of the theorem's error architecture, not as an equality between two different residuals.

Even if one optimistically promoted the same `o(HX)` aggregate scale to the total `E(h)`, (7) would still fall short of (5) by (8). Thus no hidden identification of `mathcal E_I` is needed for the negative conclusion.

## 3. Why the target scale is second-order

Montgomery and Soundararajan's short-interval prime model predicts, for `N^delta<=H<=N^{1-delta}`, that

\[
\operatorname{Var}\bigl(\psi(x+H)-\psi(x)\bigr)
\sim H\log(N/H).
\tag{10}
\]

Integrating over a base interval of length comparable to `X` produces the `XH log(X/H)` scale in (4). Classical work connecting Selberg integrals and zero pair correlation likewise treats this variance as a genuinely second-order object; later Selberg-class generalizations preserve that distinction.

For the current line, (4) is a **conditioning/target scale**, not a new unconditional asymptotic asserted for every fixed mod-5 or quarter-turn channel. `PL-432` already isolates the relevant multiscale Selberg-type `L^2` quantities, and `PL-421` asks for a covariance matrix with a fixed normalized spectral margin. Any fixed-modulus/channel application must propagate the appropriate local density and singular-series constants before importing the scalar model.

The key scale comparison does not depend on the exact constant: whenever the centered covariance is `XH` times only a logarithmic or subpolynomial factor, a first-order `o(XH^2)` correlation remainder is parametrically too coarse on polynomial `H` scales.

## 4. Relation to `PL-434`

`PL-434` showed that MRSTT Theorem 3.1 already controls the **exact quarter-turn multiplicative phase** and fixed mod-5 residue restrictions at extremely strong logarithmic accuracy, but only as a linear moving-sum estimate. Turning that estimate into an `L^2` source replacement loses the square-root-in-`H` factor needed for covariance stability.

Theorem 1.5 is the obvious possible escape: rather than replace the source in `L^2`, estimate the quadratic correlations directly. The present finding shows that this escape reaches the correct *type* of object but still not the required *precision*. The obstruction moves from a norm mismatch to a cancellation/conditioning mismatch:

\[
\text{leading pair correlations at scale }XH^2
\quad\hbox{versus}\quad
\text{centered variance at scale }XH L_X.
\]

Thus `PL-434` is not superseded by MRSTT's quadratic application. The current theorem solves neither the variance residual nor the oriented mod-5 covariance matrix at the precision required by `PL-421`.

## 5. Prior-art and novelty audit

Primary current source:

- Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, “Higher uniformity of arithmetic functions in short intervals II. Almost all intervals,” *Inventiones Mathematicae* **244** (2026), 967–1091. DOI `10.1007/s00222-026-01408-6`; published 26 January 2026; arXiv `2411.05770`. Theorem 1.5 is the one-averaging-variable Hardy--Littlewood result; proof equation (8.14) and the subsequent unimodular reduction record the `o(HX)` scale for the model-decomposition error in the von-Mangoldt case.

Variance-scale anchors:

- Hugh L. Montgomery, K. Soundararajan, “Primes in short intervals,” *Communications in Mathematical Physics* **252** (2004), 589–617; arXiv `math/0409258`. Their mesoscopic model gives variance `~H log(N/H)` rather than the naive `H log N` scale.
- H. M. Bui, J. P. Keating, D. J. Smith, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *Journal of the London Mathematical Society* **94**(1) (2016), 161–185, DOI `10.1112/jlms/jdw030`; arXiv `1506.03741`. This is already source 106 in the line ledger and anchors the established variance/pair-correlation bridge beyond zeta.

The Fejér/triangular identity (9), the relation between prime pair correlations and Selberg-type variances, and the expected `H log(X/H)` variance scale are classical. No novelty is claimed for them. Targeted current-literature search did not locate a published theorem deriving the `PL-421` oriented covariance gate, or even the required unweighted principal Selberg variance asymptotic in this polynomial short-shift range, merely from MRSTT Theorem 1.5.

The durable line-specific delta is the **quantitative route audit**: comparing the strongest directly relevant 2026 almost-all Hardy--Littlewood theorem with the exact triangular covariance transform shows that leading-order pair control remains short by a factor `H/L_X` in aggregate precision. This is a negative/redirect, not a claimed new number-theoretic theorem.

## 6. Adversarial audit

1. **Almost-all is not automatically too weak.** A sufficiently quantitative exceptional-set estimate plus a sufficiently strong pointwise error could imply (5). The obstruction is to the theorem as currently stated/proved at qualitative/first-order scale, not to the logical form “almost all shifts” in general.

2. **Equation (6) is not the full prime-pair error.** The proof residual `mathcal E_I(h)` belongs to MRSTT's decomposition. The argument above explicitly does not identify it with (2). It is used only to show that the published proof supplies a key error estimate at `o(HX)` scale rather than the `o(XL_X)`-after-weighting scale the variance gate would require.

3. **The triangular weight may admit cancellation.** The absolute-value estimate (7) deliberately throws away cancellation between different shifts. A future signed/oscillatory theorem for `sum (H-h)E(h)` could reach (5) without improving `sum|E(h)|` by the full factor (8). This is precisely the surviving target.

4. **The singular-series main term also has to be averaged at second order.** Recovering the variance constant requires cancellation between the diagonal, centering terms, and the weighted average of `mathfrak S(h)-1`; controlling only `E(h)` is not by itself the whole Selberg-variance proof. The current negative is therefore conservative: even perfect handling of (2) at first-order scale would not remove the remaining main-term bookkeeping.

5. **The mod-5 oriented matrix is harder, not easier, than the scalar gate audited here.** A scalar principal-channel variance estimate would still have to be polarized across residue/character channels and combined with the quarter-turn probe from `PL-431`--`PL-432`. Failure already at the scalar second-order precision means Theorem 1.5 cannot by itself close the full matrix route.

6. **No RH/GRH assumption has been imported.** The point of using MRSTT is to audit the best matched unconditional prime-side input. Conditional pair-correlation/GRH machinery may reach related variance statements but would not provide the non-circular arithmetic bridge sought by this line.

7. **A method refinement remains possible.** MRSTT note that parts of their Gowers-uniformity machinery are kept qualitative for quantitative-effectiveness reasons. Nothing here proves that their methods cannot be reorganized to obtain a stronger weighted second-order estimate.

## Consequence for the line

The next live analytic target is now sharper than “find a quadratic theorem for primes.” Such a theorem already exists at leading order. What is needed is a **second-order weighted correlation theorem** at the Selberg scale, schematically

\[
\boxed{
\sum_{1\le h<H}(H-h)
\left(
\sum_{n\sim X}\Lambda(n)\Lambda(n+h)
-X\mathfrak S(h)
\right)
=o(XH L_X),
}
\tag{11}
\]

with the appropriate diagonal/centering conventions, and ultimately a fixed-mod-5 cross-channel/quarter-turn analogue strong enough to preserve the `PL-421` image-cone margin.

This redirects the search away from additional leading-order Hardy--Littlewood or generic higher-uniformity theorems and toward **quantitative Selberg-variance asymptotics, weighted pair-correlation remainders, or direct oriented covariance estimates**. The distinction is load-bearing: the line no longer lacks a theorem that sees prime pairs; it lacks the extra cancellation needed to recover a covariance that is smaller than the raw pair-correlation mass by a factor of order `H/L_X`.