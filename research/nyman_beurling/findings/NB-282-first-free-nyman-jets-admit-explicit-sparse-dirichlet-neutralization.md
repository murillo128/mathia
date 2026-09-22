# NB-282 — first-free Nyman jets admit explicit sparse Dirichlet neutralization

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-052, NB-117, NB-128, NB-130, NB-280, NB-281
- **Classification:** `EXACT-DERIVED + SPARSE-DIRICHLET-INTERPOLATION + FIRST-FREE-JET-NEUTRALIZATION + EXPLICIT-SECTION-LENGTH + NB-281-STRENGTHENING + NEGATIVE/ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-281` identifies the first derivative order beyond the actual zeta multiplicity as the first genuinely source-dependent jet of a finite Nyman residual. It also proves that these free jets can be prescribed independently on every finite packet if one allows an unrestricted finite Dirichlet polynomial, but deliberately leaves the arithmetic synthesis cost unpriced.

The support-length part of that cost can be priced explicitly, and it is much weaker than a generic finite-section obstruction might suggest.

Let

\[
Z=\{\rho_1,\ldots,\rho_N\}
\subset \{\zeta=0,\ \Re s>1/2\}
\tag{1}
\]

be a finite set of **distinct** nontrivial zeta zeros, and let `m_j` be the actual multiplicity of `rho_j`. For a finite Dirichlet polynomial

\[
P(s)=\sum_{n\le M}a_n n^{-s},
\qquad
Q_P(s):=P(s)-P(1),
\tag{2}
\]

the legal residual is

\[
r_P(s)
=\frac1s-\frac{\zeta(s)}sQ_P(s).
\tag{3}
\]

Form the finite half-plane Blaschke product

\[
B_Z(s)=\prod_{j=1}^N b_{\rho_j}(s)^{m_j},
\tag{4}
\]

with arbitrary unimodular normalization, and put

\[
p_Z(s)
:=P_{K_{B_Z}}k_1(s)
=\frac{1-\overline{B_Z(1)}B_Z(s)}s,
\qquad
k_1(s)=\frac1s.
\tag{5}
\]

Then the first free jet of `r_P` relative to the Burnol/model-space minimizer is

\[
\boxed{
 r_P^{(m_j)}(\rho_j)-p_Z^{(m_j)}(\rho_j)
 =
 \frac{
 \overline{B_Z(1)}B_Z^{(m_j)}(\rho_j)
 -\zeta^{(m_j)}(\rho_j)Q_P(\rho_j)
 }{\rho_j}.
}
\tag{6}
\]

Consequently all first free jets are neutralized exactly if

\[
\boxed{
Q_P(\rho_j)
=
 y_j^{\star}
:=
\overline{B_Z(1)}
\frac{B_Z^{(m_j)}(\rho_j)}{\zeta^{(m_j)}(\rho_j)},
\qquad 1\le j\le N.
}
\tag{7}
\]

The data in `(7)` are always well defined because the multiplicity is exact, so `zeta^(m_j)(rho_j) != 0`. They are also independent of the unimodular normalization of `B_Z` because the two Blaschke factors in the numerator transform with opposite phases.

The new point is that `(7)` can be solved inside an explicit **sparse natural Dirichlet section**. There exists a prime

\[
q\in\{p_1,\ldots,p_{\binom N2+1}\}
\tag{8}
\]

such that, for every prescribed vector `y=(y_1,...,y_N) in C^N`, there is a unique polynomial of the form

\[
\boxed{
P_y(s)=\sum_{k=1}^N a_k q^{-ks}
}
\tag{9}
\]

satisfying

\[
\boxed{
P_y(\rho_j)-P_y(1)=y_j,
\qquad 1\le j\le N.
}
\tag{10}
\]

Hence the first free Nyman jets of every finite packet can be neutralized by a source supported on only `N` integers,

\[
q,q^2,\ldots,q^N,
\tag{11}
\]

and therefore inside the ordinary natural section with cutoff

\[
\boxed{
M_Z\le
p_{\binom N2+1}^{\,N}.
}
\tag{12}
\]

Using the standard estimate `p_r=O(r log r)`, this is

\[
\boxed{
\log M_Z=O(N\log N).
}
\tag{13}
\]

