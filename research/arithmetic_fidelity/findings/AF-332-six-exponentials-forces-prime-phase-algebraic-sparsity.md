# AF-332 — Six exponentials forces algebraic sparsity of prime-phase coordinates

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `TRANSCENDENCE`, `POINTWISE-INCIDENCE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

Let `p_1,...,p_n` be distinct rational primes with `n>=3`, let `t in R\{0}`, and define the common-time prime phases

\[
z_j(t)=p_j^{-it}=\exp((-it)\log p_j).
\tag{1}
\]

Then among every three distinct coordinates of `z(t)` at least one is transcendental. Equivalently,

\[
\boxed{
\#\{j:z_j(t)\in\overline{\mathbb Q}\}\le 2.
}
\tag{2}
\]

Thus a nonzero real prime-phase orbit can never pass through a point of `(\overline{\mathbb Q}^{\times})^n`, and more generally cannot pass through any target stratum requiring three specified phase coordinates to be algebraic.

For the eight-prime singular-incidence problem of AF-328--AF-331, any nonzero exact hit of

\[
e_1(z)=e_4(z)=0
\tag{3}
\]

must therefore have at least six individually transcendental phase coordinates.

Combined with AF-330, this produces a useful pointwise separation. An exact algebraic incidence forces the **time parameter** `-it` to be exponentially algebraic, but the corresponding **phase point** cannot be algebraic and is in fact algebraically sparse coordinatewise. Hence classification of algebraic or torsion points of `V(e_1,e_4)` cannot by itself decide the remaining exact prime incidence.

No RH consequence is claimed.

## 1. Six exponentials gives the three-coordinate obstruction

Use the classical Six Exponentials Theorem in the following standard form. If

\[
x_1,x_2,x_3\in\mathbb C
\]

are linearly independent over `Q` and

\[
y_1,y_2\in\mathbb C
\]

are linearly independent over `Q`, then at least one of the six numbers

\[
\exp(x_i y_j),
\qquad 1\le i\le3,\ 1\le j\le2,
\tag{4}
\]

is transcendental.

Choose any three distinct indices `a,b,c` and set

\[
x_1=\log p_a,\qquad
x_2=\log p_b,\qquad
x_3=\log p_c.
\tag{5}
\]

These logarithms are `Q`-linearly independent. Indeed, after clearing denominators, a rational relation would give integers `m_a,m_b,m_c`, not all zero, with

\[
m_a\log p_a+m_b\log p_b+m_c\log p_c=0.
\tag{6}
\]

Exponentiating gives

\[
p_a^{m_a}p_b^{m_b}p_c^{m_c}=1,
\tag{7}
\]

which unique factorization forces to be trivial.

Now take

\[
y_1=1,
\qquad
y_2=-it.
\tag{8}
\]

Since `t` is real and nonzero, `1` and `-it` are `Q`-linearly independent: a relation `r+q(-it)=0` with `r,q in Q` has separately vanishing real and imaginary parts, hence `r=q=0`.

The first row of exponentials is

\[
\exp(x_i y_1)\in\{p_a,p_b,p_c\},
\tag{9}
\]

so all three are algebraic. Therefore the transcendental member required by the Six Exponentials Theorem must occur in the second row:

\[
\exp(x_i y_2)\in
\{p_a^{-it},p_b^{-it},p_c^{-it}\}.
\tag{10}
\]

At least one of those three phase coordinates is transcendental.

Because the triple `{a,b,c}` was arbitrary, no three phase coordinates can all be algebraic. This is exactly `(2)`.

## 2. Consequence for the eight-prime singular target

Fix eight distinct primes and the AF-328 phase orbit

\[
z(t)=(p_1^{-it},\ldots,p_8^{-it}).
\tag{11}
\]

AF-328 reduces the unresolved middle-singular event to the exact intersection

\[
z(t)\in V(e_1,e_4)\cap(S^1)^8.
\tag{12}
\]

Equation `(2)` applies independently of whether `(12)` holds. Hence if a nonzero exact hit exists, at most two of its eight coordinates can be algebraic and at least six must be transcendental.

In particular, the orbit cannot solve `(12)` at:

- an algebraic point of the target variety;
- a torsion point of the ambient torus;
- any target stratum on which three declared coordinates are algebraic.

The obstruction is stronger than merely ruling out roots of unity. It allows as many as two algebraic phase values of arbitrary algebraic type, but never three.

This is a source-specific restriction: it uses the `Q`-linear independence of three rational-prime logarithms and the common one-parameter exponent `-it`. An arbitrary point of `V(e_1,e_4)\cap(S^1)^8` need not satisfy `(2)`.

## 3. Exceptional parameter does not mean algebraic image

AF-330 proves a different transcendence statement. If a finite rational-prime common-power orbit satisfies any nonzero polynomial relation in its phase coordinates, then its common parameter `lambda=-it` must lie in

\[
\operatorname{ecl}_{\mathbb C}(\varnothing).
\tag{13}
\]

AF-331 then proves that the corresponding real-time exceptional set is countable but dense, so membership in `(13)` cannot be exploited through neighborhood separation or a positive distance margin.

The present theorem clarifies what `(13)` does **not** mean. Even when the parameter is forced into the exceptional exponential-algebraic class, a nonzero real prime-phase point cannot become an algebraic point of the ambient torus. In the eight-prime problem the two restrictions coexist:

\[
\boxed{
\text{exact hit}
\Longrightarrow
-it\in\operatorname{ecl}_{\mathbb C}(\varnothing)
\quad\text{and}\quad
\#\{j:p_j^{-it}\in\overline{\mathbb Q}\}\le2.
}
\tag{14}
\]

Thus the remaining incidence, if it exists, lies in an unusual mixed regime: an exponentially algebraic common time produces a phase tuple satisfying the target polynomial relations while most individual phase coordinates remain transcendental.

This rules out a tempting continuation of AF-330--AF-331. Restricting the target search to algebraic points, torsion points, or algebraic-coordinate strata cannot capture a genuine nonzero hit. Any successful pointwise argument must control transcendental target points through their common prime-log provenance rather than replace the incidence problem by algebraic-point classification.

## 4. What the theorem does not decide

The result does not exclude `(12)`. The equations `e_1=e_4=0` are algebraic relations among the coordinates, and an algebraic variety can of course contain points with all or most coordinates transcendental. Six exponentials supplies individual-coordinate transcendence, not algebraic independence of the phase tuple.

Indeed AF-330 shows that at an exact hit the tuple is algebraically dependent by construction. There is no contradiction between that dependence and `(2)`: several transcendental numbers may satisfy polynomial relations over `Q`.

Nor does `(2)` classify the pure-imaginary elements of `ecl_C(empty)`, produce a lower bound on `|e_1|+|e_4|`, or separate exact hits from the arbitrarily accurate near-hits of AF-329. It is a pointwise exclusion theorem for one class of possible target points.

The restriction also depends essentially on having at least three `Q`-independent source logarithms and a nonzero real common time. At `t=0` all phases equal `1`, so the conclusion is false. For sources with multiplicative relations, the required independence of the selected logarithms may fail.

## Prior art and novelty assessment

The decisive theorem is classical transcendence theory.

- K. Ramachandra, **“Contributions to the theory of transcendental numbers (I),”** *Acta Arithmetica* 14 (1968), 65--72, DOI `10.4064/aa-14-1-65-72`, and **“(II),”** *Acta Arithmetica* 14 (1968), 73--88, DOI `10.4064/aa-14-1-73-88`. These papers contain Ramachandra's independent development of the Six Exponentials Theorem.
- Serge Lang, ***Introduction to Transcendental Numbers***, Addison-Wesley (1966), Chapter 2. Role: classical independent formulation/proof and standard transcendence-theory context.
- Michel Waldschmidt, **“Further Variations on the Six Exponentials Theorem,”** *Hardy-Ramanujan Journal* 28 (2005), DOI `10.46298/hrj.2005.86`. Role: modern explicit formulation in terms of a `2 x 3` matrix of logarithms of algebraic numbers and the neighboring sharp variants.

No novelty is claimed for the Six Exponentials Theorem, linear independence of logarithms of distinct primes, or the elementary three-subset deduction. The Arithmetic Fidelity contribution is the exact placement of that classical theorem at the AF-328--AF-331 frontier: exponential algebraicity of the common time does not turn the unresolved prime incidence into an algebraic-point problem; any nonzero eight-prime hit would necessarily live in the transcendental-coordinate part of the target variety.

## Consequence for the research line

AF-330 and AF-331 moved the exact-incidence frontier from generic time to a dense exceptional parameter class. AF-332 removes another possible simplification inside that class: **exceptional time is not algebraic target provenance**.

For any future attack on the eight-prime common zero, algebraic/torsion-point classification is therefore too small a destination category. The useful retained structure must couple the transcendental phase coordinates through their common prime-log parameterization. A theorem that sees only whether the target point is algebraic, torsion, or coordinatewise algebraic cannot cross the remaining gate.