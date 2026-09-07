# ANF-085 — proportional vertical fibers are globally safe at all heights

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + ALL-HEIGHTS + HETEROGENEOUS-HORIZONTAL-MULTIPLICITY + MIXED-REAL-COMPLEX + STRUCTURAL-BOUNDARY`. `ANF-035` proves that attaching one common nonzero symmetric vertical fiber to a simple real base cannot lower the energy below the corresponding uniform real collision. `ANF-081` later closes the full real-multiplicity problem for one fixed central-notch profile, and `ANF-083` lifts that certificate to an arbitrary complex tube of fixed height. Combining the exact product factorization behind `ANF-035` with the heterogeneous real certificate of `ANF-081` removes the height restriction completely for a strictly larger complex class: the horizontal multiplicities may be arbitrary, the common vertical fiber may contain a real layer, and its nonreal heights may be arbitrarily large.

Fix the central-notch spectrum and constant supplied by `ANF-081`,

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad
F_s=\widehat J_s,
\qquad
q_s>0,
\tag{1}
\]

so that every finite real multiset `Z` satisfies

\[
\sigma(Z)\ge 2|Z|-q_s^{-1}E_{F_s}(Z)
\tag{2}
\]

and

\[
2-\frac{C(J_s)}{q_s}>2-C_{\rm MT}.
\tag{3}
\]

Let `x_1,...,x_r` be distinct real centers with arbitrary positive integer horizontal multiplicities `a_1,...,a_r`. Let `Y` be any nonempty finite symmetric real multiset,

\[
Y=-Y,
\tag{4}
\]

where zero is allowed and every nonzero height may be arbitrarily large. Form the product multiset

\[
W
=
\biguplus_{i=1}^r a_i\,(x_i+iY).
\tag{5}
\]

Thus every horizontal center carries a **proportional copy of the same vertical profile**; equivalently, after grouping by horizontal center and vertical height, the occupation matrix has product form `n_{ij}=a_i b_j`.

Then, with `N=|W|`, one has the same affine certificate as on the real axis,

\[
\boxed{
\sigma(W)\ge 2N-q_s^{-1}E_{F_s}(W),
}
\tag{6}
\]

with no restriction on the heights in `Y`. If `Y` contains a nonzero height, the stronger estimate

\[
\boxed{
E_{F_s}(W)\ge 2q_sN
}
\tag{7}
\]

holds. Consequently the fixed central-notch profile of `ANF-081` is globally safe on every separable height-center occupation pattern, including arbitrary horizontal multiplicity variation and mixed real/nonreal product layers.

## 1. Product factorization survives arbitrary horizontal multiplicities

Write the horizontal structure factor

\[
A_X(\alpha)
:=
\sum_{i=1}^r a_i e^{-2\pi i\alpha x_i}.
\tag{8}
\]

Represent the symmetric vertical multiset by a possible zero multiplicity `b_0>=0` and positive heights `y_1,...,y_d` with multiplicities `b_j>=1`. Its total size is

\[
m:=|Y|=b_0+2\sum_{j=1}^d b_j,
\tag{9}
\]

and its Fourier--Laplace factor is

\[
B_Y(\alpha)
:=
\sum_{y\in Y}e^{2\pi\alpha y}
=
 b_0+2\sum_{j=1}^d b_j\cosh(2\pi\alpha y_j).
\tag{10}
\]

For every real `alpha`,

\[
\boxed{
B_Y(\alpha)\ge B_Y(0)=m.
}
\tag{11}
\]

The product geometry (5) gives the exact factorization

\[
S_W(\alpha)=A_X(\alpha)B_Y(\alpha).
\tag{12}
\]

Let `R(W)` be the real-part collapse of `W`. It is exactly the real multiset obtained by multiplying every horizontal occupancy by `m`:

\[
R(W)=mX,
\qquad
S_{R(W)}(\alpha)=mA_X(\alpha).
\tag{13}
\]

Because `J_s>=0`, equations (11)--(13) imply pointwise in the spectral integral

\[
\begin{aligned}
E_{F_s}(W)
&=\int_{-1}^{1}J_s(\alpha)
 |A_X(\alpha)|^2 B_Y(\alpha)^2\,d\alpha\\
&\ge
m^2\int_{-1}^{1}J_s(\alpha)|A_X(\alpha)|^2\,d\alpha\\
&=E_{F_s}(mX).
\end{aligned}
\tag{14}
\]

This is the same positive-cone mechanism as `ANF-035`, but the base is now an arbitrary real multiset rather than a simple set, and a zero-height layer in `Y` is allowed. Neither horizontal collisions nor vertical height size enter the estimate.

If `Y` contains a nonzero height, symmetry forces `m>=2`. Hence every site of the collapsed real multiset `mX` has multiplicity at least two, so

\[
\sigma(mX)=0,
\qquad
|mX|=|W|=N.
\tag{15}
\]

Applying the all-real theorem (2) to `mX` yields

\[
E_{F_s}(mX)\ge2q_sN.
\tag{16}
\]

Together with (14), this proves (7), and since `sigma(W)>=0`, equation (6) follows immediately. If `Y={0}` with multiplicity one, `W` is itself real and (6) is exactly `ANF-081`; if the zero fiber has multiplicity at least two, the same argument as (15)--(16) applies.

## 2. The previously open mixed-real bookkeeping is harmless in product form

`ANF-035` deliberately excluded zero from the common vertical fiber and took the horizontal base to be simple. Those restrictions mattered at that stage because the real certificate had not yet been proved for arbitrary occupancies, and a real layer can change the simple-point count.

After `ANF-081`, that bookkeeping ceases to be an obstruction for product fibers. For example, take

\[
Y=\{0,-y,+y\},
\qquad y>0.
\tag{17}
\]

and allow arbitrary occupancies `a_i` at the horizontal centers. The complex multiset contains a real layer with occupancies `a_i` together with two nonreal layers carrying the same occupancies. Some real points of `W` may therefore be simple. Nevertheless its real-part collapse has occupancy `3a_i` at every center and hence no simple sites. The spectral factor

\[
1+2\cosh(2\pi\alpha y)\ge3
\tag{18}
\]

forces its energy above that no-simple real collision, which is already covered by `ANF-081`.

Thus neither heterogeneous horizontal multiplicity nor the presence of a real layer can create a new complex falsifier as long as all horizontal centers carry proportional vertical fibers.

## 3. The complementary-height frontier now requires center--height correlation

`ANF-083` proves that **every** finite conjugation-invariant multiset is safe when all heights lie in one fixed tube `|Im z|<=h_*`, independently of cardinality and pair count. The present result is transverse to that theorem: it permits unbounded heights but imposes separability of the center-height occupation pattern.

Combining the two statements gives a sharper necessary condition for any remaining complex obstruction to the central-notch certificate. After grouping a conjugation-invariant multiset by distinct horizontal centers `x_i` and distinct vertical levels `y_j`, a counterexample must simultaneously

1. leave the uniform tube of `ANF-083`, so at least one occupied level satisfies `|y_j|>h_*`; and
2. have a **nonseparable** occupation matrix: its vertical profiles at the different horizontal centers cannot all be proportional to one common symmetric profile.

In matrix language, product/rank-one center-height coupling is globally harmless. Any surviving obstruction must use genuine center-height correlation, i.e. rank at least two after zero rows and columns are removed. This condition is necessary, not sufficient: the low-cardinality theorems earlier in the line already eliminate many rank-two patterns.

This sharpens the large-height research target. Large imaginary displacement by itself is not the missing mechanism, nor is arbitrary multiplicity variation by itself. What remains is the interaction between horizontal phase and **relative changes of the vertical profile from center to center**.

## 4. Stress tests and evidence boundary

The proof uses only three exact inputs: the structure-factor identity for `E_{F_s}`, spectral nonnegativity `J_s>=0`, and the all-real affine theorem of `ANF-081`. There is no Taylor expansion, small-height approximation, cardinality truncation, or numerical optimization. The factorization is stable under repeated horizontal sites because those repetitions are absorbed into the integers `a_i`, and it is stable under arbitrary finite symmetric vertical multiplicities because all terms in (10) are nonnegative and `cosh u>=1`.

The conclusion would fail as a proof strategy once different centers carry nonproportional vertical profiles: then `S_W` is a sum of several distinct Fourier--Laplace factors rather than the single product (12), and their horizontal phases can interfere destructively. `ANF-067` already exhibits the local form of precisely such a phenomenon when one displaced pair interacts with several real anchors. Therefore (6) is not being extrapolated beyond the separable class.

The Fourier transform factorization of product measures is classical background. A targeted prior-art check did not identify a literature result supplying the line-specific affine consequence (6); the load-bearing argument here is the exact finite factorization above combined with the already established Mathia real certificate. No new durable external dependency is required, so `SOURCES.md` is unchanged.

## Research consequence

The complementary-height problem left by `ANF-083` can now be restricted without loss to nonseparable center-height occupation patterns. In particular, searches over common-height clouds, common multi-height fibers, proportional vertical multiplicity profiles, or those same families with an added common real layer cannot produce the missing falsifier regardless of how large the heights become. The next useful invariant should measure deviation from this product cone rather than absolute height alone; a quantitative rank-one-plus-defect decomposition is the natural local gate.