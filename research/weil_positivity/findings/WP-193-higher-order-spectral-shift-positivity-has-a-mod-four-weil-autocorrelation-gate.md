# WP-193 — Higher-order spectral-shift positivity has a mod-four Weil autocorrelation gate

**Status:** `LITERATURE+DERIVED + HIGHER-ORDER-SPECTRAL-SHIFT + EVEN-ORDER-POSITIVE-DENSITY + MOD-FOUR-AUTOCORRELATION-GATE + EXACT-FOURIER-CRITERION + FOURTH-ORDER-SURVIVOR-NARROWING + MATCHED-SCALAR-COUNTEREXAMPLE + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-188` excludes ordinary trace-class Birman--Krein scattering for the exact Gamma phase, while `WP-192` shows that the first canonical nontrace-class positive replacement, the second-order Koplienko remainder, is negative on sufficiently wide Weil autocorrelations for every nontrivial Hilbert--Schmidt pair. A natural question is whether going to a still higher regularized spectral-shift order can change that cone mismatch.

There is now a sharper answer. Higher-order spectral-shift theory supplies an `L^1` density `eta_n` for every Schatten perturbation `V in S^n`. A recent preprint of Pradhan--Skripka proves that **all even-order spectral-shift functions are nonnegative**. Thus even orders really do provide an independent positive density, rather than positivity inserted by hand.

Nevertheless the canonical Taylor-remainder functional has a rigid parity interaction with the Weil autocorrelation cone. For every even order `n=2m`, every nonzero bounded self-adjoint Schatten perturbation satisfies

\[
\boxed{
\lim_{L\to\infty}
L^{2m}\,\mathcal R_{2m}(h_L)
=
(-1)^m\,
\frac{\|V\|_{2m}^{2m}}{(2m)!}\,
\|g^{(m)}\|_2^2,
}
\tag{1}
\]

where `0!=g in C_c^infty(R)`, `h=g*\widetilde g`, and `h_L(t)=h(t/L)`. Consequently:

\[
\boxed{
2m\equiv2\pmod4
\quad\Longrightarrow\quad
\mathcal R_{2m}(h_L)<0
\text{ for all sufficiently large }L,
}
\tag{2}
\]

for **every** nontrivial pair. Orders `2,6,10,...` are therefore categorically excluded as bare global Weil-positive remainders. `WP-192` is the first member of this exact mod-four obstruction.

Orders `4,8,12,...` survive only this broad-scale test. They do not inherit Weil positivity merely because `eta_{4k}>=0`. On the full real autocorrelation cone the exact condition is instead that the **even part** of `eta_{4k}` be positive definite:

\[
\boxed{
\widehat{\eta_{4k}^{\rm ev}}(\xi)\ge0
\quad\text{for all }\xi.
}
\tag{3}
\]

That is a strictly stronger order structure than pointwise positivity of the spectral-shift density. Already in one dimension there is an exact fourth-order counterexample with `eta_4>=0` but `\widehat{\eta_4^{\rm ev}}<0` at a concrete frequency. Hence the first higher-order category not killed by (2), order four, is **not automatically Weil-positive either**.

The surviving spectral-shift question is therefore sharply narrowed: a Mathia-native fourth-order or `4k`-order construction would have to force positive definiteness of the even spectral-shift density, not merely its pointwise nonnegativity, while the same source geometry must still generate the finite Mangoldt, Gamma, and polar/global terms. No such construction is supplied here.

## 1. Higher-order spectral shift gives a genuine positive density at every even order

Let

\[
H=H^*,\qquad V=V^*\in\mathcal S^n,
\tag{4}
\]

with `H` bounded for the mass calculation below. Write

\[
\mathcal R_n(f;H,V)
=
\operatorname{Tr}\!\left(
 f(H+V)
 -\sum_{j=0}^{n-1}\frac1{j!}
 \frac{d^j}{dt^j}f(H+tV)\bigg|_{t=0}
\right).
\tag{5}
\]

Potapov--Skripka--Sukochev's higher-order spectral-shift theorem gives a unique `eta_n in L^1(R)` such that, for the standard admissible compactly supported smooth test functions,

\[
\boxed{
\mathcal R_n(f;H,V)
=
\int_{\mathbb R} f^{(n)}(\lambda)\eta_n(\lambda)\,d\lambda.
}
\tag{6}
\]

For `n=2`, Koplienko positivity `eta_2>=0` is classical. Pradhan and Skripka's December 2025 preprint proves the higher-order sign theorem

\[
\boxed{
\eta_{2m}\ge0
\quad\text{for every }m\ge1
}
\tag{7}
\]

