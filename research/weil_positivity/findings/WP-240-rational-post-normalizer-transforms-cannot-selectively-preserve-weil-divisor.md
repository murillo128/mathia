# WP-240 — Rational post-normalizer transforms cannot selectively preserve the Weil divisor: monomials keep it whole, nonmonomials create level-set divisors

**Status:** `EXACT-DERIVED + RATIONAL-DIVISOR-RIGIDITY + MATCHED-SCALAR-CONTROL + CAYLEY-RESOLVENT-NO-GO + SHIFTED-FESHBACH-DETERMINANT-NARROWING + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-238` and `WP-239` show that once the `SL(2)` global intertwiner has already formed as

\[
M(s)=m(s)R(s),
\tag{1}
\]

with the completed-L-function information carried by the central scalar factor `m`, static channels and every scalar-homogeneous post-normalizer reduction retain the logarithmic derivative `m'/m` as one inseparable block. `WP-239` deliberately leaves nonhomogeneous operations such as Cayley transforms, shifted resolvents, and shifted Schur/Feshbach maps open.

There is an exact obstruction for the most canonical finite-dimensional version of that escape. Let

\[
F\in \mathbb C(z)^\times
\tag{2}
\]

be a fixed rational scalar postprocessor, chosen independently of the detailed zero/prime/Gamma decomposition of `m`, and put

\[
\Psi(s)=F(m(s)).
\tag{3}
\]

Then exactly one of two things happens.

1. If `F` has no zero or pole in `\mathbb C^\times`, then

\[
\boxed{F(z)=c z^k,\qquad c\ne0,\quad k\in\mathbb Z,}
\tag{4}
\]

and therefore

\[
\boxed{\frac{\Psi'}{\Psi}=k\frac{m'}m.}
\tag{5}
\]

The complete scalar explicit-formula channel survives with one common integer multiplicity. No zero-versus-prime-versus-Gamma separation has occurred.

2. If `F` is not a monomial, then it has a zero or pole at some finite nonzero value `a`. Wherever `m(s)=a`, the composition `F(m(s))` acquires a zero or pole controlled by that **level set**, even though `s` need not be a zero or pole of `m`. These new divisor points move under the matched replacement `m\mapsto c_0m`, although multiplication by `c_0\ne0` leaves the original zero/pole divisor of `m` unchanged.

Consequently a rational post-normalizer transform cannot both evade the scalar homogeneity obstruction and preserve the original completed-zeta divisor in a source-independent, matched-control-stable way. The rational transforms that are divisor-faithful under scalar-normalizer controls are exactly the monomials, and those reduce to the already-closed homogeneous case. Nonmonomial transforms gain apparent nonlinear freedom only by introducing level-set spectral data not present in the original divisor.

This closes, at determinant/logarithmic-derivative level, the ordinary rational Cayley/resolvent escape left open by `WP-239`, and it sharply restricts finite-dimensional shifted Feshbach reductions. It does **not** rule out nonrational or infinite-dimensional functional calculus, a scalar-sensitive geometry carrying genuinely new arithmetic input, a genuinely matrix-valued global normalizer, or a construction acting before the finite and archimedean factors have collapsed into `m`.

## 1. Rational divisor rigidity on the scalar normalizer

Write a nonzero rational function in reduced form

\[
F(z)=\frac{P(z)}{Q(z)},
\qquad \gcd(P,Q)=1.
\tag{6}
\]

Suppose first that every zero and pole of `F` on the Riemann sphere lies in `{0,\infty}`. Every finite zero of `P` must then be `0`, so `P(z)=a z^r`; every finite zero of `Q` must likewise be `0`, so `Q(z)=b z^q`. Reducedness removes any common power and gives

\[
F(z)=c z^{r-q}.
\tag{7}
\]

Conversely every monomial `c z^k`, with `k` allowed to be negative, has divisor supported only at `0` and `\infty`. Thus

\[
\boxed{
\operatorname{supp}\operatorname{div}(F)\subseteq\{0,\infty\}
\iff
F(z)=c z^k.
}
\tag{8}
\]

This is elementary rational-function theory; no arithmetic input enters it.

For arbitrary rational `F`, away from zeros and poles of `m` and `F(m)`, the chain rule gives

