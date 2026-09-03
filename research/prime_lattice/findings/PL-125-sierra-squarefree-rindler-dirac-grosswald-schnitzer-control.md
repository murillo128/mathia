# PL-125 — Sierra already embeds the square-free exponent lattice in a self-adjoint Rindler Dirac family, but zero-preserving Euler deformations defeat exact-prime rigidity

## Claim

A particularly natural Hilbert–Pólya route for the `prime_lattice` program is already present in prior art much more literally than a generic prime-orbit analogy suggests. Germán Sierra's massless Rindler-Dirac model places semitransparent mirrors at lengths

`ell_n = sqrt(n)`

with reflection amplitudes

`rho_n = mu(n)/sqrt(n)`.

Because `mu(n)` vanishes off the square-free integers, the active mirrors are exactly the `{0,1}` sector of the prime-exponent lattice. For a square-free exponent vector `alpha=v(n)`,

`ell_alpha = exp((1/2)<alpha,(log p)_p>)`,

`rho_alpha = (-1)^|alpha| exp(-(1/2)<alpha,(log p)_p>)`.

Moreover the Rindler round-trip time from the boundary to the prime mirror `p` is exactly `log p`. Thus the model contains, simultaneously and non-metaphorically, the square-free Möbius orientation, the exponent-lattice energy map, the prime frequencies, a self-adjoint Dirac family, and a transfer/scattering mechanism.

This does **not** provide the missing RH rigidity. In Sierra's construction a critical zero becomes a normalizable eigenstate only after the self-adjoint boundary phase is tuned to that individual zero; Sierra explicitly states that this gives no single fixed Hamiltonian containing all zeros. The first derivation also uses `sum mu(n)n^(-s)=1/zeta(s)` on the critical line where the Dirichlet series need not converge. A later partial-sum/Perron analysis improves the analytic status but still leaves convergence/asymptotic control that Sierra says needs further analysis.

There is an even stronger matched control. Grosswald and Schnitzer proved that one may replace each prime `p_n` in the Euler product by a number `q_n` with `p_n <= q_n <= p_(n+1)` and obtain a modified function `zeta*(s)` which continues meromorphically to `Re(s)>0` and has **exactly the same zeros, with multiplicity, as zeta in that half-plane**. Sierra then constructs the analogous Rindler-Dirac model from the inverse coefficients `mu*(n)`. The `q_n` may be composite (Sierra gives `2,4,6,8,12,...` as an example), and `mu*` is no longer the canonical square-free Möbius function. Hence the same zero divisor can be transported into the same spectral architecture after destroying the exact rational-prime basis geometry.

**Evidence/status:** `LITERATURE+DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE` for the route

`canonical square-free exponent lattice + log-prime mirror periods + self-adjoint Dirac/transfer dynamics -> exact-prime geometry itself forces a global Hilbert–Pólya realization / RH`.

The finding is not a negative result about all Dirac, scattering, or Hilbert–Pólya programs. It rules out treating the mere presence of the exact square-free lattice, `log p` periods, and self-adjoint transfer dynamics as the missing localization mechanism. A surviving construction must add a global canonical law that cannot be preserved under the Grosswald–Schnitzer deformation and cannot be tuned zero by zero.

## Exact bridge from the square-free exponent lattice

Sierra's model is a massless Dirac fermion on a Rindler half-line with delta-function scatterers. The exact transfer-matrix setup is parametrized by mirror positions `ell_n`, reflection coefficients `rho_n`, and a real boundary parameter `vartheta` specifying a self-adjoint extension. In the transparent-mirror analysis he chooses

`ell_n = n^(1/2),    rho_n = mu(n)/n^(1/2)`.

Let `alpha=(alpha_p)_p` be square-free, so `alpha_p in {0,1}` and

`n_alpha = product_p p^(alpha_p)`.

Then

`log ell_alpha = (1/2) log n_alpha = (1/2)<alpha,(log p)_p>`

and

`mu(n_alpha)=(-1)^|alpha|`,

so

`rho_alpha = (-1)^|alpha| exp(-(1/2)<alpha,(log p)_p>)`.

This is stronger than saying that primes label periodic orbits. The **support** of the interaction is the square-free hypercube itself, the sign is its parity character, and the radial position is the exponent-lattice linear functional used throughout this research line.

The dynamical frequency match is equally exact. Sierra computes the proper-time lapse for a ray leaving the Rindler boundary, reflecting at `ell_n`, and returning:

