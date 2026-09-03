# WP-125 — Critical product completion has infinite mass in every fixed Kronecker band

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRODUCT-SPECIFIC + ALL-CONTINUOUS-SPECTRAL-MULTIPLIERS + GAMMA-BANDPASS-STRESS-TEST + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-110` proves that the explicit critical positive product completion of `WP-097` has infinite Kronecker spectral cost for every inhomogeneous Sobolev order, and more generally for every nonnegative spectral multiplier that stays positive at zero. It deliberately leaves a zero-frequency-degenerate band-pass escape: a positive multiplier could vanish near the Kronecker origin and also decay at high frequency.

For this **specific product completion**, that escape is actually impossible. Its factorized two-prime coefficients place divergent Fourier mass not merely near zero but in **every fixed nonempty Kronecker-frequency band**. Consequently every nonzero continuous nonnegative scalar multiplier has infinite cylindrical cost, including operator-positive band-pass filters that evade both endpoint tests of `WP-109` and `WP-114`.

This is not a theorem for arbitrary correlated completions. The proof uses the exact product factorization of `WP-097`; correlations may redistribute the mixed-prime mass, and `WP-114` remains the architecture-free statement only near zero frequency.

## 1. The product completion and its two-prime modes

At the critical exponent, fix the positive product completion from `WP-097` with finite normalization

\[
C\ge C_* = \frac{2\log 2}{\sqrt2-1}.
\tag{1}
\]

For every finite prime set `P`, let `eta_P` be its normalized marginal. For distinct primes `p,q in P`, `WP-110` gives the exact coefficient

\[
\boxed{
\widehat\eta_P(e_q-e_p)
=
\frac{(\log p)(\log q)}{C^2\sqrt{pq}}.
}
\tag{2}
\]

The Kronecker generator has frequency

\[
E(\alpha)=\sum_{p\in P}\alpha_p\log p,
\qquad
E(e_q-e_p)=\log(q/p).
\tag{3}
\]

Write

\[
b_p:=\frac{(\log p)^2}{p}.
\tag{4}
\]

Then

\[
\left|\widehat\eta_P(e_q-e_p)\right|^2
=
\frac{b_pb_q}{C^4}.
\tag{5}
\]

The question is whether a scalar positive spectral multiplier can avoid the near-zero pileup found in `WP-110` by concentrating on a band away from zero. Equation (5) makes that test exact.

## 2. Every prescribed positive-frequency band contains divergent product mass

Let `I` be a nonempty open interval in `(0,infinity)`. Choose `t_0 in I` and `epsilon>0` so small that

\[
[t_0-\epsilon,t_0+\epsilon]\subset I,
\qquad
0<\epsilon<t_0.
\tag{6}
\]

For large `X`, define two disjoint fixed-width multiplicative prime shells

\[
A_X=\{p:X<p\le e^\epsilon X\},
\qquad
B_X=\{q:e^{t_0}X<q\le e^{t_0+\epsilon}X\}.
\tag{7}
\]

For every `p in A_X` and `q in B_X`,

\[
t_0-\epsilon
\le
\log(q/p)
\le
t_0+\epsilon,
\tag{8}
\]

so all the modes `e_q-e_p` lie inside the prescribed band `I`.

The prime number theorem and partial summation give, for every fixed `epsilon>0`,

\[
\sum_{X<p\le e^\epsilon X}\frac{(\log p)^2}{p}
=
\epsilon\log X+O_\epsilon(1).
\tag{9}
\]

The shifted shell has the same leading growth:

\[
\sum_{e^{t_0}X<q\le e^{t_0+\epsilon}X}
\frac{(\log q)^2}{q}
=
\epsilon\log X+O_{\epsilon,t_0}(1).
\tag{10}
\]

Take `P_X=A_X union B_X`. Using (5), the Fourier mass carried only by these cross-shell modes is

\[
\begin{aligned}
\sum_{\substack{p\in A_X\\q\in B_X}}
\left|\widehat\eta_{P_X}(e_q-e_p)\right|^2
&=
\frac1{C^4}
\left(\sum_{p\in A_X}b_p\right)
\left(\sum_{q\in B_X}b_q\right)\\
&=
\frac{\epsilon^2}{C^4}\log^2X+O_{\epsilon,t_0,C}(\log X).
\end{aligned}
\tag{11}
\]

Hence

\[
\boxed{
\sup_{P\Subset\mathcal P}
\sum_{\substack{\alpha\in\mathbb Z^P\\|E(\alpha)|\in I}}
|\widehat\eta_P(\alpha)|^2
=+\infty
}
\tag{12}
\]

for every nonempty open interval `I subset (0,infinity)`.

The band may be arbitrarily narrow and centered at any fixed positive frequency. No Diophantine approximation is needed: ordinary prime density in two multiplicatively matched shells already supplies the required modes.

## 3. The zero band is also divergent

If a relative-open band in `[0,infinity)` contains zero, choose `epsilon>0` inside it and use one shell

\[
Q_X=\{p:X<p\le e^\epsilon X\}.
\tag{13}
\]

For distinct `p,q in Q_X`,

\[
|\log(q/p)|<\epsilon.
\tag{14}
\]

The calculation of `WP-110` gives

\[
\sum_{\substack{p,q\in Q_X\\p\ne q}}
|\widehat\eta_{Q_X}(e_q-e_p)|^2
\sim
\frac{\epsilon^2}{C^4}\log^2X.
\tag{15}
\]

Combining (12) and (15), the product completion has divergent cylindrical Fourier mass in **every nonempty open band of the absolute Kronecker spectrum**.

## 4. Every nonzero continuous scalar positive multiplier diverges

Let

\[
w:[0,infinity)\to[0,infinity)
\tag{16}
\]

be continuous and not identically zero. Define

\[
\mathcal Q_{w,P}(\eta_P)
=
\sum_{\alpha\in\mathbb Z^P}
 w(|E(\alpha)|)
 |\widehat\eta_P(\alpha)|^2.
\tag{17}
\]

There is some `t_0>=0` with `w(t_0)>0`. By continuity, a nonempty open band `I` around `t_0` and a constant `c_w>0` exist such that

\[
w(t)\ge c_w
\qquad(t\in I).
\tag{18}
\]

Retaining only modes in `I` and applying (12) or (15) gives

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal Q_{w,P}(\eta_P)
=+\infty
\qquad
\text{for every nonzero continuous }w\ge0.
}
\tag{19}
\]

This strictly strengthens the product-specific multiplier statement of `WP-110`. Vanishing at zero, compact spectral support, arbitrarily strong high-frequency decay, or a smooth band-pass shape do not help. Any fixed continuous scalar spectral geometry that charges even one open frequency band sees infinite critical mass.

The theorem is deliberately about a **fixed** multiplier. A cutoff-dependent family whose support or amplitude changes with `P` is not one global geometric form and therefore does not evade (19) within the research mandate.

## 5. Gamma heat-dissipation is a decisive band-pass stress test

`WP-117` derives the intrinsic archimedean Gamma symbol

\[
H_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-
\psi\!\left(\frac14\right),
\tag{20}
\]

with `H_infty(0)=0`, `H_infty(t)>0` for `t>0`, and

\[
H_\infty(t)=\log|t|+O(1)
\qquad(|t|\to\infty).
\tag{21}
\]

A natural nonlocal operator-positive band-pass obtained from this canonical archimedean generator is the heat-dissipation multiplier

\[
\boxed{
w_\tau(t)=H_\infty(t)e^{-\tau H_\infty(t)},
\qquad\tau>0.
}
\tag{22}
\]

Indeed, on the Kronecker spectral side,

\[
\langle f,
H_\infty(|X|)e^{-\tau H_\infty(|X|)}f\rangle
=
\left\|
H_\infty(|X|)^{1/2}
e^{-\tau H_\infty(|X|)/2}f
\right\|^2
\ge0.
\tag{23}
\]

This family was not killed by the endpoint logic alone. It satisfies `w_tau(0)=0`, so the `w(0)>0` theorem `WP-114` does not apply. At the mandatory critical prime axes, (21) gives

\[
w_\tau(\log p)
\asymp_\tau
(\log\log p)(\log p)^{-\tau},
\tag{24}
\]

and therefore

\[
\sum_p
w_\tau(\log p)
\frac{(\log p)^2}{p}
\asymp_\tau
\sum_p
\frac{(\log p)^{2-\tau}\log\log p}{p}.
\tag{25}
\]

By the prime number theorem, the series in (25) converges exactly when

\[
\boxed{\tau>2.}
\tag{26}
\]

Thus for `tau>2` the Gamma heat-dissipation form genuinely passes the two elementary endpoint necessary tests: it vanishes at the low-frequency endpoint and sufficiently suppresses the compulsory high-frequency prime axes. It is also outside the scalar Lévy/Dirichlet cone of `WP-115`: if it were a nonzero CND symbol, `WP-115` would force the axis series (25) to diverge.

Nevertheless `w_tau` is continuous, nonnegative, and nonzero for every fixed `tau>0`. Equation (19) therefore gives

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal Q_{w_\tau,P}(\eta_P)=+\infty
\qquad(\tau>0)
}
\tag{27}
\]

for the explicit critical product completion. In particular, even the `tau>2` forms that pass both endpoint tests fail because the product completion carries divergent mass in every interior frequency band.

This is a useful falsifier for the surviving nonlocal/infinite-order escape left by `WP-123`--`WP-124`: **endpoint-adapted smoothing is not enough on the canonical independent product completion, even when the smoothing is built directly from the intrinsic Gamma generator.**

## 6. Matched controls and scope

### Supercritical attenuation passes the same bounded band-pass test

At exponent `sigma>1/2`, the product completion has uniformly finite cylindrical `L^2` Fourier mass, as recorded in `WP-110`. Since `w_tau` is bounded (`x e^{-tau x}<=1/(e tau)` for `x>=0`),

\[
\mathcal Q_{w_\tau,P}(\eta_{\sigma,P})
\le
\|w_\tau\|_\infty
\mathcal S_{0,P}(\eta_{\sigma,P})
\tag{28}
\]

is uniformly finite in `P`. Thus the same Gamma band-pass that necessarily diverges for the critical product completion is harmless immediately on the convergent side `sigma>1/2`.

### Sparse generalized generators do not force the band explosion

The proof of (11) uses both the exact product coefficient and the ordinary-prime shell law (9). For a free multiplicative control with generator energies `E_j=j` and critical-looking amplitudes `E_j e^{-E_j/2}`, the squared-amplitude mass in any fixed-width high-energy shell tends exponentially to zero. Two shifted shells therefore do not produce (11). The fixed-band explosion is tied to the density and critical amplitude scale of ordinary prime energies, not to every free-monoid product geometry.

### Arbitrary correlations remain a genuine escape

The identity (2) is essential. A correlated positive completion may alter or suppress the cross-shell coefficients `e_q-e_p` while keeping the exact one-prime moments. `WP-114` proves that positivity still forces divergent mixed mass arbitrarily close to zero, but it does not force that mass into every band away from zero once the multiplier itself vanishes there.

Therefore (19) must **not** be promoted to all positive completions. A correlated/nonseparable completion paired with a zero-degenerate band-pass remains logically open, as do architectures that change the state space or finite observable before scalar spectral positivity is formed.

### The result still does not supply Weil positivity

No Gamma heat-dissipation form above is identified with the Weil explicit formula. Equation (27) is a negative stress test on one positive completion, not a candidate proof of RH. The missing global problem remains: one architecture must generate the finite Mangoldt contribution, the Gamma/pole terms, and an independently positive global form with the correct normalization.

## 7. Prior-art and novelty audit

The proof ingredients are classical and no theorem-level historical novelty is claimed for them.

- The infinite-prime-torus/Bohr realization of Dirichlet-series frequencies is classical; the repository anchor is Hedenmalm--Lindqvist--Seip, *A Hilbert space of Dirichlet series and systems of dilated functions in L2(0,1)*, Duke Math. J. 86 (1997), already recorded in `research/weil_positivity/SOURCES.md`.
- Product/Riesz-product factorization of Fourier coefficients is standard harmonic analysis.
- The weighted fixed-width prime-shell asymptotic (9) is an elementary consequence of the prime number theorem and partial summation.
- The Gamma/digamma asymptotic and Schoenberg/Markov interpretation used in the stress test are already audited in `WP-117` and `WP-118`.

A bounded literature audit of Bohr lifts of Dirichlet series, infinite prime-torus harmonic analysis, Riesz products, and Kronecker flows found the standard ambient machinery but no external result that changes the branch-local statement proved here. In particular, the Hedenmalm--Lindqvist--Seip framework identifies the prime character torus, while the present fixed-band divergence comes from combining the specific `WP-097` critical product coefficients with ordinary prime density. The absence of a matching paper is not used as a claim of historical novelty.

This result is therefore best read as an exact **Mathia-internal strengthening** of `WP-110`: the explicit product completion is spectrally saturated on every fixed band, so scalar positive functional calculus cannot repair it.

## Research consequence

For the `WP-097` independent positive completion, the scalar Kronecker spectral route is now closed much more sharply:

\[
\boxed{
\text{critical product completion}
+
\text{any fixed nonzero continuous }w(|X|)\ge0
\Longrightarrow
\text{infinite cylindrical cost}.
}
\tag{29}
\]

The important surviving distinction is **product versus correlated/nonseparable completion**, not merely low versus high frequency. A successful Mathia-native route must change the mixed-prime architecture before scalar positivity is taken, or leave fixed continuous scalar functional calculus altogether. The Gamma heat-dissipation example shows that even a natural archimedean band-pass with the correct endpoint behavior cannot rescue the independent product completion.