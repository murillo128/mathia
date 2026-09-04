# ANF-023 — iid lattice perturbations pay a unit diffuse tax when they cloak the first Bragg peak

**Status:** `EXACT-DERIVED + LITERATURE-BRIDGE + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-020` asks whether the closed convex finite-configuration diffraction body can reach the Montgomery--Taylor order interval

\[
0\le \mu\le \nu_a,
\qquad
\nu_a:=a\,\delta_0+a|h|\,dh,
\qquad
0<a<1,
\]

with the zeta application at

\[
a=a_{\rm MT}=C_{\rm MT}^{-1}=0.753296067856070\ldots .
\]

`ANF-022` rules out convex mixtures of *unperturbed* lattice scales, but a standard way to destroy crystalline Bragg peaks while retaining hyperuniformity is to perturb every lattice site independently. That escape also fails, for a reason sharper than a small-wave-number asymptotic.

Take a one-dimensional lattice of density `rho>0`, with sites `n/rho`, and displace the sites independently by identically distributed real random variables `U_n`. Let

\[
\varphi(h):=\mathbb E\,e^{-2\pi i hU_0}
\]

be the characteristic function of the displacement law. The expected per-particle diffraction measure is

\[
\boxed{
\mu_{\rho,\varphi}
=
\rho\sum_{m\in\mathbb Z}|\varphi(m\rho)|^2\,\delta_{m\rho}
+
\bigl(1-|\varphi(h)|^2\bigr)\,dh.
}
\tag{1}
\]

Then, for **every** `0<a<1`, every `rho>0`, and every displacement probability law,

\[
\boxed{
\mu_{\rho,\varphi}
\not\le
 a\bigl(\delta_0+|h|\,dh\bigr)
\quad\text{on }(-1,1).
}
\tag{2}
\]

The obstruction is an exact **cloaking tax**. The forward atom forces `rho<=a`, so the first reciprocal-lattice frequency `h=rho` lies inside the support-one band. Domination by an atomless target away from zero then forces the first Bragg peak to be cloaked, hence `varphi(rho)=0`. But the same zero transfers all intensity at that frequency into the diffuse part, whose density becomes exactly `1`. The target permits only `a rho`, giving

\[
1\le a\rho\le a^2<1,
\]

a contradiction.

Thus independent positional disorder cannot rescue the crystalline route eliminated in `ANF-022`. Even a displacement law tuned to cloak *all* Bragg peaks necessarily pays too much diffuse intensity at the first reciprocal vector for the Montgomery--Taylor band budget.

## 1. The perturbed-lattice diffraction formula follows directly from finite samples

For `N>=1`, consider the random finite configuration

\[
X_N
=
\left\{
\frac n\rho+U_n:0\le n<N
\right\}.
\]

At frequency `h`, put

\[
A_N(h):=
\sum_{n=0}^{N-1}
 e^{-2\pi i h(n/\rho+U_n)}.
\]

Independence and identical distribution give, for `n\ne m`,

\[
\mathbb E
\left[e^{-2\pi i h(U_n-U_m)}\right]
=|\varphi(h)|^2.
\]

Hence

\[
\begin{aligned}
\frac1N\mathbb E|A_N(h)|^2
&=1+
|\varphi(h)|^2
\left(
\frac1N\left|
\sum_{n=0}^{N-1}e^{-2\pi ihn/\rho}
\right|^2-1
\right)\\
&=
1-|\varphi(h)|^2
+
|\varphi(h)|^2 F_{N,\rho}(h),
\end{aligned}
\tag{3}
\]

where

\[
F_{N,\rho}(h)
:=
\frac1N\left|
\sum_{n=0}^{N-1}e^{-2\pi ihn/\rho}
\right|^2.
\]

The same Fejer limit used in `ANF-022` gives, weak-* on compact frequency windows,

