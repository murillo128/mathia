# WI-087 — Close-prime Ramanujan cross Grams have an exact Loewner--Bezout rank family

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It resolves `CLUE-loewner-rational-interpolation-pairwise-rank-defect`: the exceptional `(11,13,47)` rank loss from WI-081 is the first nontrivial instance of an exact arithmetic family, and along an unconditional sequence of close prime pairs the residual transversality defect from WI-086 occupies asymptotically one third of the smaller Ramanujan dimension. Thus the hope that the residual close-prime regime has universally small pairwise rank defect is false.

Let `p<q` be primes satisfying

\[
p\equiv2\pmod 3,\qquad q\equiv1\pmod 3,\qquad q<2p.
\]

Define

\[
\alpha=\frac{2p-q}{3},\qquad
\beta=\frac{p+q}{3},\qquad
\delta=\frac{pq+p-q}{3}.
\tag{1}
\]

These are positive integers. For the nearest-boundary Ramanujan cross Gram of WI-081/WI-086 with boundary length `delta`, one has the exact formula

\[
\boxed{
\operatorname{rank}G_{p,q}^{(\delta)}=\beta=\frac{p+q}{3}.
}
\tag{2}
\]

Since `delta>q-1`, WI-086's residual transversality invariant applies and gives

\[
\boxed{
\tau_{p,q}(\delta)
=(p-1)-\operatorname{rank}G_{p,q}^{(\delta)}
=\alpha-1
=\frac{2p-q-3}{3}.
}
\tag{3}
\]

In particular the known witness `(p,q,delta)=(11,13,47)` has `(alpha,beta,tau)=(3,8,2)`, exactly recovering its rank `8` without the integer-minor certificate used in WI-081.

Moreover there exist infinitely many such prime pairs with `q/p -> 1`. Along any such sequence,

\[
\frac{\operatorname{rank}G_{p,q}^{(\delta)}}{p-1}\longrightarrow\frac23,
\qquad
\frac{\tau_{p,q}(\delta)}{p-1}\longrightarrow\frac13.
\tag{4}
\]

So residual pairwise rank defect is not merely a sporadic low-dimensional accident: it can consume a positive proportion of the smaller primitive-frequency space.

## 1. The short-boundary Gram is a Loewner divided-difference matrix

WI-081 proves that after cancelling complete `lcm(p,q)=pq` periods and, when needed, passing to the translated complementary boundary, the cross Gram is, up to an overall sign and invertible diagonal phases,

\[
G_{p,q}^{(N)}\sim (V_p^{(\delta)})^*V_q^{(\delta)}.
\tag{5}
\]

For a primitive `p`-th root `z` and primitive `q`-th root `w`, the corresponding entry is

\[
\sum_{x=0}^{\delta-1}z^{-x}w^x
=z^{1-\delta}\frac{z^\delta-w^\delta}{z-w}.
\tag{6}
\]

The row factor `z^(1-delta)` is nonzero. Hence the rank equals that of the rectangular Loewner matrix

\[
L_{z,w}=\frac{z^\delta-w^\delta}{z-w}.
\tag{7}
\]

This is an exact change of representation, not yet the source of the rank drop.

## 2. A three-term rational function interpolates `X^delta` on both primitive node sets

Put

\[
\gamma=\beta-\alpha=\frac{2q-p}{3},
\]

and define

\[
P(X)=1+X^\alpha+X^\beta,
\qquad
Q(X)=1+X^\gamma+X^\beta,
\qquad
R(X)=\frac{P(X)}{Q(X)}.
\tag{8}
\]

The parameter identities

\[
\alpha+\beta=p,
\qquad
\alpha+\gamma=\beta,
\qquad
\beta+\gamma=q,
\qquad
2\beta=\alpha+q
\tag{9}
\]

give the polynomial identities

\[
\boxed{P(X)-X^\alpha Q(X)=1-X^p,}
\tag{10}
\]

\[
\boxed{P(X)-X^\beta Q(X)=(1+X^\alpha)(1-X^q).}
\tag{11}
\]

The denominator is regular on both node sets. Indeed, if a root of unity `u` of prime order `r!=3` satisfied