Thus **finite-section length alone cannot turn the first source-dependent jet into a persistent obstruction once the available cutoff satisfies `log M >> N log N`**. Any surviving source-native mechanism must charge something that `(12)` does not control: coefficient growth, the actual Nyman/Hardy synthesis norm, conditioning of the finite interpolation matrix, or a simultaneous constraint involving more than the first free jet.

This is a genuine strengthening of the unpriced surjectivity statement in `NB-281`, but it is not a norm estimate. The Vandermonde inverse can be extremely ill-conditioned when the phase nodes nearly collide. No bounded coefficient or bounded `H^2` synthesis cost is claimed.

## 1. Every zero pair rules out at most one prime base

For an integer base `q>=2`, write

\[
x_j(q):=q^{-\rho_j},
\qquad
x_0(q):=q^{-1}.
\tag{14}
\]

The interpolation matrix associated with the support `(11)` will be nonsingular as soon as the `x_j(q)` are pairwise distinct. Also

\[
|x_j(q)|=q^{-\Re\rho_j}>q^{-1}=|x_0(q)|,
\tag{15}
\]

because every nontrivial zero satisfies `Re rho_j<1`; hence `x_j(q) != x_0(q)` automatically.

Consider a fixed pair `rho_j != rho_l`. If

\[
x_j(q)=x_l(q),
\tag{16}
\]

then their real parts must agree and, writing

\[
\rho_j-\rho_l=i\tau,
\qquad \tau\ne0,
\tag{17}
\]

one has

\[
\tau\log q\in2\pi\mathbb Z.
\tag{18}
\]

A single pair cannot satisfy `(18)` for two distinct prime bases `p` and `q`. Indeed, if

\[
\tau\log p=2\pi r,
\qquad
\tau\log q=2\pi s
\tag{19}
\]

with nonzero integers `r,s`, then

\[
\frac{\log p}{\log q}=\frac rs\in\mathbb Q,
\tag{20}
\]

which would imply `p^s=q^r`, impossible for distinct primes.

There are only `binom(N,2)` zero pairs. Each pair can therefore exclude at most one prime. Among the first

\[
\binom N2+1
\tag{21}
\]

primes, at least one base `q` produces pairwise distinct nodes

\[
x_1(q),\ldots,x_N(q).
\tag{22}
\]

This proves the existence assertion in `(8)` without any separation hypothesis on the zeros.

The base selection is deliberately robust against exact vertical aliases. For a generic packet the base `q=2` will already work, but no such genericity is needed here.

## 2. The finite Dirichlet evaluation map is an ordinary Vandermonde map

Fix an admissible base `q` from Section 1 and abbreviate

\[
x_j:=q^{-\rho_j},
\qquad x_0:=q^{-1}.
\tag{23}
\]

For `(9)`,

\[
Q_{P_y}(\rho_j)
=P_y(\rho_j)-P_y(1)
=\sum_{k=1}^N a_k\bigl(x_j^k-x_0^k\bigr).
\tag{24}
\]

Thus the coefficient vector `a=(a_1,...,a_N)^T` is sent to the prescribed data by the matrix

\[
A_{j,k}=x_j^k-x_0^k,
\qquad 1\le j,k\le N.
\tag{25}
\]

Each entry factors as

\[
x^k-x_0^k
=(x-x_0)
\left(
 x^{k-1}+x^{k-2}x_0+\cdots+x_0^{k-1}
\right).
\tag{26}
\]

After factoring `x_j-x_0` from row `j`, the remaining column polynomials are monic of degrees `0,1,...,N-1`. Their evaluation determinant is therefore the ordinary Vandermonde determinant. Hence

\[
\boxed{
\det A
=
\left(\prod_{j=1}^N(x_j-x_0)\right)
\left(\prod_{1\le i<j\le N}(x_j-x_i)\right)
\ne0.
}
\tag{27}
\]

So `(24)` is an isomorphism `C^N -> C^N`, proving `(9)`--`(10)` for **arbitrary** prescribed data.

Equivalently, one may view

\[
R(x):=\sum_{k=1}^N a_k(x^k-x_0^k)
\tag{28}
\]

as the unique polynomial of degree at most `N` satisfying

\[
R(x_0)=0,
\qquad
R(x_j)=y_j.
\tag{29}
\]

The sparse Dirichlet interpolator is just ordinary polynomial interpolation transported through the map `x=q^{-s}`.

This exact reduction is useful because it separates **rank/support length** from **conditioning**. The determinant proves existence with `N` active Dirichlet atoms, but its magnitude records the possible coefficient explosion through the separation products in `(27)`.

