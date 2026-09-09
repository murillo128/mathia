# RE-002 — self-tangent Robin peaks require secant-clear CA transition gaps

**Status:** `EXACT-DERIVED + LOCAL-PEAK-EQUIVALENCE + SELF-TANGENT-GAP-GATE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-AUDITED`. `RE-001` reduces hypothetical RH failure to infinitely many regular self-tangent colossally abundant states that are local/block maxima of Robin's quotient on the CA ladder. The self-tangent condition alone only says that the intrinsic Robin tangent parameter lies between the two adjacent CA supporting slopes. Reopening the exact finite differences shows that a peak requires strictly more: the two transition coordinates must clear explicit **secant-balance points** determined by the full `log log n` normalization and the actual logarithmic jump sizes to the neighboring CA states.

Let

\[
\rho(n):=\frac{\sigma(n)}n,
\qquad
G(n):=\frac{\rho(n)}{\log\log n},
\qquad
H(X):=\log\log X,
\qquad
g(X):=H'(X)=\frac1{X\log X}.
\tag{1}
\]

Take three consecutive CA states

\[
A<C<B
\tag{2}
\]

in the large-number regime, put

\[
X:=\log C,
\qquad
w_-:=\log\frac CA,
\qquad
w_+:=\log\frac BC,
\tag{3}
\]

and let `epsilon_-`, `epsilon_+` be the exact supporting parameters of the transitions `A -> C` and `C -> B`. Define their transition coordinates by

\[
\eta_-:=g^{-1}(\varepsilon_-),
\qquad
\eta_+:=g^{-1}(\varepsilon_+).
\tag{4}
\]

For a regular self-tangent state `C`, `RE-001` gives

\[
\varepsilon_+<g(X)<\varepsilon_-,
\qquad
\text{equivalently}\qquad
\eta_-<X<\eta_+.
\tag{5}
\]

Now define the two secant-balance points `xi_-` and `xi_+` by

\[
g(\xi_-)
=\frac{H(X)-H(X-w_-)}{w_-},
\qquad
X-w_-<\xi_-<X,
\tag{6}
\]

and

\[
g(\xi_+)
=\frac{H(X+w_+)-H(X)}{w_+},
\qquad
X<\xi_+<X+w_+.
\tag{7}
\]

Then the neighboring Robin comparisons are exactly

\[
\boxed{
G(C)>G(A)\iff \eta_-<\xi_-,
}
\tag{8}
\]

and

\[
\boxed{
G(C)\ge G(B)\iff \eta_+\ge\xi_+.
}
\tag{9}
\]

Thus every self-tangent CA peak furnished by `RE-001` under hypothetical RH failure must satisfy **both** local clearance inequalities. Merely having a regular self-tangent return in the event/workload process is insufficient. This converts the next counterexample-exclusion problem into a local geometric statement about the adjacent CA transition coordinates and their true jump masses.

## 1. Exact finite differences isolate the secant thresholds

For consecutive CA states, the supporting-slope identity used in `RE-001` is

\[
\log\rho(C)-\log\rho(A)=\varepsilon_-\log\frac CA
=\varepsilon_-w_-,
\tag{10}
\]

and

\[
\log\rho(B)-\log\rho(C)=\varepsilon_+\log\frac BC
=\varepsilon_+w_+.
\tag{11}
\]

Because

\[
\log G(n)=\log\rho(n)-H(\log n),
\tag{12}
\]

we get the exact left increment

\[
\begin{aligned}
\log\frac{G(C)}{G(A)}
&=\varepsilon_-w_-
 -\bigl(H(X)-H(X-w_-)\bigr)\\
&=w_-\left[
 g(\eta_-)
 -\frac{H(X)-H(X-w_-)}{w_-}
\right]\\
&=\boxed{w_-\bigl(g(\eta_-)-g(\xi_-)\bigr)}.
\end{aligned}
\tag{13}
\]

Similarly

\[
\boxed{
\log\frac{G(B)}{G(C)}
=w_+\bigl(g(\eta_+)-g(\xi_+)\bigr).
}
\tag{14}
\]

The function `g` is strictly decreasing for `X>1`, since

\[
g'(X)
=-\frac{\log X+1}{X^2(\log X)^2}<0.
\tag{15}
\]

Therefore the signs of (13)--(14) are exactly equivalent to (8)--(9). No asymptotic approximation, prime-number-theorem input, or continuous relaxation is used.

The points in (6)--(7) exist uniquely by the mean-value theorem. If an explicit closed form is useful, solving `g(x)=s` gives

