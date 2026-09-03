# MC-034 — Matched random multiplicative signs put the Huxley–Watt annulus at the critical power scale in RMS

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `NO-NOVELTY-CLAIM`.

## Claim

The matched multiplicative controls used to stress-test `MC-033` admit an exact second-moment analysis that is substantially sharper than the annular `ell^1` mass bound.

Let `(xi_p)_p` be independent Rademacher signs, and define the square-free-supported multiplicative function

\[
f_\xi(n)=
\begin{cases}
\prod_{p\mid n}\xi_p,& n\text{ square-free},\\
0,& p^2\mid n\text{ for some }p.
\end{cases}
\tag{1}
\]

For a bounded real radial kernel `K`, define the Huxley–Watt annular functional

\[
\mathcal A_{N,K}(f)
:=
\sum_{N<q\le N^2}c_{N,f}(q)K(N^2/q),
\qquad
c_{N,f}(q):=
\sum_{\substack{mn=q\\m,n\le N}}f(m)f(n).
\tag{2}
\]

Write every nonzero product fiber uniquely as `q=ab^2` with square-free coprime `a,b`. By `MC-033`,

\[
c_{N,f_\xi}(ab^2)=f_\xi(a)R_N(a,b),
\tag{3}
\]

where `R_N(a,b)` is the nonnegative central-divisor count from that finding. Therefore

\[
\mathcal A_{N,K}(f_\xi)
=
\sum_{a\ \mathrm{square\!\!-\!free}} f_\xi(a)W_{N,K}(a),
\tag{4}
\]

with the deterministic coefficient

\[
W_{N,K}(a)
:=
\sum_{\substack{b\ \mathrm{square\!\!-\!free}\\(a,b)=1\\N<ab^2\le N^2}}
R_N(a,b)K\!\left(\frac{N^2}{ab^2}\right).
\tag{5}
\]

The square-free characters `f_\xi(a)=prod_{p|a}xi_p` are exactly orthonormal under the product Rademacher measure. Hence

\[
\boxed{
\mathbb E\,\mathcal A_{N,K}=W_{N,K}(1),
\qquad
\operatorname{Var}(\mathcal A_{N,K})
=
\sum_{\substack{a>1\\a\ \mathrm{square\!\!-\!free}}}W_{N,K}(a)^2.
}
\tag{6}
\]

If `||K||_infinity<=C`, then uniformly in the choice of bounded radial kernel,

\[
\boxed{
\operatorname{Var}(\mathcal A_{N,K})
=O_C\!\left(N^2(\log N)^4\right),
\qquad
\operatorname{sd}(\mathcal A_{N,K})
=O_C\!\left(N(\log N)^2\right).
}
\tag{7}
\]

The deterministic mean satisfies `W_{N,K}(1)=O_C(N)`.

Two source-natural cases therefore have the **critical square-scale power exponent in matched-control RMS**:

1. an individual reciprocal Fourier mode, `K(x)=sin(2 pi h x)`, uniformly in `h`;
2. the full retained Huxley–Watt weighted Fourier aggregate, `K(x)=S_H(x)=sum_{h<=H} sin(2 pi h x)/(pi h)`, uniformly in `H`, because the classical partial harmonic sine sums are uniformly bounded as already used in `MC-032`.

For every fixed deterministic schedule `H=H(N)` and every `epsilon>0`, Chebyshev plus Borel–Cantelli on dyadic `N` gives, for almost every one-time choice of the prime signs,

\[
\mathcal A_{N,S_{H(N)}}(f_\xi)
=O_\varepsilon(N^{1+\varepsilon})
\tag{8}
\]

along all sufficiently large dyadic scales. No zeta zero-free region, Mertens estimate, or independence of the pair coefficients is used.

