# RE-003 — consecutive CA jumps are logarithmic and Robin peaks need half-mass event gaps

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + UNIFORM-CA-JUMP-BOUND + SELF-TANGENT-GAP-GATE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-AUDITED`. `RE-002` proves an exact secant-clearance criterion for a regular self-tangent colossally abundant state to be a local Robin peak. Its transparent half-jump form was stated there under the additional regime `w_\pm=o(X)`, where `X=\log C` and `w_\pm` are the logarithmic jumps to the neighboring CA states. That size condition is not an extra hypothesis for actual CA transitions. The classical Alaoglu--Erdos theorem that a quotient of consecutive colossally abundant numbers is a prime or a product of two distinct primes, combined with the exact prime-layer event locations and one use of Bertrand's postulate, gives

\[
\boxed{w_-=O(\log X),\qquad w_+=O(\log X)}
\tag{1}
\]

uniformly around every sufficiently large regular self-tangent state.

Consequently the local peak gate of `RE-002` is unconditionally in its asymptotic half-jump regime on the genuine CA ladder. If

\[
A<C<B
\]

are the neighboring CA states around such a peak, and `eta_-<X<eta_+` are the adjacent prime-layer transition coordinates, then necessarily

\[
\boxed{
\eta_+-\eta_-
>
\frac12\log\frac BA
-O\!\left(\frac{(\log X)^2}{X}\right).
}
\tag{2}
\]

Thus hypothetical Robin failure does not merely require infinitely many self-tangent returns. By `RE-001`, it requires infinitely many returns lying in event gaps that are large enough to absorb asymptotically **half of the total logarithmic mass of both boundary CA jumps**. This turns the remaining local route into a comparison between event spacing and event mass, with no unconstrained transition-size regime left.

## 1. Every prime-layer event controls the size of its prime

Retain the event notation of `RE-001`. For prime `p` and layer `j>=1`, put

\[
\lambda_{p,j}
:=
\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\qquad
m_{p,j}:=\frac{\lambda_{p,j}}{\log p},
\tag{3}
\]

and define the event coordinate `eta_{p,j}` by

\[
\frac1{\eta_{p,j}\log\eta_{p,j}}
=m_{p,j}.
\tag{4}
\]

The abundance increment has the exact elementary form

\[
\lambda_{p,j}
=
\log\!\left(
1+\frac{p-1}{p(p^j-1)}
\right).
\tag{5}
\]

Since

\[
\frac{p-1}{p(p^j-1)}\le\frac1{p^j}
\]

for every `j>=1`, `log(1+u)<=u` gives

\[
\lambda_{p,j}\le p^{-j}.
\tag{6}
\]

Equations (4)--(6) imply the useful finite bound

\[
\boxed{
p^j\log p
\le
\eta_{p,j}\log\eta_{p,j}.
}
\tag{7}
\]

In particular, every prime contributing to an event at coordinate `eta` satisfies

\[
\log p
\le
\log\!\left(\frac{\eta\log\eta}{\log2}\right),
\tag{8}
\]

so a transition occurring at polynomial scale in `X` has only logarithmic mass.

The first layer is sharper. Here

\[
\lambda_{p,1}=\log(1+1/p).
\]

The elementary inequalities

\[
\frac1{p+1}\le\log(1+1/p)\le\frac1p
\tag{9}
\]

give

\[
p\log p
\le
\eta_{p,1}\log\eta_{p,1}
\le
(p+1)\log p.
\tag{10}
\]

Since `x log x` is increasing for `x>1`,

\[
\boxed{p\le\eta_{p,1}<p+1.}
\tag{11}
\]

Thus the new-prime event axis differs from the ordinary prime axis by less than one unit, with no asymptotic theorem or numerical approximation.

## 2. There is always another CA event within a constant multiple of `X`

Let `X` be a sufficiently large regular self-tangent coordinate and let `eta_+` be the first prime-layer event strictly to its right. Choose `n=ceil(X)`. Bertrand's postulate supplies a prime `q` with

\[
n<q<2n.
\]

By (11), its first-layer event satisfies

\[
X<q\le\eta_{q,1}<q+1<2X+3.
\tag{12}
\]

Because `eta_+` is the next event after `X`,

\[
\boxed{\eta_+<2X+3.}
\tag{13}
\]

No assertion is made that this first-layer prime is itself the next event; higher prime-power layers may interlace before it. Equation (13) only supplies a uniform ceiling for wherever the actual next transition occurs.

The left event already obeys `eta_-<X`. Hence all primes contributing to either adjacent transition have event coordinates at most `2X+3`.

## 3. Alaoglu--Erdos makes the adjacent logarithmic jump uniformly small

Alaoglu and Erdos proved that the quotient of two consecutive colossally abundant numbers is either one prime or the product of two distinct primes. This theorem is exactly what is needed here; the stronger conjecture that every quotient is prime is not assumed.

For the consecutive states

\[
A<C<B,
\]

write

\[
w_-:=\log(C/A),
\qquad
w_+:=\log(B/C).
\tag{14}
\]

Every prime factor of `C/A` corresponds to a layer event at `eta_-`, and every prime factor of `B/C` corresponds to a layer event at `eta_+`. There are at most two such prime factors in each quotient. Combining this with (8), `eta_-<X`, and (13) gives explicitly

\[
w_-
\le
2\log\!\left(\frac{X\log X}{\log2}\right),
\tag{15}
\]

and

\[
w_+
\le
2\log\!\left(
\frac{(2X+3)\log(2X+3)}{\log2}
\right).
\tag{16}
\]

Therefore

\[
\boxed{
w_\pm=O(\log X)=o(X).}
\tag{17}
\]

This is uniform over prime and semiprime CA transitions, over first and higher prime-power layers, and over the admissible tied-transition cases. It does not use the experimentally verified prime-quotient conjecture.

Zimov's 2025 preprint also uses the classical prime-or-semiprime quotient theorem, but for a different purpose: bounding the one-step growth of `G` near the least hypothetical CA counterexample. Equations (7)--(17) use the same classical structural theorem to control **event-axis transition mass**, so that the secant geometry in `RE-002` becomes uniform.

## 4. The exact secant thresholds are always asymptotically half-jump

`RE-002` defines the backward and forward secant-balance points by

\[
g(\xi_-)
=\frac{H(X)-H(X-w_-)}{w_-},
\qquad
H(t)=\log\log t,
\qquad
g(t)=\frac1{t\log t},
\tag{18}
\]

and

\[
g(\xi_+)
=\frac{H(X+w_+)-H(X)}{w_+}.
\tag{19}
\]

It proves the exact peak equivalences

\[
G(C)>G(A)\iff\eta_-<\xi_-,
\qquad
G(C)\ge G(B)\iff\eta_+\ge\xi_+.
\tag{20}
\]

The same finding obtains, whenever `w_\pm=o(X)`,

\[
X-\xi_-
=\frac{w_-}{2}+\kappa(X)w_-^2
+O\!\left(\frac{w_-^3}{X^2}\right),
\tag{21}
\]

\[
\xi_+-X
=\frac{w_+}{2}-\kappa(X)w_+^2
+O\!\left(\frac{w_+^3}{X^2}\right),
\tag{22}
\]

where

\[
\kappa(X)
=\frac{2(\log X)^2+3\log X+2}
{24X\log X(\log X+1)}
=O(X^{-1}).
\tag{23}
\]

Equation (17) now shows that this regime contains **every** sufficiently large genuine CA transition adjacent to a regular self-tangent state. The errors in (21)--(22) are uniformly

\[
O\!\left(\frac{(\log X)^3}{X^2}\right),
\tag{24}
\]

and the quadratic corrections are uniformly

\[
O\!\left(\frac{(\log X)^2}{X}\right).
\tag{25}
\]

There is therefore no remaining large-jump chamber in which the half-jump interpretation of `RE-002` might fail.

## 5. A Robin peak requires an event gap carrying half the two boundary masses

Put

\[
d_-:=X-\eta_->0,
\qquad
d_+:=\eta_+-X>0.
\tag{26}
\]

If `C` is a local Robin peak on the CA ladder, (20)--(22) give

\[
d_->
\frac{w_-}{2}+\kappa(X)w_-^2
+O\!\left(\frac{(\log X)^3}{X^2}\right),
\tag{27}
\]

and

\[
d_+\ge
\frac{w_+}{2}-\kappa(X)w_+^2
+O\!\left(\frac{(\log X)^3}{X^2}\right).
\tag{28}
\]

Adding and using `eta_+-eta_-=d_-+d_+` yields the refined necessary condition

\[
\boxed{
\eta_+-\eta_-
>
\frac{w_-+w_+}{2}
+\kappa(X)(w_-^2-w_+^2)
+O\!\left(\frac{(\log X)^3}{X^2}\right).
}
\tag{29}
\]

Since

\[
w_-+w_+=\log(B/A),
\]

(23)--(25) give the simpler uniform form (2):

\[
\boxed{
\eta_+-\eta_-
>
\frac12\log\frac BA
-O\!\left(\frac{(\log X)^2}{X}\right).
}
\tag{30}
\]

The error tends to zero absolutely, not only relative to `X`. Hence for every fixed `delta>0`, every sufficiently large regular self-tangent peak must satisfy

\[
\eta_+-\eta_-
>
\frac12\log\frac BA-\delta.
\tag{31}
\]

This is an event-spacing condition independent of any hypothetical smooth relaxation. The gap has to be wide enough to accommodate the local plateau `X=\Phi(X)` after trimming asymptotically half of the logarithmic jump mass at each boundary.

Combining with `RE-001`,

\[
\boxed{
\mathrm{RH\ false}
\Longrightarrow
\text{infinitely many regular self-tangent CA gaps satisfy (29)--(31).}
}
\tag{32}
\]

An unconditional theorem that all sufficiently large regular returns violate this mass-versus-spacing condition would therefore close the Robin route.

## 6. New-prime boundaries turn the gate into an ordinary prime-gap restriction

There is a useful concrete specialization. Suppose the two adjacent CA transitions are both single **first-layer** insertions of new primes `p` and `q`. Then

\[
w_-=\log p,
\qquad
w_+=\log q,
\tag{33}
\]

and (11) gives

\[
p\le\eta_-<p+1,
\qquad
q\le\eta_+<q+1.
\tag{34}
\]

In particular

\[
\eta_+-\eta_-<q-p+1.
\tag{35}
\]

Combining (30), (33), and (35), every sufficiently large self-tangent Robin peak with such boundaries must satisfy

\[
\boxed{
q-p
>
\frac{\log p+\log q}{2}-1-o(1).
}
\tag{36}
\]

Thus bounded prime gaps, and more generally first-layer gaps with

\[
q-p\le(1-\delta)\log p
\]

for a fixed `delta>0` and sufficiently large comparable `p,q`, cannot bracket one of the counterexample peaks forced by `RE-001`. This does not prove that peak boundaries are eventually first-layer events; higher prime-power layers and semiprime transitions remain admissible. It identifies an explicit infinite class of local event geometries that is excluded without any RH-strength prime-distribution input.

## 7. Prior art, stress tests, and remaining boundary

The load-bearing literature inputs are deliberately modest. Alaoglu--Erdos supplies the prime-or-product-of-two-distinct-primes theorem for consecutive CA quotients; its stronger prime-only conjecture is not used. Bertrand's postulate is used only to guarantee one first-layer event before `2X+O(1)`, which bounds the coordinate of the actual next event. Robin supplies the CA reduction already used in `RE-001`. Mantovanelli's August 2026 preprint supplies the closest event-axis/workload prior-art framework, while `RE-001` independently reconstructs the identities needed here. Zimov's 2025 preprint is the closest located work using consecutive prime/semiprime CA quotients around a hypothetical Robin violation.

A targeted search across consecutive-CA quotient literature, Mantovanelli's self-tangent/workload terminology, and local Robin counterexample analyses did not locate the uniform splice (17) making the `RE-002` secant thresholds globally half-jump, nor the two-boundary event-mass condition (29)--(30). This is a mechanism-level boundary assessment, not a blanket novelty claim. The new step is elementary once the classical quotient theorem and exact event coordinates are put in the same normalization.

Several controls are essential. First, (15)--(16) require **true consecutive CA states**; arbitrary exponent exchanges need not have prime/semiprime quotient. Second, semiprime transitions are retained, so the unresolved four-exponentials conjecture is not imported. Third, (13) does not assume that prime events are consecutive: interlaced higher layers can only move the actual next event closer. Fourth, the first-layer corollary (36) must not be applied when either boundary transition increments an existing prime exponent or contains two tied prime factors.

Finally, a large enough event gap is only a necessary condition for a peak, not a sufficient one. Large prime gaps exist unconditionally, and higher-layer event spacing can create other chambers. No universal gap exclusion, workload sign theorem, Robin inequality improvement, or proof of RH is established. The durable narrowing is that the exact `RE-002` local gate has no hidden large-transition regime: every hypothetical self-tangent counterexample peak must satisfy an asymptotically half-mass spacing condition on its two actual neighboring CA events.