\[
1+u^\gamma+u^\beta=0,
\]

then three complex numbers of modulus one would sum to zero. They must form an equilateral triple, so `u^gamma` and `u^beta` would be nontrivial cube roots of unity. But the cyclic group of `r`-th roots has no element of order `3`, contradiction. This applies to `r=p` and `r=q`.

Therefore (10) and (11) imply, respectively,

\[
R(z)=z^\alpha\quad(z^p=1),
\qquad
R(w)=w^\beta\quad(w^q=1).
\tag{12}
\]

The congruences following from (1) are

\[
\delta\equiv\alpha\pmod p,
\qquad
\delta\equiv\beta\pmod q,
\tag{13}
\]

so on the primitive node sets

\[
\boxed{R(z)=z^\delta,\qquad R(w)=w^\delta.}
\tag{14}
\]

Thus the monomial Loewner matrix (7) is exactly the rational Loewner matrix sampled from `R` on the two cyclotomic node sets.

## 3. Coprimality plus the Bezoutian forces rank exactly `beta`

The rational representation in (8) is reduced. If `P` and `Q` had a common complex root `xi`, then (10) would force `xi^p=1`; but the node-regularity argument above shows that `Q` has no zero among the `p`-th roots. Hence

\[
\gcd(P,Q)=1.
\tag{15}
\]

Both polynomials have degree `beta`. Form their Bezoutian

\[
\mathcal B(X,Y)
=
\frac{P(X)Q(Y)-Q(X)P(Y)}{X-Y}.
\tag{16}
\]

It has degree at most `beta-1` in each variable, so in the monomial bases it has a `beta x beta` coefficient matrix `B`. The classical Bezout-resultant identity says that this matrix is nonsingular exactly when `P,Q` are coprime. Thus (15) gives

\[
\operatorname{rank}B=\beta.
\tag{17}
\]

For node sets `Z` and `W` of primitive `p`- and `q`-th roots, the rational Loewner matrix factors as

\[
L
=D_Z^{-1}V_Z B V_W^T D_W^{-1},
\tag{18}
\]

where `D_Z,D_W` are the nonzero diagonal matrices of denominator values and `V_Z,V_W` are the evaluation Vandermonde matrices with monomials `1,X,...,X^(beta-1)`.

It remains only to check that both node sets contain at least `beta` points. Since `q<2p`, integrality gives `q<=2p-1`; the endpoint `q=2p-1` is incompatible with the prescribed congruences modulo `3`, and parity then gives

\[
q\le2p-3.
\]

Therefore

\[
\beta=\frac{p+q}{3}\le p-1<q-1.
\tag{19}
\]

The two Vandermonde matrices have full column rank `beta`. Equation (18) therefore has rank exactly `beta`, proving (2). This proof uses the classical Loewner/Bezout machinery only after the special cyclotomic rational interpolant has been constructed explicitly.

## 4. The WI-086 defect is exactly `alpha-1`

For the parameters (1),

\[
\delta-(q-1)
=\frac{q(p-4)+p+3}{3}>0
\tag{20}
\]

because `p>=5`. Hence this family lies genuinely in WI-086's residual regime `delta>max(p-1,q-1)=q-1`.

WI-086 gives, with the smaller dimension `a=p-1`,

\[
\operatorname{rank}G=a-\tau.
\]

Substituting (2) yields (3):

\[
\tau=p-1-\beta
=\frac{2p-q-3}{3}
=\alpha-1.
\]

Exact regression examples are

\[
(11,13,47):\ (\beta,\tau)=(8,2),
\]
\[
(17,19,107):\ (\beta,\tau)=(12,4),
\]
\[
(23,31,235):\ (\beta,\tau)=(18,4),
\]
\[
(29,31,299):\ (\beta,\tau)=(20,8).
\]

Direct integer-incidence rank calculations reproduce these values, but they are now corollaries rather than evidence needed for the theorem.

## 5. The relative defect can approach one third unconditionally

The prime number theorem in arithmetic progressions modulo `3` supplies primes in each reduced residue class inside every fixed positive relative interval once the scale is large enough. For each `k`, choose a sufficiently large scale `X_k` and primes

