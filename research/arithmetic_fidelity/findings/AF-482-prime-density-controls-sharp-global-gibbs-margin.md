# AF-482 — Prime density controls the sharp global Gibbs margin

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INPUT`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `GLOBAL-FIDELITY`, `MATCHED-CONTROL`, `BOUNDARY-CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-481 showed that the local `1/log` collapse of the canonical Hilbert margin for the rational-prime Gibbs curve is already forced by the coarse counting law

\[
N_Q(x)\sim \frac{x}{\log x}.
\]

The same is true of the **sharp anchored global half-line margin**.

Let

\[
Q=\{q_1<q_2<\cdots\}\subset(1,\infty)
\]

be any discrete sequence with

\[
N_Q(x):=\#\{q\in Q:q\le x\}
\sim \frac{x}{\log x}.
\tag{1}
\]

For `sigma>1`, define

\[
P_Q(\sigma)=\sum_{q\in Q}q^{-\sigma},
\qquad
\mu^Q_\sigma(q)=\frac{q^{-\sigma}}{P_Q(\sigma)},
\qquad
H(\mu)=\sqrt2\,\mu\in\ell^2(Q).
\tag{2}
\]

For an anchor `sigma_0>1`, let

\[
c_Q(\sigma_0)
:=
\inf_{\sigma_0\le\sigma<\tau}
\frac{
\|H(\mu^Q_\sigma)-H(\mu^Q_\tau)\|_2
}{
\|\mu^Q_\sigma-\mu^Q_\tau\|_1
}.
\tag{3}
\]

Then

\[
\boxed{
P_Q(\sigma_0)c_Q(\sigma_0)
\longrightarrow
\sqrt{\frac{P_Q(2)}2}
\qquad (\sigma_0\downarrow1).
}
\tag{4}
\]

Since AF-481 gives

\[
P_Q(1+\varepsilon)\sim\log\frac1\varepsilon,
\tag{5}
\]

this is equivalently

\[
\boxed{
c_Q(1+\varepsilon)
\sim
\frac{\sqrt{P_Q(2)/2}}
     {\log(1/\varepsilon)}.
}
\tag{6}
\]

Thus the AF-480 prime theorem is not merely locally density-generic. Under `(1)`, the exact asymptotic of the **worst pair anywhere on the anchored half-line** is already forced by first-order prime-scale density together with the canonical coordinate geometry.

In particular, the shifted-composite control

\[
Q_+=\{p+1:p\ge3\text{ prime}\}
\]

and the smooth pseudo-prime control

\[
Q_{\rm sm}=\{n\log n:n\ge2\}
\]

inherit the same sharp global law with their respective values of `P_Q(2)`.

The Arithmetic Fidelity consequence is stronger than AF-481:

\[
\boxed{
\text{even the sharp global anchored Gibbs-conditioning collapse detects the density class, not rational primality.}
}
\tag{7}
\]

Any prime-specific discriminator must therefore enter through structure finer than the counting law `(1)`, the Gibbs one-crossing order, and the resulting global canonical Hilbert margin.

## Exact derivation

Write

\[
A=P_Q(\sigma),\qquad
B=P_Q(\tau),\qquad
h=\tau-\sigma,\qquad
\Delta=A-B>0.
\tag{8}
\]

AF-478 applies to every fixed anchored half-line because `(1)` gives finite partition function and first logarithmic moment at every `sigma>1`. The additional issue here is to determine the **sharp degeneration of the best global constant as the anchor approaches `1`**.

### Exact one-crossing estimates

For `\tau>\sigma`,

\[
\frac{\mu^Q_\tau(q)}{\mu^Q_\sigma(q)}
=
\frac AB q^{-h},
\tag{9}
\]

which is strictly decreasing in `q`. Therefore

\[
d_q:=\mu^Q_\tau(q)-\mu^Q_\sigma(q)
\tag{10}
\]

has one sign crossing. On its positive block,

\[
0<d_q
=\mu^Q_\tau(q)
\left(1-\frac BA q^h\right)
\le
\mu^Q_\tau(q)\frac\Delta A.
\tag{11}
\]

Since the positive and negative Jordan parts have equal `ell^1` mass,

\[
\boxed{
\|\mu^Q_\tau-\mu^Q_\sigma\|_1
\le \frac{2\Delta}{A}.
}
\tag{12}
\]