for self-adjoint Schatten perturbations, including possibly unbounded `H`. Their result is current preprint literature, not a Mathia theorem, and its publication status should be kept distinct from the exact derivations below.

The point for this branch is that (7) passes the **independent-sign** test at the density level: no RH assumption, zeta zero divisor, or Weil kernel is used to prove `eta_{2m}>=0`. The question is whether the canonical functional (6) is positive on the right test cone.

## 2. Every even-order density has a fixed positive total mass

Because `H` is bounded and `V` is compact, the spectral hull of `H+tV`, `0<=t<=1`, is compact. Choose a compactly supported smooth `f` that agrees on that hull with

\[
f(\lambda)=\frac{\lambda^n}{n!}.
\tag{8}
\]

Functional calculus makes (5) identical to the polynomial calculation. In

\[
\frac{(H+tV)^n}{n!},
\tag{9}
\]

the coefficient of `t^n` is exactly `V^n/n!`; all terms of lower degree are removed by the Taylor polynomial in (5). Therefore

\[
\mathcal R_n(f;H,V)=\frac1{n!}\operatorname{Tr}(V^n).
\tag{10}
\]

Since `f^{(n)}=1` on the support of `eta_n`, equation (6) gives

\[
\boxed{
\int_{\mathbb R}\eta_n(\lambda)\,d\lambda
=\frac1{n!}\operatorname{Tr}(V^n).
}
\tag{11}
\]

At even order `n=2m`, self-adjointness implies

\[
\boxed{
\int\eta_{2m}
=\frac{\|V\|_{2m}^{2m}}{(2m)!}>0
\quad\text{whenever }V\ne0.
}
\tag{12}
\]

Notice that the broad-scale obstruction below needs only (12) and `eta_{2m} in L^1`; it does not depend on the newer pointwise positivity theorem (7).

## 3. Autocorrelations alternate sign under even differentiation

Let `0!=g in C_c^infty(R)` and define

\[
\widetilde g(x)=\overline{g(-x)},
\qquad
h=g*\widetilde g.
\tag{13}
\]

Then `h` is a smooth compactly supported Weil autocorrelation and

\[
\widehat h(\xi)=|\widehat g(\xi)|^2\ge0.
\tag{14}
\]

At the origin, repeated integration by parts gives

\[
\begin{aligned}
h^{(2m)}(0)
&=\int_{\mathbb R}g(x)\overline{g^{(2m)}(x)}\,dx\\
&=(-1)^m\int_{\mathbb R}|g^{(m)}(x)|^2\,dx.
\end{aligned}
\tag{15}
\]

Thus

\[
\boxed{
h^{(2m)}(0)=(-1)^m\|g^{(m)}\|_2^2.}
\tag{16}
\]

This is the higher-order version of the strict concavity identity used in `WP-192`. The sign alternates every two spectral-shift orders.

Now use the `L^2`-normalized dilation

\[
g_L(x)=L^{-1/2}g(x/L),
\qquad
h_L=g_L*\widetilde g_L.
\tag{17}
\]

Then

\[
h_L(t)=h(t/L),
\qquad
h_L^{(2m)}(t)=L^{-2m}h^{(2m)}(t/L).
\tag{18}
\]

Substituting into (6),

\[
L^{2m}\mathcal R_{2m}(h_L;H,V)
=
\int_{\mathbb R}
 h^{(2m)}(\lambda/L)\eta_{2m}(\lambda)\,d\lambda.
\tag{19}
\]

Because `h^{(2m)}` is bounded and continuous and `eta_{2m} in L^1`, dominated convergence gives

\[
\begin{aligned}
\lim_{L\to\infty}
L^{2m}\mathcal R_{2m}(h_L;H,V)
&=h^{(2m)}(0)\int\eta_{2m}\\
&=(-1)^m\|g^{(m)}\|_2^2
\frac{\|V\|_{2m}^{2m}}{(2m)!},
\end{aligned}
\tag{20}
\]

which proves (1).

Therefore every nontrivial remainder of order

\[
2m\equiv2\pmod4
\tag{21}
\]

is eventually strictly negative on **every** dilated nonzero autocorrelation family. No spectral engineering of `H` or `V` can repair the bare functional at orders `2,6,10,...`; only making `V=0` removes the positive mass, and then all arithmetic content disappears.

## 4. The exact Weil-cone criterion is Fourier positivity of the even density

For even `n=2m`, the derivative `h^{(2m)}` is even, so only

\[
\eta_{2m}^{\rm ev}(x)
=\frac12\bigl(\eta_{2m}(x)+\eta_{2m}(-x)\bigr)
\tag{22}
\]

