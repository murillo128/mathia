# WP-216 — Bost–Connes critical conditioning forces the Poisson/GCD Gram, but the Weil ray is its indefinite defect

**Status:** `DERIVED + EXACT + BOST-CONNES-KMS + SOURCE-FORCED-DIVISIBILITY-PROJECTIONS + CRITICAL-HALF-DENSITY + GCD-GRAM + POISSON-KERNEL + MANGOLDT-SCALE-AVAILABLE + WEIL-SIGN-DEFECT + MATCHED-CONTROL + PRIOR-ART-AUDITED + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

The Bost–Connes branch contains a stronger intrinsic relation than the scalar selectors rejected in `WP-214` and `WP-215`. Let

\[
E_n:=\mu_n\mu_n^*
\]

be the canonical range projection of the multiplicative isometry `mu_n`. The projections form the divisibility semilattice

\[
E_mE_n=E_{\operatorname{lcm}(m,n)}.
\]

For **every** `KMS_beta` state,

\[
\phi_\beta(E_n)=n^{-\beta}.
\]

Hence, after conditioning and normalizing the KMS cyclic vector by these source-defined projections,

\[
\xi_n^{(\beta)}:=n^{\beta/2}\pi_\beta(E_n)\Omega_\beta,
\]

the resulting positive Gram kernel is exactly

\[
\boxed{
G_\beta(m,n)
:=\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle
=\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta.
}
\]

At the **actual Bost–Connes critical inverse temperature `beta=1`** this becomes

\[
\boxed{
G_1(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}
=\prod_p p^{-\frac12|v_p(m)-v_p(n)|}.
}
\]

On one prime axis it is the Toeplitz kernel

\[
G_{1,p}(a,b)=p^{-|a-b|/2},
\]

whose circle spectral density is the Poisson kernel with radius `p^{-1/2}`. Thus the critical Weil half-density appears here without a scalar `F(H)`, without selecting prime-power energies by a Borel projector, and without putting zero data into the construction. In particular,

\[
\langle\xi_1^{(1)},\xi_{p^k}^{(1)}\rangle=p^{-k/2}.
\]

The logarithmic prime scale is also intrinsic to the same Bost–Connes dynamics, since

\[
\sigma_t(\mu_p)=p^{it}\mu_p,
\qquad
\delta(\mu_p)=i(\log p)\mu_p.
\]

So the source now contains both the exact critical magnitude `p^{-k/2}` and the canonical scale `log p`.

But the decisive sign test fails in an exact way. In the multiplicative Toeplitz normalization already used in `WP-096`, the finite Weil ray at `p` has off-diagonal coefficients

\[
-\frac{\log p}{p^{|k|/2}},\qquad k\ne0.
\]

Writing `r=p^{-1/2}`, these coefficients are precisely the nonzero Fourier coefficients of

\[
\boxed{
\log p\,(1-P_r(\theta)).
}
\]

Equivalently, the desired local finite-Weil Toeplitz kernel is the zero-diagonal defect

\[
\boxed{
W_p=\log p\,(I-G_{1,p}).
}
\]

The Bost–Connes geometry therefore lands extremely close to the target, but on the wrong side of positivity: `G_{1,p}` is a genuine Gram kernel, whereas `I-G_{1,p}` is indefinite. Its symbol changes sign and at `theta=0` equals

\[
\log p\left(1-\frac{1+r}{1-r}\right)
=-\frac{2(\log p)r}{1-r}<0.
\]

A scalar diagonal repair must add at least

\[
\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}}
\]

on that prime coordinate, exactly the local threshold underlying `WP-096`; the sparse all-prime sum of those compensations diverges. Allowing mixed-prime terms can restore an ordinary positive kernel as in `WP-097`, but that is an additional affine/product completion of the Poisson factors, not a sign theorem inherited from the KMS conditional Gram itself.

This gives a sharper boundary for the current Bost–Connes clue. A source-forced relation stronger than mere affiliation or scalar interpolation **does exist**: the divisibility projections plus the KMS state canonically generate the critical Poisson/GCD geometry. What is still missing is precisely the global operation that reverses the finite Weil orientation while preserving positivity and simultaneously supplies the archimedean and polar terms. The obvious defect operation destroys the sign theorem instead of proving it.

## 1. The range projections form the exact divisibility semilattice

The rational Bost–Connes algebra is generated in particular by the multiplicative isometries `mu_n` with

\[
\mu_m\mu_n=\mu_{mn},
\qquad
\mu_n^*\mu_n=1,
\]

and by the rational phase algebra. Put

\[
E_n:=\mu_n\mu_n^*.
\tag{1}
\]

Using the standard Bost–Connes relation at the trivial phase,

\[
E_n
=\mu_n e(0)\mu_n^*
=\frac1n\sum_{n\rho=0}e(\rho),
\tag{2}
\]

so `E_n` is the normalized idempotent attached to the `n`-torsion subgroup of `Q/Z`. If `l=lcm(m,n)` and `d=gcd(m,n)`, the sum of the `m`-torsion and `n`-torsion subgroups is the `l`-torsion subgroup and every element has exactly `d` decompositions. Therefore

\[
\begin{aligned}
E_mE_n
&=\frac1{mn}
\sum_{m\rho=0}\sum_{n\eta=0}e(\rho+\eta)\\
&=\frac d{mn}\sum_{l\tau=0}e(\tau)\\
&=\frac1l\sum_{l\tau=0}e(\tau)\\
&=\boxed{E_l}.
\end{aligned}
\tag{3}
\]

In the standard positive-energy representation this is simply the statement that `E_n` projects onto the basis states whose integer label is divisible by `n`; intersections of divisibility conditions are governed by the least common multiple.

This structure is source-defined. No prime-power support or Weil coefficient has been selected yet.

## 2. KMS alone fixes the projection masses

The Bost–Connes time evolution satisfies

\[
\sigma_t(\mu_n)=n^{it}\mu_n.
\tag{4}
\]

Let `phi_beta` be any `KMS_beta` state with `beta>0`. Since `mu_n` is entire analytic for the flow, the KMS relation gives

\[
\begin{aligned}
\phi_\beta(E_n)
&=\phi_\beta(\mu_n\mu_n^*)\\
&=\phi_\beta\!\left(
\mu_n^*\sigma_{i\beta}(\mu_n)
\right)\\
&=n^{-\beta}\phi_\beta(\mu_n^*\mu_n)\\
&=\boxed{n^{-\beta}}.
\end{aligned}
\tag{5}
\]

Thus the formula holds in both the Gibbs phase and the high-temperature KMS phase; it is not an artifact of using the type-I Gibbs trace where that trace exists.

Now let `(pi_beta,H_beta,Omega_beta)` be the GNS representation. Equation (5) gives

\[
\|\pi_\beta(E_n)\Omega_\beta\|^2=n^{-\beta}.
\tag{6}
\]

Hence the normalized conditioned vectors

\[
\xi_n^{(\beta)}
:=n^{\beta/2}\pi_\beta(E_n)\Omega_\beta
\tag{7}
\]

are canonical unit vectors. By (3) and (5),

\[
\begin{aligned}
G_\beta(m,n)
&=\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle\\
&=(mn)^{\beta/2}
\phi_\beta(E_mE_n)\\
&=(mn)^{\beta/2}
\operatorname{lcm}(m,n)^{-\beta}\\
&=\boxed{
\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta
}.
\end{aligned}
\tag{8}
\]

The last equality uses `gcd(m,n) lcm(m,n)=mn`.

Equation (8) is positive by construction, not by an arithmetic conjecture. It also depends only on the reduced multiplicative ratio:

\[
G_\beta(m,n)
=\prod_p p^{-\frac\beta2|v_p(m)-v_p(n)|}.
\tag{9}
\]

Thus it defines a positive-definite function on `Q_+^x`.

## 3. The Bost–Connes critical point forces exactly the Poisson radius `p^{-1/2}`

The rational Bost–Connes phase transition occurs at

\[
\beta_c=1.
\tag{10}
\]

Substituting this source-selected value into (8) gives

\[
G_1(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.
\tag{11}
\]

On the `p`-axis, put `m=p^a`, `n=p^b`. Then

\[
\boxed{
G_{1,p}(a,b)=p^{-|a-b|/2}.
}
\tag{12}
\]

Writing

\[
r_p:=p^{-1/2},
\tag{13}
\]

the positive-definite sequence `r_p^{|k|}` has the standard Poisson spectral density

\[
P_{r_p}(\theta)
=\frac{1-r_p^2}
{1-2r_p\cos\theta+r_p^2}
=1+2\sum_{k\ge1}r_p^k\cos(k\theta).
\tag{14}
\]

Therefore the critical conditional Gram is exactly the product prime-torus Poisson kernel whose one-prime Fourier moments are

\[
\widehat P_{r_p}(k)=p^{-|k|/2}.
\tag{15}
\]

This is a new provenance statement inside the current line. `WP-096`--`WP-100` analyzed Poisson/product positive kernels after the critical one-prime moments had been imposed as the target ray data. Equations (1)--(15) show that the **positive** Poisson moments themselves arise without such insertion from the Bost–Connes divisibility semilattice and its actual critical KMS state.

In particular, taking the vacuum integer `1`,

\[
\boxed{
\langle\xi_1^{(1)},\xi_{p^k}^{(1)}\rangle
=p^{-k/2}.
}
\tag{16}
\]

Unlike the KMS-midpoint mechanism of `WP-209`, (16) is a static conditional-state fidelity/overlap. It therefore evades the specific statement that one bounded correlation vector cannot carry the entire Mangoldt mass: the all-prime family appears as a positive Gram geometry of separately normalized conditioned vectors rather than as the finite spectral measure of one bounded vector.

## 4. The same source contains the logarithmic prime scale, but not in the Gram sign

The multiplicative generator has exact energy grade

\[
\delta(\mu_p)=i(\log p)\mu_p.
\tag{17}
\]

The logarithmic factor needed for `Lambda(p^k)=log p` is therefore present in the source before any Weil comparison. There is also a useful operator-level valuation identity in the standard positive-energy representation. Since `E_{p^k}` is the indicator of `p^k|n`,

\[
N_p:=\sum_{k\ge1}E_{p^k}
\tag{18}
\]

is the positive occupation operator with

\[
N_p\varepsilon_n=v_p(n)\varepsilon_n.
\tag{19}
\]

Consequently the standard Bost–Connes Hamiltonian has the monotone quadratic-form decomposition

\[
\boxed{
H
=\sum_p(\log p)N_p
=\sum_p\sum_{k\ge1}(\log p)E_{p^k}.
}
\tag{20}
\]

This is simply unique factorization written as a positive operator identity: `log n=sum_p v_p(n)log p`. It shows that prime-power indexing and the repetition-independent coefficient `log p` need not be manufactured by a scalar `F(H)` at all.

For `beta>1`, evaluating finite partial sums in the Gibbs KMS state and passing monotonically gives the classical identity

\[
\phi_\beta(H)
=\sum_{p,k\ge1}(\log p)p^{-k\beta}
=-\frac{\zeta'(\beta)}{\zeta(\beta)}.
\tag{21}
\]

This is prior-art classicalization, not a new zeta formula. At the critical state `beta=1`, the corresponding positive all-prime partial sums diverge:

\[
\sum_{p,k\ge1}\frac{\log p}{p^k}
=\sum_p\frac{\log p}{p-1}
=+\infty.
\tag{22}
\]

More importantly for the present route, the range projections are time-invariant:

\[
\sigma_t(E_n)=E_n,
\qquad
\delta(E_n)=0.
\tag{23}
\]

So applying the KMS midpoint or a time derivative directly to the conditional Gram cannot insert another square-root Boltzmann factor or the missing sign. The half-density in (16) comes from normalizing the conditioned KMS vectors; the `log p` comes from a different piece of the same source dynamics. Combining their magnitudes is canonical enough to survive the scalar-programmability control, but positivity still has to survive the orientation test.

## 5. Exact comparison with the finite Weil ray: the target is an indefinite defect

`WP-096` fixes the multiplicative Toeplitz normalization of the finite Weil prime ray. On the signed `p`-power grades, the desired nonzero Fourier coefficients are

\[
\varphi_W(p^k)
=-\frac{\log p}{p^{|k|/2}},
\qquad k\ne0.
\tag{24}
\]

Equations (14)--(15) show that these are exactly the nonconstant Fourier coefficients of

\[
\boxed{
D_p(\theta)
:=\log p\left(1-P_{p^{-1/2}}(\theta)\right).
}
\tag{25}
\]

Thus, in kernel notation,

\[
\boxed{
W_p=\log p\,(I-G_{1,p}),
}
\tag{26}
\]

where the diagonal coefficient is zero and every nonzero displacement has the exact finite-Weil value (24).

Equation (26) is the closest direct bridge found in this Bost–Connes fork: the arithmetic ray is not merely similar to the critical positive geometry; it is its zero-diagonal **defect**.

But the defect is not positive. At `theta=0`,

\[
P_r(0)=\frac{1+r}{1-r},
\]

so

\[
D_p(0)
=-\frac{2(\log p)r}{1-r}<0.
\tag{27}
\]

At `theta=pi`, `P_r(pi)=(1-r)/(1+r)<1`, hence

\[
D_p(\pi)>0.
\tag{28}
\]

The symbol changes sign. Therefore

\[
\boxed{
G_{1,p}\succeq0
\quad\not\Longrightarrow\quad
\log p(I-G_{1,p})\succeq0.
}
\tag{29}
\]

Adding a scalar diagonal `C_p I` repairs the one-prime defect if and only if

\[
C_p\ge
\frac{2(\log p)p^{-1/2}}{1-p^{-1/2}},
\tag{30}
\]

the exact one-prime threshold already underlying `WP-096`. If mixed-prime Fourier terms are prohibited, summing these thresholds over all primes diverges. `WP-097` proves that specially chosen mixed-prime product terms can instead give a finite global diagonal, but their local factors are an additional deformation

\[
1+\frac{\log p}{C}(1-P_{p^{-1/2}}),
\]

not the positive KMS conditional density `P_{p^{-1/2}}` itself. The Bost–Connes source therefore explains the Poisson factor but does not explain the affine sign reversal that makes its one-prime moments Weil-oriented.

## 6. Aggressive falsification

**Does this finally derive prime-power support without target coding?** In a meaningful but limited sense, yes. The family `E_{p^k}` is forced by the semigroup/divisibility structure, (20) forces the coefficient `log p`, and the critical KMS conditional overlap forces `p^{-k/2}`. This is strictly stronger than saying that an arbitrary positive `F(H)` can interpolate the desired sequence.

**Does the normalized Gram itself equal the finite Weil form?** No. Its nonzero ray moments have the opposite sign. Equation (26) shows that the finite Weil ray is a defect of the positive Gram, and (27)--(29) show that taking that defect destroys ordinary positivity.

**Can one flip the sign by multiplying conditioned vectors by phases?** A phase can make a chosen vacuum-to-vector overlap negative while preserving Gram positivity. That does not produce the Weil quadratic form: it changes only a representation-dependent Gram row, and arbitrary target weights can be hidden in vector scalings. The sign theorem must survive after the target is read out as a quadratic/boundary response, not merely after choosing phases for auxiliary vectors.

**Can the `log p` factor be obtained by differentiating the projection correlation?** No. Equation (23) puts every `E_n` in the time-invariant sector. Differentiating its time evolution gives zero. Differentiating the temperature dependence of (12) instead produces the wrong repetition factor `|a-b| log p`, the same thermodynamic multiplicity defect seen from a different angle in `WP-210`.

**Does the construction solve the global mass problem of `WP-209`?** It bypasses that particular finite-measure obstruction by using a Gram family rather than one bounded correlation vector. It does not solve the global Weil problem. The target-oriented defect needs divergent sparse self-energy unless mixed terms are introduced, and no archimedean or polar sector has appeared.

**Can the mixed terms already present in the full GCD Gram be declared the needed completion?** No. Their signs and magnitudes are the positive products in (9). The mixed completion of `WP-097` that supports negative one-prime Weil moments has different local factors. Passing from one to the other is precisely the unexplained sign-changing affine operation that the mandate requires the geometry itself to force.

**Does an archimedean term emerge from the same relation?** No. Equations (1)--(23) are finite-semigroup/KMS data. They generate neither the Euler–Gamma contribution nor the polar/global counterterms. Adding those later by hand would fail the same-source requirement.

**Is this special enough to distinguish the rational primes from generalized free generators?** Not by itself. For a free commutative semigroup with generator lengths `ell(q)` and a compatible KMS scaling, the same range-projection calculation gives a product kernel `exp[-beta/2 sum_q |a_q-b_q| ell(q)]`. The Bost–Connes source does nontrivially select its own critical `beta_c=1`, but the conditional-Gram mechanism remains a broad semigroup construction. This is another reason it cannot by itself imply a specifically Riemann global sign theorem.

## 7. Prior-art and novelty boundary

No novelty is claimed for the Bost–Connes algebra, its multiplicative isometries, its phase transition, its KMS states, its logarithmic Hamiltonian, or the partition function `zeta(beta)`. The durable source remains Bost and Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411–457, already recorded in this line's `SOURCES.md`. The KMS identity (5) is an immediate application of the defining time evolution and the KMS condition.

No novelty is claimed for GCD matrices or their positivity as an independent matrix-theory topic. A directed literature audit found the classical GCD-matrix tradition going back to H. J. S. Smith, and modern work such as Dominique Guillot and Jiaru Wu, *Total nonnegativity of GCD matrices and kernels*, Linear Algebra and its Applications **578** (2019), 156–184, arXiv:1901.01947. Likewise, the fact that `r^{|k|}` is positive definite with Poisson spectral density is classical harmonic analysis.

The Bost–Connes/Weil literature already connects the dynamical system, scaling, zeta thermodynamics and noncommutative trace constructions. The search did not identify a basis for claiming historical novelty for the normalized GCD kernel itself, and none is claimed.

The durable Mathia-specific delta is instead the **exact provenance-and-sign comparison** across already-audited structures:

\[
\boxed{
\text{BC divisibility semilattice}
+\text{KMS}_{\beta_c=1}\text{ conditioning}
\Longrightarrow
G_1(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}
\Longrightarrow
P_{p^{-1/2}}\text{ on every prime axis},
}
\tag{31}
\]

while the finite Weil ray in the existing multiplicative Toeplitz dictionary is exactly

\[
\boxed{
W_p=\log p(I-G_{1,p}),
}
\tag{32}
\]

and that defect is indefinite. This identifies a source-forced relation stronger than affiliation/scalar filtering and then falsifies its most direct sign mechanism without invoking RH or zero data.

## 8. Consequence for the research frontier

The Bost–Connes branch should no longer be described as lacking an intrinsic prime-power/critical-half-density geometry. It has one: critical KMS conditioning of the divisibility projections canonically produces the normalized GCD/Poisson Gram, while the time generator independently fixes the logarithmic prime scale.

The obstruction has moved to a sharper place. To obtain Weil positivity, a surviving construction must explain why the **defect** of this positive Gram, rather than the Gram itself, belongs inside a larger positive finite–archimedean form. That enlargement must force the necessary mixed-prime/global compensation, produce Gamma and polar terms from the same structure, and retain an independent sign theorem. Reusing the `WP-097` affine product completion without deriving its sign reversal and global coupling from Bost–Connes data would only reinsert the missing step.

This also gives a concrete disposition for the current Bost–Connes affiliation/conditioning clue: a non-programmable source relation exists and is mathematically productive, but it does **not** yet satisfy the clue's positive outcome because its exact Weil-oriented readout is the indefinite defect (32), with the archimedean/global sign mechanism still absent.
