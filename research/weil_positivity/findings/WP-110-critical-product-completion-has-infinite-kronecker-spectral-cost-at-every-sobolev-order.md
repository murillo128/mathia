# WP-110 — Critical product completion has infinite Kronecker spectral cost at every Sobolev order

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRODUCT-SPECIFIC + ALL-SOBOLEV-ORDERS + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-109` proves that the exact one-prime Weil rays force infinite cylindrical Kronecker spectral cost for every inhomogeneous Sobolev order `s >= -1`, independently of how the mixed-prime coefficients are completed. It deliberately leaves `s < -1` open because sufficiently strong negative-order smoothing makes the forced one-prime axes summable.

For the explicit positive **independent product completion** constructed in `WP-097`, that escape does not exist. The same mixed-prime coefficients that rescue finite diagonal positivity create an infrared accumulation of near-resonant modes. At the critical exponent `sigma=1/2`, these modes force

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal S_{s,P}(\eta_P)=+\infty
\qquad\text{for every real }s,
}
\tag{1}
\]

where `S_{s,P}` is exactly the Kronecker spectral form of `WP-109`.

More generally, if `w:[0,\infty)\to[0,\infty)` is continuous at `0` and `w(0)>0`, then the product completion has infinite cylindrical cost for the spectral multiplier `w(|X|)` as well. Thus **arbitrarily strong high-frequency smoothing cannot regularize this product completion while the positive spectral form remains nondegenerate at zero frequency**.

This is a decisive negative only for the `WP-097` product completion. `WP-101` shows that correlated completions can change mixed-prime coefficients, so (1) is not a no-go theorem for every positive completion of the critical one-prime rays. Nor is `S_s` a Weil positivity form: it contains no intrinsic archimedean or pole terms.

## 1. Product completion and Kronecker spectral form

At the critical exponent, `WP-097` gives, for every fixed

\[
C\ge C_* = \frac{2\log 2}{\sqrt2-1},
\tag{2}
\]

the positive product measure

\[
\mu_C
=C\bigotimes_p
\left[
1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta_p)\right)
\right]\frac{d\theta_p}{2\pi}.
\tag{3}
\]

For a finite prime set `P`, normalize its marginal to probability mass one:

\[
\eta_P:=C^{-1}(\pi_P)_*\mu_C.
\tag{4}
\]

The one-coordinate Fourier coefficients are

\[
\widehat\eta_P(k e_p)
=-\frac{\log p}{C\,p^{|k|/2}}
\qquad(k\ne0).
\tag{5}
\]

Because (3) is a product, the two-prime difference modes factor exactly. For distinct primes `p,q in P`,

\[
\boxed{
\widehat\eta_P(e_p-e_q)
=
\frac{(\log p)(\log q)}{C^2\sqrt{pq}}.
}
\tag{6}
\]

The intrinsic multiplicative/Kronecker generator is

\[
X_P=\sum_{p\in P}(\log p)\partial_{\theta_p},
\qquad
X_P z^\alpha=iE(\alpha)z^\alpha,
\qquad
E(\alpha)=\sum_{p\in P}\alpha_p\log p.
\tag{7}
\]

Following `WP-109`, for real `s` define

\[
\mathcal S_{s,P}(\eta_P)
=
\sum_{\alpha\in\mathbb Z^P}
\bigl(1+E(\alpha)^2\bigr)^s
\left|\widehat\eta_P(\alpha)\right|^2.
\tag{8}
\]

The obstruction below uses only the finite marginals (4), so the Haar singularity of the infinite product from `WP-100` is irrelevant to the argument.

## 2. Comparable primes produce low-frequency mixed modes

Fix `epsilon>0`. Choose `delta>0` so that

\[
\log(1+\delta)<\epsilon.
\tag{9}
\]

For large `X`, let

\[
P_X:=\{p\text{ prime}:X<p\le(1+\delta)X\}.
\tag{10}
\]

For every ordered pair of distinct primes `p,q in P_X`, the mixed mode

\[
\alpha_{p,q}=e_p-e_q
\tag{11}
\]

has Kronecker frequency

\[
E(\alpha_{p,q})
=\log p-\log q
=\log(p/q),
\tag{12}
\]

hence

\[
\boxed{|E(\alpha_{p,q})|<\epsilon.}
\tag{13}
\]

There is no exact nonzero resonance: unique factorization implies `E(alpha)=0` only for `alpha=0`. What matters here is not an exact kernel of `X_P` but an increasing family of distinct mixed modes inside a fixed arbitrarily small spectral window around zero.

Set

\[
b_p:=\frac{(\log p)^2}{p}.
\tag{14}
\]

Equation (6) gives

\[
\left|\widehat\eta_{P_X}(e_p-e_q)\right|^2
=\frac{b_pb_q}{C^4}.
\tag{15}
\]

Define the shell sums

\[
A_\delta(X)
:=\sum_{X<p\le(1+\delta)X}b_p,
\qquad
B_\delta(X)
:=\sum_{X<p\le(1+\delta)X}b_p^2.
\tag{16}
\]

The prime number theorem and partial summation give, for fixed `delta`,

\[
\boxed{
A_\delta(X)
=\log(1+\delta)\log X+O_\delta(1),
}
\tag{17}
\]

so `A_delta(X) -> infinity`. Meanwhile the elementary bound `#P_X=O_delta(X)` already yields

