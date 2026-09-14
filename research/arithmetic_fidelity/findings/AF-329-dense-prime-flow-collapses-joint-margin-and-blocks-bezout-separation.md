# AF-329 — Dense prime flow collapses the joint singular margin and blocks Bézout separation

**Status:** `EXACT-DERIVED`, `CLASSICAL-CONSEQUENCE`, `ARITHMETIC-FIDELITY`, `EXPONENTIAL-SUMS`, `KRONECKER`, `IDEAL-THEORY`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-328 isolates the unresolved eight-prime middle-singular incidence as the common-zero problem

\[
F(it)=G(it)=0,
\]

where, for eight distinct rational primes `p_1,\ldots,p_8`,

\[
F(s)=\sum_{j=1}^8p_j^{-s},
\qquad
G(s)=\sum_{|I|=4}\left(\prod_{i\in I}p_i\right)^{-s}.
\tag{1}
\]

AF-328 also proves that `F` and `G` are coprime in the classical ring of finite complex exponential sums, but coprimality does not exclude an isolated common zero. The next natural escape would be stronger: perhaps the pair is uniformly separated from `(0,0)`, or perhaps coprimality upgrades to a Bézout identity.

Neither is possible.

Let

\[
\lambda_j=-\log p_j,
\qquad
Z_P(t)=\left(e^{i\lambda_1t},\ldots,e^{i\lambda_8t}\right)
       =\left(p_1^{-it},\ldots,p_8^{-it}\right)
\in\mathbb T^8,
\tag{2}
\]

and define the retained target map

\[
\Phi(z_1,\ldots,z_8)=\bigl(e_1(z),e_4(z)\bigr).
\tag{3}
\]

The prime logarithms are linearly independent over `\mathbb Q`, so the continuous one-parameter orbit `Z_P(\mathbb R)` is dense in `\mathbb T^8`. Since the regular-octagon configuration

\[
Z_*=\{1,\omega,\ldots,\omega^7\},
\qquad \omega=e^{2\pi i/8},
\tag{4}
\]

is the root set of `w^8-1`, it satisfies

\[
e_1(Z_*)=e_4(Z_*)=0.
\tag{5}
\]

Therefore

\[
\boxed{
\inf_{t\in\mathbb R}
\left\|igl(F(it),G(it)\bigr)\right\|=0.
}
\tag{6}
\]

More strongly, for every `\varepsilon>0`, the set of real times

\[
\left\{t:
\left\|igl(F(it),G(it)\bigr)\right\|<\varepsilon
\right\}
\tag{7}
\]

is relatively dense: there is `L_\varepsilon<\infty` such that every interval of length `L_\varepsilon` contains one such time. No quantitative estimate for `L_\varepsilon` is claimed.

Thus even if the exact common-zero set on the imaginary axis is empty, the pair has **zero joint value margin** and returns arbitrarily close to the singular target with bounded gaps depending on the requested tolerance.

There is a matching algebraic statement. Let `\mathcal E` be the full ring of finite complex exponential sums used in AF-328. Although

\[
\gcd_{\mathcal E}(F,G)
\]

is a unit, the ideal they generate is proper:

\[
\boxed{(F,G)\ne\mathcal E.}
\tag{8}
\]

Equivalently, there do not exist finite exponential sums `A,B\in\mathcal E` with

\[
AF+BG=1.
\tag{9}
\]

So the AF-328 frontier has an exact two-part obstruction:

\[
\boxed{
\text{coprime}
\quad\not\Rightarrow\quad
\text{Bézout-separated},
\qquad
\text{zero-free}
\quad\not\Rightarrow\quad
\text{positive joint margin}.
}
\tag{10}
\]

Any eventual exclusion of an exact eight-prime singular hit must therefore be genuinely pointwise/nonuniform. It cannot come from a positive lower bound on `|(F,G)|`, nor from upgrading the known common-factor obstruction to a unit-ideal certificate inside `\mathcal E`.

## 1. Dense torus orbits erase every continuous value margin whose ambient target is nonempty

The prime specialization is an instance of a general compact-dynamical fact.

Let `\lambda=(\lambda_1,\ldots,\lambda_d)\in\mathbb R^d` satisfy

