# PL-373 — Infinite-alphabet Venturini witnesses are Liouville times a zero-free holomorphic gauge

**Evidence:** `VENTURINI-2020 + EXACT-DERIVED-EULER-LOG + PRIOR-ART-CALIBRATED + DECISIVE-NARROWING`.

**Parent finding:** `PL-372`.

**Related findings:** `PL-369`, `PL-370`, `PL-371`, `PL-372`.

**Status:** `IN-THE-RH-RELEVANT-HALF-PLANES-EVERY-GENUINE-VENTURINI-WITNESS-HAS-THE-LIOUVILLE-DIVISOR-UP-TO-A-HOLOMORPHIC-ZERO-FREE-FACTOR; FOR-INFINITE-ALPHABETS-THE-REMAINING-FIRST-ORDER-PRIME-DEFECT-MUST-ITSELF-ADMIT-HOLOMORPHIC-CONTINUATION`.

## Claim

Fix

\[
\frac12\le \sigma_0<1,
\qquad
\Omega_{\sigma_0}=\{s:\Re s>\sigma_0\}.
\]

Let `a:N->C` be bounded and completely multiplicative, and let

\[
L(a,s)=\sum_{n\ge1}\frac{a(n)}{n^s}
\]

be its Dirichlet series on `Re(s)>1`.

Assume that `L(a,s)` extends holomorphically to `Omega_(sigma_0)` and that

\[
L(a,1)=0.
\]

Then there exists a holomorphic zero-free function `C_a` on `Omega_(sigma_0)` such that

\[
\boxed{
L(a,s)=\frac{\zeta(2s)}{\zeta(s)}\,C_a(s)
}
\tag{PL373-1}
\]

throughout that half-plane, with the equality interpreted after the removable singularity at `s=1` is filled in.

Thus the finite-alphabet hypothesis in `PL-372` is **not needed for divisor rigidity**. It was needed there only to obtain a normally convergent relative Euler product. Every genuine Venturini witness in the RH-relevant range already has exactly the Liouville zero/pole divisor; an infinite alphabet can alter only a zero-free holomorphic gauge.

There is also a sharper first-order consequence. On `Re(s)>1`, define

\[
P_a(s)=\sum_p\frac{1+a(p)}{p^s}.
\tag{PL373-2}
\]

Then `P_a` admits a holomorphic continuation to all of `Omega_(sigma_0)`.

Conversely, suppose only that `|a(p)|<=1` and that the prime series `P_a(s)` in (PL373-2) has a holomorphic continuation to `Omega_(sigma_0)`. Then the original Dirichlet series has the meromorphic continuation

\[
L(a,s)=\frac{\zeta(2s)}{\zeta(s)}
\exp\bigl(P_a(s)+R_a(s)\bigr),
\tag{PL373-3}
\]

where `R_a` is holomorphic on `Re(s)>1/2`. The exponential factor is zero-free, so this continuation is holomorphic on `Omega_(sigma_0)` **if and only if** zeta is zero-free there. In particular, conditional first-order organization of an infinite prime alphabet cannot cancel, move, or hide a zeta zero.

No theorem-priority claim is made. The forward nonvanishing input is Venturini's 2020 theorem and its proof; the Liouville-gauge factorization and first-order logarithmic splitting below are exact consequences of that input and elementary Euler-log comparison.

## 1. Venturini makes the witness itself zero-free away from the forced zero

Venturini proves that if a bounded completely multiplicative `a` has a Dirichlet series holomorphic on `Omega_(sigma_0)` with `L(a,1)=0`, then zeta is zero-free on the same half-plane.

The proof gives slightly more structure than the headline implication. On `Re(s)>1` he forms a conjugate symmetrization of the shape

\[
F(s)=\zeta(s)^2L(a,s)L^\sharp(a,s),
\qquad
L^\sharp(a,s)=\overline{L(a,\overline s)},
\tag{PL373-4}
\]

and writes `F=exp G`, where `G` is a Dirichlet series with nonnegative coefficients. His nonvanishing principle extends `G` holomorphically whenever `F` extends, and therefore forces

\[
F(s)\ne0
\qquad(s\in\Omega_{\sigma_0}).
\tag{PL373-5}
\]

The zero of `L(a,s)` at `1` cancels the zeta pole in (PL373-4); `PL-370` independently shows that this zero is simple. At any other point of `Omega_(sigma_0)`, Venturini's theorem gives `zeta(s)!=0`, while zeta has no pole away from `1`. Hence (PL373-5) implies

\[
L(a,s)\ne0
\qquad
(s\in\Omega_{\sigma_0},\ s\ne1).
\tag{PL373-6}
\]

This is the load-bearing point for the infinite-alphabet argument: the continued witness has no private zero divisor available to compensate a zeta pole in a relative quotient.

Primary source: Sergio Venturini, “Non vanishing of Dirichlet series of completely multiplicative functions,” *Rivista di Matematica della Università di Parma* **11**(1) (2020), 153–180, arXiv:2002.08903, especially Theorems 1.2 and 1.3 and the proof in Section 4.

