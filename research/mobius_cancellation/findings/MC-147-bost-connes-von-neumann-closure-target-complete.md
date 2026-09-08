# MC-147 — The canonical Bost–Connes von Neumann closure is target-complete

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation used in `MC-138`–`MC-146`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
\pi(e(r))\varepsilon_k=e^{2\pi i k r}\varepsilon_k,
\qquad
\pi(\mu_n)\varepsilon_k=\varepsilon_{nk}.
\tag{1}
\]

Let

\[
\mathcal C:=\pi\bigl(C^*(\mathbb Q/\mathbb Z)\bigr)
\subset B(\mathcal H)
\tag{2}
\]

be the represented Bost–Connes coefficient algebra. `MC-143` proves that its norm closure is too small to recover Möbius orientation continuously: coefficient observables are restrictions of functions in `C(\widehat{\mathbb Z})`, and their uniform distance from the square-free Möbius sign is at least `1`.

The opposite phenomenon occurs as soon as the closure topology is weakened to the strong or weak operator topology. Precisely,

\[
\boxed{
\mathcal C''
=
\overline{\mathcal C}^{\mathrm{SOT}}
=
\overline{\mathcal C}^{\mathrm{WOT}}
=
\mathcal D
\cong \ell^\infty(\mathbb N),
}
\tag{3}
\]

where `\mathcal D` is the algebra of all bounded diagonal operators in the number basis.

Consequently the Möbius diagonal

\[
M_\mu\varepsilon_k=\mu(k)\varepsilon_k
\tag{4}
\]

belongs to both the strong and weak operator closures of the coefficient algebra. More strongly, **every bounded arithmetic sequence** `a:\mathbb N\to\mathbb C` occurs as the diagonal of an operator in `(3)`.

There is an explicit contractive sequence of coefficient-algebra elements converging strongly to `M_\mu`. For each `N`, choose an integer `Q_N>N` and define a function on `\mathbb Z/Q_N\mathbb Z` by

\[
c_N(j)=
\begin{cases}
\mu(j),&1\le j\le N,\\
0,&\text{otherwise},
\end{cases}
\tag{5}
\]

where the residues `1,\ldots,N` are distinct because `Q_N>N`. Fourier expansion on the finite cyclic group lifts `c_N` to a locally constant coefficient function

\[
f_N\in C(\widehat{\mathbb Z})
\cong C^*(\mathbb Q/\mathbb Z),
\qquad
\|f_N\|_\infty\le1.
\tag{6}
\]

Then

\[
f_N(k)=\mu(k)
\qquad(1\le k\le N),
\tag{7}
\]

so the corresponding diagonal operators satisfy

\[
\boxed{
\pi(f_N)\xrightarrow[N\to\infty]{\mathrm{SOT}}M_\mu,
}
\tag{8}
\]

and hence also converge weakly. There is no contradiction with `MC-143`: the convergence in `(8)` is not norm convergence. The topology has become weak enough that arbitrary bounded pointwise lookup tables enter the closure.

The full Bost–Connes algebra collapses even further in this representation. If

\[
\mathcal A:=\pi(A_{BC}),
\tag{9}
\]

then

\[
\boxed{
\mathcal A'=\mathbb C I,
\qquad
\mathcal A''=B(\ell^2(\mathbb N)).
}
\tag{10}
\]

Thus the strong/weak operator closure of the full represented Bost–Connes algebra is all bounded operators. An unrestricted von Neumann completion therefore cannot by itself be an arithmetic explanation of Möbius cancellation: it is **target-complete**, not target-selective.

The mathematical consequence for the live Bost–Connes escape is sharp. `MC-143`–`MC-146` show that norm-continuous coefficient/band readouts lose Möbius orientation. The present result shows that merely replacing norm continuity by unrestricted strong/weak closure does not repair that loss in a useful way; it overshoots to a class capable of encoding any bounded target. A surviving weak-completion route must therefore supply an independently justified regularity, complexity, state, dynamical, or source-to-excursion restriction that selects a much smaller class than the whole von Neumann closure.