\[
 k\cdot\lambda\ne0
\qquad
\text{for every }0\ne k\in\mathbb Z^d,
\tag{11}
\]

and let

\[
z_\lambda(t)=\left(e^{i\lambda_1t},\ldots,e^{i\lambda_dt}\right).
\tag{12}
\]

Kronecker's theorem gives

\[
\overline{z_\lambda(\mathbb R)}=\mathbb T^d.
\tag{13}
\]

For any continuous map `\Psi:\mathbb T^d\to\mathbb C^r`, continuity and compactness imply

\[
\overline{\Psi(z_\lambda(\mathbb R))}
=
\Psi(\mathbb T^d).
\tag{14}
\]

Hence, for any norm on `\mathbb C^r`,

\[
\boxed{
\inf_{t\in\mathbb R}\|\Psi(z_\lambda(t))\|
=
\min_{z\in\mathbb T^d}\|\Psi(z)\|.
}
\tag{15}
\]

In particular, if the ambient target fiber `\Psi^{-1}(0)` is nonempty, then the dense source orbit has zero value margin whether or not it ever enters that fiber exactly.

This separates two questions that are often conflated:

\[
\text{exact incidence: }0\in\Psi(z_\lambda(\mathbb R)),
\tag{16}
\]

versus

\[
\text{stable value separation: }
\inf_t\|\Psi(z_\lambda(t))\|>0.
\tag{17}
\]

For a dense source orbit and continuous target, `(17)` is controlled entirely by the ambient torus geometry. It contains no information about the special arithmetic placement of the orbit beyond density.

This is a direct Arithmetic Fidelity no-go principle: once a compression asks only for a continuous distance from a target that already occurs somewhere in the ambient completion, dense source dynamics destroy every positive discriminator margin before the exact arithmetic-incidence question is reached.

## 2. Near-singular prime times are relatively dense

Equation `(6)` follows immediately from `(15)`, but the recurrence is stronger than existence of a sequence of near-hits.

Fix `\varepsilon>0` and choose an open neighborhood `U\subset\mathbb T^8` of the regular octagon `Z_*` such that

\[
Z\in U
\Longrightarrow
\|\Phi(Z)\|<\varepsilon.
\tag{18}
\]

The irrational translation flow generated by `\lambda` on the compact torus is minimal: every orbit is dense. Therefore the family of open sets

\[
\{\varphi_{-t}(U):t\in\mathbb R\}
\]

covers `\mathbb T^8`, where `\varphi_t` denotes the torus translation flow. Compactness gives a finite subcover

\[
\mathbb T^8
=
\bigcup_{j=1}^m\varphi_{-t_j}(U).
\tag{19}
\]

Let

\[
L_\varepsilon
=
\max_j t_j-\min_j t_j.
\]

For every starting time `T`, the point `Z_P(T-\min_jt_j)` belongs to one member of the cover, so for some `j`

\[
Z_P(T-\min_jt_j+t_j)\in U.
\]

The resulting hitting time lies in an interval of length `L_\varepsilon`. After translating the interval origin harmlessly, every interval of that length contains a time satisfying `(18)`, which proves `(7)`.

The statement is qualitative. Effective Kronecker theory can price recurrence for more specific targets, and AF-325 already uses Baker-type height estimates for a different near-singular geometry, but no useful `\varepsilon`-dependence is needed here. The purpose is to classify the exact stability boundary: approximate common zeros are not rare excursions of the fixed prime support; they recur syndetically.

## 3. The AF-328 pair is coprime but not comaximal

AF-328 proves that `F` is irreducible in `\mathcal E` and that `F` does not divide `G`; hence the pair has no common nonunit factor. That is strictly weaker than `(F,G)=\mathcal E`.

Assume for contradiction that there exist `A,B\in\mathcal E` with

\[
A(s)F(s)+B(s)G(s)=1.
\tag{20}
\]

Let

\[
\Gamma_{\mathbb Q}
=
\operatorname{span}_{\mathbb Q}\{\lambda_1,\ldots,\lambda_8\}
\subset\mathbb C.
\tag{21}
\]