## 3. The first free jet relative to the Burnol minimizer

`NB-281` proves that the finite residual satisfies

\[
r_P^{(\ell)}(\rho_j)
=k_1^{(\ell)}(\rho_j),
\qquad 0\le\ell<m_j,
\tag{30}
\]

and that the first source-dependent derivative is

\[
r_P^{(m_j)}(\rho_j)
=k_1^{(m_j)}(\rho_j)
-
\frac{\zeta^{(m_j)}(\rho_j)}{\rho_j}
Q_P(\rho_j).
\tag{31}
\]

The finite model-space projection `(5)` has the same forced jets through order `m_j-1`. Since

\[
k_1(s)-p_Z(s)
=
\overline{B_Z(1)}\frac{B_Z(s)}s,
\tag{32}
\]

and `B_Z` has a zero of exact order `m_j` at `rho_j`, Leibniz gives

\[
k_1^{(m_j)}(\rho_j)-p_Z^{(m_j)}(\rho_j)
=
\overline{B_Z(1)}
\frac{B_Z^{(m_j)}(\rho_j)}{\rho_j}.
\tag{33}
\]

Subtracting `(33)` from `(31)` gives `(6)`.

Therefore the specific values `(7)` force

\[
\boxed{
r_P^{(\ell)}(\rho_j)
=p_Z^{(\ell)}(\rho_j),
\qquad
0\le\ell\le m_j,
\quad 1\le j\le N.
}
\tag{34}
\]

The forced multiplicity jets `0,...,m_j-1` agree automatically; `(7)` neutralizes precisely the first jet that `NB-281` showed to be source-dependent.

Applying the interpolation theorem of Section 2 to the data `y_j=y_j^star` gives a finite legal Nyman source with the sparse support `(11)` and cutoff `(12)` satisfying `(34)` simultaneously for the whole packet.

The data `(7)` depend on actual zeta derivatives and on the finite Blaschke packet. This is not a formal-zero construction: the theorem applies to whatever finite set of actual right-half zeros exists. It also does not assert that any such zeros exist.

## 4. What support length can and cannot certify

Let `M` be the available natural Dirichlet cutoff. If

\[
M\ge p_{\binom N2+1}^{\,N},
\tag{35}
\]

then the section contains a source that neutralizes all first free jets of the packet relative to `p_Z`. Hence no lower-bound argument depending only on the impossibility of realizing those first free jet values can survive in that regime.

The asymptotic version is particularly transparent. The standard `p_r=O(r log r)` estimate turns `(35)` into

\[
\log M\gg N\log N
\tag{36}
\]

as a sufficient support-length budget. Therefore, in any rank-coupled application where

\[
N\log N=o(\log M),
\tag{37}
\]

first-free-jet **existence** is already too cheap to provide a finite-section obstruction.

This does **not** say the interpolator is cheap in the metric that matters to Nyman--Beurling. Near collisions of the nodes `x_j=q^{-rho_j}` make the Vandermonde factors in `(27)` small, and the coefficients can become enormous. The corresponding Nyman synthesis norm can therefore be large even though the support is sparse.

This distinction is the new boundary left by the calculation:

\[
\text{support/rank obstruction}
\quad\text{is removed by `(12)`,}
\]

whereas

\[
\text{conditioning/Hilbert-cost obstruction}
\quad\text{remains live.}
\]

The correct next finite quantity is thus not another zero-only Hermite Gram and not merely the smallest section length. It is the weighted inverse of the actual finite synthesis map. If `Phi_n(s)=zeta(s)(n^{-s}-n^{-1})/s` denotes the natural Nyman atom and `R_M=(<Phi_n,Phi_m>)` its section Gram, then for a packet evaluation matrix

\[
U_{j,n}=n^{-\rho_j}-n^{-1}
\tag{38}
\]

the least source norm for prescribed `Q_P(rho_j)=y_j` is governed by the constrained quadratic form built from

\[
U R_M^{-1}U^*.
\tag{39}
\]

Equation `(39)` is stated only as the next object, not as a new theorem here. Its high-ordinate behavior, especially for the neutralizing data `(7)`, is exactly the conditioning question that `(12)` leaves unresolved.

## 5. Relation to earlier findings

