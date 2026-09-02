# WP-098 — Positive prime-torus quotients preserving coordinate observables cannot erase mixed-prime modes

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`. This closes the same-algebra, state-independent positive quotient / conditional-expectation escape left by `WP-096` and `WP-097`. The operator-algebra rigidity is classical; the Mathia-specific content is its application to the exact-cover prime-torus normal form and the sharp matched control supplied by `WP-097`. This does **not** rule out an auxiliary finite--archimedean enlargement formed before compression, a nonunital mass-changing construction, or a nonlinear geometric readout with its own sign theorem.

## Claim

Let `P` be a finite set of primes and let

\[
A_P=C(\mathbb T^P),
\qquad
z_p(\theta)=e^{i\theta_p}
\tag{1}
\]

be the prime-coordinate unitaries. These are exactly the character coordinates in the prime-torus representation of the exact-cover-positive cone classified in `WP-096`.

There is a strong rigidity obstruction to the most natural escape suggested by `WP-097`.

Let

\[
\Phi:A_P\longrightarrow B
\tag{2}
\]

be a **unital positive linear map** into a `C*`-algebra `B`. If every prime coordinate remains a unitary after the map,

\[
u_p:=\Phi(z_p)\in B,
\qquad
u_p^*u_p=u_pu_p^*=1,
\tag{3}
\]

then every `z_p` lies in the multiplicative domain of `Phi`, and therefore

\[
\boxed{
\Phi\!\left(\prod_{p\in P}z_p^{k_p}\right)
=\prod_{p\in P}u_p^{k_p}
\qquad(k_p\in\mathbb Z).
}
\tag{4}
\]

In particular, if the proposed quotient is a positive unital endomorphism of `A_P` that preserves the one-prime observables pointwise,

\[
\Phi(z_p)=z_p
\qquad(p\in P),
\tag{5}
\]

then

\[
\boxed{\Phi=\operatorname{id}_{A_P}.}
\tag{6}
\]

It cannot annihilate a single mixed-prime character while retaining all prime-coordinate characters. The same conclusion holds on the infinite prime torus by density of finite-coordinate trigonometric polynomials.

Thus a state-independent **positive/unital quotient, Markov operator, or conditional expectation on the same prime-torus algebra cannot keep the one-prime character data and delete the mixed-prime sector that pays for positivity in `WP-097`**.

The canonical linear projector that does exactly the desired Fourier deletion exists algebraically, but it is not positive. For `|P|=r`, let `E_p` average over every coordinate except `p`, and let `E_0` be full Haar averaging. Then

\[
\boxed{
\Pi_{\le1}
:=\sum_{p\in P}E_p-(r-1)E_0
}
\tag{7}
\]

is the unique Fourier projection onto constants plus characters supported on one prime coordinate. It fixes every `z_p^k`, kills every mixed-prime character, and is idempotent. Already on two coordinates it fails positivity:

\[
f(\theta_1,\theta_2)
=(1+\cos\theta_1)(1+\cos\theta_2)\ge0,
\tag{8}
\]

but

\[
\Pi_{\le1}f
=1+\cos\theta_1+\cos\theta_2,
\tag{9}
\]

so

\[
(\Pi_{\le1}f)(\pi,\pi)=-1.
\tag{10}
\]

Applied to the positive product completion of `WP-097`, `Pi_{<=1}` returns **exactly** the sparse carrier of `WP-096`. At the sharp endpoint `C=C_*`, the two-prime set `{2,3}` already gives a negative value at the simultaneous Poisson maximum. Hence the failure is not an asymptotic artifact: the canonical mixed-mode deletion destroys positivity with two prime coordinates.

A weaker, state-specific escape also fails globally at finite mass. If any operation — linear or nonlinear — outputs a positive measure with the same one-prime Weil moments, zero mixed-prime moments, and finite diagonal mass `C`, then `WP-096` applies to the output itself and forces

\[
C\ge
D(P)=2\sum_{p\in P}\frac{\log p}{\sqrt p-1}
\tag{11}
\]

on every finite prime set. Since `D(P)\to\infty`, no all-prime finite-mass positive output exists. A state-specific selector can evade the multiplicative-domain theorem only by ceasing to be a state-independent positive quotient, but it still cannot evade the sparse-output divergence.

## 1. Positive maps from the prime torus are completely positive

The domain `A_P=C(T^P)` is commutative. A classical consequence of Stinespring's theory is that every positive map from a commutative `C*`-algebra is completely positive. Therefore the unital map `Phi` in (2) obeys the Kadison--Choi Schwarz inequalities

\[
\Phi(a)^*\Phi(a)\le\Phi(a^*a),
\qquad
\Phi(a)\Phi(a)^*\le\Phi(aa^*).
\tag{12}
\]

For `a=z_p`, unitality and (3) make both inequalities equalities:

\[
\Phi(z_p)^*\Phi(z_p)
=1
=\Phi(z_p^*z_p),
\tag{13}
\]

and

\[
\Phi(z_p)\Phi(z_p)^*
=1
=\Phi(z_pz_p^*).
\tag{14}
\]

Choi's multiplicative-domain criterion therefore gives

\[
\Phi(z_pa)=\Phi(z_p)\Phi(a),
\qquad
\Phi(az_p)=\Phi(a)\Phi(z_p)
\tag{15}
\]

for every `a in A_P`. The same holds for `z_p^*`, so iteration gives (4) for arbitrary integer exponents.

If (5) holds, every trigonometric monomial is fixed. Their linear span is uniformly dense in `C(T^P)`, and `Phi` is bounded, hence (6) follows.

This is stronger than a statement about one particular `WP-097` measure. It says that **there is no geometry-independent positive channel on the same observable algebra whose meaning is “retain every prime coordinate but forget their mixed interactions.”** Retaining unitary coordinates already retains their products.

### Conditional expectations are even more rigid

If `E:A_P->D` is a conditional expectation onto a `C*`-subalgebra and fixes every coordinate `z_p`, then `D` contains the `C*`-algebra generated by those coordinates. But

\[
C^*(z_p:p\in P)=C(\mathbb T^P),
\tag{16}
\]

so `D=A_P` and `E=id`. Tomiyama's theorem places norm-one projections onto `C*`-subalgebras in exactly this conditional-expectation class. Thus changing the vocabulary from positive quotient to conditional expectation does not create an escape.

## 2. The exact sparse selector is the first-order Fourier/ANOVA projector, and it is not positive

For a character

\[
z^\alpha=\prod_{p\in P}z_p^{\alpha_p},
\qquad
\alpha\in\mathbb Z^P,
\tag{17}
\]

`E_p z^alpha` is nonzero exactly when `alpha` is supported in `{p}`, while `E_0 z^alpha` is nonzero exactly for `alpha=0`. Hence (7) has Fourier multiplier

\[
\widehat{\Pi_{\le1}}(\alpha)
=
\begin{cases}
1,&|\operatorname{supp}\alpha|\le1,\\
0,&|\operatorname{supp}\alpha|\ge2.
\end{cases}
\tag{18}
\]

This is precisely the desired “keep constants and one-prime rays, remove mixed-prime modes” operation.

Equation (10) is an arithmetic-free matched control showing that this projector is not order preserving. The obstruction is structural to product harmonic analysis, not to the particular Weil coefficients. Orthogonal projection in `L^2` onto first-order Hoeffding/ANOVA chaos is a positive **Hilbert-space operator** in the sense `Pi=Pi*=Pi^2`, but it is not a positivity-preserving map on functions or measures. Those two notions of positivity must not be conflated.

This distinction is decisive here. `WP-097` needs **order positivity of the carrier measure** to obtain a Gram form. Merely having an orthogonal projection on the ambient Hilbert space does not preserve that order cone.

## 3. The WP-097 product completion gives an exact two-prime counterexample

Write the `WP-097` finite-prime density as

\[
w^{\rm prod}_{P,C}(\theta)
=C\prod_{p\in P}
\left[
1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta_p)\right)
\right]
\ge0.
\tag{19}
\]

Its constant plus one-coordinate Fourier part is

\[
\Pi_{\le1}w^{\rm prod}_{P,C}
=C+\sum_{p\in P}(\log p)
\left(1-P_{p^{-1/2}}(\theta_p)\right)
=:w^{\rm sparse}_{P,C},
\tag{20}
\]

exactly the sparse density of `WP-096`.

Recall

\[
c_p=\frac{2\log p}{\sqrt p-1},
\qquad
C_*=c_2.
\tag{21}
\]

At the sharp positive-completion endpoint `C=C_*` and on only the two coordinates `P={2,3}`,

\[
w^{\rm prod}_{\{2,3\},C_*}\ge0,
\tag{22}
\]

whereas at `(theta_2,theta_3)=(0,0)`,

\[
\begin{aligned}
w^{\rm sparse}_{\{2,3\},C_*}(0,0)
&=C_*-c_2-c_3\\
&=-c_3\\
&=-\frac{2\log3}{\sqrt3-1}<0.
\end{aligned}
\tag{23}
\]

So the smallest-diagonal positive completion discovered in `WP-097` loses positivity immediately when the first mixed-prime sector is removed. No infinite-prime limit, regularization, or asymptotic estimate is needed for this witness.

For a larger fixed `C`, the same phenomenon occurs once `P` is large enough that `D(P)>C`. Thus mixed-prime interactions are not optional noise that a positive selector can forget. They are required by the order structure at every fixed finite normalization once sufficiently many prime coordinates are present.

## 4. A state-specific selector cannot save finite all-prime mass

The multiplicative-domain argument assumes a state-independent map on the observable algebra. One might weaken the requirement dramatically and ask only for some operation tailored to the particular positive state `mu_C` of `WP-097`.

Suppose the output is a positive finite measure `nu` whose Fourier coefficients satisfy

\[
\widehat\nu(p^k)
=-\frac{\log p}{p^{|k|/2}},
\qquad k\ne0,
\tag{24}
\]

for every prime coordinate, while

\[
\widehat\nu(r)=0
\tag{25}
\]

whenever the reduced rational `r` involves at least two distinct primes. Let

\[
C=\widehat\nu(1)<\infty.
\tag{26}
\]

Nothing about the construction of `nu` matters now. Restricting to any finite prime set gives exactly the sparse Fourier problem solved in `WP-096`, so positivity forces (11). Exhausting the primes contradicts finite `C`.

Therefore state dependence does not rescue the desired final selector at fixed finite diagonal mass. It can only hide where the diverging normalization was inserted. If an operation is allowed to increase the diagonal mass with `P`, the minimum required increase is already quantified by `D(P)` and diverges globally.

This closes a possible loophole in reading the multiplicative-domain theorem too strongly: the theorem is not being used to claim that **every** state-tailored nonlinear map is the identity. Instead there are two separate obstructions:

\[
\boxed{
\begin{array}{ll}
\text{state-independent positive/unital map}
&\Rightarrow\text{ mixed products cannot be erased},\\[2mm]
\text{state-specific positive sparse output}
&\Rightarrow C\ge D(P)\to\infty.
\end{array}}
\tag{27}
\]

Together they cover the two direct meanings of a positive quotient of the `WP-097` carrier.

## 5. Prior-art and novelty audit

The operator-algebra ingredients are classical and should not be presented as new mathematics.

- W. Forrest Stinespring, *Positive Functions on C*-Algebras*, Proceedings of the American Mathematical Society **6** (1955), 211--216, DOI `10.1090/S0002-9939-1955-0069403-4`, is the foundational dilation theorem and the classical source behind complete positivity for positive maps from commutative `C*`-algebras.
- Man-Duen Choi, *A Schwarz Inequality for Positive Linear Maps on C*-Algebras*, Illinois Journal of Mathematics **18** (1974), 565--574, DOI `10.1215/ijm/1256051007`, gives the Schwarz/equality machinery underlying the multiplicative-domain criterion used in (12)--(15).
- Jun Tomiyama, *On the Projection of Norm One in W*-Algebras*, Proceedings of the Japan Academy **33** (1957), 608--612, DOI `10.3792/pja/1195524885`, is the classical norm-one-projection / conditional-expectation boundary invoked after (16).

The first-order Hoeffding/ANOVA decomposition of product spaces is also classical. No prior-art claim is needed for its nonpositivity here because the explicit witness (8)--(10) proves it directly.

The durable Mathia-specific result is the conjunction of those classical rigidity facts with the exact carrier obtained in `WP-096`--`WP-097`: **the mixed-prime completion cannot be converted into the sparse Weil selector by an inherited same-algebra positive quotient.** The exact two-prime witness (23) makes the sign failure concrete on the sharp `WP-097` completion.

## 6. Scope boundary: what remains genuinely open

This finding does not close every quotient-like construction mentioned after `WP-097`.

**Auxiliary finite--archimedean enlargement.** A map

\[
C(\mathbb T^P)\longrightarrow B_{\rm enlarged}
\longrightarrow B_{\rm output}
\tag{28}
\]

may compress each coordinate unitary to a strict contraction rather than a unitary. Then equality in Schwarz fails and the multiplicative-domain theorem no longer forces mixed products to survive. Such a construction would need an independently forced auxiliary sector and an independent sign theorem; merely choosing a dilation to engineer the desired moments is not enough.

**Nonunital or mass-changing maps.** These can alter the diagonal/self-energy. Equation (11) shows the price of producing exact sparse output: unless another global term cancels or renormalizes it by an independently derived mechanism, the required mass diverges.

**Nonlinear geometric invariants.** A determinant, capacity, rank, quotient norm, or other nonlinear scalarization need not be a positive linear map on `C(T^P)`. It is therefore outside the multiplicative-domain theorem, but it also cannot inherit positivity merely from complete positivity; its sign theorem must be established separately.

**Mixed modes retained until a later global pairing.** The final Weil readout might arise only after coupling the finite carrier to an archimedean/global sector, so that mixed-prime modes are not deleted as a positive measure at all. This is the principal surviving route compatible with the present obstruction.

The research boundary is therefore sharper than after `WP-097`:

\[
\boxed{
\text{positive mixed-prime completion}
\not\xrightarrow[\text{same prime-torus algebra}]
{\text{positive quotient preserving prime coordinates}}
\text{sparse Weil carrier}.
}
\tag{29}
\]

Any surviving mechanism must alter the observable architecture **before** the sign is inherited, or provide a genuinely new nonlinear/global positivity theorem.

## Consequence for the research line

`WP-097` showed that cross-prime coupling can pay the finite positivity debt. The natural next hope was that a canonical positive quotient could then forget those auxiliary mixed interactions while retaining the one-prime Weil rays.

`WP-098` rules out that hope in its strongest intrinsic same-algebra form. A positive map that truly preserves each prime coordinate as an observable automatically preserves their products; the exact Fourier projector that deletes products is not positive; and even a state-tailored sparse positive output recreates the divergent `WP-096` diagonal requirement.

So the remaining question is no longer “which positive projection on the prime torus extracts the Weil selector?” There is no such state-independent projection with the required coordinate preservation. The live question is whether Mathia contains a **larger finite--archimedean object in which prime coordinates cease to be unitary before compression, or in which mixed-prime interactions survive until a later global pairing whose positivity is proved independently**.