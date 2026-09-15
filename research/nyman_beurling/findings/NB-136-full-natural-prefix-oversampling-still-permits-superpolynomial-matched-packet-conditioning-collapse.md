# NB-136 — full natural-prefix oversampling still permits superpolynomial matched-packet conditioning collapse

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FULL-NATURAL-PREFIX + LOGARITHMIC-RANK + POLYNOMIAL-HEIGHT + ZERO-COUNT-COMPATIBLE + VINOGRADOV-KOROBOV-COMPATIBLE + SUPERPOLYNOMIAL-LOWER-FRAME-COLLAPSE + NB-128-BOUNDARY + NB-135-ROUTE-BOUNDARY + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`NB-135` closes the naive repair of `NB-133`--`NB-134` by adding more separately scalarized geometric recurrences: under the current polynomial-height zero-count gate, only finitely many integer bases have enough visible depth to certify a complete recurrence. One live escape is therefore to stop scalarizing base by base and use the whole natural prefix at once. That route is genuinely richer: `NB-128` proves that the phase vector `(n^{iT})_(n<=R)` resolves a **single common vertical translation** to scale `1/log R` throughout a height window of size `Theta(R)`.

The remaining question is whether that much oversampling automatically conditions a logarithmic-rank zero packet. It does not at the level of the same coarse source information used in `NB-132`--`NB-135`.

Fix `A>0`, choose

\[
0<c<0.10076A,
\tag{1}
\]

and let `B>0` be arbitrary. There is a family of distinct simple formal right-half-plane packets

\[
F_R=\{\rho_{j,R}:0\le j<d_R\},
\qquad
d_R=\lfloor c\log R\rfloor,
\tag{2}
\]

with

\[
|\Im\rho_{j,R}|\asymp R^A,
\qquad
1-\Re\rho_{j,R}
\asymp
(\log R)^{-2/3}(\log\log R)^{-1/3},
\tag{3}
\]

whose total vertical diameter is `o(1)`, which stay on the permitted side of the same explicit Vinogradov--Korobov zero-free boundary used in `NB-125` and fit below the shrinking-window numerical zero-count allowance used in `NB-133`.

Nevertheless the complete natural-prefix evaluation matrix

\[
V_R
:=
\bigl(n^{-\overline{\rho_{j,R}}}\bigr)_{
1\le n\le R,
\ 0\le j<d_R}
\in\mathbb C^{R\times d_R}
\tag{4}
\]

is superpolynomially ill-conditioned. More precisely, if

\[
S_R:=\sum_{n\le R}n^{-2\beta_R},
\qquad
\beta_R:=\Re\rho_{j,R},
\tag{5}
\]

then every column has Euclidean norm `S_R^(1/2)` and

\[
\boxed{
\frac{\sigma_{\min}(V_R)}{S_R^{1/2}}
\le
\exp\!\left(
-(cB+o(1))(\log R)^2
\right).
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\kappa_2(V_R)
\ge
\exp\!\left(
(cB+o(1))(\log R)^2
\right)
=R^{(cB+o(1))\log R}.
}
\tag{7}
\]

There is an even stronger pointwise formulation. One can choose a coefficient vector `u_R` with `||u_R||_2=1` such that the corresponding zero-power primitive

\[
P_R(n)
:=
\sum_{j=0}^{d_R-1}
(u_R)_j n^{-\overline{\rho_{j,R}}}
\tag{8}
\]

satisfies

\[
\boxed{
\max_{1\le n\le R}|P_R(n)|
\le
\exp\!\left(
-(cB+o(1))(\log R)^2
\right).
}
\tag{9}
\]

Thus the failure is not caused by selecting too few natural samples. **All `R` natural coordinates are present while the packet rank is only `Theta(log R)`.** The obstruction is a high-order near-confluent cancellation among extremely close ordinates.

This is a matched-control result. The points below are not asserted to be zeta zeros, and `(6)`--`(9)` do not assert that the actual Nyman zero-power coefficient vector occupies the bad singular direction. The durable conclusion is narrower and decisive for the current route: **zero-count rank control plus Vinogradov--Korobov horizontal depth do not by themselves give a polynomial lower frame bound for ordinary full-natural-prefix zero-power coordinates.** Any successful joint natural-grid certificate must use additional source-specific arrangement/coefficient information or be stable under near-confluence by construction.

## 1. A logarithmic-rank packet compatible with the current coarse source envelopes

Use the same explicit Vinogradov--Korobov constant already anchored for `NB-125`--`NB-133`,

\[
K_{\rm VK}=53.989.
\tag{10}
\]

Choose a height

\[
G_R=\frac12R^A+O(1),
\tag{11}
\]

and put

