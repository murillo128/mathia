# PF-298 — tight-pant constant response is an asymptotically conservative killed-conductance edge

**Status:** `EXACT-DERIVED + MAXIMUM-PRINCIPLE + ASYMPTOTIC-DERIVED + NEGATIVE/ROUTE-NARROWING`. PF-297 shows that the canonical fixed-axis Robin inverse cannot supply a depth-uniform contraction in the conserved `q` currency. The accepted source/escape clue therefore asks whether genuine loss appears in the remaining neighboring-pant/Schur reassembly. On the lowest symmetric constant channel, the one-cusp pant core does **not** provide such a uniform local discount either.

PF-215 already proves two decisive estimates for the positive-shift Dirichlet-to-Neumann form of the pant core between consecutive natural-width seam strips: the constant cross coefficient is negative with magnitude `c_n \gtrsim s_n^{-1}`, while the energy of equal constant data is at most the pant area `2\pi`. The maximum principle adds the missing sign information on the two row sums. Consequently the exact constant-boundary compression is

\[
\boxed{
M_n
=
c_n
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
+
\begin{pmatrix}
\kappa_{n,L}&0\\
0&\kappa_{n,R}
\end{pmatrix},
\qquad
c_n>0,
\quad
\kappa_{n,L},\kappa_{n,R}>0,
}
\]

with

\[
\boxed{
\kappa_{n,L}+\kappa_{n,R}\le 2\pi,
\qquad
\frac{\max(\kappa_{n,L},\kappa_{n,R})}{c_n}
\lesssim s_n\longrightarrow0.
}
\]

Thus, after normalization by its large cross-conductance, the constant response converges to the conservative two-node graph Laplacian. Equivalently, the scalar constant-mode Schur transmission through one isolated pant is

\[
\theta_{n,L\to R}
=
\frac{c_n}{c_n+\kappa_{n,R}}
=1-O(s_n),
\]

and likewise in the reverse direction. For the prime geometry PF-215 gives `s_n=O(P_n^{-0.475})`, hence `1-\theta_n=O(P_n^{-0.475})` on this compression.

This is a **local negative** for the return-potential program, not a global recurrence theorem. It says that the positive `+1` term on a narrow one-cusp pant appears, in the constant response, only as bounded killing attached to a conductance diverging like at least `1/s_n`. Therefore one cannot close the source/escape gate by assigning each neighboring pant a source-independent contraction bounded away from one. Any successful bound for the actual PF-290 mixed response must instead use accumulated nonuniform escape, the physical `P/H` split, nonconstant channels, source-specific forcing compensation, signed cancellation, or another reassembly factor that changes the relevant currency.

## Claim

Let `E_n` be the one-cusp pant core between two consecutive PF-205 natural-width seam strips, with finite artificial boundary components `\Sigma_{n,L}` and `\Sigma_{n,R}`. Use the positive shifted operator

\[
L=\Delta+1
\]

and let `\Lambda_{E,n}` be its positive Dirichlet-to-Neumann form. Restrict that form to boundary data that are constant on each of the two finite components. With

\[
e_L=(1,0),
\qquad
e_R=(0,1),
\]

write

\[
A_n=\langle e_L,\Lambda_{E,n}e_L\rangle,
\qquad
B_n=\langle e_L,\Lambda_{E,n}e_R\rangle,
\qquad
C_n=\langle e_R,\Lambda_{E,n}e_R\rangle.
\]

The compressed response matrix is

\[
M_n=
\begin{pmatrix}
A_n&B_n\\
B_n&C_n
\end{pmatrix}.
\tag{1}
\]

PF-215 proves, after a finite head,

\[
B_n<0,
\qquad
c_n:=-B_n\ge \frac{c}{s_n},
\tag{2}
\]

and for equal boundary values

\[
E_{+,n}:=A_n+2B_n+C_n\le 2\pi.
\tag{3}
\]

Define the row-sum coefficients

\[
\kappa_{n,L}:=A_n+B_n,
\qquad
\kappa_{n,R}:=C_n+B_n.
\tag{4}
\]

Then

\[
\boxed{
\kappa_{n,L}>0,
\qquad
\kappa_{n,R}>0,
\qquad
\kappa_{n,L}+\kappa_{n,R}=E_{+,n}\le2\pi.
}
\tag{5}
\]

Combining (2), (4), and (5) gives the exact decomposition

\[
\boxed{
M_n
=c_n
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
+
\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
}
\tag{6}
\]

and the quantitative relative-killing estimate

