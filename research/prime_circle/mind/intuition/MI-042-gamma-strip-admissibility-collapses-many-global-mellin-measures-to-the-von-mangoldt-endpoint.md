# MI-042 — Gamma-strip admissibility collapses many global Mellin selectors to the von Mangoldt endpoint

**Evidence level:** exact synthesis from [PC-335](../../findings/PC-335-bounded-indefinite-mellin-symbols-cannot-separate-prime-powers.md) through [PC-341](../../findings/PC-341-prime-log-uniqueness-extends-to-bounded-characteristic-on-gamma-strip.md). The Fourier--Laplace, Blaschke, finite-order distribution and Nevanlinna-class mechanisms are classical; the Mathia content is their interaction with the prime-circle shell factorization and semiprime-null constraints.

PC-338 classified compactly supported distributions in Mellin frequency, and PC-339 showed that compact support was not essential for finite global measures. The native `Gamma` factor supplies a horizontal strip of half-width `pi/2`; semiprime nulls turn every prime logarithm into a zero. PC-340 then showed that finite distributional order is not an escape either: fixed polynomial growth can be absorbed by a zero-free strip factor without reducing the available strip, so the same uniqueness argument survives.

PC-341 identifies the sharper boundary: **polynomial growth is not load-bearing; bounded characteristic on the native strip is enough**. Let `S_a={z:|Im z|<a}` and map it conformally to the disk by

`phi_a(z)=tanh(pi z/(4a))`.

For a prime `p`,

`1-|phi_a(log p)| = 2/(p^(pi/(2a))+1)`.

Thus the prime-log image fails the Blaschke condition exactly when `a>=pi/2`. Every nonzero Nevanlinna-class / bounded-characteristic function has a Blaschke zero set, so on the full Gamma strip `S_(pi/2)` a bounded-characteristic interpolation function vanishing at all but finitely many prime logarithms must vanish identically.

Applied to the Prime-Circle shell factorization, this leaves the PC-339 classification unchanged under a much larger analytic class. If the semiprime interpolation functions `F_2,F_3` are in `N(S_(pi/2))`, exact mixed-semiprime nulls force them to vanish. Off the endpoint line `sigma!=1`, the visible shell response is zero on every `n>1`; on `sigma=1`, the selector itself is `T=c delta_0`, hence `L_T(n)=c Lambda(n)`.

Bounded characteristic is genuinely broader than bounded or polynomial strip growth. The remaining scalar loophole on the full strip is therefore not “faster finite-order growth” but **leaving the Nevanlinna class itself**. Conversely, the width is sharp at the zero-set level: for every `a<pi/2`, the prime-log points satisfy the Blaschke condition and their disk Blaschke product pulls back to a nonzero bounded function in `H^infty(S_a)` vanishing at every prime logarithm.

The reusable boundary is two-dimensional: analytic **class** and analytic **domain width** must be kept separate. On the full Gamma strip, bounded characteristic is already too rigid. On a narrower strip, even bounded holomorphic functions can carry all prime-log zeros, so the zero locations alone no longer imply collapse. A proposed scalar Mellin escape must therefore either produce a full-strip interpolation function outside bounded characteristic, or explain which additional source-forced constraints supplement the prime-log zero set after the strip narrows.

Shell-dependent symbols/order, nonlinear or matrix-valued operations and genuinely cross-shell coupling before scalar evaluation remain outside this scalar classification. But escaping the representation class is only an admission condition: any survivor still needs an independent zero-sensitive destination theorem.

**Boundary.** PC-341 does not classify arbitrary analytic functionals outside bounded characteristic, nor does it show that a narrower-strip construction with extra source constraints must survive. The `pi/2` threshold is exact for uniqueness from the prime-log zero set inside bounded characteristic. The endpoint von Mangoldt channel still does not constrain the Riemann zero divisor by itself.