`tau_n = 2 log(ell_n/ell_1)`.

With `ell_1=1` and `ell_p=sqrt(p)`,

`tau_p = log p`.

Thus the primitive prime direction `e_p` carries the period `<e_p,log q>=log p`. In logarithmic spatial coordinate `x=log rho`, the mirrors are at `x_n=(1/2)log n`, so the exponent lattice is projected directly onto the Rindler coordinate by the same energy map `alpha -> <alpha,log p>`.

This is therefore genuine prior art for a geometric/spectral realization of the canonical square-free prime lattice, not merely an analogy reconstructed after the fact.

## What the self-adjoint spectrum actually gives

For real `vartheta`, Sierra's Hamiltonian family is self-adjoint, so its genuine eigenvalues are real. In the transparent-mirror expansion the normalizability condition leads formally to

`1 ~ 2 epsilon exp(i vartheta) sum_n mu(n)n^(-1/2-iE)`.

Replacing the series by `1/zeta(1/2+iE)` suggests critical zeros as limiting bound states. Sierra is explicit that this step is heuristic: the Dirichlet identity

`sum_n mu(n)n^(-s) = 1/zeta(s)`

is being used where the series may fail to converge.

The same calculation yields the phase condition

`exp(2i(vartheta + theta(E_n))) = 1`

for a critical zero `1/2+iE_n`, with a refined sign term in the later treatment. Hence `vartheta` must depend on the chosen zero. Sierra states the consequence directly: this is a **local** spectral realization, not the global Pólya–Hilbert conjecture; within this family there is no single fixed boundary phase whose Hamiltonian contains all Riemann zeros.

That distinction is decisive for this research line. Self-adjointness proves reality of the spectrum of each already-chosen `H_vartheta`; it does not prove that the complete zeta divisor is the spectrum of one canonical operator. The target zero enters the operator through the boundary condition needed to make it an eigenvalue.

## Analytic-continuation audit

The critical-line use of the Möbius Dirichlet series in Sierra's first spectral argument cannot be promoted to an identity by analytic continuation. The series identity is valid in its ordinary convergence region, initially `Re(s)>1`, whereas the model needs `s=1/2+iE`.

Sierra recognizes this problem and later rewrites the analysis in terms of finite Möbius sums and Perron-type formulas. This is a genuine improvement: the global zeta function enters through contour/zero information rather than by pretending that the Euler product or reciprocal Dirichlet series converges on the critical line. But the resulting asymptotic argument still requires control of sums over zeros and related convergence assumptions. Sierra's conclusion explicitly says that the proposed RH-by-contradiction argument assumes convergence of mathematical series that requires more thorough analysis.

Accordingly this finding records the exact self-adjoint/transfer construction and the exact lattice embedding as prior art, but **does not** promote Sierra's proposed RH argument to a theorem.

## Grosswald–Schnitzer gives the matched falsification control

Grosswald and Schnitzer choose numbers `q_n` satisfying

`p_n <= q_n <= p_(n+1)`

and define, first for `Re(s)>1`,

`zeta*(s)=product_n (1-q_n^(-s))^(-1)`.

Their Theorem 1 proves that `zeta*` extends meromorphically to `Re(s)>0`, has the expected single pole at `1`, and has exactly the same zeros with exactly the same multiplicities as ordinary zeta in that half-plane. Their proof factors

`zeta*(s)=phi(s) zeta(s)`

with `phi` analytically continued and nonvanishing in `Re(s)>0`. Thus the equality of zero divisors is a theorem about the continued functions, not a formal manipulation of divergent Euler products.

The local data need not be the rational primes. Sierra notes, for example, an admissible integer sequence beginning

`2,4,6,8,12,...`.

Writing

`1/zeta*(s)=sum_n mu*(n)n^(-s)`,

he defines the analogous Rindler reflection amplitudes

`r_n=mu*(n)/sqrt(n)`

and applies the same Dirac construction. The coefficients are now representation-count differences for products of the `q_j`; they need not equal ordinary Möbius coefficients and may have magnitude greater than one. In Sierra's explicit example even nonsquare-free ordinary integers occur with nonzero coefficients.

So the deformation removes exactly the structure that looked most promising from the `prime_lattice` viewpoint:

