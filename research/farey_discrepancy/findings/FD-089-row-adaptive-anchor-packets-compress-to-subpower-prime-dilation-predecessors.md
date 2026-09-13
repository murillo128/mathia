# FD-089 — row-adaptive anchor packets compress to subpower prime-dilation predecessors

**Status:** `EXACT-DERIVED + FALSE-RH-FRONTIER + SMALL-REPEATED-PRIME-CONCENTRATION + COMMON-ANCHOR-COMPRESSION + SUBPOWER-MULTIHORIZON-RECURRENCE + NEAR-FRONTIER-PREDECESSOR + INTER-BLOCK-COMPOSITION-FRONTIER`.

`FD-088` shows that a fixed positive share of the nonsquarefree energy on a false-RH frontier block can be stitched row by row to exact lower horizons

\[
a_r=\frac{N_r}{p_r},
\qquad p_r^2\mid r,
\qquad N_r\in[H,H+L_H],
\]

with unit Jordan-weight distortion. Its explicit remaining obstruction is that the lower horizon depends on the row, so the packet is not one physical predecessor state and cannot be inserted directly into the existing scalar GCD-duality identities.

The row dependence can be compressed much further. First, the zero-frontier pointwise bound for the quotient-shell source implies that, on sufficiently sharp frontier blocks, rows whose repeated prime factor is larger than `H^alpha` carry negligible energy for **every fixed `alpha>0`**. Second, once a repeated prime `p` is fixed, all row-adaptive anchors with that label can be rounded to the single canonical lower horizon

\[
A_p:=\left\lceil\frac Hp\right\rceil
\]

with at most unit source error in each participating coordinate. The same `O(R_H)` Hilbert error already absorbed in `FD-088` therefore collapses the whole bulk packet to at most `H^alpha` genuine physical predecessor horizons.

Consequently, for every fixed sufficiently small `alpha>0`, arbitrarily large occupied frontier blocks satisfy

\[
\boxed{
\sum_{\substack{p\le H^\alpha\\p\ {m prime}}}
E_{\lceil H/p\rceil,1}
\ge
(\eta-o(1))E_{H,1}.
}
\tag{1}
\]

Here `eta>0` is any fixed occupation level supplied by `FD-084`--`FD-088`, for example any `eta<3/64`. Diagonalizing `alpha\downarrow0` produces a false-RH frontier sequence on which the row-adaptive packet is carried by only `H^{o(1)}` canonical predecessors, all at scale `H^{1-o(1)}`. Pigeonholing (1) then gives one prime `p_H=H^{o(1)}` for which

\[
\boxed{
E_{\lceil H/p_H\rceil,1}
\ge H^{-o(1)}E_{H,1},
\qquad
\left\lceil\frac H{p_H}\right\rceil=H^{1-o(1)}.
}
\tag{2}
\]

If the chosen frontier losses are diagonalized to zero as well, both sides of (2) have the full energy exponent `2 Theta`. Thus the first bulk predecessor supplied by `FD-088` is not intrinsically a high-entropy family: at the power-exponent level it compresses to a subpower family, and one member of that family is itself a near-frontier-energy horizon.

This still does not close the GCD-duality accumulation problem. The single predecessor selected from (2) need not have positive nonsquarefree occupation, and the coordinate mask transported from it may carry only an `H^{-o(1)}` fraction rather than a fixed positive fraction. What is removed is the stronger obstruction that row adaptivity alone forces polynomially many unrelated lower states.

## 1. Setup from the super-block anchor packet

Assume

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}>\frac12.
\tag{3}
\]

Fix

\[
0<\delta<\Theta-\frac12
\tag{4}
\]

and a fixed occupation threshold `eta>0` available from `FD-084`; one may take any `eta<3/64`. Along the recurrent frontier blocks used in `FD-088`, write

\[
L_H:=\lfloor H^{\Theta-\delta}\rfloor,
\qquad
R_H:=\left\lfloor\frac{H}{L_H+1}\right\rfloor.
\tag{5}
\]

