# RE-204 — Continuous vertical Euler windows remain noncoercive below the KV phase scale

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + SPECTRAL-GAP-SYNTHESIS + EXPONENTIAL-COMPLEXITY-LAW + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent findings:** RE-200, RE-203.

`RE-203` shows that any finite vertical Euler panel with `M=o(V(Q))` can be hidden by distributing the repair across several ordinary-prime shells. Its explicit caveat is a continuum of heights: finite polynomial interpolation no longer applies once the observation set is an interval. The continuum does impose a genuine new cost, but below the Korobov--Vinogradov phase-resolution scale that cost is still affordable to the same ordinary-prime source class.

Put

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\qquad
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{1}
\]

Fix a positive logarithmic repair gap `H`; for the arithmetic realization below we take `H=log 8`. Let `T_Q>=1` and `0<epsilon_Q<=1/4` satisfy

\[
\boxed{
H T_Q+\log(1/\epsilon_Q)=o(V(Q)).
}
\tag{2}
\]

Then there is a finite ordinary-prime perturbation with coefficients `c_q in {-1,+1}` such that, for

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\tag{3}
\]

one has the **uniform continuum estimate**

\[
\boxed{
\sup_{|t|\le T_Q}|D_Q(1+it)|
\le (\epsilon_Q+o(1))d_Q.
}
\tag{4}
\]

Before the first remote repair shell arrives, the local packet still carries

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q).
\tag{5}
\]

The full perturbation uses only multiplicities `{0,1,2}` relative to the ordinary-prime baseline and, for every fixed `b>0`, satisfies

\[
|\Delta\vartheta(x)|=o\!\left(xe^{-bV(x)}\right)
\tag{6}
\]

through and beyond all affected scales. In particular, choosing any `epsilon_Q -> 0` with `log(1/epsilon_Q)=o(V(Q))` shows that **an entire vertical interval of height `T_Q=o(V(Q))` can be made `o(d_Q)`-blind to a selector-scale transient**.

There is also a matching generic complexity law at fixed accuracy. If a signed or complex remote repair measure is separated from the local packet by logarithmic distance at least `H` and approximates the local first harmonic uniformly on `[-T,T]`, then its reciprocal total variation must grow like `exp(Omega(HT))`. The construction below uses `exp(O(HT+log(1/epsilon)))`. Thus the continuum costs exponentially more than a finite panel in the natural time--gap product, but that exponential remains `e^{o(V(Q))}` in the regime (2), which is still cheap for the present prime/KV source class.

## 1. A continuum spectral-gap repair has an exponential lower bound

First isolate the representation-independent Fourier geometry. Let `mu` be any finite signed or complex measure supported on

\[
[H,\infty),
\tag{7}
\]

and write

\[
\widehat\mu(t):=\int e^{-itL}\,d\mu(L),
\qquad
A:=\|\mu\|_{TV}.
\tag{8}
\]

Assume, for some `0<=epsilon<1`,

\[
\sup_{|t|\le T}|1-\widehat\mu(t)|\le\epsilon.
\tag{9}
\]

When `HT>=4`, put

\[
n:=\left\lfloor\frac{HT}{2}\right\rfloor.
\tag{10}
\]

Let `v_n` be the uniform probability density on `[-T/n,T/n]`, and let `w_n=v_n^{*n}`. Then `w_n` is a probability density supported on `[-T,T]`, while

\[
\widehat w_n(L)
=\left(\frac{\sin(LT/n)}{LT/n}\right)^n.
\tag{11}
\]

For every `L>=H` one has `LT/n>=2`, hence

\[
|\widehat w_n(L)|\le2^{-n}.
\tag{12}
\]

Pairing (9) against the nonnegative probability density `w_n`, using Fubini, gives

\[
\left|
1-\int\widehat w_n(L)\,d\mu(L)
\right|
\le\epsilon.
\tag{13}
\]

Therefore

\[
1-\epsilon
\le A2^{-n},
\tag{14}
\]

or

