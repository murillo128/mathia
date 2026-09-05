# WP-154 — Resultant chord curvature is positive on prime towers but flat across primes

**Status:** `EXACT-DERIVED + SHARP-RESTRICTION + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + DISCRETE-COBOUNDARY + PRIME-STEP-EXACTNESS + POSITIVE-PRIME-TOWER-CURVATURE + MIXED-PRIME-FLATNESS + SPECTATOR-DIVERGENCE + PRIOR-ART-CLASSICALIZATION` for the direct Hodge/cochain use of the normalized zero-order Prime-Circle resultant coefficients.

`WP-145`--`WP-153` leave genuinely higher-cohomological or nonlocal constructions outside the direct Hessian, centered-kernel, graph-Dirichlet, and normalized-spectral no-go results. The normalized resultant graph itself suggests a canonical first test: orient every nonzero resultant edge upward by divisibility and regard its exact coefficient as a real `1`-cochain.

That cochain has a surprisingly rigid structure. On the nearest-neighbor prime-step skeleton it is **globally exact**. Adding the direct longer prime-power chords creates a nonzero ordered triangle coboundary, and on each repeated-prime tower that curvature is strictly positive and even recovers the exact critical Weil ray coefficient as a boundary limit. But the curvature is completely **flat across distinct primes**: every mixed-prime rectangle has zero circulation, and all nonzero curvature is confined to one prime coordinate at a time. Moreover every nonzero prime-tower curvature cell has infinitely many spectator-prime copies with exactly the same value, so the resulting arithmetic curvature is not in the natural counting `ell^2` cell space.

Thus the resultant coefficients do contain a canonical positive local second-difference signal, but it is not the missing global Weil sign mechanism. The direct Hodge route either annihilates the prime-step carrier as an exact form, retains only place-local prime-tower curvature, or turns that curvature into a generic positive cell/Dirichlet energy whose boundary conductances return to the globally divergent category already closed by `WP-148`--`WP-150`. A surviving cohomological construction must introduce a genuinely global finite--archimedean coupling, cell structure, quotient, or topology **before** the ordinary resultant cochain is passed to Hodge positivity.

## 1. The full normalized resultant edge law is coordinate-local

Use the normalized zero-order Prime-Circle coupling from `WP-145` and `WP-148`,

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}
\qquad (m\ne n).
\tag{1}
\]

It is nonzero exactly when one index is a prime-power multiple of the other. Orient such an edge upward,

\[
m\longrightarrow mp^k,
\qquad k\ge1.
\tag{2}
\]

The Apostol formulas already audited in `WP-145`/`WP-148` give the exact coefficient

\[
\boxed{
J_{m,mp^k}
=
\begin{cases}
\displaystyle
\frac{\log p}{p^{(k-1)/2}\sqrt{p-1}},&p\nmid m,\\[8pt]
\displaystyle
\frac{\log p}{p^{k/2}},&p\mid m.
\end{cases}}
\tag{3}
\]

Put

\[
a_p:=\frac{\log p}{\sqrt{p-1}},
\qquad
b_p:=\frac{\log p}{\sqrt p},
\qquad
q_p:=p^{-1/2}.
\tag{4}
\]

Then the edge law depends only on the changed prime coordinate, its jump length, and whether that coordinate was previously zero:

\[
J_{m,mp^k}
=
\begin{cases}
a_p q_p^{k-1},&v_p(m)=0,\\
b_p q_p^{k-1},&v_p(m)\ge1.
\end{cases}
\tag{5}
\]

All other prime exponents are spectators. This is the load-bearing structural fact for the cohomological audit.

## 2. The nearest-neighbor prime-step `1`-cochain is exactly a gradient

First retain only the canonical cover edges of length one,

\[
m\longrightarrow mp.
\tag{6}
\]

Define the scalar potential on shell indices

\[
\boxed{
F(n)
=
\sum_{p\mid n} a_p
+
\sum_p (v_p(n)-1)_+ b_p.
}
\tag{7}
\]

Both sums are finite for each integer `n`. Multiplication by a prime changes exactly one exponent. If `p\nmid n`, the first occurrence adds `a_p`; if `p\mid n`, increasing the exponent adds `b_p`. Therefore

\[
\boxed{
F(np)-F(n)=J_{n,np}
}
\tag{8}
\]

for every prime step.

Hence the oriented prime-step resultant cochain is exactly

\[
\boxed{J^{(1)}=dF.}
\tag{9}
\]

Every cycle integral on the prime-step graph vanishes. In particular the Boolean square obtained by multiplying in either order by two distinct primes carries no holonomy. Thus a graph-Hodge/cycle projection of the nearest-neighbor resultant coefficients has **zero harmonic/cycle content before any positivity theorem is applied**.

This is stronger than saying that one convenient square happens to cancel: equation (7) is a global primitive on the whole finite-support exponent lattice.

## 3. Longer prime-power chords create a positive same-prime curvature

The full resultant graph also contains direct chords `m -> mp^k` with `k>=2`. These are not equal to the sum of their unit-step edges, so the full `1`-cochain is not exact.

