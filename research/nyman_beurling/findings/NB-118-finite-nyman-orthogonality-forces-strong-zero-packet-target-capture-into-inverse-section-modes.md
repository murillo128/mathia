# NB-118 — finite Nyman orthogonality forces strong zero-packet target capture into inverse-section modes

**Status:** `EXACT-DERIVED + ACTUAL-ZETA-SOURCE-ORTHOGONALITY + TARGET-AWARE-CELL-COMPRESSION + INVERSE-SECTION-RETENTION + NB-117-SHARPENING + REPRESENTATION-AUDIT`.

`NB-117` converts the remaining high-zero finite-section escape into a weighted interpolation problem for actual zeta-zero power sums. Its quantitative source input is still height-sensitive: for a packet above ordinate `G`, order-one finite target capture forces a direction with cell-retained energy `O(1/G+1/R)`. There is a second source constraint that does not use the zero height at all. Every actual zeta-zero packet is orthogonal to every fixed finite Nyman generator space, while the target has an explicit finite projection onto that space. If a compressed zero packet captures more target than the residual left by that fixed Nyman section, the excess correlation must be cancelled beyond the cell cutoff.

Let

\[
V_M=\operatorname{span}\{g_2,\ldots,g_M\},
\qquad
p_M=P_{V_M}e,
\qquad
r_M=e-p_M,
\qquad
d_M=\|r_M\|,
\tag{1}
\]

in the natural-cell realization of `NB-117`, and retain

\[
\mathcal E_R=\operatorname{span}\{\psi_n:1\le n<R\},
\qquad Q_R=P_{\mathcal E_R},
\qquad e_R=Q_Re,
\qquad L_R=\|e_R\|^2=1-\frac1R.
\tag{2}
\]

Put

\[
d_{M,R}:=\|Q_Rr_M\|,
\qquad
S_{M,R}:=\|(I-Q_R)p_M\|^2.
\tag{3}
\]

For every finite multiset `F` of actual right-half off-critical zeta zeros, multiplicities included, every `f in K_F` with `Q_Rf ne 0` satisfies the following implication. If

\[
q_R(f):=
\frac{|\langle Q_Rf,e_R\rangle|^2}
{\|Q_Rf\|^2L_R}
\tag{4}
\]

obeys

\[
q_R(f)L_R>d_{M,R}^2,
\tag{5}
\]

then

\[
\boxed{
\frac{\|Q_Rf\|^2}{\|f\|^2}
\le
\frac{S_{M,R}}
{S_{M,R}+
 \bigl(\sqrt{q_R(f)L_R}-d_{M,R}\bigr)^2}.
}
\tag{6}
\]

Because `p_M` is a fixed finite combination of bounded Nyman generators,

\[
S_{M,R}=O_M(R^{-1}),
\qquad
d_{M,R}\le d_M,
\qquad
d_{M,R}\longrightarrow d_M.
\tag{7}
\]

Consequently, for every fixed `M` and every fixed target fraction `c>d_M^2`, any finite actual-zero packet with `chi_(F,R)>=c` contains a target-bearing witness satisfying

\[
\boxed{
\frac{\|Q_Rf\|^2}{\|f\|^2}
=O_{M,c}(R^{-1}).
}
\tag{8}
\]

This is strictly deeper than the inverse-height scale from `NB-116`--`NB-117` whenever `R/G -> infinity`. The finite escape can no longer be described merely as an `O(1/G)` compression mode once its target capture clears a fixed finite-section baseline: it must collapse at the **inverse section scale** itself.

The first source equation already gives a clean explicit threshold. For `M=2`,

\[
p_2=2g_2,
\qquad
d_2^2=1-\log2.
\tag{9}
\]

Hence any fixed capture fraction

\[
c>1-\log2\approx0.3068528
\tag{10}
\]

forces `(8)`. Using only `g_2` and `g_3` lowers the baseline much further. If `G_3` is their `2 x 2` Gram matrix and `b_3=(\langle e,g_2\rangle,\langle e,g_3\rangle)^T`, then

\[
d_3^2=1-b_3^*G_3^{-1}b_3
\approx0.0957477839277540.
\tag{11}
\]

Thus already two fixed source normal equations force every finite actual-zero packet capturing more than about `9.575%` of the visible target into an `O(1/R)` cell-compression direction. No zero counting, zero-density estimate, packet-width assumption, or lower bound on the ordinate enters this conclusion.

## 1. Actual zero powers satisfy every fixed Nyman source equation

Use the primitive normal form from `NB-117`. For a simple zero packet,

\[
P_f(n)=\sum_{\rho\in F}c_\rho n^{-\overline\rho},
\tag{12}
\]

and a zero of multiplicity `m` contributes the confluent block

\[
n^{-\overline\rho}(\log n)^k,
\qquad0\le k<m.
\tag{13}
\]

For an integer `b>=2`, the classical Dirichlet series

\[
(1-b^{1-s})\zeta(s)
=
\sum_{n\ge1}a_b(n)n^{-s},
\qquad
a_b(n)=1-b\,\mathbf1_{b\mid n},
\tag{14}
\]

