# AF-333 — Schanuel forces prime-phase algebraic codimension at most one

**Status:** `CONJECTURAL`, `CONDITIONAL-ON-SCHANUEL`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TRANSCENDENCE`, `POINTWISE-INCIDENCE`, `DECISIVE-CONDITIONAL-NEGATIVE`, `NO-NOVELTY-CLAIM`

## Claim

Assume **Schanuel's conjecture**. Let

\[
a_1,\ldots,a_n\in\overline{\mathbb Q}_{>0}^{\times}
\]

be multiplicatively independent, let `t\in\mathbb R\setminus\{0\}`, and define

\[
z_j(t)=a_j^{-it}.
\tag{1}
\]

Then the phase tuple has transcendence degree

\[
\boxed{
\operatorname{trdeg}_{\mathbb Q}
\mathbb Q(z_1(t),\ldots,z_n(t))\ge n-1.
}
\tag{2}
\]

Equivalently, the `\mathbb Q`-Zariski closure of a nonzero real common-time phase point has algebraic codimension at most one in `(\mathbb C^\times)^n`. Thus, under Schanuel, such a phase point cannot lie on any `\mathbb Q`-defined algebraic target of codimension at least two.

For `n\ge3`, this immediately forbids an equal-weight phase cancellation:

\[
\boxed{
\sum_{j=1}^n a_j^{-it}\ne0
\qquad(t\ne0).
}
\tag{3}
\]

Indeed a zero sum on the unit torus supplies **two** independent algebraic constraints, not one. In particular, for any distinct rational primes `p_1,\ldots,p_n` with `n\ge3`, Schanuel implies

\[
\sum_{j=1}^n p_j^{-it}\ne0
\qquad(t\in\mathbb R\setminus\{0\}).
\tag{4}
\]

Hence the eight-prime middle-singular incidence left open by AF-328--AF-332 is conditionally impossible already from its first equation `e_1=0`; the additional equation `e_4=0` is not needed under Schanuel.

The threshold is sharp for this mechanism. For `n=2`, the two unit phases can cancel at infinitely many nonzero times, and the conjugate/reciprocal equation does not create a second independent algebraic constraint.

No unconditional zero-free statement and no RH consequence are claimed.

## 1. Schanuel upgrades the phase tuple to codimension at most one

Put

\[
x_j=\log a_j\in\mathbb R,
\qquad
\lambda=-it,
\qquad
y_j=\lambda x_j,
\qquad
z_j=e^{y_j}.
\tag{5}
\]

Because the `a_j` are multiplicatively independent, the real logarithms `x_1,\ldots,x_n` are linearly independent over `\mathbb Q`. An integer relation among them would exponentiate to a multiplicative relation among the `a_j`.

The `2n` complex numbers

\[
x_1,\ldots,x_n,y_1,\ldots,y_n
\tag{6}
\]

are also linearly independent over `\mathbb Q`. If rational coefficients `r_j,s_j` gave

\[
\sum_j r_jx_j+\sum_j s_jy_j=0,
\]

then, writing

\[
A=\sum_jr_jx_j\in\mathbb R,
\qquad
B=\sum_js_jx_j\in\mathbb R,
\]

we would have

\[
A-itB=0.
\tag{7}
\]

Since `t\ne0`, real and imaginary parts force `A=B=0`, and the `\mathbb Q`-independence of the `x_j` then forces all coefficients to vanish.

Schanuel's conjecture applied to the `2n` inputs in `(6)` therefore gives

\[
\operatorname{trdeg}_{\mathbb Q}
\mathbb Q(x_1,\ldots,x_n,
          y_1,\ldots,y_n,
          e^{x_1},\ldots,e^{x_n},
          e^{y_1},\ldots,e^{y_n})
\ge2n.
\tag{8}
\]

Now `e^{x_j}=a_j` is algebraic and `e^{y_j}=z_j`. Moreover `y_j=\lambda x_j`, while

\[
\lambda=\frac{y_1}{x_1}
\tag{9}
\]

because `x_1\ne0`. Thus the field in `(8)`, up to adjoining algebraic numbers, is exactly

\[
\mathbb Q(x_1,\ldots,x_n,\lambda,z_1,\ldots,z_n).
\]

Consequently

\[
2n
\le
\operatorname{trdeg}_{\mathbb Q}
\mathbb Q(x_1,\ldots,x_n,\lambda,z_1,\ldots,z_n)
\le
(n+1)+
\operatorname{trdeg}_{\mathbb Q}\mathbb Q(z_1,\ldots,z_n).
\tag{10}
\]

Rearranging proves `(2)`.

This is the useful structural form of the conditional statement: after the common real-time map, at most **one algebraic codimension** can be lost from the `n` phase coordinates. It upgrades AF-310--AF-311 from restrictions on monomial/algebraic-affine relations to a restriction on arbitrary polynomial relations among the phase coordinates.

## 2. A unit-circle zero secretly imposes codimension two

Assume now `n\ge3` and suppose, for contradiction, that

\[
e_1(z)=z_1+\cdots+z_n=0.
\tag{11}
\]

Because every `|z_j|=1`, complex conjugation gives

\[
\sum_{j=1}^n z_j^{-1}=0.
\tag{12}
\]

Multiplying `(12)` by the nonzero product `e_n(z)=z_1\cdots z_n` yields

\[
e_{n-1}(z)=0.
\tag{13}
\]

For `n\ge3`, `(11)` and `(13)` are genuinely independent algebraic equations. One elementary way to see this is to eliminate

\[
z_n=-(z_1+\cdots+z_{n-1})
\tag{14}
\]

using `e_1=0`. The restriction of `e_{n-1}` to this hyperplane is not the zero polynomial: setting

\[
z_1=\cdots=z_{n-1}=1,
\qquad z_n=-(n-1)
\]

gives

\[
e_{n-1}(z)
=(z_1\cdots z_n)\sum_jz_j^{-1}
=-n(n-2)\ne0.
\tag{15}
\]

Hence after `(14)` the first `n-1` coordinates satisfy one further nonzero polynomial relation. Therefore any point satisfying `(11)` and `(13)` obeys

\[
\operatorname{trdeg}_{\mathbb Q}
\mathbb Q(z_1,\ldots,z_n)
\le n-2.
\tag{16}
\]

Equations `(2)` and `(16)` contradict each other. This proves `(3)` and `(4)` under Schanuel.

The crucial extra constraint is not visible if one regards `e_1=0` merely as one complex polynomial equation. It comes from retaining the **unit-circle provenance** of the compressed phase tuple: conjugation becomes inversion, turning the zero into the second algebraic relation `e_{n-1}=0`. In Arithmetic Fidelity language, the source geometry makes one apparently codimension-one target event consume two algebraic degrees of freedom.

## 3. The two-term boundary is exact

When `n=2`, the reciprocal equation adds nothing:

\[
e_{n-1}=e_1.
\]

Accordingly the transcendence-degree bounds do not conflict. Schanuel would give only

\[
\operatorname{trdeg}_{\mathbb Q}\mathbb Q(z_1,z_2)\ge1,
\]

while a cancellation `z_1+z_2=0` also has algebraic dimension one.

And such cancellations genuinely occur. For distinct positive `a_1,a_2`,

\[
a_1^{-it}+a_2^{-it}=0
\]

whenever

\[
t=\frac{(2k+1)\pi}{\log(a_1/a_2)},
\qquad k\in\mathbb Z.
\tag{17}
\]

Thus the `n\ge3` threshold is not an artifact of a loose dimension count. The mechanism fails exactly where the unit-circle conjugate relation ceases to be independent.

## 4. Relation to the current prime-incidence frontier

AF-330 proves unconditionally, using the Bays--Kirby--Wilkie theorem on exponentially transcendental powers, that any exact polynomial relation among a multiplicatively independent algebraic common-power tuple forces the common parameter into exponential algebraic closure. AF-331 shows that the corresponding real exceptional-time set is countable but dense, so genericity or distance from that set cannot finish the exact problem. AF-332 then shows unconditionally that a nonzero prime-phase point has at most two algebraic coordinates, so the exceptional parameter cannot be replaced by an algebraic-point classification of the target.

The present result is a conditional continuation in a different direction. Schanuel does not try to classify the exceptional times. Instead it bounds the **total algebraic dependence budget of the phase image** at every nonzero real time:

\[
\boxed{
\operatorname{codim}_{\mathrm{alg},\mathbb Q} z(t)\le1.
}
\tag{18}
\]

For the current eight-prime target, the retained unitary provenance converts `e_1=0` into the independent pair

\[
e_1=e_7=0,
\tag{19}
\]

which already exceeds that budget. Thus, assuming Schanuel, no exponentially algebraic exceptional time from AF-330--AF-331 can realize the hit.

This also explains precisely what an unconditional replacement would need to achieve: not merely another coordinatewise transcendence theorem, but a lower bound approaching

\[
\operatorname{trdeg}_{\mathbb Q}\mathbb Q(p_1^{-it},\ldots,p_n^{-it})\ge n-1
\tag{20}
\]

for a common nonzero real time, or another theorem strong enough to exclude two independent algebraic relations on the same prime-phase tuple.

## Prior art and novelty assessment

The transcendence input is Schanuel's classical conjecture. Serge Lang, *Introduction to Transcendental Numbers*, Addison-Wesley (1966), p. 30, is a standard early source for the conjecture. Francesco Paolo Gallinaro, **“Exponential sums equations and tropical geometry,”** *Selecta Mathematica* 29, article 49 (2023), DOI `10.1007/s00029-023-00853-y`, states Schanuel in the transcendence-degree form used here and describes its geometric interpretation as forbidding unexpectedly low-dimensional algebraic containment on the graph of exponentiation. Boris Zilber, **“Exponential Sums Equations and the Schanuel Conjecture,”** *Journal of the London Mathematical Society* 65(1), 27--44 (2002), DOI `10.1112/S0024610701002861`, is neighboring prior art on exponential-sum systems under Schanuel-type hypotheses.

No novelty is claimed for Schanuel's conjecture, transcendence-degree dimension counting, or the elementary reciprocal identity on the unit circle. A targeted search across Schanuel/exponential-sum and algebraic-power literature found closely related uses of Schanuel to control algebraic dependence of powers, but no reason to present `(2)`--`(4)` as a new standalone transcendence theorem. The durable contribution here is narrower and Mathia-specific: the Schanuel dimension budget closes the exact prime-phase zero frontier conditionally and identifies **unitary provenance as the second algebraic constraint** that makes the contradiction possible.

## Boundaries and failure modes

- The entire conclusion `(2)`--`(4)` is conditional on the still-unproved Schanuel conjecture. It must not be used as unconditional evidence that the prime-phase zero set is empty.
- The proof uses a common **nonzero real** time. For a general complex parameter, the real/pure-imaginary separation establishing the `2n`-input `\mathbb Q`-independence need not hold.
- Multiplicative independence of the positive algebraic bases is essential. If the source logarithms have rational relations, the Schanuel input rank falls and so does the lower bound.
- The zero-free corollary uses equal coefficients and unit-modulus outputs. A general weighted exponential sum need not turn one polynomial zero into an independent reciprocal polynomial relation.
- Bound `(2)` allows one algebraic relation among the phase coordinates. It does not prove full algebraic independence and does not contradict AF-330's exceptional-time gate, which is unconditional and concerns when even one relation may occur.
- The argument is exact and pointwise; it gives no positive lower bound for `|\sum a_j^{-it}|`. AF-329's arbitrarily accurate near-incidences therefore remain fully compatible with this conditional zero-free statement.

## Consequence for the research line

For the eight-prime middle-singular branch, Schanuel would settle the remaining exact-incidence question negatively: the orbit cannot satisfy even `e_1=0` at nonzero real time. More importantly for Arithmetic Fidelity, it exposes a reusable mechanism that is stronger than coordinatewise transcendence: **source provenance can turn a seemingly single compressed event into multiple algebraic constraints, and a source-side transcendence budget can then rule out the event by codimension.**

The unconditional frontier is consequently sharper. Six Exponentials in AF-332 controls how many coordinates may be algebraic, but it does not control the algebraic dimension of the whole phase tuple. Any unconditional attack that genuinely replaces Schanuel must control joint polynomial dependence rather than add more genericity, local conditioning, or algebraic-point classification.