\[
\boxed{
\left\|
\frac{M_n}{c_n}
-
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
\right\|
=
\frac{\max(\kappa_{n,L},\kappa_{n,R})}{c_n}
\le C s_n.
}
\tag{7}
\]

For the prime tail, PF-215's unconditional estimate

\[
s_n=O(P_n^{-0.475})
\tag{8}
\]

therefore yields

\[
\boxed{
\left\|c_n^{-1}M_n-L_{\mathrm{edge}}\right\|
=O(P_n^{-0.475}),
\qquad
L_{\mathrm{edge}}=
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
}
\tag{9}
\]

No sharpness is claimed for the exponent in (8)--(9).

## 1. The row sums are positive killing, not an uncontrolled diagonal remainder

Let `u_{+,n}` be the finite-energy Poisson solution on `E_n` with boundary value `1` on both finite boundary components. Coercivity of `\Delta+1` gives the unique minimizer of

\[
\int_{E_n}(|\nabla u|^2+|u|^2)\,d\mu
\]

with those traces. The weak/strong maximum principle gives

\[
0<u_{+,n}<1
\]

in the interior. On each smooth finite boundary component the Hopf boundary lemma gives a strictly positive outward flux in the positive-energy Dirichlet-to-Neumann convention. By Green's identity those two integrated fluxes are exactly

\[
\int_{\Sigma_{n,L}}\partial_\nu u_{+,n}
= A_n+B_n=\kappa_{n,L},
\]

\[
\int_{\Sigma_{n,R}}\partial_\nu u_{+,n}
= C_n+B_n=\kappa_{n,R}.
\tag{10}
\]

This proves the two strict inequalities in (5). The cusp causes no additional boundary term in this local sign argument: one may apply the maximum/Hopf argument on compact cusp truncations and pass to the coercive finite-energy solution, or use the standard local boundary lemma directly once the solution is constructed.

The total row sum is the energy of `u_{+,n}`:

\[
\kappa_{n,L}+\kappa_{n,R}
=\langle(1,1),\Lambda_{E,n}(1,1)\rangle.
\tag{11}
\]

The constant trial function `u\equiv1` is admissible because a one-cusp hyperbolic pant has finite area `2\pi`. Therefore

\[
\kappa_{n,L}+\kappa_{n,R}
\le \operatorname{Area}(E_n)
\le2\pi,
\tag{12}
\]

which is the final part of (5).

Thus the constant response is not merely a positive `2\times2` matrix with a large negative cross term. It is exactly a two-node conductance edge of strength `c_n`, with nonnegative shunt/killing terms `\kappa_{n,L},\kappa_{n,R}` created by the positive shift.

## 2. Narrow pants make conductance dominate killing

PF-215 obtains the lower bound `c_n\ge c/s_n` from a fixed tangential corridor whose transverse width is `O(s_n)`: opposite constants must pay gradient energy of order `1/s_n`. Equal constants, by contrast, pay only the positive-shift mass term and have the uniform trial bound (12).

Consequently

\[
0<\frac{\kappa_{n,L}}{c_n},
\frac{\kappa_{n,R}}{c_n}
\le
\frac{2\pi}{c_n}
\le C s_n.
\tag{13}
\]

Equation (7) is now immediate from (6). The narrow-pant limit is therefore a **large-conductance / bounded-killing limit**, not a uniformly absorbing local response.

This distinction matters for the current source/escape question. The diagonal `+1` term is genuinely present and makes the response nonsingular, but its strength does not scale with the transverse conductance. Normalizing by the interaction that actually transports the constant mode across the pant sends the killing fraction to zero.

## 3. The constant-mode scalar Schur transfer loses only `O(s_n)` per isolated pant

For constant boundary coefficients `(x,y)`, equation (6) gives the exact compressed quadratic form

\[
Q_n(x,y)
=c_n(x-y)^2
+\kappa_{n,L}x^2
+\kappa_{n,R}y^2.
\tag{14}
\]

If the left coefficient `x` is fixed and the right coefficient is eliminated **within this two-dimensional constant-boundary compression**, the minimizer is

\[
y
=\theta_{n,L\to R}x,
\qquad
\theta_{n,L\to R}
=\frac{c_n}{c_n+\kappa_{n,R}}.
\tag{15}
\]

Hence

\[
\boxed{
0<1-\theta_{n,L\to R}
=\frac{\kappa_{n,R}}{c_n+\kappa_{n,R}}
\le C s_n,
}
\tag{16}
\]

and the reverse orientation obeys the same estimate with `\kappa_{n,L}`. The effective scalar energy left after the elimination is

