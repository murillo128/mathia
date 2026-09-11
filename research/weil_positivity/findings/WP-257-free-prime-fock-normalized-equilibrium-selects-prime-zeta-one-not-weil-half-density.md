# WP-257 — Free-prime Fock normalized equilibrium selects prime-zeta one, not the Weil half-density

**Status:** `EXACT-DERIVED + FREE-PRIME-FOCK + PRIME-ZETA-BOUNDARY + NORMALIZED-KMS-THRESHOLD + CRITICALITY-SEPARATION + SCALAR-CLOCK-RIGIDITY + WP256-CANONICITY-NARROWING + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-256` gives a genuine positive semifinite escape from `WP-255`: on the free Fock space over prime letters,

\[
T_1=P_{\rm simp}HN^{-1}e^{-H/2}\succeq0
\]

has the exact diagonal spectrum

\[
T_1e_w=\frac{\Lambda(n(w))}{\sqrt{n(w)}}e_w.
\]

That identity survives. But the free-Fock source contains **two different critical parameters**, and they must not be conflated.

The arithmetic one-particle partition function is the prime zeta function

\[
P(s):=\sum_p p^{-s}.
\]

Its abscissa of convergence is `s=1`. This makes `s=1` an intrinsic one-particle spectral boundary and explains why the semifinite weight at `beta=1` is not an arbitrary numerical insertion.

The normalized free-Fock equilibrium boundary is different. A Fock word of length `m` contributes total Boltzmann mass `P(beta)^m`, so the full Fock Gibbs partition sum is

\[
Z_{\mathcal F}(\beta)
=\sum_{m\ge0}P(\beta)^m
=\frac1{1-P(\beta)}
\]

whenever `P(beta)<1`. There is a unique number

\[
\boxed{\beta_* >1\quad\text{such that}\quad P(\beta_*)=1,}
\]

numerically `beta_* = 1.3994333287...`. The normal Fock Gibbs state exists only for `beta>beta_*`; the orthogonal-range KMS packing inequality of `WP-255` rules out every normalized KMS state for `beta<beta_*`. At the boundary `beta=beta_*`, the Fock trace itself is already infinite, although the standard Toeplitz--Cuntz equilibrium theory may admit a boundary state after passage to the appropriate quotient.

Consequently the exact Weil half-density in `WP-256` occurs at the **one-particle convergence boundary `beta=1`, inside the semifinite nonstate regime**, not at the normalized equilibrium threshold of the free-Fock system. If one instead lets normalized free-Fock thermodynamics select the parameter, the same intrinsic simple-spectrum/mean-energy construction gives

\[
P_{\rm simp}HN^{-1}e^{-\beta_*H/2}e_w
=\Lambda(n(w))n(w)^{-\beta_*/2}e_w,
\]

whose exponent is approximately `0.6997166643`, not `1/2`.

This is not a retraction of the operator identity in `WP-256`. It is a canonicity correction: **free-Fock normalized equilibrium does not independently select the Weil exponent**. The surviving source principle for `beta=1` is the one-particle arithmetic spectral boundary (and its agreement with the Bost--Connes/Weil critical parameter), not the free-Fock equilibrium phase transition.

## 1. The two intrinsic critical parameters are unequal

Let

\[
\mathcal K=\ell^2(\mathbb P),
\qquad
he_p=(\log p)e_p,
\]

and let

\[
\mathcal F
=\mathbb C\Omega\oplus\bigoplus_{m\ge1}\mathcal K^{\otimes m}
\]

be the full free Fock space from `WP-256`. The second-quantized word Hamiltonian satisfies

\[
He_{(p_1,\ldots,p_m)}
=\left(\sum_{j=1}^m\log p_j\right)e_{(p_1,\ldots,p_m)}.
\tag{1}
\]

On the one-particle space,

\[
\operatorname{Tr}_{\mathcal K}(e^{-s h})
=P(s)
:=\sum_p p^{-s}.
\tag{2}
\]

