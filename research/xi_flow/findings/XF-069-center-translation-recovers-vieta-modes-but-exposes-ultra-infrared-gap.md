# XF-069 — center translation recovers Vieta modes but exposes an ultra-infrared gap

**Status:** `EXACT-DERIVED` + `LOCALIZATION-IDENTITY` + `STRUCTURAL/RESTRICTION` + `MATCHED-CONTROL`. XF-067 diagonalizes the full periodic zero heat flow in Vieta coordinates, and XF-068 shows that converting uniformly small power sums into Vieta coefficients costs only a polynomial factor after fixed positive heat time. The remaining source-to-Vieta bridge has two logically distinct parts. The compact taper itself is not an inverse-conditioning obstruction: translating the taper center through one period and taking one Fourier coefficient recovers each raw periodic power sum **exactly, with no loss in the period length**. But the Xi source selector of XF-059 only reaches frequencies whose distance from zero is many selector-resolution cells. In Vieta index this leaves an ultra-infrared block that contains every fixed mode.

More precisely, let

\[
M=q^2,\qquad N=2M,
\tag{1}
\]

and let a periodic point configuration in index coordinates satisfy

\[
x_{j+N}=x_j+N.
\tag{2}
\]

Choose the same admissible bandlimited envelope as in XF-056--XF-064, with Fourier convention

\[
\chi(\eta)=\widehat g(\eta)
=\int_{\mathbb R}g(v)e^{-i\eta v}\,dv,
\qquad
\chi\in C_c^\infty((-1,1)),
\qquad
\chi(0)\ne0.
\tag{3}
\]

For a translated center `r` define

\[
\mathcal S_r(\theta)
:=
\sum_{j\in\mathbb Z}
 g\!\left(\frac{x_j-r}{M}\right)
 e^{-i\theta(x_j-r)}.
\tag{4}
\]

Then `r -> S_r(theta)` is `N`-periodic. Writing

\[
\xi_k:=\frac{2\pi k}{N},
\qquad
P_k:=\sum_{j=0}^{N-1}e^{-i\xi_kx_j},
\tag{5}
\]

one has the exact center-Fourier identity

\[
\boxed{
\frac1N\int_0^N
\mathcal S_r(\theta)e^{-i\xi_kr}\,dr
=
\frac{M}{N}\,
\chi\!\bigl(M(\theta-\xi_k)\bigr)P_k.
}
\tag{6}
\]

At the matching frequency `theta=xi_k`, since `N=2M`,

\[
\boxed{
P_k
=
\frac{2}{\chi(0)}
\frac1N\int_0^N
\mathcal S_r(\xi_k)e^{-i\xi_kr}\,dr.
}
\tag{7}
\]

Consequently

\[
\boxed{
|P_k|
\le
\frac{2}{|\chi(0)|}
\left(
\frac1N\int_0^N|\mathcal S_r(\xi_k)|^2\,dr
\right)^{1/2}
\le
\frac{2}{|\chi(0)|}
\sup_r|\mathcal S_r(\xi_k)|.
}
\tag{8}
\]

Thus a future localization theorem does **not** need to flatten the XF-059 taper into a box or invert a badly conditioned `N x N` windowing matrix. It is enough to compare the actual Xi selector with a periodic surrogate in normalized `L^2` over one translated-center period. The normalization in (8) introduces no factor growing with `M` or `N`.

The restriction is at the opposite end. Since

\[
\xi_k=\frac{\pi k}{q^2},
\tag{9}
\]

XF-059 with its convenient fixed choice `delta=1/2`, namely

\[
q^{-3/2}\le |\theta|\le
\frac{C\log\log T}{q},
\tag{10}
\]

corresponds only to

\[
\boxed{
\frac{q^{1/2}}{\pi}
\lesssim k
\lesssim
\frac{C}{\pi}q\log\log T.
}
\tag{11}
\]

Using arbitrary fixed `delta>0` in XF-059 pushes the lower Vieta index to `k \gtrsim q^delta`, but no fixed `delta` reaches `k=O(1)`. For fixed `k`,

\[
M\xi_k=\pi k=O(1),
\tag{12}
\]

which is exactly the selector-resolution regime where the positive-frequency band approaches the zero-frequency background and the XF-059 integration-by-parts gain disappears.

This matters because the fixed Vieta modes are not removed by positive heat time. XF-067 gives

\[
E_k(t+\tau)
=E_k(t)
\exp\!\left(
-\frac{4\pi^2k(N-k)}{L^2}\tau
\right),
\qquad L=Ns,
\tag{13}
\]

so for fixed `k` and the Xi scale `s^{-2}=Theta(q)`, `N=2q^2`,

\[
\frac{4\pi^2k(N-k)}{L^2}\tau
=
\Theta_\tau\!\left(\frac{k}{q}\right)
=o(1).
\tag{14}
\]

The missing ultra-infrared coefficients therefore survive essentially unchanged over the fixed heat interval in which XF-068 regularizes the high Newton map.