Thus the finite visualization behind `CLUE-reciprocal-phase-prime-log-slab-coupling` was sampling an ensemble whose natural second-moment scale is already RH-compatible for this **annular Fourier functional**, even though `MC-033` proves that the same annulus has absolute coefficient mass asymptotic to a constant times `N^2`.

The unresolved arithmetic problem is correspondingly sharper. Actual Möbius is the single deterministic prime-sign assignment `xi_p=-1` for every prime, so

\[
\mu(a)=(-1)^{\omega(a)}=f_{-1}(a)
\quad(a\ \mathrm{square\!\!-\!free}).
\tag{9}
\]

The matched-control variance does not bound that deterministic Walsh-cube point. A useful continuation must control the correlation of the parity character with the deterministic weight vector `W_{N,K}`. Equivalently, after subtracting the `a=1` term and writing

\[
\sigma_{N,K}^2:=\sum_{a>1}W_{N,K}(a)^2,
\tag{10}
\]

the exact normalized diagnostic

\[
Z_{N,K}
:=
\frac{\sum_{a>1}(-1)^{\omega(a)}W_{N,K}(a)}{\sigma_{N,K}}
\tag{11}
\]

has mean zero and variance one under the matched random multiplicative ensemble, while the Möbius value is one distinguished deterministic evaluation. Since `sigma_{N,K}=O(N log^2 N)`, any deterministic theorem giving `Z_{N,K}=N^{o(1)}` for the source-prescribed kernel would already place this annular functional at the required `N^{1+epsilon}` power scale.

This does **not** prove such a theorem for Möbius. It identifies an exact information budget and removes Monte Carlo control bands as the primary normalization problem.

## 1. Product-fiber reduction leaves one random character per square-free kernel

For the controls (1), `f_\xi(b)^2=1` whenever `b` is square-free. The product-fiber calculation of `MC-033` therefore gives (3) exactly: all admissible representations with the same `q=ab^2` carry the common random sign `f_\xi(a)` and the same radial kernel value.

Grouping first by `a` yields (4)–(5). This is the decisive simplification. Randomness does not live on the ordered pairs `(m,n)` or on the individual divisor representations inside one product fiber; it lives only on the square-free kernel characters `f_\xi(a)`.

For square-free `a,a'`,