## 2. The Liouville quotient is holomorphic and zero-free without a finite alphabet

Write

\[
Q(s)=L(\lambda,s)=\frac{\zeta(2s)}{\zeta(s)}.
\tag{PL373-7}
\]

Because `sigma_0>=1/2`, every point of `Omega_(sigma_0)` satisfies `Re(2s)>1`. Therefore `zeta(2s)` is holomorphic and nonzero throughout this open half-plane.

Venturini gives `zeta(s)!=0` there. Consequently `Q` is holomorphic on `Omega_(sigma_0)`, except that the pole of zeta at `s=1` appears as a simple zero of `Q`. It has no other zero or pole in the half-plane.

By `PL-370`, `L(a,s)` also has a simple zero at `1`, and by (PL373-6) it has no other zero there. Therefore

\[
C_a(s)=\frac{L(a,s)}{Q(s)}
      =\frac{L(a,s)\zeta(s)}{\zeta(2s)}
\tag{PL373-8}
\]

has a removable singularity at `1` and extends to a holomorphic zero-free function on all of `Omega_(sigma_0)`. This proves (PL373-1).

The distinction from `PL-372` is important. For a finite prime alphabet, `PL-372` proved that `C_a` is represented by a normally convergent relative Euler product throughout the continued half-plane. For a general infinite alphabet, (PL373-8) gives the same divisor conclusion **analytically**, but does not assert absolute or normal convergence of the relative Euler product there.

## 3. The higher prime powers are harmless beyond the half-line

On `Re(s)>1`, all Euler products and logarithms below are absolutely convergent. Since

\[
\frac{L(a,s)}{L(\lambda,s)}
=
\prod_p\frac{1+p^{-s}}{1-a(p)p^{-s}},
\tag{PL373-9}
\]

we have

\[
\log C_a(s)
=
\sum_p\sum_{k\ge1}
\frac{a(p)^k-(-1)^k}{k p^{ks}}.
\tag{PL373-10}
\]

Separate the first prime-axis layer from the higher powers:

\[
P_a(s)=\sum_p(1+a(p))p^{-s},
\tag{PL373-11}
\]

and

\[
R_a(s)=
\sum_p\sum_{k\ge2}
\frac{a(p)^k-(-1)^k}{k p^{ks}}.
\tag{PL373-12}
\]

Bounded complete multiplicativity implies `|a(p)|<=1`. Hence, for every compact set contained in `Re(s)>1/2`, choose `sigma>1/2` below all its real parts. Uniformly on that compact set,

\[
|R_a(s)|
\le
2\sum_p\sum_{k\ge2}\frac{p^{-k\sigma}}k.
\tag{PL373-13}
\]

The right side converges because its leading term is controlled by `sum_p p^(-2 sigma)`. Thus

\[
\boxed{R_a\text{ is holomorphic on }\Re s>1/2.}
\tag{PL373-14}
\]

All possible non-absolute first-order behavior of the relative Euler logarithm is therefore concentrated in `P_a`. Higher prime powers cannot carry a hidden continuation obstruction in the RH-relevant half-plane.

## 4. A genuine witness forces the first-order prime defect to continue

The half-plane `Omega_(sigma_0)` is simply connected, and `C_a` is holomorphic and zero-free there. It therefore has a holomorphic logarithm `H_a`:

\[
C_a(s)=e^{H_a(s)}.
\tag{PL373-15}
\]

On the connected sub-half-plane `Re(s)>1`, choose the additive constant in `H_a` so that it agrees with the absolutely convergent Euler logarithm (PL373-10). Then

\[
H_a(s)=P_a(s)+R_a(s)
\qquad(\Re s>1).
\tag{PL373-16}
\]

Since `H_a` is holomorphic on `Omega_(sigma_0)` and `R_a` is holomorphic on the larger half-plane `Re(s)>1/2`, the difference

\[
\widetilde P_a(s)=H_a(s)-R_a(s)
\tag{PL373-17}
\]

is holomorphic on `Omega_(sigma_0)` and agrees with the prime Dirichlet series `P_a` on `Re(s)>1`. By uniqueness of analytic continuation, it is the holomorphic continuation of `P_a`.

Thus the “conditionally organized first-order prime information” left open after `PL-372` is not unconstrained. If it comes from a genuine Venturini witness, its prime series must itself cross every point of the same half-plane holomorphically.

This condition is diagnostic rather than constructive. It is forced by an already-existing global continuation of `L(a,s)`; it does not produce that continuation by itself.

## 5. Conversely, first-order continuation can only supply a zero-free gauge

The previous argument can be reversed without assuming a Venturini witness.

Let prime values satisfy `|a(p)|<=1`, extend them completely multiplicatively, and suppose the series

\[
P_a(s)=\sum_p(1+a(p))p^{-s}
\]

