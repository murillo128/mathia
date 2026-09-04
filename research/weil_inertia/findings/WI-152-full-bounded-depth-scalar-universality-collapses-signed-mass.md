# WI-152 — full bounded-depth scalar universality collapses signed spectral mass into an `O(B^{-1})` central boundary layer

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-151 proves that the full bounded-depth Lamzouri-form scalar census forces the pointwise spectral floor

\[
\phi(a)\ge -2\phi(0)\operatorname{sech}^2(2\pi Ba),
\qquad a>0.
\tag{1}
\]

That result still leaves a visible escape: a moving signed profile could push its negative feature toward the origin on a shrinking scale. Combining (1) with the **real-axis two-point condition already isolated in WI-146** closes that escape at the level of total signed mass. Under the same universal scalar hypothesis, the entire negative part of `phi` is forced into a central boundary layer of width `O(B^{-1})`, with an exact `L^1` budget

\[
\boxed{
\int_{\mathbb R}\phi_-(t)\,dt
\le
\frac{C_*}{\pi B}\,\phi(0),
\qquad
C_*:=\log(1+\sqrt2)+2-\sqrt2
=1.467160024646\ldots .
}
\tag{2}
\]

Equivalently,

\[
\boxed{
\int\phi_-\le 0.467011540458\ldots\frac{\phi(0)}B.
}
\tag{3}
\]

Moreover, beyond any radius `a` larger than the central crossover scale,

\[
\boxed{
\int_{|t|\ge a}\phi_-(t)\,dt
\le
\frac{2\phi(0)}{\pi B}
\bigl(1-\tanh(2\pi Ba)\bigr)
\le
\frac{4\phi(0)}{\pi B}e^{-4\pi Ba}.
}
\tag{4}
\]

Thus a moving family with `phi_T(0)=o(B_T)` cannot retain a fixed amount of signed Fourier mass anywhere: its total negative mass tends to zero. If the negative mass stays outside a fixed positive radius, it vanishes exponentially unless the central value grows exponentially in the available off-line depth. This is stronger than the pointwise statement of WI-151 in exactly the remaining moving/narrow-feature direction.

No new zeta-zero proportion is claimed. The conclusion concerns the **full universal one-scalar finite-multiset abstraction** of Lamzouri's census. A zeta-specific restriction to realizable configurations, a matrix/joint observable, a nonlinear correction, or an independent horizontal-defect charge remains outside the theorem.

## 1. The real two-point test makes the spectral profile positive definite

Assume the hypotheses of WI-151. Thus `B>0`, `phi : R -> R` is continuous and real-even,

\[
\int_{\mathbb R}\phi(t)\,dt=1,
\qquad
\int_{\mathbb R}|\phi(t)|e^{4\pi B|t|}\,dt<\infty,
\tag{5}
\]

and

\[
H(z)=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt
\tag{6}
\]

satisfies the Lamzouri-form scalar inequality

\[
s(\mathcal Z)
\ge
2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{7}
\]

for every nonempty finite conjugation-invariant multiset contained in `|Im z|<=B`.

WI-146 already records the exact two-point real-axis consequence. For two distinct simple real points `{0,x}`, equation (7) gives

\[
\boxed{H(x)\ge0\qquad(x\in\mathbb R).}
\tag{8}
\]

The following classical Fourier step is useful because WI-151 used only off-real multiplicity scaling and therefore did not consume (8). Put

\[
w_R(x)=\left(1-\frac{|x|}{R}\right)_+.
\tag{9}
\]

Since `H>=0`, the quantities

\[
I_R:=\int_{\mathbb R}H(x)w_R(x)\,dx
\tag{10}
\]

increase with `R`. Fubini and the Fourier transform of the triangular cutoff give

\[
I_R
=
\int_{\mathbb R}
\phi(t)
R\left(\frac{\sin(\pi Rt)}{\pi Rt}\right)^2dt.
\tag{11}
\]

The factor on the right is the Fejer approximate identity of mass one. Continuity of `phi` at the origin therefore gives

\[
I_R\longrightarrow\phi(0).
\tag{12}
\]

Monotone convergence on the left yields the exact identity

\[
\boxed{
H\in L^1(\mathbb R),
\qquad
\int_{\mathbb R}H(x)\,dx=\phi(0).
}
\tag{13}
\]

In particular `phi(0)>=0`. Since both `phi` and `H` are integrable, Fourier inversion at every point (all points are continuity points of `phi`) gives

\[
\phi(t)=\int_{\mathbb R}H(x)e^{2\pi ixt}\,dx.
\tag{14}
\]