On a stable repeated-prime ray, `p\mid m`, equation (3) is the exact critical Weil profile

\[
j_p(k):=J_{m,mp^k}
=(\log p)q_p^k.
\tag{10}
\]

Take the canonically ordered triangle

\[
m
\longrightarrow mp^k
\longrightarrow mp^{k+\ell},
\qquad
m\longrightarrow mp^{k+\ell},
\tag{11}
\]

with `k,ell>=1`. Its oriented coboundary is

\[
\begin{aligned}
\kappa_p(k,\ell)
&:=
J_{m,mp^k}
+J_{mp^k,mp^{k+\ell}}
-J_{m,mp^{k+\ell}}\\
&=
\boxed{
(\log p)
\left(q_p^k+q_p^\ell-q_p^{k+\ell}\right)>0.}
\tag{12}
\end{aligned}
\]

The first-entry case is also strictly positive. If `p\nmid m`, then

\[
\boxed{
\kappa_{p,0}(k,\ell)
=
a_p q_p^{k-1}(1-q_p^\ell)
+(\log p)q_p^\ell
>0.}
\tag{13}
\]

So the direct prime-power chords do expose a genuine scalar sign that was absent on the prime-step skeleton: **ordered same-prime triangle curvature is positive for every nondegenerate triangle.** No RH assumption, zero data, or fitted kernel enters the inequality; it follows directly from the exact resultant edge law.

There is an additional exact relation that makes this route initially tempting. Hold the first chord fixed and send the second leg to infinite exponent depth. Equations (12)--(13) give

\[
\boxed{
\lim_{\ell\to\infty}\kappa_p(k,\ell)
=J_{m,mp^k}.}
\tag{14}
\]

On a repeated-prime ray this boundary value is exactly

\[
(\log p)p^{-k/2},
\tag{15}
\]

the critical finite-place coefficient already identified by `PC-004` and `WP-001`.

Thus the normalized resultant coefficient is not merely *represented* by a new arbitrary positive kernel: it is the endpoint limit of a canonical positive ordered triangle defect inside the same shell geometry.

## 4. Every mixed-prime rectangle is exactly flat

The apparent cohomological gain in section 3 does not create a global prime interaction. Let `p!=q`, let `k,ell>=1`, and orient the multiplicative rectangle

\[
m
\to mp^k
\to mp^kq^\ell
\to mq^\ell
\to m.
\tag{16}
\]

Changing the `q`-exponent does not change the `p`-edge law in (5), and changing the `p`-exponent does not change the `q`-edge law. Therefore

\[
J_{m,mp^k}
=J_{mq^\ell,mp^kq^\ell},
\qquad
J_{m,mq^\ell}
=J_{mp^k,mp^kq^\ell},
\tag{17}
\]

and hence

\[
\boxed{
\oint_{\square(p^k,q^\ell)} J=0
}
\tag{18}
\]

for **every** base shell `m`, including cases where either prime already divides `m`.

Equivalently, the full resultant coefficient field is a sum of pullbacks of one-prime edge laws on exponent coordinates. Its nonzero cycle content comes from the failure of a *single* prime coordinate's long chord to equal a path of shorter chords; commuting distinct-prime directions contribute no curvature.

The simplest arithmetic control makes the distinction visible. The square

\[
1\to2\to6\to3\to1
\]

has exact circulation zero, while the same-prime triangle

\[
2\to4\to8\to2
\]

has circulation

\[
2\frac{\log2}{\sqrt2}-\frac{\log2}{2}>0.
\tag{19}
\]

Thus the first nontrivial discrete curvature of the zero-order resultant geometry is **prime-tower curvature, not cross-prime curvature**.

## 5. The natural curvature carrier has infinite spectator multiplicity

Fix any same-prime triangle with nonzero curvature `kappa>0`. For every fresh spectator prime `r` not dividing its vertices, multiply all three shell indices by `r`. Equation (5) is spectator-invariant, so the copied triangle has exactly the same curvature `kappa`.

Choosing infinitely many distinct spectator primes gives infinitely many distinct copied cells. Consequently the arithmetic curvature `2`-cochain is not square summable in the natural counting cell geometry:

\[
\boxed{
\sum_T |(dJ)(T)|^2
\ge
\sum_{r\ \mathrm{spectator}}\kappa^2
=\infty.}
\tag{20}
\]

The same argument excludes every finite counting `ell^s`, `s>0`, for the raw curvature carrier. This is the cell-level analogue of the spectator replication that collapses the all-prime resultant Dirichlet space in `WP-149`.

A nonuniform cell measure, quotient by spectator directions, or global normalization can evade (20), but then that additional measure/quotient/topology is part of the proposed mechanism and must be forced independently. Uniform Hodge counting does not supply it.

## 6. Why positive triangle curvature is still not a Weil-positive form

Equation (12) is a real positive result, but three adversarial checks prevent promoting it to the branch objective.

