# RE-164 — Quantitative PNT fidelity collapses terminal generalized-source ambiguity

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-PNT-FIDELITY + MATCHED-SOURCE-RIGIDITY + TERMINAL-GENERALIZED-SOURCE-BOUNDARY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-015, RE-153, RE-155, RE-157, RE-162, RE-163.

`RE-155`--`RE-163` show that terminal modifications of a prime-like source can move the normalized Robin source coordinate by order one while remaining invisible to **coarse** PNT information such as `vartheta_Q(x)=x+o(x)`. Those controls were intentionally information-theoretic: they identify what coarse density, finite moment matching, and even sharp Chebyshev-moment matching fail to determine.

They do **not** survive the quantitative PNT remainder already used to define the upper Robin horizon. If two sources agree below a cutoff `T` and both satisfy a Korobov--Vinogradov-scale Chebyshev remainder above `T`, then their contribution to the `RE-153` source coordinate beyond `T` differs by at most the same integrable PNT tail that appears in `RE-015`. At the canonical horizon `U_A(p)`, this is `o(1)`. In particular, every order-one terminal control from `RE-155`--`RE-163` must violate quantitative PNT fidelity somewhere inside its modified shell, regardless of how many terminal moments it matches.

Retain

\[
U:=U_A(p),\qquad
J_p=[p+p^\alpha,U],\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\]

and the normalized source coordinate from `RE-153`,

\[
\mathcal A_p(Q)
:=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t),
\qquad
\nu_p(dt)=\frac{\sqrt p\log p\,\sqrt t\,(-h'(t))}{Z_p}\,dt,
\qquad
Z_p=2+o(1).
\tag{1}
\]

Let `Q_1,Q_2` be two prime-like sources whose Chebyshev functions agree below `T`, where

\[
p+p^\alpha\le T<U.
\tag{2}
\]

Then the exact matched-source identity is

\[
\boxed{
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\int_T^U
\bigl(\vartheta_{Q_2}(t)-\vartheta_{Q_1}(t)\bigr)(-h'(t))\,dt.
}
\tag{3}
\]

Define the relative source discrepancy

\[
M_{12}(T,U)
:=
\sup_{T\le t\le U}
\frac{|\vartheta_{Q_1}(t)-\vartheta_{Q_2}(t)|}{t}.
\tag{4}
\]

Since

\[
-h'(t)
=
\frac1{t(t-1)\log t}
+
\frac{-\log(1-t^{-1})}{t(\log t)^2},
\tag{5}
\]

we have, uniformly for large `T`,

\[
\int_T^U t(-h'(t))\,dt
\le
(1+o(1))
\log\frac{\log U}{\log T}.
\tag{6}
\]

Consequently

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\sqrt p\log p\,M_{12}(T,U)
\log\frac{\log U}{\log T}.
}
\tag{7}
\]

For a terminal logarithmic shell

\[
T=Ue^{-L},\qquad 0<L=o(\log U),
\tag{8}
\]

put, as in `RE-160`--`RE-163`,

\[
\eta_p:=\frac{\log U}{\sqrt p\log p}.
\tag{9}
\]

Then (7) becomes

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\frac{L}{\eta_p}\,M_{12}(Ue^{-L},U).
}
\tag{10}
\]

Thus any fixed separation `|mathcal A_p(Q_1)-mathcal A_p(Q_2)|>=Delta>0` in such a shell forces

\[
\boxed{
M_{12}(Ue^{-L},U)
\gg_\Delta
\frac{\eta_p}{L}.
}
\tag{11}
\]

This necessary excursion is independent of cardinality, moment order, or Chebyshev-mode cancellation. Those refinements can hide the perturbation from selected terminal statistics, but they cannot hide the cumulative Chebyshev source discrepancy from the positive Robin kernel itself.

## 1. Quantitative PNT fidelity gives a stronger matched-source bound

Put

\[
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
\tag{12}
\]

Suppose that, on `[T,U]`, each source satisfies a quantitative PNT envelope

\[
|\vartheta_{Q_i}(t)-t|
\le C_i t e^{-b_iV(t)},
\qquad i=1,2,
\tag{13}
\]

for fixed positive `b_i,C_i`. This is an explicit **fidelity hypothesis** on a generalized control; no theorem is being asserted that an arbitrary Beurling source must satisfy it. With

\[
b:=\min(b_1,b_2),
\tag{14}
\]

we obtain

\[
|\vartheta_{Q_1}(t)-\vartheta_{Q_2}(t)|
\ll t e^{-bV(t)}.
\tag{15}
\]

Equations (3), (5), and the same change of variables used in `RE-015` therefore give

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\sqrt p\log p
\int_T^U
\frac{e^{-bV(t)}}{t\log t}\,dt.
}
\tag{16}
\]

There are two useful forms of (16). Monotonicity of `V` yields the local-shell bound

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\sqrt p\log p\,e^{-bV(T)}
\log\frac{\log U}{\log T},
}
\tag{17}
\]