Then

\[
R_H=H^{1-\Theta+\delta+o(1)},
\qquad
R_H=o(L_H).
\tag{6}
\]

The seed extraction in `FD-084` allows the frontier loss to be chosen arbitrarily small and fixed before each extraction. Thus, for a parameter `kappa>0` to be chosen below, we may take the block seed so that

\[
E_{H,1}>H^{2\Theta-\kappa}.
\tag{7}
\]

Retain the complete physical Jordan vector

\[
V_{H,1}(r)
=
\sqrt{w(r)}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right),
\qquad
w(r)=\frac{J_2(r)}{r^2},
\tag{8}
\]

and the stitched core vector from `FD-088`,

\[
W_H(r)
=
\sqrt{w(r)}\,
\mathcal H(m_r),
\qquad
m_r:=\left\lceil\frac Hr\right\rceil,
\qquad 2\le r\le R_H.
\tag{9}
\]

That finding gives

\[
\boxed{
\|W_H-P_{\le R_H}V_{H,1}\|_2^2\le R_H=o(E_{H,1})
}
\tag{10}
\]

and, on the nonsquarefree coordinates,

\[
\boxed{
\|P_{\rm ns}W_H\|_2^2
\ge(\eta-o(1))E_{H,1}.
}
\tag{11}
\]

The task is to control how many genuinely different repeated-prime labels are needed to support the energy in (11).

## 2. Large repeated primes carry negligible frontier energy

Fix `alpha>0` and put

\[
P_H:=H^\alpha.
\tag{12}
\]

Let `B_(H,alpha)` be the set of nonsquarefree core rows `r<=R_H` for which

\[
p^2\nmid r
\qquad\text{for every prime }p\le P_H.
\tag{13}
\]

Every `r` in this set is divisible by `p^2` for at least one prime `p>P_H`.

By `FD-046`, for every fixed `sigma>Theta`,

\[
|\mathcal H(n)|\ll_\sigma n^\sigma.
\tag{14}
\]

Since `w(r)<=1`, a union bound over square divisors gives

\[
\begin{aligned}
\sum_{r\in B_{H,\alpha}}|V_{H,1}(r)|^2
&\le
\sum_{p>P_H}
\sum_{m\ge1}
\left|
\mathcal H\!\left(\left\lfloor\frac{H}{p^2m}\right\rfloor\right)
\right|^2\\
&\ll_\sigma
H^{2\sigma}
\sum_{p>P_H}p^{-4\sigma}
\sum_{m\ge1}m^{-2\sigma}.
\end{aligned}
\tag{15}
\]

Because `sigma>Theta>1/2`, both series are convergent and

\[
\boxed{
\sum_{r\in B_{H,\alpha}}|V_{H,1}(r)|^2
\ll_\sigma
H^{2\sigma}P_H^{1-4\sigma}.
}
\tag{16}
\]

The prime restriction is not even needed for the last estimate; bounding the prime tail by the corresponding integer tail is sufficient.

Write `sigma=Theta+epsilon`. Dividing (16) by (7) gives

\[
\frac{1}{E_{H,1}}
\sum_{r\in B_{H,\alpha}}|V_{H,1}(r)|^2
\ll
H^{\,2\epsilon+\kappa-\alpha(4\sigma-1)}.
\tag{17}
\]

For every fixed `alpha>0`, choose `epsilon>0` and then `kappa>0` sufficiently small that

\[
2\epsilon+\kappa<\alpha(4\sigma-1).
\tag{18}
\]

This is always possible because `4Theta-1>1`. Then (17) is `o(1)`.

The same conclusion holds for the stitched vector. From (10),

\[
\|P_{B_{H,\alpha}}W_H\|_2
\le
\|P_{B_{H,\alpha}}V_{H,1}\|_2+\sqrt{R_H},
\tag{19}
\]

and the second term is `o(sqrt(E_(H,1)))`. Combining (11), (17), and (19), the complementary small-square set