converges for `Re s>0` by bounded partial sums. Its partial coefficient sums are

\[
A_b(N):=\sum_{n\le N}a_b(n)
=N-b\left\lfloor\frac Nb\right\rfloor
=N\bmod b.
\tag{15}
\]

At every zeta zero `rho` with `Re rho>1/2`, `(14)` vanishes at `s=overline rho`; if the zero has multiplicity `m`, its first `m-1` derivatives vanish as well. The differentiated Dirichlet series are legitimate on compact subsets of `Re s>0` by Dirichlet convergence, since `(log n)^k n^{-s}` tends to zero with eventually decreasing modulus after fixing a right half-plane.

Abel summation therefore gives, for every primitive `(12)`--`(13)`,

\[
0
=
\sum_{n\ge1}a_b(n)P_f(n)
=
\sum_{n\ge1}(n\bmod b)
   \bigl(P_f(n)-P_f(n+1)\bigr).
\tag{16}
\]

Under the harmonic-cell unitary, `g_b` has value `{n/b}` on the `n`th cell, while `NB-117` gives

\[
\langle f,\psi_n\rangle
=
\sqrt{n(n+1)}
\bigl(P_f(n)-P_f(n+1)\bigr).
\tag{17}
\]

Since `{n/b}=(n mod b)/b`, equation `(16)` is exactly

\[
\boxed{\langle f,g_b\rangle=0.}
\tag{18}
\]

Thus every finite actual-zero packet space `K_F` is orthogonal to every fixed `V_M`. For `b=2`, `(16)` reduces to

\[
\sum_{n\ \mathrm{odd}}
\bigl(P_f(n)-P_f(n+1)\bigr)=0,
\tag{19}
\]

the dual zero-packet form of the same parity cancellation already used for the primal best residual in `NB-009`--`NB-010`. No novelty is claimed for this annihilator by itself; the new use is to constrain the `NB-117` finite compression escape.

## 2. Excess finite target correlation has to pass through the fixed source projection

Fix `M`, `R`, and `f in K_F`, and abbreviate

\[
x:=Q_Rf,
\qquad X:=\|x\|.
\tag{20}
\]

Because `e=p_M+r_M`,

\[
\langle x,e_R\rangle
=
\langle x,Q_Rp_M\rangle
+
\langle x,Q_Rr_M\rangle.
\tag{21}
\]

If `q_R(f)` is as in `(4)`, then

\[
|\langle x,e_R\rangle|
=\sqrt{q_R(f)L_R}\,X.
\tag{22}
\]

Cauchy--Schwarz on the residual term in `(21)` therefore forces

\[
\boxed{
|\langle x,Q_Rp_M\rangle|
\ge
\bigl(
 \sqrt{q_R(f)L_R}-d_{M,R}
\bigr)X.
}
\tag{23}
\]

The right side is positive precisely under `(5)`. This is the finite-section baseline: target alignment up to `d_(M,R)^2/L_R` can be supplied entirely by the residual left after the first `M` Nyman generators, but any stronger alignment must use the visible part of `p_M` itself.

That visible correlation cannot be free for an actual zero packet. Equation `(18)` gives

\[
\langle f,p_M\rangle=0.
\tag{24}
\]

Since `p_M` is cell-constant and splits orthogonally at the cutoff,

\[
\langle x,Q_Rp_M\rangle
=-
\langle (I-Q_R)f,(I-Q_R)p_M\rangle.
\tag{25}
\]

Thus every unit of visible correlation with the finite Nyman projection has to be cancelled by the packet beyond `R`.

## 3. Tail cancellation gives the inverse-section retention bound

Combining `(23)` and `(25)` with Cauchy--Schwarz gives

\[
\|(I-Q_R)f\|
\sqrt{S_{M,R}}
\ge
\bigl(
 \sqrt{q_R(f)L_R}-d_{M,R}
\bigr)X.
\tag{26}
\]

If `S_(M,R)=0`, condition `(5)` is impossible unless `X=0`; otherwise square `(26)` and use

\[
\|f\|^2
\ge
\|Q_Rf\|^2+
\|(I-Q_R)f\|^2.
\tag{27}
\]

This proves `(6)`.

To estimate the source tail, write

\[
p_M=\sum_{b=2}^M\alpha_b g_b,
\qquad
A_M:=\sum_{b=2}^M|\alpha_b|.
\tag{28}
\]

Every generator satisfies `|g_b|<=1` cellwise. Therefore

\[
S_{M,R}
\le
A_M^2
\sum_{n\ge R}\frac1{n(n+1)}
=
\frac{A_M^2}{R}.
\tag{29}
\]

Also `Q_Rr_M -> r_M` in norm, so `d_(M,R)->d_M`. If `c>d_M^2`, then for all sufficiently large `R`,

\[
\sqrt{cL_R}-d_{M,R}
\ge
\frac12(\sqrt c-d_M)>0.
\tag{30}
\]

Equations `(6)`, `(29)`, and `(30)` prove `(8)`.

