# PF-156 — matched short-orbit packets cancel the absolute Selberg divergence at test-function level

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-036 shows that the absolute Selberg hyperbolic orbital measure of the prime flute has infinite mass in every positive length window because iterates of primitive lengths tending to zero accumulate everywhere. The exact all-composite shift clone does not remove those short primitive classes; instead PF-109 and PF-138 give a canonical marked pairing whose **logarithmic length defects are absolutely summable over the entire source Margulis-short family**. For every smooth Selberg test function in the class below, the full repeated-orbit packet of each matched short primitive is uniformly Lipschitz in logarithmic length. Consequently the sum of the matched packet differences converges absolutely. The same statement holds for the Selberg heat packet at every fixed positive time.

This is not a full relative trace formula and it does not make the relative orbital difference a locally finite signed measure: the paired atoms generally occur at different times, so total variation need not cancel. The result is precisely a test-function/distribution-level cancellation of the nowhere-locally-finite short-orbit obstruction from PF-036.

## Claim

For a primitive closed geodesic of length `L>0`, define its full repeated Selberg packet against a test function `phi` by

\[
\mathcal T_L(\phi)
:=
\sum_{k\ge1}
\frac{L}{2\sinh(kL/2)}\,\phi(kL).
\tag{1}
\]

Put

\[
F_\phi(x)
:=
\frac{x}{2\sinh(x/2)}\,\phi(x),
\tag{2}
\]

with the continuous value at `x=0` when needed. Then

\[
\mathcal T_L(\phi)
=
\sum_{k\ge1}\frac1k F_\phi(kL).
\tag{3}
\]

Assume

\[
F_\phi'\in W^{1,1}(0,\infty),
\tag{4}
\]

i.e. `F_phi'` and `F_phi''` are integrable. This includes every `phi in C_c^infty((0,infinity))`, and it also includes the heat test

\[
\phi_t(x)=e^{-x^2/(4t)},\qquad t>0.
\tag{5}
\]

For every finite `L_*>0` there is

\[
C_{\phi,L_*}
=
\|F_\phi'\|_{L^1}
+L_*\|F_\phi''\|_{L^1}
\tag{6}
\]

such that whenever

\[
0<L\le L_*,\qquad
L'=e^\tau L\le L_*,
\tag{7}
\]

we have the logarithmic Lipschitz estimate