\[
G_{H,\alpha}
:=
\{2\le r\le R_H:\exists p\le P_H\text{ prime with }p^2\mid r\}
\tag{20}
\]

satisfies

\[
\boxed{
\|P_{G_{H,\alpha}}W_H\|_2^2
\ge
(\eta-o(1))E_{H,1}.
}
\tag{21}
\]

Thus an arbitrarily small positive power cutoff on the repeated prime already captures essentially all of the constant nonsquarefree frontier mass supplied by `FD-088`.

## 3. A fixed repeated prime collapses all of its row-adaptive anchors to one physical horizon

Make the assignment deterministic: for each `r in G_(H,alpha)`, let

\[
p(r):=\min\{p\le P_H:p\text{ prime and }p^2\mid r\}.
\tag{22}
\]

Put

\[
s_r:=\frac{r}{p(r)}.
\tag{23}
\]

Then `p(r)|s_r`, so repeated-prime deflation preserves the Jordan weight exactly:

\[
w(s_r)=w(r).
\tag{24}
\]

For a prime `p<=P_H`, define the single canonical lower horizon

\[
\boxed{A_p:=\left\lceil\frac Hp\right\rceil.}
\tag{25}
\]

Consider a row assigned to `p`, so `r=ps` with `p|s`. The stitched source argument is

\[
m_r=\left\lceil\frac{H}{ps}\right\rceil.
\tag{26}
\]

Since

\[
\frac Hp\le A_p<\frac Hp+1,
\tag{27}
\]

one has

\[
\frac{H}{ps}
\le
\frac{A_p}{s}
<
\frac{H}{ps}+\frac1s.
\tag{28}
\]

Here `s>=p>=2`. If `H/(ps)` is an integer then `H/p` is an integer multiple of `s`, so the two quotient arguments agree exactly. Otherwise (28) shows

\[
\boxed{
0\le
m_r-\left\lfloor\frac{A_p}{s}\right\rfloor
\le1.
}
\tag{29}
\]

The quotient-shell source has the exact one-step bound from `FD-084`,

\[
|\mathcal H(n)-\mathcal H(n-1)|\le1.
\tag{30}
\]

Therefore

\[
\left|
\sqrt{w(r)}\mathcal H(m_r)
-
\sqrt{w(s)}\mathcal H\!\left(\left\lfloor\frac{A_p}{s}\right\rfloor\right)
\right|
\le1.
\tag{31}
\]

The second term is the `s`th coordinate of the genuine physical vector `V_(A_p,1)`. Under the exact dilation operator `mathscr D_p` of `FD-087`, its image lands at row `r=ps`; because `p|s`, (24) makes the dilation factor exactly one.

Let `S_(p,H)` be the set of lower rows `s=r/p` assigned to `p`, and let `Q_(p,H)` be the corresponding output-row projection. Define

\[
C_H
:=
\sum_{p\le P_H}
Q_{p,H}\mathscr D_p P_{S_{p,H}}V_{A_p,1}.
\tag{32}
\]

The output supports in (32) are disjoint by construction. Equation (31) gives

\[
\boxed{
\|C_H-P_{G_{H,\alpha}}W_H\|_2^2
\le \#G_{H,\alpha}
\le R_H
=o(E_{H,1}).
}
\tag{33}
\]

Combining (21) and (33),

\[
\boxed{
\|C_H\|_2^2
\ge(\eta-o(1))E_{H,1}.
}
\tag{34}
\]

This is the desired compression: the rowwise horizons `a_r` from `FD-088` have been replaced, up to vanishing Hilbert error, by one actual physical horizon for each repeated-prime label.

## 4. The compressed packet gives a scalar multihorizon energy recurrence

On every selected lower row in `S_(p,H)`, the dilation in (32) has unit weight distortion by (24). Since the output supports are disjoint,

