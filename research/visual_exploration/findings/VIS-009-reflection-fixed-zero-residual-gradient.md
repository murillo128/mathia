# VIS-009 — Reflection-fixed zeros force the first residual gradient along the symmetry line

## Claim

Let `f` be holomorphic near a point

`rho = 1/2 + i gamma`

and suppose that, in a neighborhood of the vertical line `Re(s)=1/2`, it obeys the reflection-real symmetry

`f(1-conj(s)) = conj(f(s))`.

Assume `rho` is a zero of exact multiplicity `m>=1`, and write

`f(rho+w) = a_m w^m + a_(m+1) w^(m+1) + O(w^(m+2))`, with `a_m != 0`.

Then

`a_(m+1)/a_m` is purely imaginary. Equivalently, for the Taylor-normalized residual

`H(w) = f(rho+w)/(a_m w^m) = 1 + c w + O(w^2)`,

one has `c in i R`. Writing `w=x+i y` and `c=i beta`, `beta in R`,

`log|H(x+i y)| = -beta y + O(x^2+y^2)`

and, after choosing the local argument branch with `arg H(0)=0`,

`arg H(x+i y) = beta x + O(x^2+y^2)`.

Thus, after the universal monomial of `VIS-008` is divided out, the **first-order modulus residual has zero normal derivative across the reflection line**:

`partial_x log|H|(0) = 0`.

Its first-order gradient is tangent to the fixed line, while the first-order phase residual is normal to it.

For Riemann's `xi` function this applies at every critical-line zero. At a simple zero `rho`,

