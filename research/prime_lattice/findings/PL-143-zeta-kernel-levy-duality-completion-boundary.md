# PL-143 — Native zeta-kernel infinite divisibility is universal; RH-sensitive Lévy positivity appears only after completion

## Claim

The Hedenmalm–Lindqvist–Seip zeta kernel has a strong positivity property that survives the complete-Pick obstruction of `PL-142`, but that property is **too universal to encode RH**. On the natural evaluation half-plane

`H = {s : Re(s)>1/2}`,

let

`K(s,u)=zeta(s+conj(u))`.

For every real `tau>0`, the analytic power

`K_tau(s,u)=zeta(s+conj(u))^tau`

is positive definite on `H`. Equivalently, the native zeta kernel is infinitely divisible in the standard kernel-power sense. Moreover,

`log K(s,u)=sum_(p,r>=1) p^(-r(s+conj(u)))/r`

is itself a positive-definite kernel and is supported, in prime-exponent coordinates, only on the prime-power axis rays `r e_p`. Mixed-prime exponent vectors appear only after exponentiating this logarithmic kernel.

On every vertical slice this kernel positivity becomes a classical probability law. If `sigma>1` and `a=sigma/2`, then

`K(a+it,a)/K(a,a)=zeta(sigma+it)/zeta(sigma)`

is the characteristic function of a compound-Poisson distribution with Lévy measure

`nu_sigma = sum_p sum_(r>=1) p^(-r sigma)/r * delta_(-r log p)`.

Thus the prime-power axis skeleton `r e_p` is pushed by the energy map

`E(v)=<v,(log p)_p>`

to the jump frequencies `r log p`. This is unconditional and uses only the absolutely convergent Euler-product region.

The RH-sensitive probabilistic mechanism occurs only after a qualitatively different operation: **global completion plus explicit-formula dualization**. Nakamura and Suzuki proved that a completed zeta screw/explicit-formula function `g_zeta(t)` satisfies

`RH <=> exp(g_zeta(t)) is the characteristic function of an infinitely divisible distribution on R`.

Under RH its Lévy measure is

`nu_zeta = sum_gamma m_gamma/gamma^2 * delta_(-gamma)`,

where `gamma` runs over the zeros of `xi(1/2-i z)` and is real under RH. Their exact zero expansion is

`g_zeta(t)=sum_gamma m_gamma (exp(-i gamma t)-1)/gamma^2`.