## 1. The coefficient characters separate number states

Take distinct positive integers `m\ne n`. Choose an integer `q>|m-n|` and put

\[
r=1/q\pmod{\mathbb Z}.
\tag{11}
\]

Then `q\nmid m-n`, so

\[
e^{2\pi i m/q}\ne e^{2\pi i n/q}.
\tag{12}
\]

Therefore the represented coefficient algebra separates every pair of basis vectors `\varepsilon_m,\varepsilon_n` by diagonal eigenvalue.

Let `T\in\mathcal C'`. Writing

\[
T_{mn}=\langle\varepsilon_m,T\varepsilon_n\rangle,
\tag{13}
\]

commutation with `\pi(e(r))` gives

\[
\left(e^{2\pi i mr}-e^{2\pi i nr}\right)T_{mn}=0
\qquad(r\in\mathbb Q/\mathbb Z).
\tag{14}
\]

For `m\ne n`, choose `r` as in `(11)`–`(12)`; then `(14)` forces `T_{mn}=0`. Hence every operator commuting with `\mathcal C` is diagonal. Conversely every bounded diagonal operator commutes with every coefficient character. Thus

\[
\boxed{
\mathcal C'=\mathcal D.
}
\tag{15}
\]

The diagonal algebra is maximal abelian in `B(\ell^2(\mathbb N))`, so

\[
\mathcal D'=\mathcal D.
\tag{16}
\]

Combining `(15)`–`(16)` gives

\[
\mathcal C''=\mathcal D.
\tag{17}
\]

By the von Neumann bicommutant theorem, the bicommutant of a unital self-adjoint operator algebra is exactly both its strong and weak operator closure. This proves `(3)`.

The point is not special to Möbius. The norm closure remembers the profinite topology because it is `C(\widehat{\mathbb Z})`; the represented von Neumann closure remembers only that the countable number states are mutually distinguishable. Once all bounded diagonal operators are admitted, no continuity across profinitely nearby integers remains.

## 2. Explicit finite-congruence interpolation converges strongly to Möbius

The abstract bicommutant argument already puts `M_\mu` in the closure, but an explicit approximation makes the information transition transparent.

Fix `N` and choose `Q_N>N`. Any complex function on the finite cyclic group `\mathbb Z/Q_N\mathbb Z` has a finite Fourier expansion

\[
c_N(j)
=
\sum_{h=0}^{Q_N-1}\widehat c_N(h)e^{2\pi i hj/Q_N}.
\tag{18}
\]

Each character in `(18)` is a Bost–Connes coefficient generator `e(h/Q_N)`. Hence the pullback of `c_N` along

\[
\widehat{\mathbb Z}\longrightarrow\mathbb Z/Q_N\mathbb Z
\tag{19}
\]

is an element `f_N` of the coefficient algebra. By construction it satisfies `(6)`–`(7)`.

For `\xi=(\xi_k)_{k\ge1}\in\ell^2(\mathbb N)`, equation `(7)` gives pointwise convergence

\[
f_N(k)\to\mu(k)
\qquad\text{for every fixed }k,
\tag{20}
\]

while

\[
|f_N(k)-\mu(k)|\le2.
\tag{21}
\]

Therefore

\[
\begin{aligned}
\|\bigl(\pi(f_N)-M_\mu\bigr)\xi\|_2^2
&=
\sum_{k\ge1}|f_N(k)-\mu(k)|^2|\xi_k|^2\\
&\longrightarrow0
\end{aligned}
\tag{22}
\]

by dominated convergence. This proves the strong convergence `(8)` with a uniformly bounded approximating sequence.

The same construction works for an arbitrary bounded sequence `a(k)`: replace `\mu(j)` in `(5)` by `a(j)` and keep the remaining residues at zero. If `\|a\|_\infty\le C`, the approximants all have norm at most `C`, and the same dominated-convergence argument gives strong convergence to `\operatorname{diag}(a(k))`.

