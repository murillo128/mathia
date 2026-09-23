# PL-434 — MRSTT already controls the quarter-turn twist, but only at first-moment scale

**Evidence/status:** `LITERATURE+DERIVED + QUANTITATIVE-OBSTRUCTION + CURRENT-LITERATURE-BOUNDARY`.

**Parent findings:** `PL-421`, `PL-423`, `PL-429`, `PL-431`, `PL-432`, `PL-433`.

## Claim

The direct-prime route left by `PL-432` and `PL-433` has a surprisingly close current-literature theorem, but that theorem stops at the wrong norm scale for the `PL-421` positivity gate.

Let

\[
\Lambda^\sharp(n)=\frac{P(R)}{\varphi(P(R))}1_{(n,P(R))=1},
\qquad
R=\exp((\log X)^{1/10}),
\]

be the sieve approximant used by Matomäki--Radziwiłł--Shao--Tao--Teräväinen (MRSTT). Their Theorem 3.1 proves that, for

\[
X^{1/3+\varepsilon}\le H\le X,
\qquad |T|\le X^C,
\]

and every fixed `A>0`, one has

\[
\left|
\sum_{x<n\le x+H}
(\Lambda(n)-\Lambda^\sharp(n))n^{-iT}
\right|^*
\ll H\log^{-A}X
\tag{1}
\]

for all `x in [X,2X]` outside a set of measure `O(X log^{-A}X)`. The star is a supremum over arithmetic progressions contained in the interval.

Consequently the exact quarter-turn frequency forced by `PL-431`,

\[
t_X=-\frac{\pi}{2\log X},
\tag{2}
\]

is already covered unconditionally, and the starred norm in (1) also covers each fixed residue class modulo `5`. Finite linear combinations therefore give the same type of bound for every mod-5 character channel. **The shrinking vertical twist and the fixed residue decomposition are not the first-order analytic obstruction in the range `H>=X^{1/3+epsilon}`.**

However, (1) is a density-scale / first-moment approximation. The covariance matrix in `PL-421` is built from `L^2(dx)` inner products of moving short-interval channel sums. To transfer a fixed positive spectral margin from the sieve model to the actual prime source, one needs a variance-scale approximation.

Write, for one fixed residue or character channel,

\[
E_T(x)
:=
\sum_{x<n\le x+H}
(\Lambda(n)-\Lambda^\sharp(n))\omega(n)n^{-iT},
\tag{3}
\]

where `omega` is either a fixed mod-5 progression indicator or a fixed mod-5 character. Theorem 3.1 and the trivial bound on its exceptional set imply, for every fixed `B>0`,

\[
\boxed{
\|E_T\|_{L^2([X,2X])}
\ll_B X^{1/2}H\log^{-B}X,
}
\tag{4}
\]

