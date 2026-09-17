# RE-190 — Shrinking Euler sampling windows collapse to reciprocal-mass rank one

**Status:** `EXACT-DERIVED + EULER-SPECTRAL-SAMPLING + SHRINKING-WINDOW + OPERATOR-NORM-RANK-ONE + SELECTOR-SCALE + CONDITIONING-BOUND + SOURCE-INFORMATION-BOUND`.

**Parent findings:** RE-174, RE-188, RE-189.

`RE-189` shows that sufficiently high factorial-normalized derivatives at the Mertens boundary eventually lose prime-location information and collapse toward a common net-multiplicity mode. A different possible escape is to stop differentiating and instead sample the exact Euler discrepancy at many nearby spectral points. The continuum might appear to carry more robust information than a finite Taylor jet.

On a fixed multiplicative selector window it does not, as long as the spectral window itself shrinks to `s=1`.

Fix constants `0<A<B<infinity`. Let a finite ordinary-prime multiplicity perturbation be supported on

\[
Ap\le q\le Bp,
\]

with signed coefficients `c_q`, and define

\[
D_p(s):=\sum_{Ap\le q\le Bp}c_q\log(1-q^{-s})^{-1}.
\tag{1}
\]

Put

\[
L_p:=\log p,
\qquad
A_p:=\sum_q\frac{c_q}{q},
\qquad
V_p:=\sum_q\frac{|c_q|}{q}.
\tag{2}
\]

Let `T_p>=0` satisfy

\[
T_p=o(L_p),
\tag{3}
\]

and sample the exact Euler discrepancy throughout

\[
s=1+\frac{\tau}{L_p},
\qquad |\tau|\le T_p.
\tag{4}
\]

After removing the common first-harmonic factor by

\[
G_p(\tau):=e^\tau D_p\!\left(1+\frac{\tau}{L_p}\right),
\tag{5}
\]

there is a constant `C_{A,B}` such that

\[
\boxed{
\sup_{|\tau|\le T_p}
|G_p(\tau)-A_p|
\le
C_{A,B}
\left(
\frac{T_p}{\log p}+p^{-1+o(1)}
\right)V_p.
}
\tag{6}
\]

Hence, uniformly for every `T_p=o(log p)`, the entire continuum of Euler values in the shrinking spectral neighborhood

\[
|s-1|\le \frac{T_p}{\log p}=o(1)
\tag{7}
\]

is asymptotically one-dimensional at the natural weighted-total-variation scale. After the trivial normalization in (5), it sees only the reciprocal-mass coordinate `A_p` to relative operator error `o(1)`.

Equivalently, if the coefficient space is given the norm

\[
\|c\|_{p,1}:=\sum_q\frac{|c_q|}{q},
\tag{8}
\]

and `\mathcal E_p` maps `c` to the function `G_p` on `[-T_p,T_p]`, then

\[
\boxed{
\left\|
\mathcal E_p-\mathbf 1\otimes r_p
\right\|_{\ell^1(q^{-1})\to L^\infty[-T_p,T_p]}
=o(1),
\qquad
r_p(c)=\sum_q\frac{c_q}{q}.
}
\tag{9}
\]

This is an operator-norm rank-one collapse, not merely a statement about one chosen packet or one finite sampling grid.

## 1. Uniform first-harmonic reduction

Write

\[
q=pe^\alpha,
\qquad
\alpha\in[\log A,\log B].
\tag{10}
\]

For `s=1+tau/L_p` with `|tau|<=T_p`, condition (3) gives `Re(s)=1-o(1)` uniformly. The exact Euler factor has the absolutely convergent expansion

\[
\log(1-q^{-s})^{-1}
=q^{-s}+O_{A,B}(q^{-2\operatorname{Re}s}),
\tag{11}
\]

uniformly throughout the sampled window for large `p`.

For the first harmonic,

\[
\begin{aligned}
e^\tau q^{-1-\tau/L_p}
&=q^{-1}
\exp\!\left(
\tau-\tau\frac{\log q}{L_p}
\right)\\
&=q^{-1}
\exp\!\left(-\tau\frac{\alpha}{L_p}\right).
\end{aligned}
\tag{12}
\]

Because `alpha` stays in a fixed compact interval and `T_p/L_p->0`,

\[
\exp\!\left(-\tau\frac{\alpha}{L_p}\right)
=1+O_{A,B}\!\left(\frac{T_p}{L_p}\right)
\tag{13}
\]

uniformly in both `q` and `tau`. Therefore

\[
e^\tau\sum_qc_qq^{-1-\tau/L_p}
=A_p+O_{A,B}\!\left(\frac{T_p}{L_p}V_p\right).
\tag{14}
\]

The source-location dependence inside a fixed multiplicative selector shell has already disappeared at this stage: a spectral displacement `o(1)` changes the relative weight of two shell locations by only `1+o(1)`.

## 2. Prime powers remain below the natural source scale

It remains to control the higher prime powers in (11). Uniformly on the same window,

\[
e^\tau q^{-2\operatorname{Re}s}
\le
p^{-2+o(1)},
\tag{15}
\]

because `T_p=o(log p)` implies `e^{O(T_p)}=p^{o(1)}` and `q` is comparable with `p`. Moreover

\[
\sum_q|c_q|
\le Bp\sum_q\frac{|c_q|}{q}
=BpV_p.
\tag{16}
\]

Consequently

\[
e^\tau
\sum_q|c_q|q^{-2\operatorname{Re}s}
\le
p^{-1+o(1)}V_p.
\tag{17}
\]

Combining (14) and (17) proves (6). Since both error terms tend to zero, (9) follows directly.

No prime-distribution theorem is used. The result is local to the exact Euler kernel and remains valid for arbitrary finite signed coefficients; honest `{0,1,2}` multiplicity controls are a special case.

