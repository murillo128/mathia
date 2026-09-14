# PF-341 — thin-pant self-DtN contrast has a common positive sign

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + COMMON-SIGN + TRANSLATION-ROUTE-OBSTRUCTION`.

PF-340 leaves one precise cancellation gate in the PF-336 translation route. On cuff module `n`, the raw symmetric half-cuff contrast is

\[
\Delta_n^{\mathrm{sym}}=\frac12(\Delta_n^-+\Delta_n^+),
\]

where `\Delta_n^-` and `\Delta_n^+` are the self-DtN energy contrasts contributed by the two adjacent one-cusp pant cores. A large right-pant term alone is insufficient because the left term could in principle cancel it.

That cancellation does **not** occur in the prime-flute tail. The PF-216 growing-corridor geometry gives a one-pant estimate that is strong enough for the explicit PF-339 pair. On any tail one-cusp pant, viewed from one finite boundary of period `L` and finite-finite core separation `s`, let `A` be the positive `\Delta+1` self-DtN block with zero datum on the other finite boundary, center `t=0` at the finite-finite common-perpendicular foot, and put

\[
c_m(t)=\sqrt{\frac2L}\cos\frac{2\pi mt}{L},\qquad
f_+=\frac{c_2+c_1}{\sqrt2},\qquad
f_-=\frac{c_2-c_1}{\sqrt2}.
\]

Then, once `sL\to0`,

\[
\boxed{
\langle f_+,Af_+\rangle
\ge \frac{c}{sL},
\qquad
\langle f_-,Af_-\rangle
\le C\left(1+\frac1{sL^5}\right),
}
\]

and hence

\[
\boxed{
\langle f_+,Af_+\rangle-
\langle f_-,Af_-\rangle
\ge \frac{c'}{sL}>0
}
\]

for the whole tail. The mechanism is simple but quantitative: `f_+` is nonzero at the collapsing finite-finite corridor, while `f_-` has a quadratic zero there. The corridor therefore charges `f_+` at the full `1/(sL)` conductance scale, whereas the only potentially singular part of an explicit `f_-` trial costs `O(1/(sL^5))`; the rest of the one-cusp pant has a uniformly noncollapsing/cusp-side extension cost.

Applied to the two pant cores adjacent to module `n`, this gives

\[
\boxed{
\Delta_n^+
\ge \frac{c}{s_nL_n},
\qquad
\Delta_n^-
\ge \frac{c}{s_{n-1}L_n}
}
\]

after a finite head. In particular the two terms have the **same positive sign**, so PF-340's cancellation gate closes. Since PF-216 gives `s_j=O(P_j^{-0.475})`, `L_n=O(\log P_n)`, while PF-205 gives `w_n\asymp P_n^{-1}`, neighboring prime labels are comparable and

\[
\boxed{
\frac{\Delta_n^{\mathrm{sym}}}{w_n}
\gtrsim
\frac{P_n^{1.475}}{\log P_n}
\longrightarrow\infty.
}
\]

Therefore PF-339's necessary condition `\Delta_n^{\mathrm{sym}}=o(w_n)` is false, in fact on the whole tail rather than only on the PF-324 subsequence. Consequently the **PF-336 normalized-insertion translation gate cannot hold**. This kills that translation-transport route; it does not by itself give a lower bound for the completed polar angle and does not rule out the independent PF-318/PF-320 direct Hilbert--Schmidt upper-bound route.

## Claim

Consider one PF-205 one-cusp pant core `E` between two long finite cuffs after the simultaneous natural-width seam cut. Fix one finite artificial boundary as the target boundary, let its Fermi tangential period be `L`, and let

\[
s=\operatorname{dist}(C,C')
\]

be the original finite-finite cuff distance. Let `A` be the target self-DtN block for the positive shifted energy

\[
\mathcal E_E(u)=\int_E(|\nabla u|^2+|u|^2)\,d\mu,
\]

with zero Dirichlet datum on the other finite artificial boundary. Use the zero-twist Fermi coordinate `t` on the target boundary with `t=0` at the finite-finite common-perpendicular foot.

For the two normalized cosine modes and their half-cuff exchanged combinations

\[
c_m(t)=\sqrt{\frac2L}\cos\frac{2\pi mt}{L},
\]

\[
f_+(t)=\frac1{\sqrt L}\left(
\cos\frac{4\pi t}{L}+
\cos\frac{2\pi t}{L}
\right),
\]

\[
f_-(t)=\frac1{\sqrt L}\left(
\cos\frac{4\pi t}{L}-
\cos\frac{2\pi t}{L}
\right),
\tag{1}
\]

there are absolute tail constants `c,C>0` such that

\[
\boxed{
\mathcal E_A(f_+):=\langle f_+,Af_+\rangle
\ge \frac{c}{sL},
}
\tag{2}
\]

\[
\boxed{
\mathcal E_A(f_-)
\le C\left(1+\frac1{sL^5}\right).
}
\tag{3}
\]

Whenever `sL\to0`, equations (2)--(3) imply

\[
\boxed{
\mathcal E_A(f_+)-\mathcal E_A(f_-)
\ge \frac{c'}{sL}
}
\tag{4}
\]

after a finite head.

For the prime-flute adjacent self-blocks in PF-340 this specializes to

\[
\boxed{
\Delta_n^+\ge \frac{c}{s_nL_n},
\qquad
\Delta_n^-\ge \frac{c}{s_{n-1}L_n}.
}
\tag{5}
\]

Hence

\[
\boxed{
\Delta_n^{\mathrm{sym}}
=\frac12(\Delta_n^-+\Delta_n^+)
\ge
\frac{c}{L_n}
\left(\frac1{s_{n-1}}+\frac1{s_n}\right)>0.
}
\tag{6}
\]

## 1. The `f_+` datum pays the full collapsing-corridor conductance

PF-216 gives a growing embedded finite-finite corridor. For

\[
T_s=\operatorname{arsinh}\frac{\theta}{\sinh s}
\]

with fixed small `0<\theta<1`, the remaining core-ray length `\ell(t)` after the PF-205 strip removal satisfies

\[
\boxed{
c_0s\cosh t\le \ell(t)\le C_0s\cosh t}
\tag{7}
\]

for `|t|\le T_s`, with uniform constants. The associated Fermi metric is uniformly equivalent there to the product metric at the scale needed for the one-dimensional variational estimate.

For every fixed `|t|\le1` and large `L`, equation (1) gives

\[
|f_+(t)|^2\ge \frac{c_1}{L}.
\tag{8}
\]

Any admissible extension has boundary values `f_+(t)` and `0` at the two ends of the corresponding core ray. The one-dimensional positive-shift minimum, or simply weighted Cauchy--Schwarz after dropping nonnegative tangential and mass terms, gives

\[
\mathcal E_{\text{ray}}(t)
\ge c_2\frac{|f_+(t)|^2}{\ell(t)}.
\tag{9}
\]

Using the upper bound in (7) on the fixed window `|t|\le1` and integrating (9) proves

\[
\mathcal E_A(f_+)
\ge
c\int_{-1}^1\frac{dt}{sL\cosh t}
\ge \frac{c'}{sL},
\]

which is (2). No information from the cusp-side part of the pant is needed for this lower bound.

## 2. The half-cuff partner has a quadratic zero at the collapsing corridor

The decisive cancellation is already visible algebraically. From (1),

\[
f_-(t)
=-\frac{2}{\sqrt L}
\sin\frac{3\pi t}{L}
\sin\frac{\pi t}{L},
\]

so for all real `t`,

\[
\boxed{|f_-(t)|\le C\frac{t^2}{L^{5/2}}.}
\tag{10}
\]

Similarly

\[
|f_-'(t)|
\le C\min\left(L^{-3/2},\frac{|t|}{L^{5/2}}\right).
\tag{11}
\]

On the PF-216 corridor use the explicit raywise trial

\[
u(t,r)=f_-(t)\left(1-\frac r{\ell(t)}\right),
\qquad 0\le r\le\ell(t).
\tag{12}
\]

The exact ultraparallel graph used in PF-215/PF-216 gives not only (7) but a uniform logarithmic derivative bound `|\partial_t\ell|/\ell\le C` on every slightly shortened fixed-`\theta` corridor. Therefore the transverse, tangential, and positive-shift pieces of (12) obey

\[
\mathcal E_{\mathrm{corr}}(u)
\le
C\int_{-T_s}^{T_s}
\left[
\frac{|f_-(t)|^2}{s\cosh t}
+s\cosh t\bigl(|f_-'(t)|^2+|f_-(t)|^2\bigr)
\right]dt.
\tag{13}
\]

The first integral is the only singular one. Equation (10) and the finite fourth moment of `\operatorname{sech}t` give

\[
\int_{-T_s}^{T_s}
\frac{|f_-(t)|^2}{s\cosh t}\,dt
\le
\frac{C}{sL^5}
\int_{\mathbb R}t^4\operatorname{sech}t\,dt
\le \frac{C'}{sL^5}.
\tag{14}
\]

For the remaining terms, PF-216 gives

\[
\int_{-T_s}^{T_s}s\cosh t\,dt=O(1),
\]

while `\|f_-\|_\infty^2=O(L^{-1})` and `\|f_-'\|_\infty^2=O(L^{-3})`. Hence

