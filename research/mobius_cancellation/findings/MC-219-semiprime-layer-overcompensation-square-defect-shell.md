# MC-219 — The semiprime layer overcompensates the coherent prime layer on the first square-defect shell

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-218` shows that on the first active square-defect shell the degree-one Möbius layer is a coherent negative prime vector whose weighted energy is polynomially above the `MC-209` diagonal target. The first higher Hamming degree does not repair that mismatch. It **overcompensates it by a factor tending to infinity**.

Keep the `MC-218` regime

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

and let

\[
y<d\le2y,
\qquad d\text{ prime}.
\tag{2}
\]

Put `a_d=-q mod d^2`. As in `MC-218`, define the degree-one count

\[
P_d(X)
:=
\#\{p\le T:\ p\text{ prime},\ (p,q)=1,\ p\equiv a_d\pmod{d^2}\}.
\tag{3}
\]

The degree-one contribution to

\[
A_d(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a_d\pmod{d^2}}}\mu(n)
\tag{4}
\]

is `-P_d(X)`.

Now let

\[
Q_d(X)
:=
\#\{n\le T:\ n=pr,\ y<p<r\text{ prime},\ pr\equiv a_d\pmod{d^2}\}.
\tag{5}
\]

Because `(n,q)=1` forces every prime factor of a contributing square-free `n` to exceed `y`, `Q_d` is exactly the `\omega(n)=2` contribution to `(4)`, with positive Möbius sign.

Define

\[
L_X
:=
\log\!\left(\frac{\log T-\log y}{\log y}\right)
=
\log\log X-\log\log\log X+o(1).
\tag{6}
\]

Then uniformly for every prime `d` in `(2)`,

\[
\boxed{
Q_d(X)
=
\left(L_X+O(1)\right)
\frac{T}{\varphi(d^2)\log T}
=
\left(L_X+O(1)\right)P_d(X).
}
\tag{7}
\]

In particular `L_X\to\infty`, so the signed degree-one-plus-degree-two contribution

\[
C_d(X):=-P_d(X)+Q_d(X)
\tag{8}
\]

is eventually positive for every shell modulus and satisfies

\[
\boxed{
C_d(X)=\left(L_X+O(1)\right)P_d(X).
}
\tag{9}
\]

Thus degree two does not merely cancel the coherent prime layer. It reverses the sign and leaves a residual vector larger than the original prime vector by the slowly diverging factor `L_X`.

Let

\[
\mathcal P_1(X)
:=
\sum_{y<d\le2y\atop d\text{ prime}}d\,P_d(X)^2.
\tag{10}
\]

`MC-218` proves

\[
\mathcal P_1(X)
\sim
\frac{3}{8c^2}
\frac{X^2}{(\log X)^4\log\log X}.
\tag{11}
\]

Equations `(7)`--`(9)` therefore give the first-two-degree energy

\[
\boxed{
\sum_{y<d\le2y\atop d\text{ prime}}
 d\,C_d(X)^2
\sim
\frac{3}{8c^2}
\frac{L_X^2X^2}{(\log X)^4\log\log X}.
}
\tag{12}
\]

This sharpens the compensation obligation from `MC-218`. Write

\[
H_d(X):=A_d(T)-C_d(X),
\tag{13}
\]

so `H_d` contains the possible degree-zero term `n=1` and all square-free terms with `\omega(n)\ge3`. If the first-shell `MC-209` target

\[
W_y(X)
:=
\sum_{y<d\le2y\atop d\text{ prime}}
 d|A_d(T)|^2
\le X^{1+o(1)}
\tag{14}
\]

holds, then exactly

\[
\sum_d d|H_d(X)+C_d(X)|^2=W_y(X).
\tag{15}
\]

Combining `(12)` and `(14)`,

\[
\boxed{
\frac{
\left(\sum_d d|H_d+C_d|^2\right)^{1/2}}
{
\left(\sum_d dC_d^2\right)^{1/2}}
\le X^{-1/2+o(1)}.
}
\tag{16}
\]

Hence any diagonal-scale theorem must force the degree-`>=3` tail to reproduce **the negative of the already overcompensated first-two-degree vector** with relative weighted `L^2` error `X^{-1/2+o(1)}`. The required cancellation is therefore not a prime-versus-composite balance localized at degree two. It has already become a cross-degree cascade on the first square-defect shell.

No estimate for the actual `W_y`, `A_d`, `M(X)`, or the zeta zero set is proved here.

## 1. Exact semiprime decomposition

Every square-free semiprime counted by `(5)` has a unique ordering `p<r`, hence `p\le\sqrt T`. Conversely, for every prime

\[
y<p\le\sqrt T,
\qquad p\ne d,
\tag{17}
\]

the residue condition `pr\equiv a_d mod d^2` is equivalent to

\[
r\equiv a_d\bar p\pmod{d^2}.
\tag{18}
\]

The case `p=d` cannot contribute because `a_d=-q` is coprime to `d`. Therefore

\[
\boxed{
Q_d(X)
=
\sum_{\substack{y<p\le\sqrt T\\p\text{ prime}\\p\ne d}}
\left[
\pi\!\left(\frac Tp;d^2,a_d\bar p\right)
-
\pi\!\left(p;d^2,a_d\bar p\right)
\right].
}
\tag{19}
\]

The subtraction enforces `r>p`, so prime squares are excluded exactly rather than corrected asymptotically.

## 2. Siegel--Walfisz evaluates the upper endpoint uniformly

On the first shell,

\[
d^2\ll(\log X)^2.
\tag{20}
\]

For every `p\le\sqrt T`, the upper endpoint `T/p` is at least `\sqrt T`. Hence `d^2` lies in the Siegel--Walfisz range for `T/p` with room to spare. For any fixed large `B`, uniformly in `p`, `d`, and the reduced residue in `(18)`,

\[
\pi\!\left(\frac Tp;d^2,a_d\bar p\right)
=
\frac{\operatorname{Li}(T/p)}{\varphi(d^2)}
+O_B\!\left(\frac{T/p}{(\log X)^B}\right).
\tag{21}
\]

Summing the errors over `p` costs only reciprocal-prime mass and is negligible compared with the main term below after taking `B` sufficiently large.

The lower endpoints in `(19)` need no fine prime-distribution theorem. A residue class modulo `d^2` contains at most `p/d^2+1` integers up to `p`, so

\[
\sum_{y<p\le\sqrt T}
\pi(p;d^2,a_d\bar p)
\ll
\frac1{d^2}\sum_{p\le\sqrt T}p
+\pi(\sqrt T)
\ll
\frac{T}{d^2\log T}
+rac{\sqrt T}{\log T}.
\tag{22}
\]

Since `\varphi(d^2)\asymp d^2` and `L_X\to\infty`, `(22)` is `o(TL_X/(\varphi(d^2)\log T))` uniformly on the shell.

The omitted outer prime `p=d` changes the main sum by at most `O(T/(d\log T))` before division by `\varphi(d^2)`, again negligible relative to the factor `L_X` main term.

## 3. Reciprocal-prime mass creates the diverging factor

It remains to evaluate

\[
S(T,y)
:=
\sum_{y<p\le\sqrt T}\operatorname{Li}(T/p).
\tag{23}
\]

Put `U=\log T`. Uniformly for `p\le\sqrt T`,

\[
\operatorname{Li}(T/p)
=
\frac{T}{p(U-\log p)}
+O\!\left(\frac{T}{p(U-\log p)^2}\right).
\tag{24}
\]

Mertens' theorem for reciprocal primes, followed by partial summation, gives

\[
\sum_{y<p\le\sqrt T}
\frac1{p(U-\log p)}
=
\frac1U
\left[
\log\!\left(\frac{U-\log y}{\log y}\right)+O(1)
\right].
\tag{25}
\]

The main integral behind `(25)` is elementary:

\[
\int_y^{\sqrt T}
\frac{dt}{t\log t\,(U-\log t)}
=
\frac1U
\log\!\left(\frac{U-\log y}{\log y}\right).
\tag{26}
\]

The error term in `(24)` contributes `O(TL_X/U^2)`, lower order. Thus

\[
\boxed{
S(T,y)
=
\frac{T}{\log T}\left(L_X+O(1)\right).
}
\tag{27}
\]

Substituting `(21)`, `(22)`, and `(27)` into `(19)` proves

\[
Q_d(X)
=
\frac{T}{\varphi(d^2)\log T}
\left(L_X+O(1)\right)
\tag{28}
\]

uniformly for all first-shell `d`.

`MC-218` already gives

\[
P_d(X)
=(1+o(1))\frac{T}{\varphi(d^2)\log T}
\tag{29}
\]

on the same shell. Equations `(7)`--`(9)` follow.

## 4. The first two degrees force an even larger tail compensation

The key point is the sign. Möbius contributes `-1` on every prime and `+1` on every square-free semiprime. Equation `(7)` says that the second layer is not of comparable size to the first: it is larger by

\[
L_X
=
\log\log X-\log\log\log X+o(1).
\tag{30}
\]

Thus the first two signed layers already point coherently in the **opposite** direction from the prime layer, with magnitude `L_XP_d(1+o(1))`.

Because the ratio `(7)` is uniform in `d`, squaring and summing with weight `d` gives

\[
\sum_d dC_d^2
=(L_X^2+O(L_X))\mathcal P_1(X),
\tag{31}
\]

which together with `MC-218` proves `(12)`. Equation `(16)` is then just the exact decomposition `A_d=C_d+H_d` measured in the same weighted Hilbert norm used by `MC-209`.

This is stronger than saying that some higher-degree mass must exist. If `(14)` is true, the degree-`>=3` vector must be anti-aligned with `C=(C_d)_d` to square-root relative accuracy. Any approach that bounds the degree-`>=3` tail only by magnitude, or treats degree two as the final compensating shell, has therefore lost the required sign geometry.

## 5. Prior art and novelty boundary

Counting products of two primes in arithmetic progressions is classical. Heath-Brown, *Almost-primes in arithmetic progressions and short intervals*, Math. Proc. Cambridge Philos. Soc. 83 (1978), 357--375, studies almost-primes in progressions in substantially more difficult parameter ranges. Dummit, Granville and Kisilevsky, *Big biases amongst products of two primes*, Mathematika 62 (2016), 502--507, DOI `10.1112/S0025579315000339`, shows that semiprime residue classes can carry lower-order arithmetic biases. Neither is used here as a new theorem claim.

The present asymptotic needs only the classical ingredients already retained by this line: Siegel--Walfisz/PNT in arithmetic progressions (`MC-S15`) and reciprocal-prime Mertens asymptotics (`MC-S6`). The modulus is only `d^2=O((log X)^2)`, so `(19)`--`(28)` are an elementary polylog-modulus specialization rather than a new almost-primes-in-progressions theorem. The known semiprime-bias literature is also compatible with `(7)`: such biases are lower-order relative to the leading equidistributed semiprime mass used here.

There is an internal prior-art boundary as well. `MC-097` proves a positive degree-two main term for the earlier Huxley--Watt radial functional, and `MC-105` proves that every fixed degree in that **different functional** can carry a growing Landau main term, forcing endpoint cancellation into growing Hamming degree. `MC-218` explicitly identified that analogy but did not evaluate degree two on the current source-prescribed square-modulus shell.

The mathematical delta here is therefore narrow and line-specific: on the exact `MC-209` first shell, the semiprime coordinate can be evaluated uniformly, its ratio to the already-audited prime coordinate is the diverging quantity `L_X`, and the diagonal-energy hypothesis forces the remaining degree-`>=3` tail to cancel the resulting enlarged vector as in `(16)`. No novelty is claimed for semiprime counting, Siegel--Walfisz, Landau-type almost-prime growth, or the existence of cross-degree parity cancellation in other representations.

## 6. Boundaries and falsification tests

- The result is confined to the first active shell `y<d\le2y`, where `d` is prime and `d^2` is polylogarithmic. It does not claim `(7)` uniformly for root moduli approaching `X^{1/2}`.
- `Q_d` counts **square-free** semiprimes with distinct factors. Prime squares are removed exactly by the lower endpoint in `(19)` and do not contribute to Möbius.
- The asymptotic `(7)` is a positive counting statement. It does not itself provide cancellation for `A_d`; its purpose is the opposite, to quantify how much alternating cross-degree cancellation remains necessary.
- Equation `(12)` is not a lower bound for the full energy `W_y`; degree `>=3` terms may cancel `C_d`. Equation `(16)` states the precise compensation they would have to supply if the target holds.
- Lower-order semiprime race biases do not change the conclusion because `L_X\to\infty` and `(7)` only needs the leading term uniformly at polylogarithmic modulus.
- No inference from the earlier radial Hamming findings is used as evidence for `(7)`. The square-modulus progression count is derived independently above.
- A proof of `(14)` that assumes RH-quality Möbius cancellation remains circular; the semiprime asymptotic only sharpens the necessary source-side structure.

The exact result is falsified if the counting identity `(19)` fails, if Siegel--Walfisz cannot be applied uniformly to the upper endpoints `T/p\ge\sqrt T` at modulus `d^2=O((log X)^2)`, if the elementary lower-endpoint bound `(22)` is not negligible against the main term, or if Mertens partial summation does not yield `(25)`--`(27)`. The frontier interpretation is falsified if the first-shell diagonal target can hold while the degree-`>=3` tail fails the weighted approximation `(16)`, which would contradict the exact decomposition `(13)`--`(15)`.

## Consequence for the research line

`MC-218` showed that diagonal-scale energy cannot come from random-like cancellation inside the deterministic prime layer. `MC-219` now shows that the obvious next repair is also structurally wrong: **degree two does not balance degree one; it overshoots it by `L_X\to\infty`.**

The live question should therefore be treated as a genuine growing-degree source problem. The next useful theorem surface is not another random-sign calibration or a two-layer covariance estimate, but a source-forced recurrence or asymptotic across several consecutive square-free degrees on the same lifted residue family. A particularly sharp continuation is to determine how far the ratio pattern in `(7)` persists with `\omega(n)=k` as `k` grows, and whether the onset of cancellation occurs only near a moving degree comparable to the rough almost-prime saddle rather than at any bounded Hamming depth.