\[
\eta_R
:=
\frac{2}
{K_{\rm VK}
(\log G_R)^{2/3}
(\log\log G_R)^{1/3}},
\qquad
\beta_R:=1-\eta_R.
\tag{12}
\]

For the vertical spacing take

\[
\varepsilon_R:=R^{-B}
\tag{13}
\]

and define

\[
\boxed{
\rho_{j,R}
:=
\beta_R+i(G_R+j\varepsilon_R),
\qquad
0\le j<d_R.
}
\tag{14}
\]

All points are simple and distinct. Their total vertical diameter is

\[
(d_R-1)\varepsilon_R
=O(R^{-B}\log R)
=o(1).
\tag{15}
\]

The horizontal placement is deliberately the same safe-side calibration as in `NB-133`. At ordinate `G_R+o(1)`, the explicit forbidden depth is asymptotic to `eta_R/2`, while

\[
1-\beta_R=\eta_R.
\tag{16}
\]

Hence the formal points lie a fixed factor farther left than the zero-free boundary. The one-sided Vinogradov--Korobov law does not reject their horizontal location.

The packet also survives the stronger shrinking-window zero-count check from `NB-133`. Its actual vertical width is `O(R^{-B}log R)`, so the main term in the zero-count difference across that window is `o(log R)`. The two explicit endpoint errors allow

\[
(0.20152A+o(1))\log R
\tag{17}
\]

total zeros counted with multiplicity. Functional-equation symmetry pairs each right-half off-critical zero with a left-half zero at the same positive ordinate, leaving the numerical right-half allowance

\[
(0.10076A+o(1))\log R.
\tag{18}
\]

Because of `(1)`,

\[
d_R=c\log R+O(1)
<
(0.10076A+o(1))\log R.
\tag{19}
\]

So neither the current population envelope nor the current horizontal-depth envelope rules out the scales in `(14)`. As always for a matched control, compatibility with those necessary numerical laws is **not** evidence that the points occur as genuine zeros.

If desired, one may adjoin the functional-equation reflections and conjugates to form a globally symmetric formal configuration. The positive-frequency right-half packet `(14)` and the matrix `(4)` are unchanged.

## 2. The natural-prefix matrix has full column rank

For `rho_(j,R)` from `(14)`,

\[
n^{-\overline{\rho_{j,R}}}
=
n^{-\beta_R}
 e^{iG_R\log n}
 e^{ij\varepsilon_R\log n}.
\tag{20}
\]

Thus, after factoring the common nonzero row multiplier

\[
n^{-\beta_R}e^{iG_R\log n},
\tag{21}
\]

the columns are powers of

\[
z_n:=e^{i\varepsilon_R\log n}.
\tag{22}
\]

For large `R`,

\[
\varepsilon_R\log R<2\pi.
\tag{23}
\]

If `1<=m<n<=R` and `z_m=z_n`, then

\[
\varepsilon_R\log(n/m)
\in2\pi\mathbb Z.
\tag{24}
\]

The left side lies strictly between `0` and `2pi` by `(23)`, which is impossible. Hence all `z_n` are distinct. In particular, the first `d_R` rows contain an ordinary square Vandermonde matrix in `z_1,...,z_(d_R)`, multiplied by nonzero row factors. Therefore

\[
\boxed{\operatorname{rank}V_R=d_R.}
\tag{25}
\]

The conditioning collapse below is consequently genuine near-singularity, not an exact rank defect disguised as bad conditioning.

## 3. A high-order finite difference kills every natural coordinate simultaneously

Put

\[
m_R:=d_R-1
\tag{26}
\]

and define the alternating binomial vector

\[
x_{j,R}
:=
(-1)^{m_R-j}\binom{m_R}{j},
\qquad
0\le j\le m_R.
\tag{27}
\]

The binomial theorem gives the exact identity

\[
\sum_{j=0}^{m_R}
 x_{j,R}e^{ij\theta}
=
(e^{i\theta}-1)^{m_R}.
\tag{28}
\]

Applying `(28)` with `theta=varepsilon_R log n` and using `(20)`,

\[
(V_Rx_R)_n
=
n^{-\beta_R}e^{iG_R\log n}
\left(
 e^{i\varepsilon_R\log n}-1
\right)^{m_R}.
\tag{29}
\]

Since `|e^(it)-1|<=|t|`, every natural coordinate satisfies

\[
|(V_Rx_R)_n|
\le
n^{-\beta_R}
(\varepsilon_R\log n)^{m_R}
\le
(\varepsilon_R\log R)^{m_R}.
\tag{30}
\]

The coefficient norm is exact as well. Vandermonde's convolution gives

\[
\|x_R\|_2^2
=
\sum_{j=0}^{m_R}\binom{m_R}{j}^2
=
\binom{2m_R}{m_R}.
\tag{31}
\]

For the unit vector

