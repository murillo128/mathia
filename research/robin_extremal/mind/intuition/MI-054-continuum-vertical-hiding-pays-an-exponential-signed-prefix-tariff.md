# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff with a sharp positive-window unit rate

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-213](../../findings/RE-213-adaptive-kaiser-tests-close-the-separated-vertical-endpoint-at-unit-rate.md). The compact-support Fourier/spectral-gap geometry is classical; the Mathia content is its exact pullback to separated ordinary-prime Euler repairs at selector scale under KV source fidelity.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs only when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then uncertainty is no longer a rank question: the gap forces an exponentially large weighted cumulative primitive.

RE-209 identifies the physical primitive after pulling the generic harmonic statement back to ordinary primes. The exponentially weighted primitive is exactly a signed prime-count prefix, and partial summation converts it into a Chebyshev-prefix excursion. Thus the continuum observation width is priced in a source currency that fixed Korobov--Vinogradov fidelity constrains.

RE-210 sharpens the repeated-uniform test to the optimized sinc-tail rate `gamma_*=0.5979019108...`; RE-211 improves this with a Blackman window; RE-212 uses continuous Kaiser--Bessel windows to approach unit exponential rate. RE-213 makes that limit uniform when the Kaiser parameter grows with the asymptotic scale. Writing `A=HT`, the adaptive choice `beta=sqrt(A log A)` yields

`log R >= A-O(sqrt(A log A))`.

For the ordinary-prime separated repair with `T_Q=O(log Q)`, the loss is `o(V(Q))`, `V(Q)=(log Q)^(3/5)/(log log Q)^(1/5)`. Therefore preserving every fixed KV envelope requires

`((1/2)log Q-H T_Q)/V(Q) -> +infinity`.

In particular, if `T_Q=c log Q` with fixed `c`, then necessarily

`c<1/(2H)`.

The endpoint is now excluded. At `H=log 8`, no separated ordinary-prime `{0,1,2}` repair of this kind can hide the selector-scale packet for `c>=0.2404491734...`, while explicit hiding remains constructed only below `0.0289079...`.

RE-213 also closes the window-design problem itself. For any nonnegative probability density `w` supported on `[-1,1]`, if `M(a)=sup_(|x|>=a)|w_hat(x)|`, then the Chebyshev/Remez limiting argument gives

`M(a)>=sech(a)`.

Hence

`Gamma(w)=sup_a[-log M(a)]/a <= 1`,

and the Kaiser construction from RE-212 shows `sup_w Gamma(w)=1`. The unit coefficient is the exact supremal exponential rate available to **positive compact-window tests**.

The reusable distinction is therefore between **local spectral rank, global continuum source cost, and proof-representation optimality**. Finite panels ask whether source vectors are distinguishable at sampled phases. A continuum interval plus support separation asks how much signed prefix must be generated to approximate an entire Fourier profile. RE-213 additionally shows that optimizing the positive compact test cannot raise the exponential coefficient beyond one; any stronger converse must use a genuinely different mechanism.

The remaining constructive/coercive gap is already in the correct source currency. On the constructive side, a better repair must control signed weighted prefixes more efficiently than the current absolute-variation/KV realization. On the obstruction side, progress past the unit-rate boundary must leave the positive compact-window method rather than merely shape a better window.

**Boundary.** The coercive theorem assumes a fixed pre-repair logarithmic gap, ordinary-prime edits with the stated integer multiplicities, selector-scale local mass and fidelity to every fixed KV envelope. `sup_w Gamma(w)=1` is a method boundary for nonnegative compact windows, not a universal upper bound on every possible coercive argument. The result does not prove Robin, eliminate repairs without a fixed separation gap, close the constructive/coercive constant gap, or show that a hypothetical Robin counterexample necessarily supplies the required continuum vertical observation.