# RE-176 — First-slope matching forces a KV terminal-tail capacity

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + TWO-JET-MATCHING + MINIMAL-SIGN-ESCAPE + KV-TAIL-CAPACITY + PLACEMENT-BOUND + ROBIN-SCALE-CONDITIONING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-166, RE-168, RE-169, RE-173, RE-175.

`RE-175` shows that matching the Mertens charge and the first Euler boundary slope forces at least two sign changes in any sufficiently far-out prime-supported multiplicity perturbation. That theorem is qualitative: after the initial deletion packet one could try to add a positive compensating phase and then push the required final negative phase arbitrarily far away, hoping that its mass becomes negligible.

For the minimal two-sign-change geometry this does not work under a Korobov--Vinogradov source envelope. The first slope does more than demand one extra alternation: it leaves a **fixed weighted debt** in the terminal one-sign tail. Moving that tail farther out decreases the required Mertens mass only like the reciprocal log-distance, while the first-slope mass remains on the original Robin scale. A KV envelope gives that one-sign tail only

\[
\boxed{
\ell_{\rm KV}(Y)e^{-bV(Y)},
\qquad
\ell_{\rm KV}(Y):=\frac{\log Y}{V(Y)},
\qquad
V(Y):=\frac{(\log Y)^{3/5}}{(\log\log Y)^{1/5}},
}
\tag{1}
\]

of first-slope capacity beyond height `Y`.

Concretely, retain the `RE-173` deletion packet in `[2p,3p]`, of Mertens mass

\[
d_p\asymp \frac1{\sqrt p\log p}.
\tag{2}
\]

Suppose a redesigned control has exactly the minimal sign pattern

\[
-\quad +\quad -,
\tag{3}
\]

with the positive phase beginning at `16p`, the final negative phase beginning at `Y`, exact matching

\[
D_Q(1+)=D_Q'(1+)=0,
\tag{4}
\]

and quantitative source fidelity

\[
|\vartheta_Q(x)-\vartheta(x)|
\le C_b x e^{-bV(x)}
\qquad (x\ge 2p)
\tag{5}
\]

for some fixed `b>0`. Then necessarily

\[
\boxed{
\sqrt p\log p\,
\ell_{\rm KV}(Y)e^{-bV(Y)}\gg_b 1.
}
\tag{6}
\]

In particular,

\[
\boxed{
bV(Y)\le \left(\frac12+o(1)\right)\log p.}
\tag{7}
\]

Thus the second sign change cannot be exiled beyond the corresponding KV first-slope capacity horizon. The result does **not** yet rule out a two-sign-change control inside that horizon, nor a control with more alternations. It closes only the simplest remote redesign of `RE-173` and exposes a new conditioning scale between the scalar Mertens charge and the full Euler germ.

## 1. Exact two-jet bookkeeping turns the terminal phase into a positive debt

Use the notation of `RE-175`,

\[
H(q):=\log\frac q{q-1},
\qquad
B(q):=-J_1(q)=\frac{\log q}{q-1},
\qquad
A(q):=\frac{B(q)}{H(q)}.
\tag{8}
\]

For large primes,

\[
\log q<A(q)<\frac q{q-1}\log q.
\tag{9}
\]

Let `D`, `P`, and `N` denote respectively the initial negative, middle positive, and final negative phases of the perturbation. We allow arbitrary integer magnitudes inside a phase; only the sign is fixed. Put

\[
h_D:=\sum_{q\in D}(-c_q)H(q),
\qquad
h_P:=\sum_{q\in P}c_qH(q),
\qquad
h_N:=\sum_{q\in N}(-c_q)H(q),
\tag{10}
\]

and analogously

\[
b_D:=\sum_{q\in D}(-c_q)B(q),
\qquad
b_P:=\sum_{q\in P}c_qB(q),
\qquad
b_N:=\sum_{q\in N}(-c_q)B(q).
\tag{11}
\]

Assume the absolute convergence required for the first boundary jet. Exact zeroth- and first-jet matching is equivalent to

\[
\boxed{
h_P=h_D+h_N,\qquad b_P=b_D+b_N.}
\tag{12}
\]

Write the phase-averaged logarithmic locations