- there is no longer a basis indexed by the actual rational primes;
- unique factorization in those chosen `q_n` is absent;
- the canonical `{0,1}` Möbius hypercube is lost;
- nevertheless the continued zero divisor in `Re(s)>0` is unchanged, and Sierra can feed the modified inverse coefficients into the same spectral architecture.

This is a direct instance of the README's required arithmetic-specificity control. A mechanism that survives this deformation has not yet used the exact rational-prime norm/factorization structure strongly enough to explain RH.

## Prior art and novelty audit

Primary sources:

- **Germán Sierra**, “The Riemann Zeros as Spectrum and the Riemann Hypothesis,” *Symmetry* **11**(4) (2019), 494. DOI: https://doi.org/10.3390/sym11040494. arXiv: https://arxiv.org/abs/1601.01797. Sections XI--XII give the square-free Möbius mirror model, `ell_n=sqrt(n)`, the `log p` return time, the self-adjoint boundary phase, and the critical-zero normalizability analysis; Section XIV explicitly imports Grosswald–Schnitzer deformations and constructs the corresponding modified Dirac models.

- **Emil Grosswald, F. J. Schnitzer**, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. Theorem 1 proves meromorphic continuation of the modified Euler products to `Re(s)>0` and equality, including multiplicity, of their zeros with those of zeta there.

No part of Sierra's model or the Grosswald–Schnitzer theorem is claimed as new. The exponent-coordinate rewrite is elementary. The durable contribution here is the **matched-control synthesis for the canonical research mandate**: the line's desired square-free exponent-lattice / `log p` / self-adjoint scattering package already exists, but the same literature supplies a deformation that preserves the zero divisor while removing exact rational-prime lattice geometry. That materially redirects the novelty target.

A repository audit found no existing `PL-*` finding centered on Sierra's Rindler model or the Grosswald–Schnitzer control. The closest stored negatives are `PL-021` (native Bohr-Hardy Möbius cyclicity is automatic where defined), `PL-023` (full prime-shift invariance plus normality collapses), `PL-033`/`PL-039` (classical scattering can realize zero data without supplying localization), and `PL-124` (Poisson–Newton trace architecture is too universal). The present finding is distinct because the positive prior art uses the **canonical square-free Möbius lattice itself** inside a self-adjoint transfer model, while the paired deformation tests whether that exact arithmetic geometry is actually responsible for the zero spectrum.

## Falsification boundary and surviving route

The negative conclusion is deliberately narrow. It would be materially escaped by a construction satisfying both of the following conditions.

First, it must produce a **single canonical global operator or positive form** from the rational-prime lattice, rather than choosing a self-adjoint extension parameter from the target zero. The zero divisor must emerge from the operator, not be selected through a boundary knob.

Second, the construction must be **non-isospectral under Grosswald–Schnitzer deformations** for a mathematically identifiable reason. It must use an invariant of actual rational-prime factorization, the exact norm map, an adelic/global compatibility law, or another arithmetic structure that the `q_n` replacement destroys. Merely rebuilding transfer matrices from coefficients of `1/zeta*` is insufficient, because that transports already-preserved zero data into the model.

A useful adversarial test for any future prime-lattice Hilbert–Pólya candidate is therefore: replace the local prime data by a Grosswald–Schnitzer sequence with the same zero divisor. If the proposed positivity, determinant, boundary condition, or scattering law remains intact after this replacement, it cannot by itself explain why the rational-prime zeta divisor lies on `Re(s)=1/2`.

## Consequence for the research line

The line no longer needs to ask whether the canonical `{0,1}` exponent sector can be embedded in a self-adjoint quantum/scattering geometry with primitive periods `log p`: Sierra already does so. More importantly, this example shows why such a realization is not enough. The spectral model can be **target-relative**, and its apparent prime specificity can survive at the level of the zero divisor even after the actual prime basis is replaced.

The surviving target is consequently sharper than “find a Hamiltonian using the prime lattice.” It is:

`derive one canonical global spectral/positive structure whose zero localization depends essentially on exact rational-prime arithmetic and fails under zero-preserving Euler-factor deformations`.

That criterion joins the main redirects of the line: `PL-119`--`PL-120` isolate the missing positivity/metric step even when zeros already appear spectrally, while `PL-124` shows that trace formulas are too universal. Sierra plus Grosswald–Schnitzer add the complementary warning that **even an explicit self-adjoint square-free-lattice scattering model can still be a realization of supplied zero data rather than an arithmetic mechanism forcing RH**.