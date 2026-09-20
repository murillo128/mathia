# VIS-347 — variable Wang phase banks pay a Turán–Nazarov phase-entropy budget

## Claim

Let Wang's exact multiplier be

`m(xi)=4(1+i xi)/(4+xi^2)`.

For each large `X`, consider a finite translated-dilate bank

`M_X(xi)=sum_j c_(j,X) exp(-i b_(j,X) xi) m(a_(j,X) xi)`,

with `a_(j,X)>0` and frequency-independent complex coefficients. Group terms with the same translation and define the first inverse-scale moment

`S_(b,X)=sum_(j:b_(j,X)=b) c_(j,X)/a_(j,X)`

and the scale-conditioning quantity

`T_X=sum_j |c_(j,X)|/a_(j,X)^2`.

Let `B_X` be the number of translations with `S_(b,X) != 0`; if `B_X>=2`, let

`Delta_X=min_(b!=b') |b-b'|`

among those active first-moment phases. Let `J_X subset [X,2X]` be an interval of length `ell_X>0` and suppose, for some fixed `r>=2`,

`sup_(xi in J_X) |M_X(xi)| <= C_0 X^(-r)`.

Define

`P_X(xi)=sum_b S_(b,X) exp(-i b xi)`.

Then the exact rational form of `m` gives

`sup_(xi in J_X)|P_X(xi)| <= D_X/X`,

where

`D_X=C_0/2+2T_X`.

If `B_X=1`, this already forces

`X ||S_X||_2 <= D_X`.

If `B_X>=2`, put

`L_X=4(B_X-1)/Delta_X`,
`e_X=min(ell_X,L_X)`.

There is an absolute Turán–Nazarov constant `A>=1` such that every nonzero first-moment vector must satisfy the necessary budget

`(B_X-1) log(A L_X/e_X)`
` >= log( X ||S_X||_2 / (sqrt(2) D_X) )`.

Equivalently,

`sup_(xi in J_X)|P_X(xi)|`
` >= (1/sqrt(2)) ||S_X||_2 (e_X/(A L_X))^(B_X-1)`.

Thus a scale-dependent translated Wang bank cannot evade the fixed-bank obstruction merely by allowing its phase geometry to vary with `X`. To obtain even the first extra inverse-frequency order on a window, it must pay through at least one of:

- growing phase complexity `B_X`;
- shrinking windows `ell_X`;
- coalescing phase gaps `Delta_X`;
- a first-moment vector `||S_X||_2` that itself becomes small;
- a growing tail/conditioning cost `T_X`.

In particular, if

`D_X/||S_X||_2 = X^(o(1))`,

then the phase-entropy term must obey

`(B_X-1) log(A L_X/e_X) >= (1-o(1)) log X`.

Two useful corollaries are immediate.

1. If `B_X=B>=2` is fixed, `ell_X=X^(-alpha+o(1))`, and `Delta_X=X^(-beta+o(1))`, then nondegenerate first-moment cancellation requires

`(B-1)(alpha+beta) >= 1`.

For `beta=0` this recovers the fixed-gap threshold of `VIS-346`; phase coalescence and window shrinkage enter only through their combined logarithmic resolution cost.

2. If `ell_X` and `Delta_X` are bounded below by positive constants while `B_X->infinity`, then nondegenerate cancellation requires

`B_X log B_X >= (1-o(1)) log X`,

up to constants depending only on those lower bounds and on `A`. Hence a well-separated macroscopic-window escape needs at least logarithmic-over-logarithmic phase complexity:

