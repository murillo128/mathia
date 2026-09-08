# PF-215 — thin pant corridors force normalized adjacent hopping to diverge

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + NEGATIVE/OBSTRUCTION`. PF-214 isolates a simple sufficient gate for the smooth decomposition-interface route: if the adjacent blocks of the energy-normalized exterior precision

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

are uniformly bounded, then its inverse `D=(I+K)^{-1}` has uniform exponential module decay and PF-213 closes the weak-trace reassembly. That sufficient gate is **false for the canonical PF-205 seam cut**. The obstruction already appears on the constant symmetric boundary modes. The one-cusp pant core between neighboring long cuffs contains a fixed-tangential-width corridor whose transverse thickness is `O(s_n)`, where the exact tight-pants cuff distance is

\[
s_n=\frac{h_n+h_{n+1}}2.
\]

Opposite constant boundary values therefore cost at least `c/s_n` in the positive-shift exterior energy, while equal constant values cost only `O(1)`. Polarization forces the exterior DtN cross form between the two neighboring constant modes to have magnitude `\gtrsim s_n^{-1}`. By contrast, the PF-205 two-sided strip energy of the symmetric constant module mode is at most its area `2w_nL_n`. Hence every bounded realization of the normalized adjacent block satisfies

\[
\boxed{
\|Q_{n+1}KQ_n\|
\ge
\frac{c}{s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}}.
}
\]

Using `w_n\asymp P_n^{-1}`, `L_n=O(\log P_n)`, and Baker--Harman--Pintz `g_n=O(P_n^{0.525})`, the right side is

\[
\boxed{
\|Q_{n+1}KQ_n\|
\gtrsim
\frac{P_n^{1.475}}{\log P_n}
\longrightarrow\infty.
}
\]

Thus PF-214's uniform-hopping hypothesis cannot hold, already on the prime-side metric. This does **not** show that the Schur factor `D` lacks sufficient decay: the large off-diagonal conductance is accompanied by large diagonal energies, and inversion may exploit their correlated structure. It does show that the next smooth-route argument must be scale-sensitive and use that structure; a uniform absolute bound on normalized neighboring hopping is no longer a live branch.

## Claim

Use the PF-205 simultaneous natural-width seam cut on the prime flute. Let `C_n,C_{n+1}` be two neighboring distinguished cuffs bounding one one-cusp pant, with circumferences

\[
L_n=2a_n,
\qquad
L_{n+1}=2a_{n+1}.
\]

To avoid collision with PF-205's cuff-defect notation `d_n=a_n^+-a_n`, write

\[
\boxed{
s_n:=\operatorname{dist}(C_n,C_{n+1})
=\frac{h_n+h_{n+1}}2
}
\tag{1}
\]

for the exact common-perpendicular distance inside the tight pant, as in PF-032/PF-026. Let the PF-205 Fermi-area halfwidths be

\[
w_j=\kappa d_j,
\qquad
\rho_j:=\operatorname{arsinh}(w_j)
\tag{2}
\]

in normal-distance coordinates, and let `E_n` be the remaining one-cusp pant core after removing the two neighboring seam strips. Let `\Lambda_{E,n}` be its positive Dirichlet-to-Neumann form for `\Delta+1` on its two finite artificial boundary components.

Denote by `\mathbf 1_n` the boundary vector which is identically one on **both** sides of the strip module `Q_n`, and put

\[
q_n:=\langle \mathbf 1_n,\Lambda_{Q,n}\mathbf 1_n\rangle.
\tag{3}
\]

Let

\[
\beta_n
:=
\Lambda_{E,n}(1\text{ on the }n\text{-side},
1\text{ on the }(n+1)\text{-side})_{\rm cross}
\tag{4}
\]

be the bilinear cross term between the two constant boundary data. Then, after a finite head,

\[
\boxed{|β_n|\ge \frac{c}{s_n}}
\tag{5}
\]

and

\[
\boxed{q_n\le 2w_nL_n.}
\tag{6}
\]

Consequently, if the adjacent normalized form block

\[
K_{n+1,n}:=Q_{n+1}\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}Q_n
\tag{7}
\]

extends to a bounded operator on the normalized boundary-energy modules, then

\[
\boxed{
\|K_{n+1,n}\|
\ge
\frac{c}{s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}}.
}
\tag{8}
\]

If for some tail indices the form block does not have such a bounded extension, PF-214's uniform bounded-extension hypothesis already fails there. Thus (8) covers precisely the remaining case relevant to that hypothesis.

For the exact prime parameters, with `P_n=p_{n-1}` and `g_n=p_n-p_{n-1}` as in PF-205,

\[
w_n\asymp P_n^{-1},
\qquad
L_n=O(\log P_n),
\qquad
s_n=O(P_n^{-0.475}),
\tag{9}
\]

so

\[
\boxed{
\|K_{n+1,n}\|
\ge
c\frac{P_n^{1.475}}{\log P_n}
}
\tag{10}
\]

for all sufficiently large `n` whenever the block is bounded. In particular

\[
\boxed{
\sup_n\|Q_{n+1}KQ_n\|=\infty.
}
\tag{11}
\]

Equation (11) refutes PF-214's simplest sufficient locality gate. No claim is made here about the actual off-diagonal decay of `D=(I+K)^{-1}`.

## 1. A fixed tangential window across the tight pant has thickness `O(s_n)`

The narrow-pant estimate can be seen directly in hyperbolic Fermi coordinates and does not require a degeneration theorem. Around `C_n`, use normal distance `r` and arclength `t`, so

\[
g=dr^2+\cosh^2r\,dt^2.
\tag{12}
\]

Normalize `t=0` at the common perpendicular to `C_{n+1}`. In the hyperbolic plane, the lift of the second geodesic at distance `s=s_n` is the exact graph

\[
\boxed{
\sinh r_s(t)
=
\frac{\sinh s}
{\sqrt{1-\cosh^2s\,\tanh^2t}}.
}
\tag{13}
\]

One derivation uses the hyperboloid parametrization

\[
X(\tau)
=(\cosh s\cosh\tau,\sinh\tau,\sinh s\cosh\tau)
\]

for the second geodesic and eliminates `\tau` against the Fermi coordinates of the first. For every fixed `T<\infty`, (13) gives uniformly for `|t|\le T`,

\[
r_s(t)=s\cosh t\,(1+O_T(s^2)),
\qquad
r_s(t)\le C_Ts
\tag{14}
\]

once `s` is small.

The PF-205 strip boundary adjacent to the pant is at normal distance `\rho_n=\operatorname{arsinh}(w_n)` from `C_n`. The strip around `C_{n+1}` is disjoint and its pant-facing boundary is encountered before the original geodesic `C_{n+1}` along each normal ray in a sufficiently small fixed window. Therefore the part of `E_n` on such a ray has length at most `r_{s_n}(t)`, hence at most `C_Ts_n`. Because `L_n\to\infty`, a fixed interval `|t|\le T` lies inside the lifted cuff fundamental segment for the whole tail.

This is the only geometric input needed below: **a fixed amount of tangential measure is separated by a transverse distance of order at most `s_n`**.

## 2. Opposite constants force `1/s_n` exterior energy

For real constant boundary values, let

\[
A_n:=\mathcal E_{E_n}(1,0),
\qquad
C_n:=\mathcal E_{E_n}(0,1),
\qquad
B_n:=\beta_n,
\tag{15}
\]

where `\mathcal E_{E_n}` is the minimized positive-shift energy associated with `\Lambda_{E,n}`. By bilinearity,

\[
E_{+,n}:=\mathcal E_{E_n}(1,1)=A_n+C_n+2B_n,
\tag{16}
\]

\[
E_{-,n}:=\mathcal E_{E_n}(1,-1)=A_n+C_n-2B_n.
\tag{17}
\]

The same-sign energy is uniformly bounded. The constant trial function `u\equiv1` is admissible, and a one-cusp hyperbolic pair of pants has area `2\pi`; deleting the seam strips only lowers the area. Hence

\[
\boxed{E_{+,n}\le \operatorname{Area}(E_n)\le2\pi.}
\tag{18}
\]

For opposite boundary values, take any admissible finite-energy extension `u`. On every normal segment from the `+1` artificial boundary to the `-1` artificial boundary inside the fixed `|t|\le T` corridor, the fundamental theorem of calculus and weighted Cauchy--Schwarz give

\[
4
\le
\left(\int |\partial_ru|^2\cosh r\,dr\right)
\left(\int \operatorname{sech}r\,dr\right).
\tag{19}
\]

The second factor is at most the segment length, hence `C_Ts_n` by (14). Integrating (19) over a fixed nonzero `t` interval gives

\[
\boxed{E_{-,n}\ge \frac{c_T}{s_n}.}
\tag{20}
\]

The positive `L^2` term in the `\Delta+1` energy only strengthens this lower bound. Subtracting (16) from (17),

\[
E_{-,n}-E_{+,n}=-4B_n.
\tag{21}
\]

Since `s_n\to0`, equations (18)--(21) imply, after a finite head,

\[
B_n<0,
\qquad
\boxed{|B_n|\ge c/s_n,}
\tag{22}
\]

which is (5). The sign has the expected conductance interpretation: neighboring boundary components are strongly coupled with a negative off-diagonal DtN term.

## 3. The symmetric strip mode has vanishing normalization energy

On the PF-205 two-sided strip

\[
Q_n=(-w_n,w_n)\times(\mathbb R/L_n\mathbb Z)
\]

in signed Fermi-area coordinates,

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad
d\mu=dx\,ds.
\tag{23}
\]

The boundary vector `\mathbf1_n=(1,1)` has the constant extension `u\equiv1`. Therefore the variational characterization of the positive DtN form gives the exact trial bound

\[
q_n
\le
\int_{Q_n}1\,d\mu
=
\boxed{2w_nL_n.}
\tag{24}
\]

This is precisely the low symmetric sector that PF-212 and PF-214 warned cannot be treated by a one-sided trace estimate. Its interior normalization energy collapses with the strip area.

Now set

\[
f_n
:=
\frac{\Lambda_{Q,n}^{1/2}\mathbf1_n}{\sqrt{q_n}},
\qquad
\|f_n\|=1.
\tag{25}
\]

For the adjacent block of `K`, the only exterior component coupling modules `n` and `n+1` is `E_n`. Hence, at form level,

\[
\left|
\langle f_{n+1},Kf_n\rangle
\right|
=
\frac{|B_n|}{\sqrt{q_nq_{n+1}}}.
\tag{26}
\]

If that form block extends boundedly, equations (22) and (24) give

\[
\|K_{n+1,n}\|
\ge
\frac{c}{s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}},
\tag{27}
\]

up to one harmless absolute factor. This proves (8).

## 4. Prime geometry makes the lower bound diverge polynomially

PF-205/PF-107 give

\[
d_n=\frac1{P_n}+o(P_n^{-1}),
\qquad
w_n=\kappa d_n\asymp P_n^{-1}.
\tag{28}
\]

The exact tight-pants relation PF-032 gives (1), while

\[
h_n=\frac{g_n}{P_n}(1+o(1)).
\tag{29}
\]

Baker--Harman--Pintz gives the unconditional consecutive-prime envelope

\[
g_n=O(P_n^{0.525}).
\tag{30}
\]

Since `P_{n+1}/P_n\to1`, equations (1), (29), and (30) yield

\[
\boxed{s_n=O(P_n^{-0.475}).}
\tag{31}
\]

The cuff formula together with the elementary lower bound on odd-prime gaps gives

\[
L_n=O(\log P_n),
\tag{32}
\]

and likewise for `n+1`. Combining (27)--(32),

\[
s_n\sqrt{w_nL_n\,w_{n+1}L_{n+1}}
\le
C\frac{\log P_n}{P_n^{1.475}},
\tag{33}
\]

which proves (10)--(11).

The exponent `1.475` is not asserted to be sharp. It merely converts the standard unconditional `0.525` prime-gap envelope into a convenient whole-tail divergence statement. Any stronger prime-gap upper bound would strengthen the displayed rate, but no such improvement is needed for the obstruction.

## 5. What PF-214's scalar falsifier was warning about now occurs geometrically

PF-214 showed abstractly that positive nearest-neighbor precision does not imply a uniform inverse-decay rate: the scalar family

\[
K_t=t(2I-S-S^*)
\]

has a correlation length that diverges with `t`. PF-215 does not identify the PF boundary precision with that scalar model, but it shows that the canonical PF geometry lives on the **large-hopping**, not uniformly bounded, side of the same dichotomy.

The mechanism is geometric and unavoidable for the chosen normalization. Neighboring distinguished cuffs become close at scale `s_n`, so the pant core strongly penalizes opposite constants by `s_n^{-1}`. At the same time the natural PF-205 strip normalizes the symmetric constant mode by the much smaller area scale `w_nL_n`. Conjugating exterior energy by this vanishing interior energy magnifies the adjacent low-symmetric coupling.

Therefore the implication

\[
\text{block Jacobi precision}
+\text{uniform adjacent normalized hopping}
\Longrightarrow
\text{uniform exponential Schur locality}
\]

remains correct as PF-214 states it, but its second hypothesis is not satisfied by the actual PF tail.

## 6. What remains alive

This obstruction does **not** prove that the smooth-interface route fails. The quantity required by PF-213 is decay of

\[
D=(I+K)^{-1},
\]

not boundedness of `K` itself. The same narrow pant that creates a large cross term also contributes large diagonal energy. A scale-sensitive inverse argument may exploit the resulting correlated, graph-Laplacian-like structure even though an absolute Combes--Thomas bound based only on `\sup\|K_{n+1,n}\|` is impossible.

The next smooth-route target is therefore one of the following genuinely stronger structural statements:

1. derive the low-symmetric compression of `K` closely enough to control the inverse of the resulting variable-conductance block-Jacobi form, including the diagonal/cross cancellation;
2. prove a weighted or nonuniform Combes--Thomas estimate whose final `D` blocks satisfy PF-213's transport budget despite the divergent raw hopping scale;
3. bypass blockwise `D` decay with another exact weighted-ideal factorization that retains the physical `d_n` coefficient on its module.

PF-204's unsmoothed native two-Hilbert-space factorization remains a separate interface route. PF-183's true-short-collar endpoint splice also remains independent.

## 7. Prior art and novelty audit

No novelty is claimed for the Dirichlet principle, polarization of DtN forms, hyperbolic Fermi coordinates, narrow-gap energy growth, or the idea that DtN operators can converge to network conductances in singular geometries.

A structure-directed literature audit found close generic analogues. Liliana Borcea, Yuliya Gorb, and Yingpei Wang, *Asymptotic Approximation of the Dirichlet to Neumann Map of High Contrast Conductive Media*, Multiscale Modeling & Simulation **12** (2014), 1494--1532, DOI `10.1137/140960761`, derives DtN asymptotics for close-to-touching inclusions and an associated resistor-network description. David Krejčiřík, *Spectrum of the Laplacian in a narrow curved strip with combined Dirichlet and Neumann boundary conditions*, ESAIM: COCV **15** (2009), 555--568, DOI `10.1051/cocv:2008035`, provides nearby prior art for width-dependent variational/norm-resolvent behavior in narrowing strips. Neither setting is the hyperbolic one-cusp pant with PF's interior-energy normalization.

The project-specific deduction is the combination of four already-persisted PF facts with the elementary corridor estimate: the exact tight-pants separation `s_n=(h_n+h_{n+1})/2`, the natural PF-205 width `w_n\asymp P_n^{-1}`, the low-symmetric strip energy normalization, and prime-gap growth. That combination rules out the particular uniform adjacent-hopping hypothesis proposed in PF-214. No broad new theorem about degenerating DtN maps is claimed.

## 8. Falsification and boundary checks

A later adversary should test the result at these points.

1. Equation (13) must describe the actual lift of two ultraparallel neighboring cuff geodesics with `t=0` at their common perpendicular. A sign or coordinate error here would invalidate the fixed-window corridor estimate.
2. The PF-205 artificial boundaries must remain disjoint and lie between the two cuffs so that each normal ray in the chosen fixed window crosses the pant core from one artificial boundary to the other before reaching `C_{n+1}`.
3. The opposite-constant lower bound uses a fixed tangential interval, not the entire long cuff. No factor `L_n` is being claimed in (20).
4. The same-sign bound uses the positive shift `\Delta+1` and finite pant area. At an on-spectrum or zero-shift problem the coercive boundary form requires separate treatment.
5. The strip test vector is the two-sided **symmetric** constant mode. Replacing it by one-sided or antisymmetric data changes the normalization scale and does not prove (27).
6. Equation (27) is a form test. If the adjacent form block is unbounded, that already contradicts PF-214's bounded-extension hypothesis; if it is bounded, the displayed operator-norm lower bound follows.
7. The rate in (10) uses BHP only as an upper envelope for consecutive gaps. The conclusion `\sup_n\|K_{n+1,n}\|=\infty` does not depend on any conjectural prime-gap estimate.
8. Nothing here proves slow decay or noncompactness of `D`, failure of PF-213's weighted transport criterion, failure of the unsmoothed PF-204 route, failure of the true-short-collar splice, or failure of the full weak-`S_1` first-relative-resolvent target.

## Consequences for the research line

The smooth decomposition-interface problem is now narrower. PF-214 correctly reduces global topology to a block-Jacobi precision, but PF-215 removes its cheapest quantitative completion: **the actual normalized adjacent pant hopping is not uniformly bounded; it diverges strongly on the low symmetric strip modes.**

The next useful calculation should therefore study the inverse of the actual large-conductance block-Jacobi form, not seek a uniform bound that the geometry forbids. The decisive question is whether diagonal/off-diagonal cancellation and the module-dependent prime weights produce enough decay in `D=(I+K)^{-1}` for PF-213, or whether this low-symmetric conductance channel becomes a genuine endpoint obstruction.