\[
\boxed{
A\ge(1-\epsilon)2^{\lfloor HT/2\rfloor}
\ge(1-\epsilon)e^{cHT}
}
\tag{15}
\]

for an absolute `c>0` once `HT>=4`.

This is the first qualitative difference from `RE-203`. A finite set of samples can be annihilated by finite algebra with no interval observability requirement. A continuum forces an exponentially large signed reciprocal variation whenever every repair frequency is separated from zero by a fixed logarithmic gap.

The lower bound is intentionally stated for arbitrary measures, not just shell sums. Splitting one shell into many shells, allowing continuous shell locations, or choosing complex amplitudes cannot remove the `exp(Omega(HT))` cost. It is a generic Fourier/spectral-gap statement rather than an arithmetic one.

## 2. Binomial spectral-gap synthesis attains the exponential scale

The lower bound does not imply coercivity because an exponential cost in `T` may still be far below the source budget. We now construct a real discrete repair with the matching exponential order.

Fix `T>=1` and `0<epsilon<=1/4`. Set

\[
\delta:=\frac1{4T},
\qquad
m:=\lceil H/\delta\rceil,
\qquad
z:=e^{-i\delta t}.
\tag{16}
\]

For `|t|<=T`,

\[
|1-z|
=2\left|\sin\frac{\delta t}{2}\right|
\le2\sin(1/8)<\frac14.
\tag{17}
\]

The exact binomial series

\[
z^{-m}
=\bigl(1-(1-z)\bigr)^{-m}
=\sum_{k=0}^{\infty}
\binom{m+k-1}{k}(1-z)^k
\tag{18}
\]

therefore converges uniformly on the relevant arc. Truncate it at

\[
N:=m+\left\lceil\log_2(1/\epsilon)\right\rceil
\tag{19}
\]

and define

\[
S_{m,N}(z)
:=\sum_{k=0}^{N}
\binom{m+k-1}{k}(1-z)^k
=\sum_{j=0}^{N}b_jz^j.
\tag{20}
\]

All `b_j` are real. For the tail terms in (18), once `k>=m` the ratio of consecutive absolute terms is less than `1/2` by (17). Moreover

\[
\binom{m+N}{N+1}4^{-(N+1)}
\le2^{m-N-2}.
\tag{21}
\]

Hence

\[
\sup_{|t|\le T}
\left|z^{-m}-S_{m,N}(z)\right|
\le2^{m-N-1}
\le\epsilon.
\tag{22}
\]

Multiplying by `z^m`, define

\[
G(t):=z^mS_{m,N}(z)
=\sum_{j=0}^{N}b_j e^{-itL_j},
\qquad
L_j:=(m+j)\delta.
\tag{23}
\]

Then

\[
\boxed{
\sup_{|t|\le T}|1-G(t)|\le\epsilon,
\qquad
L_j\ge m\delta\ge H.
}
\tag{24}
\]

At `t=0`, `S_{m,N}(1)=1`, so `G(0)=1` exactly.

The coefficient cost is explicit. Since the coefficient `ell^1` norm of `(1-z)^k` is `2^k` and

\[
\binom{m+k-1}{k}\le2^{m+k-1},
\tag{25}
\]

we obtain

\[
A_{m,N}:=\sum_{j=0}^{N}|b_j|
\le
\sum_{k=0}^{N}
\binom{m+k-1}{k}2^k
\le(N+1)2^{m+2N}.
\tag{26}
\]

Thus

\[
\boxed{
\log A_{m,N}
=O\!\left(HT+\log(1/\epsilon)\right).
}
\tag{27}
\]

There are only

\[
N+1=O\!\left(HT+\log(1/\epsilon)\right)
\tag{28}
\]

shells, and their largest logarithmic displacement satisfies

\[
L_{\max}
=(m+N)\delta
=O\!\left(
H+\frac{\log(1/\epsilon)}{T}
\right).
\tag{29}
\]

Equations (15) and (27) show that at fixed accuracy the exponential dependence on `HT` is not an artifact of this particular binomial construction. The representation itself demands exponential reciprocal variation once the repair spectrum has a fixed gap from the local carrier.