\[
p_k\equiv2\pmod3,
\qquad
X_k<p_k<(1+1/(4k))X_k,
\]

\[
q_k\equiv1\pmod3,
\qquad
(1+1/(2k))X_k<q_k<(1+3/(4k))X_k.
\]

Then `p_k<q_k<2p_k` and

\[
\frac{q_k}{p_k}\to1.
\]

Applying (2)--(3),

\[
\frac{\beta_k}{p_k-1}
=
\frac{p_k+q_k}{3(p_k-1)}\to\frac23,
\]

and

\[
\frac{\tau_k}{p_k-1}
=
\frac{2p_k-q_k-3}{3(p_k-1)}\to\frac13.
\]

This is the decisive negative consequence. No modulus-uniform theorem can strengthen WI-086 by asserting that every residual close-prime pair has rank `p-1-o(p)` or transversality defect `o(p)`. Such a statement is contradicted by this explicit Loewner--Bezout family.

## 6. Prior art and novelty boundary

The algebraic tools are classical.

- A. C. Antoulas and B. D. O. Anderson, **On the Scalar Rational Interpolation Problem**, *IMA Journal of Mathematical Control and Information* 3 (1986), 61--88, DOI `10.1093/imamci/3.2-3.61`, is classical prior art for scalar rational interpolation organized by Loewner matrices and their ranks.
- A. C. Antoulas and B. D. O. Anderson, **State-space and Polynomial approaches to Rational Interpolation**, in *Realization and Modelling in System Theory*, gives the standard interpretation of Loewner rank as encoding admissible rational complexity.
- S. Barnett, **A Note on the Bezoutian Matrix**, *SIAM Journal on Applied Mathematics* 22 (1972), 84--86, DOI `10.1137/0122009`, is classical Bezoutian matrix prior art. The nonsingularity/resultant criterion for the Bezout matrix of two equal-degree polynomials is standard elimination theory.
- K. G. Ivanov, T. J. Rivlin and E. B. Saff, **The Representation of Functions in Terms of Their Divided Differences at Chebyshev Nodes and Roots of Unity**, *J. London Math. Soc.* 42 (1990), 309--328, DOI `10.1112/jlms/s2-42.2.309`, is prior art for divided differences on root-of-unity node sets.
- WI-081 supplies the exact nearest-LCM boundary factorization and the `(11,13,47)` rank-eight witness; WI-086 supplies the max-totient threshold and the exact transversality-defect normalization `tau`.

A targeted audit for combinations of Ramanujan subspaces/sums, cyclotomic primitive-node cross Grams, Loewner matrices, Bezoutians, and the three-term rational family above located the classical ingredients but no direct formulation of (1)--(4). That search result is **not** a priority claim. The durable claim here is only the exact derivation from established algebra plus the classical prime-number theorem in arithmetic progressions.

One subtle prior-art warning matters: general scalar rational interpolation does **not** permit the slogan `minimal rational degree = rank Loewner` without hypotheses; Antoulas--Anderson's general theory has multiple cases. The proof above deliberately avoids that shortcut. It obtains exact rank from the explicit reduced `P/Q`, the nonsingular Bezoutian, and full-rank Vandermonde evaluation factors.

## 7. Research consequence

The clue's proposed rational-interpolation explanation is supported, but the implication for the wider `weil_inertia` program is mostly a barrier rather than an immediate escape.

The residual pairwise defect `tau` is now known to have a concrete arithmetic mechanism and can be macroscopic. Therefore a continuation that merely tries to prove that primitive-frequency subspaces are generically or uniformly transverse cannot close the scalar signed-inertia problem. Any useful positive theorem must use information absent from arbitrary pairwise rank: actual source coefficients and signs, singular-value magnitudes, simultaneous consistency across several moduli, or a source representation retaining labels erased by the scalar quotient of WI-085.

This does not reopen the global scalar routes already obstructed by WI-082--WI-085 and does not itself improve the zeta-zero proportion. Its substantive value is to turn WI-086's abstract residual `tau` into an exact structured family and to close the tempting `tau=o(phi(p))` universal pairwise escape.