has a holomorphic continuation to `Omega_(sigma_0)`. Define `R_a` by (PL373-12), which is already holomorphic on `Re(s)>1/2`, and set

\[
C_a(s)=\exp(P_a(s)+R_a(s)).
\tag{PL373-18}
\]

Then `C_a` is holomorphic and zero-free on `Omega_(sigma_0)`. On `Re(s)>1`, absolute Euler expansion gives exactly

\[
C_a(s)=\frac{L(a,s)}{L(\lambda,s)}.
\tag{PL373-19}
\]

Therefore

\[
\widetilde L_a(s)
=
\frac{\zeta(2s)}{\zeta(s)}C_a(s)
\tag{PL373-20}
\]

is the meromorphic continuation of the original Dirichlet series from `Re(s)>1` into `Omega_(sigma_0)`.

Inside this half-plane `zeta(2s)` is nonzero and `C_a(s)` is nonzero. Hence every zeta zero in `Omega_(sigma_0)` produces an uncancelled pole of `\widetilde L_a`, while if zeta is zero-free there the continuation is holomorphic. At `s=1`, the pole of zeta in the denominator gives a simple zero because the other factors are finite and nonzero.

Consequently

\[
\boxed{
\widetilde L_a\text{ holomorphic on }\Omega_{\sigma_0}
\iff
\zeta(s)\ne0\text{ on }\Omega_{\sigma_0}.
}
\tag{PL373-21}
\]

This closes the most direct infinite-alphabet escape left by `PL-372`: even a conditionally continued first-order prime defect cannot provide a compensating zero. Its exponential is necessarily a zero-free gauge multiplying the Liouville quotient.

## 6. Adversarial controls and boundaries

### No Euler product is being continued formally

Equations (PL373-9)--(PL373-12) are derived only on `Re(s)>1`, where absolute convergence is available. Beyond that line, `R_a` is continued by an independently absolutely convergent series and `P_a` by a holomorphic function. The factorization then follows by analytic uniqueness. Nothing treats the original Euler product as convergent in the critical strip.

### Infinite alphabets remain different from finite alphabets

This finding does **not** upgrade `C_a` to a normally convergent relative Euler product on `Omega_(sigma_0)`. The weighted `ell^2` control from `PL-372` still does not imply

\[
\sum_p |1+a(p)|p^{-\sigma}<\infty
\]

at every crossed exponent. Infinite alphabets may therefore contain genuine conditional first-order structure. The point is narrower: after holomorphic continuation, that structure lives in a logarithm of a zero-free factor and cannot alter the zeta divisor.

### The result does not construct a witness

For `a=lambda`, `P_a=0` and `C_a=1`, so (PL373-20) reduces to `zeta(2s)/zeta(s)`. This is the sharp control: having the cleanest possible prime defect does not make the continuation holomorphic unless the target zero-free region already holds.

More generally, proving holomorphic continuation of `P_a` for some infinite alphabet may be mathematically interesting, but by (PL373-21) it cannot by itself turn the associated completely multiplicative series into a Venturini witness without also establishing the same zeta zero-free half-plane.

### The half-plane threshold is essential to this formulation

The clean argument is stated only for `sigma_0>=1/2`. It uses both `Re(2s)>1`, so `zeta(2s)` has no interior singularity or zero, and absolute convergence of the higher-power remainder `R_a` on `Re(s)>1/2`. Nothing here claims the same divisor classification unchanged for half-planes extending left of `1/2`.

### Prior-art calibration

Venturini's theorem is the decisive prior-art input, and his proof already supplies the nonvanishing symmetrization used in Section 1. Kahane--Saïas and related work on completely multiplicative functions with sum zero provide nearby precedent for studying stability under changes of prime values. Helson-zeta constructions provide the opposite control: without complete multiplicativity plus this pole-neutral continuation structure, prime phases can exhibit much greater zero/pole programmability.

The literature audit did not locate the exact formulation (PL373-1)/(PL373-17) as a separately stated theorem. It should nevertheless be treated as an **exact derived consequence of known machinery**, not as a theorem-priority claim.

## Research consequence

`PL-372` left two broad possibilities: a finite alphabet, which it collapsed to an absolutely convergent zero-free correction of Liouville, and an infinite alphabet whose first-order deviations from `-1` might be only conditionally organized.

The second possibility no longer supplies an independent divisor mechanism. A genuine infinite-alphabet witness also has the form

\[
\frac{\zeta(2s)}{\zeta(s)}\times\text{(holomorphic zero-free gauge)},
\]

and its first-order prime defect must itself continue holomorphically through the desired half-plane.

The remaining live question is therefore not whether a clever infinite prime alphabet can cancel zeta zeros inside the Venturini class. It cannot. Any genuinely new route must explain **why the required global continuation is forced**, or leave this scalar completely-multiplicative witness class for a structure carrying additional global information such as a source-native functional equation, trace/positivity identity, or another rigidity principle not reducible to a zero-free multiplicative gauge.