Because `H(x)dx` is a finite positive measure, (14) is precisely the classical Bochner representation. Hence `phi` is positive definite and the elementary two-by-two consequence is

\[
\boxed{
|\phi(t)|\le\phi(0)
\qquad(t\in\mathbb R).
}
\tag{15}
\]

The use of Bochner here is classical; the new zero-side input is only that the finite census itself supplies the nonnegative Fourier density `H` through (8).

## 2. Combining positive definiteness with the phase-mask floor

WI-151 gives, for every real `t`,

\[
\phi(t)
\ge
-2\phi(0)\operatorname{sech}^2(2\pi B|t|).
\tag{16}
\]

Equation (15) independently gives `phi(t)>=-phi(0)`. Therefore

\[
\boxed{
\phi_-(t)
\le
\phi(0)
\min\left\{1,
2\operatorname{sech}^2(2\pi B|t|)
\right\}.
}
\tag{17}
\]

Let

\[
x_*:=\operatorname{arcosh}\sqrt2
=\log(1+\sqrt2).
\tag{18}
\]

Then `2 sech^2 x >=1` exactly for `0<=x<=x_*`, and

\[
\tanh x_*=\frac1{\sqrt2}.
\tag{19}
\]

Integrating (17), using evenness and the substitution `x=2 pi B t`, gives

\[
\begin{aligned}
\int_{\mathbb R}\phi_-(t)\,dt
&\le
\frac{\phi(0)}{\pi B}
\left(
\int_0^{x_*}1\,dx
+
2\int_{x_*}^{\infty}\operatorname{sech}^2x\,dx
\right)\\
&=
\frac{\phi(0)}{\pi B}
\left(
x_*+2(1-\tanh x_*)
\right)\\
&=
\frac{\phi(0)}{\pi B}
\left(
\log(1+\sqrt2)+2-\sqrt2
\right),
\end{aligned}
\tag{20}
\]

which proves (2).

WI-151 alone would give the weaker constant `2/pi = 0.636619...` after integration. The real two-point condition improves it to `C_*/pi = 0.467011...`; more importantly, (20) upgrades a pointwise fixed-radius obstruction into a global statement that also controls signed mass whose location and width vary with `B`.

## 3. Exponential tail localization

For

\[
a\ge a_B:=\frac{x_*}{2\pi B},
\tag{21}
\]

the `sech^2` branch is already the stronger part of (17). Hence

\[
\begin{aligned}
\int_{|t|\ge a}\phi_-(t)\,dt
&\le
4\phi(0)\int_a^\infty
\operatorname{sech}^2(2\pi Bt)\,dt\\
&=
\frac{2\phi(0)}{\pi B}
\left(1-\tanh(2\pi Ba)\right).
\end{aligned}
\tag{22}
\]

Since

\[
1-\tanh x=\frac{2}{e^{2x}+1}\le2e^{-2x},
\tag{23}
\]

(22) gives the second inequality in (4).

Two useful contrapositive forms are immediate. If the total negative mass is at least `delta>0`, then

\[
\boxed{
\phi(0)
\ge
\frac{\pi B}{C_*}\,\delta
=
2.14127470815\ldots\,B\delta.
}
\tag{24}
\]

If instead at least `delta` negative mass lies outside a radius `a>=a_B`, then

\[
\boxed{
\phi(0)
\ge
\frac{\pi B\,\delta}
{2(1-\tanh(2\pi Ba))}
\ge
\frac{\pi B\,\delta}{4}e^{4\pi Ba}.
}
\tag{25}
\]

Thus the only way a fully universal scalar profile can retain `O(1)` negative mass while `B` grows is to build at least an `Omega(B)` central spike and concentrate the negative mass in an `O(B^{-1})` boundary layer around the spectral origin. Any `O(1)` negative mass kept at a fixed positive spectral radius costs an exponentially large central value.

## 4. Quantitative collapse toward the nonnegative Fourier cone

Let

\[
N_-:=\int\phi_-,
\qquad
\phi=\phi_+-\phi_-.
\tag{26}
\]

Normalization `int phi=1` gives `int phi_+=1+N_-`. Define the normalized nonnegative profile

\[
\psi(t):=\frac{\phi_+(t)}{1+N_-}.
\tag{27}
\]

Then `psi>=0`, `int psi=1`, and a direct calculation gives

\[
\boxed{
\|\phi-\psi\|_{L^1}=2N_-.
}
\tag{28}
\]

Combining (20) and (28),