Hence the completed explicit formula converts the prime-power energy skeleton into a zero-frequency Lévy representation, and **critical-line localization is exactly what makes the zero-side jump locations real**. This is a mathematically substantive Fourier/probabilistic interpretation, but it is established prior art and is equivalent to RH rather than a proof of it.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/BOUNDARY` for any route of the form

`native Bohr/HLS zeta-kernel positivity or infinite divisibility -> RH`.

The surviving target is narrower: explain, directly from arithmetic/global structure, why the *completed* explicit-formula exponent has the required Lévy/negative-definiteness property. Native prime-torus kernel positivity cannot supply that implication because it is already unconditional and generic.

## Native kernel powers are positive for every positive exponent

For `w=s+conj(u)` with `Re(w)>1`, the Euler product is absolutely convergent and zero-free. Choose the analytic branch of `zeta(w)^tau` that is positive for real `w>1`. For every `tau>0`,

`zeta(w)^tau = prod_p (1-p^(-w))^(-tau)`.

The generalized binomial expansion gives

`(1-x)^(-tau)=sum_(k>=0) (tau)_k/k! * x^k`,

with `(tau)_k/k!>0`. Multiplying the local series yields the absolutely convergent Dirichlet expansion

`zeta(w)^tau = sum_(n>=1) d_tau(n)n^(-w)`,

where

`d_tau(n)=prod_p (tau)_(v_p(n))/v_p(n)! > 0`.

Therefore

`K_tau(s,u)=sum_(n>=1) d_tau(n)n^(-s-conj(u))`

is positive definite, because for any finite set `s_j in H` and coefficients `c_j`,

`sum_(j,k) c_j conj(c_k) K_tau(s_j,s_k)
 = sum_n d_tau(n) |sum_j c_j n^(-s_j)|^2 >= 0`.

This property is logically distinct from the complete Nevanlinna–Pick property rejected in `PL-142`. Complete-Pick requires a particular sign pattern in the reciprocal kernel coefficients; positive definiteness of every positive real power instead follows here from the positive Euler/binomial coefficients. Thus `PL-142` does not leave an RH-sensitive loophole merely by weakening “complete Pick” to “all positive powers remain kernels.” The weaker property is automatic.

Taking the logarithm in the same valid half-plane gives

`log zeta(w)=sum_p sum_(r>=1) p^(-r w)/r`.

Consequently

`L(s,u):=log K(s,u)=sum_(p,r>=1) (p^(-r s)/sqrt(r)) conj(p^(-r u)/sqrt(r))`

is itself positive definite, with feature map

`Phi(s)=(p^(-r s)/sqrt(r))_(p,r)`.

In exponent coordinates, every feature is indexed by

`v(p^r)=r e_p`.

No mixed vector such as `e_p+e_q` appears in `log K`. Those composite lattice points are generated only after exponentiation. This is the same prime-power-axis compression seen in the explicit-formula and Poisson–Newton findings, now at the level of the native HLS reproducing kernel.

## Vertical slices are classical compound-Poisson zeta distributions

Fix `sigma>1` and set `a=sigma/2>1/2`. Along the vertical HLS orbit,

`K(a+it,a)/K(a,a)=zeta(sigma+it)/zeta(sigma)`.

The logarithm is, still entirely inside `Re(s)>1`,

`log(zeta(sigma+it)/zeta(sigma))
 = sum_p sum_(r>=1) p^(-r sigma)/r * (exp(-i t r log p)-1)`.

This is already in compound-Poisson Lévy–Khintchine form. With the convention `hat(mu)(t)=int exp(i t lambda) mu(dlambda)`, its finite Lévy measure is

`nu_sigma(dlambda)=sum_p sum_(r>=1) p^(-r sigma)/r * delta_(-r log p)(dlambda)`.

The total mass is

`nu_sigma(R)=sum_(p,r) p^(-r sigma)/r = log zeta(sigma)<infinity`.

Thus the arithmetic geometry is exact:

`r e_p -> r log p -> -r log p as a Lévy jump`.

The result is classical probability theory. Nakamura and Suzuki explicitly recall that `Z_sigma(t)=zeta(sigma+it)/zeta(sigma)` is an infinitely divisible characteristic function for `sigma>1`, in fact compound Poisson. Earlier probability literature on the Riemann zeta distribution gives the same interpretation.

This observation also supplies a strong universality control. Replace the rational-prime energies `log p` by any positive independent energies `lambda_j` for which

`prod_j (1-exp(-lambda_j w))^(-1)`

converges. The logarithmic kernel is again

`sum_(j,r>=1) exp(-r lambda_j(s+conj(u)))/r`,

all positive powers of the kernel are positive definite, and every vertical slice is a compound-Poisson law with jumps `-r lambda_j`. Hence native kernel infinite divisibility is a feature of the free Euler-coordinate gas, not a rigidity specific to the rational primes or to RH.

## The completed RH-sensitive Lévy mechanism is different

Nakamura and Suzuki introduce an even real function `g_zeta(t)` built from the completed zeta explicit-formula data. Its arithmetic term contains the finite von-Mangoldt sum

`sum_(n<=exp(t)) Lambda(n)/sqrt(n) * (t-log n)`

for `t>=0`, together with the pole/archimedean completion terms. Since `Lambda(n)` is supported on prime powers, its non-archimedean support is again precisely

`n=p^r`,  `v(n)=r e_p`,  `log n=r log p`.

The essential distinction is that `g_zeta` is not obtained by pretending the Euler product converges in the critical strip. Nakamura–Suzuki prove the transform identity

`int_0^infinity g_zeta(t) exp(i z t) dt
 = z^(-2) * xi'/xi(1/2-i z)`

for `Im(z)>1/2`. In the appendix they use the Dirichlet expansion of `-zeta'/zeta` only where `Re(s)>1`, then combine it with the completed gamma/pole terms; the global zero representation is controlled by the entire Hadamard theory of `xi`.

They prove the exact expansion

`g_zeta(t)=sum_gamma m_gamma (exp(-i gamma t)-1)/gamma^2`,

