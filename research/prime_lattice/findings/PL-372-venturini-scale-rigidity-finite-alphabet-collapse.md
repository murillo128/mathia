# PL-372 — Venturini continuation forces scale-by-scale Liouville rigidity; finite prime alphabets collapse to zero-free corrections

## Claim

The continuation hypothesis in the Venturini witness class is substantially more rigid than the local `1/p` conclusion isolated in `PL-370`.

Fix `sigma_0<1`. Let `a:N->C` be bounded and completely multiplicative, and suppose

`L(a,s)=sum_(n>=1) a(n)n^(-s)`

extends holomorphically to `Re(s)>sigma_0` and satisfies `L(a,1)=0`. Then for every real `sigma>sigma_0`,

`sum_p (1+Re a(p))/p^sigma < infinity`,

and therefore

`sum_p |1+a(p)|^2/p^sigma < infinity`.

Equivalently, every genuine Venturini witness lies at finite Liouville distance in **every** power-weighted prime metric strictly inside its continuation half-plane, not only in the boundary `1/p` metric forced locally at `s=1` by `PL-370`.

There is a sharper consequence for finite prime alphabets. Assume additionally that all prime values `a(p)` lie in a fixed finite set `S` contained in the closed unit disk. Then `-1` must belong to `S`, and if

`E={p:a(p)!=-1}`,

one has

`sum_(p in E) p^(-sigma) < infinity`

for every `sigma>sigma_0`. Hence the relative Euler correction

`C_a(s)=product_(p in E) (1+p^(-s))/(1-a(p)p^(-s))`

converges normally and is holomorphic and zero-free on `Re(s)>sigma_0`. In that half-plane the meromorphic continuation satisfies

`L(a,s) = [zeta(2s)/zeta(s)] C_a(s)`.

For `1/2<=sigma_0<1`, `zeta(2s)` is holomorphic and nonzero throughout `Re(s)>sigma_0`. Consequently a finite-alphabet Venturini witness has **exactly the same zero/pole obstruction as the Liouville quotient**: the correction `C_a` cannot cancel or move any zero of `zeta(s)`.

In particular, at `sigma_0=1/2`, every finite-alphabet witness is analytically just the Liouville witness multiplied by a holomorphic zero-free factor. This is a decisive restriction of the source-forced filter route after `PL-369`--`PL-371`: a finite prime alphabet cannot provide an independent continuation mechanism or alter the RH-sensitive divisor.

**Evidence/status:** `VENTURINI-2020 + EXACT-DERIVED-LANDAU + PRIOR-ART-CALIBRATED + DECISIVE-NARROWING`.

No theorem-priority claim is made. The scale-by-scale conclusion is extracted from Venturini's nonvanishing mechanism plus the classical Landau theorem for Dirichlet series with nonnegative coefficients. The finite-alphabet factorization is then elementary Euler-product comparison in a region where the relative product itself converges normally.

## 1. Venturini's positive logarithm extends with the witness

Define the reflected Dirichlet series

`L^sharp(a,s)=overline(L(a,overline(s)))`.

It is holomorphic wherever `L(a,s)` is holomorphic, and on `Re(s)>1` it has coefficients `overline(a(n))`. Since `L(a,1)=0`, both `L(a,s)` and `L^sharp(a,s)` vanish at `1`. Therefore

`F(s)=zeta(s)^2 L(a,s)L^sharp(a,s)`

has a removable singularity at `s=1` and is holomorphic on `Re(s)>sigma_0`.

For `Re(s)>1`, complete multiplicativity gives the absolutely convergent exponential representation used by Venturini:

`F(s)=exp G(s)`,

where

`G(s)=2 sum_(n>=2) (1+Re a(n)) Lambda(n)/(n^s log n)`.

Every coefficient of this Dirichlet series is nonnegative because `|a(n)|<=1`.