For each fixed coordinate one also has the exact identity

\[
d_q
=
\frac{q^{-\sigma}\Delta}{AB}
\left[
1-
\frac{A(1-q^{-h})}{\Delta}
\right].
\tag{13}
\]

The only question is therefore whether, uniformly over all pairs approaching the singular boundary, the correction term in brackets disappears on every fixed finite coordinate set.

### Density alone gives the required uniform boundary control

Set

\[
\sigma=1+\varepsilon,
\qquad
\tau=1+\delta,
\qquad
0<\varepsilon<\delta\le\eta,
\tag{14}
\]

and write

\[
L=\log\frac1\varepsilon,
\qquad
r=\log\frac\delta\varepsilon.
\tag{15}
\]

AF-481 derived from `(1)` the Abelian asymptotics

\[
P_Q(1+u)\sim\log\frac1u,
\qquad
-P_Q'(1+u)\sim\frac1u
\qquad (u\downarrow0).
\tag{16}
\]

Because these are ordinary limits, they hold uniformly over the full sufficiently small tail `0<u<=eta`. Hence

\[
\Delta
=
\int_\varepsilon^\delta
-P_Q'(1+u)\,du
\ge
(1-o_\eta(1))r,
\tag{17}
\]

and

\[
A\le(1+o_\eta(1))L.
\tag{18}
\]

Consequently

\[
\frac{Ah}{\Delta}
\le
(1+o_\eta(1))
\frac{L(\delta-\varepsilon)}r.
\tag{19}
\]

The last quantity tends to zero **uniformly** over `0<epsilon<delta<=eta`. Indeed, if `r>=L/2`, then

\[
\frac{L(\delta-\varepsilon)}r
\le2(\delta-\varepsilon)
\le2\eta.
\tag{20}
\]

If `r<L/2`, put `D=log(1/delta)=L-r>L/2`, so `L<2D`. Also

\[
r=\int_\varepsilon^\delta\frac{du}{u}
\ge\frac{\delta-\varepsilon}{\delta},
\tag{21}
\]

and therefore, for sufficiently small `eta`,

\[
\frac{L(\delta-\varepsilon)}r
\le2\delta\log\frac1\delta
\le2\eta\log\frac1\eta.
\tag{22}
\]

Thus

\[
\boxed{
\sup_{0<\varepsilon<\delta\le\eta}
\frac{P_Q(1+\varepsilon)(\delta-\varepsilon)}
     {P_Q(1+\varepsilon)-P_Q(1+\delta)}
\longrightarrow0
\qquad(\eta\downarrow0).
}
\tag{23}
\]

For fixed `q`, `1-q^{-h}<=h\log q`, so `(23)` gives

\[
\sup_{0<\varepsilon<\delta\le\eta}
\frac{A(1-q^{-h})}{\Delta}
\longrightarrow0.
\tag{24}
\]

The convergence is uniform over every fixed finite set `F subset Q`.

### Fixed coordinates force the sharp global lower bound near the boundary

Let `F subset Q` be finite. Combining `(13)` and `(24)`, uniformly over the boundary pairs `(14)`,

\[
\left(\sum_{q\in F}d_q^2\right)^{1/2}
=
\frac{\Delta}{AB}
\left(
\sqrt{\sum_{q\in F}q^{-2}}
+o_{F,\eta}(1)
\right),
\tag{25}
\]

where `o_{F,eta}(1)->0` as `eta->0`. Together with `(12)`,

\[
\frac{
\sqrt2\,\|\mu^Q_\tau-\mu^Q_\sigma\|_2
}{
\|\mu^Q_\tau-\mu^Q_\sigma\|_1
}
\ge
\frac1B
\left(
\sqrt{\frac12\sum_{q\in F}q^{-2}}
+o_{F,\eta}(1)
\right).
\tag{26}
\]

If `sigma>=sigma_0`, then `B=P_Q(tau)<=P_Q(sigma_0)`. Hence every pair with `tau<=1+eta` satisfies

\[
P_Q(\sigma_0)
\frac{
\sqrt2\,\|\mu^Q_\tau-\mu^Q_\sigma\|_2
}{
\|\mu^Q_\tau-\mu^Q_\sigma\|_1
}
\ge
\sqrt{\frac12\sum_{q\in F}q^{-2}}
+o_{F,\eta}(1).
\tag{27}
\]