Decompose the finite supports of `A` and `B` into additive cosets of `\Gamma_{\mathbb Q}`. Since every frequency of `F` and `G` lies in `\Gamma_{\mathbb Q}`, multiplication by either `F` or `G` preserves those cosets. Distinct exponential frequencies are linearly independent as entire functions, so the `\Gamma_{\mathbb Q}`-coset component of `(20)` must itself satisfy

\[
A_0F+B_0G=1,
\tag{22}
\]

where all frequencies of `A_0,B_0` lie in `\Gamma_{\mathbb Q}`. Every other coset component separately sums to zero.

Only finitely many rational coordinates occur in the supports of `A_0,B_0`. Choose `N\ge1` clearing their denominators relative to the basis `\lambda_1,\ldots,\lambda_8`, and introduce Laurent variables

\[
Y_j=e^{\lambda_js/N}.
\tag{23}
\]

The `\mathbb Q`-linear independence of the `\lambda_j` makes distinct Laurent monomials in the `Y_j` correspond to distinct exponential frequencies. Therefore `(22)` becomes an identity in

\[
\mathbb C[Y_1^{\pm1},\ldots,Y_8^{\pm1}]:
\]

\[
a(Y)P_N(Y)+b(Y)Q_N(Y)=1,
\tag{24}
\]

with

\[
P_N(Y)=\sum_{j=1}^8Y_j^N,
\qquad
Q_N(Y)=e_4(Y_1^N,\ldots,Y_8^N).
\tag{25}
\]

Now let

\[
y_j=\omega^{j-1},
\qquad1\le j\le8,
\tag{26}
\]

be the regular-octagon roots. For each `j`, choose any nonzero `N`-th root `Y_j` of `y_j`. Then

\[
P_N(Y)=e_1(y_1,\ldots,y_8)=0,
\qquad
Q_N(Y)=e_4(y_1,\ldots,y_8)=0.
\tag{27}
\]

Evaluating `(24)` at this point gives `0=1`, a contradiction. Hence no identity `(20)` exists and `(8)` follows.

This also explains geometrically why AF-328's coprimality result cannot be strengthened by purely formal factorization. In every finite rational-frequency refinement, the two Laurent pullbacks retain a common algebraic torus zero. Their greatest common divisor is nevertheless trivial because a codimension-two common zero need not generate a common hypersurface factor.

## 4. Proper ideal does not mean an actual common analytic zero

The distinction in `(8)` is algebraic, not a hidden solution of the original incidence problem.

The regular-octagon evaluation used in `(27)` is a character of the rational-frequency group algebra after denominator clearing. It need not come from evaluation at any single complex number `s`. In particular,

\[
(F,G)\ne\mathcal E
\]

does **not** imply the existence of `s\in\mathbb C` with

\[
F(s)=G(s)=0.
\]

AF-328's pointwise common-zero problem therefore remains untouched.

This boundary is precisely the one needed for the research line. Common-factor theory asks whether the common zero set contains enough repeated/algebraic structure to force a divisor. Unit-ideal theory asks whether the pair admits an algebraic global certificate of no common zero inside the exponential-sum ring. The ambient torus zero obstructs that certificate even if the one-dimensional analytic prime orbit misses it forever.

Thus the remaining exact question is narrower than both algebraic tests:

\[
\boxed{
\text{Does the specific one-parameter prime-log orbit itself enter }
V(e_1,e_4)?
}
\tag{28}
\]

Neither gcd data nor Bézout data decide that incidence.

## Arithmetic-fidelity consequence

AF-309 already shows that exact zeros of a single saturated exponential sum form a dense measure-zero frequency incidence set, so exact arithmetic membership is topologically unstable. AF-329 identifies the corresponding target-side mechanism for the two-observable singular problem.

For the exact AF-328 pair, the ambient retained map has a genuine zero and the rational-prime orbit is dense. Therefore every continuous norm of the retained defect loses stable separation automatically. The arithmetic discriminator, if it exists, can only live in the distinction between

\[
\text{arbitrarily close recurrent approach}
\quad\text{and}\quad
\text{exact incidence}.
\tag{29}
\]

