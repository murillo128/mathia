# WP-101 — Correlations restore Haar equivalence at the critical sharp diagonal, but only below the Zygmund endpoint

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-BOUNDARY + MATCHED-CONTROL` for the mixed-prime prime-torus completion route. This is not a global Weil-positivity mechanism.

## Claim

`WP-097` constructs a positive mixed-prime product completion of the exact one-prime Weil rays with sharp diagonal mass

\[
C_*=\sup_p \frac{2\log p}{\sqrt p-1}
=\frac{2\log 2}{\sqrt2-1},
\tag{1}
\]

while `WP-100` proves that this **independent product** completion is singular to product Haar at the critical exponent `sigma=1/2`. That singularity is not correlation-invariant.

Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T,
\qquad m=\bigotimes_p\frac{d\theta_p}{2\pi}.
\]

There exists a finite positive measure

\[
\boxed{\mu_*=C_*W_*\,dm\sim m}
\tag{2}
\]

with the same **sharp** total mass `mu_*(T^P)=C_*` and with every exact one-prime ray

\[
\boxed{
\widehat\mu_*(k e_p)
=-(\log p)p^{-|k|/2},
\qquad p\in\mathcal P,\ k\ne0.
}
\tag{3}
\]

The density `W_*` is an explicit countable mixture of finite-block product densities. Thus mixed-prime correlations can restore Haar equivalence even exactly at the diagonal threshold where the natural all-prime product is Kakutani-singular.

However the restoration is necessarily extremely rough. If **any** completion `mu=w dm` has even the first critical moments

\[
\widehat\mu(e_p)=-\frac{\log p}{\sqrt p},
\tag{4}
\]

then

\[
\boxed{
w\notin L(\log L)^{1/2}(m),
}
\tag{5}
\]

where the endpoint class means, equivalently up to the usual Orlicz normalization,

\[
\int |w|\sqrt{\log(e+|w|)}\,dm<\infty.
\tag{6}
\]

In particular

\[
w\notin L^{1+\varepsilon}(m)
\qquad\text{for every }\varepsilon>0.
\tag{7}
\]

Consequently `WP-100` should be read as a **factorization obstruction**, not a general measure-class obstruction. The correlated Haar-equivalent escape is real, but every such escape is forced below the classical Zygmund regularity endpoint. This does not supply the archimedean term, the polar counterterm, a canonical selector, or an independent global sign theorem.

## 1. The local positive factor and its exact threshold

Write

\[
r_p=p^{-1/2},
\qquad
P_{r_p}(\theta)=\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2}.
\]

For a positive parameter `a`, define the normalized one-coordinate factor

\[
F_{p,a}(\theta)
=
1+\frac{\log p}{C_*a}\bigl(1-P_{r_p}(\theta)\bigr).
\tag{8}
\]

It has Haar mean one. Since

\[
\max_\theta P_r(\theta)=\frac{1+r}{1-r},
\]

we have

\[
F_{p,a}\ge0
\quad\Longleftrightarrow\quad
1-\frac{\log p}{C_*a}\frac{2r_p}{1-r_p}\ge0.
\]

Define

\[
c_p=\frac{2\log p}{\sqrt p-1},
\qquad
d_p=\frac{c_p}{C_*}.
\tag{9}
\]

Then exactly

\[
\boxed{F_{p,a}\ge0\iff a\ge d_p.}
\tag{10}
\]

Moreover, for every nonzero integer `k`, the Poisson Fourier series gives

\[
\boxed{
\widehat F_{p,a}(k)
=-\frac{\log p}{C_*a}p^{-|k|/2}.
}
\tag{11}
\]

The threshold sequence is strictly decreasing with the prime. Indeed, with `x=y^2`,

\[
\frac{2\log x}{\sqrt x-1}
=\frac{4\log y}{y-1},
\]

and its derivative has the sign of

\[
\frac{y-1}{y}-\log y<0
\qquad(y>1).
\]

Hence `d_2=1`, `d_3<1`, and `d_p\downarrow0`. This recovers the sharp `WP-097` mass threshold without any zero data.

## 2. Exact correlated Haar-equivalent completion at `C_*`

The prime `2` saturates the local threshold, so keep its factor in every mixture component:

\[
G_2(\theta_2)=F_{2,1}(\theta_2)\ge0.
\tag{12}
\]

It is positive except at the single point `theta_2=0`, hence positive Haar-a.e.

Enumerate the remaining primes increasingly and put

\[
D=d_3<1,
\qquad
\alpha_1=D,
\qquad
\alpha_j=(1-D)2^{-(j-1)}\quad(j\ge2).
\tag{13}
\]

Then

\[
\sum_{j\ge1}\alpha_j=1,
\qquad \alpha_j\downarrow0.
\tag{14}
\]

Because `d_p\downarrow0`, the primes `p>=3` can be partitioned into finite consecutive blocks

\[
\mathcal P\setminus\{2\}=\bigsqcup_{j\ge1}B_j
\tag{15}
\]

such that

\[
d_p\le\alpha_j
\qquad(p\in B_j).
\tag{16}
\]

One deterministic construction is to start with `B_1` at `p=3`; after the start of block `j`, choose the next block boundary far enough out that all remaining `d_p` are at most `alpha_{j+1}`. Since `d_p` tends to zero, every boundary is finite.

For each block set

\[
H_j(\theta)
=
\prod_{p\in B_j}F_{p,\alpha_j}(\theta_p).
\tag{17}
\]

By (10), every factor is nonnegative, so `H_j>=0`; because the block is finite and every factor has mean one,

\[
\int H_j\,dm=1.
\]

Now take the convex mixture

\[
H=\sum_{j\ge1}\alpha_jH_j.
\tag{18}
\]

The series converges in `L^1(m)` because

\[
\sum_j\|\alpha_jH_j\|_1=\sum_j\alpha_j=1.
\]

It is finite a.e., has mean one, and is positive a.e.; for example `H>=alpha_1 H_1` and the finite product `H_1` is positive outside a Haar-null set.

Finally define

\[
W_*(\theta)=G_2(\theta_2)H(\theta).
\tag{19}
\]

The two factors use disjoint coordinate sets, so `W_*>=0`, `W_*` has mean one, is finite a.e., and is positive a.e. Therefore

\[
\mu_*=C_*W_*dm
\]

is equivalent to Haar and has mass `C_*`.

The pure prime-ray coefficients are exact. For `p in B_j` and `k!=0`, every mixture component other than `j` is constant in the `p` coordinate, hence contributes zero, while (11) gives

\[
\widehat H(k e_p)
=\alpha_j\widehat F_{p,\alpha_j}(k)
=-\frac{\log p}{C_*}p^{-|k|/2}.
\tag{20}
\]

For `p=2` the same identity follows directly from `G_2`. Multiplication by the mass `C_*` proves (3).

The completion necessarily has mixed coefficients. Within a block they are the finite-product coefficients needed to pay for positivity; modes across different tail blocks vanish because (18) is a mixture rather than a product. Mixed modes involving `2` survive because the saturated `2` factor is common to all components. None of these mixed coefficients is chosen from zero data.

For any `C>C_*`, simply set

\[
\mu_C=\mu_*+(C-C_*)m.
\tag{21}
\]

This preserves every nonzero Fourier coefficient, has mass `C`, and has density bounded below by the positive constant `C-C_*`. Thus even strict Haar equivalence with a positive lower density bound is compatible with the exact critical prime rays; what fails is upper/integrability regularity, not measure class.

## 3. Zygmund endpoint: every absolutely continuous critical completion is rough

Let `w in L^1(m)` and write its first coordinate coefficients as

\[
a_p=\int_{\mathbb T^{\mathcal P}}w(\theta)\,\overline{z_p(\theta)}\,dm(\theta).
\tag{22}
\]

The coordinate characters `z_p` are independent Steinhaus variables under product Haar. For every finite scalar family `(b_p)`, the linear combination

\[
S_b=\sum_p b_p z_p
\]

is subgaussian with

\[
\|S_b\|_{\exp L^2}
\le K\Bigl(\sum_p|b_p|^2\Bigr)^{1/2}
\tag{23}
\]

for an absolute `K`. This can be proved directly from independence: for every real direction, the moment generating function factors into one-coordinate Bessel factors and satisfies `I_0(t)<=e^{t^2/4}`; the resulting Gaussian tail bound gives (23).

The complementary Orlicz class to `exp L^2` is `L(log L)^{1/2}`. Orlicz Hölder therefore gives

\[
\left|\sum_p b_p a_p\right|
=
\left|\int w\,\overline{S_b}\,dm\right|
\le
K'\|w\|_{L(\log L)^{1/2}}
\Bigl(\sum_p|b_p|^2\Bigr)^{1/2}.
\tag{24}
\]

Hence `(a_p)` defines a bounded functional on `ell^2`, and by Hilbert-space duality

\[
\boxed{
 w\in L(\log L)^{1/2}(m)
 \quad\Longrightarrow\quad
 (a_p)_p\in\ell^2.
}
\tag{25}
\]

This is the independent-coordinate form of the classical Zygmund restriction inequality for lacunary/quasi-independent Fourier sets.

For the critical Weil moments,

\[
a_p=-\frac{\log p}{\sqrt p},
\]

so

\[
\sum_p|a_p|^2
=
\sum_p\frac{(\log p)^2}{p}
=\infty.
\tag{26}
\]

The last divergence already follows from Euler's divergence of `sum_p 1/p`, since `(log p)^2>=1` for all sufficiently large primes. Equations (25)--(26) prove (5). On a probability space every `L^{1+epsilon}` embeds into `L(log L)^{1/2}`, proving (7).

More generally, at attenuation exponent `sigma`, exact first moments

\[
a_p(\sigma)=-(\log p)p^{-\sigma}
\]

can come from an `L(log L)^{1/2}` Haar density only if

\[
\sum_p(\log p)^2p^{-2\sigma}<\infty.
\tag{27}
\]

For the ordinary primes this holds exactly when `sigma>1/2`. Thus the same critical boundary found in `WP-022`, `WP-032`, and `WP-100` reappears here without assuming product factorization.

## 4. Sharpness and what `WP-100` actually ruled out

For `sigma>1/2`, `WP-100` computes the finite-cylinder `L^2` norms of the explicit `WP-097` product densities and shows them uniformly bounded. The cylinder densities are a positive martingale, so the bounded `L^2` norms yield an actual `L^2(m)` density in the infinite-prime limit.

At `sigma=1/2`, `WP-100` instead proves that **that factorized product** is singular to Haar. The construction above shows that this singularity cannot be promoted to a theorem about all positive completions with the same one-prime marginals:

\[
\boxed{
\text{critical independent product is singular}
\quad\not\Rightarrow\quad
\text{every critical positive completion is singular}.
}
\tag{28}
\]

The correlation-robust statement is the weaker but sharp regularity obstruction (5): every Haar-density completion lies beyond the `L(log L)^{1/2}` Zygmund endpoint.

This distinction matters for subsequent geometric arguments. A proof that requires a bounded, `L^2`, `L^{1+epsilon}`, finite-entropy-type, or comparably regular density perturbation of Haar cannot use an exact critical completion. But arguments depending only on mutual absolute continuity or null sets cannot reject the correlated route.

## 5. Matched generalized-generator control

Nothing in the block-mixture mechanism distinguishes the rational primes. For a countable free multiplicative generator set with energies `E_j>0`, target ray moments

\[
-E_j e^{-\sigma |k|E_j}
\]

have the same local positive threshold

\[
c_j(\sigma)
=\frac{2E_j}{e^{\sigma E_j}-1}.
\tag{29}
\]

Whenever `c_j` has a finite maximum and tends to zero, the same finite-block mixture constructs a Haar-equivalent positive completion at the sharp maximum mass. Likewise the Zygmund argument forces every `L(log L)^{1/2}` density to satisfy

\[
\sum_j E_j^2e^{-2\sigma E_j}<\infty.
\tag{30}
\]

Therefore neither the existence of the correlated completion nor its endpoint regularity obstruction is an RH-specific geometric sign theorem. The rational-prime threshold enters through the energy distribution `E_p=log p`; the mechanism itself is universal harmonic/probabilistic geometry.

This matched control is decisive against treating (2) as the sought Mathia-native Weil positivity structure.

## 6. Prior-art and novelty audit

The harmonic-analysis input in (23)--(25) is classical, not a Mathia discovery. It is the Steinhaus/dissociated-set form of Khintchine--Zygmund restriction. A modern audit reference is Odysseas Bakas, *On a Problem of Pichorides*, Journal of Geometric Analysis 31 (2021), 7455--7512, DOI `10.1007/s12220-020-00550-8`; §5.1 records the classical Zygmund estimate

\[
\left(\sum_{\lambda\in\Lambda}|\widehat f(\lambda)|^2\right)^{1/2}
\lesssim
1+\int |f|\sqrt{\log(e+|f|)}
\]

for lacunary/quasi-independent frequency sets. Jerzy Sawa, *The best constant in the Khintchine inequality for complex Steinhaus variables, the case p=1*, Studia Mathematica 81 (1985), 107--126, DOI `10.4064/sm-81-1-107-126`, is a classical Steinhaus-Khintchine anchor.

The elementary idea that correlations/couplings can share prescribed one-coordinate marginals is also not novel. What is Mathia-specific here is the exact application to the `WP-096`/`WP-097` prime-torus normal form at the **sharp Weil diagonal**, together with the explicit finite-block mixture and the endpoint theorem showing exactly what regularity every correlated Haar-density escape must sacrifice.

This differs materially from earlier findings:

- `WP-022` concerns the canonical factorized Poisson family and its Fisher norm;
- `WP-032` concerns the rank-one determinantal Gram completion and closability;
- `WP-096` proves that deleting all mixed modes forces divergent diagonal mass;
- `WP-097` proves that mixed modes restore finite positive mass using one explicit all-prime product;
- `WP-100` classifies Haar equivalence versus singularity for that product family.

`WP-101` shows that the `WP-100` measure-class transition does **not** survive arbitrary correlations, while a classical Zygmund endpoint obstruction does.

No zero set, explicit-formula zero term, analytic continuation of zeta, or RH-equivalent positivity criterion enters the derivation.

## 7. Failure modes and surviving search space

The result should not be overread.

1. The block partition and convex mixture are engineered to realize already-specified one-prime moments. They are a **matched control**, not an intrinsic Mathia construction whose geometry independently predicts the Weil coefficients.
2. The mixed coefficients are not the sparse Weil selector. They are auxiliary positivity-paying correlations, and no canonical positive quotient removing them is obtained; `WP-098` and `WP-099` still block the direct positive/passive eliminations.
3. Haar equivalence gives no Weil sign theorem. The density is necessarily outside `L(log L)^{1/2}`, and ordinary Hilbert-density perturbation arguments therefore remain unavailable at the critical point.
4. No archimedean Gamma/digamma term or global polar term is generated.
5. The endpoint theorem does **not** prove that every critical completion is singular or nonclosable. In fact (2) explicitly disproves the former statement.
6. Singular states, endpoint-rough Haar-equivalent states, nonlinear/off-diagonal reductions, and genuinely global finite--archimedean constructions remain logically open, but each still needs an independently forced sign theorem.

The decisive methodological consequence is:

\[
\boxed{
\text{do not use product-Haar singularity as a correlation-robust no-go.}
}
\tag{31}
\]

The robust finite-place boundary is instead that exact critical rays force any absolutely continuous completion below the `L(log L)^{1/2}` regularity threshold. A successful global route must either make such roughness geometrically canonical and still control a positive form, or introduce the finite and archimedean sectors together before this scalar prime-torus completion is formed.

## Consequence for the primary question

This finding does **not** provide a Mathia-native geometric structure whose positivity yields the global Weil criterion. It removes one misleading obstruction and replaces it with a sharper one:

```text
exact critical one-prime Weil rays
    + finite sharp positive diagonal
    + arbitrary mixed-prime correlations
        -> Haar-equivalent completion exists
        -> but every Haar density is below L(log L)^{1/2}
        -> no regular Hilbert-density perturbation at the Weil boundary
        -> still no archimedean/global sign theorem
```

Thus the remaining problem is not simply to escape a singular measure class. It is to explain, intrinsically and globally, why the necessary endpoint-rough mixed correlations and the infinite-place contribution should arise from one geometry with an independent positivity theorem.