## 3. Ordinary primes realize the continuum synthesis

Now take the arithmetic scale `Q` and set

\[
H:=\log 8,
\qquad
X_0:=2Q.
\tag{30}
\]

Apply the construction of Section 2 with `T=T_Q` and `epsilon=epsilon_Q`. For every coefficient `b_j` use the remote center

\[
X_j:=X_0e^{L_j}.
\tag{31}
\]

Because `L_j>=H`, the first remote center is at least `16Q`. Hence there is a fixed multiplicative corridor after the local packet in which the selector-scale debt is present before any repair begins.

Use the Korobov--Vinogradov PNT input already anchored in `SOURCES.md`: for some absolute `a>0`, the prime-counting error inherited from `theta(x)-x` is `O(xe^{-aV(x)})`. Put

\[
\eta_Q:=e^{-aV(Q)/4}.
\tag{32}
\]

Under (2), equations (28)--(29) give uniformly over all shells

\[
\log X_j=\log Q+o(V(Q)),
\qquad
V(X_j)=(1+o(1))V(Q).
\tag{33}
\]

Also the shell spacing is `delta=1/(4T_Q)`, while `eta_Q T_Q -> 0`; hence the logarithmic bins

\[
I_j:=[X_je^{-\eta_Q},X_je^{\eta_Q}]
\tag{34}
\]

are pairwise disjoint for large `Q`. The PNT/KV estimate yields

\[
\#\{q\text{ prime}:q\in I_j\}
=(2+o(1))\frac{\eta_QX_j}{\log X_j}.
\tag{35}
\]

Choose

\[
B\asymp\frac{\sqrt Q}{\log Q}
\tag{36}
\]

ordinary primes from `I_0` and assign coefficient `+1`. For each remote shell choose

\[
N_j:=\left\lfloor |b_j|e^{L_j}B\right\rceil
\tag{37}
\]

ordinary primes from `I_j` and assign to each the coefficient

\[
c_q=-\operatorname{sgn}(b_j).
\tag{38}
\]

There are enough distinct primes. Indeed, using (27), the ratio of the required population in any remote bin to the available population is

\[
\ll
\frac{A_{m,N}}{\eta_Q\sqrt Q}\,Q^{o(1)}
=
\exp\{-\tfrac12\log Q+o(V(Q))+aV(Q)/4\}
=o(1).
\tag{39}
\]

Thus every coefficient is implemented by deleting or duplicating a genuine ordinary prime exactly once; all multiplicities remain in `{0,1,2}`.

Ignoring bin width and integer rounding, the local first Euler harmonic equals

\[
B X_0^{-1-it}.
\tag{40}
\]

The remote shells contribute

\[
-BX_0^{-1-it}
\sum_{j=0}^{N}b_je^{-itL_j}
=-BX_0^{-1-it}G(t).
\tag{41}
\]

By (24), the ideal residual is therefore at most

\[
\epsilon_Q\frac{B}{X_0}
\asymp\epsilon_Q d_Q
\tag{42}
\]

**uniformly for every `|t|<=T_Q`**, not merely at a finite sample set.

## 4. Prime quantization and exact Euler factors stay below selector scale

For `q in I_j` and `|t|<=T_Q`, elementary differentiation gives

\[
q^{-1-it}
=X_j^{-1-it}
\left(1+O((1+T_Q)\eta_Q)\right),
\tag{43}
\]

uniformly because `T_Q eta_Q -> 0`. The total ideal reciprocal variation, normalized by the local reciprocal mass, is `A_{m,N}`. Hence prime placement contributes

\[
\ll
d_QA_{m,N}(1+T_Q)\eta_Q
=o(d_Q)
\tag{44}
\]

by (2), (27) and (32).

Rounding (37) changes the first harmonic by at most

\[
O\!\left(\sum_{j=0}^{N}X_j^{-1}\right)
=O(N/Q)
=o(d_Q).
\tag{45}
\]

Finally, uniformly on `Re s=1`,

\[
\log(1-q^{-s})^{-1}=q^{-s}+O(q^{-2}).
\tag{46}
\]

