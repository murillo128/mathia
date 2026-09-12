# MC-230 — Exact first-shell incidence cells cost only subpower entropy, so cross-cell anti-alignment is not power-essential

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the first square-defect shell of `MC-209` and `MC-221`--`MC-229`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
\mathcal D_y=\{d:\ y<d\le2y,\ d\text{ prime}\},
\qquad
\mathcal R_d=\{n\le T:(n,P)=1,\ n\equiv-P\pmod{d^2}\}.
\]

For every rough input `n<=T`, define its exact shell-incidence set

\[
I_y(n):=\{d\in\mathcal D_y:d^2\mid n+P\}.
\tag{1}
\]

For every nonempty `S\subseteq\mathcal D_y`, let

\[
\mathcal E_S
:=
\{n\le T:(n,P)=1,\ I_y(n)=S\},
\qquad
C_S(X):=\sum_{n\in\mathcal E_S}\mu(n),
\tag{2}
\]

and put

\[
w(S):=\sum_{d\in S}d.
\tag{3}
\]

The cells `\mathcal E_S` partition the union of the selected shell supports. Therefore every shell coordinate has the exact decomposition

\[
\boxed{
A_d(T)
:=\sum_{n\in\mathcal R_d}\mu(n)
=
\sum_{S\ni d} C_S(X).
}
\tag{4}
\]

The first-shell target energy is

\[
W_y(X)=\sum_{d\in\mathcal D_y}d|A_d(T)|^2.
\tag{5}
\]

Define the **exact-cell diagonal energy**

\[
\boxed{
\mathcal C_y(X)
:=
\sum_{\varnothing\ne S\subseteq\mathcal D_y}
w(S)|C_S(X)|^2.
}
\tag{6}
\]

Then

\[
\boxed{
W_y(X)
\le
(2^{|\mathcal D_y|}-1)\,\mathcal C_y(X)
=
X^{o(1)}\mathcal C_y(X).
}
\tag{7}
\]

Indeed the prime number theorem gives

\[
|\mathcal D_y|
=(c+o(1))\frac{\log X}{\log\log X},
\qquad
2^{|\mathcal D_y|}=X^{o(1)}.
\tag{8}
\]

Consequently the sufficient theorem surface

\[
\boxed{
\mathcal C_y(X)\le X^{1+o(1)}
}
\tag{9}
\]

already implies the desired first-shell bound

\[
W_y(X)\le X^{1+o(1)}.
\tag{10}
\]

This removes one apparent obligation left by `MC-228`--`MC-229` and summarized in `MI-017`: **fixed-power progress does not require anti-alignment between different exact incidence cells.** All cross-cell terms may be discarded by Cauchy--Schwarz at a cost of only `X^{o(1)}` because the entire shell-incidence alphabet has subpolynomial cardinality. What remains genuinely necessary for this route is signed cancellation *inside* the low/mesoscopic exact cells, or some alternative mechanism that controls `(5)` more directly.

The same quarter threshold from `MC-229` survives at the stronger exact-cell level. For fixed `0<\alpha<c`, set

\[
r_\alpha(X)
=
\left\lceil
\alpha\frac{\log X}{\log\log X}
\right\rceil
\tag{11}
\]

and define

\[
\mathcal C_y^{\ge\alpha}(X)
:=
\sum_{|S|\ge r_\alpha(X)}w(S)|C_S(X)|^2.
\tag{12}
\]

Then support alone gives

\[
\boxed{
\mathcal C_y^{\ge\alpha}(X)
\le X^{2-4\alpha+o(1)}.
}
\tag{13}
\]

Hence, when `c>1/4`,

\[
\boxed{
\mathcal C_y^{\ge1/4}(X)
\le X^{1+o(1)}.
}
\tag{14}
\]

So the entire high-incidence exact-cell sector may be diagonalized and bounded without Möbius cancellation. Combining `(7)` and `(14)`, a sufficient remaining target is only

\[
\boxed{
\sum_{0<|S|<r_{1/4}(X)}
w(S)|C_S(X)|^2
\le X^{1+o(1)}.
}
\tag{15}
\]

The matched Rademacher multiplicative control shows that `(9)` is not generically overconstrained by the incidence geometry. Give each rational prime an independent Rademacher sign `\xi_p` and put

\[
f_\xi(n)=\mu^2(n)\prod_{p\mid n}\xi_p.
\tag{16}
\]

