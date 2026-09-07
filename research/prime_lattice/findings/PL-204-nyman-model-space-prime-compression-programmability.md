# PL-204 — Nyman model-space prime compressions encode arbitrary Blaschke zeros and do not force RH

**Status:** negative result / structural classicalization  
**Evidence class:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the canonical common-inner/model-space compression route  
**Research line:** `prime_lattice`

## Claim

The target-relative model-space compression left open by `PL-020` is genuinely zero-sensitive, but its native prime-lattice spectrum is fully programmable by an arbitrary inner function and therefore does not itself force Riemann zeros onto the critical line.

Let

\[
\Omega=\{s:\Re s>1/2\},\qquad H=H^2(\Omega),
\]

and for every positive integer `n` define the bounded inner multiplier

\[
\varphi_n(s)=n^{1/2-s}.
\]

These are exactly the Mellin multipliers of the integer Nyman dilation semigroup from `PL-017`, and

\[
\varphi_m\varphi_n=\varphi_{mn}.
\]

For any inner function `B` on `Omega`, form the model space

\[
K_B=H\ominus BH
\]

and the compressed integer operators

\[
C_n^B=P_{K_B}M_{\varphi_n}|_{K_B}.
\]

Then:

\[
\boxed{C_m^B C_n^B=C_{mn}^B}
\]

for all positive integers `m,n`. Hence the prime directions still give an exact representation of the positive exponent cone,

\[
C_n^B=\prod_p (C_p^B)^{v_p(n)}.
\]

If `rho in Omega` is a zero of `B`, the Hardy reproducing kernel `k_rho` belongs to `K_B` and is a joint eigenvector of the adjoint prime tuple:

\[
\boxed{
(C_p^B)^*k_\rho=p^{1/2-\overline\rho}k_\rho
\qquad\text{for every prime }p.
}
\]

Thus the prime-exponent lattice gives a precise joint spectral encoding of the zeros of the chosen inner function. In particular, taking `B=B_Z`, the Blaschke product of hypothetical zeta zeros in `Re(s)>1/2` from `PL-020`, every off-line zeta zero becomes a joint prime-lattice eigencharacter.

However, the same construction works for **every** admissible Blaschke divisor. Given any prescribed point `rho_0 in Omega`, the one-zero Blaschke factor `b_{rho_0}` has one-dimensional model space and produces exactly the scalar prime tuple

\[
C_p^{b_{\rho_0}}=p^{1/2-\rho_0}I.
\]

More generally an arbitrary Blaschke sequence in `Omega` supplies the corresponding joint kernel eigencharacters. Therefore the compressed prime tuple contains no mechanism that distinguishes the Riemann zero divisor from a freely chosen off-critical divisor. It faithfully **reads** the inner factor but does not constrain it.

For the zeta specialization,

\[
\boxed{
RH\iff B_Z=1\iff K_{B_Z}=\{0\}.
}
\]

This is an exact spectral restatement of the Blaschke obstruction, not a Hilbert–Pólya mechanism. The route is killed unless an additional arithmetic structure constrains `B` or supplies a positivity/coercivity statement not present in the model-space compression itself.

## 1. The compressed prime action remains an exact semigroup

Because `B H` is invariant under every analytic multiplier `M_{varphi_n}`, the orthogonal complement `K_B` is invariant under every adjoint `M_{varphi_n}^*`. Consequently

\[
(C_n^B)^*=M_{\varphi_n}^*|_{K_B}.
\]

For `f in K_B`, invariance lets the adjoints compose without inserting any intermediate projection:

\[
(C_m^B)^*(C_n^B)^*f
 =M_{\varphi_m}^*M_{\varphi_n}^*f
 =M_{\varphi_{mn}}^*f
 =(C_{mn}^B)^*f.
\]

Taking adjoints and using commutativity gives

\[
C_m^B C_n^B=C_{mn}^B.
\]

No invertibility of the compressed operators is used. The calculation is the standard coinvariant/model-space mechanism behind analytic truncated Toeplitz operators. In prime coordinates it means that compression does **not** destroy the exact exponent-cone multiplication law.

Each `M_{varphi_n}` is an isometry on the boundary because

\[
|\varphi_n(1/2+it)|=1,
\]

and its compression is therefore a contraction. The `1/2` in this statement is the same Mellin/`L^2` normalization already isolated in `PL-017`; it is not a conclusion about zeta zeros.

## 2. Zeros become joint adjoint eigencharacters

Let `k_rho` be the reproducing kernel of `H` at `rho in Omega`. If `B(rho)=0`, then for every `h in H`,