\[
\boxed{
|\mathcal T_{L'}(\phi)-\mathcal T_L(\phi)|
\le C_{\phi,L_*}|\tau|.}
\tag{8}
\]

Now let `S_*` be the set of essential simple primitive prime-flute geodesics satisfying

\[
\ell(\eta)\le
\mu_*:=2\operatorname{arsinh}1,
\tag{9}
\]

and let `ell_+(eta)` be the length of the same marked topological class on the normalized all-composite shift clone. Then

\[
\boxed{
\sum_{\eta\in S_*}
\left|
\log\frac{\ell_+(\eta)}{\ell(\eta)}
\right|<\infty.}
\tag{10}
\]

Hence, for every admissible `phi`,

\[
\boxed{
\sum_{\eta\in S_*}
\left|
\mathcal T_{\ell_+(\eta)}(\phi)
-
\mathcal T_{\ell(\eta)}(\phi)
\right|<\infty.}
\tag{11}
\]

In particular, for every fixed `t>0`, the complete repeated-orbit **heat packet difference over the source Margulis-short family** is absolutely summable.

## 1. Uniform sampling estimate

The only analytic input needed for (8) is an elementary sampling bound. Let

\[
G\in W^{1,1}(0,\infty)
\]

and `h>0`. On the cell

\[
I_k=[(k-1)h,kh]
\]

we have for almost every `x in I_k`

\[
|G(kh)|
\le
|G(x)|+
\int_{I_k}|G'(u)|\,du.
\]

Integrating over `I_k` and summing gives

\[
\boxed{
h\sum_{k\ge1}|G(kh)|
\le
\|G\|_{L^1}
+h\|G'\|_{L^1}.}
\tag{12}
\]

Apply this with `G=F_phi'`. Differentiating (3) in logarithmic length gives

\[
\frac{d}{ds}
\mathcal T_{e^sL}(\phi)
=
 e^sL
\sum_{k\ge1}F_\phi'(ke^sL).
\tag{13}
\]

For compactly supported smooth `phi`, termwise differentiation is immediate after fixing `e^sL>0`; for the heat test it follows from the Gaussian decay, and (12) supplies a uniform absolute bound. If `e^sL<=L_*`, then

\[
\left|
\frac{d}{ds}
\mathcal T_{e^sL}(\phi)
\right|
\le
\|F_\phi'\|_1
+L_*\|F_\phi''\|_1.
\tag{14}
\]

Integrating (14) from `s=0` to `s=tau` proves (8).

The estimate remains uniform as `L->0`. This is the feature needed here: each individual heat packet diverges logarithmically in the pinching limit, but two multiplicatively matched pinching lengths differ by only `O(|tau|)` at packet level.

## 2. The prime/shift short-core logarithmic defect is ell-one

PF-138 classifies every source simple closed geodesic below the Margulis threshold (9). Apart from finitely many distinguished tight-flute cuffs, every such geodesic in the tail is a PF-004 canonical separator of a finite consecutive cusp block.

If `P` is the left exterior prime label of such a separator, PF-138 proves the crude but sufficient count

\[
N(P)=O(P^\theta),
\qquad \theta=0.525,
\tag{15}
\]

using the Baker--Harman--Pintz gap envelope. PF-109 proves uniformly for every canonical separator, including the pinching regime,

\[
\left|
\log\frac{\ell_+}{\ell}
\right|
=O(P^{-3}).
\tag{16}
\]

Therefore

\[
\sum_{\eta\in S_*}
\left|
\log\frac{\ell_+(\eta)}{\ell(\eta)}
\right|
\le
C_{\rm head}
+C\sum_P P^{\theta-3}
<\infty,
\tag{17}
\]

which is (10).

The same estimates give a finite uniform bound on the length ratios in the matched source-short family. Thus one may choose one finite `L_*` containing every logarithmic interpolation between `ell(eta)` and `ell_+(eta)`. Applying (8) class by class and summing (10) gives (11).

## 3. Heat-trace specialization

Jorgenson--Lundelius, *A regularized heat trace for hyperbolic Riemann surfaces of finite volume*, Comment. Math. Helv. 72 (1997), Proposition 2.1, isolate the classical degenerating hyperbolic heat contribution as

\[
\frac{e^{-t/4}}{\sqrt{16\pi t}}
\sum_{k\ge1}
\frac{L}{\sinh(kL/2)}
 e^{-(kL)^2/(4t)}
\tag{18}
\]

per pinching primitive class (summed over the pinching set). Thus, with the normalization (1), the primitive heat packet is

\[
\frac{e^{-t/4}}{\sqrt{4\pi t}}
\mathcal T_L(\phi_t).
\tag{19}
\]

For fixed `t>0`, the function

\[
F_t(x)
=
\frac{x}{2\sinh(x/2)}e^{-x^2/(4t)}
\tag{20}
\]

is smooth at `0`, with `F_t(0)=1`, and has integrable first and second derivatives because of Gaussian decay. Equation (11) therefore implies

\[
\boxed{
\sum_{\eta\in S_*}
\left|
H_t(\ell_+(\eta))-H_t(\ell(\eta))
\right|<\infty
\qquad(t>0),}
\tag{21}
\]

where `H_t(L)` denotes the standard primitive repeated-orbit heat packet (19).

The absolute prime-flute sum itself still diverges: PF-036 proves much more, namely infinite Selberg orbital mass in every positive time window. Equation (21) says that this specific divergence is removed after **canonical marked prime/shift subtraction at the smooth-test level**.

## 4. What this changes in the trace branch

PF-036 ruled out the route

\[
\text{absolute global Selberg/wave localization}
\longrightarrow
\text{isolate distinguished prime-flute orbit times},
\]

because iterates of `L_j->0` carry infinite orbital mass into every positive window.

One natural objection to relative trace ideas was that the same infinitely repeated pinching family might survive subtraction and make even a matched relative trace undefined before any operator theory is reached. PF-156 removes that particular obstruction for the canonical shift control:

\[
\boxed{
\text{source Margulis-short primitive family}
\xrightarrow{\text{all iterates}}
\text{nowhere-locally-finite absolute orbital sum}
\quad\text{but}\quad
\text{absolutely summable paired test-function difference}.}
\tag{22}
\]

The cancellation is nontrivial because it includes **all repetitions** `k>=1` of every pinching primitive; it is not a cutoff at one iterate or a finite truncation.

This complements PF-155. The local heat-invariant tower is area-only and therefore cannot encode the prime data, while PF-156 shows that the most violent nonlocal short-orbit heat divergence is nevertheless stable under the shift control after marked subtraction. Any useful relative trace information must therefore live in the finite nonlocal remainder rather than in either the local heat coefficients or the raw pinching divergence.

## 5. Adversarial scope: this is a distributional cancellation, not a relative measure theorem

There is an important limitation. For `L'!=L`, the atoms

\[
kL
\quad\text{and}\quad
kL'
\]

usually occur at different positions. Therefore (11) does **not** imply that

\[
\sum_{k\ge1}
\frac{L'}{2\sinh(kL'/2)}\delta_{kL'}
-
\sum_{k\ge1}
\frac{L}{2\sinh(kL/2)}\delta_{kL}
\]

has finite total variation, nor that the global prime/shift orbital difference is a Radon signed measure. Smooth test functions permit cancellation through the small displacement of the atoms; total variation does not.

Nor does PF-156 establish any of the following:

- a full relative Selberg trace formula for the infinite flute;
- convergence of the matched contribution from all longer primitive classes;
- control of cusp-winding or other global primitive sectors;
- trace-class first relative resolvent;
- the still-open global squared-resolvent `S_1` gate of PF-146--PF-148;
- wave/scattering completeness;
- a relative determinant or resonance theory;
- an RH mechanism.

In particular PF-103's universal cusp-winding half-threshold is untouched. The present result only says that the **specific repeated-short-orbit catastrophe used by PF-036** is not an obstruction to a smooth marked relative trace against the exact all-composite shift control.

## 6. Universal control and novelty audit

The analytic lemma (8) is not prime-specific. Any two pinching length families with an `ell^1` sequence of logarithmic defects enjoy the same packet cancellation. Thus the cancellation itself is not evidence for RH or for a special arithmetic spectrum.

The general strategy of isolating the heat contribution of pinching geodesics is classical. Jorgenson and Lundelius define the degenerating heat trace precisely by summing the repeated hyperbolic packets of the pinching classes and prove convergence of the remaining finite-volume heat trace under degeneration:

- J. Jorgenson and R. Lundelius, *A regularized heat trace for hyperbolic Riemann surfaces of finite volume*, Comment. Math. Helv. 72 (1997), 636--659, DOI `10.1007/S000140050039`, especially Proposition 2.1 and Theorem 2.2.
- Their earlier paper *Convergence of the heat kernel and the resolvent kernel on degenerating hyperbolic Riemann surfaces of finite volume*, Quaestiones Mathematicae 18 (1995), 345--363, DOI `10.1080/16073606.1995.9631808`, supplies the classical finite-volume degeneration background.
- Later Selberg-zeta degeneration work, including Avdispahić--Jorgenson--Smajlović, *Asymptotic Behavior of the Selberg Zeta Functions for Degenerating Families of Hyperbolic Manifolds*, Comm. Math. Phys. 310 (2012), 217--236, DOI `10.1007/s00220-011-1408-5`, treats the corresponding finite-geometry zeta degeneration problem.

A directed search did not locate the exact elementary logarithmic-Lipschitz estimate (8) stated as a standalone theorem, but no general novelty is claimed for it. It is a Riemann-sum estimate around a classical degenerating packet.

The durable project-specific content is the composition

\[
\boxed{
\text{PF-138 complete source short-core classification/count}
+
\text{PF-109 }O(P^{-3})\text{ matched log-length defect}
+
\text{uniform repeated-packet estimate}
\Longrightarrow
\text{absolute convergence of the entire matched source-short relative packet}.}
\tag{23}
\]

This is outside the standard finite-pinching setting because the one fixed prime flute has infinitely many short primitives and its absolute orbital measure is nowhere locally finite. PF-156 does not claim a new theorem about general infinite-type trace formulas; it records the exact boundary condition relevant to this research line.

## 7. Evidence level

`proved` for the matched packet difference over the complete **source Margulis-short simple primitive family**, conditional only on the already persisted PF-109/PF-138 estimates; `positive/boundary` for the relative-trace program because it removes one major natural obstruction but leaves the global primitive and operator-theoretic completions open.
