# AF-167 — Phase-gradient moments sharply recover finite Blaschke zero divisors

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `MINIMAL-LIFT-STRUCTURE`, `PHASE/ORIENTATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-166 shows that boundary modulus forgets the entire inner factor and therefore cannot recover a Blaschke zero divisor. For finite Blaschke products, however, the missing zero information does not require the full boundary phase to be restored: a finite, sharply sized phase-gradient mark is enough.

Let

\[
B(z)=c\prod_{j=1}^{n}\frac{z-a_j}{1-\overline{a_j}z},
\qquad |c|=1,
\qquad a_j\in\mathbb D,
\tag{1}
\]

where zeros are repeated according to multiplicity. Since `B` is unimodular on the unit circle, choose a continuous lifted boundary phase

\[
B(e^{it})=e^{i\beta(t)}.
\tag{2}
\]

Its derivative is periodic and satisfies the classical identity

\[
\boxed{
\beta'(t)
=
\sum_{j=1}^{n}
\frac{1-|a_j|^2}{|e^{it}-a_j|^2}
=
\sum_{j=1}^{n}P_{a_j}(e^{it}),
}
\tag{3}
\]

so the phase gradient is exactly a sum of Poisson kernels centered at the zeros.

Use the Fourier convention

\[
\widehat g(k)
=
\frac1{2\pi}\int_0^{2\pi}g(t)e^{-ikt}\,dt.
\tag{4}
\]

Then

\[
\boxed{
\widehat{\beta'}(0)=n,
\qquad
\widehat{\beta'}(k)=\sum_{j=1}^{n}\overline{a_j}^{\,k}
\quad(k\ge 1).
}
\tag{5}
\]

Hence the mean of the phase derivative gives the total zero multiplicity, while its positive Fourier coefficients are the conjugates of the power sums of the zero multiset.

It follows that, on the degree-`n` class, the first `n` positive phase-gradient Fourier coefficients determine the entire zero divisor exactly. Indeed, after setting

\[
p_k=\sum_{j=1}^{n}a_j^k
=\overline{\widehat{\beta'}(k)},
\qquad 1\le k\le n,
\tag{6}
\]

Newton--Girard identities recursively recover the elementary symmetric functions `e_1,...,e_n`, hence the monic polynomial

\[
Q(z)
=
\prod_{j=1}^{n}(z-a_j)
=
z^n-e_1z^{n-1}+e_2z^{n-2}-\cdots+(-1)^ne_n.
\tag{7}
\]

The roots of `Q`, with multiplicity, are exactly the Blaschke zero divisor.

The threshold is sharp in the worst case. Knowing the degree together with only the first `n-1` positive Fourier coefficients is not enough. For `0<r<s<1` and

\[
\omega=e^{2\pi i/n},
\tag{8}
\]

consider the two zero multisets

\[
Z_r=\{r,r\omega,\ldots,r\omega^{n-1}\},
\qquad
Z_s=\{s,s\omega,\ldots,s\omega^{n-1}\}.
\tag{9}
\]

For every `1<=k<n`,

\[
\sum_{a\in Z_r}a^k
=
r^k\sum_{j=0}^{n-1}\omega^{jk}
=0
=
s^k\sum_{j=0}^{n-1}\omega^{jk}
=
\sum_{a\in Z_s}a^k,
\tag{10}
\]

while

\[
\sum_{a\in Z_r}a^n=nr^n
\ne
ns^n=\sum_{a\in Z_s}a^n.
\tag{11}
\]

Thus their phase gradients have the same mean and the same first `n-1` positive Fourier modes, yet their zero divisors are different. The `n`th mode is precisely the first one that distinguishes this matched pair.

Therefore finite Blaschke zero recovery has an exact endpoint-relative hierarchy:

1. boundary modulus is completely blind to the divisor;
2. the phase-gradient mean recovers only the zero count;
3. fewer than `n` nonzero Fourier moments are not uniformly faithful on degree-`n` divisors;
4. the first `n` positive Fourier moments recover the full degree-`n` divisor;
5. the entire phase or entire phase derivative contains strictly more information than this endpoint requires.

This is a concrete sharp instance of the Arithmetic Fidelity principle that a repair should retain the **smallest structurally adequate witness class for the declared endpoint**, rather than restoring the whole discarded representation.

## Derivation

### Boundary phase derivative is a Poisson mixture

For one Blaschke factor

\[
b_a(z)=\frac{z-a}{1-\overline a z},
\tag{12}
\]

write `b_a(e^{it})=e^{i\beta_a(t)}` up to an irrelevant constant phase. Direct differentiation gives

\[
\beta_a'(t)
=
\frac{1-|a|^2}{|e^{it}-a|^2}.
\tag{13}
\]

The right side is the usual Poisson kernel. Because the phase of a product is the sum of the lifted phases modulo an additive constant, derivatives add, yielding `(3)`.

The Poisson kernel has the absolutely convergent Fourier expansion

\[
P_a(e^{it})
=
1+
\sum_{k\ge1}
\left(
\overline a^{\,k}e^{ikt}
+a^ke^{-ikt}
\right).
\tag{14}
\]

Summing `(14)` over the zeros gives

\[
\beta'(t)
=
n+
\sum_{k\ge1}
\left(
\sum_{j=1}^{n}\overline{a_j}^{\,k}
\right)e^{ikt}
+
\sum_{k\ge1}
\left(
\sum_{j=1}^{n}a_j^k
\right)e^{-ikt},
\tag{15}
\]

which proves `(5)`. Since `\beta'` is real, negative and positive Fourier coefficients are conjugate; retaining both sides would duplicate information.