\[
\boxed{
\mathcal E_{\mathrm{corr}}(u)
\le C\left(\frac1{sL^5}+\frac1L\right).
}
\tag{15}
\]

This is the key scale separation: the same collapsing corridor that costs `f_+` order `1/(sL)` costs its half-cuff partner four additional powers of `L^{-1}` in the singular term.

## 3. The cusp-side remainder contributes only a nonsingular amount

It remains to complete the trial outside a slightly shortened PF-216 corridor. Cut the one-cusp pant along its standard orthogeodesic seams into the two isometric right-angled ideal hexagons. Once the finite-finite region with `s\cosh t\lesssim1` is removed, the remaining target-boundary arcs meet only noncollapsing hexagon/cusp-side geometry. They admit a cover by unit-scale hyperbolic boundary charts with bounded overlap and a standard cusp chart at the ideal end. The number of ordinary charts is `O(L)`.

Extend the trace in each ordinary chart by a fixed inward cutoff and use the standard decaying cutoff in the cusp chart. Since

\[
|f_-(t)|^2\le \frac4L,
\qquad
|f_-'(t)|^2\le \frac{C}{L^3},
\]

each unit chart costs `O(L^{-1})`, the bounded-overlap sum costs `O(1)`, and the two transition strips at the corridor ends cost the same order. Thus the corridor trial (12) can be completed to an admissible global extension with

