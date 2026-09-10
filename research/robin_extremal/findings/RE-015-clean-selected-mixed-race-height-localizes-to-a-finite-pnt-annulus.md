# RE-015 — clean selected mixed-race height localizes to a finite PNT annulus

**Status:** `LITERATURE+DERIVED + UNCONDITIONAL-ASYMPTOTIC + PNT-TAIL-TRUNCATION + FINITE-ANNULUS-LOCALIZATION + CLEAN-COUNTEREXAMPLE-NECESSARY-CONDITION + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-014` shows that, at a clean regular self-tangent CA local peak, deleting the direct mixed-tail contribution of every fixed initial window `[p,p+p^\alpha]` with `alpha<3/4` does not change the Robin height at first square-root order. That leaves open whether the relevant excursion might live arbitrarily far out in the future tail.

The ordinary unconditional prime number theorem with Korobov--Vinogradov remainder closes that escape. Keep the notation of `RE-014`:
\[
\Delta(t):=\vartheta(t)-t,\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},\qquad
k(t):=\frac1{t\log t},
\]
\[
I(t):=\Delta(t)h'(t)-\bigl(h(t)-k(t)\bigr),\qquad
\mathcal M_*(x):=\int_x^\infty I(t)\,dt.
\tag{1}
\]
For large `t`, put
\[
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
\tag{2}
\]

There are absolute constants `a,C>0` such that
\[
|\Delta(t)|\le C\,t\,e^{-aV(t)}
\tag{3}
\]
for all sufficiently large `t`. Consequently,
\[
\boxed{
\left|\mathcal M_*(U)\right|
\ll
\frac{e^{-aV(U)}}{V(U)}
+\frac1{U\log U}.
}
\tag{4}
\]

Now define, for fixed `A>0`,
\[
U_A(p):=
\exp\!\left(
A(\log p)^{5/3}(\log\log p)^{1/3}
\right).
\tag{5}
\]
There exists an absolute `A_0>0` such that for every fixed `A>A_0`,
\[
\boxed{
\sqrt p\log p\;\mathcal M_*(U_A(p))=o(1).
}
\tag{6}
\]

Combining (6) with `RE-014` yields the two-sided scale localization. For every fixed `0<alpha<3/4` and every fixed `A>A_0`, along any unbounded sequence of sufficiently large clean regular self-tangent CA local peaks with left boundary prime `p`,
\[
\boxed{
\sqrt p\log p\,
\bigl(\log G(C)-\gamma\bigr)
=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)} I(t)\,dt
-2\sqrt2+o(1).
}
\tag{7}
\]
Hence every unbounded clean Robin-counterexample sequence necessarily satisfies
\[
\boxed{
\liminf
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)} I(t)\,dt
\ge 2\sqrt2.
}
\tag{8}
\]

Thus the first-order clean counterexample excursion is neither a local prime-gap effect nor an arbitrarily remote tail phenomenon. With current unconditional PNT technology it must be carried, in the direct integral representation, by a finite but very broad intermediate annulus from beyond every fixed `p^alpha`, `alpha<3/4`, up to
\[
p^{\,A(\log p)^{2/3}(\log\log p)^{1/3}}.
\]
This is a localization theorem, not an exclusion theorem.

## 1. The unconditional PNT remainder transfers from `psi` to `theta`

A current sharp treatment of the classical Korobov--Vinogradov zero-free-region method gives a prime-number-theorem remainder of the form
\[
\psi(t)-t\ll t\,e^{-a_1V(t)}
\tag{9}
\]
for some absolute `a_1>0`; only existence of a positive constant at this scale is needed here.

The difference between `psi` and `vartheta` comes from prime powers:
\[
\psi(t)-\vartheta(t)
=
\sum_{m\ge2}\vartheta(t^{1/m})
=O(\sqrt t\log t)
\tag{10}
\]
using only the elementary Chebyshev bound `vartheta(y)=O(y)` and the fact that at most `O(log t)` exponents occur. Since
\[
\sqrt t\log t
=o\!\left(t e^{-aV(t)}\right)
\]
after decreasing `a>0` if necessary, (9)--(10) give (3).