### Pairs away from the singular boundary cannot minimize at the `1/P_Q(sigma_0)` scale

Fix `eta>0`. If `sigma>=1+eta/2`, AF-478 applied with anchor `1+eta/2` gives a positive lower Hilbert/TV constant depending only on `eta`, not on `sigma_0`.

It remains to consider

\[
\sigma<1+\eta/2,
\qquad
\tau\ge1+\eta.
\tag{28}
\]

The lowest-coordinate mass

\[
\mu^Q_u(q_1)=\frac{q_1^{-u}}{P_Q(u)}
\tag{29}
\]

is strictly increasing in `u`, since

\[
\frac d{du}\log\mu^Q_u(q_1)
=m_Q(u)-\log q_1>0
\tag{30}
\]

for the nondegenerate infinite support `Q`. Therefore `(28)` gives the fixed positive coordinate gap

\[
\mu^Q_\tau(q_1)-\mu^Q_\sigma(q_1)
\ge
\mu^Q_{1+\eta}(q_1)-\mu^Q_{1+\eta/2}(q_1)
=:\gamma_\eta>0.
\tag{31}
\]

Since the `ell^1` distance between probability vectors is at most `2`, the ratio in `(3)` is at least `gamma_eta/sqrt2` on these pairs. Thus all pairs with `tau>=1+eta` have a lower bound `k_eta>0` independent of `sigma_0`.

But `P_Q(sigma_0)->infinity` as `sigma_0 downarrow1`. Hence such pairs are asymptotically much better conditioned than the `1/P_Q(sigma_0)` boundary scale and cannot control the limiting infimum.

Combining this observation with `(27)`, first letting `sigma_0 downarrow1`, then `eta downarrow0`, gives

\[
\liminf_{\sigma_0\downarrow1}
P_Q(\sigma_0)c_Q(\sigma_0)
\ge
\sqrt{\frac12\sum_{q\in F}q^{-2}}.
\tag{32}
\]

Finally let the finite sets `F` increase to `Q`. Since `(1)` implies `P_Q(2)<infinity`, monotone convergence yields

\[
\boxed{
\liminf_{\sigma_0\downarrow1}
P_Q(\sigma_0)c_Q(\sigma_0)
\ge
\sqrt{\frac{P_Q(2)}2}.
}
\tag{33}
\]

### Local tangent pairs give the matching upper bound

For each fixed anchor, pairs with `tau downarrow sigma=sigma_0` are admissible in `(3)`. Therefore

\[
c_Q(\sigma_0)\le\rho_Q(\sigma_0),
\tag{34}
\]

where `rho_Q` is AF-481's local tangent ratio. AF-481 proved

\[
P_Q(\sigma)\rho_Q(\sigma)
\longrightarrow
\sqrt{\frac{P_Q(2)}2}.
\tag{35}
\]

Equations `(33)`--`(35)` prove `(4)` and `(6)`.

## What changed relative to AF-480 and AF-481

AF-480 proved `(4)` for the rational primes using the sharper prime-zeta boundary expansion. AF-481 then showed that only the **local tangent asymptotic** follows from the much weaker source assumption `(1)`, and deliberately left the global anchored asymptotic open.

The uniform estimate `(23)` closes that gap. It shows that the first-order Abelian data already supplied by `(1)` are enough to synchronize all fixed coordinates uniformly over every near-boundary secant. AF-478 then excludes remote secants from becoming competitive with the collapsing boundary scale.

So the dependency is now precise:

\[
N_Q(x)\sim x/\log x
\Longrightarrow
\text{partition singularity + derivative singularity}
\Longrightarrow
\text{uniform fixed-coordinate boundary transport}
\Longrightarrow
\text{sharp global anchored margin}.
\tag{36}
\]

No rational-prime multiplicative relation enters this chain.

## Matched-control audit

The controls from AF-481 now falsify a stronger arithmetic interpretation.

For `Q_+={p+1:p>=3 prime}`, every element is an ordinary composite, while `N_{Q_+}(x)~x/log x`. Therefore

\[
P_{Q_+}(\sigma_0)c_{Q_+}(\sigma_0)
\to\sqrt{P_{Q_+}(2)/2}.
\tag{37}
\]