\[
\boxed{
\operatorname{dist}_{L^1}
\left(
\phi,
\{\psi\ge0:\int\psi=1\}
\right)
\le
\frac{2C_*}{\pi B}\phi(0)
=
0.934023080917\ldots\frac{\phi(0)}B.
}
\tag{29}
\]

Consequently, for any family with `B_T->infinity` and `phi_T(0)=o(B_T)`,

\[
\boxed{
\int(\phi_T)_-\to0,
\qquad
\operatorname{dist}_{L^1}(\phi_T,\text{normalized nonnegative profiles})\to0.
}
\tag{30}
\]

The Fourier transforms on the real axis inherit the same uniform approximation:

\[
\sup_{x\in\mathbb R}
|H_T(x)-\widehat\psi_T(x)|
\le
\|\phi_T-\psi_T\|_1
\to0.
\tag{31}
\]

This gives a precise meaning to the collapse of the one-scalar signed-kernel program: unless the central spectral value grows at least linearly with available depth, full finite-multiset universality drives the profile into the Fourier-positive cone in total variation, not merely pointwise at each fixed radius.

## 5. Relation to WI-145--WI-151

WI-145 rules out a genuine uncompensated negative outer tail using one off-line conjugate pair. WI-146 shows that the complete two-point tests alone do **not** control signed mass: a fixed intermediate negative mass can be repaired by an arbitrarily small amount of farther-out positive mass. WI-147--WI-150 progressively show that larger universal configurations recover Fourier positivity, Gaussian-smoothed positivity, or lattice-alias positivity under stronger depth/support hypotheses. WI-151 then uses positive phase masks to eliminate the higher-harmonic repair channel and obtains the pointwise floor (16).

The present deduction uses a piece of WI-146 that WI-151 did not need: real two-point configurations force `H>=0`, and therefore make `phi` positive definite. Integrating the stronger of that universal `|phi|<=phi(0)` bound and WI-151's hyperbolic floor yields the global budget (20).

In particular, the cheap remote-repair family of WI-146 cannot satisfy the **full** bounded-depth universal scalar inequality with fixed `O(1)` negative mass and a sublinear central value. To survive full universality at depth `B`, any such family must pay at least the linear central cost (24); if its negative mass remains at a fixed nonzero spectral radius, it must pay the exponential cost (25).

This closes a specific loophole left after WI-151. Moving a signed feature toward the origin does evade fixed-radius pointwise convergence, but it does **not** preserve a fixed signed budget for free: the entire negative mass is confined to a boundary layer whose integrated capacity is `O(phi(0)/B)`.

## 6. Prior-art audit and novelty boundary

The primary zero-side source remains Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. Lamzouri supplies the universal finite-multiset census for his specific square kernel. WI-145--WI-151 abstract that census to determine what any one-scalar replacement would have to satisfy. Lamzouri does not state (20), (22), or the total-variation collapse (29).

The Fourier ingredients used in Section 1 are classical. The triangular Fejer approximate identity is the standard Fourier-inversion device, and Bochner's theorem identifies continuous positive-definite functions with Fourier transforms of finite positive measures. The implication `H>=0`, `H=widehat phi`, `phi` continuous `L^1` => `H in L^1`, `int H=phi(0)`, and hence `phi` positive definite is a direct Fejer-inversion argument under the present hypotheses.

A targeted audit of the current `weil_inertia` frontier WI-145--WI-151 and searches around bounded-strip positive-definite functions, copositive kernels, signed Fourier profiles, and negative-mass bounds located no stored or published theorem giving the particular `O(phi(0)/B)` total-negative-mass budget (20) from the Lamzouri-form finite census. The integration once (15)--(16) are available is elementary. This is the novelty boundary used for persistence, not a claim of mathematical priority.

## 7. Scope and next falsification test

The bound does **not** show that `phi(0)=o(B)` follows from universal scalar census alone. A profile can still attempt to evade (30) by developing an increasingly tall central spike. Normalization `int phi=1` does not by itself bound that spike because its width may shrink. Therefore no unconditional zero-percentage improvement follows from (20).

The next arithmetic gate is now sharp: any signed scalar proposal that hopes to retain a non-vanishing negative budget must explain how its prime-side/test-function admissibility permits `phi(0)` to grow at least linearly with the normalized off-line depth `B`; if the useful negative mass is kept outside a fixed support radius, the required growth is exponential. Proving a source-specific upper bound on this central spike would convert WI-152 into a complete no-go for that signed scalar family.

Conversely, matrix-valued/joint observables, nonlinear incidence statistics, and inequalities restricted to actual zeta configurations do not factor through the universal one-scalar profile `phi` and remain live. Those are the appropriate places to look if the prime-side normalization does not allow the central-spike escape.