At packet level, the finite-dimensional quotient defining `chi_(F,R)` attains its supremum on `Q_RK_F`. Hence `chi_(F,R)>=c>d_M^2` supplies a witness to which `(8)` applies. The result is independent of packet rank and remains valid for confluent multiplicity blocks because the source orthogonality `(18)` was proved with the corresponding derivatives in `(14)`.

## 4. The first two finite baselines are already quantitative

For `M=2`, the harmonic-cell values are

\[
g_2|_{I_n}
=\frac12\mathbf1_{n\ \mathrm{odd}}.
\tag{31}
\]

Hence

\[
\langle e,g_2\rangle=\frac{\log2}{2},
\qquad
\|g_2\|^2=\frac{\log2}{4},
\tag{32}
\]

so `p_2=2g_2` and `(9)` follows. In fact here one can retain the exact finite quantities:

\[
d_{2,R}^2
=
\sum_{\substack{n<R\\n\ \mathrm{even}}}
\frac1{n(n+1)},
\qquad
S_{2,R}
=
\sum_{\substack{n\ge R\\n\ \mathrm{odd}}}
\frac1{n(n+1)}.
\tag{33}
\]

Thus `(6)` is exactly the parity tail-compensation inequality, not merely an asymptotic consequence of it.

For `M=3`, direct summation over the six residue classes gives

\[
b_3=
\begin{pmatrix}
\log2/2\\
\log3/3
\end{pmatrix},
\tag{34}
\]

and

\[
G_3=
\begin{pmatrix}
\log2/4 &
\log2/6+\log3/12-\pi\sqrt3/54\\[1mm]
\log2/6+\log3/12-\pi\sqrt3/54 &
2\log3/9-\pi\sqrt3/81
\end{pmatrix}.
\tag{35}
\]

Therefore `(11)` is an exact finite expression, with the decimal shown only for scale. The corresponding projection coefficients are approximately `1.1567613542` and `1.3745047793`, so `(29)` has a finite absolute constant already for this two-generator control. The important point is not the decimal improvement itself: **any fixed finite Nyman section supplies its own rigorous capture threshold `d_M^2`, and every capture above that threshold is forced onto the `1/R` compression scale.**

## 5. Relation to the high-zero frontier and failure modes

For a packet supported above height `G`, `NB-116` and `NB-117` give the source-height requirement

\[
\frac{\|Q_Rf\|^2}{\|f\|^2}
\ll_c
\frac1G+\frac1R
\tag{36}
\]

for a witness capturing a fixed target fraction. The present estimate is different rather than a reproof. Once the capture exceeds `d_M^2` for some fixed source section, `(8)` removes the `1/G` branch completely:

\[
\boxed{
\frac{\|Q_Rf\|^2}{\|f\|^2}
=O_{M,c}(R^{-1}).
}
\tag{37}
\]

In the regime `R/G -> infinity`, any successful strong finite rescue must therefore use a cell-compression mode parametrically smaller than the inverse-height modes isolated in `NB-116`. This narrows the live interpolation problem from "can actual zero powers pay continuum norm `Omega(G)`?" to the stronger question "can they produce the required target angle while hiding all but an `O(1/R)` fraction of their continuum norm in the first `R` natural cells?"

Several boundaries are essential. First, `(6)` does **not** rule out such a mode; an arbitrarily large invisible tail can still compensate the visible source correlation. Second, a single fixed `M` says nothing below its baseline `d_M^2`. Sending `M` to infinity is not free: the statement `d_M -> 0` is itself the Báez-Duarte/Nyman form of RH, and the tail constant `A_M` may deteriorate badly. Third, the theorem does not assert that `O(1/R)` compression modes are absent from abstract exponential-polynomial families. That remains the source-specific obstruction to prove.

These controls also prevent a representation overclaim. The result uses no new arithmetic information beyond two already existing structures: actual zeta-zero annihilation of the Nyman generators and the natural-cell truncation of `NB-117`. Its content is the quantitative incompatibility between **excess finite target angle** and **moderate cell retention**. A generic vector not satisfying `(18)` is a matched control: it may align with `e_R` at order one while retaining order-one continuum energy, so the source orthogonality is load-bearing.

The classical Nyman--Beurling/Báez-Duarte finite distances, zeta-zero orthogonality, and the Dirichlet identity `(14)` are standard; `NB-009`--`NB-010` already exploit the `g_2` parity normal equation on the primal residual side. A targeted prior-art search did not locate the specific finite-cutoff implication `(6)` or its use to sharpen the `NB-117` high-zero compression escape from `O(1/G+1/R)` to `O(1/R)` above a finite Nyman-distance threshold. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The next theorem boundary is now explicit: for a useful joint regime `R/G -> infinity`, exclude target-bearing actual-zero power sums with

\[
q_R(f)\ge c>d_M^2,
\qquad
\frac{\|Q_Rf\|^2}{\|f\|^2}=O(R^{-1}),
\tag{38}
\]

or derive a growing-`M` version of `(6)` with simultaneous control of `d_M` and the projection-tail constant. Either route would attack the remaining finite-section rescue at the scale forced by the source equations themselves.