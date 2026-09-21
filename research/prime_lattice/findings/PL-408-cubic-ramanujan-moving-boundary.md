# PL-408 — The cubic filter pushes the singular-series correction to a moving square-free Ramanujan boundary

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + ROUTE-ADVANCE + SPECTRAL-ENDPOINT-REFORMULATION`.

**Parent findings:** `PL-404`, `PL-405`, `PL-406`, `PL-407`.

## Claim

The cubic source test of `PL-404`--`PL-407` has a sharper prime-exponent interpretation than the generic short-interval-variance formulation alone reveals. In the classical Ramanujan spectrum of the Hardy--Littlewood pair singular series, the forced cubic filter suppresses every fixed nontrivial denominator and, quantitatively, every fixed fractional interior of the square-free exponent-energy ball. The deterministic `H^{-1}` correction and the RH-sensitive `H^{-7/4}` layer therefore cannot be carried by finitely many local Ramanujan modes; they are a genuinely moving-boundary phenomenon in the square-free exponent lattice.

Fix

\[
a=\frac\pi6,
\qquad
K_\eta(x)
=|x|e^{-\eta|x|^3}\sin(a|x|^3),
\qquad \eta>0,
\tag{1}
\]

which is the even extension of the shifted Abel weight from `PL-404`. Let

\[
\widehat K_\eta(\xi)
=\int_{\mathbb R}K_\eta(x)e^{-2\pi i x\xi}\,dx.
\tag{2}
\]

For `Q>=1`, truncate the singular series in its Ramanujan denominator:

\[
\mathfrak S_{\le Q}(h)
:=\sum_{q\le Q}
\frac{\mu(q)^2}{\phi(q)^2}c_q(h),
\tag{3}
\]

and define the corresponding cubic source statistic

\[
A_{\eta,\le Q}^{[2]}(H)
:=\frac1H\sum_{d\ge1}
\mathfrak S_{\le Q}(d)K_\eta(d/H).
\tag{4}
\]

Then, uniformly for `2<=Q<=H`,

\[
\boxed{
A_{\eta,\le Q}^{[2]}(H)
=W_{1,\eta}
+O_\eta\!\left(
H^{-7}Q^6\{\log\log(3Q)\}^2
\right),
}
\tag{5}
\]

where `W_(1,eta)` is the leading constant already defined in `PL-404`, equivalently

\[
2W_{1,\eta}=\widehat K_\eta(0).
\tag{6}
\]

Consequently, if `Q=H^kappa` with fixed `0<kappa<1`,

\[
A_{\eta,\le H^\kappa}^{[2]}(H)
=W_{1,\eta}
+O_\eta\!\left(
H^{-7+6\kappa}(\log\log H)^2
\right).
\tag{7}
\]

Two thresholds follow immediately.

First, for every fixed `kappa<1`,

\[
A_{\eta,\le H^\kappa}^{[2]}(H)
=W_{1,\eta}+o(H^{-1}).
\tag{8}
\]

Thus the nonzero deterministic `-W_(0,eta)/(2H)` term in the full `PL-404` singular-series asymptotic cannot be produced by any fixed fractional interior `q<=H^(1-epsilon)`.

Second, for every fixed `kappa<7/8`,

\[
A_{\eta,\le H^\kappa}^{[2]}(H)
=W_{1,\eta}+o(H^{-7/4}).
\tag{9}
\]

Hence no denominator range `q<=H^(7/8-epsilon)` can carry information at the already-fixed RH-sensitive `H^{-7/4}` resolution. The number `7/8` is a **method-relative localization threshold**, not a sharp arithmetic phase transition: it comes from the seventh-order Fourier decay available for this exact Abel kernel and the elementary absolute summation over Ramanujan denominators.

Because `mu(q)^2` restricts (3) to square-free `q`, the cutoff `q<=H^kappa` is exactly the prime-exponent energy cutoff

\[
\langle v(q),(\log p)_p\rangle
=\log q
\le \kappa\log H,
\qquad
v(q)\in\{0,1\}^{(\mathcal P)}.
\tag{10}
\]

Equations (8)--(9) therefore say that the interesting subleading source information escapes every fixed interior of the square-free energy ball and is forced toward a denominator scale growing with `H`. This is a genuine exponent-lattice statement, not merely a change of notation for the singular-series Euler product.

## 1. Poisson summation isolates each Ramanujan denominator

The kernel (1) has the expansion

\[
K_\eta(x)
=\frac\pi6x^4
-\frac{\pi\eta}{6}|x|^7
+O_\eta(x^{10})
\qquad(x\to0).
\tag{11}
\]

It therefore has seven weak derivatives in `L^1(R)`, while all derivatives needed below decay exponentially at infinity. In particular,

\[
\widehat K_\eta(\xi)
=O_\eta((1+|\xi|)^{-7}).
\tag{12}
\]

For a single Ramanujan denominator put

\[
B_{q,\eta}(H)
:=\frac1H\sum_{h\in\mathbb Z}
K_\eta(h/H)c_q(h).
\tag{13}
\]

Use the standard divisor formula

\[
c_q(h)=\sum_{r\mid(q,h)}r\,\mu(q/r).
\tag{14}
\]

Since the sums in (13) are absolutely convergent, insert (14), write `h=rk`, and apply Poisson summation to the scaled kernel. This gives the exact identity

\[
\boxed{
B_{q,\eta}(H)
=
\sum_{r\mid q}\mu(q/r)
\sum_{m\in\mathbb Z}
\widehat K_\eta(Hm/r).
}
\tag{15}
\]

For `q>1`, the zero Fourier mode cancels because

\[
\sum_{r\mid q}\mu(q/r)=0.
\tag{16}
\]

If additionally `q<=H`, then `H/r>=1` for every divisor `r|q`, and (12) yields

\[
|B_{q,\eta}(H)|
\ll_\eta
H^{-7}\sum_{r\mid q}r^7
\ll_\eta H^{-7}q^7.
\tag{17}
\]

This is the key cancellation. It does not use RH, Hardy--Littlewood, pair correlation, or an interchange of the critical Ramanujan endpoint. It is an exact consequence of the declared cubic test, the Ramanujan divisor identity, and Poisson summation.

For `q=1`, there is no Möbius cancellation. Equation (15) becomes

\[
B_{1,\eta}(H)
=\sum_{m\in\mathbb Z}\widehat K_\eta(Hm)
=\widehat K_\eta(0)+O_\eta(H^{-7})
=2W_{1,\eta}+O_\eta(H^{-7}).
\tag{18}
\]

Because `K_eta(0)=0` and both `K_eta` and `c_q` are even,

\[
A_{\eta,\le Q}^{[2]}(H)
=\frac12
\sum_{q\le Q}
\frac{\mu(q)^2}{\phi(q)^2}
B_{q,\eta}(H).
\tag{19}
\]

Combining (17)--(19) gives

\[
A_{\eta,\le Q}^{[2]}(H)-W_{1,\eta}
\ll_\eta
H^{-7}
\sum_{2\le q\le Q}
\frac{q^7}{\phi(q)^2}.
\tag{20}
\]

The elementary bound

\[
\frac q{\phi(q)}\ll\log\log(3q)
\tag{21}
\]

then gives

\[
\sum_{q\le Q}\frac{q^7}{\phi(q)^2}
=
\sum_{q\le Q}q^5\left(\frac q{\phi(q)}\right)^2
\ll Q^6\{\log\log(3Q)\}^2,
\tag{22}
\]

which proves (5).

## 2. The endpoint is a filtered square-free spectral measure

`PL-405` already identified the regulated Ramanujan covariance

\[
\mathfrak S_\delta(h)
=
\sum_{q\ge1}
\frac{\mu(q)^2}{\phi(q)^2q^{2\delta}}c_q(h),
\qquad \delta>0.
\tag{23}
\]

It is useful to package this as the positive atomic measure on the additive torus

\[
\nu_\delta
:=
\sum_{q\ge1}
\frac{\mu(q)^2}{\phi(q)^2q^{2\delta}}
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
\delta_{a/q}.
\tag{24}
\]

Its Fourier coefficients are exactly

\[
\widehat\nu_\delta(h)=\mathfrak S_\delta(h),
\tag{25}
\]

while its total mass is the divergent endpoint energy from `PL-405`,

\[
\nu_\delta(\mathbb T)
=
\sum_{q\ge1}
\frac{\mu(q)^2}{\phi(q)q^{2\delta}}
\sim\frac1{2\delta}
\qquad(\delta\downarrow0).
\tag{26}
\]

The regulator itself is geometric in prime-exponent coordinates:

\[
q^{-2\delta}
=
\exp\!\left(
-2\delta\langle v(q),(\log p)_p\rangle
\right).
\tag{27}
\]

Thus `nu_delta` is a Gibbs-damped square-free exponent-lattice measure pushed to rational additive characters.

Define the periodized cubic Fourier filter

\[
\mathcal W_{\eta,H}(\alpha)
:=
\sum_{m\in\mathbb Z}
\widehat K_\eta(H(\alpha+m)).
\tag{28}
\]

Poisson summation gives

\[
\mathcal W_{\eta,H}(\alpha)
=
\frac1H\sum_{h\in\mathbb Z}
K_\eta(h/H)e^{-2\pi i h\alpha}.
\tag{29}
\]

Hence, for every fixed `delta>0`, the regulated model source has the exact spectral form

\[
\boxed{
A_{\eta,\delta}^{[2]}(H)
=
\frac12\int_{\mathbb T}
\mathcal W_{\eta,H}(\alpha)\,d\nu_\delta(\alpha).
}
\tag{30}
\]

The filter has zero Haar mean,

\[
\int_{\mathbb T}\mathcal W_{\eta,H}(\alpha)\,d\alpha
=\frac{K_\eta(0)}H=0,
\tag{31}
\]

while

\[
\mathcal W_{\eta,H}(0)
=2W_{1,\eta}+O_\eta(H^{-7})>0
\tag{32}
\]

for large `H`; it is therefore necessarily sign-changing. The endpoint mass in (26) diverges, but the cubic observable tests it with an exactly zero-mean signed filter. This explains in spectral language the diagonal-energy projection already found in `PL-406`.

There is a stronger local statement behind that cancellation. From (11) and Fourier inversion,

\[
\int_{\mathbb R}\xi^j\widehat K_\eta(\xi)\,d\xi=0
\qquad(0\le j\le3),
\tag{33}
\]

and

\[
\int_{\mathbb R}\xi^4\widehat K_\eta(\xi)\,d\xi
=
\frac1{4\pi^3}.
\tag{34}
\]

Thus the exact `PL-404` test is a fourth-order spectral contrast on smooth backgrounds. This does **not** by itself yield an arithmetic power saving, because the prime spectral measure varies on an `X`-dependent fine scale; it only identifies what the declared kernel cancels automatically.

## 3. What the moving boundary means for the live source bridge

For a finite real arithmetic sequence `f`, let

\[
F_f(\alpha)=\sum_n f(n)e^{2\pi i n\alpha},
\qquad
\mu_f(d\alpha)=|F_f(\alpha)|^2d\alpha.
\tag{35}
\]

The exact Fourier identity of `PL-406` may then be written

\[
\frac1{2H}
\sum_{h\in\mathbb Z}
K_\eta(h/H)C_f(h)
=
\frac12\int_{\mathbb T}
\mathcal W_{\eta,H}(\alpha)\,d\mu_f(\alpha),
\tag{36}
\]

with the normalization of `mu_f` adjusted by `1/X` in the prime application. Equation (30) gives the corresponding regulated Ramanujan model measure.

The live `PL-405`--`PL-407` replacement problem can therefore be viewed as **one filtered spectral-measure comparison at an infinite-energy endpoint**, not as convergence of the whole measures. A sufficient route would control, after the already-recorded interval-boundary and `Lambda_1 -> Lambda` alignments,

\[
\int_{\mathbb T}\mathcal W_{\eta,H}\,
 d\left(X^{-1}\mu_{\Lambda_1,X}-\nu_{\delta(H)}\right)
=o(H^{-7/4})
\tag{37}
\]

together with removal of the Ramanujan regulator at the same scale. Neither statement is proved here.

Equation (5) adds a useful localization to this formulation. The low-energy square-free interior is too smooth for the cubic contrast. In particular, merely approximating the critical Ramanujan source by a fixed or slowly growing list of local denominators cannot see the first deterministic correction, much less the zero-sensitive layer. Any successful arithmetic bridge has to control the moving rational-frequency boundary rather than only finitely many Euler/Ramanujan channels.

This matches the live fork in `PL-407`: either obtain a source-subtracted prime-variance theorem with enough power saving, or exploit the sign of the one forced spectral multiplier directly. The present result says where that signed multiplier is looking on the model side.

## 4. Prior-art and novelty audit

The ingredients are classical and are **not** claimed as new:

- the Ramanujan expansion of the modified von Mangoldt function and the coefficient-square singular-series spectrum are classical; Gadiyar and Padma, “Ramanujan-Fourier series and the conjecture D of Hardy and Littlewood,” *Czechoslovak Mathematical Journal* **64** (2014), 251--267, DOI `10.1007/s10587-014-0098-5`, explicitly use this spectrum and identify the unjustified endpoint interchange in the heuristic prime-pair argument;
- Ramanujan's divisor formula, Poisson summation, and Fourier moment identities are standard;
- the prime-short-interval variance / zero-pair-correlation bridge is classical. Languasco--Perelli--Zaccagnini, “Explicit relations between pair correlation of zeros and primes in short intervals,” *Journal of Mathematical Analysis and Applications* **394** (2012), 761--771, DOI `10.1016/j.jmaa.2012.04.058`, gives a quantitative Goldston--Montgomery transfer and the standard smooth-kernel Fourier machinery used in this sector;
- rigorous Parseval-type shifted-convolution theorems for suitably decaying Ramanujan expansions are established prior art, e.g. Murty--Saha, *Journal of Number Theory* **156** (2015), 125--134, DOI `10.1016/j.jnt.2015.04.026`.

Targeted searches around smooth Ramanujan truncation, Poisson summation, cubic kernels, and the numerical threshold `7/8` found these general ingredients and neighboring correlation theory but no prior statement of the line-specific estimate (5), its `H^{-1}`/`H^{-7/4}` consequences, or the interpretation of the exact `PL-404` cubic filter as forcing the zero-sensitive source toward a moving square-free exponent-energy boundary. The safe novelty claim is only this **derived localization for the already-fixed Mathia kernel and scale**, not a new theorem about Ramanujan expansions in general.

## 5. Adversarial audit and boundaries

1. **`7/8` is not a sharp arithmetic barrier.** It follows from the robust but crude decay `widehat K_eta(xi)=O(|xi|^-7)` and absolute summation in `q`. Sharper use of the exact transform, cancellation between denominators, or another admissible kernel could move this number.

2. **The statement localizes the model spectrum, not the actual primes.** Equations (5)--(9) are exact for the truncated singular-series/Ramanujan model. Transferring them to the finite prime spectrum is precisely the unresolved arithmetic bridge.

3. **No joint `delta-H` endpoint theorem is proved.** `PL-405` proves regulator removal for fixed `H`; (30) repackages the regulated source exactly but does not make that convergence uniform as `H -> infinity`.

4. **The zero Haar mean does not guarantee prime cancellation.** A signed filter can pair strongly with structured spectral spikes. Equation (31) removes flat background only; the required `o(H^-7/4)` estimate in (37) remains a genuine arithmetic statement.

5. **Finite-window boundary terms remain a gate.** The correlation measure in (36) is exact for the chosen finite support. A standard sharp-cutoff prime variance must still be aligned with the asymmetric `n<=X, n+d` source used upstream, as already recorded in `PL-407`.

6. **The full endpoint measure does not exist as a finite positive measure.** Equation (26) is the point: total mass diverges as `delta -> 0`. The meaningful object here is the filtered endpoint functional, not weak convergence of `nu_delta` to a finite measure.

7. **No RH implication is added.** `PL-404` already contains the model-level RH-equivalent asymptotic. The present finding identifies where its subleading information resides in prime-exponent/Ramanujan energy, but does not prove the prime-to-model replacement needed for an intrinsic arithmetic criterion.

## Consequence for the line

The current source bridge is more localized than `PL-407` alone suggests. On the model side, the forced cubic filter annihilates the zero Fourier mode of every nontrivial fixed Ramanujan denominator and suppresses all square-free exponent vectors with

\[
\log q\le\kappa\log H
\]

by the quantitative law (7). The leading constant comes from `q=1`; the first deterministic correction already escapes every `kappa<1` interior, and information at the critical `H^{-7/4}` resolution escapes every `kappa<7/8` interior under the robust seventh-decay bound.

The next useful arithmetic target is therefore not a finite-prime or fixed-denominator approximation of the singular series. It is a theorem controlling the **moving rational-frequency boundary** sampled by `mathcal W_(eta,H)`, either through the signed prime variance / zero-pair machinery of `PL-406`--`PL-407` or through an equivalent direct estimate for the one filtered spectral discrepancy (37).