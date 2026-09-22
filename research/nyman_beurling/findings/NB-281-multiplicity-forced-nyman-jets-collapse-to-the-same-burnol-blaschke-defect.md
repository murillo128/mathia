# NB-281 — Multiplicity-forced Nyman jets collapse to the same Burnol Blaschke defect

**Status:** `EXACT-DERIVED + NB-280-HIGHER-JET-ESCAPE-CLOSED + MULTIPLICITY-HERMITE-COLLISION + FINITE-DIRICHLET-INTERPOLATION + PRIOR-ART-CLASSICALIZATION + HIGH-ZERO-O1G`.

`NB-280` identifies the canonical point-value certificate from `NB-279` with the finite Burnol/Blaschke defect and leaves one explicit escape: a zero of multiplicity greater than one forces higher derivative data, so perhaps the corresponding Hermite channel carries more Hardy mass than point sampling.

For the legal finite Nyman residual

\[
r_P(s)
=
\frac1s-
\frac{\zeta(s)}s\bigl(P(s)-P(1)\bigr),
\tag{1}
\]

that escape can be classified exactly.

If `rho` is a right-half zeta zero of multiplicity `m`, then every finite Dirichlet source satisfies

\[
\boxed{
 r_P^{(\ell)}(\rho)
 =
 \left(\frac1s\right)^{(\ell)}\!\!(\rho)
 =
 \frac{(-1)^\ell\ell!}{\rho^{\ell+1}},
 \qquad 0\le \ell<m.
}
\tag{2}
\]

These are all the source-independent jets forced by the zero. At the next order,

\[
\boxed{
 r_P^{(m)}(\rho)
 =
 \frac{(-1)^m m!}{\rho^{m+1}}
 -
 \frac{\zeta^{(m)}(\rho)}{\rho}
 \bigl(P(\rho)-P(1)\bigr),
}
\tag{3}
\]

and the second term is genuinely free. More strongly, for any finite set of distinct nontrivial zeros `rho_j`, the values

\[
P(\rho_j)-P(1)
\tag{4}
\]

can be prescribed independently by a finite Dirichlet polynomial. Thus the first jet beyond the actual zero multiplicity is independently source-adjustable across every finite packet.

The complete collection of **forced** Hermite data therefore says only that `r_P-1/s` is divisible by the finite Blaschke product carrying the same zero multiplicities. Its exact least Hardy norm is

\[
\boxed{
\mathcal E_{\mathrm{jet}}(Z)
=
1-|B_Z(1)|^2
=
1-
\prod_{\rho\in Z}
\left(
1-
\frac{2\Re\rho-1}{|\rho|^2}
\right)^{m_\rho}.
}
\tag{5}
\]

This is not a new destination quantity. It is precisely the multiplicity-counted Burnol defect already controlled in `NB-116`. For every finite packet of actual right-half zeros above height `G`, counted with multiplicity,

\[
\boxed{
\mathcal E_{\mathrm{jet}}(Z)
\ll \frac1G.
}
\tag{6}
\]

Hence multiplicity-forced derivative sampling does **not** rescue the `NB-279`/`NB-280` boundary route at high ordinate. At simple zeros the only forced datum is the value `r_P(\rho)=1/\rho`; at a multiple zero the additional forced jets merely repeat the same Blaschke multiplicity already present in Burnol's product. Any derivative information beyond that multiplicity necessarily measures the finite arithmetic source itself and must be priced through its section geometry rather than treated as another universal zero-sampling certificate.

## 1. Exact jet law at a zeta zero

Put

\[
Q_P(s):=P(s)-P(1),
\qquad
k_1(s):=\frac1s.
\tag{7}
\]

Then `(1)` is simply

\[
r_P-k_1
=
-\frac{\zeta Q_P}{s}.
\tag{8}
\]

Let `rho` be a nontrivial zero of exact multiplicity `m`. Write locally

\[
\zeta(s)
=(s-\rho)^m a_\rho(s),
\qquad
a_\rho(\rho)\ne0.
\tag{9}
\]

Both `Q_P` and `1/s` are holomorphic at `rho`. Therefore the right-hand side of `(8)` has a zero of order at least `m`, and

\[
(r_P-k_1)^{(\ell)}(\rho)=0,
\qquad 0\le\ell<m.
\tag{10}
\]

This proves `(2)`.

At order `m`, every Leibniz term in which fewer than `m` derivatives hit `zeta` vanishes. Consequently