\[
u_R:=\frac{x_R}{\|x_R\|_2},
\tag{32}
\]

we therefore obtain the pointwise bound

\[
\boxed{
\max_{n\le R}|(V_Ru_R)_n|
\le
\frac{(\varepsilon_R\log R)^{m_R}}
{\sqrt{\binom{2m_R}{m_R}}}.
}
\tag{33}
\]

The central binomial coefficient satisfies

\[
\sqrt{\binom{2m}{m}}
=
\frac{2^m}{(\pi m)^{1/4}}(1+o(1)).
\tag{34}
\]

Using `varepsilon_R=R^(-B)` and `m_R=c log R+O(1)`, the logarithm of the right side in `(33)` is

\[
\begin{aligned}
&m_R\bigl(-B\log R+\log\log R-\log2\bigr)
+O(\log m_R)\\
&\qquad=
-cB(\log R)^2
+c\log R\log\log R
+O(\log R).
\end{aligned}
\tag{35}
\]

Hence

\[
\boxed{
\max_{n\le R}|(V_Ru_R)_n|
\le
\exp\!\left(
-(cB+o(1))(\log R)^2
\right),
}
\tag{36}
\]

which is `(9)`. In particular the complete natural prefix can be superpolynomially insensitive to a unit coefficient direction even though its number of rows exceeds the packet rank by a factor `Theta(R/log R)`.

The mechanism is transparent in `(28)`: the clustered packet forms a finite difference of order `m_R`, so the first `m_R-1` Taylor orders in the tiny phase increment cancel identically. Ordinary oversampling does not undo that local confluence.

## 4. The same witness forces superpolynomial spectral conditioning

Every column of `V_R` has the same Euclidean norm because all points have the same real part:

\[
\|V_Re_j\|_2^2
=
\sum_{n\le R}n^{-2\beta_R}
=S_R.
\tag{37}
\]

Equation `(29)` gives

\[
\|V_Rx_R\|_2^2
\le
S_R(\varepsilon_R\log R)^{2m_R}.
\tag{38}
\]

Therefore

\[
\sigma_{\min}(V_R)
\le
S_R^{1/2}
\frac{(\varepsilon_R\log R)^{m_R}}
{\sqrt{\binom{2m_R}{m_R}}}.
\tag{39}
\]

This proves `(6)` by the same asymptotic calculation as `(35)`. On the other hand,

\[
\sigma_{\max}(V_R)
\ge
\|V_Re_0\|_2
=S_R^{1/2}.
\tag{40}
\]

Dividing `(40)` by `(39)` yields

\[
\boxed{
\kappa_2(V_R)
\ge
\frac{\sqrt{\binom{2m_R}{m_R}}}
{(\varepsilon_R\log R)^{m_R}}
=
\exp\!\left(
(cB+o(1))(\log R)^2
\right),
}
\tag{41}
\]

which is `(7)`.

Because the column norms are already identical, this collapse is not repaired by the most obvious column normalization. It is the relative geometry of the clustered columns that fails.

## 5. Why this does not contradict the positive phase modulus in NB-128

`NB-128` compares two **individual common translates**. If one ordinate moves by `Delta`, some natural coordinate detects the factor `n^(iDelta)` at scale `Delta log R` until the section-height boundary. That statement is correct and remains useful.

The present packet asks a different question: can `Theta(log R)` individually visible columns cancel each other as a linear family? Equation `(28)` answers yes. For every `n<=R`, all adjacent phase increments satisfy

\[
|\varepsilon_R\log n|
\le
R^{-B}\log R
=o(1),
\tag{42}
\]

and the alternating binomial combination cancels them to order `m_R`. Thus **single-height identifiability does not imply multi-root lower-frame conditioning**.

This also differs materially from `NB-130`--`NB-131`. Those findings use enough formal rank to interpolate a fixed finite natural prefix exactly and then exploit vertical translation/reinterpolation. Here the rank is only `Theta(log R)`, the observation set itself grows all the way to `R`, the height is polynomial in `R`, and the conclusion is a quantified near-null direction rather than arbitrary exact interpolation.

Finally, the obstruction is stronger than the finite-base alias of `NB-126`--`NB-134`: there is no exact phase period being exploited. The complete natural grid sees every individual ordinate. What fails is stable separation of a growing **cluster** of ordinates.

## 6. What this closes, and what remains open

The current source envelope supplies two useful facts in the narrow polynomial-height regime: the right-half packet rank is at most logarithmic, and actual zeros cannot approach `Re s=1` more closely than the Vinogradov--Korobov depth. `NB-136` shows that these facts still leave ordinary natural-grid inversion without a polynomial lower frame bound. Population and radial depth do not control near-confluence.

Accordingly, a route of the form

