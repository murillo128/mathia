# RE-167 — Fixed-width KV shells have a distinct local capacity center

**Status:** `EXACT-DERIVED + LOCAL-SHELL-CAPACITY + GENERALIZED-RELOCATION-SHARPNESS + TWO-SCALE-KV-TRANSITION + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-154, RE-164, RE-165, RE-166.

`RE-164` gives two different quantitative-PNT bounds for matched generalized sources: a local-shell estimate and a remote-tail estimate. `RE-165`--`RE-166` prove that the remote estimate is sharp and locate its moving capacity center. The local estimate has its own, strictly lower, sharp transition.

For a fixed multiplicative-width shell beginning at `T`, the correct capacity is

\[
\boxed{
\mathfrak L_b(p,T)
:=
\sqrt p\log p\,
\frac{e^{-bV(T)}}{\log T},
\qquad
V(T):=\frac{(\log T)^{3/5}}{(\log\log T)^{1/5}}.
}
\tag{1}
\]

If two quantitative-PNT-faithful sources differ only inside `[T,CT]`, with fixed `C>1`, then their normalized Robin source coordinates differ by `O_C(\mathfrak L_b(p,T))`. Conversely, generalized-prime mass can be relocated inside the same fixed-width shell, with the cumulative Chebyshev discrepancy returning exactly to zero at the upper edge, while attaining a fixed multiple of `\mathfrak L_b(p,T)` and remaining in the same Korobov--Vinogradov exponent class.

Thus `\mathfrak L_b` is the sharp local-shell analogue of the remote capacity

\[
\mathfrak K_b(p,T)
=
\sqrt p\log p\,
\frac{e^{-bV(T)}}{V(T)}
\tag{2}
\]

from `RE-165`. Since `V(T)\ll\log T`, the local shell loses capacity before the full remote tail does. Its moving center lies lower by `Theta(log log p)` in the `V` coordinate.

Most importantly for the accepted selector-height problem, every bounded-multiplicative post-selector scale `T=Bp` lies very far inside the ambiguous regime:

\[
\boxed{
\mathfrak L_b(p,Bp)=p^{1/2-o(1)}\longrightarrow\infty.
}
\tag{3}
\]

Consequently the `RE-154` order-one post-selector relocations can be made **uniformly quantitative-PNT faithful**, with an `o(1)` deterioration of the allowed KV envelope constant. The stronger source fidelity introduced in `RE-164` therefore does not repair the bounded-multiplicative selector obstruction; it only becomes coercive at a much larger moving height.

## 1. The local-shell upper capacity

Retain the normalized Robin source coordinate from `RE-153`, with upper horizon `U=U_A(p)`,

\[
\mathcal A_p(Q)
=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t),
\qquad
\nu_p(dt)
=
\frac{\sqrt p\log p\,\sqrt t\,(-h'(t))}{Z_p}\,dt,
\qquad
Z_p=2+o(1),
\tag{4}
\]

where

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t}.
\tag{5}
\]

Fix `C>1`. Let `Q_1,Q_2` agree below `T` and again above `CT`, so that

\[
\vartheta_{Q_1}(t)-\vartheta_{Q_2}(t)=0
\qquad
(t<T\text{ or }t>CT).
\tag{6}
\]

Assume that on the shell both sources satisfy, for fixed `b>0`,

\[
|\vartheta_{Q_i}(t)-t|
\le C_i t e^{-bV(t)}.
\tag{7}
\]

The exact matched-source identity of `RE-164` reduces to

\[
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)
=
\frac{\sqrt p\log p}{Z_p}
\int_T^{CT}
\bigl(\vartheta_{Q_2}(t)-\vartheta_{Q_1}(t)\bigr)(-h'(t))\,dt.
\tag{8}
\]

For large `t`,

\[
-h'(t)\ll\frac1{t^2\log t},
\tag{9}
\]

while `V` is increasing. Hence

\[
\begin{aligned}
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
&\ll_C
\sqrt p\log p\,e^{-bV(T)}
\int_T^{CT}\frac{dt}{t\log t}\\
&=
O_C\!\left(
\sqrt p\log p\,
\frac{e^{-bV(T)}}{\log T}
\right).
\end{aligned}
\tag{10}
\]

Therefore

\[
\boxed{
\mathfrak L_b(p,T)\to0
\quad\Longrightarrow\quad
\text{fixed-width shell rigidity}.
}
\tag{11}
\]

This is the moving-scale form of the local estimate already implicit in `RE-164`; unlike the remote bound, it charges only the logarithmic width of one proportional shell.

## 2. Mass-balanced relocation attains the same scale

The upper bound is sharp within the same generalized-source fidelity class. Fix constants

\[
1<\rho<\sigma<C.
\tag{12}
\]

Assume

\[
T\ge Bp\quad(B>1\text{ fixed}),
\qquad
CT<U_A(p),
\qquad
\frac{T\log T}{\sqrt p\log p}\to\infty,
\tag{13}
\]

which includes both bounded-multiplicative shells and the KV transition scales below.

Let the ordinary source satisfy

\[
|\vartheta(t)-t|
\le C_0 t e^{-bV(t)}.
\tag{14}
\]

Put

\[
E_b(T):=T e^{-bV(T)}.
\tag{15}
\]

For a parameter `lambda=lambda_p` with `0<lambda<=lambda_0`, delete ordinary primes from `[T,\rho T]` until their total logarithmic Chebyshev mass is

\[
M_p=\lambda E_b(T)+O(\log T).
\tag{16}
\]

The ordinary PNT supplies much more than the required mass because `E_b(T)=o(T)`. Next insert distinct generalized real labels in `[\sigma T,CT]` whose logarithms sum **exactly** to the deleted mass. Such a packet exists for large `p`: `M_p/\log T\to\infty` in the regimes used below, while the allowed interval of logarithmic label weights has fixed positive width. One may choose an integer number of labels whose mean logarithmic weight lies inside that interval and perturb the labels slightly while preserving the total sum.

Call the resulting source `Q_p`. Its Chebyshev discrepancy relative to the ordinary source satisfies

\[
0\le
\vartheta(t)-\vartheta_{Q_p}(t)
\le M_p
\qquad(T\le t\le CT),
\tag{17}
\]

and, because the inserted and deleted logarithmic masses match exactly,

\[
\boxed{
\vartheta_{Q_p}(t)=\vartheta(t)
\qquad(t<T\text{ or }t>CT).
}
\tag{18}
\]

The envelope itself is eventually increasing, as already used in `RE-165`:

\[
E_b(t)=t e^{-bV(t)},
\qquad
\frac{d}{d\log t}\log E_b(t)=1-o(1)>0.
\tag{19}
\]

Equations (16)--(19) therefore give uniformly on the shell

\[
|\vartheta_{Q_p}(t)-t|
\le
(C_0+\lambda+o(1))\,t e^{-bV(t)}.
\tag{20}
\]

Thus the relocation preserves the same KV exponent `b`; if `lambda_p->0`, even the deterioration of the envelope constant tends to zero.

During the entire middle interval `[\rho T,\sigma T]`, all deletions have occurred and no compensating insertion has yet occurred, so

\[
\vartheta(t)-\vartheta_{Q_p}(t)=M_p.
\tag{21}
\]

The exact kernel identity then gives the positive lower bound

\[
\mathcal A_p(Q_p)-\mathcal A_p(P)
\ge
\frac{\sqrt p\log p}{Z_p}
M_p\bigl(h(\rho T)-h(\sigma T)\bigr).
\tag{22}
\]

Since, uniformly for fixed `a>0`,

\[
h(aT)
=
\frac{1+o(1)}{aT\log T},
\tag{23}
\]

we obtain

\[
\boxed{
\mathcal A_p(Q_p)-\mathcal A_p(P)
\ge
\left[
\frac{\lambda}{2}
\left(\frac1\rho-\frac1\sigma\right)
+o(\lambda)
\right]
\mathfrak L_b(p,T).
}
\tag{24}
\]

Together with (10), this proves sharpness up to constants depending only on the fixed shell geometry.

If `\mathfrak L_b(p,T)` has a positive finite lower limit, a fixed small `lambda` yields a nonvanishing Robin displacement while preserving the quantitative PNT class. If

\[
\mathfrak L_b(p,T)\to\infty,
\tag{25}
\]

choose `lambda_p` proportional to `1/\mathfrak L_b(p,T)`. Then `lambda_p->0`, the source becomes asymptotically indistinguishable even at the level of the KV envelope constant, yet (24) retains any prescribed fixed positive displacement. Under (13), the relocated logarithmic mass still tends to infinity, so the discretization remains available.

## 3. Bounded-multiplicative selectors remain ambiguous under full KV fidelity

Take

\[
T=Bp
\tag{26}
\]

with fixed `B>1`. Write

\[
L:=\log p,
\qquad
R:=\log L.
\tag{27}
\]

Then

\[
V(Bp)
=
L^{3/5}R^{-1/5}(1+o(1)),
\qquad
\log(Bp)=L+O(1),
\tag{28}
\]

and therefore

\[
\boxed{
\log\mathfrak L_b(p,Bp)
=
\frac12L
-bL^{3/5}R^{-1/5}(1+o(1))
+O(1)
\longrightarrow+\infty.
}
\tag{29}
\]

In particular,

\[
\mathfrak L_b(p,Bp)=p^{1/2-o(1)}.
\tag{30}
\]

This retroactively strengthens the matched control of `RE-154`. Its `Theta(\sqrt p/\log p)` bounded-multiplicative relocations cost only `O(\sqrt p)` in cumulative Chebyshev mass. At scale `Bp`, the allowed KV remainder is

\[
Bp\,e^{-bV(Bp)}
=p^{1-o(1)},
\tag{31}
\]

so the relocation occupies a vanishing fraction of the full unconditional PNT envelope. More precisely,

\[
\sup_{t\ge Bp}
\frac{|\vartheta_{Q_p}(t)-\vartheta(t)|}
{t e^{-bV(t)}}
\ll
p^{-1/2}e^{bV(Bp)}
=
o(1)
\tag{32}
\]

for the fixed-shell controls, with equality restored after the upper shell edge in the mass-balanced version.

Hence knowing the ordinary source exactly through any fixed multiple `Bp`, and imposing the same quantitative Korobov--Vinogradov PNT exponent on every later point, still does not determine the normalized Robin source coordinate to `o(1)`. The missing information is stronger than quantitative PNT fidelity at ordinary multiplicative distance: it must couple the actual CA selector to signed square-root-scale source structure across growing multiplicative radii.

## 4. The local capacity center is below the remote-tail center

The local transition is defined by

\[
\mathfrak L_b(p,T_{\mathrm{loc}})=1.
\tag{33}
\]

Put

\[
y_{\mathrm{loc}}:=\log T_{\mathrm{loc}},
\qquad
v_{\mathrm{loc}}:=V(T_{\mathrm{loc}}).
\tag{34}
\]

Equation (33) is exactly

\[
\boxed{
bv_{\mathrm{loc}}+\log y_{\mathrm{loc}}
=\frac12L+R.
}
\tag{35}
\]

The leading inversion is the same as in `RE-166`. With

\[
B_0
:=
\left(\frac53\right)^{1/3}(2b)^{-5/3},
\qquad
S:=\log R,
\tag{36}
\]

we have

\[
y_{\mathrm{loc}}
=B_0L^{5/3}R^{1/3}(1+o(1)),
\tag{37}
\]

so

\[
\log y_{\mathrm{loc}}
=
\frac53R+rac13S+\log B_0+o(1).
\tag{38}
\]

Substituting (38) into (35),

\[
\boxed{
v_{\mathrm{loc}}
=
\frac{L}{2b}
-
\frac{2R}{3b}
-
\frac{S}{3b}
-
\frac{\log B_0}{b}
+o(1).
}
\tag{39}
\]

By contrast, `RE-166` locates the remote-tail capacity-one center at

\[
v_*(p)
=
\frac{L}{2b}
+
\frac{\log(2b)}b
+o(1).
\tag{40}
\]

Therefore

\[
\boxed{
v_*(p)-v_{\mathrm{loc}}(p)
=
\frac{2}{3b}\log\log p
+
\frac{1}{3b}\log\log\log p
+
\frac1b\log(2bB_0)
+o(1).
}
\tag{41}
\]

The distinction is structural. A perturbation confined to one fixed multiplicative shell loses order-one Robin leverage at `T_loc`; a source allowed to spend its quantitative-PNT budget across the whole remote tail retains order-one capacity until the higher center `T_*` of `RE-166`.

Each local fixed-capacity contour still has only additive `O(1)` width in `V`. Indeed, if `V(T)=v_{\mathrm{loc}}+\Delta` with bounded `Delta`, then `\log T/\log T_{\mathrm{loc}}=1+o(1)` and

\[
\mathfrak L_b(p,T)
=e^{-b\Delta}(1+o(1)).
\tag{42}
\]

Thus the `Theta(log log p)` separation in (41) is much wider than either individual boundary layer.

## 5. Research consequence

The quantitative-PNT branch now has two distinct information scales. `RE-165`--`RE-166` identify the capacity of a **remote tail**, where discrepancy may be distributed over many logarithmic scales. The present finding identifies the smaller capacity of a **single proportional shell** and shows that the corresponding upper bound is attained by an exact mass-balanced generalized-prime relocation.

This matters directly for `CLUE-clean-peak-selector-height-coupling`. Strengthening a bounded-multiplicative selector argument by appending the unconditional KV PNT remainder is still insufficient: at `T=Bp`, the allowed source envelope exceeds the square-root Chebyshev mass needed to move the Robin coordinate by order one by a factor `p^{1/2-o(1)}`. The control can even preserve the KV envelope constant up to `o(1)`.

The clue therefore remains open, but its missing resource is sharper. A successful ordinary-prime/CA theorem must either propagate selector information toward the moving local center `T_loc(p)`, control signed source errors far below the full PNT envelope, or use an exact ordinary-prime/global-CA correlation that generalized mass relocation cannot preserve. Merely invoking quantitative PNT fidelity at fixed multiplicative distance does not change the information boundary.

## 6. Prior-art boundary

The load-bearing external input remains the quantitative ordinary-prime PNT remainder already anchored in `SOURCES.md` through Bellotti; no improved constant is needed. Classical Beurling-prime literature studies PNT remainder classes and their stability, and finite source modifications preserving asymptotic prime laws are not novel. A fresh search over Beurling PNT remainders, generalized-prime perturbations, Mertens products, and Robin criteria did not locate the shell-capacity parameter (1), the mass-balanced sharpness statement (24), or the separation (41) between local and remote Robin-capacity centers.

The new content is the line-specific propagation of the quantitative PNT envelope through the exact `RE-153` Robin kernel and the matching relocation control. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

## Bottom line

For source changes confined to one fixed multiplicative shell,

\[
\boxed{
\mathfrak L_b(p,T)
=
\sqrt p\log p\,
\frac{e^{-bV(T)}}{\log T}
}
\]

is the sharp quantitative-PNT capacity up to shell-dependent constants. It becomes rigid `Theta(log log p)` earlier in the `V` coordinate than the full remote tail of `RE-165`--`RE-166`. Nevertheless every bounded-multiplicative post-selector scale `T=Bp` has `\mathfrak L_b=p^{1/2-o(1)}`, so the `RE-154` order-one relocation obstruction survives the full Korobov--Vinogradov PNT fidelity class with asymptotically vanishing envelope cost.