\[
\left(\frac{\zeta Q_P}{s}\right)^{(m)}\!(\rho)
=
\zeta^{(m)}(\rho)\frac{Q_P(\rho)}{\rho},
\tag{11}
\]

which proves `(3)`.

Equation `(11)` is the sharp transition. Zero multiplicity forces agreement with the canonical target through order `m-1`, and no algebraic cancellation from the Nyman normalization extends that agreement to order `m` unless the particular source happens to satisfy `Q_P(\rho)=0`.

For a simple zero, `m=1`, so the distinction is especially stark:

\[
r_P(\rho)=\frac1\rho,
\qquad
r_P'(\rho)
=-\frac1{\rho^2}
-\frac{\zeta'(\rho)}\rho Q_P(\rho).
\tag{12}
\]

The first derivative is already source-dependent.

## 2. The first free jet is independently adjustable on every finite packet

It is not enough to observe that one source can change one derivative. A possible boundary repair could still hope that the source-dependent terms in `(3)` obey a hidden finite-packet relation. They do not at the level of unrestricted finite Dirichlet sources.

### Lemma: finite Dirichlet values interpolate arbitrary finite data

Let `z_1,\ldots,z_N` be distinct complex numbers, none equal to `1`. Consider the map

\[
T:P\longmapsto
\bigl(P(z_j)-P(1)\bigr)_{j=1}^N
\tag{13}
\]

from finite Dirichlet polynomials to `\mathbb C^N`. Then

\[
\boxed{T\text{ is surjective}.}
\tag{14}
\]

To prove this, suppose a vector `lambda=(lambda_j)` annihilates the range. Testing only the Dirichlet monomials

\[
P_n(s)=n^{-s},
\qquad n\ge2,
\tag{15}
\]

gives

\[
\sum_{j=1}^N
\lambda_j
\bigl(n^{-z_j}-n^{-1}\bigr)
=0
\qquad(n\ge2).
\tag{16}
\]

Define the exponential polynomial

\[
F(x)
:=
\sum_{j=1}^N\lambda_j e^{-z_jx}
-
\left(\sum_{j=1}^N\lambda_j\right)e^{-x}.
\tag{17}
\]

Then

\[
F(\log n)=0
\qquad(n\ge2).
\tag{18}
\]

The function `F` is entire of exponential type. If it were nonzero, Jensen's formula applied after translating away from any zero at the origin would give only

\[
N_F(R)=O(R)
\tag{19}
\]

zeros in a disk of radius `R`. But `(18)` supplies at least

\[
\lfloor e^R\rfloor-1
\tag{20}
\]

distinct real zeros in that disk for large `R`, a contradiction. Hence `F\equiv0`.

The exponents `z_1,\ldots,z_N,1` are distinct, so the corresponding exponential functions are linearly independent. Thus every `lambda_j=0`. The range of `T` has trivial annihilator in the finite-dimensional space `\mathbb C^N`, proving `(14)`.

Apply the lemma to distinct nontrivial zeta zeros `rho_j`. Given arbitrary complex numbers `q_j`, there is a finite Dirichlet polynomial with

\[
Q_P(\rho_j)=q_j
\qquad(1\le j\le N).
\tag{21}
\]

If `m_j` is the multiplicity of `rho_j`, equation `(3)` becomes

\[
r_P^{(m_j)}(\rho_j)
=
\frac{(-1)^{m_j}m_j!}{\rho_j^{m_j+1}}
-
\frac{\zeta^{(m_j)}(\rho_j)}{\rho_j}q_j.
\tag{22}
\]

Because exact multiplicity gives `\zeta^{(m_j)}(\rho_j)\ne0`, the first non-forced derivative at each node can be chosen independently across the packet.

This statement is deliberately **unpriced**: the interpolating Dirichlet polynomial may require a long section or large coefficients. The conclusion is only that there is no source-independent Hermite identity beyond the zero multiplicity. If a future argument makes `(22)` coercive by restricting the arithmetic section and charging the interpolation cost, that would be a genuinely different mechanism and remains live.

## 3. All multiplicity-forced jets form one finite Blaschke model space

Let `Z` be a finite set of distinct right-half zeros, and let `m_\rho` denote the actual multiplicity of each zero. Form the finite half-plane Blaschke product

\[
B_Z(s)
:=
\prod_{\rho\in Z} b_\rho(s)^{m_\rho},
\tag{23}
\]

where

\[
|b_\rho(s)|
=
\left|
\frac{s-\rho}{s+\overline\rho-1}
\right|.
\tag{24}
\]

Consider the affine Hermite interpolation class

\[
\mathcal A_Z
:=
\left\{
 f\in H^2(\Re s>1/2):
 f^{(\ell)}(\rho)
 =k_1^{(\ell)}(\rho),
 \ 0\le\ell<m_\rho,
 \ \rho\in Z
\right\}.
\tag{25}
\]

A function belongs to `\mathcal A_Z` exactly when `f-k_1` vanishes at each `rho` to order at least `m_\rho`. Finite inner-outer factorization therefore gives

\[
\boxed{
\mathcal A_Z
=
k_1+B_ZH^2.
}
\tag{26}
\]

Thus the derivative reproducing kernels associated with the multiplicity constraints do not create a new subspace beyond the standard finite model space

\[
\mathcal K_{B_Z}
:=
H^2\ominus B_ZH^2.
\tag{27}
\]

The least-norm function in `(26)` is the model-space projection of `k_1`:

\[
\inf_{f\in\mathcal A_Z}\|f\|_{H^2}^2
=
\|P_{\mathcal K_{B_Z}}k_1\|^2.
\tag{28}
\]

With the normalization of `NB-279`--`NB-280`, `\|k_1\|^2=1`, and the model-space kernel formula gives

\[
\|P_{\mathcal K_{B_Z}}k_1\|^2
=1-|B_Z(1)|^2.
\tag{29}
\]

At `s=1`, each factor obeys

\[
|b_\rho(1)|^2
=
1-
\frac{2\Re\rho-1}{|\rho|^2}.
\tag{30}
\]

Equations `(23)`, `(29)`, and `(30)` prove `(5)`.

So the confluent/Hermite Gram that one would obtain by writing derivative reproducing kernels explicitly is only another coordinate representation of the same finite model-space projection. Its inverse conditioning can be complicated, but for the canonical target jet vector it collapses to the multiplicity-counted Blaschke product exactly as the ordinary Cauchy Gram collapsed in `NB-280`.

## 4. The high-zero jet budget is already `O(1/G)`

Define

\[
\delta_\rho
:=
\frac{2\Re\rho-1}{|\rho|^2}.
\tag{31}
\]

For a finite packet with multiplicities,

\[
\mathcal E_{\mathrm{jet}}(Z)
=
1-
\prod_{\rho\in Z}
(1-\delta_\rho)^{m_\rho}.
\tag{32}
\]

The elementary inequality `1-\prod(1-x_i)\le\sum x_i`, with repeated factors counted according to multiplicity, gives

\[
\mathcal E_{\mathrm{jet}}(Z)
\le
\sum_{\rho\in Z}m_\rho\delta_\rho.
\tag{33}
\]

`NB-116` proves, using Selberg zero density and counting zeros with multiplicity, that for all actual right-half zeros above height `G`,

\[
\sum_{\substack{\zeta(\rho)=0\\\Re\rho>1/2\\|\Im\rho|\ge G}}
\delta_\rho
\ll \frac1G,
\tag{34}
\]

where the sum itself is already multiplicity-counted. Therefore every finite packet in that tail satisfies `(6)`.

This closes the most direct reading of the higher-jet escape in `NB-280`: replacing distinct-point sampling by all derivative constraints that are **universally forced by the actual multiplicities** cannot produce an order-one high-zero Hardy certificate. The multiplicities are already charged in the Burnol tail, and the whole charge is `O(1/G)`.

## 5. What the result does and does not close

### 5.1 Simple zeros force no derivative channel beyond point values

At a simple zero the universal condition is only

\[
r_P(\rho)=1/\rho.
\tag{35}
\]

The derivative can be moved arbitrarily by changing `Q_P(\rho)`, and the interpolation lemma shows that these first derivatives can be moved independently on any finite set of simple zeros. Thus a derivative Gram built at distinct simple zeros is not a source-free analogue of the `NB-279` point-sampling Gram.

### 5.2 Multiple zeros add jets, but exactly in Burnol's multiplicity

If a zero has multiplicity `m>1`, the forced derivatives of orders `0,\ldots,m-1` are real additional bounded functionals in the Hardy half-plane. But together they are precisely the statement that the error is divisible by `b_\rho^m`. Their aggregate least-norm cost is already represented by the exponent `m` in `(32)`.

The first derivative order not represented by that Blaschke multiplicity is source-dependent by `(3)` and independently adjustable by `(22)`.

### 5.3 This does not price finite arithmetic interpolation

Surjectivity in `(14)` allows the Dirichlet polynomial length and coefficient norm to grow without restriction. It therefore does **not** prove that the free jets in `(22)` are cheap in a fixed Báez-Duarte section, in the source Hilbert norm, or under any coefficient constraint.

That distinction is now the useful frontier. A viable finite-source mechanism would have to show that making `Q_P(\rho_j)` take the values needed to neutralize or exploit the free jets has a nontrivial arithmetic-section cost. Such a statement would couple the zero-side Hermite data to the actual finite Dirichlet synthesis map and would no longer reduce to a universal Blaschke projection.

### 5.4 Critical-line zeros remain outside this interior sampling theorem

All Hardy point and derivative evaluations here are at `\Re\rho>1/2`. Critical-line zeros lie on the boundary of `H^2(\Re s>1/2)`, where these evaluation functionals are not bounded. No limiting Hermite interpolation claim at `\Re\rho=1/2` is made.

### 5.5 The matched Ford controls remain controls, not zero assertions

The phase-aligned packets of `NB-225`--`NB-231` remain compatibility constructions. This finding does not assume that actual zeta zeros realize them. It says instead that even if actual high zeros possess multiplicities, the universally forced Hardy jet mass of any finite packet is bounded by the same inverse-height Burnol budget.

## 6. Prior-art and novelty audit

The model-space part of this finding is classical rather than new. Burnol's *A note on Nyman's equivalent formulation of the Riemann Hypothesis* states the Blaschke projection product with zeta zeros counted according to multiplicity. That source is already anchored in `SOURCES.md` and is the load-bearing prior-art boundary behind `NB-052` and `NB-280`.

Burnol's later *A lower bound in an approximation problem involving the zeros of the Riemann zeta function* goes further in a neighboring finite-cutoff problem: it constructs vectors indexed by pairs `(rho,k)` with `0\le k<m_\rho` and explicitly uses the multiplicity jet structure. That paper is also already anchored in `SOURCES.md` under the quantitative approximation boundary. The fresh prior-art audit therefore confirms that derivative vectors attached to zero multiplicity must not be presented as a new Nyman idea.

Standard finite model-space/Hermite interpolation likewise identifies repeated Blaschke zeros with derivative reproducing kernels. No novelty is claimed for that Hardy-space fact.

The substantive line-local contribution is the collision with the exact finite residual of `NB-276`--`NB-280`:

1. equations `(2)`--`(3)` locate the precise boundary between **forced** and **source-dependent** jets for every legal finite Nyman residual;
2. the interpolation lemma `(14)` shows that the first source-dependent jet is not merely noncanonical but independently adjustable across every finite packet of distinct zeros;
3. equations `(26)`--`(32)` show that exhausting all universally forced jets gives exactly the multiplicity-counted Burnol defect, so `NB-116` immediately supplies the high-zero `O(1/G)` ceiling.

No new durable external dependency is introduced, so `SOURCES.md` does not change.

## 7. Falsification and follow-up

The exact statements `(2)`, `(3)`, `(14)`, and `(26)` are algebraic/Hardy identities. They would be falsified by any of the following:

- a finite legal residual whose difference from `1/s` fails to vanish to the zeta multiplicity at an interior zero;
- a nonzero annihilator of the finite Dirichlet evaluation map `(13)`;
- an interior Hardy function satisfying the multiplicity jets for which `f-k_1` is not divisible by the corresponding finite Blaschke product.

The natural next test is no longer another zero-only Hermite Gram. It is to fix an actual finite arithmetic section, write the map from its Dirichlet coefficients to the free values

\[
\bigl(Q_P(\rho_j)\bigr)_j,
\tag{36}
\]

and compare the least coefficient/source norm required for prescribed data against the Ford scaling. If that finite interpolation map has a source-native lower bound that survives high ordinate, it would be genuinely new information. If it remains cheap on matched controls, then the higher-jet route is closed more broadly and the next mechanism must be nonlinear or use a different boundary observable.

## Conclusion

The higher-jet possibility left open by `NB-280` splits cleanly at the actual zero multiplicity. A zero of multiplicity `m` forces exactly the target jets of orders `0` through `m-1`; their full Hardy interpolation cost is the same multiplicity-counted Burnol/Blaschke defect and is `O(1/G)` for actual high zeros. The order-`m` jet and everything beyond it are source-dependent, with the first free jet independently adjustable across any finite packet by finite Dirichlet polynomials.

Thus **universal derivative sampling does not provide a new high-zero boundary currency**. Any surviving jet-based mechanism must pay for the finite arithmetic source needed to realize its derivative data; that source-side interpolation cost, not another zero-only Gram, is the next quantity worth testing.