`B_X = Omega(log X / log log X)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TURAN-NAZAROV PROPAGATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The result is a necessary first-moment obstruction, not a construction and not a theorem about the arithmetic remainder `G`. It does not exclude banks that genuinely pay the displayed phase-entropy budget, frequency/source-dependent coefficients, infinite expansions, or signed arithmetic estimates that do not require one multiplier to be uniformly small on a window.

## 1. Wang's exact first tail has a uniform remainder bound

For real `z>0`,

`m(z)-4i/z = 4(z-4i)/(z(z^2+4))`.

Moreover,

`z^2 |m(z)-4i/z|`
` = 4z sqrt(z^2+16)/(z^2+4)`
` <= 4z(z+4)/(z^2+4)`
` <= 8`.

Therefore, term by term,

`M_X(xi)=4i xi^(-1) P_X(xi)+R_X(xi)`

with

`|R_X(xi)| <= 8 xi^(-2) T_X`.

On `J_X subset [X,2X]`,

`|P_X(xi)|`
` <= (xi/4)|M_X(xi)| + (xi/4)|R_X(xi)|`
` <= (C_0/2) X^(1-r) + 2T_X/X`
` <= D_X/X`,

because `r>=2`.

This step is important for a changing bank: all dependence on dilation scales and coefficient magnitudes is exposed explicitly through `T_X` rather than hidden in an asymptotic `O`-constant.

## 2. A variable phase bank still has a reference-frame lower bound

Write

`P_X(xi)=sum_(p=1)^(B_X) d_(p,X) exp(-i b_(p,X) xi)`

using only nonzero first-moment coefficients. For `B_X>=2`, choose an interval `I_X` of length

`L_X=4(B_X-1)/Delta_X`

that contains a subinterval `E_X subset J_X` of length

`e_X=min(ell_X,L_X)`.

The direct finite exponential-sum calculation used in `VIS-345` is pointwise in the bank parameters. Since `L_X Delta_X=4(B_X-1)`, it gives

`RMS_(I_X)(P_X) >= (1/sqrt(2)) ||S_X||_2`,

and hence

`sup_(I_X)|P_X| >= (1/sqrt(2)) ||S_X||_2`.

No fixed-in-`X` phase separation is required here; the reference interval simply grows as the phase geometry becomes harder to resolve.

## 3. Turán–Nazarov converts concentration into an entropy budget

For an exponential polynomial with `B_X` terms and purely imaginary exponents, the measurable Turán–Nazarov inequality gives an absolute constant `A` such that

`sup_(I_X)|P_X|`
` <= (A |I_X|/|E_X|)^(B_X-1) sup_(E_X)|P_X|`.

Combining this with the reference-frame lower bound yields

`sup_(J_X)|P_X|`
` >= sup_(E_X)|P_X|`
` >= (1/sqrt(2)) ||S_X||_2 (e_X/(A L_X))^(B_X-1)`.

The upper bound from the exact Wang remainder then gives

`D_X/X`
` >= (1/sqrt(2)) ||S_X||_2 (e_X/(A L_X))^(B_X-1)`.

Taking logarithms proves the claimed phase-entropy inequality whenever the right-hand logarithm is positive; when it is nonpositive the inequality is true but gives no useful obstruction.

This identifies the previously qualitative escape parameters on one common scale. Adding phases, shrinking the observation window, and coalescing phases all increase the Turán–Nazarov concentration budget, while small first moments or a large `T_X` weaken the information carried by the bank before any arithmetic input is used.

## 4. Power-law and growing-phase consequences

Assume first that `B_X=B` is fixed and

`ell_X=X^(-alpha+o(1))`,
`Delta_X=X^(-beta+o(1))`.

Eventually `e_X=ell_X`, and

`log(A L_X/e_X)=(alpha+beta+o(1)) log X`.

If `D_X/||S_X||_2=X^(o(1))`, the phase-entropy inequality therefore forces

`(B-1)(alpha+beta)>=1`.

So a bounded number of phases can trade window localization against phase coalescence, but cannot avoid paying one full logarithmic power in their combined resolution scale.

Now suppose instead that `ell_X>=ell_0>0` and `Delta_X>=Delta_0>0`. For growing `B_X`, one has `L_X=O(B_X)` and eventually `e_X>=min(ell_0,L_X)` with

`log(A L_X/e_X)=O(log B_X)`.

The nondegenerate budget then implies

`B_X log B_X >= (1-o(1)) log X`,

which in turn requires `B_X=Omega(log X/log log X)` up to absolute/lower-bound constants. A changing bank can therefore evade the fixed finite-bank theorem by growing its phase dimension, but not at bounded or extremely slowly growing complexity if it keeps macroscopic windows, separated phases, and controlled coefficient geometry.

## Prior-art audit

The propagation inequality is classical. F. L. Nazarov, **Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type**, *Algebra i Analiz* 5:4 (1993), 3–66; English translation *St. Petersburg Mathematical Journal* 5:4 (1994), 663–717, gives the local Turán-type estimates for exponential polynomials underlying `VIS-346` and the present variable-parameter application.

Omer Friedland and Yosef Yomdin, **An observation on the Turán–Nazarov inequality**, *Studia Mathematica* 218:1 (2013), 27–39, DOI `10.4064/sm218-1-2`, explicitly treats the measurable-set form and refinements by metric entropy. The original Turán–Nazarov inequality already carries the number-of-terms exponent used here; no novelty is claimed for that concentration theorem.

The Mathia-specific contribution is only the coupling of the classical variable-`B` concentration factor with Wang's exact rational first-tail remainder, exposing `B_X`, `Delta_X`, `ell_X`, `||S_X||_2`, and `T_X` in one necessary budget. This is a direct extension of the fixed-bank obstruction in `VIS-346`, not a new general theorem on exponential polynomials.

## Dependencies

- `VIS-333`: exact Wang multiplier and source transfer.
- `VIS-343`: inverse-scale moment interpretation for Wang dilates.
- `VIS-344`: translation-fiber moment decomposition.
- `VIS-345`: phase-frame lower bound on a resolving interval.
- `VIS-346`: fixed-bank Turán–Nazarov shrinking-window obstruction.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue narrowed here.

## Research consequence

The phrase "let the packet bank vary with scale" is no longer by itself an escape from the fixed-bank negative results. Before any arithmetic advantage is credited, a scale-dependent Wang construction must exhibit enough phase entropy to satisfy the displayed budget or explain explicitly which conditioning quantity degenerates.

For separated phases on macroscopic windows, the first-moment gate alone forces `B_X` to grow at least on the order of `log X/log log X`. For bounded phase count, microscopic windows and coalescing phases obey the combined threshold `(B-1)(alpha+beta)>=1`. A surviving route must therefore either pay this structural complexity honestly or exploit signed/source-dependent information in `G` that is not equivalent to uniform multiplier smallness.