For `s>1`, `P(s)` is finite, continuous, and strictly decreasing. Euler's divergence of `sum_p1/p` gives

\[
P(s)\to+\infty
\qquad(s\downarrow1),
\tag{3}
\]

while `P(s)\to0` as `s\to+\infty`. Moreover

\[
P(2)
<\sum_{n\ge2}n^{-2}
=\zeta(2)-1
<1.
\tag{4}
\]

Hence by monotonicity there is a unique

\[
\boxed{\beta_*\in(1,2):P(\beta_*)=1.}
\tag{5}
\]

A direct prime-zeta evaluation gives

\[
\beta_*=1.3994333287263303\ldots.
\tag{6}
\]

Equation (2) therefore has its **convergence boundary** at `1`, whereas the value at which its finite value falls to total mass one is the strictly larger number `beta_*`.

Those are different source statements. The first is a one-particle spectral-dimension statement. The second is the packing/equilibrium threshold for an orthogonal Fock alphabet.

## 2. Full Fock normalization is controlled by `P(beta)=1`

For `beta>1`, summing the diagonal Gibbs weight over words of fixed length gives

\[
\begin{aligned}
\operatorname{Tr}_{\mathcal K^{\otimes m}}(e^{-\beta H})
&=\sum_{p_1,\ldots,p_m}
(p_1\cdots p_m)^{-\beta}\\
&=P(\beta)^m.
\end{aligned}
\tag{7}
\]

Thus

\[
Z_{\mathcal F}(\beta)
:=\operatorname{Tr}_{\mathcal F}(e^{-\beta H})
=\sum_{m\ge0}P(\beta)^m.
\tag{8}
\]

Therefore

\[
\boxed{
Z_{\mathcal F}(\beta)<\infty
\quad\Longleftrightarrow\quad
P(\beta)<1
\quad\Longleftrightarrow\quad
\beta>\beta_*.
}
\tag{9}
\]

For `beta>beta_*`, the normalized density

\[
\rho_\beta
=Z_{\mathcal F}(\beta)^{-1}e^{-\beta H}
\tag{10}
\]

defines the ordinary normal Gibbs/KMS state in the Fock representation.

The converse obstruction is already encoded without using the trace formula. The prime left-creation isometries `L_p` have orthogonal ranges and arithmetic dynamics

\[
e^{itH}L_pe^{-itH}=p^{it}L_p.
\tag{11}
\]

Any normalized `KMS_beta` state on a system retaining these normalized orthogonal eigen-isometries must satisfy, exactly as in `WP-255`,

\[
\phi_\beta(L_pL_p^*)=p^{-\beta}
\tag{12}
\]

and hence for every finite set of primes `F`,

\[
\sum_{p\in F}p^{-\beta}\le1.
\tag{13}
\]

Letting `F` increase gives the necessary condition

\[
P(\beta)\le1.
\tag{14}
\]

So no normalized KMS state preserving the free-prime eigen-isometry relations can exist for `beta<beta_*`. In particular,

\[
\boxed{1<\beta_*\quad\Longrightarrow\quad
\text{there is no normalized free-prime }KMS_1\text{ state}.}
\tag{15}
\]

At `beta=beta_*`, equation (8) diverges because the geometric ratio is exactly one. Classical Toeplitz--Cuntz/Pimsner KMS theory distinguishes this boundary from the finite-type Gibbs region and may realize the critical state on the corresponding quotient. That distinction does not affect the present argument: every normalized critical range mass is then `p^{-\beta_*}`, not `p^{-1}`.

## 3. The exact Mangoldt carrier exists at every parameter, but only `beta=1` has the Weil exponent

Retain the source-defined simple-spectrum projection `P_simp` and Fock number operator `N` of `WP-256`. For every `beta>0`, define the diagonal positive operator

