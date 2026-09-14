# AF-330 — Exact prime algebraic incidence forces an exponentially algebraic time

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `TRANSCENDENCE`, `EXPONENTIAL-ALGEBRAICITY`, `POINTWISE-INCIDENCE`, `NO-NOVELTY-CLAIM`

## Claim

There is an unconditional pointwise transcendence restriction on the exact prime-phase incidence problem left open by AF-328--AF-329.

Let

\[
a_1,\ldots,a_n\in\overline{\mathbb Q}^{\times}
\]

be multiplicatively independent, choose logarithms `x_j` with `exp(x_j)=a_j`, and let `lambda in C`. If `lambda` is **exponentially transcendental** in the complex exponential field, then

\[
\boxed{
\exp(\lambda x_1),\ldots,\exp(\lambda x_n)
\text{ are algebraically independent over }\mathbb Q(\lambda).
}
\tag{1}
\]

Consequently, for every nonzero polynomial

\[
P\in\mathbb Q(\lambda)[X_1,\ldots,X_n],
\]

one has

\[
P\!\left(\exp(\lambda x_1),\ldots,\exp(\lambda x_n)\right)\ne0.
\tag{2}
\]

Equivalently, **any exact hit of a proper algebraic target by such a common-power orbit forces `lambda` to be exponentially algebraic**.

For distinct rational primes `p_1,...,p_n`, take `x_j=log p_j` and `lambda=-it`. Then

\[
z_j(t)=p_j^{-it}=\exp(\lambda\log p_j).
\tag{3}
\]

The primes are multiplicatively independent, so every exact polynomial relation over `Q` among the phases forces

\[
\boxed{-it\in\operatorname{ecl}_{\mathbb C}(\varnothing).}
\tag{4}
\]

In particular, for the eight-prime middle-singular target of AF-328,

\[
F(it)=e_1(z(t))=0,
\qquad
G(it)=e_4(z(t))=0,
\tag{5}
\]

can occur only at an exponentially algebraic parameter. In fact either equation in `(5)` by itself already forces `(4)`.

This is the first source-specific **pointwise** restriction after AF-328 isolated exact incidence as the remaining problem. It does not prove that the exceptional set contains no hit. Instead it moves every possible hit out of the exponentially transcendental regime and into the universal countable exponential-algebraic closure.

Combined with AF-329, the result gives a sharp exact/stable split: the prime-log orbit approaches the algebraic singular target arbitrarily closely and relatively densely, including at exponentially transcendental times, while exact incidence is forbidden at every such time.

No RH consequence is claimed.

## 1. The Bays--Kirby--Wilkie power theorem gives full algebraic independence

Bays, Kirby, and Wilkie prove the following unconditional theorem for arbitrary exponential fields. If `lambda` is exponentially transcendental and `x=(x_1,...,x_n)` is such that

\[
\exp(x_1),\ldots,\exp(x_n)
\]

are multiplicatively independent, then

\[
\operatorname{td}\!\left(
\exp(x),\exp(\lambda x)\,/\,\lambda
\right)\ge n.
\tag{6}
\]

Here `td(A/B)` is the transcendence degree of `Q(A,B)` over `Q(B)`.

Apply `(6)` in the ordinary complex exponential field with `exp(x_j)=a_j`. Since every `a_j` is algebraic over `Q`, adjoining `exp(x)` contributes zero transcendence degree over `Q(lambda)`. Therefore

\[
\operatorname{td}_{\mathbb Q(\lambda)}
\mathbb Q\!\left(
\lambda,
\exp(\lambda x_1),\ldots,\exp(\lambda x_n)
\right)
\ge n.
\tag{7}
\]

There are only `n` displayed power values, so the left-hand side is at most `n`. Equality holds, proving that those `n` values are algebraically independent over `Q(lambda)`. This is `(1)`.

The contrapositive is the useful Arithmetic Fidelity form:

\[
\boxed{
P(\exp(\lambda x_1),\ldots,\exp(\lambda x_n))=0
\text{ for some }0\ne P\in\mathbb Q(\lambda)[X]
\Longrightarrow
\lambda\text{ exponentially algebraic}.
}
\tag{8}
\]

Nothing about `(8)` is specific to `e_1`, `e_4`, polygon closure, or eight variables. It applies to every proper algebraic failure locus visible through a finite family of multiplicatively independent algebraic generators.

## 2. Rational-prime phases satisfy the multiplicative-independence hypothesis exactly