The important repair is that these modes are also too flat to carry the transition observable used by XF-062--XF-066. An explicit periodic control shows that raw Vieta smallness is a stronger requirement than the destination geometry actually needs. The correct next bridge should therefore **quotient or weight away the ultra-infrared Vieta sector**, rather than try to prove that all raw `P_1,...,P_K` are source-small.

## 1. Exact extraction by translating the selector center

Write

\[
h_\theta(u):=g(u/M)e^{-i\theta u}.
\tag{15}
\]

Using (2), decompose the infinite periodic point set into representatives `j=0,...,N-1` and their translates `x_j+nN`. Then

\[
\begin{aligned}
&\frac1N\int_0^N
\mathcal S_r(\theta)e^{-i\xi_kr}\,dr\\
&=\frac1N
\sum_{j=0}^{N-1}\sum_{n\in\mathbb Z}
\int_0^N
h_\theta(x_j+nN-r)e^{-i\xi_kr}\,dr.
\end{aligned}
\tag{16}
\]

For each fixed representative put `u=x_j+nN-r`. The intervals obtained as `n` varies partition the real line, while

\[
e^{-i\xi_k(x_j+nN-u)}
=e^{-i\xi_kx_j}e^{i\xi_ku}
\tag{17}
\]

because `xi_k N=2 pi k`. Hence (16) becomes

\[
\frac1N
\sum_{j=0}^{N-1}e^{-i\xi_kx_j}
\int_{\mathbb R}
g(u/M)e^{-i(\theta-\xi_k)u}\,du.
\tag{18}
\]

After `u=Mv`, the integral is

\[
M\chi\!\bigl(M(\theta-\xi_k)\bigr),
\tag{19}
\]

which proves (6). No approximation, root reality beyond the displayed real periodic configuration, gap regularity, or small-displacement assumption is used.

Equation (8) follows from Cauchy--Schwarz in the normalized center variable. This is the useful conditioning statement: the extraction constant is `2/|chi(0)|`, independent of the growing period.

## 2. What localization estimate would now suffice

Let `S_r^per(theta,t)` denote the periodic surrogate statistic (4), after rescaling a candidate local transition block into the XF-062 index coordinates, and let `S_r^Xi(theta,t)` denote the corresponding actual Xi moving-line statistic with physical center translated by `sr`. Define the normalized center mismatch

\[
\mathfrak D_T(\theta,t)
:=
\left(
\frac1N\int_0^N
|\mathcal S_r^{\rm per}(\theta,t)
-\mathcal S_r^{\Xi}(\theta,t)|^2\,dr
\right)^{1/2}.
\tag{20}
\]

The physical center shift over one period is only

\[
Ns=2Ms=2W=O(\!\log^3T)=o(T).
\tag{21}
\]

The moving-high-line proof of XF-059 is stable under such center shifts: the shifted centers remain in the same `T+O(W)` mesoscopic region, the prime-free frequency support is unchanged, and all load-bearing powers of `T` and `log T` are uniform after replacing `T` by `T+O(W)`. Thus its rapid source bound may be used uniformly over the center scan for frequencies in its admissible cone.

Combining that uniform source estimate with (8) gives the conditional transfer

\[
\boxed{
|P_k^{\rm per}(t)|
\le
\frac{2}{|\chi(0)|}
\left[
\mathfrak D_T(\xi_k,t)
+O_B((\log T)^{-B})
\right]
}
\tag{22}
\]

for every fixed `B`, uniformly over Vieta indices whose `xi_k` lie in the XF-059 cone. This identifies the nonperiodic burden much more sharply than “remove the taper”: prove a small center-averaged periodic-surrogate mismatch. Once that is available, extraction of each source-visible raw power sum is exact and well conditioned.

Equation (22) does not assert that the needed mismatch is already small. Near the ends of a finite block the artificial periodic continuation can disagree with the neighboring true Xi zeros, and the full center scan deliberately exposes that interface. The boundary/interface comparison is the remaining localization theorem.

## 3. The source-visible Vieta range starts above the fixed modes

At the periodic DFT nodes (9), the XF-059 lower edge `q^{-2+delta}` becomes

\[
k\ge \frac1\pi q^\delta.
\tag{23}
\]

For the concrete band used by XF-062--XF-066, `delta=1/2`, this is the lower edge in (11). The upper edge becomes `k=O(q log log T)`, exactly the growing range whose post-heat Newton conditioning is polynomial in XF-068.

The lower mismatch is not removable by merely choosing a smaller fixed `delta`. For every fixed `k`, `M xi_k=pi k` stays bounded, whereas XF-059 requires the center to be a growing number of support widths from frequency zero. Thus the source theorem approaches the Vieta origin arbitrarily slowly in power scale but never reaches the finitely many lowest modes.

This is precisely where the full Newton hypothesis in XF-068 is stronger than the current source information. Newton--Girard gives