The complete higher-prime-power contribution is therefore

\[
\ll
\frac{B}{Q^2}
+
\sum_{j=0}^{N}
\frac{|b_j|e^{L_j}B}{X_j^2}
\ll
\frac{d_Q}{Q}A_{m,N}
=o(d_Q).
\tag{47}
\]

Combining (42), (44), (45) and (47) proves (4). At `t=0` the ideal first harmonic cancels exactly because `G(0)=1`; the remaining exact-Euler discrepancy is still `o(d_Q)`. Before the first remote shell, however, the local packet alone has

\[
\sum_{q\in I_0}\log(1-q^{-1})^{-1}
=\Theta(B/Q)
=\Theta(d_Q),
\tag{48}
\]

which proves (5).

The total absolute Chebyshev edit mass is bounded by

\[
\ll
B\log Q
\left(
1+\sum_{j=0}^{N}|b_j|e^{L_j}
\right)
\le
\sqrt Q\,A_{m,N}e^{L_{\max}}Q^{o(1)}.
\tag{49}
\]

By (2), (27) and (29),

\[
A_{m,N}e^{L_{\max}}=e^{o(V(Q))},
\tag{50}
\]

so (49) is `Q^(1/2+o(1))`. All affected centers are `Qe^{o(V(Q))}=Q^{1+o(1)}`. Consequently, for every fixed `b>0`, every partial Chebyshev discrepancy through the affected range is dominated by

\[
Q^{1/2+o(1)}
=o\!\left(xe^{-bV(x)}\right),
\tag{51}
\]

and the same remains true beyond the last shell. This proves the KV fidelity statement (6).

## Representation audit

