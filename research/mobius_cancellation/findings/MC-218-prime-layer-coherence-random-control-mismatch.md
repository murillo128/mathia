# MC-218 — Prime-layer coherence is polynomially larger than the random square-defect calibration

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `MATCHED-CONTROL`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-217` gives an exact and useful matched-control calibration for the live square-defect energy: if the Möbius prime signs are replaced by independent Rademacher signs while preserving multiplicativity, rational-prime locations, square-free support, the primorial pre-sieve, and every lifted incidence `d^2 | n+q`, then each dyadic raw energy is at diagonal power scale in expectation.

That calibration does **not** preserve the cancellation mechanism of actual Möbius even on the first active square-defect shell. The mismatch is already polynomially large in the degree-one (prime) Walsh layer.

Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
q=\prod_{p\le y}p,
\qquad
T=X-q,
\tag{1}
\]

and consider the first root shell

\[
y<d\le2y,
\qquad \mu^2(d)=1,
\qquad(d,q)=1.
\tag{2}
\]

For sufficiently large `X`, every `d` in `(2)` is itself prime: every prime factor of `d` exceeds `y`, while a composite such `d` would exceed `y^2>2y`. Put

\[
P_d(X)
:=
\#\{p\le T:\ p\text{ prime},\ (p,q)=1,\ p\equiv-q\pmod{d^2}\}.
\tag{3}
\]

The degree-one contribution to the actual selected Möbius sum

\[
A_d(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\d^2\mid n+q}}\mu(n)
\tag{4}
\]

is exactly `-P_d(X)`, because every prime has Möbius value `-1`.

Since `d^2\ll (\log X)^2` and `(-q,d)=1`, the classical Siegel--Walfisz theorem gives uniformly on this shell

\[
\boxed{
P_d(X)
=(1+o(1))\frac{\operatorname{Li}(X)}{\varphi(d^2)}
=(1+o(1))\frac{\operatorname{Li}(X)}{d(d-1)}.
}
\tag{5}
\]

(The finitely many primes `p\le y` excluded by `(p,q)=1` contribute only a negligible error.) Therefore the weighted energy of the **prime layer alone** is

\[
\mathcal P_1(X)
:=
\sum_{\substack{y<d\le2y\\d\ {m prime}}}
 d\,P_d(X)^2.
\tag{6}
\]

Using the prime number theorem on the outer `d`-sum,

\[
\sum_{y<d\le2y\atop d\ {m prime}}\frac1{d^3}
\sim
\int_y^{2y}\frac{dt}{t^3\log t}
\sim
\frac{3}{8y^2\log y},
\tag{7}
\]

and hence

\[
\boxed{
\mathcal P_1(X)
\sim
\frac38\,
\frac{\operatorname{Li}(X)^2}{y^2\log y}
=
\left(\frac{3}{8c^2}+o(1)\right)
\frac{X^2}{(\log X)^4\log\log X}.
}
\tag{8}
\]

This is polynomially above the desired `MC-209` shell scale `X^{1+o(1)}`.

The same degree-one layer behaves completely differently in the Rademacher source of `MC-217`. Let

\[
L_d^\xi
:=
\sum_{\substack{p\le T\\(p,q)=1\\p\equiv-q\pmod{d^2}}}\xi_p.
\tag{9}
\]

Independence gives

\[
\mathbb E_\xi|L_d^\xi|^2=P_d(X),
\tag{10}
\]

so

\[
\boxed{
\mathbb E_\xi
\sum_{y<d\le2y\atop d\ {m prime}}
 d|L_d^\xi|^2
=
\sum_d dP_d(X)
\sim
(\log2)\frac{\operatorname{Li}(X)}{\log y}
\sim
(\log2)\frac{X}{\log X\log\log X}.
}
\tag{11}
\]

Comparing `(8)` and `(11)`,

\[
\boxed{
\frac{\mathcal P_1(X)}
{\mathbb E_\xi\sum_d d|L_d^\xi|^2}
=
\left(\frac{3}{8c^2\log2}+o(1)\right)
\frac{X}{(\log X)^3}.
}
\tag{12}
\]

Thus the random comparator obtains a polynomial factor of cancellation **before any interaction between different Hamming degrees occurs**: its prime contributions cancel among themselves because their signs are randomized. Actual Möbius has no such mechanism. Its entire prime layer points coherently in the same direction.

This gives a sharp necessary condition for the deterministic `MC-209` target. Define the non-prime remainder

\[
R_d(X):=A_d(T)+P_d(X).
\tag{13}
\]

It contains the possible degree-zero term `n=1` and all square-free composite terms `\omega(n)\ge2`. If the first-shell target

\[
W_y(X):=
\sum_{y<d\le2y\atop d\ {m prime}}
 d|A_d(T)|^2
\le X^{1+o(1)}
\tag{14}
\]

holds, then `(13)` gives the exact weighted identity

\[
\sum_d d|R_d(X)-P_d(X)|^2=W_y(X).
\tag{15}
\]

Together with `(8)`,

\[
\boxed{
\frac{
\left(\sum_d d|R_d-P_d|^2\right)^{1/2}}
{\left(\sum_d dP_d^2\right)^{1/2}}
\le X^{-1/2+o(1)}.
}
\tag{16}
\]

So diagonal-scale deterministic energy on the first shell requires the higher-degree square-free contribution to reproduce and cancel the coherent prime vector with **relative weighted `L^2` error `X^{-1/2+o(1)}`**. In particular,

\[
\sum_d dR_dP_d
=(1+o(1))\mathcal P_1(X),
\qquad
\sum_d dR_d^2
=(1+o(1))\mathcal P_1(X).
\tag{17}
\]

The all-minus source is therefore not merely an atypical sample of the `MC-217` ensemble in an abstract probabilistic sense. On the exact live incidence family, its first Walsh degree already has a coherent energy larger than the random degree-one energy by `X^{1-o(1)}`, and the desired theorem can hold only through an almost complete **cross-degree parity compensation**.

There is also an exact comparator-rigidity reason why this mismatch cannot be repaired while retaining the same multiplicative randomization class. Let `f` be any multiplicative function with

\[
f(n)=0\quad\text{for nonsquare-free }n,
\qquad
f(p)=-1\quad\text{for every prime }p\le T.
\tag{18}
\]

Then for every square-free `n\le T`,

\[
f(n)=\prod_{p\mid n}f(p)=(-1)^{\omega(n)}=\mu(n),
\tag{19}
\]

and hence `f(n)=\mu(n)` for all `n\le T`. Thus **a nontrivial square-free-supported multiplicative control cannot simultaneously preserve the exact Möbius prime layer and randomize the composite layers.** Random multiplicative controls necessarily give up the parity orientation whose cancellation is the deterministic question.

No estimate for the actual `W_y`, `A_d`, `M(X)`, or the zeta zero set is proved here.

## 1. Why the first active shell consists only of primes

Every active `d` in `(2)` is square-free and coprime to `q`. Since `q` contains every prime at most `y`, every prime divisor of `d` is larger than `y`. If `d` had at least two prime divisors, then

\[
d>y^2>2y
\]

for large `X`, contradicting `(2)`. Hence `d` is prime.

This makes the first shell unusually clean: the square modulus is `d^2` with `d\asymp\log X`, so the selected prime residue can be counted uniformly by classical primes-in-progressions theory without importing any zero information near the critical line.

## 2. Siegel--Walfisz makes the coherent prime layer explicit

For every shell prime `d`, the selected residue `-q mod d^2` is reduced because `d\nmid q`. Since `d^2\le4c^2(\log X)^2`, Siegel--Walfisz applies uniformly to the family of moduli and residues. Also

\[
q=e^{\vartheta(y)}=X^{c+o(1)},
\]

so `T=X-q=X(1+o(1))`. Partial summation gives `(5)`.

Substituting `(5)` into `(6)` gives

\[
\mathcal P_1(X)
=(1+o(1))\operatorname{Li}(X)^2
\sum_{y<d\le2y\atop d\ {m prime}}
\frac1{d(d-1)^2}.
\tag{20}
\]

The summand is `d^{-3}(1+O(1/d))`, and the PNT gives `(7)`, proving `(8)`.

For the random degree-one energy, `(10)` is exact. Equation `(5)` gives

\[
\sum_d dP_d(X)
=(1+o(1))\operatorname{Li}(X)
\sum_{y<d\le2y\atop d\ {m prime}}
\frac1{d-1}.
\tag{21}
\]

Mertens' theorem for reciprocal primes yields

\[
\sum_{y<d\le2y\atop d\ {m prime}}\frac1d
\sim
\frac{\log2}{\log y},
\tag{22}
\]

which proves `(11)`. Equation `(12)` follows immediately.

The use of Siegel--Walfisz here is far weaker than any RH-scale input. It is confined to moduli of size `O((log X)^2)` and only counts the degree-one prime shell.

## 3. The random model and Möbius cancel in different directions

For the Rademacher source

\[
f_\xi(n)=\mu^2(n)\prod_{p\mid n}\xi_p,
\]

Walsh orthogonality gives the full second-moment identity in `MC-217`. At degree one it reduces to the elementary random-walk identity `(10)`: distinct prime monomials are orthogonal.

For actual Möbius, however, every degree-one monomial is evaluated at the same deterministic cube vertex `\xi_p=-1`. The prime shell therefore has no internal cancellation at all. Any small value of `A_d` must come from cancellation **between different values of `\omega(n)`**, beginning with the positive square-free composite layers compensating the negative prime layer.

This distinction is not semantic. Equation `(12)` shows a polynomial separation on the live shell, and `(16)` quantifies how accurately the non-prime layers would have to compensate the prime vector if the raw-energy theorem is true.

The rigidity `(18)`--`(19)` explains why there is no obvious stronger multiplicative matched control between the two endpoints. In the square-free-supported multiplicative category, fixing the prime coordinates fixes the entire function. One can randomize prime signs and obtain the classical Rademacher model, or retain the Möbius prime signs and recover Möbius itself; there is no multiplicative interpolation that holds degree one fixed while independently randomizing higher Hamming degrees.

## 4. Prior art and novelty boundary

Rademacher random multiplicative functions are classical models for Möbius. `MC-217` records the standard Wintner lineage and modern literature and already warns that expectation over prime-sign assignments gives no pointwise estimate at the all-minus Möbius assignment. The present result sharpens that warning on the exact square-defect frontier by exhibiting a **polynomial quantitative mechanism mismatch in the first Hamming degree**.

The primes-in-progressions input is classical Siegel--Walfisz theory. The line's existing source `MC-S15` points to Montgomery--Vaughan's standard treatment of primes in arithmetic progressions; A. Page's classical paper *On the Number of Primes in an Arithmetic Progression*, Proc. London Math. Soc. (2) 39 (1935), 116--141, DOI `10.1112/plms/s2-39.1.116`, is an early primary-source anchor for the relevant uniform theory. No novelty is claimed for Siegel--Walfisz, the PNT, reciprocal-prime asymptotics, random-walk variance, or the multiplicative identity `(19)`.

There is also an internal prior-art boundary. `MC-105` proves in a different annular/Hamming functional that every fixed positive Hamming degree can carry a large classical Landau main term and that cancellation escapes to growing degree. The new mathematical delta here is not that Möbius parity alternates by `\omega(n)`. It is the specialization to the **current `MC-209` source-prescribed square-modulus energy**, where the degree-one layer can be evaluated uniformly and compared directly with the exact `MC-217` random calibration. That comparison yields the polynomial ratio `(12)` and the compensation condition `(16)`.

A targeted literature search found extensive work on random multiplicative functions, primes in arithmetic progressions, almost-prime/Hamming-degree distributions, and parity phenomena, but no need to posit a new general theorem for `(8)`--`(19)`. The finding is therefore a line-specific obstruction/filter built from classical mechanisms, not a novelty claim.

## 5. Boundaries and falsification tests

- The quantitative asymptotics `(5)`--`(12)` use only the first root shell `y<d\le2y`. They do not claim an analogous prime-layer formula uniformly up to `d\asymp\sqrt X`.
- The degree-one energy `(8)` is **not** a lower bound for the full deterministic energy `W_y`; cross-degree cancellation can make `A_d` much smaller. The point is precisely that such cancellation is mandatory if `(14)` holds.
- The term `n=1` is included in `R_d`; at most it contributes a degree-zero coordinate of size one and is negligible compared with `(8)`. No assumption about whether some `d^2` divides `q+1` is needed.
- The random comparison does not invalidate `MC-217`. That finding remains a valid power-scale calibration for the raw energy and lift incidence. The present result only shows that its random cancellation mechanism cannot be transferred to Möbius without new parity-sensitive information.
- The comparator rigidity `(19)` is limited to square-free-supported multiplicative controls. Nonmultiplicative, conditioned, or representation-level controls can preserve the prime layer while altering composites, but then they have given up one of the strongest structural matches of `MC-217` and must justify the replacement structure independently.
- A proof of `(14)` obtained by already assuming RH-quality Möbius cancellation is still circular. Equation `(16)` is a necessary consequence, not a cheaper proof of the compensation.

The exact asymptotic claim is falsified if Siegel--Walfisz does not give `(5)` uniformly for `d^2=O((log X)^2)`, if the dyadic prime sums in `(7)` or `(22)` have the stated asymptotics, or if the algebraic decomposition `A_d=R_d-P_d` does not lead to `(15)`--`(16)`. The structural interpretation is falsified if one exhibits a nontrivial square-free-supported multiplicative comparator that agrees with Möbius on every prime up to `T` but differs from Möbius somewhere below `T`, contradicting `(19)`.

## Consequence for the research line

`MC-217` localizes the post-gauge frontier to the deterministic all-minus prime-sign point. `MC-218` now shows exactly why that point is difficult in the current square-defect representation: **its prime layer is maximally coherent and already polynomially too large, whereas the matched random ensemble cancels that same layer internally.**

The next deterministic mechanism therefore cannot be justified by diagonal-scale random energy alone. It must control a source-specific cross-degree parity relation strong enough to compensate the coherent prime vector, or find a different representation in which this compensation is encoded by an independently estimable signed covariance rather than by pointwise Mertens cancellation. Any proposed random/moment transfer should first be tested against the ratio `(12)` and the rigidity `(19)`; if it uses cancellation already present in randomized prime signs, it has not reached the actual Möbius frontier.