\[
a_D:=\frac{b_D}{h_D},
\qquad
a_P:=\frac{b_P}{h_P},
\qquad
a_N:=\frac{b_N}{h_N}.
\tag{13}
\]

Equation (12) gives the exact barycentric identity

\[
\boxed{
h_D(a_P-a_D)=h_N(a_N-a_P).}
\tag{14}
\]

This is the quantitative content hidden behind the second sign change. More importantly for a remote tail,

\[
\begin{aligned}
b_N
&=h_Na_N\\
&=h_D(a_P-a_D)+h_Na_P\\
&\ge h_D(a_P-a_D).
\end{aligned}
\tag{15}
\]

For the canonical `RE-173` deletion packet, `D\subset[2p,3p]`, `c_q=-1` on `D`, and

\[
h_D=d_p\asymp \frac1{\sqrt p\log p}.
\tag{16}
\]

If the middle positive phase begins at `16p`, then (9) gives

\[
a_P\ge \log(16p),
\qquad
a_D\le (1+o(1))\log(3p),
\tag{17}
\]

hence

\[
\boxed{
a_P-a_D\ge \log(16/3)-o(1).}
\tag{18}
\]

Combining (15)--(18),

\[
\boxed{
b_N
\ge
\bigl(\log(16/3)-o(1)\bigr)d_p
\asymp
\frac1{\sqrt p\log p}.}
\tag{19}
\]

The important point is that this lower bound is on the **first-slope mass** `b_N`, not on the terminal Mertens mass `h_N`. The latter may tend to zero as the final phase moves outward; (14) indeed permits that because `a_N` grows. But the product `h_Na_N` cannot fall below the fixed debt (19). Distance trades Mertens mass for logarithmic leverage without erasing the first-slope workload.

The same statement holds with `16` replaced by any fixed `lambda>3`, with `log(16/3)` replaced by `log(lambda/3)+o(1)`.

## 2. A one-sign KV tail has only `ell_KV(Y)e^{-bV(Y)}` first-slope capacity

Now use the source envelope. Let

\[
\Delta\vartheta(x)
:=\vartheta_Q(x)-\vartheta(x)
=\sum_{q\le x}c_q\log q.
\tag{20}
\]

Suppose the final negative phase begins at `Y`, so every nonzero coefficient after `Y` is negative. Define its increasing Chebyshev mass

\[
M_N(x)
:=\sum_{\substack{Y\le q\le x\\q\in N}}(-c_q)\log q.
\tag{21}
\]

For `x\ge Y`,

\[
\Delta\vartheta(x)=C_Y-M_N(x),
\qquad
C_Y:=\Delta\vartheta(Y^-).
\tag{22}
\]

From (5), with an immaterial endpoint adjustment if `Y` itself is modified,

\[
|C_Y|\ll_b Ye^{-bV(Y)},
\qquad
M_N(x)\ll_b Ye^{-bV(Y)}+xe^{-bV(x)}.
\tag{23}
\]

The weighted prime mass appearing in the boundary slope satisfies

\[
\begin{aligned}
b_N
&=\sum_{q\in N}(-c_q)\frac{\log q}{q-1}\\
&\le (1+o(1))
\sum_{q\in N}(-c_q)\frac{\log q}{q}.
\end{aligned}
\tag{24}
\]

Stieltjes partial summation and (23) give

\[
\begin{aligned}
\sum_{q\in N}(-c_q)\frac{\log q}{q}
&=\int_{[Y,\infty)}\frac1t\,dM_N(t)\\
&\ll_b
e^{-bV(Y)}
+
\int_Y^\infty e^{-bV(t)}\frac{dt}{t}.
\end{aligned}
\tag{25}
\]

The boundary term at infinity vanishes because `M_N(x)/x\ll e^{-bV(x)}+O(Y/x)`.

Put `u=log t` and

\[
W(u):=V(e^u)=\frac{u^{3/5}}{(\log u)^{1/5}}.
\tag{26}
\]

Then

\[
W'(u)
=
\left(\frac35-\frac1{5\log u}\right)\frac{W(u)}u.
\tag{27}
\]

A one-sided Laplace estimate, obtained directly by integration by parts using (27), yields