Thus strong approximation here is not an arithmetic achievement. It is simply finite-prefix interpolation plus a topology that tests convergence vector by vector rather than uniformly over all number states.

## 3. The norm/strong transition is exact

`MC-143` proves

\[
\inf_{g\in C(\widehat{\mathbb Z})}
\sup_{\mu(k)\ne0}|g(k)-\mu(k)|=1.
\tag{23}
\]

Hence no sequence in the coefficient algebra can converge in operator norm to `M_\mu`: operator norm for diagonal operators is the supremum norm of the diagonal sequence.

At the same time `(8)` gives a uniformly bounded strong-convergent sequence. Therefore the topology change is not rhetorical but exact:

\[
\boxed{
\text{norm closure: profinite-continuous and Möbius-obstructed},
\qquad
\text{SOT/WOT closure: all bounded diagonal sequences}.
}
\tag{24}
\]

This also explains why merely allowing "measurable", "pointwise", or "weak" coefficient limits is not a viable residual unless the allowed completion is specified more narrowly. In the atomic number-state representation, the von Neumann closure already contains every bounded lookup table on `\mathbb N`.

Equation `(24)` does not say that every mathematically meaningful weak completion is useless. It says that the **unrestricted** operator-topology closure is too large to certify arithmetic structure. A useful proposal must identify which smaller subclass is canonical and why its restriction is independently controlled.

## 4. Adding the semigroup isometries makes the representation irreducible

Now let `T\in\mathcal A'`, where `\mathcal A` is the full represented Bost–Connes algebra. Since `\mathcal C\subset\mathcal A`, equation `(15)` first forces

\[
T\varepsilon_k=d_k\varepsilon_k
\qquad(k\ge1)
\tag{25}
\]

for some bounded sequence `(d_k)`.

Commutation with the semigroup isometry `\pi(\mu_n)` gives

\[
T\pi(\mu_n)\varepsilon_k
=
d_{nk}\varepsilon_{nk},
\tag{26}
\]

while

\[
\pi(\mu_n)T\varepsilon_k
=
d_k\varepsilon_{nk}.
\tag{27}
\]

Thus

\[
d_{nk}=d_k
\qquad(n,k\ge1).
\tag{28}
\]

Taking `k=1` yields

\[
d_n=d_1
\qquad(n\ge1),
\tag{29}
\]

so `T=d_1I`. Therefore

\[
\mathcal A'=\mathbb CI.
\tag{30}
\]

Its bicommutant is consequently

\[
\mathcal A''=(\mathbb CI)'=B(\mathcal H),
\tag{31}
\]

which proves `(10)` by the bicommutant theorem. In this canonical representation, the full Bost–Connes algebra is irreducible and its von Neumann closure has no residual operator-level restriction at all.

This is stronger than the coefficient result `(3)`, but it should be interpreted more cautiously. The C*-algebraic norm structure, time evolution, KMS conditions, arithmetic subalgebras, distinguished states, and specific finite-energy observables remain highly nontrivial. Equation `(31)` says only that **forgetting all of those restrictions and retaining the generated von Neumann algebra** gives the whole ambient operator algebra.

## 5. Prior art and novelty audit

The operator-algebraic ingredients are established prior art.

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457, DOI `10.1007/BF01589495`, introduced the arithmetic `C^*`-dynamical system and its number-theoretic representation framework.
- Marcelo Laca and Iain Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, realize the Bost–Connes algebra as a semigroup crossed product and study its representations.
- Takuya Takeishi, *Irreducible representations of Bost–Connes systems*, Journal of Noncommutative Geometry **10** (2016), 889–906, DOI `10.4171/JNCG/251`, studies irreducible representation theory of Bost–Connes systems and explicitly builds on the `\mathbb Q` case of Laca–Raeburn.
- The von Neumann bicommutant theorem, identifying the bicommutant of a unital self-adjoint operator algebra with its strong and weak operator closures, is classical operator-algebra theory; see for example standard treatments in the Takesaki operator-algebra series or the Encyclopedia of Mathematics entry *Von Neumann algebra*.