The precise best constant is irrelevant. The later upper horizon is deliberately allowed to absorb whatever positive `a` the unconditional PNT theorem supplies.

## 2. The mixed kernel turns the PNT error into an integrable remote-tail bound

Let
\[
f(t):=-\log(1-t^{-1}).
\]
Then
\[
f'(t)=-\frac1{t(t-1)}
\]
and
\[
h'(t)
=
-\frac1{t(t-1)\log t}
-\frac{f(t)}{t(\log t)^2}.
\tag{11}
\]
Also, from the positive logarithm series,
\[
0<f(t)-\frac1t
=\sum_{m\ge2}\frac1{m t^m}
\le\frac1{t(t-1)}.
\tag{12}
\]
Equations (11)--(12) imply, for large `t`,
\[
|h'(t)|\ll\frac1{t^2\log t},
\qquad
0<h(t)-k(t)\ll\frac1{t^2\log t}.
\tag{13}
\]
Together with (3),
\[
|I(t)|
\ll
\frac{e^{-aV(t)}}{t\log t}
+\frac1{t^2\log t}.
\tag{14}
\]

It remains to integrate the first term without losing its stretched-logarithmic decay. Put `y=log t` and
\[
\phi(y):=\frac{y^{3/5}}{(\log y)^{1/5}},
\qquad V(t)=\phi(\log t).
\]
For sufficiently large `y`,
\[
\frac{y\phi'(y)}{\phi(y)}
=
\frac35-\frac1{5\log y}
\ge\frac12.
\tag{15}
\]
Thus, with `u=phi(y)`,
\[
\begin{aligned}
\int_U^\infty
\frac{e^{-aV(t)}}{t\log t}\,dt
&=
\int_{\log U}^\infty
\frac{e^{-a\phi(y)}}y\,dy\\
&\ll
\int_{V(U)}^\infty \frac{e^{-au}}u\,du
\ll
\frac{e^{-aV(U)}}{V(U)}.
\end{aligned}
\tag{16}
\]
The second term in (14) contributes `O((U log U)^{-1})`. This proves (4).

Notice that (4) is an ordinary unconditional PNT consequence; no CA selection has entered yet. Its role is to quantify how much of the `RE-008` improper tail can remain after a large finite cutoff.

## 3. Inverting the PNT scale gives a finite upper horizon at Robin normalization

For `U_A(p)` from (5),
\[
\log U_A(p)
=
A(\log p)^{5/3}(\log\log p)^{1/3},
\]
while
\[
\log\log U_A(p)
=
\frac53\log\log p+o(\log\log p).
\]
Therefore
\[
\boxed{
V(U_A(p))
=
\kappa_A\log p\,(1+o(1)),
\qquad
\kappa_A:=A^{3/5}\left(\frac35\right)^{1/5}.
}
\tag{17}
\]

Choose `A_0` so that
\[
a\kappa_A>\frac12
\qquad(A>A_0).
\tag{18}
\]
Then (4) and (17) give
\[
\begin{aligned}
\sqrt p\log p\,|\mathcal M_*(U_A(p))|
&\ll
\sqrt p\log p\,
\frac{e^{-aV(U_A(p))}}{V(U_A(p))}
+
\frac{\sqrt p\log p}{U_A(p)\log U_A(p)}\\
&=
p^{1/2-a\kappa_A+o(1)}+o(1)
=o(1),
\end{aligned}
\tag{19}
\]
which proves (6).

More generally, any cutoff `U=U(p)` satisfying
\[
V(U(p))\ge
\left(\frac1{2a}+\delta\right)\log p
\tag{20}
\]
for some fixed `delta>0` has the same property. The explicit family (5) is the natural inversion of the current unconditional PNT scale. A coarser constant-free choice such as `U(p)=exp((log p)^2)` also works for every positive `a`.

The normalization in (19) is deliberately **pinned to the selected boundary prime `p`**. It does not say that `sqrt(U_A) log(U_A) M_*(U_A)` is bounded; such a global normalized statement would collide with the RH-equivalence obstruction in `RE-009`.

## 4. The clean Robin excursion is trapped between the lower and upper cutoffs

`RE-014` proves that for every fixed `alpha<3/4`,
\[
\sqrt p\log p
\int_p^{p+p^\alpha}I(t)\,dt=o(1)
\tag{21}
\]
along the clean selected peak sequence. Since
\[
\mathcal M_*(p)
=
\int_p^{p+p^\alpha}I(t)\,dt
+
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
+
\mathcal M_*(U_A(p)),
\tag{22}
\]
equations (6) and (21) imply
\[
\sqrt p\log p\,\mathcal M_*(p)
=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
+o(1).
\tag{23}
\]

The clean height formula already established in `RE-014` is
\[
\sqrt p\log p\,
\bigl(\log G(C)-\gamma\bigr)
=
\sqrt p\log p\,\mathcal M_*(p)-2\sqrt2+o(1).
\tag{24}
\]
Substituting (23) gives (7). If `C` is a Robin counterexample, the left side of (24) is positive; taking the lower limit yields (8).

This is genuinely stronger than either truncation separately. `RE-014` says the direct contribution from a polynomial initial future window is invisible at Robin scale. Equation (6) says that the direct contribution after the PNT-inverted upper horizon is also invisible at the same normalization. Whatever first-order signed mass a clean counterexample needs must therefore accumulate between those two scales.

## 5. Prior art and novelty boundary

The PNT input is classical in shape. Bellotti's 2026 Bulletin of the London Mathematical Society paper gives a current sharp zero-density route to the optimal PNT error associated with a Korobov--Vinogradov zero-free region. No novelty is claimed for (3), for the kernel estimates (11)--(16), or for the fact that sufficiently remote smooth weighted tails can be truncated using a PNT remainder.

Likewise, `RE-009` already identifies `sqrt(x) log(x) M_*(x)` with the mixed standard/reciprocal prime-race coordinate studied by Bhattacharya--Martin--Simpson, up to `o(1)`. Their global one-sided boundedness theorem remains an essential obstruction: proving a uniform global bound for that normalized race would already be RH-equivalent.

A targeted search across current weighted-prime-error correlation work, Mertens-product error literature, PNT-remainder literature, and recent Robin/CA work did not locate the specific **CA-selected two-sided scale splice** (7)--(8). No blanket novelty claim is made. The Mathia-specific delta is elementary but useful: the lower cutoff comes from the exact clean CA selector, while the upper cutoff comes from an unconditional global PNT remainder, and together they turn the improper future-tail obligation into a finite annular one without assuming an RH-strength mixed-race bound.

## 6. Boundaries, falsification, and research consequence

All selection quantifiers from `RE-014` remain load-bearing. The lower cutoff requires an unbounded sequence of sufficiently large clean regular self-tangent CA local peaks and a fixed `alpha<3/4`. The upper cutoff uses a fixed `A>A_0`; neither `A_0` nor the displayed scale is claimed optimal. A stronger unconditional PNT remainder would move the upper frontier inward, while the present theorem alone gives no cancellation inside the annulus.

The upper horizon is enormous compared with `p`: it is super-polynomial but subexponential in `p`. Therefore "finite annulus" must not be read as a local-statistics theorem. Nor does deleting the direct integrals outside the annulus erase their causal influence. Prime jumps before the lower cutoff alter the state `Delta(t)` seen later, just as `RE-014` already warns; (7) localizes the **integral contribution**, not the provenance of the state carried through it.

Nothing here applies to the higher-layer/tied exceptional chamber of `RE-004`, and nothing bounds the annular integral by less than `2sqrt(2)`. The result therefore does not prove Robin's inequality or RH. It closes a narrower escape: a clean counterexample cannot obtain its first-order height solely from arbitrarily remote tail mass beyond the unconditional PNT inversion scale.

The clean branch is now a finite-scale correlation problem. Any positive continuation must exploit how the full logarithmic-depth CA selector constrains the signed mixed-race mass across the broad annulus
\[
[p+p^\alpha,\ U_A(p)],
\]
or prove that hypothetical counterexamples are forced into the exceptional transition chamber. Extending the tail farther without using the selector cannot create a new first-order channel.