For distinct rational primes `p_1,...,p_n`, an integer relation

\[
\prod_{j=1}^n p_j^{m_j}=1
\tag{9}
\]

forces every `m_j=0` by unique factorization. Hence the tuple

\[
(p_1,\ldots,p_n)
\]

is multiplicatively independent.

Choose the ordinary real logarithms `x_j=log p_j`. For a real common time `t`, put

\[
\lambda=-it.
\tag{10}
\]

Then `(3)` holds with no branch ambiguity because `x_j` has been fixed before applying the exponential map.

If, for example,

\[
\sum_{j=1}^n p_j^{-it}=0,
\tag{11}
\]

then the nonzero rational polynomial

\[
P(X)=X_1+\cdots+X_n
\]

vanishes at the common-power tuple. By `(8)`, `lambda=-it` cannot be exponentially transcendental. Thus `(4)` follows already from an exact zero of the first power sum.

Likewise any equation

\[
e_k(p_1^{-it},\ldots,p_n^{-it})=0,
\qquad 1\le k\le n,
\tag{12}
\]

or any other nontrivial rational polynomial identity in the prime phases gives the same conclusion. The AF-328 joint system `e_1=e_4=0` is therefore a special case of a much broader algebraic-incidence barrier.

This differs fundamentally from the rank-one integer-character restriction in AF-310. A polynomial relation such as `e_1=0` need not force any monomial relation among the phases, so character-lattice methods can fail while `(8)` still applies. The BKW theorem sees **algebraic dependence of the whole phase tuple**, not only multiplicative dependence.

## 3. The exceptional parameter class is universal and countable

Exponential algebraicity is defined through a finite Khovanskii system: finitely many exponential-polynomial equations with nonvanishing Jacobian at the solution. The Jacobian condition makes the solution isolated. There are only countably many finite systems with integer coefficients, and every discrete subset of finite-dimensional complex Euclidean space is countable. Therefore

\[
\operatorname{ecl}_{\mathbb C}(\varnothing)
\tag{13}
\]

is countable.

More importantly, `(13)` is **independent of the chosen prime support and of the chosen algebraic target**. Thus all exact algebraic incidences of all finite rational-prime common-power orbits are forced into the same universal exceptional parameter class.

The statement is stronger than saying that the zero set of one fixed Dirichlet polynomial is discrete or countable. That analytic fact depends on the chosen function. Equation `(13)` instead supplies a support-independent transcendence class which every such exact algebraic hit must share.

It is also important not to overinterpret this class. Exponentially algebraic does not mean algebraic in the ordinary field-theoretic sense. The exponential algebraic closure contains transcendental elements, including kernel-related values, and there is no usable classification of all of its elements. The theorem narrows the incidence mechanism without enumerating the remaining candidates.

## 4. Exact incidence and arbitrarily accurate approach separate even more sharply

AF-329 proves that for a fixed set of eight distinct rational primes the phase orbit

\[
t\longmapsto
(p_1^{-it},\ldots,p_8^{-it})
\tag{14}
\]

is dense in the full torus and that the ambient target

\[
V(e_1,e_4)\cap(S^1)^8
\tag{15}
\]

is nonempty. Therefore for every `epsilon>0` the set

\[
U_\epsilon
=
\left\{
t\in\mathbb R:
|F(it)|^2+|G(it)|^2<\epsilon^2
\right\}
\tag{16}
\]

is nonempty and, by minimality/recurrence of the irrational torus flow, relatively dense. It is also open by continuity.

The exceptional set

\[
E=\{t\in\mathbb R:-it\in\operatorname{ecl}_{\mathbb C}(\varnothing)\}
\tag{17}
\]

is countable. Every nonempty open interval contained in `U_epsilon` therefore contains times outside `E`. Hence the near-hit statement can be strengthened to

\[
\boxed{
\forall\epsilon>0,
\text{ exponentially transcendental common times occur relatively densely with }
0<\sqrt{|F(it)|^2+|G(it)|^2}<\epsilon.
}
\tag{18}
\]

At every time appearing in `(18)`, exact equality is forbidden by `(8)`.

So the current obstruction is not merely that exact hits are hard to distinguish from near hits numerically. There is now an exact structural separation:

- exponentially transcendental times can approach the failure locus arbitrarily well but cannot enter it;
- any genuine entry must occur at an exponentially algebraic time.