where `gamma` ranges over zeros of `xi(1/2-i z)`, initially with no RH assumption and therefore potentially complex. Their Theorem 1.1 is the equivalence

`RH <=> exp(g_zeta(t)) is an infinitely divisible characteristic function`.

Under RH all `gamma` are real, and Theorem 1.2 identifies the Lévy measure as

`nu_zeta(dlambda)=sum_gamma m_gamma/gamma^2 * delta_(-gamma)(dlambda)`.

The sum of `m_gamma/gamma^2` converges, so this is a compound-Poisson distribution. Pairing the symmetric zeros `gamma` and `-gamma` gives, under RH,

`g_zeta(t)=2 sum_(gamma>0) m_gamma (cos(gamma t)-1)/gamma^2 <= 0`.

This supplies the exact spectral/probabilistic interpretation sought by the research mandate: on the prime side, the completed function is assembled from prime-power energy thresholds plus archimedean data; on the dual side, the zero ordinates become Lévy jump frequencies. The critical line is singled out because a Lévy measure on the real line can only place mass at **real** jump locations. Off RH the corresponding `gamma` leave the real axis, and the representation no longer defines such a positive real Lévy measure.

The converse in Nakamura–Suzuki is not merely the observation that nonreal atoms are illegal. From infinite divisibility they obtain the sign/analytic properties of `g_zeta`; the Fourier–Laplace identity with `xi'/xi` then excludes zeros of `xi(1/2-i z)` off the real axis. Thus the equivalence is rigorous, but it does not independently establish the needed infinite divisibility.

## Analytic-continuation and positivity boundary

The native zeta kernel itself cannot simply be meromorphically continued into the critical strip while retaining positive definiteness. On the diagonal,

`K(s,s)=zeta(2 Re(s))`.

For `0<Re(s)<1/2`, one has `0<2 Re(s)<1` and

`zeta(2 Re(s))<0`.

A positive-definite kernel must have a nonnegative diagonal, so the meromorphic scalar continuation of `zeta(s+conj(u))` already fails this elementary test immediately to the left of the HLS boundary. At `Re(s)=1/2`, the diagonal hits the pole `zeta(1)`.

Therefore the unconditional infinite-divisibility statement has a sharp domain limitation:

`native HLS/Bohr kernel positivity: Re(s),Re(u)>1/2`,

with the Euler/logarithmic series used only when `Re(s+conj(u))>1`.

The RH-sensitive completed object is a different construction. It crosses the Euler-product boundary using the completed `xi` function, the explicit formula, and Hadamard/transform identities. No statement here extends the prime Euler product formally into `Re(s)<=1`.

## Prior art and novelty audit

Primary sources:

- **Håkan Hedenmalm, Peter Lindqvist, Kristian Seip**, “A Hilbert space of Dirichlet series and systems of dilated functions in L2(0,1),” *Duke Mathematical Journal* **86** (1997), 1–37. This is the standard HLS Dirichlet-series Hilbert space whose evaluation kernel is `zeta(s+conj(u))` on `Re(s)>1/2`; it is baseline prior art for the research line.
- **Takashi Nakamura, Masatoshi Suzuki**, “On infinitely divisible distributions related to the Riemann hypothesis,” *Statistics & Probability Letters* **201** (2023), 109889, DOI `10.1016/j.spl.2023.109889`, arXiv:`2306.08317`. Theorem 1.1 proves `RH <=> exp(g_zeta)` is an infinitely divisible characteristic function; Theorem 1.2 gives the zero-supported Lévy measure under RH; equation (1.7) and Lemma 2.2 give the zero expansion and Fourier–Laplace transform. The paper also recalls the classical compound-Poisson law `zeta(sigma+it)/zeta(sigma)` for `sigma>1`.
- **Takashi Nakamura**, “A complete Riemann zeta distribution and the Riemann hypothesis,” *Bernoulli* **21** (2015), 604–617, DOI `10.3150/13-BEJ581`, arXiv:`1504.03438`. This is earlier probability-theoretic prior art connecting completed zeta characteristic functions and RH; its “pretended infinitely divisible” formulation is distinct from the later exact infinitely-divisible criterion above.
- **Takashi Nakamura, Masatoshi Suzuki**, “A probabilistic interpretation for central zeros of L-functions in the Selberg class,” arXiv:`2307.02027` (submitted 2023; version dated 22 March 2026). It generalizes the probabilistic/infinitely-divisible viewpoint to `L`-functions in the Selberg class. This is an important control against interpreting the completed Lévy mechanism as unique to the rational-prime exponent lattice.