Venturini's nonvanishing principle says more than merely `F(s)!=0`: because `G` is completely monotone on the real interval `(1,infinity)` and `exp G=F` extends holomorphically to `Re(s)>sigma_0`, the function `G` itself extends holomorphically to the same half-plane. This is exactly the continuation step behind his proof that a pole-neutral completely multiplicative witness forces a zeta zero-free region.

The important point for the present finding is that `G` is still the analytic continuation of a Dirichlet series with **nonnegative coefficients**.

## 2. Landau converts analytic continuation into scale-by-scale prime rigidity

Let `sigma_c(G)` be the abscissa of convergence of the nonnegative-coefficient Dirichlet series defining `G`. Classically, Landau's theorem implies that if `sigma_c(G)` is finite, the real point `s=sigma_c(G)` is a singularity of the represented function.

But Venturini's continuation makes `G` holomorphic at every real point larger than `sigma_0`. Therefore

`sigma_c(G)<=sigma_0`.

Hence for every real `sigma>sigma_0`,

`sum_(n>=2) (1+Re a(n)) Lambda(n)/(n^sigma log n) < infinity`.

Keeping only the prime terms `n=p` gives

`sum_p (1+Re a(p))/p^sigma < infinity`.

Since `|a(p)|<=1`,

`|1+a(p)|^2 = 1+|a(p)|^2+2 Re a(p) <= 2(1+Re a(p))`,

so also

`sum_p |1+a(p)|^2/p^sigma < infinity`.

Thus the `PL-370` metric constraint at exponent `1` was only the boundary shadow of a stronger half-plane statement: if the witness reaches `Re(s)>sigma_0`, then it is Liouville-close at every radial exponent strictly larger than `sigma_0`.

In the notation of the power-sensitive pretentious geometry audited in `PL-138`, this says

`D_sigma(a,lambda)<infinity`

for every `sigma>sigma_0`. The direction is important: here the family of weighted distances is **forced by the assumed analytic continuation**. It does not produce that continuation.

## 3. Finite alphabets turn quadratic closeness into sparse support

Assume now that `a(p)` belongs to a fixed finite set `S` in the closed unit disk. If `-1` were not in `S`, then

`delta=min_(z in S) (1+Re z)>0`.

The scale-by-scale estimate would then imply

`delta sum_p p^(-sigma)<infinity`

for every `sigma>sigma_0`. Taking any `sigma` with `sigma_0<sigma<=1` gives a contradiction. Hence `-1 in S`.

For the exceptional set

`E={p:a(p)!=-1}`,

the finite alphabet gives a positive gap

`delta_S=min_(z in S\{-1}) (1+Re z)>0`.

Therefore, for every `sigma>sigma_0`,

`delta_S sum_(p in E) p^(-sigma)
 <= sum_p (1+Re a(p))/p^sigma
 < infinity`.

So the prime Dirichlet series of `E` has abscissa of convergence at most `sigma_0`.

This is exactly the tail control that `PL-371` showed cannot be recovered from the weaker local condition `sum_(p in E)1/p<infinity`. Its counterexample chooses `E_alpha` with a larger abscissa `alpha>sigma_0`; the present argument shows that such an `E_alpha` is automatically excluded as soon as true Venturini continuation to `Re(s)>sigma_0` is imposed.

## 4. The finite-alphabet correction is holomorphic and zero-free

On `Re(s)>1`, ordinary absolute convergence gives

`L(a,s)=product_p (1-a(p)p^(-s))^(-1)`

and

`L(lambda,s)=product_p (1+p^(-s))^(-1)=zeta(2s)/zeta(s)`.

The local factors agree whenever `a(p)=-1`. Thus

`L(a,s)=[zeta(2s)/zeta(s)] C_a(s)`

with

`C_a(s)=product_(p in E) (1+p^(-s))/(1-a(p)p^(-s))`.