\[
\kappa_{n,L}
+\frac{c_n\kappa_{n,R}}{c_n+\kappa_{n,R}}
\le
\kappa_{n,L}+\kappa_{n,R}
\le2\pi.
\tag{17}
\]

The qualifier in (15) is essential. The full PF boundary problem contains nonconstant modes, physical `P/H` projections, strip normalization, and the rest of the chain. Equation (15) is **not** asserted to be the actual complete return coefficient. It is a sharp falsifier for one tempting local mechanism: even the exact constant-mode pant compression has no contraction factor bounded away from one.

## 4. Consequence for the source-weighted return-potential clue

PF-297 and the present result now remove two different candidates for a hidden uniform discount:

- fixed-axis Robin normalization is `q`-nonexpansive and becomes exactly `q`-mass preserving on the complete positive inverse;
- the neighboring one-cusp pant, on its lowest symmetric constant compression, is a killed conductance edge whose relative killing is only `O(s_n)`.

Therefore a prospective finite-depth return equation cannot justify a uniform Green bound by multiplying generic local contraction constants from these two pieces. Any source-adapted excessive potential must identify where the **actual** mixed response loses mass or where its forcing decays fast enough to compensate a long lifetime.

This does not show that the return potential diverges. The small losses in (16) can accumulate over many pants; `\sum s_n` is not summable on the prime flute, and the physical `P/H` split may create additional escape or cancellation. It also does not identify the correct coefficient currency after nonconstant-mode reassembly. The result only says that the local constant channel is asymptotically conservative after its natural conductance normalization, so a depth-uniform local spectral gap is unavailable there.

The next discriminating calculation remains the one in the accepted clue: derive the actual `P/H`-split neighboring-pant return/reassembly equation in PF-296 source coordinates. The new constraint is that its source/escape estimate must survive the nearly conservative constant pant channel rather than silently replacing it by a fixed discount.

## 5. Prior art and novelty audit

The analytic ingredients are classical. The strong maximum principle and Hopf boundary lemma for second-order elliptic equations are standard; a canonical reference is D. Gilbarg and N. S. Trudinger, *Elliptic Partial Differential Equations of Second Order*, 2nd ed., Springer, DOI `10.1007/978-3-642-61798-0`. The interpretation of a symmetric response matrix with negative off-diagonal entries as conductances plus diagonal killing is likewise standard in electrical-network/Schrödinger response theory; for a discrete comparison see C. Araúz, A. Carmona, A. M. Encinas, *Dirichlet-to-Robin maps on finite networks*, Applicable Analysis and Discrete Mathematics **9** (2015), 85--102, DOI `10.2298/AADM150207004A`.

No novelty is claimed for the maximum principle, Hopf lemma, `M`-matrix/response-matrix language, Schur elimination, or the abstract killed-edge decomposition. A structure-directed literature search did not locate the project-specific statement for the degenerating hyperbolic one-cusp pant family. The Mathia-specific contribution is the combination of the exact PF-215 corridor estimate with the shifted pant response to obtain the quantitative ratio

\[
\frac{\text{killing}}{\text{conductance}}=O(s_n)
\]

and to place that ratio inside the current PF-296/PF-297 source/escape gate. This is a route-narrowing reduction, not a claim of a new general theorem about Dirichlet-to-Neumann maps.

## 6. Boundary conditions and falsification tests

The sign conclusion (5) uses the positive shifted problem and the positive-energy DtN convention of PF-211--PF-215. A different normal/sign convention must be translated through Green's identity before importing (4)--(6). At an on-spectrum or zero-shift parameter the same killing interpretation is not automatic.

The constant-mode compression is exact as a quadratic-form restriction but is not asserted to be invariant under the full Schur elimination. A later argument must not replace the physical `P/H`-split return operator by the scalar coefficient `\theta_n` unless it proves the required invariant/reducing structure. Coupling to nonconstant modes may create either additional damping or additional long-range transfer.

The estimate `O(s_n)` is one-sided: it proves that local relative killing is small, not that it is comparable to `s_n`. The shunt terms may be much smaller. Conversely, because `\sum s_n` diverges, (16) does not prove survival of a product of transfers over the whole flute. Any global recurrence/transience or Green-potential conclusion requires a separate accumulated-loss analysis with the actual source and physical projections.

Finally, this result concerns the low symmetric constant channel. It does not alter PF-280's one-sided mixed-frequency ideal factorization, PF-282's extension-angle criterion, PF-287's heavy-range projection problem, or PF-290's basis-invariant shorting deficit except by constraining one possible mechanism used to estimate their complete reassembly.