`c = xi''(rho)/(2 xi'(rho)) in i R`.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + VISUAL-CONTROL + NEGATIVE/BASELINE`.

No novelty is claimed for the underlying reflection/Taylor fact. The research contribution is its role as a mandatory control for visual comparisons between critical-line zeros and off-line surrogate zeros.

## Exact derivation

The reflection map `s -> 1-conj(s)` fixes every point of `Re(s)=1/2`. Hence the assumed symmetry gives

`f(1/2+i t) in R`

for real `t` near `gamma`.

Set

`F(y) = f(rho+i y)`.

The function `F` is real-valued for real `y` near zero, and its Taylor expansion is

`F(y) = sum_(n>=m) a_n i^n y^n`.

Every Taylor coefficient of a real-valued real-analytic function is real, so

`a_n i^n in R`

for all relevant `n`. In particular there are real nonzero `r_m` and real `r_(m+1)` such that

`a_m = r_m i^(-m)`,
`a_(m+1) = r_(m+1) i^(-(m+1))`.

Therefore

`a_(m+1)/a_m = -i r_(m+1)/r_m in i R`.

Dividing the local expansion by `a_m w^m` gives

`H(w)=1+c w+O(w^2)`

with `c=i beta`. Since `H(0)=1`, a holomorphic logarithm exists near zero and

`log H(w)=c w+O(w^2)`.

Taking real and imaginary parts yields

`log|H(w)| = Re(i beta(x+i y))+O(|w|^2) = -beta y+O(|w|^2)`

and

`arg H(w) = Im(i beta(x+i y))+O(|w|^2) = beta x+O(|w|^2)`.

The directional statement is therefore exact and independent of rendering choices.

For `xi`, the standard functional equation `xi(s)=xi(1-s)` together with conjugation symmetry implies

`xi(1-conj(s))=conj(xi(s))`,

so the result applies on the critical line.

## Off-line surrogate confound

A reflection-symmetric off-line zero is not fixed by the reflection map: if

`rho_+ = 1/2 + epsilon + i gamma`,

then

`rho_- = 1/2 - epsilon + i gamma`

is its distinct reflected companion. If a local model factors as

`f(s)=(s-rho_+)(s-rho_-) g(s)`

with `g(rho_+) != 0`, then around `rho_+`, with `w=s-rho_+`,

`f(rho_+ + w)/(f'(rho_+) w)
 = (1 + w/(2 epsilon)) g(rho_+ + w)/g(rho_+)`.

Thus the first residual coefficient contains the explicit real term `1/(2 epsilon)`. In a surrogate family that perturbs only this reflection pair while the logarithmic derivative of `g` remains bounded, the horizontal residual slope becomes large as the pair approaches the critical line.

This does **not** prove that an arbitrary hypothetical off-line `xi` zero must have a nonzero horizontal residual gradient: the remaining factor can contribute and, in principle, cancel. It does show that a naive on-line/off-line visual control can be discriminated by the local symmetry-pair split alone. Such discrimination is therefore not evidence of a deeper mesoscopic or RH-specific geometry.

## Visual and computational audit

Visualization: [[research/visual_exploration/visualizations/critical-line-residual-gradient-baseline.md]].

The retained figure uses the first critical-line zero

`rho ~= 1/2 + 14.1347251417347 i`

and the spacing to the second positive critical-line zero,

`Delta ~= 6.88731449703686`.

The left panel renders

`R(x,y) = log|xi(rho + Delta(x+i y))/(xi'(rho) Delta(x+i y))|`

on `|x|,|y|<=0.34`, with the removable value at the origin filled by continuity. Its contours cross the critical line with the first-order orientation predicted above. Numerically,

`xi''(rho)/(2 xi'(rho)) ~= 0.579630577477882 i`,

so in spacing-normalized coordinates the linear coefficient has magnitude about `0.5796305775*Delta ~= 3.99210`.

As a direct arithmetic check rather than visual evidence, 50-digit evaluations at the first twenty positive critical-line zeros gave

`max |Re(xi''(rho)/(2 xi'(rho)))| < 1.6e-66`.

The imaginary parts varied substantially, so the observation is an axis constraint, not a claim of a universal residual profile.

The right panel is the explicit reflection-pair control

`P_epsilon(w)=w(w+2 epsilon)`

viewed from the zero at `w=0`, with `epsilon/Delta=0.25`. Its normalized residual is exactly `1+w/(2 epsilon)`, giving the orthogonal first-order gradient. The figure illustrates the theorem and the control failure mode; neither numerical panel is the proof.

## Prior-art and novelty assessment

NIST DLMF §25.4 gives Riemann's `xi` function and its reflection functional equation, while DLMF §25.10 records the critical-line symmetry setting for the nontrivial zeros. Combined with ordinary Taylor expansion, the fixed-line coefficient constraint above is immediate. It is treated here as classical symmetry calculus, not as a new theorem about `xi` or zeta zeros.

The useful new research role is negative/control-oriented: `VIS-008` says the leading normalized zero portrait is universal, and the present result shows that the **next first-order residual jet can still carry a trivial reflection-fixed-point signature**. Therefore a visual statistic that separates on-line and off-line zero controls at this order has not yet reached the intended mesoscopic question.

## Boundary conditions and counterarguments

The claim concerns the first residual Taylor coefficient after removing the zero multiplicity and leading coefficient. It does not say that higher jets, finite-radius contours, or mesoscopic fields are determined by reflection symmetry.

The coefficient `beta` need not be universal, nonzero, or bounded uniformly with height. If `beta=0`, the first nontrivial residual term starts at higher order.

The off-line pair calculation is a control model, not a theorem excluding cancellation from the remaining analytic factor in a full function. Its purpose is to identify a mechanism that can make an off-line surrogate visually easy to distinguish for an uninteresting reason.

Finally, the axis statement depends on using coordinates in which the reflection line is geometrically represented as `Re(s)=1/2`. Under a coordinate map that mixes normal and tangent directions, the rendered angle changes. The invariant content is that the differential of the modulus residual annihilates the normal direction to the fixed set of the anti-holomorphic reflection.

## Consequence for the research line

The accepted mesoscopic clue [[research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md]] must now control **two** local baselines before treating an on-line/off-line difference as interesting:

1. remove the universal multiplicity monomial from `VIS-008`;
2. remove or explicitly match the first residual jet forced by reflection fixing in this finding.

Only structure surviving beyond those local jets, at scales comparable to a non-negligible fraction of zero spacing and under matched reflection-symmetric controls, remains evidence for a genuinely mesoscopic visual question.