\[
\frac{d}{ds}\log F(m(s))
=
\frac{F'(m(s))}{F(m(s))}m'(s)
=
A_F(m(s))\frac{m'(s)}{m(s)},
\tag{9}
\]

where

\[
A_F(z):=z\frac{F'(z)}{F(z)}.
\tag{10}
\]

For a monomial, `A_F\equiv k`; the logarithmic derivative of the central normalizer is merely multiplied by one constant integer. For a nonmonomial, `A_F` is nonconstant and has singularities or zeros tied to the finite nonzero divisor of `F`. That is exactly where the postprocessor stops being divisor-neutral.

## 2. Nonmonomial transforms create level-set divisors

Let `a\in\mathbb C^\times` be a zero or pole of `F`, and write

\[
\nu=\operatorname{ord}_a F\ne0.
\tag{11}
\]

Suppose `s_0` is regular for `m`, `m(s_0)=a`, and

\[
\operatorname{ord}_{s_0}(m-a)=r\ge1.
\tag{12}
\]

Locally,

\[
F(z)=(z-a)^\nu u(z),\qquad u(a)\ne0,
\tag{13}
\]

so composition gives the exact divisor identity

\[
\boxed{
\operatorname{ord}_{s_0}(F\circ m)=\nu r.
}
\tag{14}
\]

Thus a finite nonzero zero/pole of `F` is pulled back to the level set `m^{-1}(a)`. These are not, in general, zeros or poles of `m`; they are additional spectral points selected by the chosen rational coordinate on the scalar scattering value.

The important statement is deliberately **not** that every nonmonomial `F` must add an extra divisor point for one fixed `m`: a particular meromorphic normalizer can omit a relevant value or special cancellations can occur. The exact obstruction is the stronger matched-control statement below.

## 3. Matched scalar controls make the new divisor movable while preserving the old one

Take any regular noncritical point `s_0` with

\[
m(s_0)\in\mathbb C^\times,
\qquad
m'(s_0)\ne0.
\tag{15}
\]

For a chosen finite nonzero divisor value `a` of a nonmonomial `F`, set

\[
c_0:=\frac{a}{m(s_0)}\ne0,
\qquad
\widetilde m(s):=c_0m(s).
\tag{16}
\]

Multiplication by a nonzero constant changes neither zeros nor poles of the original scalar normalizer:

\[
\operatorname{div}(\widetilde m)=\operatorname{div}(m).
\tag{17}
\]

But `\widetilde m(s_0)=a`, and because `m'(s_0)\ne0`, equation (14) produces a nonzero order of `F(\widetilde m)` at `s_0`. Therefore

\[
\boxed{
\text{nonmonomial rational postprocessing is not divisor-faithful under scalar-normalizer matched controls.}
}
\tag{18}
\]

This is the same kind of scalar-normalizer control already used in `WP-239`, where replacing `m` by `hm` showed that moving-compression geometry could not distinguish the analytic origin of a scalar factor. Here the control is even weaker: `h=c_0` is constant, so it leaves the entire original divisor unchanged. A postprocessor that nevertheless changes its output divisor is reacting to the **value coordinate** of `m`, not to the arithmetic zero/pole structure that drives the explicit formula.

Equation (18) also clarifies the logical boundary. One could choose a special rational `F` after exploiting detailed value-distribution facts of the actual zeta normalizer, perhaps proving that certain level sets are absent or cancel. That would be new arithmetic information encoded in the choice of postprocessor. Its sign and canonicity would require an independent theorem; it is not inherited from rational functional calculus or from Maaß–Selberg positivity.

## 4. Consequence for the Riemann explicit-formula channel

In Wong's `SL(2)` zeta specialization, the scalar scattering normalizer is

\[
m(s)=\frac{\xi(s)}{\xi(1+s)}
\tag{19}
\]

in his trace-formula parameter, and the continuous spectral term contains `m^{-1}m'`. Wong's explicit-formula calculation resolves that one scalar logarithmic derivative into the nontrivial-zero contribution together with finite-prime, archimedean, conductor/polar terms. This is the central-scalar bottleneck isolated in `WP-238`.

If `F` is monomial, (5) says that the transformed logarithmic derivative gives the same completed scalar distribution multiplied by `k`. The zero term cannot acquire a coefficient different from the finite-prime or Gamma companions.

If `F` is nonmonomial, the divisor of `F(m)` is no longer simply the divisor of `m` with a common multiplicity. The logarithmic derivative now has residues at the new level-set points described by (14), whenever they occur. A contour/explicit-formula treatment of `F(m)` must therefore account for those new points. The postprocessor has not isolated the old Weil zero functional; it has changed the meromorphic divisor whose residues are being sampled.

This is why a rational change of scattering coordinate is not the missing sign mechanism. It either preserves the whole central arithmetic package or replaces the target divisor by a larger/different one.

## 5. Ordinary Cayley and shifted-resolvent transforms fall in the level-set branch

The standard scalar Cayley/Möbius transforms are nonmonomial. For example,

\[
F(z)=\frac{1-z}{1+z}
\tag{20}
\]

has a zero at `z=1` and a pole at `z=-1`. Therefore its logarithmic derivative samples the level sets

\[
m(s)=1,
\qquad
m(s)=-1,
\tag{21}
\]

in addition to whatever information is carried by the original divisor. Likewise

\[
F(z)=\frac1{z-a}
\quad\text{or}\quad
F(z)=z-a,
\qquad a\ne0,
\tag{22}
\]

introduces poles or zeros at `m(s)=a`.

These transforms can be extremely natural for converting unitary, contractive, or dissipative objects into Herglotz/resolvent coordinates, and positivity/passivity theorems may apply to those new coordinates. The present obstruction does not dispute that positivity. It says that **the price of the nonhomogeneous rational coordinate is a new divisor**. Positivity of the transformed response is therefore not automatically positivity of the original Weil zero form.

This differs from `WP-184`. That finding concerns whether the isolated archimedean Gamma phase can be repaired inside bounded characteristic by Möbius/Cayley algebra. The present claim concerns the already-formed **global central scalar normalizer** and the fidelity of its divisor under rational postprocessing. The mechanisms and obstructions are distinct.

## 6. Finite-dimensional shifted Schur/Feshbach determinants obey the same dichotomy

`WP-239` proves exact homogeneity for the zero-shift Schur complement of `M=mR`. Consider instead a finite-dimensional block decomposition and a fixed additive shift `z\ne0`. Whenever the eliminated block is invertible, define

\[
\begin{aligned}
S_z(mR)
&:=mR_{PP}-zI\\
&\quad-m^2R_{PQ}(mR_{QQ}-zI)^{-1}R_{QP}.
\end{aligned}
\tag{23}
\]

The standard block determinant identity gives

\[
\boxed{
\det S_z(mR)
=
\frac{\det(mR-zI)}{\det(mR_{QQ}-zI)}.
}
\tag{24}
\]

For fixed `R`, `z`, and finite blocks, the right side is a rational function of the scalar variable `m`. Therefore the divisor-rigidity dichotomy applies directly to the determinant response.

If all finite nonzero zeros and poles cancel so that the rational dependence on `m` is a monomial, the shifted determinant has collapsed, as far as the scalar normalizer is concerned, to the same homogeneous branch: its logarithmic derivative carries `m'/m` only with a common integer multiplicity.

If the reduced rational function is not a monomial, its remaining finite nonzero zeros/poles correspond to level conditions on `m`, equivalently to shifted spectral equations such as `m\lambda=z` for relevant eigenvalues of the retained/full/eliminated blocks. Those are precisely the new level-set divisors of Sections 2–3.

Hence a finite-dimensional shifted Feshbach construction does not obtain a third rational possibility. At determinant/log-derivative level it must either reduce to a monomial in the central scalar or become sensitive to new scalar-value level sets. Exceptional cancellations are allowed; they place the response in the first branch rather than evading the theorem.

At `z=0`, equation (24) specializes to the scalar-homogeneous Schur identity already proved in `WP-239`. Thus the shifted and unshifted cases meet continuously at the exact structural boundary expected from that finding.

## 7. Positivity does not by itself restore divisor fidelity

The branch mandate asks for a geometric form whose nonnegativity is established independently **before** the arithmetic consequence is identified. Rational transformations often have exactly this appeal: Cayley transforms can trade unitary data for self-adjoint or Herglotz data, and Schur/Feshbach elimination can preserve passivity or positivity under suitable hypotheses.

But such a positivity theorem controls the transformed object. To yield the Riemann Weil criterion, one still needs an exact bridge from that transformed positive object to the original zero-divisor functional over the full admissible test class. The dichotomy above blocks the naive bridge through rational determinant/logarithmic-derivative scalarization:

\[
\text{monomial} \Rightarrow \text{whole central explicit formula retained},
\]

whereas

\[
\text{nonmonomial} \Rightarrow \text{level-set divisor sensitivity}.
\]

Thus rational nonhomogeneity is not free arithmetic selectivity. Any successful positive rational construction would additionally need a source-forced theorem showing why its level-set divisor cancels, is independently signed, or itself assembles with the old divisor into exactly the Weil form. That theorem is the missing mathematics, not a consequence of the rational transform.

## 8. Prior art and novelty boundary

No historical novelty is claimed for the mathematical ingredients. The facts that a rational function with divisor supported at `0` and `\infty` is a monomial, that orders multiply under composition at a finite level set, and that block determinants factor through Schur complements are standard elementary complex analysis and linear algebra.

The automorphic input is Tian An Wong, *Explicit formulas for the spectral side of the trace formula of SL(2)*, Acta Arith. 195 (2020), 149–175, arXiv `1608.02296`. Wong expresses the continuous spectrum through intertwining operators whose scalar normalizing factors are quotients of completed `L`-functions and converts their logarithmic derivatives into Riemann–Weil explicit-formula distributions. The relevant factorization and central-scalar consequence are already audited in `WP-237`--`WP-239`.

For Schur complements, the determinant identity in (24) is standard; `WP-239` already records Fuzhen Zhang (ed.), *The Schur Complement and Its Applications*, Springer, 2005, as a general reference. A bounded literature audit around rational/Cayley postprocessing of scattering normalizers did not identify a theorem that should be presented as the novelty here. Absence of an exact wording match is not evidence of historical novelty.

The Mathia-specific delta is instead a **routing obstruction**. `WP-239` explicitly left rational nonhomogeneous post-normalizer operations as an escape from scalar homogeneity. Equations (8), (14), and (24) show that, for divisor-sensitive determinant/log-derivative readouts, that escape has only two outcomes: return to homogeneity or introduce a new level-set divisor. This materially narrows which kind of post-scalar geometry can still plausibly explain the Weil sign.

## 9. Aggressive falsification and exact scope

**Could a nonmonomial rational function happen to preserve the divisor for the actual zeta normalizer?** Possibly on a special value-omission or cancellation theorem. The finding does not exclude that. It says such preservation is not source-independent and is not stable under the scalar-normalizer matched control (16). Establishing the exceptional theorem would itself be new arithmetic input requiring a separate sign/canonicity audit.

**Does a finite nonzero zero of `F` always produce an extra zeta point?** No. It produces a divisor wherever the corresponding value is attained. The uniform matched-control statement, not unconditional value-surjectivity of one fixed `m`, is the exact no-go.

**Does the constant multiplier control preserve unitary scattering normalization?** Not for arbitrary `c_0`. Equation (16) is an algebraic scalar-normalizer matched control, not a claim that every multiplier is a physical unitary scattering system. Its purpose is to test whether the purported geometry reads the original divisor or merely a chosen scalar coordinate. Stronger physically constrained controls would require their own value-distribution analysis.

**Could an entire zero-free transform avoid level-set divisors?** Yes. For instance `F(z)=\exp G(z)` can be zero-free without being a monomial. Such nonrational transforms lie outside the theorem. Their logarithmic derivatives introduce `G'(m)m'` and potentially very different growth, Hardy/Smirnov, Paley–Wiener, or operator-domain issues; those require a separate audit.

**Could infinite-dimensional determinant regularization evade the result?** Not automatically covered. Ordinary finite-dimensional rational determinants are covered by (24). Fredholm and modified determinants have additional analytic/regularization structure already treated in different contexts by `WP-177`--`WP-179`; a genuinely new global construction would need its own convergence and divisor theorem.

**Could a genuinely matrix-valued arithmetic normalizer evade central scalar rigidity?** Yes. If the finite and archimedean information remains noncommuting/operator-valued before determinant scalarization, the one-variable rational lemma no longer captures the available geometry. This remains one of the clean surviving routes.

**Could a construction act before `m` is formed?** Yes. The theorem is explicitly post-normalizer. A finite–archimedean pairing, cohomology, intersection form, or boundary response assembled before the local factors collapse into one scalar is untouched.

**Does this prove or imply RH?** No. It is a negative structural result. It eliminates a family of plausible but insufficient postprocessing moves and does not supply a global positive Weil form.

## 10. Consequence for the research line

The Maaß–Selberg branch has now crossed three successive structural gates. Height variation cannot resolve the `T`-independent explicit-formula block (`WP-237`). Static and scalar-homogeneous post-normalizer channel geometry cannot split the central normalizer (`WP-238`--`WP-239`). The present finding shows that **finite-dimensional rational nonhomogeneity does not provide selective divisor fidelity either**: it either collapses back to monomial homogeneity or replaces the original divisor by level-set data.

The clean surviving search space is therefore narrower. A serious next mechanism must supply at least one ingredient absent from rational post-scalar calculus: genuinely matrix-valued arithmetic normalizers, nonrational/infinite-dimensional geometry with a separately audited growth and divisor theorem, scalar-sensitive structure justified independently of the desired zeta decomposition, or—most naturally relative to the branch mandate—a finite–archimedean coupling that acts **before central scalar normalizer formation**.

This is exactly the distinction the Weil Positivity line needs to preserve. Producing a positive transform of an already-known scalar zeta response is not enough; the geometry must explain why the original arithmetic/archimedean Weil decomposition inherits a sign without replacing its divisor by a coordinate-selected one.