For

\[
C_S^\xi:=\sum_{n\in\mathcal E_S}f_\xi(n),
\]

square-free prime-support characters are orthogonal, so exactly

\[
\mathbb E_\xi |C_S^\xi|^2
=
N_S,
\tag{17}
\]

where

\[
N_S:=\#\{n\in\mathcal E_S:\mu^2(n)=1\}.
\]

Therefore

\[
\boxed{
\mathbb E_\xi\mathcal C_y^\xi
=
\sum_S w(S)N_S
=
\sum_{d\in\mathcal D_y}dN_d(T),
}
\tag{18}
\]

with `N_d(T)` from `MC-221`. Its established first-shell asymptotic gives

\[
\boxed{
\mathbb E_\xi\mathcal C_y^\xi
\sim
 e^{-\gamma}(\log 2)
\frac{X}{(\log\log X)^2}.
}
\tag{19}
\]

Thus the exact-cell diagonalization sits at diagonal power scale for the matched random multiplicative source. The unresolved issue is deterministic Möbius parity inside the low-incidence cells, not a combinatorial explosion of cell types and not a probabilistic necessity for cancellation between different cells.

No estimate `(9)` or `(15)` for the deterministic Möbius function is proved. No improved bound for `W_y`, `M(X)`, or the zeta zero set follows by itself.

## 1. The shell energy is a subpower sum of exact incidence vectors

Let `\mathcal H_y` be the coordinate space indexed by `\mathcal D_y` with weighted norm

\[
\|v\|_y^2
:=
\sum_{d\in\mathcal D_y}d|v_d|^2.
\tag{20}
\]

For a nonempty incidence set `S`, let `\mathbf 1_S` be its coordinate indicator. Equation `(4)` is the vector identity

\[
(A_d(T))_{d\in\mathcal D_y}
=
\sum_{\varnothing\ne S\subseteq\mathcal D_y}
C_S\mathbf 1_S.
\tag{21}
\]

Moreover

\[
\|C_S\mathbf 1_S\|_y^2
=w(S)|C_S|^2.
\tag{22}
\]

If `N_y` denotes the number of nonempty cells that occur, then

\[
N_y\le2^{|\mathcal D_y|}-1.
\tag{23}
\]

Cauchy--Schwarz in `\mathcal H_y` gives

\[
\left\|\sum_S C_S\mathbf 1_S\right\|_y^2
\le
N_y\sum_S\|C_S\mathbf 1_S\|_y^2,
\tag{24}
\]

which is `(7)` once `(8)` is inserted.

The factor in `(24)` is large in absolute terms but negligible on the polynomial scale relevant to the line:

\[
\log N_y
\le |\mathcal D_y|\log2
=O\!\left(\frac{\log X}{\log\log X}\right)
=o(\log X).
\tag{25}
\]

This is the crucial feature of the first shell. Replacing each integer input by its full shell-incidence word loses no fixed power because that word has only `|\mathcal D_y|=o(\log X)` bits.

Equation `(24)` is one-sided. Large cross-cell anti-alignment may make the true `W_y` much smaller than `\mathcal C_y`, so `(9)` is sufficient rather than necessary. The useful conclusion is exactly that such anti-alignment need not be proved if one can instead establish diagonal-scale signed control of the exact cells.

## 2. The high-incidence exact cells are already support-harmless

Fix a nonempty `S\subseteq\mathcal D_y` with `s=|S|` and write

\[
Q_S:=\prod_{d\in S}d^2.
\tag{26}
\]

By definition

\[
\mathcal E_S\subseteq\bigcap_{d\in S}\mathcal R_d.
\tag{27}
\]

The exact CRT description from `MC-229` therefore gives the simple upper bound

\[
|\mathcal E_S|
\le
\frac{X}{Q_S}
\le
\frac{X}{y^{2s}}.
\tag{28}
\]

Since `|\mu|\le1`,

\[
|C_S|\le\frac{X}{y^{2s}},
\tag{29}
\]

while

\[
w(S)\le2ys.
\tag{30}
\]

For a fixed degree `s`, equations `(29)`--`(30)` imply

\[
\sum_{|S|=s}w(S)|C_S|^2
\le
2ys\binom{|\mathcal D_y|}{s}
\frac{X^2}{y^{4s}}.
\tag{31}
\]

