# WP-226 — Zero-frequency self-pairing of the Bost–Connes Weil defect is positive but squares the critical half-density

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + SOURCE-TIME-CONDITIONAL-EXPECTATION + OPPOSITE-BOHR-MODE-PAIRING + POSITIVE-ZERO-MODE-ENERGY + HALF-DENSITY-SQUARED + CROSS-PRIME-RESONANCE-ABSENT + CRITICAL-KMS-DIVERGENCE + MATCHED-CONTROL + PRIOR-ART-CLASSICAL-CONDITIONAL-EXPECTATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-225` closes every normal positive operation which acts **linearly** on the critical Bost--Connes finite Weil defect while remaining covariant with the original source time evolution: the defect has no zero-Bohr-frequency component, so a covariant positive image is either zero or indefinite. Its sharp boundary leaves open a natural nonlinear-looking but geometrically standard escape: first pair opposite time modes, then project the product to zero frequency. A product of a mode of frequency `omega` with one of frequency `-omega` can be time invariant even when neither factor is.

For the source-forced finite-prime defect of `WP-216`, the most canonical such repair can be computed exactly. Let `E_F` denote the normal conditional expectation onto the fixed-point algebra of the finite-prime Bost--Connes time action. Then

\[
\boxed{
D_F:=E_F(W_F^2)\succeq0.
}
\tag{1}
\]

Thus opposite-frequency pairing really does escape the *linear* hollowness theorem of `WP-225`: it manufactures a nonzero positive zero-frequency object from the same defect without choosing a sign by hand.

However, it does so in exactly the wrong way for Weil positivity. On each prime ray the pairing squares both pieces of the critical finite coefficient,

\[
(\log p)p^{-k/2}
\quad\longmapsto\quad
(\log p)^2p^{-k},
\tag{2}
\]

and unique factorization kills every cross-prime zero-frequency term. Consequently `D_F` is an **additive sum of independent prime self-energies**, not a global mixed-prime form. In the canonical critical KMS cylinder state its exact value is

\[
\boxed{
\varphi_{1,F}(D_F)
=
\sum_{p\in F}(\log p)^2\frac{p+2}{p^2-1},
}
\tag{3}
\]

which diverges as `F` exhausts the primes. Taking a square root mode by mode would recover the finite magnitude only by a nonlinear post-processing that discards the additive quadratic geometry and still supplies no Weil orientation, Gamma sector, or polar term.

Therefore **canonical self-doubling of the source defect is not the missing global sign mechanism**. A surviving opposite-frequency construction must pair the finite defect with a genuinely different source sector -- most plausibly an archimedean or nonseparable mixed-prime sector -- before the zero-mode projection. Merely pairing the finite object with its own adjoint/conjugate converts the critical half-density into ordinary squared energy and leaves the primes separated.

## 1. Prime-axis mode decomposition

Fix a finite prime set `F` and use the exponent Hilbert space

\[
\mathcal H_F
=
\ell^2(\mathbb N_0^F).
\tag{4}
\]

For one prime `p`, write

\[
q_p=p^{-1/2},
\qquad
\ell_p=\log p,
\tag{5}
\]

and let `S_p` be the unilateral shift on the `p`-exponent coordinate. The critical conditioned Gram from `WP-216` is the Toeplitz operator

\[
G_p(a,b)=q_p^{|a-b|}.
\tag{6}
\]

Because `0<q_p<1`, its shift expansion converges in operator norm:

\[
G_p
=
I+
\sum_{k\ge1}q_p^k
\left(S_p^k+S_p^{*k}\right).
\tag{7}
\]

Hence the finite Weil defect is

\[
\boxed{
W_p
=
\ell_p(I-G_p)
=
-\ell_p
\sum_{k\ge1}q_p^k
\left(S_p^k+S_p^{*k}\right).
}
\tag{8}
\]

The finite-prime defect is

\[
W_F=\sum_{p\in F}W_p,
\tag{9}
\]

with each `W_p` acting on its own tensor factor.

The source Hamiltonian is

\[
H_F e_\alpha
=
\left(\sum_{p\in F}\alpha_p\log p\right)e_\alpha,
\tag{10}
\]

so

\[
\tau_t(S_p^k)=e^{ikt\log p}S_p^k,
\qquad
\tau_t(S_p^{*k})=e^{-ikt\log p}S_p^{*k}.
\tag{11}
\]

Equation (8) therefore resolves `W_p` into the exact nonzero Bohr modes `\pm k\log p`. This is the mode statement used abstractly in `WP-225`, now with the amplitudes retained.

## 2. The canonical zero-mode square is positive

Let

\[
\mathbb E_F(X)
=
\operatorname*{w^*\! -lim}_{T\to\infty}
\frac1{2T}\int_{-T}^{T}\tau_t(X)\,dt.
\tag{12}
\]

For the present pure-point action this is simply the normal conditional expectation onto the energy diagonal. It is positive, unital, and source defined. Since `W_F=W_F^*`,

\[
W_F^2\succeq0
\quad\Longrightarrow\quad
D_F:=\mathbb E_F(W_F^2)\succeq0.
\tag{13}
\]

This is a genuine independent positivity theorem. The sign in (13) is not inferred from RH, zero data, or a target-fitted kernel.

For one prime, multiply (8) by itself. The only products with zero total Bohr frequency are those pairing `+k\log p` with `-k\log p`. Therefore

\[
\boxed{
D_p
:=\mathbb E_p(W_p^2)
=
\ell_p^2
\sum_{k\ge1}p^{-k}
\left(S_p^{*k}S_p^k+S_p^kS_p^{*k}\right).
}
\tag{14}
\]

Since `S_p^{*k}S_p^k=I`, every summand in (14) is positive. On the exponent basis,

\[
\begin{aligned}
\langle e_a,D_pe_a\rangle
&=
\ell_p^2
\sum_{k\ge1}p^{-k}
\left(1+\mathbf 1_{a\ge k}\right)\\
&=
\boxed{
(\log p)^2\frac{2-p^{-a}}{p-1}
}.
\end{aligned}
\tag{15}
\]

Thus the zero-mode self-energy is nonzero and positive already on every one-prime cylinder. This explicitly demonstrates why `WP-225` had to leave quadratic mode pairing outside its linear channel theorem.

## 3. The half-density and logarithmic scale are both squared

Equation (14) retains the contribution of the resolved `k`th prime mode with coefficient

\[
\boxed{
(\log p)^2p^{-k}.
}
\tag{16}
\]

The finite-place Weil amplitude carried by the original defect is instead

\[
\boxed{
(\log p)p^{-k/2}.
}
\tag{17}
\]

The ratio of (16) to (17) is

\[
(\log p)p^{-k/2},
\tag{18}
\]

which depends on both `p` and `k`. No universal scalar normalization converts the quadratic zero-mode energy back to the Weil ray.

One can of course take the square root of the positive mode weight in (16). That operation returns the absolute magnitude in (17), but it is not a quadratic-form theorem: it is a modewise nonlinear readout performed *after* the orientation has been erased by `A\mapsto A^*A`. It therefore falls on the same side of the research mandate as replacing an indefinite operator by its absolute value. The missing sign has not been explained; it has been discarded.

This distinction also separates the present calculation from `WP-209`--`WP-212`. Those findings classify positive KMS correlation/canonical-correlation metrics when one asks them to **generate** the Weil spectral carrier from a bounded equilibrium observable. Here the observable is no longer arbitrary: `WP-216` has already source-forced the exact finite defect. The question is whether the canonical opposite-frequency self-pairing of that specific defect can orient it. Equations (14)--(18) answer that later question negatively.

## 4. Unique factorization forbids cross-prime zero-mode rescue

The square of (9) contains cross terms `W_pW_r` for distinct primes `p\ne r`. A typical product of homogeneous components has total frequency

\[
\pm k\log p\pm j\log r,
\qquad k,j\ge1.
\tag{19}
\]

If such a frequency vanished, then either

\[
p^k=r^j
\tag{20}
\]

or

\[
p^kr^j=1.
\tag{21}
\]

Neither is possible for distinct primes and positive `j,k`. Therefore

\[
\boxed{
\mathbb E_F(W_pW_r)=0
\qquad(p\ne r),
}
\tag{22}
\]

and hence

\[
\boxed{
D_F
=
\sum_{p\in F}D_p.
}
\tag{23}
\]

This is a stronger failure than mere coefficient mismatch. The canonical source-time self-pairing cannot create the mixed-prime incidence repeatedly identified as missing by this research line. It removes all such cross terms by exact frequency arithmetic.

The result is not a generic statement that zero-frequency pairing can never couple places. It says that **self-pairing the existing finite defect cannot do so**. A second sector with frequencies exactly opposite to the finite modes could produce genuine mixed zero-frequency terms; that is one of the surviving boundaries below.

## 5. Exact critical KMS energy and all-prime divergence

For finite `F`, the critical Bost--Connes cylinder state is normal on `B(\mathcal H_F)` and factorizes over the prime coordinates. On one prime coordinate its diagonal density is

\[
\rho_p
=
(1-p^{-1})
\sum_{a\ge0}p^{-a}|e_a\rangle\langle e_a|.
\tag{24}
\]

This is the finite-cylinder form of the source relation `\varphi_1(E_{p^a})=p^{-a}` used in `WP-216`. In particular,

\[
\varphi_{1,p}(S_p^kS_p^{*k})=p^{-k}.
\tag{25}
\]

Applying the state to (14) gives

\[
\begin{aligned}
\varphi_{1,p}(D_p)
&=(\log p)^2
\sum_{k\ge1}p^{-k}(1+p^{-k})\\
&=(\log p)^2
\left(\frac1{p-1}+\frac1{p^2-1}\right)\\
&=
\boxed{
(\log p)^2\frac{p+2}{p^2-1}.
}
\end{aligned}
\tag{26}
\]

Cross-prime terms vanish by (22), so (3) follows.

As `F` exhausts the primes,

\[
\sum_p
(\log p)^2\frac{p+2}{p^2-1}
\tag{27}
\]

diverges. Indeed the summand is asymptotic to `(\log p)^2/p`, and for all sufficiently large primes it is larger than `1/p`; Euler's divergence of the reciprocal-prime series suffices.

The same obstruction is visible before taking the KMS expectation. At the vacuum vector, (15) gives

\[
\langle e_0,D_pe_0\rangle
=
\frac{(\log p)^2}{p-1},
\tag{28}
\]

whose all-prime sum also diverges. Thus the failure is not an artifact of one particular scalar KMS readout.

## 6. Matched controls and prior-art boundary

Nothing in the positivity mechanism (12)--(14) is Riemann-specific. Replace the primes by any multiplicatively independent family `b_j>1`, take source energies `\log b_j`, and use the critical-looking Toeplitz amplitudes `b_j^{-k/2}`. The same calculation gives positive zero-mode energies

\[
(\log b_j)^2b_j^{-k}
\tag{29}
\]

and kills cross terms whenever the source energies have no integer resonances. This is the appropriate matched control: the positivity comes from ordinary Hilbert/operator squaring plus symmetry projection, not from a global arithmetic sign law.

The operator-algebraic ingredients are classical. The existence and positivity of conditional expectations onto modularly invariant von Neumann subalgebras is part of Takesaki's conditional-expectation theory; see Masamichi Takesaki, *Conditional expectations in von Neumann algebras*, Journal of Functional Analysis **9** (1972), 306--321, DOI `10.1016/0022-1236(72)90004-3`. The decomposition into time/symmetry modes and the fact that symmetric processing respects those modes is standard harmonic analysis; a modern quantum-information formulation is Iman Marvian and Robert W. Spekkens, *Modes of asymmetry: the application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, Physical Review A **90** (2014), 062110, DOI `10.1103/PhysRevA.90.062110`, arXiv `1312.0680`.

No novelty is claimed for conditional expectations, GNS/standard-form quadratic norms, or opposite-frequency multiplication. Bost and Connes already supply the logarithmic time evolution in the arithmetic quantum statistical system. The durable delta here is the exact placement of the **source-forced `WP-216` Weil defect** under the canonical quadratic zero-mode operation: the result is positive, but its resolved coefficients are squared, its cross-prime part vanishes identically, and its critical all-prime energy diverges.

The closest internal prior art is `WP-209`--`WP-212` on KMS correlation metrics and `WP-217` on the Poisson-score realization. Those results act on spectral/correlation carriers before the `WP-216` defect is fixed, or on the score of its positive Gram. They do not compute the zero-frequency conditional expectation of the square of the later source-forced hollow defect. `WP-225` supplies the immediate logical predecessor by identifying opposite-frequency pre-assembly as an explicit escape from its linear covariance theorem.

## 7. Aggressive falsification and exact boundary

Several stronger constructions remain outside the result and should not be conflated with this self-pairing failure.

First, an **active finite--archimedean bilinear coupling** can have new zero modes. If an archimedean or global sector contains a source-forced component of frequency `-k\log p`, then a cross term with the finite `+k\log p` mode can survive the time projection. Equation (22) does not apply because the second frequency is no longer another prime self-mode. Such a mechanism would have to derive the matching continuum/discrete incidence before inspecting the Weil coefficients and simultaneously account for the Gamma and polar terms.

Second, enlarging the time representation can introduce genuine degeneracies or resonances. The simple-spectrum/unique-factorization argument only classifies the original finite-prime source action and its self-square. A new source-derived representation with additional zero-frequency multiplicity may carry information invisible here.

Third, an unbounded closable form, relation-valued response, cohomological pairing, or intersection form need not be obtained as `E_F(W_F^2)`. The result rules out the **canonical quadratic self-energy**, not every nonlinear or unbounded completion.

Fourth, a target-dependent diagonal insertion between the two copies of `W_F` can obviously alter (16). For example a freely chosen energy-dependent multiplier could divide by part of the squared amplitude. Such a construction is not excluded algebraically; it fails the source-selection gate unless that multiplier is independently forced by Bost--Connes/global geometry and survives matched controls.

The research boundary after `WP-226` is therefore sharper:

\[
\boxed{
\text{linear source-time-covariant processing}
\ \text{fails by }WP\text{-225},
}
\]

while

\[
\boxed{
\text{canonical opposite-mode self-pairing}
\ \text{is positive but squares the carrier and stays prime-separable}.
}
\tag{30}
\]

A live Bost--Connes route must now obtain its zero-frequency positivity from **interaction with additional source structure**, not from the finite defect alone. The most relevant surviving test is precisely the one already isolated by the line's finite--archimedean-incidence frontier: keep the signed finite modes intact until they interact with a genuinely global/archimedean sector, and only then ask whether the assembled object has an independent positive form.