That is an unusually severe compression boundary. A downstream argument that tolerates any fixed positive observation error cannot distinguish a hypothetical zero-free prime orbit from the ambient singular geometry using only `(F,G)`: for every tolerance the same fixed prime support eventually enters that tolerance, and does so with bounded recurrence gaps.

At the same time, AF-328 and `(8)` show opposite algebraic facts:

- the pair is coprime, so no common exponential-sum factor explains the target;
- the pair is not comaximal, so no finite exponential-sum Bézout certificate separates it from zero.

The exact prime incidence is trapped strictly between those two notions. A successful next theorem must therefore use pointwise arithmetic/transcendence information about the special orbit, an exact identity that creates a forbidden multiplicative relation, or another observable that changes the target geometry. Stable norm separation, ambient continuity, and factor/ideal certificates in the current exponential-sum ring are exhausted mechanisms.

## Prior art and novelty assessment

No broad novelty is claimed.

The dense-orbit step is the classical Kronecker theorem for irrational linear flows on a torus. The equality `(15)` is an immediate compactness/continuity consequence, and relative density of returns to a nonempty open set is standard minimal compact-dynamical/almost-periodic behavior. AF-309 already uses the same torus-density mechanism for the one-observable exact-zero incidence boundary.

The exponential-sum algebra is the classical Ritt/group-ring setting audited in AF-328, especially the rational support-control formulation of Everest--van der Poorten. The new algebraic step here is elementary inside that framework: decompose a hypothetical Bézout identity by frequency cosets, clear rational denominators, and evaluate the resulting Laurent identity at a common regular-octagon torus zero.

Relevant prior-art anchors already audited by the line include:

- Kronecker's approximation theorem for dense finite-dimensional torus flows;
- G. R. Everest and A. J. van der Poorten, **“Factorisation in the Ring of Exponential Polynomials,”** *Proceedings of the American Mathematical Society* 125(5), 1293–1298 (1997), DOI `10.1090/S0002-9939-97-03919-1`;
- J. F. Ritt, **“A Factorization Theory of Functions `sum a_i e^{alpha_i z}`,”** *Transactions of the American Mathematical Society* 29 (1927), 584–596;
- the Shapiro/common-zero literature recorded in AF-328.

The durable contribution is therefore not a new Kronecker or ideal-theory theorem. It is the exact **mechanism audit** for the AF-328 prime pair: the current observable has zero stability margin and no Bézout separation even though it has no common factor. That closes two natural routes without deciding exact incidence.

## Boundaries and failure modes

- Equation `(6)` does not prove `F(it)=G(it)=0` for any `t`. Infimum zero and attainment are different statements.
- Relative density in `(7)` is qualitative. No bound on `L_\varepsilon` is claimed, and its dependence on the exact prime support may be extremely poor.
- The continuous flow uses all real times. Restricting time to a prescribed sparse discrete set changes the recurrence problem.
- The regular-octagon target is an ambient torus configuration, not a rational-prime phase tuple. Its role is to certify zero target margin, not arithmetic incidence.
- Properness of `(F,G)` in `\mathcal E` does not imply an actual common complex zero of the one-variable functions. The relevant maximal ideals of the exponential-sum ring are not exhausted by point evaluations `s\mapsto s_0`.
- Coprime but noncomaximal behavior is not paradoxical in this multirank group-ring setting; the pullback Laurent polynomials have a codimension-two common algebraic zero without a common irreducible factor.
- The finding does not exclude a stronger certificate in a larger function algebra with additional inverse/closure operations. Any such enlargement would need an independently justified relation to the arithmetic observable and its own fidelity audit.
- Nothing here supplies a zeta zero count, analytic continuation theorem, critical-line statement, or RH implication.

## Consequence for the research line

AF-328 closed the common-factor route. AF-329 closes the adjacent **stable-separation and Bézout** routes for the same exact observable.

The surviving frontier is now sharply pointwise: determine whether a fixed rational-prime logarithmic direction actually intersects the codimension-two target `V(e_1,e_4)`, despite recurring arbitrarily close to it and despite the absence of any common exponential-sum factor. Any further progress should attack that exact incidence directly or change the retained representation; another continuous norm margin or another gcd/ideal reformulation of the same pair cannot supply the missing discriminator.