\[
F_{N,\rho}(h)\,dh
\overset{*}{\longrightarrow}
\rho\sum_{m\in\mathbb Z}\delta_{m\rho}.
\tag{4}
\]

Every characteristic function is continuous. Multiplying the Fejer measures by the bounded continuous function `|varphi|^2` and passing to the limit in (3) proves (1):

\[
\frac1N\mathbb E|A_N(h)|^2dh
\overset{*}{\longrightarrow}
(1-|\varphi(h)|^2)dh
+
\rho\sum_m|\varphi(m\rho)|^2\delta_{m\rho}.
\tag{5}
\]

No density, moment, smoothness, or tail assumption on the displacement law is needed. A uniform global shift may be added to stationarize the perturbed lattice without changing pair differences or the diffraction formula.

Equation (1) is the standard independently perturbed-lattice structure-factor identity in the language used by Gabrielli and by Klatt--Kim--Torquato. The derivation above fixes the exact normalization needed here from finite configurations, so the no-go below does not depend on importing a convention from that literature.

## 2. The forward atom puts the first reciprocal vector inside the band

Assume for contradiction that

\[
\mu_{\rho,\varphi}\le\nu_a
\quad\text{on }(-1,1)
\tag{6}
\]

for some `0<a<1`.

Since `varphi(0)=1`, the atom of (1) at the origin has mass exactly `rho`. The target atom has mass `a`, so

\[
\boxed{\rho\le a<1.}
\tag{7}
\]

Therefore the first nonzero reciprocal-lattice frequency

\[
h_1:=\rho
\]

lies strictly inside `(0,1)`. This is the load-bearing coupling that makes a support-one envelope much stronger than a merely local hyperuniformity test: reducing the forward atom automatically pulls the first Bragg location into the observed band.

## 3. Cloaking the first Bragg peak forces unit diffuse intensity at the same frequency

The target `nu_a` has no atom at `h=rho`. The source measure (1) has there the nonnegative atom

\[
\rho|\varphi(\rho)|^2\delta_\rho.
\]

Measure domination (6) therefore forces

\[
\boxed{\varphi(\rho)=0.}
\tag{8}
\]

This is exactly the first-Bragg cloaking condition for an iid perturbed lattice.

The absolutely continuous part of (6) simultaneously implies

\[
1-|\varphi(h)|^2\le a|h|
\quad\text{for a.e. }|h|<1.
\tag{9}
\]

Both sides are continuous. If (9) failed at one point, it would fail on an interval of positive Lebesgue measure, contradicting measure domination. Thus (9) holds pointwise throughout the open band. Evaluating it at the forced zero (8) yields

\[
1
=1-|\varphi(\rho)|^2
\le a\rho.
\tag{10}
\]

Combining (7) and (10),

\[
\boxed{
1\le a\rho\le a^2<1,
}
\tag{11}
\]

which is impossible. This proves (2).

The argument does not need the displacement process to have a particular hyperuniformity exponent. It also does not need a Taylor expansion such as `1-|varphi(h)|^2=O(h^2)`. The contradiction occurs at the finite frequency of the first reciprocal vector and therefore survives heavy-tailed or nonsmooth displacement laws.

## 4. The obstruction survives mixing displacement laws at fixed density

There is a small convex extension that is useful for the `ANF-020` viewpoint. Fix one density `rho` and average the expected diffraction (1) over any probability distribution of iid displacement laws. Writing

\[
q(h):=\int |\varphi_\theta(h)|^2\,d\Pi(\theta),
\qquad 0\le q\le1,
\tag{12}
\]

the mixture has the same form

\[
\rho\sum_m q(m\rho)\delta_{m\rho}
+
(1-q(h))dh.
\tag{13}
\]

If it were dominated by `nu_a`, the forward atom again gives `rho<=a<1`, while the nonnegative first Bragg atom forces `q(rho)=0`. Its diffuse density at that frequency is then `1-q(rho)=1`, and the same contradiction (11) follows.