The continuum mechanism is generic harmonic analysis before any prime is introduced. Approximating an out-of-band or spectrally separated mode on a finite interval by combinations of allowed Fourier modes is part of the classical superoscillation/supershift phenomenon, and the associated large dynamic-range cost is well known. Relevant prior-art boundaries include Ferreira--Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Transactions on Signal Processing **54** (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, and the survey Berry et al., *Roadmap on superoscillations*, Journal of Optics **21** (2019), 053002, DOI `10.1088/2040-8986/ab0191`. No novelty is claimed for the generic possibility of local out-of-band approximation or for the qualitative fact that it requires exponential dynamic range.

The elementary B-spline dual bound (15) and binomial construction (18)--(29) are included to pin the exact norm, one-sided spectral gap and time--gap scaling needed here; no external approximation theorem is invoked. The line-specific content is the quantitative conversion of that continuum synthesis into **ordinary-prime Euler atoms with integer multiplicities at selector reciprocal scale**, while retaining a fixed pre-repair corridor, controlling all exact prime powers, and remaining inside every fixed Korobov--Vinogradov Chebyshev envelope.

This changes the architectural lesson after `RE-203`. The relevant divide is not finite samples versus a continuum. A continuum does force exponential source variation, but under the present source class that cost is still realizable whenever the observed vertical height is sub-KV in the sense of (2).

## Adversarial self-review

**Does the lower bound assume a discrete shell architecture?** No. The measure `mu` in Section 1 may be arbitrary and complex on all of `[H,infinity)`. The B-spline test sees only the spectral gap `L>=H` and the continuum approximation hypothesis.

**Is the claimed exponential lower bound just a coefficient-count statement?** No. It is a lower bound on total variation of the normalized reciprocal repair measure. Arbitrarily many tiny coefficients do not evade it.

**Does the upper construction secretly use a zero-displacement shell?** No. Every frequency in (23) is `L_j=(m+j)delta>=H`. At `H=log 8` and `X_0=2Q`, every repair shell begins at or beyond `16Q`.

**Are complex shell weights being smuggled into the prime source?** No. The coefficients `b_j` are real because (20) is a real polynomial. Their magnitudes are implemented by integer populations, and their signs by deletion or duplication. Individual prime coefficients remain exactly `-1` or `+1`.

**Could adjacent logarithmic shells overlap when `T_Q` grows?** No in the stated regime. Their spacing is `delta=1/(4T_Q)`, whereas the PNT bins have half-width `eta_Q=e^{-aV(Q)/4}`; condition (2) gives `T_Q eta_Q -> 0`.

**Could large continuum height resolve prime placement inside the bins?** This is exactly the phase-resolution issue measured by (44). The product of continuum height, coefficient variation and bin width is `e^{-aV(Q)/4+o(V(Q))}`, hence tends to zero under (2).

**Do exact prime powers restore continuum visibility?** No at this scale. Equation (47) leaves an additional factor `Q^{-1}` after the full exponential coefficient cost.

**Does the exponential lower bound itself imply a rigidity transition at `T asymp V(Q)`?** No. Even `e^{Theta(V(Q))}` is only `Q^{o(1)}`. The present construction stops at `T=o(V(Q))` because its coefficient growth must coexist with the available KV phase resolution in the prime bins. Constants may permit part of the `T=cV(Q)` regime. Nothing here proves coercivity at, above, or near `V(Q)`.

**Does this reproduce the full matched controls of `RE-188`--`RE-199` or prove a Robin consequence?** No. It proves noncoercivity of the entire vertical Euler observation window at selector reciprocal scale within the current ordinary-prime/KV source class. It does not show that this isolated packet alone creates the complete Robin destination excursion or simultaneously enforces every earlier matched constraint.

## Prior-art audit

The literature search found the expected classical superoscillation/supershift framework and exponential dynamic-range phenomenon, including Ferreira--Kempf (2006) and later surveys. That generic approximation mechanism is therefore treated as prior art, not as a new theorem family.

No external result from that literature is load-bearing in the proof above: both the continuum lower bound and the explicit real synthesis are derived directly. The only arithmetic theorem used is the Korobov--Vinogradov PNT control already anchored in `SOURCES.md`. No durable source addition is therefore required.

The new line-specific statement is the regime comparison: **the exponential continuum hiding tariff is still affordable by genuine ordinary primes, exact `{0,1,2}` multiplicities and every-fixed-`b` KV fidelity whenever `T_Q+log(1/epsilon_Q)=o(V(Q))`**. This closes the finite-versus-continuum escape left open in `RE-203` throughout the full sub-KV vertical range.

## Caveats

The theorem is a sufficient noncoercivity construction below the KV phase scale, not a sharp transition theorem. The constants hidden in the PNT error, the bin width and the synthesis norm matter once `T_Q` is a fixed positive fraction of `V(Q)`.

The lower bound controls reciprocal total variation under a fixed pre-repair spectral gap. It does not by itself lower-bound Chebyshev discrepancy, edit count, shell range or any CA-native complexity measure sharply enough to force a contradiction.

The perturbation is finite at each `Q` and source-faithful in ordinary-prime support and multiplicity, but it remains a matched control rather than the actual prime source. No RH, Robin, zero-free-region or source-identification theorem follows.

## Next experiment

The vertical scalar frontier is now genuinely quantitative. The next test should work at the **critical phase-resolution scale** `T_Q=cV(Q)` rather than merely changing the sampling pattern. Optimize the continuum synthesis norm and the prime-bin width constants simultaneously, and determine whether there exists a positive interval of constants `c` for which ordinary-prime `{0,1,2}` realization still gives `o(d_Q)` uniform hiding.

A negative result would need more than the generic `exp(Omega(T_Q))` variation tariff, because that cost remains subpolynomial in `Q`. It would have to show that phase resolution, integer prime supply, Chebyshev fidelity or a source-native complexity law makes the required continuum repair impossible. A positive result would push scalar complex-Euler noncoercivity into the critical `V(Q)` window and make an explicitly nonlocal/structural observable still more necessary.

## Sources

- `RE-200`, *Vertical Euler phase supports linear stable dimension on one prime shell*.
- `RE-203`, *Multi-shell polynomial synthesis aliases arbitrary vertical Euler panels below the KV phase-resolution scale*.
- `RE-015`, for the Korobov--Vinogradov PNT envelope already anchored in `SOURCES.md`.