\[
B_\delta(X)
=O_\delta\!\left(\frac{(\log X)^4}{X}\right)
=o(1).
\tag{18}
\]

Therefore the total squared Fourier mass of just these ordered two-prime modes is

\[
\begin{aligned}
\sum_{\substack{p,q\in P_X\\p\ne q}}
\left|\widehat\eta_{P_X}(e_p-e_q)\right|^2
&=\frac1{C^4}
\left(A_\delta(X)^2-B_\delta(X)\right)\\
&\sim
\frac{\log^2(1+\delta)}{C^4}\log^2X
\longrightarrow+\infty.
\end{aligned}
\tag{19}
\]

Thus the critical product completion has unbounded cylindrical Fourier mass in every fixed neighborhood of **zero Kronecker frequency**.

## 3. Every inhomogeneous Sobolev order diverges

For fixed real `s`, the weight

\[
w_s(t)=(1+t^2)^s
\tag{20}
\]

has a strictly positive lower bound on `[0,epsilon]`. Explicitly,

\[
m_s(\epsilon):=
\min_{0\le t\le\epsilon}(1+t^2)^s
=
\begin{cases}
1,&s\ge0,\\
(1+\epsilon^2)^s,&s<0,
\end{cases}
>0.
\tag{21}
\]

Keeping only the modes (11) in the nonnegative sum (8), and using (13), gives

\[
\mathcal S_{s,P_X}(\eta_{P_X})
\ge
m_s(\epsilon)
\sum_{\substack{p,q\in P_X\\p\ne q}}
\left|\widehat\eta_{P_X}(e_p-e_q)\right|^2.
\tag{22}
\]

Equation (19) therefore proves (1) for **every `s in R`**.

The mechanism is complementary to `WP-109`:

- the mandatory one-prime modes `e_p` move to Kronecker frequency `log p -> infinity` and cause the high-frequency obstruction through `s=-1`;
- the product completion's mandatory two-prime modes `e_p-e_q` with comparable `p,q` accumulate at bounded, indeed arbitrarily small, Kronecker frequency and defeat every stronger negative-order inhomogeneous Sobolev weight.

In this sense the explicit product completion is trapped at both ends of the same positive spectral scale: stronger decay at high frequency does not touch the mixed-prime infrared pileup.

## 4. The obstruction is not special to power weights

Let

\[
w:[0,\infty)\to[0,\infty)
\tag{23}
\]

be continuous at zero with `w(0)>0`. There is an `epsilon>0` and a constant `c_w>0` such that

\[
w(t)\ge c_w
\qquad(0\le t<\epsilon).
\tag{24}
\]

Define the corresponding cylindrical positive spectral cost

\[
\mathcal S_{w,P}(\eta_P)
:=
\sum_{\alpha\in\mathbb Z^P}
w(|E(\alpha)|)
|\widehat\eta_P(\alpha)|^2.
\tag{25}
\]

The same shell modes then give

\[
\mathcal S_{w,P_X}(\eta_{P_X})
\ge
\frac{c_w}{C^4}
\left(A_\delta(X)^2-B_\delta(X)\right)
\longrightarrow+\infty.
\tag{26}
\]

So the failure is not an artifact of selecting the Sobolev family `(1+X^*X)^s`. Any nonnegative spectral geometry that remains nondegenerate at the bottom of the Kronecker spectrum sees the same divergent mixed-prime mass for this completion.