\[
\|C_H\|_2^2
=
\sum_{p\le P_H}
\|P_{S_{p,H}}V_{A_p,1}\|_2^2.
\tag{35}
\]

Each summand is a positive coordinate sub-energy of the genuine lower-horizon Schur energy. Hence

\[
\|P_{S_{p,H}}V_{A_p,1}\|_2^2
\le E_{A_p,1}.
\tag{36}
\]

Equations (34)--(36) prove

\[
\boxed{
\sum_{\substack{p\le H^\alpha\\p\ {m prime}}}
E_{\lceil H/p\rceil,1}
\ge
(\eta-o(1))E_{H,1}.
}
\tag{37}
\]

Unlike the coordinatewise identity in `FD-088`, (37) is a genuine scalar inequality between physical energies. It still has several lower horizons rather than one, but their number is at most

\[
\pi(H^\alpha)\le H^\alpha.
\tag{38}
\]

Moreover every participating horizon lies in

\[
\boxed{
H^{1-\alpha}
\le A_p\le\frac H2+1.
}
\tag{39}
\]

For small `alpha`, the whole packet therefore lives at almost the full logarithmic scale of `H`, not merely above the `sqrt(HL_H)` floor of `FD-088`.

Pigeonholing (37) gives at least one prime `p_H<=H^alpha` such that

\[
\boxed{
E_{\lceil H/p_H\rceil,1}
\ge
(\eta-o(1))H^{-\alpha}E_{H,1}.
}
\tag{40}
\]

For fixed `alpha`, this loses a power `alpha`; the useful conclusion comes from diagonalizing the cutoff.

## 5. Diagonalization yields subpower complexity and one near-frontier predecessor

Choose a sequence `alpha_j>0` with

\[
\alpha_j\downarrow0
\tag{41}
\]

and, if desired, keep `alpha_j<(1-Theta+delta)/2` so that the explicit cutoff remains below the automatic bound `p<=sqrt(R_H)` from `FD-088`. For each `j`, choose `epsilon_j`, `kappa_j` satisfying (18), with

\[
\epsilon_j\to0,
\qquad
\kappa_j\to0,
\tag{42}
\]

and then take a sufficiently large recurrent frontier block `H_j` so that all errors above are smaller than `1/j`. The block theorem supplies arbitrarily late choices for every fixed parameter tuple, so the horizons may be chosen increasing.

Put

\[
P_j:=H_j^{\alpha_j}.
\tag{43}
\]

Then

\[
P_j=H_j^{o(1)},
\qquad
\#\{p\le P_j\}=H_j^{o(1)},
\tag{44}
\]

and (37) becomes

\[
\boxed{
\sum_{p\le P_j}E_{\lceil H_j/p\rceil,1}
\ge(\eta-o(1))E_{H_j,1}.
}
\tag{45}
\]

All these lower horizons satisfy

\[
\left\lceil\frac{H_j}{p}\right\rceil
=H_j^{1-o(1)}
\tag{46}
\]

uniformly over the packet. A final pigeonhole therefore gives a prime `p_j<=P_j` and a lower horizon

\[
A_j:=\left\lceil\frac{H_j}{p_j}\right\rceil
\tag{47}
\]

such that

\[
\boxed{
E_{A_j,1}
\ge H_j^{-o(1)}E_{H_j,1},
\qquad
A_j=H_j^{1-o(1)}.
}
\tag{48}
\]

Because `kappa_j->0`, the chosen frontier seeds obey

\[
E_{H_j,1}=H_j^{2\Theta-o(1)}
\tag{49}
\]

in the lower-exponent sense, while `FD-046` supplies the matching upper envelope. From (48) and `log A_j/log H_j->1`,

\[
\boxed{
E_{A_j,1}=A_j^{2\Theta-o(1)}.
}
\tag{50}
\]

Thus every selected block in the diagonal sequence has a **single prime-dilation predecessor that is itself a near-frontier-energy horizon**, with only subpower scale separation and subpower energy loss.