contributes. With the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-i\xi x}\,dx,
\tag{23}
\]

Fourier inversion and (14) give

\[
\boxed{
\mathcal R_{2m}(h;H,V)
=
\frac{(-1)^m}{2\pi}
\int_{\mathbb R}
 \xi^{2m}|\widehat g(\xi)|^2
 \widehat{\eta_{2m}^{\rm ev}}(\xi)\,d\xi.
}
\tag{24}
\]

Since `eta_{2m}^{ev} in L^1` is real and even, its Fourier transform is continuous, real, and even. Equation (12) gives

\[
\widehat{\eta_{2m}^{\rm ev}}(0)
=\int\eta_{2m}>0.
\tag{25}
\]

Equation (24) now separates the two parity classes exactly.

For `2m=4k+2`, the multiplier has the wrong sign already on a punctured neighborhood of `xi=0`, by continuity and (25). This is the Fourier form of the wide-dilation no-go.

For `2m=4k`, positivity on **all real compactly supported smooth autocorrelations** is equivalent to

\[
\boxed{
\widehat{\eta_{4k}^{\rm ev}}(\xi)\ge0
\quad\text{for every }\xi.
}
\tag{26}
\]

Sufficiency is immediate from (24). For necessity, if the continuous multiplier is negative on an interval around some nonzero frequency, a broad compactly supported smooth envelope modulated at that frequency has Fourier mass concentrated inside that interval and makes (24) negative.

Thus the order required by the Weil cone is not

\[
\eta_{4k}(x)\ge0
\tag{27}
\]

but positive definiteness of its even part. These are independent positivity notions.

## 5. Exact scalar fourth-order control: `eta_4>=0` still gives a negative autocorrelation

The distinction is already visible in the smallest possible system. Work on the one-dimensional Hilbert space and take

\[
H=-a,
\qquad
V=2a,
\qquad
a>0.
\tag{28}
\]

The scalar Taylor integral remainder gives the fourth-order spectral-shift density exactly:

\[
\boxed{
\eta_4(\lambda)
=\frac{(a-\lambda)^3}{6}\,
\mathbf1_{[-a,a]}(\lambda).
}
\tag{29}
\]

It is pointwise nonnegative. Its even part is

\[
\eta_4^{\rm ev}(\lambda)
=\frac{a^3+3a\lambda^2}{6}\,
\mathbf1_{[-a,a]}(\lambda).
\tag{30}
\]

A direct cosine transform gives, with `u=a xi`,

\[
\widehat{\eta_4^{\rm ev}}(\xi)
=
\frac{a^4}{3}
\left(
4\frac{\sin u}{u}
+6\frac{\cos u}{u^2}
-6\frac{\sin u}{u^3}
\right).
\tag{31}
\]

At the explicit frequency `xi=pi/a`,

\[
\boxed{
\widehat{\eta_4^{\rm ev}}(\pi/a)
=-\frac{2a^4}{\pi^2}<0.
}
\tag{32}
\]

By the concentration argument after (26), there is therefore a real `g in C_c^infty(R)` for which

\[
\boxed{
\mathcal R_4(g*\widetilde g;H,V)<0,
}
\tag{33}
\]

even though `eta_4>=0` everywhere.

This is a decisive matched control. The new even-order positivity theorem does not turn the fourth-order Taylor remainder into a generic Weil-positive functional. A special fourth-order pair could still satisfy (26), but that property would be extra structure not supplied by spectral-shift positivity itself.

## 6. Aggressive falsification and exact scope

**Changing the spectral pair cannot rescue orders `4k+2`.** Equation (20) depends on the pair only through the strictly positive mass `||V||_{2m}^{2m}/(2m)!`. Support, multiplicity, detailed density shape, and sign of `V` do not affect the eventual negative sign.

**Pointwise density positivity cannot rescue order four.** Equations (29)--(33) give an exact one-dimensional counterexample. Any argument that uses only `eta_4>=0` has insufficient information to order the Weil cone.

**Orders `4k` are not ruled out universally.** Equation (26) identifies the exact extra theorem they would need. The finding does not prove that every higher-order spectral-shift density violates positive definiteness, nor does it exclude a source-specific pair whose even density satisfies (26).

**A counterterm or transform changes the mechanism.** Adding a source-forced functional to (6), changing the test by a canonical nonlocal transform, or coupling the spectral-shift sector nonseparably to finite/archimedean data can change the sign. Such an operation must then prove positivity for the assembled functional and derive the Weil coefficients intrinsically; it cannot cite `eta_{2m}>=0` as sufficient.

