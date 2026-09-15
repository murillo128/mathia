---
id: WP-310
title: Classical moment-Schur reduction cannot start on the critical Mangoldt Herglotz source
branch: weil_positivity
status: supported
kind: critical-mangoldt-moment-schur-admissibility-obstruction
claim_strength: exact obstruction for the infinity-based Schur/Nevanlinna moment reduction explicitly left open by WP-309; the canonical reflected critical Mangoldt Herglotz response has logarithmic rather than finite-mass 1/z asymptotics, and inserting it into the formal first Schur step with any fixed finite moment parameter eventually leaves the Herglotz class
created: 2026-09-15
related: [WP-304, WP-305, WP-308, WP-309]
prior_art:
  - Daniel Alpay, Aad Dijksma, and Heinz Langer, The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials, Operator Theory: Advances and Applications 190 (2009), 27-63, DOI 10.1007/978-3-7643-9919-1_4, arXiv:0711.4236, for the infinity-based Schur transform under finite-moment asymptotics and its compression realization
  - Barry Simon et al. classical real-line Schur/moment framework as summarized in Wall Polynomials on the Real Line: A Classical Approach to OPRL Khrushchev's Formula, Constructive Approximation 56 (2022), for the explicit observation that logarithmic Nevanlinna functions need not admit even the first real-line Schur step
---

# WP-310 — Classical moment-Schur reduction cannot start on the critical Mangoldt Herglotz source

## Claim

`WP-309` closes holomorphic scalar **automorphism gauges** but correctly leaves genuinely function-level Schur/Nevanlinna transforms open because those transforms can encode source moments and operator compressions. The most canonical such escape is the classical Schur transform at the reference point `infinity`. For the already-forced critical Mangoldt source, however, that transform does not merely fail to repair the Gamma curvature: its first step is not admissible.

Let

\[
\mu_+=\sum_{n\ge2}\frac{\Lambda(n)}{n+1}\,\delta_{\log n}
\tag{1}
\]

be the positive source of `WP-304`/`WP-305`, and let `m_-` be its reflected regularized Herglotz response. `WP-305` proves

\[
M(R):=\mu_+([0,R])
=R+C_++\varepsilon(R),
\qquad \varepsilon(R)\to0,
\tag{2}
\]

and

\[
m_-(iy)
=L(y)+iQ(y),
\tag{3}
\]

with

\[
L(y)=\log y-B+\frac{A_0}{y^2}+o(y^{-2}),
\qquad
Q(y)=\frac\pi2+\frac{C_+}{y}+o(y^{-1}),
\qquad A_0>0.
\tag{4}
\]

The infinity-based Nevanlinna Schur step instead starts from a function with finite-mass moment asymptotics

\[
n(z)=-\frac{s_0}{z}-\frac{s_1}{z^2}+\cdots,
\qquad 0<s_0<\infty,
\tag{5}
\]

and in its weakest first-step form already requires

\[
n(z)=-\frac{s_0}{z}+o(z^{-1}).
\tag{6}
\]

For such an input the first transform is

\[
\widetilde n(z)=-\frac{s_0}{n(z)}-z,
\tag{7}
\]

up to the real normalization `s_1/s_0` when the next moment exists.

The critical Mangoldt source violates the entrance condition in two equivalent exact ways:

\[
\boxed{M(R)\to\infty}
\tag{8}
\]

and

\[
\boxed{|m_-(iy)|\asymp\log y\quad\text{rather than}\quad O(y^{-1}).}
\tag{9}
\]

Moreover, this is not merely a domain-of-definition objection. If one nevertheless inserts `m_-` into the formal first Schur formula with **any fixed finite** `s_0>0` and any real constant `c`,

\[
S_{s_0,c}(z)
:=-\frac{s_0}{m_-(z)}-z+c,
\tag{10}
\]

then along `z=iy`

\[
\operatorname{Im}S_{s_0,c}(iy)
=
\frac{s_0Q(y)}{L(y)^2+Q(y)^2}-y
=
-y+O\!\left(\frac1{\log^2 y}\right)<0
\tag{11}
\]