while extending the positive majorant to infinity and applying the `RE-015` tail calculation yields

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\sqrt p\log p\,
\frac{e^{-bV(T)}}{V(T)}.
}
\tag{18}
\]

The first is sharper when `T` is a fixed multiplicative fraction of `U`; the second is the robust remote-tail form.

## 2. The canonical PNT horizon makes the terminal source rigid

For

\[
U_A(p)
=
\exp\!\left(
A(\log p)^{5/3}(\log\log p)^{1/3}
\right),
\tag{19}
\]

`RE-015` gives

\[
V(U_A(p))
=
\kappa_A\log p\,(1+o(1)),
\qquad
\kappa_A:=A^{3/5}\left(\frac35\right)^{1/5}.
\tag{20}
\]

Take a bounded terminal logarithmic width `0<L<=L_0` and `T=U_A(p)e^{-L}`. Then

\[
V(T)=\kappa_A\log p\,(1+o(1)),
\tag{21}
\]

and `RE-157` records

\[
\eta_p
=A p^{-1/2}(\log p)^{2/3}(\log\log p)^{1/3}.
\tag{22}
\]

Substituting (21)--(22) into (17),

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll_{L_0}
 p^{1/2-b\kappa_A+o(1)}
 (\log p)^{-2/3}(\log\log p)^{-1/3}.
}
\tag{23}
\]

Hence

\[
\boxed{
b\kappa_A\ge\frac12
\quad\Longrightarrow\quad
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)=o(1)
}
\tag{24}
\]

for every bounded terminal shell. The strict inequality `b kappa_A>1/2` used in the `RE-015` remote-tail truncation is more than enough.

More generally, let

\[
T=U_B(p)
=
\exp\!\left(
B(\log p)^{5/3}(\log\log p)^{1/3}
\right)
\tag{25}
\]

with `B<A`. Then (18) gives

\[
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
p^{1/2-b\kappa_B+o(1)}.
\tag{26}
\]

Thus, whenever `b kappa_B>1/2`, **all** source freedom above `U_B(p)` becomes `o(1)` in the Robin coordinate among sources that retain the quantitative PNT envelope and agree below `U_B(p)`. This is a matched-source version of the tail rigidity that `RE-015` proved for the ordinary source itself.

## 3. Consequence for RE-155--RE-163

The terminal controls in `RE-155`--`RE-163` preserve only coarse PNT information. They satisfy bounds such as

\[
\vartheta_Q(x)-\vartheta(x)=o(U)
\tag{27}
\]

while producing a nonvanishing change in `mathcal A_p`. Equation (11) now locates the missing information: an order-one terminal change necessarily creates, at some intermediate point of a shell of logarithmic width `L`, a relative Chebyshev discrepancy of size at least

\[
\asymp \frac{\eta_p}{L}.
\tag{28}
\]

At the `RE-015` horizon, the ordinary Korobov--Vinogradov remainder is smaller than this scale once its exponent clears the same `1/2` inversion threshold. Therefore a pair of order-one separated controls cannot both remain in that quantitative PNT fidelity class.

This conclusion is unaffected by the sharp hierarchy developed in `RE-159`--`RE-163`. Exact matching of many raw moments, exact matching of low Chebyshev modes, or cancellation in the kernel-weighted low-mode sum can reduce which statistics reveal the perturbation, but if the final Robin source displacement stays of order one, the positive integral (3) still forces the cumulative excursion (11). The generalized-source constructions remain valid as **coarse-information obstructions**; they are not source-faithful controls for the full unconditional PNT remainder at the canonical upper horizon.

The practical boundary is therefore sharper than “more terminal moments may be needed.” Beyond the quantitative PNT inversion scale, additional moment information is unnecessary: the known PNT envelope itself makes the terminal source rigid at Robin normalization. Any surviving ordinary-prime/CA obstruction must live lower in the annulus, exploit information not reduced to a terminal source replacement, or use a selector-height coupling not captured by these matched generalized sources.

## 4. Prior-art boundary and scope

The load-bearing external input is exactly the quantitative PNT remainder already anchored in `SOURCES.md` and used by `RE-015`; the current Bellotti treatment supplies a Korobov--Vinogradov-scale remainder for the ordinary prime source. The general literature on Beurling prime systems also studies PNTs with quantitative remainder and zero-density consequences, but the present statement does not derive (13) for arbitrary generalized sources. It assumes a source belongs to that fidelity class and propagates the envelope through the exact Robin kernel.

A targeted literature audit did not locate the line-specific matched-source conclusion (7), the terminal fidelity threshold (11), or the consequence (24) for the `RE-155`--`RE-163` terminal controls. No new external theorem is needed beyond the PNT anchor already recorded, so `SOURCES.md` requires no change.

This finding does **not** prove Robin's inequality, control the middle annulus below the PNT inversion scale, or establish the accepted CA selector-height coupling clue. It also does not invalidate the generalized-source constructions: their claims were explicitly about coarse PNT indistinguishability. The new point is a fidelity boundary. Once the comparison class is required to preserve the quantitative unconditional PNT remainder at the upper horizon, order-one terminal ambiguity disappears before any moment hierarchy is invoked.