So convexification over independent-displacement mechanisms does not help at a fixed lattice density. This is distinct from mixing **densities**: a continuous density mixture can smear reciprocal vectors across the band, as `ANF-022` already demonstrated for unperturbed lattices. The present theorem does not claim to classify a joint mixture over lattice density and displacement law.

## 5. Prior-art boundary

Randomly perturbed or "shuffled" lattices and their diffraction are classical. Andrea Gabrielli, *Point processes and stochastic displacement fields*, *Physical Review E* 70 (2004), 066131, derives exact transformation laws for two-point correlations and power spectra under correlated and uncorrelated displacement fields.

Michael A. Klatt, Jaeuk Kim and Salvatore Torquato, *Cloaking the Underlying Long-Range Order of Randomly Perturbed Lattices*, *Physical Review E* 101 (2020), 032118, DOI `10.1103/PhysRevE.101.032118`, arXiv:2001.08161, study precisely iid lattice perturbations. Their structure-factor formula is the classical counterpart of (1), and they characterize displacement distributions that cloak inherited Bragg peaks. In particular, the diffuse/Bragg tradeoff itself is prior art.

What is derived here is the specialization to the exact order interval from `ANF-020`: forward-atom contraction below one forces the first reciprocal vector into the observed band, while cloaking that vector forces diffuse density one at the same location. A targeted search across perturbed-lattice diffraction, Bragg cloaking and Montgomery--Taylor pair-correlation bounds did not locate this support-one domination obstruction. No publication-level novelty claim is made.

## 6. Audit and evidence boundary

The theorem is a **candidate-class exclusion**, not a proof that the full diffraction body `K` misses the Montgomery--Taylor order interval. It is deliberately phrased at the level of the expected perturbed-lattice diffraction profile. Establishing that every such infinite-volume random profile belongs to `K` is unnecessary for the negative conclusion: even granting the profile as an admissible witness, it violates the target measure inequality.

The iid hypothesis is load-bearing for formula (3). Correlated displacement fields have additional cross-correlation terms and may trade Bragg suppression against diffuse intensity differently; Gabrielli's general framework explicitly distinguishes this case. Likewise, random mixtures over lattice densities, coupled multiscale constructions, non-lattice hyperuniform processes, and direct finite-cluster convexifications are not covered.

Collisions between perturbed lattice sites are also irrelevant to the stated no-go. Formula (3) is an identity for the scattering amplitude with labelled sites. If one wants a simple point process, any displacement law for which collisions occur with probability zero is already enough to fall under the theorem; allowing more general laws only enlarges the candidate class being excluded at the diffraction-profile level.

Finally, the target constant enters only through `a<1`. The obstruction is therefore stronger than needed for Montgomery--Taylor but does **not** contradict the uncontracted endpoint `a=1`: for example, the unperturbed unit lattice has forward atom one and its first nonzero Bragg peaks sit at the boundary `|h|=1`, outside the open test band.

## 7. Consequence for the scalar frontier

The sequence of scalar filters now rules out three qualitatively different realizability templates. `ANF-020` excludes stationary translation-invariant DPP/free-fermion witnesses below factor one. `ANF-021` shows that symplectic Pfaffian statistics improve the local cusp but still overshoot the finite-frequency band. `ANF-022` excludes scale-randomized crystals through a Möbius dilation dual. The present result adds **independently disordered crystals**: Bragg cloaking itself creates too much diffuse intensity at the first reciprocal vector.

This narrows the realizability search toward mechanisms with genuinely correlated positional disorder, coupled scale/displacement structure, non-crystalline hyperuniform correlations, or a direct construction in the convex closure of finite cluster diffractions. Any such candidate still has to satisfy the full support-one measure envelope, not merely remove Bragg peaks or improve the small-wave-number slope.

The configuration-level escape established in `ANF-006` remains outside the scalar diffraction duality and is unaffected.