This is precisely the kind of fidelity distinction the line is intended to isolate: closure access survives the compression, while exact algebraic incidence requires a qualitatively stronger arithmetic/transcendence resource.

## 5. Consequence for the AF-328--AF-329 frontier

AF-328 showed that factorization/common-factor theory cannot decide one isolated common zero of `F` and `G`. AF-329 then showed that neither a positive joint margin nor a Bezout identity can separate the prime orbit from the ambient target.

The present theorem identifies a different pointwise gate which those arguments did not see. Any successful exact hit must satisfy

\[
-it\in\operatorname{ecl}_{\mathbb C}(\varnothing).
\tag{19}
\]

Thus the next exact-incidence question is no longer an unrestricted search over real time. A genuinely new proof route can ask whether the **pure-imaginary exponentially algebraic parameters** are compatible with the simultaneous prime-power equations `e_1=e_4=0`, or whether additional transcendence structure excludes that intersection.

This does not make the remaining problem easy. Current exponential-algebraicity theory supplies a pregeometry and strong generic-power theorems, but not a classification of the exceptional points needed to test `(19)` one by one. The contribution is therefore a rigorous reduction of the pointwise source question, not a solution of it.

## Prior art and novelty assessment

The decisive theorem is established prior art.

- Martin Bays, Jonathan Kirby, and A. J. Wilkie, **“A Schanuel property for exponentially transcendental powers,”** *Bulletin of the London Mathematical Society* 42(5) (2010), 917--922, DOI `10.1112/blms/bdq054`. Theorem 1.2 is the arbitrary-exponential-field statement used in `(6)`; Theorem 1.1 gives its real-power specialization. The proof is unconditional and uses Ax's differential version of Schanuel's theorem, not Schanuel's conjecture for complex numbers.
- Jonathan Kirby, **“Exponential algebraicity in exponential fields,”** *Bulletin of the London Mathematical Society* 42(5) (2010), 879--890, DOI `10.1112/blms/bdq044`. This develops exponential algebraic closure as a pregeometry and is the structural background for the exceptional class in `(13)`.
- James Ax, **“On Schanuel's conjectures,”** *Annals of Mathematics* 93(2) (1971), 252--268. Role: differential-algebraic Schanuel theorem used by Bays--Kirby--Wilkie in their generic-power result.

No novelty is claimed for exponential algebraicity, the BKW theorem, or Ax's theorem. The Mathia-specific derived result is the application of BKW to the rational-prime common-time phase orbit and its composition with AF-329: the unresolved exact middle-singular hit is forced into `ecl_C(empty)` even though exponentially transcendental times still approach the same target arbitrarily closely.

## Boundaries and failure modes

- Equation `(8)` is a **necessary** condition for exact algebraic incidence. Exponential algebraicity of `lambda` is not sufficient for a hit.
- The result does not classify `ecl_C(empty)` and does not prove that its pure-imaginary part misses the AF-328 common-zero set.
- Ordinary algebraicity and exponential algebraicity are different notions. Do not replace `(4)` by the stronger unsupported statement that `t` or `-it` must be algebraic.
- The BKW theorem requires multiplicative independence of `exp(x_j)`. Distinct rational primes satisfy this exactly; an arbitrary source with multiplicative relations may not.
- The algebraic target must be represented by a genuine nonzero polynomial relation in the retained phase coordinates. Purely metric, inequality, asymptotic, or nonalgebraic failure loci are not covered by `(8)`.
- Near-hit recurrence in `(18)` uses the fixed-support prime-log torus density already established in AF-329. BKW alone supplies no approximation theorem.
- Countability of the exceptional class is not an effective enumeration and gives no lower bound on distance to the target.
- No statement about Riemann zeros, the critical line, analytic continuation of zeta, or RH follows from this result.

## Consequence for the research line

The exact-incidence frontier has crossed from factorization into exponential transcendence. For multiplicatively independent algebraic sources, a common-power orbit is algebraically generic at every exponentially transcendental parameter; **proper algebraic target hits are an exponentially algebraic phenomenon**.

For the current eight-prime singular problem this means that density, continuity, stable conditioning, common-factor theory, and ideal theory all live on the wrong side of the final exact gate. AF-329 permits arbitrarily accurate approaches at generic times, while AF-330 shows that actual equality can occur only at a universal exceptional parameter class. The next useful theorem must therefore say something genuinely pointwise about that exceptional class, rather than extract another continuous margin from the dense orbit.