Fix a compact set `K` in `Re(s)>sigma_0`, and choose `sigma_1>sigma_0` below the real parts of all points in `K`. From the previous section,

`sum_(p in E) p^(-sigma_1)<infinity`.

Uniformly on `K`, the logarithm of each relative Euler factor is

`log[(1+p^(-s))/(1-a(p)p^(-s))]
 = (1+a(p))p^(-s)+O(p^(-2 sigma_1))`,

with a uniform constant because `|a(p)|<=1`. Both the first-order sum over `E` and the quadratic remainder converge absolutely. Hence the product for `C_a` converges normally on `K`.

Every local numerator and denominator is nonzero for `Re(s)>0`, so `C_a` is holomorphic and zero-free on `Re(s)>sigma_0`.

The displayed factorization was derived only in `Re(s)>1`. Its use farther left is legitimate because `C_a` has now been constructed independently by a normally convergent relative product and `zeta(2s)/zeta(s)` has its classical meromorphic continuation. The identity theorem therefore extends the equality meromorphically to `Re(s)>sigma_0`; no Euler product for ordinary zeta is being formally continued through `Re(s)=1`.

## 5. Finite-alphabet witnesses cannot modify the zeta divisor

Assume `1/2<=sigma_0<1`. In the open half-plane `Re(s)>sigma_0`, one has `Re(2s)>1`, so `zeta(2s)` is holomorphic and nonzero. The correction `C_a(s)` is also holomorphic and zero-free there. Thus all possible poles of

`[zeta(2s)/zeta(s)] C_a(s)`

come exactly from zeros of `zeta(s)`.

Consequently

`L(a,s) holomorphic on Re(s)>sigma_0`

if and only if

`zeta(s)!=0 on Re(s)>sigma_0`,

provided the finite-alphabet prime assignment has exceptional set `E` with prime-Dirichlet abscissa at most `sigma_0`.

The converse direction is equally explicit. Start from any finite alphabet `S` containing `-1`, choose prime values with

`sum_(p in E) p^(-sigma)<infinity`

for every `sigma>sigma_0`, and extend completely multiplicatively. Then `C_a` is holomorphic and zero-free in the required half-plane. If zeta is zero-free there, the factorization supplies a holomorphic continuation of `L(a,s)`. Since `sigma_0<1`, the same tail condition gives `sum_(p in E)1/p<infinity`, so `C_a(1)` is finite and nonzero; the simple zero of `zeta(2s)/zeta(s)` at `1` then gives `L(a,1)=0` automatically.

At the RH boundary `sigma_0=1/2`, the entire finite-alphabet witness problem therefore collapses to the canonical Liouville divisor:

`L(a,s) = zero-free factor * zeta(2s)/zeta(s)`.

Such witnesses may change amplitudes and local prime phases, but they cannot create an independent mechanism that localizes the zeta zeros.

## 6. Prior-art and novelty audit

The load-bearing theorem is Sergio Venturini's 2020 nonvanishing principle and its application to bounded completely multiplicative Dirichlet series. Venturini explicitly proves that holomorphic continuation plus `L(a,1)=0` forces the same half-plane to be zero-free for zeta, and he notes that the Liouville quotient supplies the converse for half-planes with boundary at or to the right of `1/2`.

The present scale-by-scale extraction uses another classical ingredient already implicit in this positive-coefficient framework: Landau's theorem says a Dirichlet series with nonnegative coefficients cannot be analytically regular at its finite abscissa of convergence. The combination forces convergence of Venturini's positive logarithmic Dirichlet series at every interior real exponent.

Two nearby literature controls were audited. Marco Aymone's 2020 work proves, for real completely multiplicative `f` with a power-saving partial-sum hypothesis and `F(1)=0`, a quantitative prime estimate of the form

`sum_(p<=x)(1+f(p)) log p << x^(1-delta+epsilon)`,

