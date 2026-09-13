# AF-311 — Baker linear-log obstructions remain generically compatible at the pentagon

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `TRANSCENDENCE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-310 shows that the first unresolved saturated exact-zero geometry, the equilateral pentagon, is already compatible with the strongest obstruction obtained from **integer** phase characters. Baker's theorem pushes the arithmetic side further, from integer coefficients to algebraic coefficients, but the pentagon remains compatible with that stronger constraint as well.

Let `p_1,...,p_5` be distinct rational primes and put

\[
\lambda_j=\log(p_j/p_5),\qquad 1\le j\le4.
\tag{1}
\]

Then Baker's theorem on linear forms in logarithms gives

\[
\boxed{
\lambda_1,\lambda_2,\lambda_3,\lambda_4
\text{ are linearly independent over }\overline{\mathbb Q}.
}
\tag{2}
\]

Consequently, for every `t\ne0`, if

\[
\theta=t\lambda\in\mathbb R^4,
\tag{3}
\]

then the algebraic-affine relation space

\[
\mathcal R(\theta)
=
\left\{
(a,b)\in\overline{\mathbb Q}^{\,4}\times\overline{\mathbb Q}:
 a\cdot\theta=2\pi b
\right\}
\tag{4}
\]

has

\[
\boxed{
\dim_{\overline{\mathbb Q}}\mathcal R(\theta)\le1.
}
\tag{5}
\]

The dimension is independent of the chosen angle lift modulo `2\pi\mathbb Z^4`. Thus (5) is a lift-invariant strengthening of AF-310's cyclic integer-character bound: a distinct-prime common-time phase point can satisfy at most one independent exact affine angle relation with algebraic coefficients.

However, this stronger arithmetic restriction still does **not** exclude pentagon closure. Around the regular pentagon there is a real-analytic two-dimensional patch of the lifted exact-zero manifold on which the points satisfying any nontrivial relation of the form

\[
a\cdot\theta=2\pi b,
\qquad
(a,b)\in\overline{\mathbb Q}^{\,4}\times\overline{\mathbb Q},
\tag{6}
\]

form a meagre set. Equivalently,

\[
\boxed{
\text{a dense residual set of nearby exact pentagon lifts has }
\mathcal R(\theta)=\{0\}.
}
\tag{7}
\]

Therefore the `k=5` zero manifold is generically compatible not merely with unique factorization / integer-character rank, but with the full **algebraic-linear** independence supplied by Baker theory. Any unconditional obstruction that settles the five-prime exact-zero problem must use structure beyond forcing algebraic-coefficient linear relations among the prime logarithms or their lifted angles.

This does not prove that a five-prime exact zero exists. It identifies a sharper boundary of a whole proof mechanism: the classical linear-forms-in-logarithms layer is arithmetically true but geometrically non-decisive at the first unresolved polygon.

## Baker upgrades rational independence to algebraic-linear independence

The four positive algebraic numbers

\[
\alpha_j=p_j/p_5
\tag{8}
\]

are multiplicatively independent. Indeed, if integers `m_j` satisfy

\[
\prod_{j=1}^4\alpha_j^{m_j}=1,
\]

then

\[
\prod_{j=1}^4p_j^{m_j}
=p_5^{\sum_jm_j},
\]

and unique factorization forces every `m_j=0`.

Hence the real logarithms `\lambda_j=\log\alpha_j` are linearly independent over `\mathbb Q`. Since they are real, adjoining `2\pi i` preserves rational linear independence. Baker's classical theorem then implies that the logarithms themselves are linearly independent over the field of algebraic numbers. This proves (2).

This is strictly stronger than the rational-log independence used in AF-306--AF-310. In particular, for every nonzero algebraic vector `a\in\overline{\mathbb Q}^4`,

\[
\sum_{j=1}^4 a_j\log(p_j/p_5)\ne0.
\tag{9}
\]

No integer-character argument is needed for (9); it is a direct linear-forms-in-logarithms obstruction.

## The algebraic-affine relation space has dimension at most one

Let `t\ne0` and `\theta=t\lambda`. Consider the projection

\[
\beta:\mathcal R(\theta)\to\overline{\mathbb Q},
\qquad
(a,b)\mapsto b.
\tag{10}
\]

This map is injective. If `b=0`, then (4) gives

\[
t\,a\cdot\lambda=0.
\]

Since `t\ne0`, equation (2) forces `a=0`. Therefore the kernel of `\beta` is trivial. Because the target of (10) is one-dimensional over `\overline{\mathbb Q}`,

\[
\dim_{\overline{\mathbb Q}}\mathcal R(\theta)\le1,
\]

which proves (5).

Equivalently, if two algebraic-affine relations

\[
a\cdot\theta=2\pi b,
\qquad
c\cdot\theta=2\pi d
\tag{11}
\]

hold, then they must be proportional over `\overline{\mathbb Q}`. Eliminating the common time gives

\[
(da-bc)\cdot\lambda=0,
\]

so Baker independence forces `da=bc`.

The bound is sharp for the unconstrained prime phase curve. Given any nonzero real algebraic vector `a`, equation (9) makes `a\cdot\lambda\ne0`, and the choice

\[
t=\frac{2\pi}{a\cdot\lambda}
\tag{12}
\]

produces the nontrivial relation `(a,1)\in\mathcal R(t\lambda)`. Thus one algebraic-affine relation can be created by choosing the time; two independent ones cannot coexist.

### Lift invariance

If another angle lift is

\[
\theta'=\theta+2\pi n,
\qquad n\in\mathbb Z^4,
\]

then

\[
a\cdot\theta'=2\pi(b+a\cdot n).
\]

Because `a\cdot n` is algebraic, the map

\[
(a,b)\longmapsto(a,b+a\cdot n)
\tag{13}
\]

is a `\overline{\mathbb Q}`-linear isomorphism between `\mathcal R(\theta)` and `\mathcal R(\theta')`. Hence the relation rank in (5) belongs to the phase point, not to an arbitrary branch choice.

For integer `a,b`, (4) contains the winding/character relations studied in AF-310. Equation (5) therefore strictly extends that obstruction from the integer lattice to all algebraic coefficients.

## A regular-pentagon chart is not contained in any affine hyperplane

The normalized five-phase zero locus is

\[
M_5
=
\left\{
(z_1,z_2,z_3,z_4)\in(S^1)^4:
1+z_1+z_2+z_3+z_4=0
\right\}.
\tag{14}
\]

Work in angle coordinates `z_j=e^{-i\theta_j}` and define the lifted equations

\[
1+\sum_{j=1}^4\cos\theta_j=0,
\qquad
\sum_{j=1}^4\sin\theta_j=0.
\tag{15}
\]

At the regular pentagon lift

\[
\theta^0=
\left(\frac{2\pi}{5},\frac{4\pi}{5},
      \frac{6\pi}{5},\frac{8\pi}{5}\right),
\tag{16}
\]

the Jacobian of (15) with respect to `(\theta_3,\theta_4)` has determinant

\[
\sin(2\pi/5)\ne0.
\]

The implicit-function theorem therefore gives a real-analytic local parametrization

\[
\theta(x,y)=(x,y,u(x,y),v(x,y))
\tag{17}
\]

near `(x,y)=(2\pi/5,4\pi/5)`.

The key point is that this local surface is not contained in **any** affine hyperplane of `\mathbb R^4`. Direct implicit differentiation of (15) at the regular pentagon gives, with `q=5+\sqrt5`,

\[
 u_{xx}=-\frac{2\sqrt{10}}{q^{3/2}},
\qquad
 u_{xy}=\frac{\sqrt2}{\sqrt q},
\tag{18}
\]

and

\[
 v_{xx}=\frac{2\sqrt{10}}{q^{3/2}},
\qquad
 v_{xy}=\frac{5\sqrt2-\sqrt{10}}{q^{3/2}}.
\tag{19}
\]

The relevant two-by-two determinant is

\[
\det
\begin{pmatrix}
 u_{xx}&v_{xx}\\
 u_{xy}&v_{xy}
\end{pmatrix}
=2-\sqrt5\ne0.
\tag{20}
\]

Suppose an affine relation

\[
a_1x+a_2y+a_3u(x,y)+a_4v(x,y)=c
\tag{21}
\]

held on a neighborhood. Differentiating (21) twice in the `xx` and `xy` directions and using (20) forces

\[
a_3=a_4=0.
\]

Then (21) on an open `(x,y)`-set forces `a_1=a_2=0`. Thus only the trivial affine relation can hold identically on this chart.

This local second-order calculation is important: it rules out the possibility that the stronger Baker condition is incompatible with pentagon closure merely because the lifted pentagon surface secretly lies in an affine linear slice.

## Baker-compatible exact pentagons are residual

The field `\overline{\mathbb Q}` is countable. For every nonzero pair

\[
(a,b)\in\overline{\mathbb Q}^{\,4}\times\overline{\mathbb Q},
\]

consider on a sufficiently small closed disk `K` inside the chart (17) the zero set

\[
Z_{a,b}
=
\{(x,y)\in K:a\cdot\theta(x,y)=2\pi b\}.
\tag{22}
\]

Each `Z_{a,b}` is closed. It has empty interior: otherwise the real and imaginary parts of (22) would give a nontrivial real affine relation on an open subset, and real-analytic continuation inside the chart would contradict the nonplanarity proved above.

There are only countably many algebraic pairs `(a,b)`. By the Baire category theorem,

\[
K\setminus
\bigcup_{(a,b)\ne0}Z_{a,b}
\tag{23}
\]

is dense and residual in `K`. Every angle lift in (23) satisfies

\[
\mathcal R(\theta)=\{0\}.
\tag{24}
\]

Thus the exact pentagon zero manifold contains, arbitrarily close to the regular pentagon, configurations that satisfy a **strictly stronger** relation condition than a prime phase point needs: they have no nontrivial algebraic-affine angle relation at all, whereas a prime phase point is only required by (5) to have relation rank at most one.

This is the algebraic-linear analogue of AF-310's residual integer-character compatibility result.

## Prior art and novelty assessment

No novelty claim is made for Baker's theorem, equilateral-pentagon moduli, the implicit-function theorem, or the Baire-category argument.

- Alan Baker, **“Linear forms in the logarithms of algebraic numbers,”** *Mathematika* 13(2) (1966), 204–216, DOI `10.1112/S0025579300003971`, established the foundational effective theory of linear forms in logarithms of algebraic numbers.
- Alan Baker, **“Linear forms in the logarithms of algebraic numbers (II),”** *Mathematika* 14(1) (1967), 102–107, DOI `10.1112/S0025579300008068`, explicitly records the consequence used here: rationally independent logarithms of algebraic numbers (with `2\pi i` independent as required) are linearly independent over the algebraic numbers.
- Stephan Klaus and Sadayoshi Kojima, **“On the moduli space of equilateral plane pentagons,”** *Beiträge zur Algebra und Geometrie* 60 (2019), 487–497, DOI `10.1007/s13366-018-0429-z`, gives the classical normalized equilateral-pentagon model and proves that `M_5` is a closed genus-four surface. AF-310 already uses this source for the first integer-character compatibility boundary.

A targeted literature search found the established linear-forms-in-logarithms theory and the classical pentagon-space literature separately, but no basis for presenting their elementary combination here as a new transcendence theorem. The durable result is instead the **mechanism audit**: upgrading unique-factorization arguments to Baker's full algebraic-linear independence still does not geometrically separate the prime direction from the first unresolved zero manifold.

The natural next transcendence layer is genuinely nonlinear. Classical Baker theory controls algebraic-coefficient **linear** forms in logarithms; it does not establish general algebraic independence of logarithms of algebraic numbers, and the exact pentagon equation is itself a nonlinear exponential incidence condition. Therefore merely invoking stronger-sounding transcendence language without an explicit new nonlinear consequence would not advance the prime-zero question.

## Boundaries and failure modes

- Equation (2) is a classical consequence of Baker theory, not a new theorem about prime logarithms.
- Equation (5) constrains algebraic-affine angle relations. It does not constrain arbitrary transcendental-coefficient relations, nonlinear polynomial relations in the angles, or algebraic relations among the phase values themselves.
- The residual set (23) consists of abstract exact pentagon configurations. It does not show that any point in that set lies on the specific one-parameter direction generated by logarithms of rational-prime ratios.
- Baire-generic compatibility is not arithmetic incidence. Just as AF-308--AF-310 warn, a special prime-log direction may still avoid the exact-zero cone for a deeper arithmetic reason.
- The local nonplanarity argument is made near the regular pentagon only. That is sufficient to prove existence and residual local compatibility; no global statement that every pentagon chart has the same property is required.
- The angle-relation rank is invariant under integer `2\pi` deck shifts by (13), but it depends on allowing algebraic coefficients. Changing the coefficient field changes the invariant.
- A single algebraic-affine relation is compatible with the prime phase curve because time can be chosen as in (12). Two independent such relations are forbidden by Baker independence.
- Nothing here proves or disproves an exact zero of `\sum_{j=1}^5 p_j^{-it}` for any five-prime support.
- Nothing here supplies a zeta zero count, analytic continuation, a Riemann-zero divisor, or an RH implication.

## Consequence for the research line

The exact saturated-prime frontier has now crossed two arithmetic relation barriers.

AF-310 showed that prime phases admit at most one independent **integer character** relation and that the pentagon zero manifold generically respects that restriction. AF-311 upgrades the source theorem to **all algebraic-coefficient affine angle relations** using Baker's theorem and again finds that the pentagon zero manifold generically respects the stronger restriction.

Therefore the unresolved `k=5` incidence cannot be attacked by simply replacing unique factorization with a standard linear-forms-in-logarithms theorem. Any decisive arithmetic obstruction must detect something more source-specific than algebraic-linear relations among the logarithmic frequencies: for example a genuinely nonlinear transcendence constraint, a special exact-incidence invariant of the prime-log direction, or a different observation that restores a stable discriminator.

This is useful negative progress for Arithmetic Fidelity. It identifies another broad class of apparently stronger arithmetic arguments that still cannot distinguish the prime source from admissible exact-zero geometry at the first unresolved cardinality, and it sharpens the next theorem surface from “use transcendence theory” to “find a nonlinear source-specific obstruction that is not already generic on the pentagon zero manifold.”