\[
T_\beta
:=P_{\rm simp}HN^{-1}e^{-\beta H/2}.
\tag{16}
\]

The same multiplicity argument used in `WP-256` gives, on every word `w`,

\[
\boxed{
T_\beta e_w
=\Lambda(n(w))n(w)^{-\beta/2}e_w.
}
\tag{17}
\]

Indeed the simple positive energy eigenspaces are exactly the pure repeated-prime words `p^k`; there `HN^{-1}=log p` and `e^{-\beta H/2}=p^{-k\beta/2}`.

The exact finite Weil coefficient requires

\[
n^{-\beta/2}=n^{-1/2}
\quad\text{for all prime powers }n,
\tag{18}
\]

and therefore

\[
\boxed{\beta=1.}
\tag{19}
\]

But normalized free-Fock equilibrium requires `beta>=beta_*` at the packing level and the normal Gibbs state requires `beta>beta_*`. Thus the two demands are disjoint:

\[
\boxed{
\text{exact Weil half-density}
\quad\Longrightarrow\quad\beta=1<\beta_*
\quad\Longrightarrow\quad
\text{semifinite/nonstate regime}.}
\tag{20}
\]

If instead the Fock equilibrium threshold is used to select the exponent, then

\[
T_{\beta_*}e_w
=\Lambda(n(w))n(w)^{-\beta_*/2}e_w,
\tag{21}
\]

with

\[
\frac{\beta_*}{2}
=0.6997166643631651\ldots,
\tag{22}
\]

which is strictly different from the Weil exponent `1/2`.

This is the first decisive narrowing. The free-word multiplicity and mean-energy mechanism source-force the **shape** of the Mangoldt carrier once a temperature is specified, but the normalized free-Fock equilibrium law does not select the temperature needed by Weil.

## 4. Scalar rescaling of the arithmetic clock cannot reconcile the two boundaries

A possible objection is that inverse temperature depends on the units chosen for time/energy. Test the entire scalar-rescaling family

\[
H_c:=cH,
\qquad c>0.
\tag{23}
\]

Then

\[
e^{itH_c}L_pe^{-itH_c}=p^{ict}L_p
\tag{24}
\]

and the one-letter Boltzmann sum at inverse temperature `beta` is

\[
P(c\beta).
\tag{25}
\]

The normalized packing threshold is therefore determined by

\[
c\beta_c=\beta_*.
\tag{26}
\]

At that threshold, the Gibbs half-density is

\[
e^{-\beta_cH_c/2}
=e^{-\beta_*H/2},
\tag{27}
\]

independently of `c`. The corresponding simple-spectrum mean-energy carrier is

\[
P_{\rm simp}H_cN^{-1}e^{-\beta_cH_c/2}e_w
=c\Lambda(n(w))n(w)^{-\beta_*/2}e_w.
\tag{28}
\]

Changing the time unit therefore changes only the overall logarithmic scale `c`; it cannot change the exponent selected at normalized equilibrium. Even after an overall scalar normalization, the factor `n^{-\beta_*/2}` remains.

Equivalently, for **any** scalar-rescaled arithmetic clock, exact Weil half-density requires

\[
c\beta=1,
\tag{29}
\]

whereas normalized orthogonal-prime KMS packing requires

\[
c\beta\ge\beta_*>1.
\tag{30}
\]

The contradiction is invariant under energy units.

Thus one cannot repair the mismatch by declaring that the normalized Fock phase transition should occur at inverse temperature one. Choosing `c=beta_*` indeed makes `beta_c=1`, but then the critical half-density is `p^{-\beta_*/2}`, not `p^{-1/2}`.

A further scalar spectral factor such as `e^{(\beta_*-1)H/2}` can of course algebraically convert (21) back to (17) at `beta=1`. But such a factor is an additional target-sensitive operation unless the source independently derives it. It is not supplied by normalized Fock equilibrium and therefore does not answer the source-selection requirement of this research line.