\[
\mathbb E[f_\xi(a)f_\xi(a')]
=
\mathbb E\prod_{p\mid aa'}\xi_p^{v_p(a)+v_p(a')}
=
\mathbf 1_{a=a'}.
\tag{12}
\]

Indeed, if `a!=a'`, their symmetric difference contains a prime that appears to the first power in the product and has zero expectation. Equation (6) follows immediately from (4) and (12), with `a=1` supplying the deterministic mean.

This orthogonality is stronger than assigning independent signs to product fibers: the variables `f_\xi(a)` satisfy many multiplicative relations, but their **second moments are still exactly orthogonal** on the square-free Walsh basis. The variance formula therefore respects the same multiplicativity that the visual controls were designed to preserve.

## 2. The control variance is only `N^2 polylog(N)`

For fixed square-free `a`, the number of admissible `b` in (5) is at most `N/sqrt(a)`. Also

\[
0\le R_N(a,b)\le \tau(a)=2^{\omega(a)}.
\tag{13}
\]

Therefore, for `||K||_infinity<=C`,

\[
|W_{N,K}(a)|
\le
C\frac{N}{\sqrt a}2^{\omega(a)}.
\tag{14}
\]

Squaring and summing gives

\[
\sum_{a>1}W_{N,K}(a)^2
\le
C^2N^2
\sum_{\substack{a\le N^2\\a\ \mathrm{square\!\!-\!free}}}
\frac{4^{\omega(a)}}{a}.
\tag{15}
\]

The last sum has a completely elementary Euler-product upper bound:

\[
\begin{aligned}
\sum_{\substack{a\le X\\a\ \mathrm{square\!\!-\!free}}}
\frac{4^{\omega(a)}}{a}
&\le
\prod_{p\le X}\left(1+\frac4p\right)\\
&\le
\exp\!\left(4\sum_{p\le X}\frac1p\right)
=O((\log X)^4).
\end{aligned}
\tag{16}
\]

The final step is the classical reciprocal-prime estimate already anchored as `MC-S6`. Taking `X=N^2` proves (7).

For `a=1`, one has `R_N(1,b)<=1` and at most `N` admissible values of `b`, so `|W_{N,K}(1)|=O_C(N)`.

The logarithmic exponent in (7) is only a convenient robust upper bound. No claim is made that it is sharp. The structural point is the power of `N`: multiplicative-sign orthogonality collapses an annulus with `ell^1` mass of order `N^2` to an RMS scale `N^{1+o(1)}`.

## 3. The full Huxley–Watt retained Fourier aggregate fits the same bound

For an individual mode take

\[
K_h(x)=\sin(2\pi h x),
\tag{17}
\]

so `||K_h||_infinity<=1` uniformly in `h`.

For the weighted truncated Fourier aggregate of `MC-032`, take

\[
K_H(x)=S_H(x)
=
\sum_{h=1}^H\frac{\sin(2\pi h x)}{\pi h}.
\tag{18}
\]

The classical partial sums `S_H` are uniformly bounded in both `H` and `x`; this is exactly the bound used in `MC-032` to make the low-product interior cheap. Therefore (7) applies to the **joint signed `h`-aggregate before taking absolute values**, uniformly for every source-allowed truncation parameter `H`.

This is important relative to `MC-031`. That finding showed that termwise triangle-inequality control of the retained modes still requires a nearly full power gain in each `Q_h`. The random-control calculation here shows that joint cancellation at the prime-kernel sign level can instead put the already-combined bounded sawtooth kernel at the target power scale without proving smallness of every individual coefficient separately.

## 4. Dyadic almost-sure consequence for the matched ensemble

Fix any deterministic schedule `H(N)` in the source-allowed range. From (6)–(7) and Chebyshev,

\[
\mathbb P\left(
|\mathcal A_{N,S_{H(N)}}-W_{N,S_{H(N)}}(1)|
>N^{1+\varepsilon}
\right)
\ll
\frac{(\log N)^4}{N^{2\varepsilon}}.
\tag{19}
\]

On `N=2^j` the right-hand side is summable in `j`. The first Borel–Cantelli lemma requires no independence between the events, so for almost every fixed random multiplicative function `f_\xi`, only finitely many dyadic scales violate the threshold. The deterministic mean is `O(N)` and may be absorbed into `N^{1+epsilon}`. This proves (8).

Equation (8) is deliberately limited to a predetermined truncation schedule and dyadic scales. Uniformity over all `H` or all integer `N` would require an additional maximal argument and is not claimed.

## 5. Matched-control interpretation and the surviving deterministic target

The visual controls associated with `MC-033` preserve square-free support, multiplicativity, the rational prime locations, and exact product-fiber sign coherence. Equations (6)–(8) show that these controls are not merely a finite plotting device: for the annular Huxley–Watt Fourier statistic their second-moment information budget already has the critical power exponent.

This has two consequences.

First, the annular absolute-mass obstruction of `MC-033` is not a probabilistic obstruction. Large `ell^1` mass can coexist with `N^{1+o(1)}` RMS once the **cross-kernel prime-sign organization** is used. The product-fiber no-go remains valid, but the matched random ensemble demonstrates an explicit route by which cross-fiber cancellation can be strong enough in power.

Second, random multiplicative behavior is not evidence for deterministic Möbius. The assignment `xi_p=-1` is highly special and has probability zero in the infinite product model. Other deterministic square-free-supported multiplicative sign systems can have very different summatory behavior, as the line's earlier matched controls already emphasize. Equation (7) therefore supplies a normalization and a falsification scale, not a proof transfer.

The clean deterministic question is (11): does the parity point have only subpolynomial correlation with the source-prescribed weight vector, or can the Huxley–Watt occupancy/phase weights align with `(-1)^{omega(a)}` much more strongly than a typical prime-sign assignment?

A finite experiment can now test this without arbitrary radial bins or Monte Carlo percentile bands by computing the exact `W_{N,K}(a)`, its exact variance norm `sigma_{N,K}`, and the Möbius z-score `Z_{N,K}`. Such a computation remains finite evidence only; a durable positive result would require an analytic bound on the deterministic parity correlation.

## 6. Prior art and novelty assessment

The Huxley–Watt sawtooth kernel, its Fourier truncation, and the source residual are from Huxley and Watt (`MC-S24`). The reciprocal-prime estimate used in (16) is classical and already anchored as `MC-S6`. The square-free product-fiber normal form and central-divisor weight `R_N(a,b)` are the exact line-specific structure persisted in `MC-033`, with Letendre's one-sided truncated Möbius divisor sum (`MC-S25`) recorded as adjacent prior art.

Random multiplicative functions generated by independent prime signs and orthogonality of the resulting square-free Walsh characters are classical mechanisms. No novelty is claimed for that probability model, for Rademacher orthogonality, for Chebyshev/Borel–Cantelli, or for the Euler-product estimate (16).

The durable contribution is their exact specialization to the **current Huxley–Watt annular frontier**: after the product-fiber sign-coherence obstruction, the same matched multiplicative control family used experimentally has an explicit deterministic weight decomposition and a critical-power second-moment bound for every bounded radial kernel, including the full retained Fourier aggregate. This converts the visual control into a precise information-budget benchmark and exposes the remaining Möbius-specific obligation as one deterministic Walsh correlation rather than an undefined notion of phase/slab anomaly.

## 7. Boundaries and falsification tests

This finding does **not** prove any new bound for the Möbius annular functional. In particular, second-moment control over random prime signs cannot be transferred to the deterministic all-minus assignment.

It does not prove that the `O(N log^2 N)` RMS bound is sharp, that the standardized control distribution is Gaussian, or that one finite Möbius z-score has asymptotic meaning. Higher moments contain multiplicative relations between the characters and need not match an independent Gaussian model.

The exact identities and bounds can be falsified directly:

1. for a finite prime-sign ensemble, direct evaluation of the annular functional must agree with (4) using the grouped weights (5);
2. exact averaging over all sign assignments on the finitely many active primes must give mean `W(1)` and variance `sum_{a>1}W(a)^2`;
3. the deterministic bound (14) must hold for every square-free `a`;
4. the Euler-product estimate (16) must dominate the finite coefficient norm;
5. replacing `K` by either an individual sine mode or the bounded partial sawtooth sum must preserve the uniform power bound.

A counterexample to any of these statements invalidates the finding. A computation showing that the actual Möbius `Z_{N,K}` is typical or atypical at finite scales would not invalidate (6)–(8); it would only guide the next deterministic question.

## Consequence for the research line

`MC-033` removed factor-fiber cancellation and left only cross-kernel arithmetic/phase organization. The accepted reciprocal-phase slab clue then identified the scalar occupancy `R_N(a,b)` as the only subset-sum information actually retained by the mode. The present result supplies the first exact quantitative benchmark for that surviving carrier.

The matched multiplicative controls already cancel at the correct **power** scale in RMS, uniformly for the bounded source Fourier aggregate. Therefore the next useful question is no longer whether random-like prime-kernel signs *could* in principle overcome the `N^2` annular mass—they can. It is whether the deterministic Möbius parity assignment can be controlled against the specific Huxley–Watt occupancy/phase weight vector by information independently weaker than the target Mertens bound.

The exact z-score (11) also freezes a bounded computational diagnostic if numerical triage is desired. The only mathematically decisive continuation, however, is an analytic estimate or obstruction for that deterministic parity correlation.