Zeros at the origin cause no difficulty. Their Poisson kernels are the constant function `1`, so they contribute to `\widehat{\beta'}(0)=n` and contribute zero to every nonzero power sum. The known degree then lets Newton identities recover the corresponding zero roots correctly.

### Newton identities close the finite divisor

Let

\[
e_k=e_k(a_1,\ldots,a_n),
\qquad e_0=1,
\tag{16}
\]

be the elementary symmetric functions. Newton--Girard gives, for `1<=k<=n`,

\[
\boxed{
k e_k
=
\sum_{j=1}^{k}(-1)^{j-1}e_{k-j}p_j.
}
\tag{17}
\]

Thus `p_1` determines `e_1`; then `p_1,p_2` determine `e_2`; continuing triangularly, `p_1,...,p_n` determine all coefficients of `(7)`. No choice of root ordering is introduced: the recovered object is intrinsically the unordered zero multiset with multiplicities.

The unimodular constant `c` in `(1)` is intentionally absent. It changes boundary phase by a constant and hence disappears under differentiation, but it is irrelevant to the zero-divisor endpoint. This is not a defect of the proposed mark; it is an endpoint-null coordinate in the sense emphasized by AF-165.

### The lower bound is a matched-control theorem, not a dimension count

A real-dimension heuristic suggests that a degree-`n` divisor should require `2n` real parameters, but that alone would not prove failure of a particular truncated phase mark. The regular `n`-gon controls `(9)` give an exact collision.

Both products have degree `n`, so their zeroth phase-gradient coefficient agrees. Root-of-unity cancellation makes every power sum through order `n-1` vanish for both. Therefore the complete retained mark