and deduces the corresponding zeta zero-free region. This is strongly consistent with scale-sensitive Liouville rigidity, but its input is a coefficient-side power-saving bound rather than Venturini's bare holomorphic-continuation hypothesis. Jung--Lemke Oliver's power-sensitive pretentious distances, already stored in `PL-138`, likewise provide a classical language for the weighted prime metrics but are relative cancellation-transfer theorems, not this continuation-to-tail implication.

Kahane--Saias also prove stability results for completely multiplicative functions of sum zero under suitably small prime modifications. Those results calibrate the idea that Liouville-like Euler corrections are classical, but they do not in the audited statements replace the half-plane argument above or furnish a new RH mechanism.

Accordingly, no novelty is claimed for weighted pretentiousness, Euler-product comparison, Landau's theorem, or Liouville stability. The durable contribution here is a line-specific closure of the frontier opened by `PL-371`: **once full Venturini continuation is present, its positivity already forces the exceptional-prime tail to be controlled on every crossed exponent scale; for finite prime alphabets this makes the witness divisor-equivalent to Liouville throughout that half-plane.**

Primary literature checked in this pass:

- Sergio Venturini, “Non vanishing of Dirichlet series of completely multiplicative functions,” *Rivista di Matematica della Università di Parma* 11(1) (2020), 153--180; arXiv:2002.08903.
- Marco Aymone, “On multiplicative functions which are small on average and zero free regions for the Riemann zeta function,” arXiv:2006.00827 (2020).
- Jean-Pierre Kahane, Eric Saïas, “Fonctions complètement multiplicatives de somme nulle,” arXiv:1507.04858 (2015).
- Junehyuk Jung, Robert J. Lemke Oliver, “Pretentiously detecting power cancellation,” *Math. Proc. Cambridge Philos. Soc.* 154(3) (2013), 481--498.

## Adversarial limits

The finite-alphabet hypothesis is essential for the divisor-collapse step as stated. For a general unit-disk-valued witness, the forced estimate

`sum_p |1+a(p)|^2/p^sigma<infinity`

is quadratic. It does not imply the absolute first-order convergence

`sum_p |1+a(p)|/p^sigma<infinity`

needed to build the relative Euler correction by the same elementary argument. Prime phases approaching `-1` through an infinite alphabet can therefore retain conditional first-order information that this finding does not eliminate.

The result also does not independently prove continuation of any critical witness. Its logical direction is deliberately diagnostic: **if** a witness already has the required half-plane continuation, then the positive logarithm forces scale-by-scale Liouville rigidity. In the finite-alphabet subclass, prescribing enough tail decay to construct the correction merely reduces the continuation problem back to zeta zero-freeness.

Nor does the argument single out `1/2` from the abstract exponent lattice. The parameter `sigma_0` remains the requested continuation boundary. The special role of `1/2` enters only when the Liouville numerator `zeta(2s)` becomes automatically regular and nonzero to the right of that boundary and the resulting zero-free statement becomes RH-equivalent.

## Consequence for the research line

`PL-371` showed that local pole neutrality permits sparse Liouville defects whose own prime Dirichlet boundary can be programmed anywhere in `(1/2,1)`. The present result supplies the converse diagnostic: a genuine Venturini continuation to `Re(s)>sigma_0` forces those defect tails to have abscissa at most `sigma_0`.

For finite prime alphabets this closes the obvious tail-control escape. Strengthening the exceptional-prime decay enough to cross the critical strip does not create a new source mechanism; it makes the witness a zero-free Euler correction of `zeta(2s)/zeta(s)` and therefore leaves the zeta divisor unchanged.

A surviving source-forced route must therefore exploit structure absent from finite-alphabet absolute corrections. The live possibilities are narrower: an infinite-alphabet phase law with genuinely conditional first-order structure, or a separate global mechanism such as a functional equation, trace/positivity identity, or other continuation principle whose content cannot be reduced to a zero-free multiplicative correction of Liouville.