There is no contradiction with the logarithmic recurrence obstructions in `NB-123`--`NB-124`. Those findings study how a fixed finite **zero-power packet** can mimic natural-grid target data. Here the direction of interpolation is reversed: the zero packet is fixed, while the finite **Dirichlet source** is chosen to match data at the zeros.

`NB-130` is the closest algebraic analogue. It shows that a formal packet of `R` zero powers can interpolate arbitrary data on `R` natural integers by a Vandermonde map. The present result is the reciprocal finite-source statement required by `NB-281`: `N` natural Dirichlet atoms on a geometric integer support interpolate arbitrary values on `N` fixed actual zeros, after choosing a base that avoids exact aliases.

`NB-052` already shows that after Blaschke deflation the remaining approximation problem is an arithmetic enrichment defect. The present result does not replace that defect by another universal zero condition. Instead it shows that its **first local jet trace has no support-length obstruction beyond `(12)`**. Any real gain from the deflated arithmetic space must therefore enter through conditioning, global norm geometry, or more data than one free jet per distinct zero.

Finally, `NB-280`--`NB-281` showed that all source-independent point and multiplicity-jet constraints collapse to the finite Burnol/Blaschke defect. `NB-282` pushes one step beyond that universal layer: even the first source-dependent jet can be matched constructively at controlled finite cutoff. What remains is no longer an existence problem; it is a quantitative synthesis-cost problem.

## 6. Prior-art and novelty audit

The determinant argument `(24)`--`(29)` is ordinary finite polynomial/Vandermonde interpolation under the exponential change of variables `x=q^{-s}`. No novelty is claimed for that algebra. Likewise the model-space projection `(5)` and the multiplicity factorization used in `(30)`--`(33)` are classical Hardy/Blaschke geometry already anchored through Burnol in `SOURCES.md` and audited in `NB-052`, `NB-280`, and `NB-281`.

A fresh search of the Nyman--Beurling/Baez--Duarte literature found the standard finite Dirichlet-polynomial formulations, Burnol's zero/multiplicity lower-bound mechanism, and the modern optimal-Dirichlet-polynomial work, but did not locate this particular sparse `q`-power interpolation of the **first source-dependent residual jets** or the explicit cutoff `(12)`. The claim made here is therefore deliberately line-local: the new content is the collision between the exact residual jet formula of `NB-281` and a constructive natural-section interpolation budget.

The nearest classical Hardy interpolation literature treats value interpolation and Blaschke separation in much greater generality. That background confirms rather than changes the classification: existence of an interpolant is standard function theory; the Nyman-specific content is the exact data `(7)` and the fact that they can be realized by an actual finite natural Dirichlet source at the cutoff `(12)`.

No new external theorem is load-bearing beyond standard prime growth for the optional asymptotic restatement `(13)`. The exact result `(12)` uses only the finite prime list and the determinant proof above. `SOURCES.md` therefore does not change.

## 7. Falsification and follow-up

The exact theorem would be falsified by any of the following:

- a pair of distinct primes that are both exact alias bases for the same distinct pair of zero exponents;
- an admissible base `q` for which the determinant `(27)` vanishes;
- a legal residual whose order-`m_j` derivative fails to satisfy `(31)`;
- the model-space projection `(5)` failing to satisfy `(33)`;
- the interpolator solving `(7)` but failing the jet identity `(34)`.

All five checks reduce to explicit algebraic identities.

The remaining quantitative test is sharper than the open statement in `NB-281`: fix the natural cutoff `M`, build the actual Nyman Gram `R_M` and the evaluation map `U`, and estimate the minimum synthesis cost for the specific neutralizing vector `(7)`. If the relevant inverse form stays large at Ford scale, the free-jet route acquires a genuinely source-native obstruction. If matched packets keep it bounded, then even the conditioning repair fails and one must move to higher/global data or a nonlinear boundary observable.

## Conclusion

The first source-dependent Nyman jet is not protected by a large finite-section **support** barrier. For every finite packet of `N` actual right-half zeros, all first free jets can be neutralized simultaneously by a Dirichlet polynomial using exactly `N` geometric integer atoms and lying inside a natural cutoff

\[
M\le p_{\binom N2+1}^{N}.
\]

Thus `NB-281`'s unrestricted surjectivity can be made constructive with `log M=O(N log N)`. The unresolved cost is now isolated cleanly: not whether the arithmetic section can realize the required free-jet values, but how badly conditioned that realization is in the actual Nyman/Hardy source norm.