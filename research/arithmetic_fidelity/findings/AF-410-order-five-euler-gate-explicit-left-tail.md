# AF-410 — The order-five Euler gate is explicitly positive for \(t\le-14\)

## Status

`EXACT-DERIVED` · `FINITE-ORDER-POSITIVE-GATE` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `TODA` · `EFFECTIVE-TAIL-BOUND` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
L(x):=-\log(1-e^{-x}),\qquad f(t):=L(e^t),\qquad x=e^t,
\]

and let

\[
H_4(t)=\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{3},
\qquad
A_4(t)=-(\log H_4(t))''
\]

be the fourth confluent determinant and the order-five Toda gate from AF-404/AF-408. Define

\[
N_4(t):=(H_4'(t))^2-H_4(t)H_4''(t),
\]

so that, wherever `H_4>0`,

\[
A_4(t)=\frac{N_4(t)}{H_4(t)^2}.
\]

Then for every `t<=-14`, writing `u=-t=-\log x`,

\[
\boxed{
N_4(t)>\frac{533}{1000}x^8>0.
}
\tag{1}
\]

AF-405 proves `H_4>0` on the whole real line. Therefore

\[
\boxed{
A_4(t)>0\qquad(t\le-14).
}
\tag{2}
\]

Together with AF-409, which proves `A_4(t)>0` for `t>=4`, this closes both effective tails around the independently frozen compact interval `[-14,4]`. The remaining order-five question is purely compact: certify or refute `A_4>0` on `[-14,4]`.

## 1. Separate the logarithmic coordinate from the analytic germ

Put

\[
u=-\log x,
\qquad
h(x):=-\log\!\left(\frac{1-e^{-x}}{x}\right).
\]

Then

\[
f(t)=u+h(x).
\]

The germ `h` is analytic for `|x|<2\pi` and has the Bernoulli expansion

\[
h(x)=\frac{x}{2}
-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\frac{x}{2}-\frac{x^2}{24}+\frac{x^4}{2880}-\frac{x^6}{181440}+\cdots.
\tag{3}
\]

Let

\[
E:=x\frac d{dx}.
\]

Since `d/dt=x\partial_x-\partial_u`, if `h_j:=E^j h`, then the derivative sequence entering `H_4` is

\[
F_0=u+h,
\qquad
F_1=-1+h_1,
\qquad
F_j=h_j\quad(j\ge2).
\tag{4}
\]

Only `F_0` contains `u`. Consequently `H_4` is affine in the logarithmic variable:

\[
H_4=u\,a(x)+b(x),
\tag{5}
\]

where

\[
a(x)=
\det
\begin{pmatrix}
h_2&h_3&h_4\\
h_3&h_4&h_5\\
h_4&h_5&h_6
\end{pmatrix},
\tag{6}
\]

and `b(x)` is the same `4x4` Hankel determinant with `u=0` in `(4)`.

This affine splitting is the useful left-tail normalization: it keeps the unbounded variable `u` explicit while all coefficient functions remain analytic on a fixed disk.

## 2. The curvature numerator is only quadratic in \(u\)

From `(5)`,

\[
H_4'=uEa+(Eb-a),
\]

and

\[
H_4''=uE^2a+(E^2b-2Ea).
\]

Hence

\[
N_4=n_0(x)+u\,n_1(x)+u^2n_2(x),
\tag{7}
\]

with analytic coefficient functions

\[
\begin{aligned}
n_0&=(Eb-a)^2-b(E^2b-2Ea),\\
n_1&=2(Ea)(Eb-a)-a(E^2b-2Ea)-bE^2a,\\
n_2&=(Ea)^2-aE^2a.
\end{aligned}
\tag{8}
\]

Direct coefficient extraction from the exact Bernoulli series `(3)` gives

\[
\boxed{
\begin{aligned}
n_0(x)
&=\frac{8}{15}x^8-\frac{32}{45}x^9-\frac{22}{105}x^{10}+O(x^{11}),\\
n_1(x)
&=\frac{4}{45}x^{10}+O(x^{11}),\\
n_2(x)&=O(x^{16}).
\end{aligned}}
\tag{9}
\]

These are coefficient statements about analytic functions, not asymptotic estimates that will be used without a remainder bound. The rest of the proof makes the three tails in `(9)` explicit.

For audit, the beginning of the combined exact expansion is

\[
N_4=
\frac{8}{15}x^8-rac{32}{45}x^9
+x^{10}\left(\frac{4u}{45}-\frac{22}{105}\right)
+O(x^{11})+uO(x^{11})+u^2O(x^{16}).
\tag{10}
\]

Dividing the leading term by `H_4^2~x^6/9` recovers AF-408's `A_4~24x^2/5`.

## 3. Uniform analytic bounds on the unit disk

The classical identity

\[
|B_{2k}|=
\frac{2(2k)!}{(2\pi)^{2k}}\,\zeta(2k)
\tag{11}
\]

turns `(3)` into an elementary absolute majorant. Since `\zeta(2k)<2` and `2\pi>6`, for `|z|=1` one obtains

\[
|E^j h(z)|
\le
\frac12+2^{j+1}\sum_{k\ge1}\frac{k^{j-1}}{36^k}
\qquad(j\ge1),
\tag{12}
\]

with the analogous `k^{-1}` sum for `j=0`. Evaluating the elementary geometric power sums gives the convenient integer bounds

\[
\boxed{
(|h_0|,|h_1|,\ldots,|h_8|)
\le(1,1,1,1,2,4,8,25,96)
\quad(|z|=1).
}
\tag{13}
\]

Expanding a determinant by permutations and differentiating its product terms gives, very crudely but sufficiently,

\[
\begin{aligned}
|a|&\le3072,& |Ea|&\le28800,& |E^2a|&\le290592,\\
|b|&\le98304,& |Eb|&\le1228800,& |E^2b|&\le16238592.
\end{aligned}
\tag{14}
\]

For example, `a` has six three-factor terms with factors bounded by `8`; one `E` produces at most `18` terms with one factor bounded by `25`; and two `E` derivatives produce the corresponding second-derivative and pairwise first-derivative terms bounded by `96` and `25`. The `4x4` determinant `b` is bounded in the same way.

Substitution in `(8)` yields the uniform circle bounds

\[
\boxed{
|n_0|<4\cdot10^{12},
\qquad
|n_1|<2\cdot10^{11},
\qquad
|n_2|<2\cdot10^9
\quad(|z|=1).
}
\tag{15}
\]

The unrounded estimates behind `(15)` are respectively

\[
3{,}119{,}489{,}482{,}752,
\quad
149{,}584{,}084{,}992,
\quad
1{,}722{,}138{,}624.
\]

Thus Cauchy's coefficient estimate, combined with the exact vanishing orders in `(9)`, gives for every real `0<x<1`

\[
\begin{aligned}
\left|n_0-\left(\frac8{15}x^8-\frac{32}{45}x^9-\frac{22}{105}x^{10}\right)\right|
&\le\frac{4\cdot10^{12}x^{11}}{1-x},\\
\left|n_1-\frac4{45}x^{10}\right|
&\le\frac{2\cdot10^{11}x^{11}}{1-x},\\
|n_2|&\le\frac{2\cdot10^9x^{16}}{1-x}.
\end{aligned}
\tag{16}
\]

This is the quantified remainder control missing from AF-408.

## 4. The cutoff \(t=-14\) has an enormous margin

For `t<=-14`, put `u=-t>=14` and `x=e^{-u}`. Then

\[
x<10^{-6},
\qquad
ux^3=ue^{-3u}\le14e^{-42}<14\cdot10^{-18},
\tag{17}
\]

because `ue^{-3u}` is decreasing for `u>=14`. Likewise

\[
u^2x^8=u^2e^{-8u}\le196e^{-112}<196\cdot10^{-48}.
\tag{18}
\]

Also `(1-x)^{-1}<2`. Divide `(7)` by `x^8`, use `(16)`, and discard the positive explicit term `(4u/45)x^2`. We obtain

\[
\begin{aligned}
\frac{N_4}{x^8}
>&\frac8{15}
-\frac{32}{45}10^{-6}
-\frac{22}{105}10^{-12}\\
&-2\left(
4\cdot10^{12}\cdot10^{-18}
+2\cdot10^{11}\cdot14\cdot10^{-18}
+2\cdot10^9\cdot196\cdot10^{-48}
\right)\\
>&0.533.
\end{aligned}
\tag{19}
\]

This proves `(1)` and hence `(2)`.

The constants are intentionally loose. The point is not to optimize the cutoff: at `x=e^{-14}` the analytic remainder is already many orders smaller than the positive `8x^8/15` numerator term. The previous existential left-tail statement can therefore be made effective without delicate cancellation estimates.

## Arithmetic-fidelity interpretation

AF-408 showed that the next possible loss of finite-order sign fidelity cannot occur asymptotically, but its left statement was only existential. AF-410 upgrades that qualitative statement to a concrete preservation theorem on the entire left semi-axis `t<=-14`.

The proof also isolates a reusable mechanism. When a compression certificate contains an unbounded logarithmic coordinate plus an analytic germ, it can be advantageous to split the certificate polynomially in the unbounded coordinate and apply analytic coefficient bounds only to the germ. Here `H_4` is affine in `u`, so its log-curvature numerator is quadratic in `u`; the exponentially small factor `x=e^{-u}` then dominates all polynomial `u` growth uniformly.

This remains a theorem about the universal one-generator Euler-log kernel, not about the rational primes. It supplies no arithmetic discriminator and no RH implication. Its role in the line is to finish the effective tail reduction for the order-five fidelity gate.

## Prior-art and novelty audit

The Bernoulli expansion and identity `(11)` are classical; NIST DLMF Chapter 24 records the Bernoulli generating-function and Fourier/zeta formulas used for the coefficient majorant. The determinant/Toda reduction and translation-kernel total-positivity machinery were already audited in AF-403/AF-404.

A fresh search after the claim was made precise found general results on totally positive Hankel matrices and recent moment-representation criteria for Hankel total positivity, but no theorem that supplies the concrete left cutoff for this Euler-log gate. Relevant neighboring literature includes Mainar, Peña and Rubio, *Total positivity and high relative accuracy for several classes of Hankel matrices* (Numerical Linear Algebra with Applications, 2024), and Salazar, *Order-Moment Transport and Hankel Determinants in Special-Function Inequalities* (arXiv:2606.31647, 2026). Neither replaces the explicit coefficient argument above. No novelty claim is made for the elementary specialization.

Sources:

- NIST DLMF, Chapter 24, Bernoulli and Euler Polynomials: https://dlmf.nist.gov/24
- NIST DLMF §24.8, Fourier/zeta formula for even Bernoulli numbers: https://dlmf.nist.gov/24.8
- E. Mainar, J. M. Peña, B. Rubio, *Total positivity and high relative accuracy for several classes of Hankel matrices*, DOI 10.1002/nla.2550.
- D. S. P. Salazar, *Order-Moment Transport and Hankel Determinants in Special-Function Inequalities*, arXiv:2606.31647.

## Boundaries and falsification checks

- The proof uses AF-405's global `H_4>0`. The new work is the explicit sign of its log-curvature numerator on `t<=-14`.
- No finite sampling or floating-point sign decision enters `(1)`; the only finite algebra is exact coefficient extraction from the Bernoulli series, followed by explicit analytic majorants.
- The Cauchy bounds are deliberately coarse. Improving them may move the cutoff rightward, but no such improvement is needed to meet `-14`.
- AF-410 does not prove the accepted compact monotonicity clue. The interval `[-14,4]` still requires a separate rigorous positivity or monotonicity certificate.
- Combining AF-410 and AF-409 proves positivity only outside `[-14,4]`; it does not by itself prove global order-five total positivity.
- AF-217 still forces failure at some finite order even if the compact order-five gate is eventually certified positive.
- No rational-prime discriminator is created, and no RH consequence follows without a separate arithmetic source theorem.

## Consequence for the research line

`CLUE-effective-order-five-tail-cutoffs.md` is now resolved: both tails meet the exact endpoints of the frozen compact window. There is no longer any hidden asymptotic bridge in the order-five program.

The only remaining order-five sign problem is the compact one already isolated by `CLUE-order-five-gate-monotonicity.md`: prove or refute `A_4>0` on `[-14,4]`, with monotonicity `A_4'\ge0` as one sufficient route. If that compact gate is certified, AF-403/AF-404 upgrade the full Euler-log translation kernel from strict total positivity through order four to strict total positivity through order five.