for all sufficiently large `y`. Thus the formal transform eventually lies in the **lower** half-plane and is not a Nevanlinna/Herglotz function.

Hence

\[
\boxed{
\text{the classical infinity/moment Schur reduction cannot start on the canonical critical Mangoldt Herglotz source.}
}
\tag{12}
\]

A valid escape must first add new structure: a finite-reference-point interpolation transform, a cutoff coupled to a separately derived renormalization law, an operator-valued/generalized resolvent construction, a compression not equivalent to the classical finite-moment step, or an independently positive archimedean channel. Those remain open. The result rules out only the canonical **source-moment-at-infinity** Schur escape left by `WP-309`.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-NEVANLINNA-SCHUR-DOMAIN + CRITICAL-INFINITE-MASS-FAILURE + DIRECT-POSITIVITY-FAILURE + MATCHED-TRUNCATION-CONTROL + PRIOR-ART-REDIRECT + NOT-WEIL-POSITIVITY`.

## 1. The critical source is outside the finite-moment Schur class

For a Nevanlinna function in the classical `R_0` moment class, Alpay--Dijksma--Langer use

\[
n(z)=\int_{\mathbb R}\frac{d\sigma(t)}{t-z}
\tag{13}
\]

with `sigma` bounded and nondecreasing. Its total mass is

\[
s_0=\int_{\mathbb R}d\sigma(t)<\infty,
\tag{14}
\]

and the first asymptotic condition is exactly (6). Higher Schur steps require further finite moments and give the expansion

\[
n(z)
=-\frac{s_0}{z}-\frac{s_1}{z^2}-\cdots.
\tag{15}
\]

The reflected measure underlying `m_-` has the same mass growth as (2), so its total mass is infinite. The regularized Herglotz representation is still legitimate because Herglotz theory only requires the weighted integrability appropriate to

\[
\int\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\mu(t),
\tag{16}
\]

not finite total mass. But precisely that larger Herglotz class is too broad for the moment-Schur step at infinity.

Equation (4) is the response-level form of the same obstruction. A finite positive measure gives a Cauchy response vanishing like `1/z`; the critical Mangoldt measure has asymptotic density one and gives a logarithmic response. No real additive normalization changes this scale.

This distinction is classical rather than a new theorem about Nevanlinna functions. The Mathia-specific point is that the source forced earlier in this line lands exactly on the wrong side of that classical admissibility boundary.

## 2. The formal first step actively breaks Herglotz positivity

The classical first Schur transform is not an arbitrary fractional-linear recoding. The cancellation between

\[
-\frac{s_0}{n(z)}
\qquad\text{and}\qquad
-z
\tag{17}
\]

works because (6) implies

\[
-\frac{s_0}{n(z)}=z+o(z).
\tag{18}
\]

For the critical Mangoldt response there is no such cancellation. From (3)--(4),

\[
-\frac{s_0}{m_-(iy)}
=
-\frac{s_0L(y)}{L(y)^2+Q(y)^2}
+i\frac{s_0Q(y)}{L(y)^2+Q(y)^2}.
\tag{19}
\]

Because `L(y)~log y` and `Q(y)->pi/2`, its imaginary part is only

\[
\frac{s_0Q(y)}{L(y)^2+Q(y)^2}
=
O(\log^{-2}y).
\tag{20}
\]

The `-iy` in (10) therefore dominates with the wrong sign, proving (11).

The additive term `s_1/s_0` of the stronger Schur transform is real and cannot affect this argument. Thus no choice of finite first two moment parameters can rescue the formal first step.

One could make the positive term in (11) compete with `y` only by allowing `s_0` itself to grow with the spectral variable, at least on the scale

\[
s_0(y)\gtrsim y\log^2y.
\tag{21}
\]

But then `s_0` is no longer a zeroth source moment and (10) is no longer the classical Schur transform. Such a spectral-variable cutoff/renormalization law would be genuinely new structure and would have to be derived independently rather than chosen to repair the target.

## 3. Constant projective preprocessing does not put the source into the moment class

A possible objection is to first apply a Herglotz-preserving Möbius map and only then start the moment-Schur algorithm. `WP-308` already classifies the asymptotic alternatives for a fixed real projective map

\[
T(w)=\frac{aw+b}{cw+d},
\qquad ad-bc>0.
\tag{22}
\]

If `c=0`, then `T(m_-(iy))` remains affine in the logarithmic end and therefore still has magnitude `Theta(log y)`.

If `c!=0`, then

\[
T(w)=\frac ac-\frac{ad-bc}{c(cw+d)},
\tag{23}
\]

so after subtracting the finite real boundary limit `a/c`,

\[
T(m_-(iy))-\frac ac
=O\!\left(\frac1{\log y}\right).
\tag{24}
\]

This is still parametrically larger than `1/y`. In particular the strongest elementary inversion control,

\[
-\frac1{m_-(iy)},
\tag{25}
\]

has magnitude `Theta(1/log y)`, so

\[
y\left|\frac1{m_-(iy)}\right|\longrightarrow\infty.
\tag{26}
\]

Therefore no fixed projective Herglotz recoding converts the canonical logarithmic source into an input satisfying (6). This is a new consequence of the asymptotic classification already established in `WP-308`; no additional projective freedom is being assumed.

`WP-309` further shows that a jointly holomorphic family of pointwise Herglotz **automorphisms** cannot evade this conclusion by depending on `z`: such a family is constant. Genuinely function-level transforms remain distinct, but the classical moment-Schur transform is precisely what (8)--(12) exclude.

## 4. Matched control: every finite cutoff admits the Schur step

The obstruction appears only in the global critical limit. Truncate the reflected positive measure at energy `R` and write

\[
\mu_R:=\mu_-|_{[-R,0]},
\qquad
s_0(R):=\mu_R([-R,0])=M(R).
\tag{27}
\]

Because `mu_R` is a finite positive measure with compact support, all of its moments are finite. Its unregularized Cauchy transform

\[
n_R(z)=\int_{-R}^0\frac{d\mu_R(t)}{t-z}
\tag{28}
\]

has the full moment asymptotic

\[
n_R(z)
=-\frac{s_0(R)}z-rac{s_1(R)}{z^2}-\cdots
\tag{29}
\]

and the classical Schur algorithm applies exactly.

But (2) gives

\[
s_0(R)=R+C_++o(1)\longrightarrow\infty.
\tag{30}
\]

Thus the admissibility is not stable under the critical `R->infinity` source limit. Normalizing each cutoff to a probability measure divides the response by `s_0(R)` and therefore changes the already-fixed arithmetic normalization; retaining the original normalization makes the zeroth Schur parameter diverge.

This matched control is important. The conclusion is **not** that Schur reduction is incompatible with positive arithmetic measures. It works perfectly at every finite cutoff. What fails is the passage from those finite-moment problems to the canonical density-one global source without an additional renormalization theorem.

The finding does not assert that no such renormalized limit can exist. It says that any such limit is extra mathematics, not the standard moment-Schur step already justified by positivity.

## 5. Subtracting the unit-density background gives a signed object, not the missing positive moment source

`WP-305` isolates the asymptotic density by writing

\[
\nu=\mu_+-dE,
\qquad
\nu([0,E])=C_++\varepsilon(E).
\tag{31}
\]

This subtraction is analytically useful: it exposes the finite remainder moment `A_0` and the `y^{-2}` curvature. But it does not repair the Schur positivity problem. The measure `nu` is a **signed** difference between the discrete arithmetic source and the Lebesgue background.

Consequently its Cauchy remainder

\[
h(z)=\int\frac{d\nu(E)}{E-z}
\tag{32}
\]

is not supplied with the positive-measure Herglotz theorem that underwrites the classical Schur compression. Using `nu` as the moment source would therefore obtain finiteness by first removing the universal positive background with a sign-changing counterterm.

That maneuver may still be useful inside a larger geometry if the subtraction itself is forced as a Schur complement, boundary quotient, or other independently positive construction. But as a standalone repair it simply moves the missing sign theorem into the renormalization step, which is exactly what the `weil_positivity` mandate forbids us to assume.

## 6. Prior-art and novelty audit

The analytic facts behind the obstruction are classical. Alpay--Dijksma--Langer explicitly formulate the infinity-based Schur transformation for Nevanlinna functions having asymptotic expansions

\[
n(z)=-s_0/z-s_1/z^2-\cdots
\tag{33}
\]

and identify the coefficients with moments of a bounded nondecreasing measure. They also show that the first Schur step corresponds at operator level to passing from a self-adjoint resolvent realization to an orthogonal-complement/compression realization. That is exactly the attractive positivity mechanism being tested here.

A separate modern exposition of the real-line Schur algorithm notes explicitly that logarithmic Nevanlinna functions are examples for which even the first step need not be possible. Hence no novelty is claimed for the statement that `log`-type Herglotz functions lie outside the regular moment-Schur class.

The repository-level contribution is narrower and source-specific:

\[
\boxed{
\text{Mathia-forced critical Mangoldt source}
\Longrightarrow
\text{density-one/infinite mass}
\Longrightarrow
\text{logarithmic Herglotz end}
\Longrightarrow
\text{no classical infinity Schur step},
}
\tag{34}
\]

with the additional direct check (11) that formally applying the first transform destroys the Herglotz sign at large imaginary energy.

The bounded audit also exposes the correct surviving boundary. Alpay--Dijksma--Langer distinguish the infinity/moment transform from Schur-type transforms at a finite point in the upper half-plane, and generalized Nevanlinna/interpolation theory contains broader transformations. Those are not ruled out here. They require additional interpolation data or realization structure and therefore must be tested as new Mathia-native mechanisms rather than inherited automatically from the source measure.

Relevant references:

- D. Alpay, A. Dijksma, H. Langer, *The Schur transformation for Nevanlinna functions: operator representations, resolvent matrices, and orthogonal polynomials*, arXiv:0711.4236; especially the asymptotic condition (1.1), first transform (1.2), moment representation (1.3), and the weaker first-step condition in Section 2: https://arxiv.org/abs/0711.4236
- *Wall Polynomials on the Real Line: A Classical Approach to OPRL Khrushchev's Formula*, Constructive Approximation 56 (2022), Section 3, for the regularity/moment gate of the real-line Schur algorithm and logarithmic counterexamples.

## 7. Consequence for the research frontier

The scalar Herglotz route is now more sharply partitioned. `WP-305` shows that the canonical reflected source has the wrong first Riemann-specific Gamma curvature. `WP-308` rules out constant projective output repair. `WP-309` rules out promoting that projective gauge to a jointly holomorphic spectral-variable automorphism family. `WP-310` removes the next canonical escape: the classical source-moment Schur compression at infinity cannot even be initiated on the global critical source.

The useful surviving mechanisms are therefore ones that genuinely alter the realization before the critical limit: a finite-reference-point transform with independently forced interpolation data, a cutoff/renormalization law arising from geometry rather than target fitting, an operator-valued or multi-channel compression, or a nonseparable finite--archimedean coupling. Any of these must produce its own positive form and then recover the Gamma/polar terms without importing them.

This remains a negative structural result. It does not construct the global Weil form, does not rule out all Nevanlinna or Schur-type machinery, and does not imply Weil positivity or RH.

## Conclusion

The classical moment-Schur transform offers exactly the kind of mechanism this research line wants in principle: positivity is inherited from a Hilbert-space resolvent and a canonical compression. But its entrance condition is finite source mass with `1/z` asymptotics. The canonical critical Mangoldt source has density one, infinite total mass, and a logarithmic Herglotz end.

Forcing the standard first formula onto that source makes its imaginary part asymptotic to `-y`, so positivity fails outright. Finite cutoffs confirm that Schur theory itself is sound; what is missing is a canonical positive renormalization that survives the critical infinite-mass limit. That missing renormalization, not another formal Schur iteration, is now the actual mathematical burden of this route.