\[
\boxed{
\int_Y^\infty e^{-bV(t)}\frac{dt}{t}
=
\left(\frac5{3b}+o(1)\right)
\frac{\log Y}{V(Y)}e^{-bV(Y)}.}
\tag{28}
\]

Therefore

\[
\boxed{
b_N
\ll_b
\ell_{\rm KV}(Y)e^{-bV(Y)},
\qquad
\ell_{\rm KV}(Y)=\frac{\log Y}{V(Y)}.}
\tag{29}
\]

This is the first-slope analogue of the remote KV capacities in `RE-165`--`RE-168`. The extra factor `log Y` relative to the Robin remote capacity is not bookkeeping noise: the boundary derivative weights a changed prime by approximately `log q/q`, whereas the remote Robin kernel contributes one further logarithmic denominator after partial summation.

## 3. The terminal sign change has a moving KV horizon

Combining the lower debt (19) with the tail capacity (29) gives

\[
\frac1{\sqrt p\log p}
\ll_b
\ell_{\rm KV}(Y)e^{-bV(Y)},
\tag{30}
\]

or equivalently the announced necessary condition

\[
\boxed{
\mathfrak J_b(p,Y)
:=
\sqrt p\log p\,
\ell_{\rm KV}(Y)e^{-bV(Y)}
\gg_b1.}
\tag{31}
\]

Taking logarithms,

\[
bV(Y)
\le
\frac12\log p
+
\log\log p
+
\log\ell_{\rm KV}(Y)
+O_b(1).
\tag{32}
\]

Since `log ell_KV(Y)=O(log V(Y))` after inverting the defining relation for `V`, (32) first implies `V(Y)=O_b(log p)` and then

\[
\boxed{
bV(Y)
\le
\left(\frac12+o(1)\right)\log p,}
\tag{33}
\]

which is (7).

There is a useful comparison with the `RE-166` Robin-capacity center. Let `v_*(p)` solve

\[
\sqrt p\log p\,\frac{e^{-bv_*}}{v_*}=1,
\tag{34}
\]

and let `v_1(p)` be the corresponding capacity-one center for (31), with `Y=Y(v_1)` determined by `V(Y)=v_1`:

\[
\sqrt p\log p\,
\frac{\log Y(v_1)}{v_1}e^{-bv_1}=1.
\tag{35}
\]

Subtracting the logarithms of (34) and (35) gives

\[
b(v_1-v_*)
+
\log\frac{v_1}{v_*}
=
\log\log Y(v_1).
\tag{36}
\]

The inversion

\[
V(Y)^5=\frac{(\log Y)^3}{\log\log Y}
\tag{37}
\]

implies

\[
\log\log Y(v)
=
\frac53\log v
+
\frac13\log\log v
+O(1).
\tag{38}
\]

Since `v_*,v_1\sim (2b)^{-1}\log p`, (36)--(38) yield

\[
\boxed{
v_1-v_*
=
\frac5{3b}\log\log p
+
\frac1{3b}\log\log\log p
+O_b(1).}
\tag{39}
\]

So the first boundary slope is well conditioned at the *local* Robin scale, as `RE-175` showed, but its **remote** one-sign tail capacity extends farther than the Robin remote-capacity center by a slowly diverging `V`-distance. This separates two notions that would otherwise be easy to conflate: detecting delayed compensation at a fixed multiplicative distance and preventing that compensation from being reorganized across the entire KV tail.

## 4. Adversarial checks and exact scope

**The two-sign-change hypothesis is essential.** The upper bound (29) uses the fact that after `Y` every modification has the same sign, making `M_N` monotone. A control with further positive phases can cancel Chebyshev discrepancy inside the remote tail and is not covered by this argument. Thus `RE-176` prices the minimal escape forced by `RE-175`; it does not inductively settle all higher oscillation counts.

**The result does not supply the first slope from Robin arithmetic.** As in `RE-175`, imposing `D_Q'(1+)=0` is additional source information. The theorem states what that information would force on a matched control, not that the CA selector or Robin inequality already controls the boundary derivative.