The complete-vector transport estimate of `FD-086` can then be applied around `A_j` itself: because (50) supplies near-frontier norm, an additive window of any fixed exponent below `Theta` is again projectively coherent after choosing the usual margin. This gives a coherent predecessor block, although no positive nonsquarefree occupation statement for that predecessor block is obtained here.

## 6. Stress tests and exact boundary

The main unresolved point is normalized overlap. Equation (45) distributes a fixed positive current-block energy over `H^{o(1)}` predecessor states. The single state obtained from (48) is guaranteed only an `H^{-o(1)}` share. That is enough to preserve the polynomial exponent but not enough to invoke a theorem requiring a fixed projective overlap or a fixed positive occupation fraction at every link.

Likewise, (50) is an energy statement, not an occupation statement. A near-frontier-energy predecessor need not satisfy `U_(A_j,1)>=eta E_(A_j,1)`. Therefore one cannot iterate `FD-089` recursively from `A_j` without an additional argument locating occupation at, or sufficiently near, the selected predecessor. `FD-084` guarantees occupied blocks in every fixed-power future window, but it does not place one inside the much narrower subpower interval between `A_j` and `H_j`.

The scalar inequality (37) also must not be replaced by

\[
E_{A,1}\gg E_{H,1}
\]

for one fixed contraction factor. The prime label may vary with the frontier block, and the pigeonhole loss is real. Nor does (37) identify the selected lower-coordinate masks with the whole lower states; the passage to full `E_(A_p,1)` is only a positive upper enlargement after the exact masked identity (35).

The argument is stated at the minimal head `D=1`. As in `FD-088`, a fixed larger head has only the finite exceptional band `D<r<=D^2` where deflation may fall through the head. Outside that band the same small-repeated-prime concentration and canonical-horizon compression work unchanged. A clean general-`D` statement therefore has the same dichotomy as `FD-088`: either the finite exceptional band carries nonvanishing frontier energy, or the remaining bulk obeys the compressed recurrence after deleting finitely many coordinates. No growing head is claimed.

Finally, the large-repeated-prime estimate (16) depends on the zero-frontier pointwise envelope for `mathcal H`. A mere density estimate for squarefull rows would not suffice because the physical energy may concentrate on sparse coordinates. The analytic amplitude cap is what converts square-divisor sparsity into an energy statement.

## 7. Prior-art boundary and research consequence

A targeted audit covered the classical Smith/Jordan GCD-matrix factorization literature, Farey--Mertens discrepancy transforms, Jordan-totient multiplicativity, square-divisor decompositions, and floor-quotient/dilation formulations. Those ingredients separately contain the Euler product for `J_2`, standard square-divisor counting, and the classical Mertens zero-frontier power bound. The search did not locate the source-specific statement proved here: compression of a false-RH nonsquarefree frontier packet to canonical prime contractions `ceil(H/p)`, followed by the scalar recurrence (37) and the subpower predecessor consequence (48)--(50). No priority claim is inferred from absence of a search hit.

No new external theorem is load-bearing. The only analytic input beyond `FD-088` is the already-sourced pointwise zero-frontier envelope from `FD-046`; the rest is the exact Jordan radical identity, the one-step shell bound, and elementary convergence of `sum p^(-4sigma)`. `SOURCES.md` therefore requires no new dependency.

The live composition problem is narrower than after `FD-088`. Row adaptivity no longer forces one unrelated physical horizon per occupied row. On a diagonal false-RH frontier sequence the whole constant-energy packet can be represented, up to vanishing Hilbert error, by only

\[
\boxed{H^{o(1)}}
\]

canonical prime-dilation predecessor states, and one of them preserves the full `2Theta` energy exponent. The next discriminating theorem can therefore target a much smaller residual: either upgrade the `H^{-o(1)}` selected overlap to a fixed-strength transport/occupation statement, show that the subpower family can be composed across consecutive frontier blocks, or construct an admissible source showing that even this zero-entropy predecessor family can remain multiplicatively incompatible.