This statement intentionally does **not** cover a multiplier with `w(0)=0`. A geometry whose spectral symbol both vanishes sufficiently strongly near zero and decays sufficiently strongly at infinity could evade the two complementary lower bounds `WP-109` and (26). Such a band-pass or homogeneous construction would still need to be forced by Mathia geometry and to generate the full finite plus archimedean Weil form; inserting a hand-picked spectral notch is excluded by the research mandate.

## 5. Matched controls and falsifiers

### Off-critical control

The all-order obstruction is critical. Replace `p^{-1/2}` in the same product construction by `p^{-sigma}` with `sigma>1/2`. The normalized one-coordinate `L^2` excess is

\[
2\left(\frac{\log p}{C}\right)^2
\frac{p^{-2\sigma}}{1-p^{-2\sigma}}.
\tag{27}
\]

Because

\[
\sum_p\frac{(\log p)^2}{p^{2\sigma}}<\infty
\qquad(\sigma>1/2),
\tag{28}
\]

the product has finite cylindrical `L^2` Fourier mass. Consequently every negative-order inhomogeneous Kronecker form satisfies

\[
\mathcal S_{s,P}\le\mathcal S_{0,P}
\qquad(s\le0)
\tag{29}
\]

uniformly in finite `P`. The near-resonant mixed-prime divergence therefore disappears on the convergent side of the critical boundary.

### Correlated-completion falsifier

Equation (6) is product-specific. `WP-101` demonstrates that correlations can alter mixed-prime coefficients while preserving the prescribed one-prime marginals. Therefore the argument cannot be promoted to a correlation-independent theorem for `s<-1`; only the `WP-109` axis obstruction is correlation-independent.

### Infinite-product singularity falsifier

No density on the full infinite torus is used. Every lower bound is proved on finite prime sets `P_X`, so changing the interpretation of the singular infinite product cannot remove (19).

### Diagonal-mass falsifier

The admissible constant `C` is fixed and finite. Its only role in (19) is the harmless factor `C^{-4}`. Increasing `C` to any other fixed finite value cannot change divergence. Allowing `C` itself to grow with the prime cutoff would abandon the finite global diagonal required by `WP-097` and return to the extensive counterterm problem already isolated in `WP-096`.

## 6. Prior-art and novelty audit

The ingredients used here are classical and are not claimed as new:

- the Bohr transform identifying Dirichlet-series frequencies with Fourier characters on the infinite prime torus;
- Kronecker flow with frequency `E(alpha)=sum_p alpha_p log p`;
- product/Riesz-product factorization of Fourier coefficients;
- the prime number theorem and partial summation.

The Hedenmalm--Lindqvist--Seip Bohr/Hardy framework already recorded in `research/weil_positivity/SOURCES.md` is a canonical prior-art anchor for the prime-polytorus representation. Classical small-divisor/Kronecker theory also makes the existence of low frequencies from differences of nearby logarithms unsurprising.

The Mathia-specific content is narrower: combining the exact `WP-097` critical positive product completion with the `WP-109` Kronecker spectral geometry shows that the previously open `s<-1` smoothing escape is **completely closed for this explicit completion**, by an exact shell lower bound that grows like `log^2 X`. A targeted repository and literature audit found no basis for claiming the harmonic-analysis ingredients themselves as novel, and no exact prior result was identified that changes this branch-local conclusion.

This result remains well inside the classical harmonic-analysis/Dirichlet-series envelope. It is a structural obstruction, not evidence for a new route to RH.

## 7. Consequence for Weil positivity

The product completion of `WP-097` was important because it proved that mixed-prime interactions can restore genuine finite-mass positivity while preserving every critical one-prime Weil ray. `WP-110` shows the cost of that repair in the intrinsic multiplicative spectral geometry: the mixed interactions create an unbounded family of near-zero-frequency modes whose positive mass cannot be removed by any inhomogeneous negative Sobolev smoothing.

Hence the route

\[
\text{critical positive product completion}
\longrightarrow
\text{stronger Kronecker resolvent/Sobolev smoothing}
\longrightarrow
\text{finite global positive energy}
\]

is closed.

A surviving route must change at least one structural ingredient before the sign theorem is applied: introduce nonproduct correlations that genuinely suppress the mixed-prime infrared mass, use an intrinsically justified spectral form degenerate at zero as well as sufficiently smoothing at infinity, or couple the finite-prime carrier nonseparably to new global/archimedean geometry. None of those mechanisms is supplied by this finding, and any successful candidate must still recover the Gamma and pole/counterterm pieces without inserting them by hand.