Now take `s\ge r_\alpha(X)`. The number of shell subsets, the factor `ys`, and the number of possible values of `s` are all `X^{o(1)}`, whereas

\[
y^{4r_\alpha(X)}
=X^{4\alpha+o(1)}.
\tag{32}
\]

Summing `(31)` over `s\ge r_\alpha(X)` proves `(13)`.

This strengthens the interpretation of `MC-229`. That finding showed directly that the **coordinate energy** contributed by all high-incidence integers is harmless above the quarter threshold. The present calculation shows that even after all cross-cell interference is erased, the **diagonal exact-cell energy** remains harmless there. The hard part is therefore genuinely confined to signed low/mesoscopic cells.

## 3. The matched random source places the cell energy at the natural diagonal scale

For square-free `n`, the Rademacher multiplicative source `(16)` is the prime-support character

\[
f_\xi(n)=\prod_{p\mid n}\xi_p.
\]

If `m` and `n` are distinct square-free integers, their prime-support sets differ, so at least one independent Rademacher variable occurs to an odd power in

\[
f_\xi(m)f_\xi(n).
\]

Hence

\[
\mathbb E_\xi[f_\xi(m)f_\xi(n)]
=
\mathbf 1_{m=n}.
\tag{33}
\]

Applying `(33)` inside one exact cell proves `(17)`. Summing with the incidence weight gives

\[
\sum_S w(S)N_S
=
\sum_{\substack{n\le T\\(n,P)=1\\\mu^2(n)=1}}
\sum_{d\in I_y(n)}d.
\tag{34}
\]

Interchanging the finite sums,

\[
\sum_S w(S)N_S
=
\sum_{d\in\mathcal D_y}d
\#\{n\in\mathcal R_d:\mu^2(n)=1\}
=
\sum_{d\in\mathcal D_y}dN_d(T),
\tag{35}
\]

which proves `(18)`. Equation `(19)` is then exactly the random-control asymptotic already derived in `MC-221`.

A convenient deterministic interpretation is to write, when `N_S>0`,

\[
\beta_S:=\frac{C_S}{N_S}.
\tag{36}
\]

Then

\[
\mathcal C_y
=
\sum_S w(S)N_S^2|\beta_S|^2,
\tag{37}
\]

while the random second-moment baseline is

\[
\sum_S w(S)N_S.
\tag{38}
\]

Thus the new sufficient target asks for a weighted aggregate parity bias whose squared cell sum remains within subpolynomial amplification of the natural diagonal count. It does not ask for independence of the Möbius signs, a Gaussian law, or pointwise square-root cancellation in every cell.

## 4. Exact cells are a Boolean-lattice refinement, not a new sieve identity

For completeness, define the signed partial-intersection sums

\[
J_U
:=
\sum_{n\in\cap_{d\in U}\mathcal R_d}\mu(n)
\qquad(\varnothing\ne U\subseteq\mathcal D_y).
\tag{39}
\]

Since an input in exact cell `S` lies in the intersection indexed by `U` exactly when `U\subseteq S`,

\[
J_U=\sum_{S\supseteq U}C_S.
\tag{40}
\]

Ordinary inclusion--exclusion, equivalently Möbius inversion on the finite Boolean lattice, gives

\[
C_S
=
\sum_{U\supseteq S}
(-1)^{|U|-|S|}J_U.
\tag{41}
\]

For each `U`, `MC-229` already gives the exact CRT parameterization of the intersection as one source-prescribed progression

\[
n=kQ_U-P,
\qquad
Q_U=\prod_{d\in U}d^2,
\qquad
(k,P)=1,
\tag{42}
\]

with the appropriate endpoint interval for `k`. Thus the exact-cell formulation does not manufacture new arithmetic data; it reorganizes the already-present partial CRT intersections and records precisely where signs must be controlled after high-incidence support has been removed.

Because the Boolean lattice itself has only `2^{|\mathcal D_y|}=X^{o(1)}` elements, passing between exact cells and all partial intersections can cost at most subpolynomial factors in crude finite-dimensional norm comparisons. That observation does **not** make the underlying Möbius sums easy: the singleton intersections in `(40)` are the original difficult coordinates `A_d`, and generic Möbius progression variance remains only logarithmically strong as quantified in `MC-227`.

## 5. Prior art and novelty boundary