\[
g^{-1}(s)=\exp W(1/s),
\tag{16}
\]

where `W` is the principal Lambert function. Hence

\[
\xi_-
=\exp W\!\left(
\frac{w_-}
{\log\!\bigl(\log X/\log(X-w_-)\bigr)}
\right),
\tag{17}
\]

and

\[
\xi_+
=\exp W\!\left(
\frac{w_+}
{\log\!\bigl(\log(X+w_+)/\log X\bigr)}
\right).
\tag{18}
\]

The implicit definitions (6)--(7) are usually cleaner, but (17)--(18) show that the gate is an explicit finite inequality in the neighboring CA data.

## 2. Self-tangency leaves a corridor; a peak needs additional clearance inside it

For a regular self-tangent state, (5) only places the transition coordinates on opposite sides of `X`. Concavity of `H` gives

\[
\frac{H(X)-H(X-w_-)}{w_-}>g(X)
>\frac{H(X+w_+)-H(X)}{w_+}.
\tag{19}
\]

Since `g` is decreasing, this is equivalent to

\[
\xi_-<X<\xi_+.
\tag{20}
\]

Combining (5) and (20), self-tangency supplies the broad ordering

\[
\eta_-<X<\eta_+,
\qquad
\xi_-<X<\xi_+,
\tag{21}
\]

but does **not** determine the relative order of `eta_-` versus `xi_-`, or `eta_+` versus `xi_+`. Equations (8)--(9) are precisely the missing comparisons.

Thus a self-tangent return can fail to be a Robin peak in either of two local ways:

\[
\eta_-\ge\xi_-
\quad\Longrightarrow\quad
G(C)\le G(A),
\tag{22}
\]

or

\[
\eta_+<\xi_+
\quad\Longrightarrow\quad
G(B)>G(C).
\tag{23}
\]

This is useful for the RH-facing reduction because `RE-001` does not merely require self-tangent states under RH failure; it produces self-tangent **block maxima**. A theorem forcing either (22) or (23) for all sufficiently large regular returns would therefore eliminate the entire hypothetical counterexample subclass isolated there.

## 3. The left side already requires more than half a logarithmic jump of clearance

The derivative `g` is not only decreasing but strictly convex:

\[
\boxed{
g''(X)
=\frac{2(\log X)^2+3\log X+2}
       {X^3(\log X)^3}>0.
}
\tag{24}
\]

Equation (6) can be written as the average

\[
g(\xi_-)
=\frac1{w_-}\int_{X-w_-}^{X}g(t)\,dt.
\tag{25}
\]

Hermite--Hadamard/Jensen convexity gives

\[
g(\xi_-)
\ge g\!\left(X-\frac{w_-}{2}\right).
\tag{26}
\]

Because `g` is decreasing,

\[
\boxed{
\xi_-\le X-\frac{w_-}{2}.
}
\tag{27}
\]

Consequently every strict left-hand Robin rise satisfies the exact necessary condition

\[
\boxed{
G(C)>G(A)
\Longrightarrow
X-\eta_->X-\xi_-\ge\frac{w_-}{2}.
}
\tag{28}
\]

A self-tangent point sitting less than half the preceding logarithmic CA jump away from its previous transition coordinate cannot be the left edge of the counterexample peak selected in `RE-001`.

There is no symmetric exact `w_+/2` lower bound on the right. Convexity places `xi_+` on the **left** side of the midpoint of `[X,X+w_+]`, so imposing a literal half-jump condition there would be an invalid strengthening. The correct right threshold is the exact point `xi_+` in (7).

## 4. Small relative jumps make both thresholds asymptotically half-jump

The exact gate is useful without any size hypothesis on `w_\pm`. In the common regime where the neighboring logarithmic jumps satisfy

\[
w_\pm=o(X),
\tag{29}
\]

its geometry becomes especially transparent. Write

