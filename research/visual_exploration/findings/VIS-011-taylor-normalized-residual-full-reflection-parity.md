# VIS-011 — Taylor-normalized residuals inherit full reflection parity

## Claim

Let `f` be holomorphic near a point

`rho = 1/2 + i gamma`

and suppose

`f(1-conj(s)) = conj(f(s))`

near the critical line. Assume `rho` is a zero of exact multiplicity `m>=1` and write

`f(rho+w) = a_m w^m + a_(m+1) w^(m+1) + ...`, with `a_m != 0`.

Define the Taylor-normalized residual by removing the complete zero monomial,

`H(w) = f(rho+w)/(a_m w^m)`

for `w!=0`, with the removable value `H(0)=1`.

Then the residual inherits the exact anti-holomorphic reflection

`H(-conj(w)) = conj(H(w))`.

Consequently, wherever `H` is nonzero,

`log|H(-x+i y)| = log|H(x+i y)|`.

Thus the complete modulus residual is **even in the normal coordinate** to the fixed critical line, not merely to first order. In any local branch of the phase with `arg H(0)=0`,

`arg H(-x+i y) = -arg H(x+i y)`.

Equivalently, if

`H(w)=1+b_1 w+b_2 w^2+...`,

then

`conj(b_k)=(-1)^k b_k`:

even-indexed residual coefficients are real and odd-indexed residual coefficients are purely imaginary.

For Riemann's `xi` function this applies at every critical-line zero. Every odd normal derivative of `log|H|` therefore vanishes on the critical line wherever the logarithm is defined; every even normal derivative of the locally chosen phase vanishes there.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + VISUAL-CONTROL + NEGATIVE/BASELINE`.

The reflection identity is elementary classical symmetry calculus. The durable research consequence is that `VIS-009`'s first-jet control extends to the entire Taylor-normalized residual: left/right modulus asymmetry cannot be used as a nontrivial classifier of a reflection-fixed xi zero at any finite radius.

## Exact derivation

Set

`g(w)=f(rho+w)`.

Because `rho` is fixed by `s -> 1-conj(s)`, the assumed symmetry becomes

`g(-conj(w))=conj(g(w))`.

Comparing the Taylor series

`g(w)=sum_(n>=m) a_n w^n`

on both sides gives, coefficient by coefficient,

`conj(a_n)=(-1)^n a_n`.

In particular,

`conj(a_m)=(-1)^m a_m`.

Now evaluate the normalized residual under the reflection:

`H(-conj(w))
 = g(-conj(w)) / (a_m (-conj(w))^m)
 = conj(g(w)) / ((-1)^m a_m conj(w)^m)
 = conj(g(w)) / (conj(a_m) conj(w)^m)
 = conj(H(w))`.

Taking absolute values gives the exact modulus parity. Since `H(0)=1`, continuity gives a zero-free neighborhood of the origin and hence a holomorphic logarithm there. Conjugating that logarithm with the branch fixed by `log H(0)=0` gives the phase oddness.

For the coefficient form, write

`b_k=a_(m+k)/a_m`.

Then

`conj(b_k)
 = conj(a_(m+k))/conj(a_m)
 = (-1)^(m+k) a_(m+k) / ((-1)^m a_m)
 = (-1)^k b_k`.

`VIS-009` is the `k=1` differential consequence: `b_1` is purely imaginary, so the first normal derivative of `log|H|` vanishes. The present claim records that this parity continues through all orders and, more strongly, at finite radius wherever the normalized residual is defined.

## Relevance to visual exploration

The accepted critical-strip multiscale clue was already required to remove the universal monomial from `VIS-008` and to match the first residual jet from `VIS-009`. That gate was still too weak.

A critical-line zero is a fixed point of the anti-holomorphic reflection, so the whole Taylor-normalized modulus field is mirror symmetric. Any visual statistic that uses its antisymmetric component,

`A_odd(x,y) = (log|H(x+i y)| - log|H(-x+i y)|)/2`,

