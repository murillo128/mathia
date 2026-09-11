# MC-224 — Generic large-sieve averaging stays one full power above the first-shell target

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-222` shows that characterwise square-root cancellation closes the first square-defect shell under Dirichlet GRH, while `MC-223` shows that merely declaring all but a sparse set of character sectors good does not help at fixed-power resolution. The next obvious escape is to avoid sectorwise estimates entirely and average the whole family by a large-sieve or Barban--Davenport--Halberstam type argument.

For the active first shell, **a coefficient-uniform large-sieve estimate cannot by itself reach the required energy scale**. The obstruction can be seen directly in the additive Fourier decomposition of the exact selected residue.

Keep

\[
y=c\log X,
\qquad 0<c<\frac12,
\qquad P=\prod_{p\le y}p,
\qquad T=X-P,
\]

and let `d` be prime with `y<d\le2y`. Put

\[
b_n:=\mu(n)\mathbf 1_{(n,P)=1},
\qquad
S(\alpha):=\sum_{n\le T}b_n e(\alpha n),
\qquad e(z):=e^{2\pi iz}.
\tag{1}
\]

The first-shell coordinate from `MC-221` is

\[
A_d(T)
=
\sum_{\substack{n\le T\\n\equiv-P\pmod{d^2}}}b_n.
\tag{2}
\]

Additive orthogonality gives the exact expansion

\[
\boxed{
A_d(T)
=
\frac1{d^2}
\sum_{r\bmod d^2}
 e\!\left(\frac{rP}{d^2}\right)
 S\!\left(\frac r{d^2}\right).
}
\tag{3}
\]

Because `d` is prime, `(3)` splits canonically into three frequency levels:

\[
A_d=A_d^{(0)}+A_d^{(1)}+A_d^{(2)},
\tag{4}
\]

where

\[
A_d^{(0)}=\frac{S(0)}{d^2},
\tag{5}
\]

\[
A_d^{(1)}
=
\frac1{d^2}
\sum_{1\le b<d}
 e\!\left(\frac{bP}{d}\right)
 S\!\left(\frac bd\right),
\tag{6}
\]

and

\[
A_d^{(2)}
=
\frac1{d^2}
\sum_{\substack{r\bmod d^2\\(r,d)=1}}
 e\!\left(\frac{rP}{d^2}\right)
 S\!\left(\frac r{d^2}\right).
\tag{7}
\]

Thus the selected square-modulus coordinate contains a zero mode, ordinary denominator-`d` modes, and genuinely primitive denominator-`d^2` modes.

Let

\[
E_j:=
\sum_{y<d\le2y\atop d\ {\rm prime}}
 d\,|A_d^{(j)}|^2.
\tag{8}
\]

The target in `MC-221` is

\[
W_y(X)=\sum_d d|A_d|^2\le X^{1+o(1)}.
\tag{9}
\]

A phase-blind componentwise proof could use

\[
W_y\le3(E_0+E_1+E_2).
\tag{10}
\]

But classical large-sieve input leaves both nonzero-frequency pieces at exponent `2-o(1)`, not exponent `1+o(1)`.

For the primitive square modes, Cauchy gives

\[
|A_d^{(2)}|^2
\le
\frac{\varphi(d^2)}{d^4}
\sum_{(r,d)=1}
\left|S\!\left(\frac r{d^2}\right)\right|^2
\ll
\frac1{d^2}
\sum_{(r,d)=1}
\left|S\!\left(\frac r{d^2}\right)\right|^2.
\tag{11}
\]

Hence

\[
E_2
\ll
\frac1y
\sum_{d\le2y}
\sum_{(r,d)=1}
\left|S\!\left(\frac r{d^2}\right)\right|^2.
\tag{12}
\]

Baier--Zhao's large sieve for power moduli, specialized to squares, bounds the last double sum by

\[
(\log\log X)^{O(1)}
\left(y^3+X+X^{1/2+\varepsilon}y^2\right)Z_X,
\tag{13}
\]

where

\[
Z_X:=\sum_{n\le T}|b_n|^2.
\tag{14}
\]

At `y=c log X`, the `X Z_X` term dominates. The same elementary primorial inclusion-exclusion used in `MC-221` gives

\[
Z_X
=
\left(e^{-\gamma}+o(1)\right)\frac{X}{\log y},
\tag{15}
\]

so `(12)`--`(15)` yield only

\[
\boxed{
E_2
\ll
\frac{X^2}{y\log y}(\log\log X)^{O(1)}
=
X^{2-o(1)}.
}
\tag{16}
\]

The ordinary denominator-`d` modes are no better at the power scale. Cauchy gives

\[
|A_d^{(1)}|^2
\le
\frac1{d^3}
\sum_{1\le b<d}
\left|S\!\left(\frac bd\right)\right|^2,
\tag{17}
\]

and the classical additive large sieve gives

\[
\boxed{
E_1
\ll
\frac{X Z_X}{y^2}
=
\frac{X^2}{y^2\log y}X^{o(1)}
=
X^{2-o(1)}.
}
\tag{18}
\]

These are not estimates for the actual sizes of `E_1` or `E_2`; they are the strongest conclusion obtained by feeding the coefficient energy into the standard phase-blind large-sieve interface. They miss `(9)` by essentially one full power of `X`.

The remaining zero mode is even more transparent:

\[
E_0
=
|S(0)|^2
\sum_{y<d\le2y\atop d\ {\rm prime}}
\frac1{d^3}
\asymp
\frac{|S(0)|^2}{y^2\log y}.
\tag{19}
\]

Thus diagonal-scale control of `E_0` already asks for

\[
|S(0)|
\le
X^{1/2+o(1)},
\tag{20}
\]

up to polylogarithmic factors: exactly the rough global zero-mode barrier isolated earlier in the line.

The conclusion is therefore sharp at the level of proof architecture. **Replacing characterwise estimates by a generic large-sieve norm bound does not evade the square-root barrier; it discards the source-selected direction and returns an almost-quadratic coefficient-energy estimate.** Any successful averaged proof must use additional Möbius-specific or source-specific information inside the signed projection, not merely better packing of the frequencies `r/d^2`.

No estimate `(9)`, no improved Mertens bound, and no new large-sieve inequality is proved here.

## 1. Exact three-level Fourier decomposition

For any modulus `m`,

\[
\mathbf 1_{n\equiv a\pmod m}
=
\frac1m\sum_{r\bmod m}e\!\left(\frac{r(n-a)}m\right).
\tag{21}
\]

Taking `m=d^2` and `a=-P` gives `(3)`. Since `d` is prime, every frequency `r mod d^2` has exactly one of the following reduced denominators:

- denominator `1` when `r=0`;
- denominator `d` when `r=db` with `1<=b<d`;
- denominator `d^2` when `(r,d)=1`.

Equations `(5)`--`(7)` are therefore not a chosen analytic partition but the exact conductor-level decomposition of the additive residue projector.

The displayed phases retain the source residue `-P`; inequalities `(11)` and `(17)` immediately erase them. That loss is deliberate here: the question is precisely what a phase-blind large-sieve argument can certify.

## 2. Square-modulus large sieve still pays the length term

Baier and Zhao, *Large Sieve Inequalities for Characters to Powerful Moduli*, Int. J. Number Theory 1 (2005), 265--279, arXiv:math/0508130, prove for power moduli the additive estimate

\[
\sum_{q\le Q}
\sum_{\substack{a\bmod q^k\\(a,q)=1}}
\left|\sum_{n=M+1}^{M+N}a_n e(an/q^k)\right|^2
\ll
(\log\log 10NQ)^{k+1}
\left(Q^{k+1}+N+N^{1/2+\varepsilon}Q^k\right)
\sum|a_n|^2.
\tag{22}
\]

See arXiv: https://arxiv.org/abs/math/0508130, Theorem 1. The same paper's introduction records the classical `k=1` large-sieve scale `(Q^2+N)Z` used for `(18)`.

For the first shell, set `k=2`, `N=T asymp X`, `Q=2y asymp log X`, and `a_n=b_n`. Then `Q^3` and `N^(1/2+epsilon)Q^2` are lower order for any fixed sufficiently small `epsilon>0`; the unavoidable-looking term is `N Z_X`. Substituting into `(12)` proves `(16)`.

The `N Z` term cannot be removed from a **coefficient-uniform** large-sieve theorem merely by improving the geometry of square moduli. Any family containing one frequency `alpha_0` admits the test coefficients `a_n=e(-alpha_0 n)` on an interval of length `N`; then the corresponding exponential sum has square magnitude `N^2` while `Z=N`. Thus a universal bound must allow a term of order `N Z`.

This does not prove that Möbius saturates `(22)`. It proves that a black-box inequality whose only coefficient input is `Z_X` cannot supply the missing power. The required gain must enter through arithmetic structure of `b_n`, source-dependent phase interference, or another non-generic statistic.

## 3. Relation to the character-family barrier

`MC-223` reaches a similar conclusion from the multiplicative Fourier side: the first-shell character family is only polylogarithmic, so cardinality cannot absorb even one fixed-power exceptional sector unless its signed contribution cancels in the distinguished coordinate.

The present calculation is independent evidence for the same frontier from the additive side. The square-modulus residue projector is a linear functional on the frequency vector `(S(r/d^2))_r`. Large sieve controls a norm of that vector. At `N asymp X` and denominator scale only `polylog(X)`, norm control is dominated by the sequence length and is nearly quadratic after insertion of `Z_X=X^{1-o(1)}`.

Thus two superficially different relaxations fail for the same information-theoretic reason inside this concrete arithmetic object:

- character sparsity forgets the signed source coordinate;
- large-sieve averaging forgets the direction of that coordinate and retains only coefficient energy.

What remains open is not another generic family-size estimate but a theorem about the **orientation** of the Möbius frequency/character vector relative to the source-selected residue projector, or an equivalent lifted statement preserving `n+P=d^2m`.

## 4. Prior-art and novelty boundary

The large-sieve inequalities in `(22)` and its `k=1` specialization are classical prior art; no novelty is claimed for them or for additive character expansion of a residue class. Baier--Zhao explicitly develop the power-modulus large-sieve framework and specialize earlier square-modulus work. The first-shell use here occurs far below the transition ranges where sparse square-modulus geometry can defeat the length term: `Q asymp log X` while `N asymp X`.

The line-specific durable result is the exponent budget obtained after composing that classical theorem with the exact `MC-221` first-shell projector. It rules out a natural proposed escape from `MC-223`: **generic second-moment averaging over the square-modulus family does not turn the first-shell problem into a routine large-sieve estimate.**

No claim is made that every dispersion, bilinear, Type-II, reciprocal-`L`, or source-lift method factors through `(22)`. Such methods may use precisely the arithmetic information erased by the coefficient-uniform norm bound.

## 5. Boundaries and falsification tests

- Equations `(16)` and `(18)` are upper bounds delivered by a proof interface, not lower bounds for the actual energies. They establish insufficiency of this black-box certificate, not largeness of the Möbius energies themselves.
- Cross terms between `A_d^(0)`, `A_d^(1)` and `A_d^(2)` may cancel. Inequality `(10)` deliberately refuses to use that interference. A successful source-sensitive proof may therefore evade this obstruction.
- The coefficient-alignment example shows that the `N Z` term is necessary for a theorem uniform over arbitrary coefficients. It does not show that a Möbius-specific refinement cannot remove a full power.
- The calculation is specialized to the first shell `d asymp log X`. At larger root-modulus scales, the relative sizes of the spacing and length terms in the power-modulus large sieve change and must be recalculated.
- The rough norm asymptotic `(15)` uses the same logarithmic-primorial regime as `MC-221`; changing the sieve level changes the logarithmic factors but not the present fixed-power conclusion while `y=X^{o(1)}`.
- The zero mode `(19)` should not be double-counted as a new RH equivalence. It is the additive version of the already-known global/principal obstruction.

The exact decomposition is falsified by any missing frequency class in `(4)`, and the power-budget conclusion is falsified if the cited square-modulus theorem at `Q=O(log X)` avoids the `N Z_X` term or if the first-shell coefficient norm is not `X^{1-o(1)}`.

## Consequence for the live frontier

After `MC-222`--`MC-224`, three standard relaxations of uniform Dirichlet-GRH-quality control have now been separated:

1. sectorwise GRH-quality estimates close the shell but overpay to the full Dirichlet family (`MC-222`);
2. sparse exceptional-sector counts cannot absorb a fixed-power bad sector without signed cancellation (`MC-223`);
3. coefficient-uniform large-sieve averaging controls only norm/energy and remains at exponent `2-o(1)` (`MC-224`).

The next useful attack should therefore preserve a signed source-selected interaction that both family counting and generic norm inequalities erase. Natural candidates are a bilinear/dispersion identity tied to the lift `n+P=d^2m`, a reciprocal-`L` family estimate that controls the **signed selected coordinate** rather than each character separately, or a moving-degree parity theorem that directly couples the even and odd sectors from `MC-221`.