\[
\kappa(X)
:=-\frac{g''(X)}{24g'(X)}
=\frac{2(\log X)^2+3\log X+2}
{24X\log X(\log X+1)}>0.
\tag{30}
\]

Taylor expansion of the two secant averages, followed by inversion through `g`, gives

\[
\boxed{
X-\xi_-
=\frac{w_-}{2}
 +\kappa(X)w_-^2
 +O\!\left(\frac{w_-^3}{X^2}\right),
}
\tag{31}
\]

and

\[
\boxed{
\xi_+-X
=\frac{w_+}{2}
 -\kappa(X)w_+^2
 +O\!\left(\frac{w_+^3}{X^2}\right).
}
\tag{32}
\]

Here the error is uniform once `X` stays in the large Robin regime and `w_\pm/X -> 0`; the derivative ratios `g'''/g'` are `O(X^{-2})`. Thus a self-tangent local peak requires, asymptotically,

\[
X-\eta_-
>\frac{w_-}{2}
 +O\!\left(\frac{w_-^2}{X}\right),
\tag{33}
\]

and

\[
\eta_+-X
\ge\frac{w_+}{2}
 +O\!\left(\frac{w_+^2}{X}\right),
\tag{34}
\]

with the signed second-order corrections given explicitly by (31)--(32). The phrase “half-jump clearance” should therefore be understood as an asymptotic description of the exact secant gate, not as a symmetric finite theorem.

This expansion does not require the conjecture that every consecutive CA quotient is prime. If a particular transition theorem supplies `w_\pm=O(\log X)`, then the correction in (31)--(32) is only `O((\log X)^2/X)`; otherwise the exact formulas (6)--(9) remain the valid statements.

## 5. Counterexample exclusion becomes a local event-gap problem

`RE-001` proves

\[
\mathrm{RH\ false}
\Longrightarrow
\text{infinitely many regular self-tangent CA counterexample peaks}.
\tag{35}
\]

Every one of those peaks has adjacent CA states and supporting coordinates satisfying (8)--(9). Hence

\[
\boxed{
\mathrm{RH\ false}
\Longrightarrow
\text{infinitely many regular self-tangent returns obey both secant-clearance inequalities.}
}
\tag{36}
\]

Equivalently, an unconditional theorem of the form

\[
\text{every sufficiently large regular self-tangent return satisfies }
\eta_-\ge\xi_-\text{ or }\eta_+<\xi_+
\tag{37}
\]

would contradict (36) and therefore prove RH through the already-established Robin reduction.

This is a different proof obligation from controlling the full workload integral between distant self-tangent states. It asks whether the **immediate** CA transition geometry around a return allows that return to be a local Robin peak at all. The workload/moment route remains valid and may be stronger globally; (37) is a local alternative that could be attacked using exact event spacing, transition quotients, or prime-layer interlacing.

The condition is not automatically easy. First-layer transition coordinates track primes at roughly the same logarithmic scale, so proving a universal clearance failure may encounter genuine prime-gap structure. Higher prime-power layers can also interlace those events. The gain is precision, not a claim that the remaining theorem is elementary.

## 6. Prior art, audit, and evidence boundary

Alaoglu--Erdos and Robin provide the classical CA variational slopes and the Robin extremal reduction. `RE-001` reconstructs the exact self-tangent consequence needed here. Marco Mantovanelli's August 2026 preprint is the closest current representation-level prior art: it places the CA thresholds on the `X=log n` event axis, identifies regular self-tangent returns, proves the exact workload/packet identity, develops a positive moment hierarchy, and gives a prime-frontier normal form. Those objects are therefore treated as prior art in this finding.

Bruce Zimov's 2025 preprint *On the Least Colossally Abundant Exception to Robin's Inequality* analyzes consecutive CA quotients to bound the possible size of the least CA counterexample. It is the closest located work focused directly on one-step CA changes near a hypothetical violation. Its stated mechanism is quotient-growth comparison, not the intrinsic tangent-versus-normalization secant gate (8)--(9).

A targeted search across the Mantovanelli workload terminology, consecutive-CA counterexample literature, and local-extremum formulations did not locate the exact secant-balanced transition-coordinate equivalence above. That is a boundary assessment, not a blanket novelty claim. The calculus in (13)--(34) is elementary once the exact CA supporting slopes are exposed; the Mathia-specific contribution is the splice to the self-tangent counterexample reduction and the resulting local exclusion target (37).

Several boundaries are load-bearing. First, `A<C<B` must be actual consecutive CA states with their true supporting transition parameters; arbitrary prime-exponent moves do not satisfy (10)--(11). Second, self-tangency alone is not upgraded to a peak: the whole point of (8)--(9) is to distinguish those notions. Third, tied CA transition parameters can be handled through the same total logarithmic jump whenever the chosen consecutive endpoints share that supporting slope, but intermediate tied maximizers must not be silently omitted when claiming a local maximum over the full CA ladder.

Finally, (37) is not proved here. No universal transition-gap bound, prime-gap estimate, workload sign theorem, Robin improvement, or RH proof is established. The durable result is the exact local criterion and its consequence that hypothetical Robin failure needs infinitely many self-tangent returns with a much more specific neighboring-transition geometry than `D(X)=0` alone.