First, the sign is the sign of a **canonically oriented scalar coboundary**. Reversing the triangle orientation reverses `dJ`; this is not by itself a positive semidefinite bilinear form on a test space. Ordinary Hodge positivity appears only after one chooses a positive cell inner product, for example

\[
\mathcal Q(\eta)
=
\sum_T w_T |(d\eta)(T)|^2,
\qquad w_T\ge0.
\tag{21}
\]

Such positivity is generic Hilbert-space geometry. In the present case the arithmetic weights and curvature still separate prime by prime because of (18).

Second, using the boundary values (14) as positive conductances on shell edges and imposing the canonical conservation law produces exactly the graph-Dirichlet completion

\[
\frac12\sum_{m\ne n}J_{m,n}|f_m-f_n|^2
\tag{22}
\]

studied in `WP-148`. Its finite-prime off-diagonal sign is attractive, but the forced diagonal has infinite all-prime degree; `WP-149` strengthens this to zero effective resistance and a constant-only global energy space, while `WP-150` shows that vertex-local finite-energy normalizations erase every fixed arithmetic edge. The curvature interpretation does not remove those global obstructions.

Third, `WP-001` already proves that independently positive finite-prime ray energies cannot themselves be the Weil summands: the exact finite term has the subtractive off-diagonal coefficients and no corresponding positive local `k=0` diagonal. The positive prime-tower curvature therefore cannot be promoted by a placewise sum alone. A real solution would have to use the finite curvature inside a global operation that simultaneously produces the archimedean and polar/counterterm structure and proves the assembled sign independently.

## 7. Matched controls and escape boundary

The local positivity is not uniquely arithmetic. Replace each prime coordinate by an arbitrary label `alpha` carrying constants `c_alpha>0` and `0<r_alpha<1`, and put

\[
j_\alpha(k)=c_\alpha r_\alpha^k.
\tag{23}
\]

Then the same ordered triangle calculation gives

\[
j_\alpha(k)+j_\alpha(\ell)-j_\alpha(k+\ell)
=c_\alpha(r_\alpha^k+r_\alpha^\ell-r_\alpha^{k+\ell})>0,
\tag{24}
\]

and independent coordinates have zero rectangular circulation. Thus the sign theorem is a generic feature of a separable exponentially decaying chord law. Arithmetic enters through the special values `c_alpha=log p` and `r_alpha=p^{-1/2}`, not through the existence of the positive curvature itself.

Several escapes remain logically open and are not ruled out here:

- a global cell complex or correspondence whose `2`-cells mix finite primes with the real place before curvature is formed;
- a source-forced non-counting cell measure or quotient that survives the spectator test without reducing to independent prime rays;
- a nonlinear/determinant-line or higher-cohomological pairing whose sign theorem is not the ordinary `||d eta||^2` Hodge sign;
- a finite--archimedean coupling that changes the resultant edge field before taking a cohomological quotient.

What is ruled out is the direct claim that the **unsupplemented normalized resultant `1`-cochain already contains a global Hodge class whose own positivity can be identified with Weil positivity**. Its nearest-neighbor part is exact, its mixed-prime curvature is identically zero, and its remaining curvature is local to one prime tower and non-square-summable under the natural spectator-invariant cell counting.

## 8. Prior art and novelty audit

No new general theorem of graph Hodge theory is claimed. Exact `1`-cochains, cycle/cut decomposition, coboundaries, and positive Hodge Laplacians are classical. The close prime/divisibility cohomology prior art already recorded in `SOURCES.md` includes Oliver Knill's *On Primes, Graphs and Cohomology*; the function-field and adele-class sources recorded there likewise emphasize that successful Weil-style positivity uses **global correspondences/cohomology**, not a place-separable scalar edge field.

The cyclotomic input is also classical: equation (3) is only the Apostol resultant formula already audited and used by `WP-145` and `WP-148`. The durable Mathia-specific content is the exact synthesis of that coefficient law with the cochain test:

\[
\boxed{
\text{prime-step resultant field}=dF,
\qquad
\text{mixed-prime curvature}=0,
\qquad
\text{prime-tower chord curvature}>0.
}
\tag{25}
\]

This is a useful restriction, not a claim of a new arithmetic-cohomology theorem. It identifies exactly where the resultant graph first develops nontrivial discrete curvature and shows that the resulting sign remains too local and too spectator-replicated to supply the global Weil mechanism without additional geometry.

## Consequence for the research line

The higher-cohomological escape left after `WP-145`--`WP-153` should no longer start by taking ordinary graph Hodge theory of the existing resultant coefficients. The exact arithmetic carrier is flat in every genuinely mixed-prime direction. The only intrinsic curvature produced by the current edge law is a positive same-prime chord defect whose boundary value recovers the local Weil ray but whose direct positive completion returns to already-closed placewise/Dirichlet mechanisms.

A materially different continuation must therefore make **global coupling precede positivity/cohomology**: the finite and archimedean sectors, or distinct prime coordinates, must interact in the geometric object before a Hodge, intersection, norm, or boundary sign theorem is invoked.