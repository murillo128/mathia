# PC-309 — transport-stable prime-source geometry collapses before the mesh scale

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the stable-geometric/topological escape left open by PC-306–PC-308.

PC-306 shows that a prime-index source on a prime polygon is algebraically recoverable from extremely little exact oriented data but unstable under a one-step matched translation; PC-307 quantifies the severe conditioning of low/polylogarithmic Fourier packets; PC-308 shows that ordinary Fourier packets regain order-one separation only at linear bandwidth, where classical fixed-denominator congruence resonances already appear.

The remaining natural escape is to replace those finite packets by a more genuinely geometric observable: the source as a probability measure on the circle, its full two-dimensional logarithmic potential, or another stable functional of the physical point configuration. For the same matched source/control experiment there is a simple exact obstruction. One polygon step is only `O(1/q)` in every physical Wasserstein metric, even though the two discrete supports are disjoint. Consequently every uniformly transport-continuous per-level observable collapses unless its conditioning grows at least linearly with `q`. For normalized logarithmic potentials the statement is stronger: the *entire interior two-dimensional field* collapses uniformly throughout every boundary layer wider than the polygon mesh.

This does not produce a new RH mechanism. It instead places a precise stability boundary on a broad class of proposed prime-circle carriers: any surviving mechanism must become singular at mesh scale, use an explicitly diverging condition number, or exploit structure not represented by a uniformly transport-continuous single-level source observable.

## 1. Matched prime source and one-step rotation

Let `q>3` be prime and retain the canonical source used in PC-306–PC-308,

\[
P_q:=\{p:2<p<q,\ p\text{ prime}\},
\qquad
M_q:=|P_q|=\pi(q)-2,
\tag{1}
\]

with normalized empirical measure

\[
\nu_q:=\frac1{M_q}\sum_{p\in P_q}\delta_{\zeta_q^p},
\qquad \zeta_q=e^{2\pi i/q}.
\tag{2}
\]

Let `R_q(z)=\zeta_q z` and define the matched one-step translate

\[
\nu_q^+:=(R_q)_\#\nu_q
=\frac1{M_q}\sum_{p\in P_q}\delta_{\zeta_q^{p+1}}.
\tag{3}
\]

The supports are disjoint: every `p\in P_q` is odd whereas every `p+1` is even, with representatives in `{1,\ldots,q-1}`. Hence

\[
\|\nu_q-\nu_q^+\|_{\mathrm{TV}}=1
\tag{4}
\]

in the standard probability convention. Thus the control is combinatorially maximally different from the source.

Equip `S^1` with Euclidean chord distance. The deterministic coupling

\[
z\longmapsto R_qz
\tag{5}
\]

moves every unit-circle point through exactly

\[
|R_qz-z|=|\zeta_q-1|=2\sin\frac{\pi}{q}.
\tag{6}
\]

Therefore, for every `1\le p\le\infty`,

\[
\boxed{
W_p(\nu_q,\nu_q^+)
\le 2\sin\frac{\pi}{q}
\sim \frac{2\pi}{q}.
}
\tag{7}
\]

No prime-distribution estimate enters (7). It is forced solely by the prime-circle geometry and the matched one-step control.

## 2. Uniformly transport-stable observables require linear conditioning

Let `G_q` be any observable from probability measures on `S^1` to a metric space `(Y,d_Y)`, and suppose that on the relevant source/control pair it obeys a Wasserstein Lipschitz bound

\[
d_Y(G_q(\mu),G_q(\eta))
\le L_q W_p(\mu,\eta).
\tag{8}
\]

Then (7) gives the exact stability obstruction

\[
\boxed{
d_Y(G_q(\nu_q),G_q(\nu_q^+))
\le 2L_q\sin\frac{\pi}{q}.
}
\tag{9}
\]

In particular, if a proposed discriminator is required to keep a fixed output margin `\delta>0`, then necessarily