## 5. Why `beta=1` is still source-visible, but in a different sense

The result should not be overread as saying that `beta=1` is numerology. Equation (3) makes `1` canonical for the one-particle prime Hamiltonian: it is the abscissa at which

\[
\operatorname{Tr}_{\mathcal K}(e^{-\beta h})
\tag{31}
\]

ceases to be finite. The same arithmetic parameter is also the Bost--Connes critical inverse temperature and is exactly the parameter at which KMS range masses would be `1/p` and their square roots `p^{-1/2}`.

What fails is a stronger statement: the **free-Fock normalized thermodynamics** does not select that value. Free tensoring changes the normalization problem from convergence of the one-particle trace to the stricter condition that the one-particle Boltzmann mass be at most one.

Hence the correct provenance statement for `WP-256` is:

\[
\boxed{
\text{prime one-particle spectral boundary }\beta=1
+\text{semifinite free Fock weight}
+\text{simple spectral multiplicity}
+\text{mean word energy}
\Longrightarrow
\frac{\Lambda(n)}{\sqrt n}.
}
\tag{32}
\]

It is **not**:

\[
\text{normalized free-Fock equilibrium criticality}
\Longrightarrow
\frac{\Lambda(n)}{\sqrt n}.
\tag{33}
\]

The distinction matters because the research mandate asks for positivity to be forced by intrinsic geometry before the arithmetic target is recognized. If future work uses the semifinite carrier, it must state what independent geometric principle promotes the one-particle convergence boundary `beta=1` to the parameter of the global pairing. Normalized free-Fock equilibrium cannot provide that principle.

## 6. Matched controls and falsification

The separation is generic. Let a countable free alphabet have positive one-letter energies `epsilon_j`, and define

\[
P_\epsilon(s)
:=\sum_j e^{-s\epsilon_j}.
\tag{34}
\]

Whenever the free-Fock Gibbs trace is meaningful,

\[
Z_\epsilon(s)
=\sum_{m\ge0}P_\epsilon(s)^m.
\tag{35}
\]

Thus normalized Fock Gibbs equilibrium requires `P_epsilon(s)<1`, and orthogonal-range KMS packing requires at least `P_epsilon(s)<=1`. If `s_0` is some distinct source boundary at which a desired half-density is read, there is no reason for

\[
P_\epsilon(s_0)=1.
\tag{36}
\]

For prime energies, the mismatch is especially sharp because the desired Weil exponent fixes `s_0=1`, while `P(1)=+infinity`.

**Finite-alphabet control.** With finitely many letters, the same distinction remains but there is no prime-zeta convergence singularity. The equilibrium threshold is the unique solution of a finite Boltzmann sum equal to one. This confirms that the `P=1` boundary is ordinary free-Fock normalization physics, not an RH-specific phenomenon.

**Generalized-prime control.** Any multiplicatively independent generalized-prime alphabet with one-particle energies `log q_j` reproduces the same word-multiplicity selector. Its normalized free-Fock threshold is determined by `sum_j q_j^{-beta}=1`, while the target half-density of that generalized system would have to be justified separately. This reinforces the `WP-256` matched control: diagonal positivity of the carrier is generic free-word geometry.

**Boundary-state control.** Passing from the Toeplitz algebra to a Cuntz/Pimsner quotient at `P(beta_*)=1` may restore a normalized boundary KMS state in the classical equilibrium theory. It does not alter the Boltzmann exponent: its prime range masses are still `p^{-beta_*}`. The quotient therefore does not recover the Weil half-density.

**Overlap control.** Bost--Connes avoids this free-Fock threshold because its prime range projections overlap according to divisibility rather than being orthogonal. It can support normalized critical masses `1/p` at `beta=1`, exactly as `WP-255` explains. But `WP-216` then returns the independent orientation obstruction: the canonical positive GCD/Poisson Gram has the finite Weil ray as an indefinite defect. Thus moving back to overlap repairs temperature selection but not the Weil sign.

