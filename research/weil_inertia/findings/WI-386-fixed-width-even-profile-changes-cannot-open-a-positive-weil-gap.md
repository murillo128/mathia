# WI-386 — Fixed-width even profile changes cannot open a positive Weil gap

**Status:** `EXACT-DERIVED + CLASSICAL-WEIL-SPECTRAL-SIDE + CLASSICAL-ALMOST-PERIODICITY + PRIMARY-SOURCE-OPERATOR-AUDIT + DECISIVE-COERCIVITY-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-385 proved zero-floor saturation for the particular first-Dirichlet cosine profile used in WI-380. The cosine is not load-bearing for that phenomenon. Under RH, every sufficiently regular **fixed-width real even profile** produces the same asymptotic zero floor after the exact Desogus source holes are imposed. Thus changing the shape of the fixed-width lobe cannot create a positive Gate-II coercivity margin compatible with RH.

Fix `L>0` and let

\[
g\in C_c^2((-L/2,L/2);\mathbb R),
\qquad g(-s)=g(s),
\qquad \|g\|_2=1.
\tag{1}
\]

Write

\[
G(z)=\int_{\mathbb R}g(s)e^{zs}\,ds,
\qquad q=g*g,
\qquad Q(z)=G(z)^2=\int q(t)e^{zt}\,dt.
\tag{2}
\]

For `A>2L` define the unperforated separated odd pair

\[
f_A^0(y)=g(y-A/2)-g(y+A/2).
\tag{3}
\]

For the integer endpoint sequence

\[
A_k=\log(k+1),
\tag{4}
\]

let `f_k` be obtained from (3) by imposing the exact source-slot cutoffs of WI-377/WI-380 separately on the two lobes, with the same smooth screened cutoff convention. Then, **if RH holds**,

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k]=0.
}
\tag{5}
\]

The near-zero returns are relatively dense in the physical separation variable `A` before integer sampling, and the mesh `A_{k+1}-A_k\to0` transfers them to a subsequence of the exact endpoint lattice.

There is an equivalent layer-by-layer statement. Define

\[
R_g(x)=
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n x\right)
-2Q(1/2)\sqrt x,
\tag{6}
\]

\[
A_g=4\sum_{\gamma>0}m_\gamma Q(i\gamma),
\tag{7}
\]

and

\[
B_g=-C_\Gamma+
\frac12\iint h(|s-t|)|g(s)-g(t)|^2\,ds\,dt,
\qquad
h(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\tag{8}
\]

The same Guinand--Weil calculation as in WI-385, with no use of the cosine formula, gives under RH

\[
\boxed{A_g+2R_g(1)=2B_g.}
\tag{9}
\]

The source-perforated arithmetic-plus-polar layer satisfies

\[
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_g(k+1)-2R_g(1)+o(1),
\tag{10}
\]

while the archimedean layer satisfies

\[
Q_k^{\rm arch}=2B_g+o(1).
\tag{11}
\]

Under RH,

\[
\liminf_{k\to\infty}R_g(k+1)=-A_g,
\tag{12}
\]

so (9)--(12) again give (5). In particular, whenever `B_g<0` so that the fixed profile is genuinely gamma-negative, the recurrent arithmetic-polar reserve is exactly `-2B_g`: it repays the two-lobe archimedean debt and leaves no positive profile-dependent surplus.

If in addition

\[
G(z)\ne0\qquad(\Re z>0),
\tag{13}
\]

then the Landau--Pintz argument of WI-382 generalizes verbatim and gives the exhaustive stronger dichotomy

\[
\mathrm{RH}\Rightarrow\liminf_k\mathcal W[f_k]=0,
\qquad
\neg\mathrm{RH}\Rightarrow\liminf_k\mathcal W[f_k]=-\infty.
\tag{14}
\]

Hence the unconditional no-positive-tariff conclusion of WI-385 extends to every fixed-width even profile satisfying the off-axis detection condition (13). Without (13), only the RH-side zero-floor assertion (5) is claimed: a deliberately chosen transform could in principle screen an off-critical pole, so the non-RH branch must not be imported without that hypothesis.

The research consequence is sharper than WI-385's cosine-specific boundary. A surviving rooted/Schur proof cannot recover a fixed positive gap merely by choosing a better **fixed-width even lobe shape**. Under the very conclusion such a proof is intended to establish, every such profile has recurrent source-zero quasimodes with Weil energy tending to zero. A successful mechanism must instead use semidefinite positivity without a fixed tariff, an exact graph/domain restriction excluding this whole translated-profile class before the old form is tested, or genuinely non-fixed-width/nonlocal structure.

## 1. The spectral side makes the profile universality transparent

Desogus's restricted odd Weil criterion, independently reconstructed in WI-361, gives for a real odd compactly supported test with bilateral Laplace transform `F`

\[
\mathcal W[f]
=\sum_\lambda F(\lambda)\overline{F(-\bar\lambda)},
\tag{15}
\]

where `\lambda=\rho-1/2` runs over centered nontrivial zeros with multiplicity. Under RH, `\lambda=i\gamma`, and real oddness gives

\[
\mathcal W[f]
=\sum_\gamma |F(i\gamma)|^2.
\tag{16}
\]

For the separated pair (3), evenness of `g` gives

\[
F_A^0(z)
=G(z)\left(e^{Az/2}-e^{-Az/2}\right)
=2G(z)\sinh(Az/2).
\tag{17}
\]

Because `g` is real and even, `G(i\gamma)` is real. Therefore under RH

\[
\boxed{
\mathcal W[f_A^0]
=4\sum_\gamma m_\gamma
G(i\gamma)^2\sin^2(\gamma A/2).
}
\tag{18}
\]

The exact overall factor is immaterial for the floor, but the sign and phase structure are not: every coefficient is nonnegative, and the entire function vanishes at `A=0` because the two lobes coincide and cancel.

The regularity in (1) gives `G(i\gamma)=O((1+|\gamma|)^{-2})`. Together with `N(T)=O(T\log T)`, this makes the series in (18) absolutely and uniformly convergent in `A`. Thus

\[
E_g(A):=\mathcal W[f_A^0]
\tag{19}
\]

is a nonnegative Bohr uniformly almost-periodic function with

\[
E_g(0)=0.
\tag{20}
\]

Uniform almost periodicity implies that for every `epsilon>0` the set of `epsilon`-almost periods is relatively dense. At every such almost period `tau`,

\[
0\le E_g(\tau)<\epsilon.
\tag{21}
\]

There are therefore arbitrarily large and relatively densely spaced separations at which the unperforated exact Weil form returns arbitrarily close to zero. No linear-independence assumption on zeta ordinates is used; this is recurrence to the already attained configuration `A=0`, exactly as in WI-383.

This argument is more primitive than the arithmetic/gamma decomposition of WI-385. It shows directly that the zero floor is a spectral consequence of translating two copies of any fixed even profile apart while retaining the odd symmetry.

## 2. The endpoint lattice does not destroy recurrence

The actual nested operator is tested at

\[
A_k=\log(k+1).
\]

Its mesh satisfies

\[
A_{k+1}-A_k
=\log\!\left(1+\frac1{k+1}\right)
\longrightarrow0.
\tag{22}
\]

Choose a sequence of almost periods `tau_j\to\infty` for which `E_g(tau_j)\to0`, and choose `k_j` with `A_{k_j}` nearest to `tau_j`. Then

\[
|A_{k_j}-\tau_j|\to0.
\tag{23}
\]

A uniformly almost-periodic function is uniformly continuous, hence

\[
E_g(A_{k_j})-E_g(\tau_j)\to0.
\tag{24}
\]

Therefore

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_{A_k}^0]=0
}
\tag{25}
\]

under RH.

The logarithmic endpoint lattice is therefore not a possible escape from the fixed-profile quasimode mechanism. Its asymptotically vanishing mesh is much finer than the bounded-gap recurrence scale in `A`.

## 3. Exact source zeros perturb every fixed profile by `o(1)`

The cosine shape played no essential role in the source-perforation estimates of WI-384. Inside a fixed-width centered lobe, the exact Desogus source slots are generated only by prime powers. Their total measure is

\[
O_L\!\left(\frac1{\sqrt{x_k}\log x_k}\right),
\qquad x_k=k+1.
\tag{26}
\]

Let `chi_k` be the same smooth source-slot cutoff used in WI-377/WI-380 and set

\[
p_k=\chi_k g.
\tag{27}
\]

Since a fixed `C_c^2` profile is bounded,

\[
\|p_k-g\|_1
=O_g\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
\tag{28}
\]

With `q_k=p_k*p_k`, Young's inequality gives

\[
\|q_k-q\|_\infty
=O_g\!\left(\frac1{\sqrt{x_k}\log x_k}\right).
\tag{29}
\]

The Mangoldt weight in the critical fixed-factor annulus is `O_L(\sqrt{x_k})`, so the critical arithmetic-profile replacement costs only

\[
O_g(1/\log x_k)=o(1).
\tag{30}
\]

The leading polar moments change by the same order after multiplication by `\sqrt{x_k}`. The finite same-lobe prime-power sum converges term by term, so the exact argument of WI-384 gives (10), with `R_L` replaced by `R_g`.

For the archimedean term, the screened cutoff construction of WI-377 has total local jump cost tending to zero. Multiplying that cutoff by one fixed `C_c^2` profile changes only the bounded local amplitude and derivative constants; the capacity estimate is unchanged in order. Hence the screened difference seminorm of `p_k-g` tends to zero. Endpoint and Hankel-image terms also vanish because the lobe width remains fixed while its center recedes like `A_k/2`. Therefore one lobe converges in the localized archimedean form to `B_g`, and the full odd fold gives (11).

Equivalently, combining the three operator layers shows directly

\[
\boxed{
\mathcal W[f_k]-\mathcal W[f_{A_k}^0]\to0.
}
\tag{31}
\]

Together with (25), this proves the profile-universal RH implication (5).

## 4. The explicit-formula cancellation is profile-by-profile

Although Section 1 already proves the zero floor, the decomposition used by Gate II is clarified by a second derivation.

Apply the standard Guinand--Weil explicit formula to

\[
H(r)=Q(ir).
\tag{32}
\]

Because `q=g*g` is even, compactly supported, and `q(0)=\|g\|_2^2=1`, its inverse Fourier transform is exactly the physical kernel `q`. Under RH the zero side is

\[
\sum_\gamma Q(i\gamma)=\frac{A_g}{2}.
\tag{33}
\]

Exactly as in WI-385, rearrangement gives

\[
A_g+2R_g(1)
=2\left[
-\log\pi+
\frac1{2\pi}\int_{\mathbb R}
Q(ir)\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
\right].
\tag{34}
\]

The digamma integral representation and Fourier inversion use only `q(0)=1` and sufficient decay of `Q`; no cosine identity enters. They give

\[
-\log\pi+
\frac1{2\pi}\int Q(ir)\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)dr
=
-C_\Gamma+2\int_0^\infty h(u)(1-q(u))\,du.
\tag{35}
\]

Finally

\[
2\int_0^\infty h(u)(1-q(u))\,du
=
\frac12\iint h(|s-t|)|g(s)-g(t)|^2\,ds\,dt,
\tag{36}
\]

which is exactly `B_g+C_Gamma`. This proves (9).

Under RH, the same contour shift as WI-383 gives

\[
R_g(x)
=-4\sum_{\gamma>0}m_\gamma Q(i\gamma)
\cos(\gamma\log x)+O_g(x^{-1}).
\tag{37}
\]

Since `G(i\gamma)` is real,

\[
Q(i\gamma)=G(i\gamma)^2\ge0,
\tag{38}
\]

and the coefficients are absolutely summable. The trigonometric series in (37) is uniformly almost periodic and attains its global lower bound `-A_g` at logarithmic phase zero. Recurrence plus the vanishing lattice mesh therefore gives (12), even if the nonnegative scalar `A_g` happens to vanish.

Substitution into (10)--(11) yields

\[
\liminf_k\mathcal W[f_k]
=2B_g-A_g-2R_g(1)=0.
\tag{39}
\]

Thus the apparent stationary arithmetic reserve and the archimedean debt are not independently optimizable at fixed profile: the explicit formula locks them together for every admissible `g` in (1).

## 5. Off-line detection requires an extra transform hypothesis

The unconditional branch of WI-385 used a special feature of its cosine profile: its transform has no zero in `Re z>0`. For a generic compactly supported even profile that need not be true, so the distinction must be retained.

The Mellin transform of `R_g` has the same form as in WI-382,

\[
\mathcal M_g(s)
=2Q(s)\left(-\frac{\zeta'}{\zeta}(s+1/2)\right)
-\frac{2Q(1/2)}{s-1/2}
+H_g(s),
\tag{40}
\]

with `H_g` entire. An off-critical zero `rho` contributes a pole at `s=rho-1/2` with residue

\[
-2m_\rho Q(\rho-1/2).
\tag{41}
\]

If (13) holds, every zero with `Re rho>1/2` remains visible. The continuous Landau principle applied to a hypothetical eventual one-sided bound then gives exactly the WI-382 contradiction. Thus one-sided boundedness of `R_g` implies RH, and if RH is false its integer samples have arbitrarily deep negative excursions. Equations (10)--(11) then imply the second branch of (14).

Without (13), equation (41) exposes the genuine limitation: a zero of `G` can screen an off-line zeta pole from this particular smoothed remainder. No generic non-RH divergence is therefore claimed. This is the correct boundary between the profile-universal RH-side quasimode theorem and the stronger unconditional dichotomy available for RH-detecting profiles.

## 6. Consequence for the current Gate-II frontier

WI-385 ruled out a fixed positive tariff on one carefully chosen cosine-convolution family. The present result removes the obvious shape-optimization escape. If a rooted/Schur mechanism evaluates the exact old Weil form on the source-zero translations of **any fixed smooth even lobe**, then under RH that family contains recurrent asymptotic null vectors.

In particular, choosing a profile with a more favorable gamma Rayleigh quotient does not help. If `B_g<0`, equation (9) forces the corresponding recurrent arithmetic-polar floor to increase by exactly the amount needed to cancel that deeper archimedean debt. If `B_g>=0`, the profile was not a gamma-negative obstruction in the first place. There is no fixed-profile choice for which the same exact three-layer ledger leaves a positive asymptotic margin under RH.

This does not classify growing-width profiles `g_k`, profiles whose shape changes essentially with `k`, or nonlocal/multiscale trials. In those cases the coefficient family in (18) itself changes with `k`, so a single Bohr recurrence argument no longer supplies a common return time. It also does not refute a proof that imposes an exact graph/domain relation excluding these source-zero vectors before the old quadratic form is evaluated.

The next efficient audit is therefore the actual graph/domain restriction or a genuinely `k`-dependent profile mechanism. Re-optimizing a fixed width/shape against the gamma kernel is no longer a live route to a positive coercivity gap.

## 7. Prior-art and novelty audit

Every analytic ingredient is classical or already present in the audited local chain. The spectral representation (15)--(16) is the restricted odd Weil criterion reconstructed in WI-361 from the standard Weil explicit formula. Uniform recurrence of absolutely convergent trigonometric series is classical Bohr almost periodicity; WI-383 already anchors J. Kaczorowski and O. Ramaré, *Almost periodicity of some error terms in prime number theory*, Acta Arith. 106 (2003), 277--297, as nearby number-theoretic prior art. The profile-by-profile identity (9) is a direct specialization of the Guinand--Weil explicit formula, and the source-hole estimates are the prime-power sparsity mechanism of WI-377/WI-384.

A targeted search around Weil explicit formulas, autocorrelation test functions, almost-periodic zeta-zero sums, fixed-width translated odd tests, and the recent Desogus rooted-operator preprint did not locate the line-specific statement that **all fixed smooth even source-zero profile shapes recurrently saturate the exact localized Weil form at zero under RH**. The search did locate broad classical and recent almost-periodicity literature for arithmetic error terms, but not this source-perforated operator consequence. Search absence is not evidence of priority, and no priority claim is made.

The durable Mathia contribution is therefore the synthesis and route barrier: the cosine in WI-385 was not a special extremizer responsible for saturation. The zero floor follows from odd translation geometry plus the spectral side, survives exact prime-power source perforation, and is reflected layer-by-layer by the classical explicit formula.

## 8. Boundaries and falsification

- `g` is fixed as `k\to\infty`. Growing-width or genuinely changing profiles are not covered.
- Real evenness is load-bearing for the simple cancellation geometry in (17)--(20). A non-even positive lobe requires a separate phase/hull analysis.
- `C_c^2` is a convenient sufficient regularity class ensuring absolute summability. The result can likely be weakened, but no sharper minimal class is claimed.
- The RH-side result (5) does **not** require `G` to be zero-free off the imaginary axis. The non-RH divergence in (14) does require the detection hypothesis (13), or a weaker hypothesis guaranteeing that an off-critical right-half-plane pole survives the smoothing.
- The source-perforation transfer uses the exact fixed-width prime-power slot geometry audited in WI-377/WI-384. A corrected admissible domain that forbids these cutoffs would invalidate that transfer and would itself be the missing structural mechanism.
- No statement about the Montgomery/Weil simple-zero proportion is changed. This is a barrier for the current individual-defect/rooted Gate-II direction of the canonical research mandate.

The decisive falsification test is now structural: exhibit a load-bearing Gate-II domain/graph condition that the source-zero cutoffs above do not satisfy, or exhibit a genuinely `k`-dependent family for which the fixed-profile spectral recurrence cannot be transferred. A stronger estimate of the same fixed-profile three-layer quadratic form cannot produce a positive RH-compatible floor.