\[
\boxed{
L_q
\ge \frac{\delta}{2\sin(\pi/q)}
\sim \frac{\delta}{2\pi}\,q.
}
\tag{10}
\]

Thus no family with `L_q=o(q)` can preserve an order-one source/control separation. This is the physical-space version of the instability seen in PC-306, but it is not tied to a Fourier truncation or to any chosen finite coordinate system.

The conclusion is intentionally conditional on the declared topology: it rules out *uniformly transport-stable* single-level observables. It does not rule out a singular functional whose transport condition number itself diverges like `q` or faster, nor cross-level data that are not functions of one source measure.

## 3. The full normalized logarithmic-potential field also collapses in the interior

For a probability measure `\mu` on `S^1`, define its logarithmic potential inside the unit disk by

\[
V_\mu(z):=\int_{S^1}\log|z-w|\,d\mu(w),
\qquad |z|<1.
\tag{11}
\]

Rotation covariance is exact:

\[
V_{(R_q)_\#\mu}(z)
=V_\mu(R_q^{-1}z).
\tag{12}
\]

For `z=re^{i\theta}` and `w\in S^1`, differentiation in the angular variable gives

\[
\left|\partial_\theta\log|re^{i\theta}-w|\right|
\le \frac{r}{|re^{i\theta}-w|}
\le \frac{r}{1-r}.
\tag{13}
\]

The angular displacement between `z` and `R_q^{-1}z` is `2\pi/q`, so (12)–(13) imply, uniformly for every probability measure `\mu`,

\[
\boxed{
\sup_{|z|\le r}
|V_{(R_q)_\#\mu}(z)-V_\mu(z)|
\le
\frac{2\pi}{q}\frac{r}{1-r}.
}
\tag{14}
\]

Applying this to `\nu_q` yields a genuinely two-dimensional statement about the complete normalized field, not a finite packet of Fourier coefficients. If `r_q<1` satisfies

\[
q(1-r_q)\longrightarrow\infty,
\tag{15}
\]

then

\[
\boxed{
\sup_{|z|\le r_q}
|V_{\nu_q^+}(z)-V_{\nu_q}(z)|
\longrightarrow 0.
}
\tag{16}
\]

Hence every fixed-depth interior disk collapses, and so does every shrinking boundary layer whose thickness is still asymptotically larger than the polygon spacing `1/q`. The first radial scale not excluded by this argument is

\[
1-r=O(1/q),
\tag{17}
\]

the mesh-scale singular layer itself.

This is directly relevant to the canonical prime-circle harmonic language. Normalized sums of `\log|z-w|` are the per-vertex potential-theoretic version of the cyclotomic fields `U_n(z)=\log|\Phi_n(z)|`. Equation (16) says that merely retaining the *whole interior field* does not evade the matched-control instability before mesh scale. Singular boundary evaluation is outside the hypothesis and must be audited separately; in particular this result does not subsume the classical anchored identity `U_n(1)=\Lambda(n)`.

## 4. PC-306–PC-308 are consistent projections of the same boundary

For the `k`-th character `f_k(e^{i\theta})=e^{ik\theta}`, the physical Lipschitz constant is `O(|k|)`. Kantorovich–Rubinstein duality therefore turns (7) into the familiar scale

\[
\left|\widehat\nu_q^+(k)-\widehat\nu_q(k)\right|
\ll \frac{|k|}{q},
\tag{18}
\]

recovering the geometric content behind the first-`K` estimate of PC-306. PC-307 adds genuinely arithmetic cancellation for the canonical prime source in low and polylogarithmic bandwidths, so it is strictly sharper there.

There is also no contradiction with PC-308. Its first order-one witnesses occur at `k=\Theta(q)`. Such characters have physical Lipschitz norm `\Theta(q)`, exactly the threshold (10) says is necessary for fixed separation. The parity and fixed-denominator major-arc witnesses therefore sit precisely at the point where the observable has enough angular conditioning to resolve individual mesh-scale structure.

The transport formulation consequently unifies the previous finite-packet facts without replacing their arithmetic content: low-frequency stability is geometric, PC-307 quantifies extra prime cancellation, and linear-frequency recovery spends `\Theta(q)` conditioning and then exposes classical congruence structure.

## 5. Prior-art and novelty audit

The abstract tools are classical. The Wasserstein estimate (7) is the elementary pushforward coupling for a small rotation, and the `W_1` formulation is standard Kantorovich–Rubinstein duality. The potential estimate (14) is an elementary derivative bound for the logarithmic kernel. None of those ingredients is novel.

The closest modern prior-art located in the audit is Ruiwen Shu and Jiuya Wang, *Generalized Erdős–Turán inequalities and stability of energy minimizers*, J. Eur. Math. Soc., published online 3 January 2025, DOI `10.4171/JEMS/1583` (https://ems.press/journals/jems/articles/14298463). They explicitly connect logarithmic/Riesz potentials, discrepancy, and Wasserstein stability. The direction is complementary: their results control geometric discrepancy from potential information, whereas (14) is a direct matched-rotation stability estimate.

The conditioning interpretation is also adjacent to the super-resolution literature, especially Emmanuel Candès and Carlos Fernandez-Granda, *Towards a Mathematical Theory of Super-Resolution*, Comm. Pure Appl. Math. 67 (2014), DOI `10.1002/cpa.21455` (https://arxiv.org/abs/1203.5871), where recovering fine point-source structure from coarse Fourier information requires resolution assumptions and exhibits scale-dependent stability.

The novelty audit therefore does **not** support claiming a new optimal-transport or potential-theory theorem. The durable content here is the exact prime-circle synthesis: the same disjoint source/control pair used in PC-306–PC-308 is `O(1/q)` apart in every physical Wasserstein metric, and its complete normalized logarithmic field is uniformly indistinguishable throughout every pre-mesh-scale interior region. Searches around Wasserstein/logarithmic-potential stability and super-resolution did not reveal this specific one-step prime-circle obstruction as an existing RH criterion or zeta mechanism.

## 6. Boundary of the negative result

The result rules out the route

\[
\text{single-level prime source}
\to
\text{uniformly transport-stable physical geometry}
\to
\text{fixed-margin arithmetic discriminator}
\tag{19}
\]

unless the intermediate map pays at least `\Omega(q)` conditioning. For normalized logarithmic potentials it additionally rules out using the complete interior field on every scale satisfying `q(1-r)\to\infty`.

It does **not** rule out:

- mesh-scale or more singular boundary operators with explicitly controlled `\Omega(q)` (or larger) norm;
- shell-dependent nonlinear operations whose transport modulus is allowed to diverge and is itself arithmetically meaningful;
- genuinely cross-level/mixed-conductor constructions that are not functions of a single source measure;
- nonlocal data that are not continuous in the physical transport topology;
- a mechanism that supplies an independent reason why the required singular conditioning is canonical and tied to zeta rather than merely decoding the discrete source.

These are the correct remaining escape hatches. In particular, merely saying that a representation is “two-dimensional” or that it retains the full harmonic field is no longer sufficient: before mesh scale the normalized field is provably stable under a combinatorially maximal matched perturbation.

## 7. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the matched source/control pair in (2)–(3) is shown not to be the intended canonical control from PC-306–PC-308;
2. a claimed transport-stable observable with `L_q=o(q)` exhibits a fixed positive separation on that pair, contradicting (7)–(10);
3. the logarithmic-potential covariance (12) or derivative estimate (13) is invalid under the normalization actually used by the line;
4. prior art is found that already formulates this exact prime-circle matched-rotation obstruction, in which case the classification must be strengthened toward pure classicalization rather than project-local synthesis.

Absent such a failure, the practical research boundary is sharp enough to guide the next step: any proposed stable single-level geometric carrier should first state its transport modulus or boundary-layer scale. If that cost is already `\Omega(q)`, it must explain what is gained beyond mesh-scale decoding or the classical congruence information exposed in PC-308.