No theorem of Nakamura or Suzuki is claimed as new. The derivations that `K^tau` is positive definite for all `tau>0`, that `log K` has feature support only on `r e_p`, and that the classical zeta-distribution Lévy measure is the pushforward of those axis rays under `v -> <v,log p>` are elementary syntheses from the absolutely convergent Euler product. A targeted repository audit found no earlier `PL-*` finding centered on this native-kernel infinite-divisibility versus completed-Lévy distinction. The closest stored findings are `PL-120` (Suzuki’s unconditional screw Hilbert space versus RH-equivalent Weil-metric identification), `PL-124` (Poisson–Newton trace universality and prime-power-axis compression), and `PL-142` (failure of the native zeta kernel to be complete Pick).

The relationship to those findings is deliberately non-duplicative. `PL-124` shows that an exact prime-frequency-to-divisor trace formula is universal and does not force localization. `PL-120` shows that an unconditional positive completed Hilbert norm can exist while the correct zero-sensitive metric identification remains RH-equivalent. The present finding shows an analogous and sharper boundary at the **probabilistic kernel level**: the uncompleted/native prime-torus kernel is infinitely divisible automatically, while the corresponding positivity after global completion is already an exact RH-equivalent criterion.

## Boundaries and falsification

1. **Native infinite divisibility does not prove RH.** It holds for every `tau>0` in the HLS half-plane and for generic independent Euler-coordinate systems. It never reaches the zero-containing critical strip.

2. **The completed criterion is not a proof of RH.** Proving that `exp(g_zeta)` is infinitely divisible without using zero localization would prove RH. Nakamura–Suzuki establish the equivalence, not the missing arithmetic positivity theorem.

3. **The logarithmic kernel sees only prime-power axes.** Mixed exponent vectors are present in `zeta(w)^tau`, but they are combinatorial products of the axis-ray contributions. No irreducible mixed-prime interaction appears in `log K`.

4. **Analytic continuation is kept separate from Euler convergence.** Every Euler/binomial/logarithmic expansion above is restricted to `Re(s+conj(u))>1`. The completed `g_zeta` identities use the analytically continued/completed `xi` machinery.

5. **The Selberg-class extension is a matched control.** The RH-sensitive Lévy architecture is tied to global `L`-function completion and explicit-formula structure, not uniquely to the bare rational-prime torus. A future `prime_lattice` claim must explain what extra rational-prime geometry adds beyond this general mechanism.

6. **A surviving escape remains possible.** A genuinely new result could prove the conditional-negative-definiteness/Lévy positivity of the completed `g_zeta` directly from arithmetic, or identify an additional full-lattice law that forces it. This finding does not rule that out; it records that both the native positive kernel and the completed RH-equivalent probabilistic formulation are already known or immediate consequences of known structure.

## Consequence for the research line

`PL-142` might suggest weakening the failed complete-Pick program to a broader positive-kernel property. This finding closes the most canonical such weakening. The zeta kernel is already as positive as one could ask with respect to positive real powers, and its vertical restrictions are already infinitely divisible compound-Poisson laws. That positivity is nevertheless confined to the absolute-convergence half-plane and survives generic replacement of the rational-prime energies.

The interesting transition occurs only after the global completion has mixed the non-archimedean prime-power skeleton with the archimedean/pole data and the explicit formula has dualized it to the zero divisor. There the same probabilistic language becomes RH-sensitive:

`prime-power completed explicit-formula data -> g_zeta -> real Lévy jump spectrum of zeros`

is valid exactly when the nontrivial zeros lie on the critical line.

Accordingly, further work should not treat “infinite divisibility of a Bohr/zeta kernel” as evidence for RH. The viable question is the missing global rigidity theorem: **what arithmetic principle could force the completed explicit-formula exponent `g_zeta` to be a Lévy–Khintchine exponent without first assuming the reality of the zero frequencies?** That is the same hard positivity/polarization gap seen from a precise probabilistic angle, and it is the part not supplied by the bare exponent lattice.