**Semifinite control.** `WP-256` remains a genuine escape from the normalized-state obstruction. A faithful normal semifinite Gibbs weight on `B(F)` exists at `beta=1` even though its value on the identity is infinite. This finding does not rule out a global Weil pairing built in that semifinite category. It proves only that such a pairing cannot cite normalized free-Fock equilibrium as the independent reason why the exponent is `1/2`.

## 7. Prior art and novelty boundary

The equilibrium mathematics is classical. Laca and Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, J. Funct. Anal. **211** (2004), 457--482, arXiv:`math/0304435`, characterize KMS states of quasi-free Toeplitz--Pimsner/Cuntz--Pimsner dynamics through trace and finite-frame inequalities. In the orthogonal scalar free-Fock case those inequalities reduce to the same Boltzmann packing condition used above.

Exel and Laca, *Partial Dynamical Systems and the KMS Condition*, Comm. Math. Phys. **232** (2003), 223--277, arXiv:`math/0006169`, analyze infinite Toeplitz--Cuntz--Krieger systems with quasi-free weights and identify phase structure through abscissae and associated Dirichlet-series critical values. This is direct prior art for treating the free-alphabet normalization threshold as an equilibrium phase boundary rather than a new phenomenon.

The prime zeta function `P(s)=sum_p p^{-s}`, its abscissa `1`, and the numerical root `P(beta_*)=1` are classical. No historical novelty is claimed for equations (2)--(15), the free-Fock partition sum, or the existence of the scalar clock-rescaling invariant `c beta`.

The durable Mathia-specific result is the **comparison with the exact live carrier of `WP-256`**:

\[
\boxed{
\text{normalized free-prime equilibrium selects }c\beta\ge\beta_*>1,
\qquad
\text{exact Weil half-density forces }c\beta=1.
}
\tag{37}
\]

The incompatibility is exact, survives scalar rescaling of the arithmetic clock, and leaves only the semifinite/one-particle-boundary interpretation of `WP-256` alive.

A bounded literature audit across quasi-free Pimsner KMS theory, infinite Toeplitz--Cuntz equilibrium, and prime-energy systems found the general phase-transition mechanism to be standard. No source found an independent Weil-positivity theorem arising from selecting the one-particle prime-zeta abscissa inside this free-Fock semifinite regime. The retained contribution is therefore a canonicity narrowing, not a claim of a new KMS phase transition.

## 8. Consequence for the Weil-positivity mandate

`WP-256` remains an important positive intermediate: a single source-defined semifinite free-word geometry can reconstruct prime-power support, the repetition-independent `log p`, and the critical `p^{-k/2}` coefficient without zeros. `WP-257` identifies exactly what that success does **not** provide.

The free-Fock system cannot derive the Weil exponent from normalized equilibrium. Its normalized packing boundary occurs at `beta_* >1`, and every scalar rescaling of the arithmetic clock leaves the boundary exponent equal to `beta_*/2`. The Weil exponent `1/2` is instead tied to the one-particle prime-zeta boundary and can only be used in the free-Fock model after accepting a genuinely semifinite infinite-mass weight.

This sharpens the surviving research question. A successful continuation must explain why the one-particle boundary `beta=1` is the parameter of an independently positive **global** finite--archimedean pairing, rather than merely the parameter at which a diagonal coefficient carrier matches Weil. It must then solve the orientation problem already isolated by `WP-009`, `WP-216`, and `WP-256`, produce the Gamma and polar sectors, and survive generalized-alphabet controls.

Any continuation that says only "the Fock KMS critical point gives `p^{-1/2}`" should now be rejected: the normalized Fock critical point gives `p^{-beta_*/2}`. The exact Weil half-density is available only after making the category change to a semifinite weight and selecting the one-particle arithmetic boundary. That route remains open, but its source-selection burden is now explicit.