**Unbounded and relative-Schatten extensions do not evade the cone issue automatically.** Broader higher-order spectral-shift theories can change support, uniqueness conventions, or admissible tests. Whenever the assembled functional still has the form `int h^(n) eta_n` with an integrable even-order density of nonzero mass, the same low-frequency parity test applies. More singular renormalized formulas with non-`L^1` counterterms lie outside this exact claim and must establish their own coercivity theorem.

**Nothing here creates arithmetic incidence.** The mod-four gate is arithmetic-free. It is a compatibility test for one candidate analytic category; it supplies neither the Mangoldt selector nor the Gamma/polar completion.

## 7. Prior art and novelty boundary

The operator theory is classical or recent external prior art:

- Denis Potapov, Anna Skripka, and Fedor Sukochev, *Spectral shift function of higher order*, Inventiones Mathematicae **193** (2013), 501--538. This establishes the higher-order trace formula and `L^1` spectral-shift functions for Schatten perturbations.
- Chandan Pradhan and Anna Skripka, *Positivity of spectral shift functions and infinite-dimensional BMV conjecture*, arXiv:`2512.05587` (submitted 5 December 2025). The preprint proves nonnegativity of every even-order spectral-shift function and the corresponding sign theorem for odd order under sign-definite perturbations.
- Anna Skripka, *On positivity of spectral shift functions*, Linear Algebra and its Applications **523** (2017), 118--130, DOI `10.1016/j.laa.2017.02.026`. This gives the earlier partial higher-order positivity results and shows why the 2025 theorem is a genuine strengthening of the available sign theory.

No novelty is claimed for higher-order spectral shift, Taylor-remainder trace formulas, or the even-order density positivity theorem. A targeted search of higher-order spectral-shift, positivity, Fourier, and autocorrelation literature did not expose the specific `weil_positivity` consequence derived here: the universal mod-four dilation limit (20), the exact autocorrelation criterion (26), or the scalar fourth-order control (29)--(33). The durable Mathia delta is this branch-specific cone classification, not a new operator-theory theorem.

## 8. Consequence for `weil_positivity`

`WP-192` did not merely reveal an accident of second order. The whole sequence of bare even-order spectral-shift remainders splits into two classes:

\[
\boxed{
\begin{array}{ll}
n\equiv2\pmod4:&
\text{universally negative on sufficiently wide Weil autocorrelations},\\[1mm]
n\equiv0\pmod4:&
\text{broad-scale sign survives, but full Weil positivity requires }
\widehat{\eta_n^{\rm ev}}\ge0.
\end{array}
}
\tag{34}
\]

Thus simply moving from Koplienko order two to a higher positive spectral-shift density is not a generic category escape. The first logically surviving order is four, and its required extra structure is now precise: **the source must force a positive-definite even spectral-shift density**, not merely a nonnegative one.

That is still only an analytic gate. A viable Mathia mechanism must additionally explain why the same construction produces the finite-prime Mangoldt term, the exact archimedean Gamma contribution, and the polar/global counterterms, with the final sign proved before any RH identification. A fourth-order pair engineered to satisfy (26) but fitted afterward to the explicit formula would remain a repackaging.

The next useful falsification target is therefore not “try another spectral-shift order.” It is whether any intrinsic finite--archimedean geometry in this line naturally generates a `4k`-order relative density satisfying the positive-definiteness condition (26) **before scalar arithmetic matching**. If no source-forced mechanism supplies that stronger order, the higher-order spectral-shift route closes at the same independence gate as its lower-order predecessors.

## Dependencies

- `research/weil_positivity/findings/WP-188-ordinary-trace-class-scattering-cannot-carry-the-exact-gamma-phase.md`
- `research/weil_positivity/findings/WP-192-koplienko-hilbert-schmidt-positivity-misses-the-weil-autocorrelation-cone.md`

## Bottom line

Higher-order spectral-shift theory now offers a genuine independent positive density at every even order, but the Weil autocorrelation cone sees the derivative parity and the Fourier order of that density. Orders `2 mod 4` fail universally by their positive total mass. Orders `0 mod 4` need the much stronger condition that the even spectral-shift density be positive definite, and pointwise positivity already fails to imply this in an exact one-dimensional fourth-order example.

So higher-order regularization does not by itself repair the positivity problem. It converts the vague escape left after `WP-192` into a precise structural obligation: only a source-forced `4k`-order density with positive-definite even part can pass the analytic sign gate, and it must still participate in the same intrinsic finite--archimedean completion before it could bear on Weil positivity or RH.