The finite-prefix interpolation in Section 2 is elementary Fourier analysis on finite cyclic groups. The commutant computations in Sections 1 and 4 are direct consequences of the concrete representation `(1)`.

A targeted literature search for Bost–Connes canonical number-state representations, irreducibility, semigroup-crossed-product representations, and operator closures found the established representation-theoretic literature above. No novelty inference is drawn from whether the exact equalities `(3)` or `(10)` appear verbatim in those sources. They are immediate operator-algebraic consequences once the concrete representation is fixed.

Accordingly **no novelty is claimed for the bicommutant, irreducibility, or approximation facts themselves**. The durable line-specific delta is the classification of the precise escape left by `MC-143`–`MC-146`: weakening norm continuity all the way to unrestricted SOT/WOT completion does not reveal a selective Möbius carrier; it makes the admissible information class universal for bounded targets.

## Boundaries and falsification tests

- **The result is representation-specific.** Equations `(3)` and `(10)` use the canonical number-state representation `(1)`. A different representation may generate a different von Neumann algebra and must be audited separately.
- **The obstruction concerns unrestricted closure.** A canonically specified proper subspace, Sobolev/Lipschitz class, energy domain, modular condition, state family, operator ideal, spectral regularity class, or complexity-bounded approximation scheme may remain genuinely restrictive.
- **Strong approximation is not norm approximation.** Any argument using `(8)` as though the approximation were uniform across number states violates `MC-143` and `(23)`.
- **Finite-prefix fitting is the mechanism.** If a proposed weak-completion carrier is admitted merely because it can match longer and longer initial Möbius segments, it has not explained cancellation; every bounded target enjoys the same property.
- **The full von Neumann algebra forgets the C*-dynamical constraints.** Equation `(31)` does not imply that every bounded operator is natural, finite-energy, KMS-observable, arithmetically generated with controlled complexity, or useful for a source-to-Mertens theorem.
- **Pointwise target completeness does not imply aggregate control.** Neither `(3)` nor `(10)` gives a bound for `M(x)` or for the first-absolute mean `D_M(X)`.
- **Unbounded affiliated operators are not classified by the bounded bicommutant statement.** They remain outside the literal theorem, although simply enlarging to an even less restrictive class cannot by itself supply selectivity.

A proposed Bost–Connes weak-completion route is decisively non-informative if its only justification is membership in `\mathcal C''` or `\mathcal A''`, strong/weak approximation by bounded Bost–Connes observables, or exact agreement on every finite prefix. To survive, it must prove an additional source-forced restriction that excludes generic bounded target sequences/operators and then connect that restricted quantity quantitatively to Mertens excursion.

## Consequence for the line

The recent Bost–Connes sequence now has a clean topology boundary.

`MC-143` rules out norm-completed continuous coefficient encoding of Möbius orientation. `MC-144` collapses every bounded canonical diagonal readout back to that coefficient quotient. `MC-145` and `MC-146` extend the collapse through fixed off-diagonal rational bands and their full product-continuous profile.

The present result classifies the obvious weaker-completion escape. **SOT/WOT completion is not a hidden arithmetic reservoir: the coefficient closure is already all bounded diagonal sequences, and the full-algebra closure is all bounded operators.** It can recover Möbius only because it can recover anything.

The remaining Bost–Connes frontier must therefore retain a nontrivial restriction before closure becomes target-complete: for example a source-natural energy/modular regularity condition, a controlled state or representation family, a quantitative complexity budget, a singular construction with an independently justified domain, or an aggregate non-pointwise statistic with a proved transfer to first-absolute Mertens scale. Merely weakening the topology is now classified as information-neutral for the RH objective.