The exact-cell partition, inclusion--exclusion formula `(41)`, and its interpretation as Möbius inversion on a Boolean lattice are classical combinatorial-sieve mechanisms. The Hilbert-space inequality `(24)` is elementary Cauchy--Schwarz. No novelty is claimed for either construction.

Random Rademacher multiplicative functions are a classical model for Möbius cancellation, and the prime-support orthogonality `(33)` is standard. `MC-217` and `MC-221` already use exactly this matched control on the same source-selected shell, so `(18)`--`(19)` are a refinement of an established internal calibration rather than a new probabilistic theorem.

The nearest arithmetic-progression prior art remains the Möbius Barban--Davenport--Halberstam theory recorded in `MC-S45` and audited in `MC-227`, together with modern variance results for bounded multiplicative functions in arithmetic progressions. Those results control residue-class averages or all-residue variance; they do not directly provide the fixed-power deterministic parity estimate `(15)` for the source-defined exact incidence cells. The present result makes no literature-absence claim and no external novelty claim.

The durable line-specific delta is instead an information-budget statement. Because the first shell has only `O(log X/loglog X)` moduli, its complete square-divisibility incidence word has only `X^{o(1)}` possible values. Therefore exact incidence refinement is fine enough to retain all source overlap while still cheap enough that discarding **all inter-cell cancellation** loses no fixed power. This narrows the active target from an unspecified need for low-incidence cross-slice interference to a concrete signed exact-cell energy `(15)`.

## 6. Boundaries and falsification tests

- Equation `(7)` is one-sided. `\mathcal C_y` may be polynomially larger than the true `W_y`; proving `(9)` is a sufficient route, not a necessary characterization of first-shell cancellation.
- The subpower factor is specific to the logarithmic first shell. If the number of selected moduli were a fixed positive multiple of `log X`, then `2^{|\mathcal D_y|}` would itself be a fixed power of `X` and the conclusion would change.
- Exact incidence is taken only with respect to the shell primes `d\in(y,2y]`. It does not encode all square divisors of `n+P` or all arithmetic information in the Möbius source.
- The support estimate `(13)` uses only `\mathcal E_S\subseteq\cap_{d\in S}\mathcal R_d`; exclusions from shell primes outside `S` can only make an exact cell smaller.
- The quarter boundary in `(13)` depends on square divisibility, the logarithmic shell, and the quadratic weighted energy. It is not asserted to persist under a different divisor power or shell geometry.
- The matched random expectation `(19)` is a calibration, not evidence that deterministic Möbius satisfies `(9)`. Higher moments and multiplicative dependence remain different from independent signs on the integers.
- Boolean inversion `(41)` does not supply cancellation. Applying absolute values to its `X^{o(1)}` terms preserves polynomial exponents but can still leave the full missing fixed power of Möbius cancellation.
- A proof of `(15)` that first assumes pointwise `X^{1/2+o(1)}` cancellation for all relevant source progressions may simply move the original difficulty into a stronger input; independence from the Mertens/RH target must still be audited.

The exact result is falsified if the cell partition fails to give `(4)`, if the weighted norm of `\mathbf1_S` is not `w(S)`, if the number of shell incidence patterns contributes a fixed power of `X`, or if the CRT support estimate `(28)` fails for an exact cell. The matched-control identity is falsified if distinct square-free prime-support characters are not orthogonal or if the double count `(35)` does not reproduce the diagonal shell support.

## Consequence for the live frontier

`MC-229` localized the unresolved first-shell source coupling below quarter incidence but left open whether useful cancellation had to occur through interference among the many partial intersections. The present result separates two possibilities more sharply.

A direct source-coupled proof may still exploit cross-cell anti-alignment. But it is **not power-essential**: the entire exact incidence partition contains only `X^{o(1)}` cells, so a diagonal bound for their signed sums reaches the same polynomial target. High-incidence cells are already harmless by support, and the matched random multiplicative source places the full cell-diagonal energy at `X^{1+o(1)}` with logarithmic room.

The next concrete theorem surface is therefore `(15)`: control the weighted squared Möbius parity sums inside exact low/mesoscopic shell-incidence cells, or exhibit a matched deterministic multiplicative control for which all currently available local/progression inputs hold while `(15)` is polynomially large. Either outcome directly tests whether exact source incidence retains enough arithmetic information without relying on cancellation between different cells.