is identically zero for the exact object. Conversely, an off-line zero is not fixed by the reflection and can acquire a large antisymmetric component simply because its reflected partner is a distinct zero. Such separation is therefore a fixed-point classifier, not evidence of deeper mesoscopic organization.

The appropriate residual search must either use reflection-invariant quantities or quotient the symmetry explicitly, for example through

`A_even(x,y) = (log|H(x+i y)| + log|H(-x+i y)|)/2`.

Only structure inside that even component can address the intended mesoscopic question without reusing the exact symmetry baseline.

## Visual and computational audit

Visualization: [[research/visual_exploration/visualizations/critical-line-residual-exact-reflection-parity.md]].

For the first positive critical-line zero

`rho ~= 1/2 + 14.1347251417347 i`

and local spacing

`Delta ~= 6.88731449703686`,

the retained figure evaluates

`A(x,y)=log|xi(rho+Delta(x+i y))/(xi'(rho) Delta(x+i y))|`

on `|x|,|y|<=0.34`. The plotted finite-radius field is mirror symmetric; its direct double-precision mirror defect is at most `2.3e-16`.

A separate 50-digit check sampled a `5 x 5` spacing-normalized grid around each of the first twelve positive critical-line zeros, using the smaller adjacent zero spacing as local scale. The maximum observed defect

`|log|H(x+i y)|-log|H(-x+i y)||`

was below `7.1e-51`.

The figure also includes the split-pair normalized control

`Q(w)=1+w/(2 epsilon)`

with `epsilon/Delta=0.22`. Its mirror defect is nonzero at finite radius, illustrating that a zero not fixed by the reflection does not inherit the same centered parity. These calculations audit the implementation and visualize the theorem; they are not its proof.

## Prior art and novelty assessment

NIST DLMF §25.4 defines Riemann's `xi` function and records its functional equation, while the usual real-coefficient/conjugation property yields

`xi(1-conj(s))=conj(xi(s))`.

DLMF §25.10 records the corresponding symmetry of the nontrivial zero set about the critical line and the real axis. The general statement above is then an immediate consequence of Taylor expansion at a fixed point of an anti-holomorphic reflection.

No mathematical novelty is claimed for the reflection identity, coefficient parity, or its application to `xi`. The result is persisted because it materially strengthens a research control already used by this line: what `VIS-009` treated as a first-order baseline is in fact an all-orders and finite-radius baseline.

## Boundary conditions and counterarguments

The theorem does **not** determine the reflection-even part of the residual. Higher-order even geometry, interactions with neighboring zeros, scale dependence, and other mesoscopic structure remain unconstrained by this parity alone.

The phase statement requires a locally consistent branch and therefore is asserted in a zero-free neighborhood of `H(0)=1`. The modulus identity itself needs no phase branch and holds wherever the normalized residual is defined.

For an off-line zero, the global xi function still obeys the same reflection symmetry, but the reflection sends that zero to its distinct partner rather than fixing its local origin. Centering separately at one member of the pair therefore does not yield the fixed-point identity `H(-conj(w))=conj(H(w))`.

The result is coordinate-covariant rather than angle-dependent: in coordinates that straighten the anti-holomorphic involution, the modulus residual is invariant under its normal reflection. A rendering that mixes tangent and normal coordinates may obscure the visible axis but cannot remove the invariant symmetry.

Finally, this is not an RH criterion. If RH were false, zeros on the critical line would still satisfy this theorem, while an off-line pair would fail the fixed-point condition for the elementary reason above.

## Consequence for the research line

The accepted clue [[research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md]] must be narrowed beyond `VIS-009`: removing only the first residual jet is insufficient. Candidate mesoscopic statistics must quotient or respect the **full reflection parity** of the Taylor-normalized residual.

A useful positive would therefore have to live in reflection-even finite-radius structure, scale interaction, or another invariant that survives after this exact symmetry is removed. A visual distinction driven by left/right modulus asymmetry around an individual zero is now closed as a research route.