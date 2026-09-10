# FD-035 — square-divisor renormalization alone does not force a pointwise linear-prefix gap

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ABSTRACT-CONTROL + SCHUR-PROJECTIVE-DEFECT + SQUARE-DIVISOR-RENORMALIZATION + POINTWISE-ESCAPE-BOUNDARY`.

`FD-034` proves a genuine normalized obstruction for every prime-square scale. For fixed Schur-head dimension `D`, its physical energy and projective defect satisfy

\[
\varepsilon_{H,D}E_{H,D}
\ge
(1-p^{-2})E_{\lfloor H/p^2\rfloor,D}
\tag{1}
\]

for every prime `p` with `floor(H/p^2)>D`. Together with the quadratic upper bound for `E`, this forces a positive geometric/Cesaro defect along each complete `4`-adic chain. The current question is whether using **all** prime-square instances of (1), rather than only `p=2`, can by itself upgrade that average obstruction to a pointwise or cofinal one.

It cannot. There is an explicit abstract energy/defect profile satisfying the complete family (1) at every horizon, satisfying even the two known coarse size properties of the physical energy,

\[
\frac{E_H}{H}\longrightarrow\infty,
\qquad
E_H\ll H^2,
\tag{2}
\]

and satisfying monotonicity, yet having an unbounded sequence of horizons on which the normalized defect tends to zero. Therefore **the separate square-divisor renormalization inequalities plus the currently available energy-size information do not logically imply a uniform pointwise gap or exclude a cofinal saturation subsequence.**

This is a limitation of that proof input, not a synthetic Mertens counterexample. The constructed profile is not asserted to come from the quotient-shell transform `mathcal H` of `FD-033`, from a Farey sequence, or from any admissible Mobius source. A successful pointwise argument must use additional structure that this control deliberately omits: for example overlap between several nonsquarefree row families before separate lower bounding, a new cross-scale regularity law for the physical energy, the exact longitudinal coordinate of `FD-034`, endpoint reachability from `FD-031`, or another identity specific to the actual Mertens tail.

## 1. Abstract the exact information supplied by the square-divisor bounds

Fix an integer `D>=1`. Consider positive numbers `F_H` and numbers `eta_H in [0,1]` for integer `H>D`. Retain exactly the renormalization constraints

\[
\boxed{
\eta_H F_H
\ge
(1-p^{-2})F_{\lfloor H/p^2\rfloor}
}
\tag{3}
\]

for every prime `p` for which `floor(H/p^2)>D`.

For the physical quantities of `FD-034`, one has `F_H=E_{H,D}` and `eta_H=epsilon_{H,D}`. The same finding gives

\[
E_{H,D}\le \zeta(2)^3H^2,
\tag{4}
\]

while `FD-033` proves for fixed `D` that

\[
\frac{E_{H,D}}H\to\infty.
\tag{5}
\]

Thus any proposed deduction that uses only (3), (4), (5), positivity, and `0<=eta<=1` must remain valid for every abstract profile obeying the same information. We now construct one for which `eta` has cofinally vanishing spikes.

## 2. A monotone superlinear energy profile with sparse quadratic jumps

Choose integers

\[
D<N_1<N_2<\cdots,
\qquad
N_{k+1}\ge N_k^4.
\tag{6}
\]

For `H>=1` put

\[
B_H:=H\log(eH),
\tag{7}
\]

and define the sparse-jump envelope

\[
S_H:=
\max\bigl(\{N_k^2:N_k\le H\}\cup\{0\}\bigr).
\tag{8}
\]

Set

\[
\boxed{F_H:=\max(B_H,S_H).}
\tag{9}
\]

Both `B_H` and `S_H` are nondecreasing, hence so is `F_H`. Moreover `log(eH)<=H` for every integer `H>=1`, and every `N_k` contributing to `S_H` satisfies `N_k<=H`. Therefore

\[
\boxed{
H\log(eH)\le F_H\le H^2.
}
\tag{10}
\]

In particular

\[
\frac{F_H}{H}\ge\log(eH)\to\infty,
\tag{11}
\]

so this abstract profile obeys a stronger quadratic upper bound than (4) and the same qualitative superlinear lower growth as (5). At every selected horizon,

\[
\boxed{F_{N_k}=N_k^2.}
\tag{12}
\]

The only artificial feature is the sparse upward jump from the superlinear baseline to the allowed quadratic ceiling.

## 3. The complete prime-square recurrence still permits vanishing defect at the jumps

For every `H>D`, define

\[
\eta_H
:=
\max_{\substack{p\ {m prime}\\\lfloor H/p^2\rfloor>D}}
(1-p^{-2})\frac{F_{\lfloor H/p^2\rfloor}}{F_H},
\tag{13}
\]

with `eta_H=0` when the set of eligible primes is empty. By construction, every inequality (3) holds.

Because `F` is nondecreasing and `floor(H/p^2)<H`, every ratio in (13) is at most one. Hence

\[
0\le\eta_H<1,
\tag{14}
\]

so the control also respects the exact range of a normalized squared projective residual.

Now evaluate (13) at `H=N_k`, with `k>=2`. For every eligible prime `p`,

\[
x:=\left\lfloor\frac{N_k}{p^2}\right\rfloor
\le\frac{N_k}{p^2}<N_k.
\tag{15}
\]

No current jump contributes below `N_k`, so

\[
S_x\le N_{k-1}^2.
\tag{16}
\]

Using `F_x=max(B_x,S_x)<=B_x+S_x`, equations (7), (15), and (16) give

\[
F_x
\le
\frac{N_k}{p^2}\log(eN_k)+N_{k-1}^2.
\tag{17}
\]

Together with `F_(N_k)=N_k^2`, this yields

\[
\eta_{N_k}
\le
\max_{p\ge2}
\left[
\frac{1-p^{-2}}{p^2}
\frac{\log(eN_k)}{N_k}
+
(1-p^{-2})\frac{N_{k-1}^2}{N_k^2}
\right].
\tag{18}
\]

For primes `p>=2`, the function `(1-p^(-2))/p^2` is maximized at `p=2`, with value `3/16`, while `1-p^(-2)<1`. Hence

\[
\boxed{
\eta_{N_k}
\le
\frac3{16}\frac{\log(eN_k)}{N_k}
+
\frac{N_{k-1}^2}{N_k^2}.
}
\tag{19}
\]

The growth condition (6) makes the second term at most `N_(k-1)^(-6)`, and the first term also tends to zero. Therefore

\[
\boxed{
\eta_{N_k}\longrightarrow0.
}
\tag{20}
\]

This is compatible with **every prime-square inequality at every horizon**, not merely with a finite selection of primes. Iterating (3) along any fixed multiplicative chain remains valid automatically; after a jump, monotonicity keeps enough energy above it for all later one-step constraints. The price is exactly what `FD-034` already permits: the resulting defects away from the selected jump horizons must compensate, so the four-adic Cesaro lower bound is not contradicted.

## 4. Why this does not contradict the four-adic average gap

At a selected `N_k`, the denominator `F_(N_k)=N_k^2` is near the allowed quadratic ceiling while every proper prime-square ancestor lies below the jump and has size at most the superlinear baseline plus the previous plateau. Equation (3) is one-sided, so each ratio can be simultaneously tiny.

Immediately above such a jump, however, the nondecreasing plateau `S_H>=N_k^2` persists until the baseline catches it. On a fixed square-multiplicative chain this forces large enough later ratios to pay back the isolated small value. This is precisely consistent with the product estimate in `FD-034`: that estimate controls the **average logarithmic defect along a complete chain**, but it never forbids isolated horizons at which current energy is much larger than all relevant lower-scale energies.

The construction therefore isolates the missing datum. To promote the four-adic result to a pointwise theorem, one needs a property preventing these projectively cheap energy jumps for the **actual** quotient-shell energy, or a residual estimate that couples several square-divisor families before their overlap is discarded. Merely adding more instances of the same one-sided inequality (3), even for every prime, cannot supply that datum.

## 5. Consequence for the linear-prime-prefix frontier

For fixed `D`, `FD-031` and `FD-034` give

\[
\widehat R_{H,D}
=C_H-\Delta_{H,D}\varepsilon_{H,D},
\qquad
C_H\to Z:=\zeta(2),
\qquad
\Delta_{H,D}\to Z-C_D>0.
\tag{21}
\]

Thus a pointwise lower bound `epsilon_(H,D)>=c_D>0` would yield a uniform linear-prefix saturation gap. `FD-035` shows that such a lower bound **cannot be deduced from the square-divisor renormalization family and the known coarse energy growth alone**. In the abstract consequence space of those inputs, (20) leaves an unbounded subsequence compatible with arbitrarily small projective loss.

This does not weaken `FD-034`. Its Cesaro and density statements remain exact and are stronger than any one-scale estimate. What changes is the next research target: extending from `p=2` to more separate prime-square inequalities is not, by itself, a route to the desired pointwise upgrade. A successful continuation must exploit a relation that the abstract pair `(F,eta)` cannot imitate.

Promising mathematically distinct possibilities include an inclusion-exclusion or orthogonal decomposition of the **union** of several nonsquarefree Jordan-row families before separate lower bounds are taken, an exact regularity constraint on `E_(H,D)` inherited from `mathcal H`, or coupling the tail defect to the longitudinal/endpoint conditions already isolated in `FD-031` and `FD-034`. These are directions, not claims established here.

## 6. Prior-art and falsification boundary

The construction is an internal implication-separation argument. A targeted literature check around Farey discrepancy/Mertens recurrences and GCD-matrix/Jordan-totient formulations found classical and modern work on Farey discrepancy, rank recurrences, and GCD matrices, but no external theorem is needed for (6)--(20). No novelty is claimed for sparse spike countermodels or monotone envelope constructions in isolation, and absence of an exact match in that search is not evidence of literature novelty.

The durable Mathia-specific content is narrower: it identifies exactly which currently persisted inputs from `FD-033`--`FD-034` are insufficient to close the live projective escape. `SOURCES.md` therefore needs no new load-bearing anchor.

The result is falsified if the abstract profile above fails any displayed constraint it claims to model. It is **not** falsified by discovering additional identities of the physical Mertens energy that the profile does not satisfy; such an identity would instead provide precisely the extra structure that this obstruction says is necessary. Conversely, the present control cannot be cited as evidence that the true `epsilon_(H,D)` ever becomes small, that a linear-prefix relaxation actually saturates on a subsequence, or that RH is true or false.