For `Q_sm={n log n:n>=2}`, the generator rule contains no prime-membership predicate at all, yet its counting law has the same asymptotic and therefore

\[
P_{Q_{\rm sm}}(\sigma_0)c_{Q_{\rm sm}}(\sigma_0)
\to\sqrt{P_{Q_{\rm sm}}(2)/2}.
\tag{38}
\]

Hence neither the existence of a global one-crossing Hilbert margin, its collapse to zero at the singular boundary, the `1/log` rate, nor the sharp normalization by `P_Q(sigma_0)` distinguishes rational primes from these controls.

The residual constant `P_Q(2)` still depends on the exact fixed generator locations. That detail is not erased, but it is a square-summable coordinate statistic rather than evidence that the rational-prime multiplicative structure survived.

## Prior art and novelty audit

The proof combines classical ingredients and makes **no novelty claim** for monotone-likelihood-ratio families, Abelian/regular-variation asymptotics, or generalized-prime density theory.

- Samuel Karlin and Herman Rubin, **“Distributions Possessing a Monotone Likelihood Ratio,”** *Journal of the American Statistical Association* 51(276), 637--643 (1956), DOI `10.1080/01621459.1956.10501355`, is classical prior art for the monotone-likelihood-ratio/single-crossing structure used in `(9)`--`(12)`.
- N. H. Bingham, C. M. Goldie, and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), is standard prior art for the Abelian/Tauberian passage from counting laws to Laplace/Stieltjes-transform asymptotics such as `(16)`.
- Arne Beurling, **“Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I,”** *Acta Mathematica* 68 (1937), 255--291, is the natural classical boundary for generalized prime-density controls.
- AF-478 and AF-481 already isolate the two reusable ingredients used here: global one-crossing secant control on a fixed half-line and the density-generic boundary asymptotics.

A targeted search across monotone-likelihood-ratio/exponential-family distance results, total variation versus `ell^2`, regular variation of partition functions, and generalized-prime systems found the component mechanisms as standard but did not identify this exact anchored sharp-margin asymptotic as a standard theorem. That search result is not evidence of novelty. The durable result here is the **matched-control consequence inside Arithmetic Fidelity**: the sharp global law previously proved for primes survives the whole density class `(1)`.

## Boundaries and falsification audit

- **The full asymptotic `(1)` is used.** In particular, `(23)` uses both `P_Q(1+u)~log(1/u)` and `-P_Q'(1+u)~1/u` uniformly on sufficiently small tails. Weaker limsup/liminf density information need not give the same sharp constant.
- **The theorem is specific to the canonical coordinate embedding.** It does not establish optimal Hilbert distortion over arbitrary nonlinear encodings.
- **The global infimum is asymptotically boundary-localized.** AF-478 is load-bearing only to show that pairs staying a fixed distance from `1` retain a positive margin. The sharp constant comes from the singular boundary.
- **The fixed-coordinate argument is not a reconstruction theorem.** It proves a metric lower bound by retaining enough low-coordinate mass in the secant. It does not recover the full generator sequence from the compressed Hilbert point.
- **The constant `P_Q(2)` is sequence-dependent.** The theorem universalizes the mechanism and normalized asymptotic, not every numerical detail. Controls matched at the stronger `P_Q(2)` layer would be needed to erase even that scalar residue.
- **No multiplicative-semigroup data enter the proof.** A later discriminator based on products, divisibility, Euler structure, prime powers, or correlations beyond the one-point counting law is not ruled out.
- **No RH implication is obtained.** The result is a negative selectivity audit: a seemingly sharp prime-derived global metric law is already reproduced by non-prime source systems.

## Research consequence

AF-481 left open whether rational primes might still be special at the level of the **global** sharp conditioning constant even though the local boundary rate was density-generic. AF-482 removes that possibility for the canonical Gibbs curve.

The next useful discriminator therefore has to be genuinely finer than first-order generator density. In particular, improving the precision of the same Gibbs normalization or studying the same one-crossing Hilbert margin cannot by itself recover rational-prime provenance: the complete boundary-minimization mechanism is already shared by broad matched controls.

A productive next gate is to identify a relational or multiplicative statistic that distinguishes the rational primes from `Q_+`, `Q_sm`, and Beurling-style density controls **before** applying a compression, and then test whether that statistic survives the intended transformation rather than being reduced again to the universal counting layer.