\[
\left(
\widehat{\beta'}(0),
\widehat{\beta'}(1),\ldots,
\widehat{\beta'}(n-1)
\right)
\tag{18}
\]

is identical, while the target divisor differs. AF-001 therefore rules out exact recovery from `(18)` on the full degree-`n` class.

At order `n`, equation `(11)` separates the pair, and the Newton reconstruction proves that this is not merely enough for this example but sufficient for every degree-`n` divisor.

For a class of degree at most `N`, the same statement can be used without knowing the degree in advance: `\widehat{\beta'}(0)` supplies the actual degree `n<=N`, after which the first `n` positive coefficients are sufficient.

## Prior art and novelty assessment

The analytic and algebraic ingredients are classical.

- Tao Qian, **“Boundary derivatives of the phases of inner and outer functions and applications,”** *Mathematical Methods in the Applied Sciences* 32 (2009), 253--263, DOI `10.1002/mma.1032`. The paper explicitly derives the phase derivative of a disk automorphism as the Poisson kernel and notes that finite Blaschke phase derivatives are sums of those kernels: https://doi.org/10.1002/mma.1032
- L. M. Delves and J. N. Lyness, **“A numerical method for locating the zeros of an analytic function,”** *Mathematics of Computation* 21 (1967), 543--560, DOI `10.1090/S0025-5718-1967-0228165-4`. Their classical contour method obtains power sums of enclosed zeros from logarithmic-derivative integrals and then reconstructs the zero polynomial through Newton identities: https://doi.org/10.1090/S0025-5718-1967-0228165-4
- Newton--Girard identities themselves are standard symmetric-polynomial algebra; no novelty is claimed for the fact that the first `n` power sums determine an unordered `n`-tuple over characteristic zero.

A targeted literature search also finds substantial work on phase derivatives, angular derivatives, finite Blaschke products, moment problems, and contour-moment zero reconstruction. Nothing in this finding should be read as claiming a new inverse-problem theorem for finite Blaschke products.

The Arithmetic Fidelity contribution is narrower: combine these classical identities into a **sharp compression/lift profile** for the endpoint exposed by AF-166. Boundary modulus discards the divisor completely; winding/mean retains only its cardinality; truncated phase-gradient moments increase fidelity in a controlled way; and exactly `n` nonzero moments are sufficient in degree `n`, while `n-1` fail by an explicit matched family. This identifies a finite relational witness that is materially smaller than restoring the entire discarded phase.

## Boundary conditions and falsification checks

- The sharp threshold is for the unrestricted class of finite Blaschke products of fixed degree `n`, with multiplicity. A narrower family may be recoverable from fewer moments because independent structural constraints reduce the admissible divisor class.
- The statement is exact, not numerical. Near-collisions can make polynomial-root reconstruction ill-conditioned even though the moment map is injective at the stated threshold. No stability modulus is claimed here.
- The phase-gradient mark presupposes access to boundary phase information. It cannot be computed from boundary modulus alone; AF-166 proves precisely why some extra inner-sensitive information is necessary.
- The result recovers the Blaschke zero divisor, not a singular inner factor and not the unimodular constant multiplying `B`.
- Full boundary phase derivative is not asserted to be a minimal representation in every coding or regularity category. The only sharp minimality claim is that the first `n-1` Fourier moments plus degree are insufficient in the declared nested Fourier-moment family, whereas the first `n` are sufficient.
- The root-of-unity controls remain strictly inside the disk for `0<r,s<1`, so there is no boundary-zero or limiting pathology in the lower-bound example.
- For `n=1`, the lower bound says that degree alone is insufficient; the first nonzero Fourier coefficient recovers the sole zero. Equations `(9)--(11)` reduce to choosing two distinct radii.
- No statement about Riemann-zeta zeros follows directly. An arithmetic application must first justify a finite-Blaschke or equivalent finite-divisor model and show that the proposed phase-gradient moments are intrinsic data of that construction rather than an externally supplied encoding of the desired zeros.

## Relationship to the current frontier

AF-164 and AF-165 emphasize that provenance recovery must be matched to the actual admissible code and downstream quotient instead of charging every hidden distinction. AF-166 gives an analytic example where modulus compression annihilates a zero-bearing coordinate but only describes coarse endpoint lifts: winding for zero count, Blaschke data for the full disk divisor, and the complete inner factor for the full function.

AF-167 fills the intermediate gap for the finite-divisor endpoint. The discarded inner coordinate has a natural hierarchy of relational summaries, and the amount required can be proved exactly rather than described as “some phase information.” In the degree-`n` model, the needed witness closes after `n` phase-gradient moments and cannot close uniformly one moment earlier.

This suggests a more precise audit for later arithmetic applications: once a compression is shown to forget a discriminator, do not jump directly from “lost” to “restore the whole source.” First identify an intrinsic transform of the missing coordinate whose truncated moments generate the declared endpoint, then prove both a reconstruction theorem and a matched-control lower bound for the truncation depth.