**The KV envelope is used on the source discrepancy itself.** The argument assumes (5) for `vartheta_Q-vartheta`, exactly the matched-source fidelity considered in `RE-164`--`RE-173`. A weaker PNT statement without a quantitative tail cannot produce (29).

**No hidden finite-support argument is used.** The final negative phase may be infinite and arbitrarily sparse. Equation (25) controls its total `log q/q` mass from the monotone cumulative Chebyshev discrepancy, so the conclusion does not require a largest modified prime and does not fall back to `RE-172`.

**The initial excursion remains available.** If the first positive phase begins at `16p`, the order-one excursion of the `RE-173` deletion packet measured at `8p` is untouched. The theorem constrains only how the later two-jet compensation can be arranged.

**The placement bound is necessary, not sufficient.** Equation (31) says that moving the final negative phase beyond the first-slope capacity horizon is impossible. It does not construct an integer prime-supported control inside the horizon, and it does not prove that such a control exists. The finite-dimensional arithmetic realization problem left at the end of `RE-175` therefore remains genuine.

A particularly important surviving route is a control with more than two sign changes. Once signs continue to alternate after `Y`, the terminal monotonicity used in (23)--(25) disappears. Any higher-jet closure will need either an iterated one-sign decomposition, a bounded-variation/transport quantity that survives those cancellations, or genuinely ordinary-prime information that limits how cheaply successive sign phases can be interlaced.

## 5. Representation audit

The proof uses three representations of the same source perturbation.

At the Euler boundary, exact zeroth and first derivatives become two signed moments `(H,B)`. For a three-phase sign pattern, those two moments give the exact barycentric identity (14), which forces the terminal `B`-mass floor (19).

In the Chebyshev representation, a final one-sign prime tail is monotone after its starting point. Stieltjes partial summation converts its `B(q)\sim log q/q` workload into the tail integral (25). The KV decay profile then turns that integral into the capacity (29).

Finally, the `V`-coordinate of `RE-166` exposes the conditioning difference between the Robin kernel and the first Euler slope: their remote capacities differ by a factor `log Y`, producing the explicit shift (39).

The **generic** ingredients are two-moment barycentric algebra and partial summation of a monotone signed tail. The **source-specific** content is their conjunction with ordinary-prime Euler kernels, the `RE-173` Robin-scale Mertens debt, and the KV Chebyshev envelope already used by this line. No broader moment theorem or new external estimate is load-bearing.

## 6. Prior-art boundary

The sign-change/moment background is classical Chebyshev-system theory, already audited in `RE-175`. Partial summation of prime weights and endpoint Laplace estimates for a Korobov--Vinogradov profile are likewise standard analytic-number-theory tools. A fresh search found neighboring literature on Mertens products, truncated moment problems, and current KV PNT estimates, but no source for the specific implication proved here: exact Mertens-plus-first-slope matching of a prime-supported `- + -` control forces a Robin-scale terminal `log q/q` debt, which a matched KV Chebyshev envelope can carry only up to the moving horizon (31).

The only external arithmetic input represented in the hypothesis is the same KV PNT envelope already anchored in `SOURCES.md` through Bellotti. Equation (28) is derived directly from the explicit profile `V`, so this finding adds no new load-bearing literature dependency and does not modify `SOURCES.md`.

## 7. Durable consequence

`RE-175` left the first nontrivial redesign of `RE-173` as a two-sign-change control matching both the Mertens value and the first Euler slope. `RE-176` now shows that the obvious noncompact version of that redesign has a hard placement cost:

\[
\boxed{
\text{minimal two-jet escape}
\quad\Longrightarrow\quad
\text{terminal one-sign debt}
\quad\Longrightarrow\quad
\mathfrak J_b(p,Y)\gg1.
}
\tag{40}
\]

The extra sign change cannot simply be moved to an arbitrarily remote, arbitrarily cheap tail while KV fidelity is retained. At the same time the allowed first-slope horizon lies farther out than the Robin remote-capacity center by the explicit shift (39), so one boundary derivative still falls short of source rigidity.

The live question is correspondingly narrower: can an actual ordinary-prime integer control realize the required `- + -` two-jet compensation **inside** this horizon while preserving the transient order-one Robin excursion, or must it use further alternations whose own tail capacities can be iterated and eventually exhausted?