\[
\langle Bh,k_\rho\rangle=(Bh)(\rho)=B(\rho)h(\rho)=0,
\]

so

\[
k_\rho\in K_B.
\]

For every bounded analytic multiplier `phi`, the standard reproducing-kernel identity is

\[
M_\phi^*k_\rho=\overline{\phi(\rho)}k_\rho.
\]

Substituting `phi=varphi_n` gives

\[
(C_n^B)^*k_\rho
 =n^{1/2-\overline\rho}k_\rho.
\]

For `n=p` prime this is exactly the prime-lattice character

\[
p^{1/2-\overline\rho}
 =\exp\bigl((1/2-\overline\rho)\log p\bigr).
\]

Two distinct prime coordinates already determine `rho` uniquely. If `rho,rho' in Omega` produced the same eigenvalues for two distinct primes `p,q`, then

\[
(\overline\rho-\overline{\rho'})\log p\in2\pi i\mathbb Z,
\qquad
(\overline\rho-\overline{\rho'})\log q\in2\pi i\mathbb Z.
\]

A nonzero difference would make `log p/log q` rational, contradicting unique factorization. Thus the **joint** prime tuple removes the periodic aliasing of a single exponential coordinate.

This makes the spectral encoding mathematically nontrivial as a dictionary: the off-line divisor is recoverable from the joint eigencharacters. What fails is the next implication. Nothing in the tuple forces those characters to have boundary modulus one.

## 3. The matched control is an arbitrary Blaschke divisor

Fix any `rho_0 in Omega`, with no arithmetic condition. Let `B=b_{rho_0}` be the elementary half-plane Blaschke factor having its only zero at `rho_0`. Its model space has dimension one and is spanned by `k_{rho_0}`. The preceding eigenvector formula therefore determines the whole compressed tuple:

\[
(C_n^B)^*=
 n^{1/2-\overline{\rho_0}}I,
\qquad
C_n^B=n^{1/2-\rho_0}I.
\]

In particular,

\[
C_p^B=p^{1/2-\rho_0}I
\]

for every prime `p`, while the exact relations

\[
C_p^B C_q^B=C_{pq}^B=C_q^B C_p^B
\]

hold automatically. Since `rho_0` may be placed anywhere in the open half-plane, the exact rational-prime frequency set `{log p}` and the full multiplicative semigroup law do not impose a critical-line condition.

The same control can be made conjugation-symmetric by taking

\[
B=b_{\rho_0}b_{\overline{\rho_0}}
\]

whenever the two points are distinct. Thus even the elementary symmetry expected of a real-coefficient divisor does not repair the obstruction.

For a general Blaschke sequence satisfying the half-plane Blaschke condition, the same model-space construction carries all its kernel eigencharacters. The compressed tuple is therefore a **carrier for chosen inner data**, not a source of arithmetic rigidity.

## 4. Zeta specialization and the exact information boundary

`PL-020` constructs the Blaschke product `B_Z` from the multiset

\[
Z_+=\{\rho:\zeta(\rho)=0,\ \Re\rho>1/2\},
\]

counting multiplicity, and shows that it divides every Nyman Hardy generator. This uses the analytically continued Nyman functions in `H^2(Omega)`, not an Euler product outside its convergence domain.

Taking `B=B_Z` therefore gives a canonical zero-sensitive quotient component

\[
K_{B_Z}=H\ominus B_ZH.
\]

If `rho in Z_+`, then

\[
(C_p^{B_Z})^*k_\rho
 =p^{1/2-\overline\rho}k_\rho.
\]

So this construction does something the generator Gram matrices of `PL-020` cannot do: it sees the off-line zero factor exactly. But it sees it only because the model space is **defined by that inner factor**. Replacing `B_Z` by any other Blaschke product produces the corresponding alternate spectral data with identical operator-theoretic rules.

Hence the implication needed for RH is absent:

\[
\text{exact prime semigroup + model-space compression}
\not\Longrightarrow
B=1.
\]

The construction is instead a faithful functorial encoding

\[
B\longmapsto \{C_p^B\}_p
\]

whose point spectral data recover the zeros already supplied by `B`.

## 5. Prior art and novelty audit

Nikolski's 1995 theorem, already recorded in `PL-018` and `SOURCES.md`, is the decisive zeta-specific prior art. For the continuously invariant Nyman space he proves that the inner obstruction is exactly the Blaschke product of the relevant zeta zeros, with no hidden singular inner factor. Thus the passage from Nyman closure to a zeta model space is classical.

Compression of Hardy multipliers to coinvariant model spaces is likewise standard operator theory; the associated compressed-shift/truncated-Toeplitz framework is classical. The semigroup identity and kernel-eigencharacter formulas used here are re-derived above and require no unproved spectral theorem. The literature audit therefore gives no basis for a novelty claim for the model-space machinery.

The durable delta for `prime_lattice` is the **matched-control obstruction**: after `PL-020` left target/model-space information as a possible escape from generator-Gram blindness, the same exact prime-lattice compression can be programmed by an arbitrary Blaschke divisor. Thus zero sensitivity is not the same as zero localization.

Closest literature anchors:

- Nikolai Nikolski, “Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann zeta-function,” *Annales de l'Institut Fourier* **45**(1) (1995), 143–159, DOI `10.5802/aif.1451`.
- Donald Sarason, “Algebraic properties of truncated Toeplitz operators,” *Operators and Matrices* **1**(4) (2007), 491–526, DOI `10.7153/oam-01-29`. This is a standard model-space compression novelty boundary, not a dependency of the elementary derivation above.

## 6. Boundary conditions and adversarial checks

### This does not classify the discrete Nyman span

`B_Z` is a common inner divisor of the discrete Nyman generators, but `PL-020` explicitly does not assert that it is their greatest common inner divisor. Balazard's discrete invariant-subspace/classification problem from `PL-019` remains open. The present result only rules out obtaining RH from the native compressed prime tuple once an inner model-space factor is supplied.

### Boundary zeros are not interior model-space eigenvectors

For `Re(rho)>1/2`,

\[
|p^{1/2-\overline\rho}|=p^{1/2-\Re\rho}<1.
\]

The critical line corresponds formally to modulus one, but points on `Re(s)=1/2` are boundary points of the Hardy half-plane, not interior Blaschke zeros producing the reproducing-kernel eigenvectors above. Under RH, `B_Z=1` and the off-line model space is zero. Imposing unit modulus on these eigencharacters would therefore simply impose the critical-line conclusion rather than derive it.

### Multiplicity is not needed for the obstruction

At a multiple zero, kernel derivatives can encode higher-order vanishing/generalized root information in standard model-space theory. The negative result needs only one simple point control: a single arbitrary `rho_0 in Omega` already disproves any claim that the prime compression law itself forces `Re(rho)=1/2`.

### No Euler-product continuation is used

The proof uses only the Hardy-space Nyman continuation already audited in `PL-017`/`PL-020`, inner-function factorization, reproducing kernels, and bounded multipliers `n^(1/2-s)`. No Euler product is evaluated or formally continued in the critical strip.

### Additional arithmetic structure is outside the negative theorem

The finding does **not** rule out a compression or quotient carrying extra source-forced information that is not determined by an arbitrary inner function: for example a completed functional equation, an explicit-formula positivity relation, a canonical target coupling, a noncommuting action, or a coercive arithmetic boundary condition. Such a mechanism would have to distinguish `B_Z` from the matched arbitrary-Blaschke controls before the compressed spectrum could have RH content.

## Falsification / audit test

The finding is falsified if any of the following exact statements fails:

1. `BH` is invariant under every `M_{varphi_n}`, hence `K_B` is invariant under every adjoint;
2. this coinvariance implies `C_m^B C_n^B=C_{mn}^B`;
3. if `B(rho)=0`, then `k_rho in K_B` and `(C_n^B)^*k_rho=n^(1/2-conjugate(rho))k_rho`;
4. an elementary Blaschke factor at an arbitrary `rho_0 in Omega` has one-dimensional model space and realizes the corresponding scalar prime tuple;
5. `B_Z` from `PL-020` is a valid inner divisor carrying every zeta zero in `Re(s)>1/2`.

A future target-relative operator theorem would evade this negative result only if its decisive hypothesis fails for the arbitrary-Blaschke controls or if it uses additional arithmetic data not functorially determined by `B`.

## Consequence for the research line

`PL-020` established that generator-only Gram geometry loses the off-line Blaschke factor and therefore pointed toward target/model-space data as a live escape. The present result closes the most canonical version of that escape:

\[
\text{Nyman off-line inner factor}
\to K_B
\to \text{compressed prime semigroup}
\to \text{joint zero eigencharacters}
\]

is exact but fully programmable by replacing `B` with an arbitrary inner divisor.

The surviving question is narrower. A useful target-relative prime-lattice construction must contain a **source-forced relation not available for an arbitrary inner function** and then prove that this relation supplies a one-sided sign, positivity, or localization principle. Merely making the prime action zero-sensitive by compressing it to the corresponding model space is not enough.