uniformly for the quarter-turn `T=t_X` (and, in fact, throughout the theorem's polynomial `T` range). The exponent `B` can be made arbitrarily large but must remain fixed.

By contrast, if the relevant centered source channel has the natural Selberg scale used in `PL-432`,

\[
\|B_T\|_2^2\asymp XHL_X,
\tag{5}
\]

with `L_X` logarithmic or otherwise subpolynomial, then covariance stability at fixed Loewner margin requires an error of order at most

\[
\|E_T\|_2=o\!\left((XHL_X)^{1/2}\right)
\tag{6}
\]

(or a sufficiently small fixed multiple if only a fixed spectral margin is sought). The bound supplied by (4), relative to (6), is only

\[
\frac{X^{1/2}H\log^{-B}X}{(XHL_X)^{1/2}}
=
\sqrt{\frac{H}{L_X}}\,\log^{-B}X.
\tag{7}
\]

For every polynomial short-interval scale `H=X^{theta+o(1)}` with fixed `theta>0` and subpolynomial `L_X`, (7) diverges for every fixed `B`. Thus the published higher-uniformity estimate does **not** imply the covariance-scale source replacement needed to push the `PL-421` dephasing image-cone inequality through the actual prime source.

This is a theorem-strength obstruction, not a lower bound on the true error. The residual in (3) may be much smaller in `L^2`; MRSTT simply does not prove the square-root-in-`H` improvement needed by this route.

## 1. Why the theorem already contains the quarter-turn and mod-5 channels

MRSTT Theorem 3.1 is stated for every real `T` with `|T|<=X^C`. Since

\[
|t_X|=\frac{\pi}{2\log X}\ll 1,
\]

(2) lies deep inside that range. No Taylor approximation to the twist is needed.

More importantly, their maximal notation is

\[
\left|\sum_{n\in I}f(n)\right|^*
=
\sup_{P\subset I\cap\mathbb Z}
\left|\sum_{n\in P}f(n)\right|,
\tag{8}
\]

where `P` runs over arithmetic progressions. Taking `P` to be the intersection with `n=a (mod 5)` gives (1) separately in every residue class. A fixed Dirichlet-character channel is a linear combination of the four reduced residue channels, so only a harmless fixed factor is lost.

This is stronger for the representation question than a generic polynomial-phase statement: it directly controls the multiplicative phase `n^{-iT}` that `PL-429` identifies with vertical translation.

## 2. The `L^2` consequence is still at density scale

On the good set supplied by Theorem 3.1,

\[
|E_T(x)|\ll H\log^{-A}X.
\tag{9}
\]

The exceptional set has measure `O(X log^{-A}X)`. Trivially, on `x in [X,2X]`,

\[
|E_T(x)|\ll H\log X
\tag{10}
\]

for the fixed-modulus channels, with more than enough slack for the sieve-model weight. Hence

\[
\begin{aligned}
\int_X^{2X}|E_T(x)|^2dx
&\ll XH^2\log^{-2A}X
 +X\log^{-A}X\,H^2\log^2X.
\end{aligned}
\tag{11}
\]

Because `A` is arbitrary and fixed, renaming the logarithmic exponent yields (4).

The proof of MRSTT also passes through mean-square estimates of size `H^2` times arbitrarily strong logarithmic savings. That is consistent with (4): the available theorem has excellent logarithmic uniformity but does not gain the factor `H^{1/2}` that separates density scale from short-interval variance scale.

## 3. Why covariance needs the stronger norm

Let `A_j=B_j+E_j` denote an actual mod-5 channel vector, a chosen model vector, and their error in `L^2([X,2X])`. Their Gram matrices satisfy

\[
\langle A_j,A_k\rangle-
\langle B_j,B_k\rangle
=
\langle E_j,B_k\rangle
+
\langle B_j,E_k\rangle
+
\langle E_j,E_k\rangle.
\tag{12}
\]

Therefore Cauchy--Schwarz controls the matrix perturbation by the `L^2` sizes of the errors. If each model channel has norm of order `(XHL_X)^{1/2}`, then preserving the normalized eigenvalue floor `1/4` from `PL-421` with a nonzero margin requires the error-to-channel norm ratio to be small enough. Equation (7) shows that Theorem 3.1 alone gives no such smallness on polynomial `H` scales.

The same issue survives at `T=t_X`: MRSTT solves the **phase-sensitive linear estimate**, while `PL-421` asks for a **quadratic covariance statement**. This distinction is exactly the norm gap left after `PL-429`--`PL-433` solved the representation and deterministic transport problems.

## 4. Principal-channel caveat

The sieve model `Lambda^sharp` is not the deterministic centering used by `PL-423` and `PL-432`. In the principal channel one has schematically

\[
\Lambda-1
=(\Lambda-\Lambda^\sharp)
 +(\Lambda^\sharp-1).
\tag{13}
\]

MRSTT controls only the first term in this decomposition. The rough-number fluctuation `Lambda^sharp-1` is part of the model covariance and must be analyzed separately. Thus (1) cannot be read as a direct estimate for the fully centered principal channel in `PL-432`.

This caveat strengthens rather than weakens the present boundary: even granting a model whose own covariance is perfectly understood, the published residual estimate is not at the `L^2` scale needed to transfer a fixed spectral floor.

## 5. Prior-art and novelty audit

The source theorem is:

- Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen, “Higher uniformity of arithmetic functions in short intervals II. Almost all intervals,” *Inventiones Mathematicae* **244** (2026), 967–1091, DOI `10.1007/s00222-026-01408-6`, published 26 January 2026; arXiv `2411.05770`.

Theorem 3.1 gives the multiplicatively twisted major-arc estimate (1), uniformly for polynomially bounded `T`, and its starred norm includes arithmetic progressions. Theorem 1.1 gives the broader nilsequence formulation. The paper itself emphasizes logarithmically strong discorrelation for `Lambda-Lambda^sharp`; it does not claim a variance-scale `L^2` source replacement of the type (6).

Targeted searches for twisted short-interval von-Mangoldt mean squares, fixed-modulus arithmetic progressions, and `Lambda^sharp` source replacement did not locate a theorem supplying (6) in the present polynomial-short-interval regime. Classical Selberg-integral and pair-correlation results control other second moments, but they do not automatically imply that this particular sieve-model residual is smaller than the natural covariance scale.

No novelty is claimed for MRSTT's theorem, for Cauchy--Schwarz, or for the observation that first-moment control need not transfer covariance. The line-specific durable content is the quantitative comparison (7): the strongest directly matched 2026 prime-side theorem already handles the exact quarter-turn/mod-5 probe, yet misses the `PL-421` covariance gate by a polynomial `sqrt(H/L_X)` factor modulo arbitrary fixed logarithmic savings.

## 6. Adversarial audit

1. **Equation (4) is an upper bound derived from the published theorem, not the true size of the residual.** Failure of that upper bound to meet (6) proves only that this theorem cannot close the route; it does not prove that a stronger estimate is false.

2. **Arbitrary logarithmic savings cannot be chosen with `A=A(X)`.** MRSTT states the result for each fixed `A`. On `H=X^{theta+o(1)}`, no fixed power of `log X` offsets the polynomial factor `H^{1/2}`.

3. **The starred progression norm does not create a covariance theorem.** It is valuable because it handles fixed mod-5 residue restrictions without a new character argument, but it remains a linear sum bound interval by interval.

4. **The model is not the PL-423 deterministic center.** Equation (13) must be retained. Any future use of `Lambda^sharp` has to propagate the rough-number model covariance and principal subtraction coherently.

5. **The variance scale (5) is a route assumption/target scale, not asserted here as a new unconditional asymptotic.** `PL-432` already isolates ordinary Selberg-type norms as the natural conditioning quantities. If a specific channel has a different scale, the comparison must be redone with that scale.

6. **A different quadratic theorem could bypass source replacement.** One might estimate the actual oriented covariance directly rather than compare `Lambda` with `Lambda^sharp`. The obstruction here is specifically to upgrading MRSTT's first-moment discorrelation into the needed matrix perturbation by elementary norm inequalities.

7. **No RH/GRH input has been imported.** The MRSTT theorem is unconditional. This is why it is a useful non-circular boundary for the direct prime-side route, even though it stops short of the required covariance control.

## Consequence for the line

The analytic target after `PL-433` can now be sharpened. It is no longer useful to ask merely for an unconditional theorem that sees the quarter-turn `n^{-it_X}` or fixed mod-5 progressions: MRSTT already supplies that at very high logarithmic accuracy for almost all intervals once `H>=X^{1/3+epsilon}`.

What is missing is specifically **quadratic-scale arithmetic control**. A theorem capable of advancing the `PL-421` route must either

\[
\boxed{
\|\Lambda-\Lambda^\sharp\|_{\text{moving short-interval }L^2}
\ll (XHL_X)^{1/2}
\times \text{(small margin)},
}
\]

with the same fixed residue/quarter-turn compatibility, or bypass `Lambda^sharp` and estimate the actual oriented covariance matrix strongly enough to place it inside the `PL-421` image cone.

This redirects the next literature and derivation pass from higher first-moment/nilsequence uniformity toward **second-moment source replacement or direct covariance estimates**. The representation problem is already solved at the relevant twist; the unresolved load-bearing step is the square-root-in-`H` gain needed at covariance scale.