\[
kE_k
=\sum_{m=1}^k(-1)^{m-1}E_{k-m}P_m,
\tag{24}
\]

so control of `P_m` only for `m>=q^delta` does not imply the hypothesis

\[
\max_{1\le m\le K}|P_m|\ll1
\tag{25}
\]

used there. In particular `P_1` enters every later coefficient recursively. XF-068 remains correct as a conditional theorem, but (25) should no longer be treated as the natural source-side target without first quotienting the ultra-infrared sector.

## 4. A fixed Vieta mode can be order one while the transition energy vanishes

The gap is not only a proof artifact. Take the exact periodic lattice perturbation

\[
x_j
=j+\varepsilon A\cos\frac{2\pi j}{N},
\qquad 0\le j<N,
\tag{26}
\]

with fixed `A` and fixed sufficiently small `epsilon`. It has bounded displacement and gap distortion `O(A epsilon/N)`.

For the first raw power sum, `xi_1=2pi/N`, the unperturbed lattice sum vanishes. Differentiating at `epsilon=0` gives

\[
\begin{aligned}
\left.\frac{dP_1}{d\varepsilon}\right|_{0}
&=-i\xi_1A
\sum_{j=0}^{N-1}
e^{-i\xi_1j}\cos(\xi_1j)\\
&=-i\xi_1A\frac N2
=-i\pi A.
\end{aligned}
\tag{27}
\]

The Taylor remainder is uniformly `O_A(epsilon^2/N)` by the elementary bound on the second derivative of the finite sum. Hence

\[
\boxed{
P_1=-i\pi A\varepsilon+O_A(\varepsilon^2/N),
}
\tag{28}
\]

so a fixed low Vieta mode remains order one as `T->infinity`.

Now evaluate the XF-062/XF-066 third-difference energy. The displacement has Fourier support only at `+-xi_1`, and Parseval gives

\[
\|a\|_2^2=\frac N2A^2\varepsilon^2=M A^2\varepsilon^2.
\tag{29}
\]

Therefore

\[
\begin{aligned}
Q_3(a)
&=M^3|e^{i\xi_1}-1|^6
\|a\|_2^2\\
&=M^4A^2\varepsilon^2
\left(2\sin\frac{\pi}{N}\right)^6\\
&=\frac{\pi^6A^2\varepsilon^2}{M^2}(1+o(1))
=O(q^{-4}).
\end{aligned}
\tag{30}
\]

Thus the same configuration has an order-one `P_1` but vanishing normalized transition energy. By (14), fixed positive heat time also leaves this mode almost unchanged. It is therefore simultaneously **source-unresolved, heat-undamped, and destination-harmless**.

This matched control rules out the strongest possible continuation of XF-068: one should not expect all low raw Vieta coordinates to become small merely because the transition-relevant third-difference state is well behaved. A bridge that insists on (25) would reject a benign long-wave gauge-like deformation for a reason unrelated to critical flux.

## 5. Consequence for the nonlinear bridge

The periodic algebraic side is now cleaner. Center translation gives an exact, condition-number-one-up-to-`chi(0)` map from localized selectors to each raw power sum in the source-visible band. The unresolved nonperiodic step is an interface mismatch in center-averaged norm, not inversion of the compact taper.

At the same time, the ultra-infrared block cannot simply be inserted into the XF-068 all-power-sums hypothesis: fixed modes are neither source-controlled nor heat-damped, and explicit bounded-displacement controls show that they need not be small. XF-062 and XF-066 already explain why this is not fatal for the target state: three discrete derivatives suppress precisely this long-wave sector.

The next useful object is therefore a **weighted or quotient Vieta bridge** that retains the exact collision-safe diagonal heat law of XF-067 while measuring only the Vieta content capable of contributing order-one `M^3 H^3` energy. A successful construction should satisfy two falsifiable requirements: it must be insensitive, with a quantified `o(1)` cost, to modes below the XF-062 infrared edge, and its source-visible component must be recoverable from (22) without requiring `P_1,...,P_{q^delta}` to vanish.

This is a restriction, not an upper bound on `Lambda`. No claim is made that an actual positive-`Lambda` transition admits the required periodic surrogate or that the interface mismatch in (20) is small. The finding only removes taper inversion as an algebraic obstacle and identifies the ultra-infrared quotient as a necessary feature of any Vieta-based nonlinear source-to-transition theorem.

## 6. Prior-art and novelty boundary

Identity (6) is elementary Fourier analysis of a periodic point measure convolved with a translated bandlimited window; it is in the classical Poisson-summation/periodic-convolution class and is not claimed as a new general Fourier theorem. A targeted prior-art audit of periodic Fourier localization and time--frequency concentration found no external theorem needed for the derivation above. The Mathia-specific content is the scale match between the XF-059 selector resolution, the `N=2q^2` Vieta period of XF-067, the polynomial Newton conditioning of XF-068, and the `M^3 H^3` destination observable of XF-062--XF-066. No new `SOURCES.md` anchor is load-bearing.