\[
\text{zero count}
+\text{zero-free depth}
+\text{all samples }1,\ldots,R
\Longrightarrow
\text{stable ordinary zero-power inversion}
\tag{43}
\]

cannot be justified from those inputs alone.

This does **not** rule out the natural-grid route itself. There are several logically distinct escapes. A genuine-zero theorem could control local arrangement strongly enough to exclude large near-confluent clusters. A joint certificate could use derivative/confluent coordinates so that coalescing roots are represented stably rather than inverted as nearly duplicate columns. The actual source coefficient vector might satisfy structure preventing significant projection onto the bad singular directions. Or one may bypass coefficient recovery entirely and construct a target-bearing functional that remains coercive under clustering.

The scale exposed here is informative. Ordinary natural-grid phases resolve one ordinate at scale `1/log R` by `NB-128`. The control above places adjacent ordinates at `R^(-B)`, far below that scale, and then amplifies the resulting local degeneracy with `Theta(log R)`-th order cancellation. To obtain ordinary Vandermonde-style conditioning one therefore needs **arrangement information at the same local phase scale**, not merely a global count over a band.

A uniform pairwise minimum spacing is probably stronger than the route truly needs and would make the argument brittle to isolated close pairs. A more natural next source question is cluster-aware: bound how many relevant zero-power directions can occupy a phase cell substantially smaller than `1/log R`, or prove that the target-bearing coefficient mass cannot concentrate on the corresponding near-confluent singular subspace.

## 7. Representation and adversarial audit

The packet points are formal matched controls, not claimed zeta zeros. The zero-count and zero-free checks above establish only that the two coarse source summaries used in the current route do not exclude their scales. No existence statement is inferred from a counting upper bound.

The matrix is genuinely full column rank by `(25)`, so the lower-frame collapse is not an artifact of repeated roots. Every point is simple. The coefficient witness is normalized in ordinary Euclidean coefficient norm, and all columns have the same Euclidean norm, so the conclusion is not created by unequal column scaling.

The bad direction `u_R` is not asserted to equal the coefficient vector produced by the actual Nyman projection or by residues of genuine zeta zeros. Thus `(36)` does not prove small Nyman distance, near-perfect target capture, or small Burnol mass. It proves failure of a **uniform ordinary-coordinate conditioning implication** from the admitted positional source laws.

The construction also does not say that a confluent reparametrization is ill-conditioned. Indeed `(28)` is exactly the signal that derivative-type coordinates may be the correct local variables when roots coalesce. Any future positive result must therefore state which coordinate system or target functional is being conditioned; condition number is representation-dependent.

The choice `varepsilon_R=R^(-B)` is not load-bearing. Any spacing with `varepsilon_R log R -> 0` can be inserted into `(33)`; the displayed polynomial spacing is convenient because it makes the superpolynomial exponent explicit. The arbitrary constant `B>0` emphasizes that the current source envelopes supply no compensating minimum-spacing scale.

## 8. Prior-art audit

The generic numerical phenomenon is established territory. Targeted literature search finds the clustered-Vandermonde and superresolution literature, including Batenkov--Demanet--Goldman--Yomdin on conditioning of partial nonuniform Fourier matrices with clustered nodes and Batenkov--Diederichs--Goldman--Yomdin on spectral properties of clustered Vandermonde matrices. Those works show that small singular values are controlled by local cluster geometry and can deteriorate rapidly with cluster multiplicity and separation. No novelty is claimed for the generic fact that clustered exponential/Vandermonde columns are ill-conditioned.

The line-local contribution is the exact splice with the Nyman--Beurling source gate: `(14)` simultaneously respects the logarithmic shrinking-window rank allowance and the Vinogradov--Korobov horizontal-depth allowance already used in `NB-133`, while `(28)` gives a self-contained witness that defeats the **entire growing natural prefix**, not only a fixed geometric trace. The proof does not import a singular-value theorem from that literature.

A targeted zeta-spacing check found results about statistics or existence of small/large gaps, typically on the critical line and often under additional hypotheses, but no result needed here is imported from them. `NB-136` makes no claim that genuine zeros realize the matched cluster. The exact missing source statement is left explicit rather than replaced by a literature assumption.

No new specialized external estimate is load-bearing. The zero-count and Vinogradov--Korobov constants are already anchored in `SOURCES.md`, while the conditioning estimate is derived directly from the binomial identity `(28)`. Therefore `SOURCES.md` remains unchanged.

The durable update to the current frontier is: **the full natural prefix repairs finite-base phase aliasing but not logarithmic-rank near-confluence.** Under the present coarse source laws, even `R` natural samples can have a superpolynomially small lower frame bound for a `Theta(log R)` polynomial-height matched packet. The next theorem must control actual-zero/coefficient arrangement at the cluster scale or use a representation that remains stable when those ordinates coalesce.