## 3. Dense sampling does not increase the effective rank

Choose any number `m_p`, possibly tending to infinity arbitrarily fast, and arbitrary sampling points

\[
\tau_1,\ldots,\tau_{m_p}\in[-T_p,T_p].
\]

The response matrix has entries

\[
M_{kq}
:=e^{\tau_k}
\log\!\left(1-q^{-1-\tau_k/L_p}\right)^{-1}.
\tag{18}
\]

Equations (11)--(17) imply uniformly in every row and every selector-scale prime that

\[
M_{kq}
=\frac1q\left(1+o(1)\right)
\tag{19}
\]

in the weighted `ell^1(q^{-1})` operator sense made precise by (9). Thus adding more points inside the shrinking window only adds asymptotically parallel observations. The conclusion does not depend on a Taylor truncation or on choosing a polynomial interpolation basis.

The scale behind the collapse is transparent. For two shell locations `q=pe^alpha`, exact first-harmonic sampling distinguishes `alpha` through

\[
e^{-(s-1)\alpha}.
\tag{20}
\]

An `O(1)` distinction across `alpha=O(1)` therefore requires

\[
|s-1|=\Theta(1).
\tag{21}
\]

Any `o(1)` spectral neighborhood is too narrow to provide an order-one location coordinate on a fixed multiplicative shell, irrespective of how densely it is sampled.

## 4. Relation to RE-189 and the scalar frontier

`RE-189` and the present result describe two different common-mode collapses. Very high normalized derivatives at the single point `s=1` are eventually dominated by the common singularity structure of the exact Euler factors and approach **net multiplicity**. Exact values throughout an `o(1)` neighborhood of `s=1`, after the first-harmonic normalization (5), approach **reciprocal mass**.

There is no contradiction. Uniformly small differences of analytic functions on a shrinking real interval need not control derivatives whose order grows with `p`. Extracting such derivatives from near-boundary samples is increasingly ill-conditioned. Conversely, `RE-189` does not say that exact spectral values a constant distance from `1` collapse; moving `s` by `Theta(1)` changes the Mellin weight across a selector shell by an order-one factor and leaves the regime proved here.

This closes a natural loophole in the scalar matched-control program. Replacing a finite or growing jet by an arbitrarily dense cloud of **near-boundary** spectral samples does not automatically supply a richer source fingerprint. A source-sensitive continuation must instead use at least one of: spectral probes a constant distance from `1`, support spanning genuinely different logarithmic scales, a joint observable whose conditioning is not governed by (20), or a nonlocal invariant tied more directly to the Robin destination.

## 5. Adversarial checks and scope

**The window must be shrinking.** If `|s-1|` is bounded below by a positive constant, (13) no longer gives a common row and shell location can remain visible at order one.

**The support must be selector-scale in the multiplicative sense.** The proof uses `log(q/p)=O(1)`. A packet spanning powers such as `[p^a,p^b]` has `log(q/p)=Theta(log p)` and can retain several spectral coordinates even when `s-1` is small on a different scale.

**This is approximate conditioning, not exact analytic non-uniqueness.** Exact equality of Euler discrepancies on a real interval would determine the analytic function and can carry much more information. Equation (9) says that recovering that information from selector-scale packets requires resolving an `o(V_p)` residue.

**Growing boundary derivatives are outside the claim.** Numerical differentiation of the shrinking-window data can amplify the small residue by large factors. That is precisely why the high-jet regime of `RE-189` must be analyzed separately rather than inferred from (6).

**No Robin impossibility theorem follows.** The result only prices one proposed scalar information channel. It does not rule out constant-distance spectral probes, multi-scale controls, or source-specific constraints not encoded by local Euler values.

## 6. Representation and prior-art audit

The object is an ordinary-prime multiplicity perturbation; the representation is its exact Euler discrepancy as a function of the spectral variable. After this representation, the core mechanism is generic: a Mellin/Laplace kernel restricted to logarithmically narrow support becomes nearly rank one when the dual spectral window shrinks faster than the inverse support width. The source-specific content is the exact Euler local factor, the uniform suppression of its prime-power remainder, and the interpretation of the resulting low-rank channel inside the ordinary-prime Robin matched-control problem.

The theorem should therefore be read as an **observable-conditioning statement**, not as reconstruction or arithmetic rigidity. A targeted prior-art search around shrinking Mellin windows, Dirichlet polynomials near `s=1`, and local Euler factors found standard adjacent Mellin/Euler-product material but no load-bearing theorem needed for (6)--(9). The proof is elementary and self-contained, so `SOURCES.md` requires no new dependency.

No clue transition is justified by this result. The existing clues concern peak/selector coupling, extremal discretization, regular-peak workload, and reciprocal zero-box visibility; none is resolved or contradicted by the rank-one conditioning statement here.

## 7. Research consequence

The scalar frontier is now narrower in two independent directions. `RE-189` says that pushing a single boundary Taylor coordinate to very high order eventually produces a universal common mode. `RE-190` says that replacing Taylor data by an arbitrarily dense continuum of exact values in any `o(1)` neighborhood of the boundary also produces a common mode at natural selector scale.

Thus **more local scalar data is not the same as more robust source information**. The next clean scalar experiment is to move spectral samples a constant distance into the absolutely convergent half-plane and ask whether an honest matched control can still preserve them while retaining the transient Robin excursion. In parallel, multi-scale support is the natural adversarial test of the rank-one argument, because it enlarges the logarithmic source diameter that the spectral variable can resolve.

**Provenance:** derived against default-branch snapshot `66e63b46a47f4d110204fd3b1a203af5fc79ffe5`; stable finding prefix `RE`; no adversarial sidecar was open; local clues were inspected; no clue-state, README, graph, intuition, or source-registry mutation required.