\[
\boxed{
\mathcal E_A(f_-)
\le C\left(1+\frac1{sL^5}\right),
}
\tag{16}
\]

which proves (3).

The estimate deliberately needs no sharp asymptotic for the cusp-side DtN map. It uses only that the finite-finite common-perpendicular is the unique collapsing interaction with the *zero Dirichlet finite boundary*; away from that corridor the one-cusp hexagon geometry is noncollapsing at unit scale.

## 4. The common sign is forced once `sL\to0`

Subtracting (16) from (2),

\[
\mathcal E_A(f_+)-\mathcal E_A(f_-)
\ge
\frac{c}{sL}
-rac{C}{sL^5}
-C.
\tag{17}
\]

Relative to the first term, the second is `O(L^{-4})` and the last is `O(sL)`. Thus if `L\to\infty` and `sL\to0`,

\[
\boxed{
\mathcal E_A(f_+)-\mathcal E_A(f_-)
\ge \frac{c'}{sL}>0
}
\tag{18}
\]

after a finite head.

This is exactly the common-sign theorem PF-340 left open. It does not come from positivity of the DtN operator alone; positivity would not fix the sign of the `c_2`--`c_1` matrix element. The sign comes from the geometry of the particular half-cuff pair: one combination is nonzero at the unique collapsing finite-finite corridor and the other vanishes there to second order.

By polarization,

\[
\mathcal E_A(f_+)-\mathcal E_A(f_-)
=2\operatorname{Re}\langle c_2,Ac_1\rangle,
\]

so (18) also identifies the sign and scale of the fixed raw odd Fourier coupling itself.

## 5. Both adjacent prime-flute pants satisfy the same estimate

For PF-340's right self-block `A_n^+`, use `s=s_n`; for the left self-block `A_n^-`, use `s=s_{n-1}`. Zero twist centers the same boundary coordinate at the finite-finite seam foot on both faces, so the same `f_{n,+},f_{n,-}` pair is used on both sides.

PF-216 gives on the prime tail

\[
s_j=O(P_j^{-0.475}),
\qquad
L_j=O(\log P_j),
\tag{19}
\]

and neighboring prime labels are asymptotically comparable. Hence

\[
s_nL_n\to0,
\qquad
s_{n-1}L_n\to0.
\tag{20}
\]

Applying (18) twice proves (5). In particular neither adjacent pant can contribute an eventually negative leading contrast, and PF-340's possible cancellation is eliminated.

Combining (5) with PF-340 gives (6). Using `1/s_{n-1}+1/s_n\gtrsim P_n^{0.475}` from (19) and `w_n\asymp P_n^{-1}` from PF-205,

\[
\boxed{
\frac{\Delta_n^{\mathrm{sym}}}{w_n}
\gtrsim
\frac{P_n^{1.475}}{\log P_n}
\to\infty.
}
\tag{21}
\]

The rate is only a convenient unconditional consequence of the Baker--Harman--Pintz exponent already used in PF-215/PF-216; no sharp prime-gap estimate is needed.

## Prior-art and novelty audit

Narrow-gap DtN conductance and graph/network reductions are classical. PF-216 already records Borcea--Gorb--Wang, *Asymptotic Approximation of the Dirichlet to Neumann Map of High Contrast Conductive Media*, Multiscale Modeling & Simulation 12 (2014), 1494--1532, DOI `10.1137/140960761`, as nearby thin-gap DtN prior art. Riemann-surface DtN gluing and degeneration are represented by Wentworth, *A Meyer-Vietoris formula for the determinant of the Dirichlet-to-Neumann operator on Riemann surfaces*, arXiv:2209.11863.

A fresh targeted search found these general narrow-gap/gluing frameworks, but no theorem stating the project-specific fixed `m=1,2` half-cuff contrast (18) for a degenerating one-cusp hyperbolic pant, nor the two-adjacent-pant no-cancellation consequence (21). No external theorem is imported into the proof: the derivation uses PF-216's already-established exact Fermi corridor bounds, elementary variational estimates, and the standard ideal-hexagon/cusp decomposition for the nonsingular remainder. No `SOURCES.md` change is required for theorem dependency.

The Mathia-specific contribution is therefore the scale-separated test function argument that turns PF-340's logical cancellation possibility into a definite common positive sign and closes the PF-336 translation gate.

## Boundaries and falsification

1. **This closes a sufficient translation gate, not the direct endpoint itself.** PF-336 transfers a small normalized-insertion translation commutator to the completed polar rotation. Failure of the premise does not imply a lower bound for the completed polar commutator.
2. **The PF-318/PF-320 upper-bound route remains open.** A direct Hilbert--Schmidt estimate for the actual shear-deleted local angle could still close the reference channel without using PF-336 translation transport.
3. **The proof is fixed-mode and low-frequency.** It does not claim a uniform asymptotic for the full DtN matrix.
4. **The positive sign is geometric, not abstract positivity.** Replacing the PF-339 pair or moving its phase origin can destroy the quadratic-zero argument.
5. **The artificial seam cut is load-bearing.** The PF-216 two-sided corridor bounds after strip removal are used directly.
6. **No scattering, determinant, zeta-zero, critical-line, or RH statement follows.**

A falsification would have to break one of three explicit ingredients: PF-216's uniform two-sided corridor estimate after the PF-205 strip removal, the global admissible extension bound (16) on the noncollapsing ideal-hexagon/cusp remainder, or the zero-twist identification of the PF-339 test origin with the finite-finite common-perpendicular foot on both adjacent pant faces.

## Consequence for the research line

The cheapest PF-340 no-cancellation task is now complete. The actual raw symmetric half-cuff contrast is not merely non-`o(w_n)`; after seam-width normalization it diverges at least like `P_n^{1.475}/\log P_n`. Therefore the PF-336 strategy of proving completed translation locality by first proving translation locality of the normalized pant insertion is no longer a live branch.

The direct-channel frontier should return to the independent PF-318/PF-320 upper-bound route, or to a different completed-angle mechanism that does not require the false normalized-insertion translation gate. PF-341 does not justify inferring a completed polar-angle obstruction from the raw contrast alone.