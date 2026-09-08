# PF-220 — coefficient-adjacent low recoupling is weak trace without Schur locality

**Status:** `EXACT-DERIVED + OPERATOR-THEORETIC + POSITIVE/ROUTE-NARROWING`. PF-217--PF-219 rule out a broad scalar completion of the smooth PF-205 seam route: after shorting, the low Schur inverse cannot be assigned the raw `q_n` endpoint damping, nor any fixed polylogarithmic weakening of it, while retaining summable module transport. Those negative results do **not** obstruct the part of the actual PF-211/PF-212 recoupling word in which the physical seam coefficient is adjacent to the same fixed-frequency low sector on both sides. After inserting the low/high identity immediately next to the coefficient, every coefficient-adjacent low block has rank `O(1+L_n)` and norm `O(d_n)` before the global Schur factors act. PF-210 therefore puts the complete block family in `S_{1,\infty}`, and bounded multiplication by the low compressions `PDP` preserves that ideal. No off-diagonal locality, scalar endpoint damping, or decay estimate for `PDP` is required.

There is also a universal positive-contraction estimate for the pieces that leave the low sector. If `0\le D\le I`, `P` is any orthogonal projection, `H=I-P`, and `W_d=\bigoplus_n d_nP_n` is the PF low-sector prime weight, then

\[
\boxed{
HDP\,W_d^{1/2}\in\mathcal S_{2,\infty},
\qquad
W_d^{1/2}PDH\in\mathcal S_{2,\infty}.
}
\]

Indeed `PDHDP\le PDP-(PDP)^2\le \tfrac14P`, while PF-210 gives `W_d\in S_{1,\infty}`. Thus low/high leakage is automatically critical weak-`S_2` **when the prime-decaying weight is already on the low endpoint**. The actual unresolved terms place the metric coefficient on the opposite, coefficient-side module after Schur transport. The remaining smooth-interface gate is therefore sharper than PF-219: it is a **coefficient-side weight-transfer / cross-frequency Schur-leakage problem** for `PDH` and `HDP`, not a problem of controlling the scalar low compression `PDP` itself.

## Claim

Use the simultaneous PF-205 seam decomposition and PF-211/PF-212 notation separately for the source and target metrics `r\in\{g,h\}`. Write the normalized boundary-energy space as

\[
\mathcal B_r=\bigoplus_n\mathcal B_{r,n},
\]

let `P_r=\bigoplus_nP_{r,n}` be the fixed physical tangential-frequency projection of PF-212, and put

\[
H_r=I-P_r.
\tag{1}
\]

The low ranks satisfy

\[
\boxed{
\operatorname{rank}P_{r,n}\le C(1+L_n),
\qquad
L_n\le C(1+\log P_n).
}
\tag{2}
\]

Let

\[
D_r=\Lambda_{Q,r}^{1/2}
(\Lambda_{Q,r}+\Lambda_{E,r})^{-1}
\Lambda_{Q,r}^{1/2},
\qquad 0\le D_r\le I,
\tag{3}
\]

and let `A_r,M_r` be the PF-211 normalized gradient/Poisson factors, so

\[
A_r^*A_r+M_r^*M_r=I,
\qquad \|A_r\|,\|M_r\|\le1.
\tag{4}
\]

The low boundary recoupling is

\[
C_{r,\rm lo}=A_rD_rP_rM_r^*.
\tag{5}
\]

Let the physical seam coefficient be module diagonal,

\[
F=\bigoplus_nF_n,
\qquad
\|F_n\|\le Cd_n,
\qquad
d_n\le \frac C{P_n},
\tag{6}
\]

as in PF-205--PF-212. All harmless fixed finite matrix fibres and finite colorings are absorbed into constants.

Then the following statements hold.

### A. One-sided low/Dirichlet coefficient-adjacent term

For a PF-212 one-sided word

\[
T_{\rm lo/D}
=C_{h,\rm lo}^*M_FG_{g,D}
=M_hP_hD_hA_h^*M_FG_{g,D},
\tag{7}
\]

insert `I=P_h+H_h` immediately between `D_h` and `A_h^*`. The coefficient-adjacent low part is

\[
T_{\rm lo/D}^{PP}
=
M_h(P_hD_hP_h)
\bigl(P_hA_h^*M_FG_{g,D}\bigr).
\tag{8}
\]

The middle operator in parentheses is a two-sided module block family. Its `n`th block has

\[
\operatorname{rank}Z_n\le C(1+L_n),
\qquad
\|Z_n\|\le Cd_n,
\tag{9}
\]

because the output lies in `P_{h,n}`, while `A_h`, the multiplication coefficient, and the Dirichlet factor are module-local and uniformly bounded at the operator level. Therefore PF-210 gives

\[
\boxed{
Z:=P_hA_h^*M_FG_{g,D}\in\mathcal S_{1,\infty}.
}
\tag{10}
\]

Since `M_h` and `P_hD_hP_h` are bounded contractions up to harmless fixed constants, the two-sided ideal property gives

\[
\boxed{T_{\rm lo/D}^{PP}\in\mathcal S_{1,\infty}.}
\tag{11}
\]

The adjoint orientation satisfies the same conclusion.

### B. Double-low coefficient-adjacent term

For a double-boundary low word,

\[
T_{\rm lo/lo}
=
M_hP_hD_hA_h^*M_FA_gD_gP_gM_g^*,
\tag{12}
\]

insert `P_r+H_r` on the two boundary slots adjacent to the middle coefficient. The `P/P` part is

\[
\begin{aligned}
T_{\rm lo/lo}^{PP}
={}&M_h(P_hD_hP_h)
\bigl(P_hA_h^*M_FA_gP_g\bigr)\\
&\times(P_gD_gP_g)M_g^*.
\end{aligned}
\tag{13}
\]

Again the middle local block `Z_n=P_{h,n}A_{h,n}^*M_{F_n}A_{g,n}P_{g,n}` has

\[
\operatorname{rank}Z_n\le C(1+L_n),
\qquad
\|Z_n\|\le Cd_n.
\tag{14}
\]

PF-210 and bounded ideal multiplication therefore give

\[
\boxed{T_{\rm lo/lo}^{PP}\in\mathcal S_{1,\infty}.}
\tag{15}
\]

Thus the exact scalar low compressions `P_rD_rP_r` may be completely nonlocal in module index and may violate every PF-218/PF-219 endpoint-damping envelope; that alone does not reopen the coefficient-adjacent low terms.

### C. Universal source-weighted low/high leakage bound

Let `D` be either normalized Schur factor, suppress the metric label, and write

\[
B=PDP,
\qquad H=I-P.
\tag{16}
\]

Because `0\le D\le I`,

\[
D-D^2\ge0.
\tag{17}
\]

Taking the `P` compression and expanding through `P+H=I` gives

\[
P(D-D^2)P
=B-B^2-PDHDP\ge0.
\tag{18}
\]

Hence

\[
\boxed{
0\le PDHDP\le B-B^2\le\frac14P.
}
\tag{19}
\]

Define the PF low prime weight

\[
W_d:=\bigoplus_n d_nP_n.
\tag{20}
\]

Each block has rank `O(1+L_n)` and norm `O(d_n)`, so PF-210 applied directly to the positive block family yields

\[
\boxed{W_d\in\mathcal S_{1,\infty}.}
\tag{21}
\]

Now set

\[
X:=HDPW_d^{1/2}.
\tag{22}
\]

Equations (19)--(22) imply

\[
0\le X^*X
=W_d^{1/2}PDHDPW_d^{1/2}
\le\frac14W_d.
\tag{23}
\]

By the min-max ordering of eigenvalues of positive compact operators,

\[
s_j(X)^2=s_j(X^*X)
\le\frac14s_j(W_d).
\tag{24}
\]

Therefore

\[
\boxed{
HDPW_d^{1/2}\in\mathcal S_{2,\infty}.
}
\tag{25}
\]

Taking adjoints gives

\[
\boxed{
W_d^{1/2}PDH\in\mathcal S_{2,\infty}.
}
\tag{26}
\]

No block locality, bounded adjacent hopping, inverse-decay theorem, or information about the shorted scalar Green kernel is used in (19)--(26).

## 1. Why PF-219 does not obstruct the `P/P` physical word

PF-218/PF-219 test whether the low inverse itself can provide endpoint damping. In scalar form they rule out estimates of the type

\[
|\langle\nu_m,D\nu_n\rangle|
\lesssim
\sqrt{q_mq_n}(\log P_m\log P_n)^{O(1)}\eta_{m-n},
\qquad \eta\in\ell^1.
\tag{27}
\]

The `P/P` recoupling terms above use a different order of operations. The small coefficient is first kept on its physical middle module and the coefficient-adjacent low projections turn that local middle operator into a rank-`O(\log P_n)`, norm-`O(P_n^{-1})` block. PF-210 performs singular-level prime counting **before** either nonlocal low compression acts. The global factors then appear only as bounded left/right multipliers.

Thus no weight is extracted from `PDP`, and no modulewise decay of `PDP` is required. This is precisely the noncommutative placement information that disappears in PF-218/PF-219's scalar endpoint-damping ansatz.

## 2. The remaining terms are exactly cross-frequency Schur transport

The same identity insertions expose what has not been closed. Equation (7) decomposes as

\[
T_{\rm lo/D}
=T_{\rm lo/D}^{PP}
+
M_hP_hD_hH_hA_h^*M_FG_{g,D}.
\tag{28}
\]

Equation (12) decomposes into the `P/P` term (13) plus three terms containing at least one of

\[
P_hD_hH_h,
\qquad
H_gD_gP_g.
\tag{29}
\]

These are **frequency-leakage blocks of the simultaneous Schur factor**. The local coefficient remains on the module reached after that leakage, not on the source low module. Therefore (25)--(26) cannot simply be inserted with `W_d` in the required place: moving `W_d^{1/2}` through `PDH` or `HDP` is exactly a weighted-transport assertion and is not implied by positivity.

This distinction is load-bearing. The abstract estimate (25) says that low/high leakage is already at critical weak-`S_2` scale if the prime weight is attached to the low endpoint before transport. The actual PF word instead asks whether the **coefficient-side** weight and the local PF-212 ideal factors compensate the transport. A valid completion must estimate those coefficient-placed leakage words directly, with the ideal exponents required by their Dirichlet/high/double-boundary partners. A negative result should construct an actual PF-compatible family showing that the output-side prime weight is transported too far or too coherently for the required weak endpoint.

## 3. Prior art and novelty audit

The operator-theoretic ingredients are standard. Weak Schatten classes are two-sided operator ideals, and singular values obey the usual bounded-multiplication and positive-order monotonicity principles; Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS Mathematical Surveys and Monographs 120 (2005), is a standard reference for the trace-ideal framework. Modern weak-Schatten literature likewise treats `\mathcal S_{p,\infty}` as a standard symmetric operator ideal. No novelty is claimed for those facts.

The defect inequality (19) is not imported as a theorem: it is the one-line block compression of the elementary positive-contraction inequality `D^2\le D`. Likewise the passage from `W_d\in S_{1,\infty}` to (25) is immediate from (23)--(24). A structure-directed literature audit did not identify a reason to attribute this elementary block calculation as a new general operator theorem, and search absence is not used as novelty evidence.

The project-specific deduction is the placement statement: **in the exact PF-211/PF-212 expansion, all low sectors whose coefficient-side slots remain low are already globally weak trace class by PF-210, even though the scalar low Schur inverse has the strong negative behavior proved in PF-217--PF-219.** What remains is isolated to coefficient-side `P D H/H D P` leakage and the corresponding weight transfer.

## 4. Falsification and boundary checks

A later adversary should check all of the following.

1. The identity insertion must occur in the exact PF-211/PF-212 simultaneous-cut expansion. It is not enough to rearrange an abstract scalar model of `D`.
2. The coefficient `F_n` must remain on its physical module. It may not be commuted through `D_r` or reassigned to the source low index.
3. The local middle blocks in (9) and (14) must be genuinely two-sided module blocks (or a fixed finite coloring) and their output/input low projections must be the fixed-physical-frequency spaces of PF-212, so PF-210's `O(1+L_n)` rank bound applies.
4. Only bounded operator norms are used for `A_r`, `M_r`, `D_r`, and the Dirichlet gradient factor in (9). No hidden trace/Schatten summation is being attributed to those factors.
5. Equation (18) must be expanded as `PD^2P=(PDP)^2+PDHDP`; the positivity conclusion uses both self-adjointness and `0\le D\le I`.
6. `W_d` in (20) is the scalar prime-decaying envelope on the **low boundary space**, not the physical bulk multiplication operator itself. Equations (25)--(26) do not authorize moving it across `D`, `A`, or `M_F`.
7. The weak-`S_2` leakage statement is one-sided in weight placement. It does not prove the actual coefficient-side leakage words are compact or in the required ideal.
8. Nothing here proves PF-213's unweighted Schur decay, the full first relative resolvent in `S_{1,\infty}`, PF-183's true-short-collar splice, PF-204's unsmoothed endpoint, wave-operator completeness, determinants/resonances, prime/clone separation, or any RH consequence.

## Consequences for the research line

PF-217--PF-219 correctly kill the entire strategy of assigning a scalar fixed-polylog endpoint damping to `PDP`. PF-220 shows that this negative result should **not** be propagated to the actual low recoupling wholesale. Once the physical coefficient is retained and the coefficient-adjacent low slots are exposed, PF-210 already closes those pieces by prime-density singular-value counting, and arbitrary bounded nonlocality of `PDP` is harmless around them.

The smooth-interface frontier is therefore smaller. Do not spend further work trying to regularize the scalar low compression or re-prove the `P/P` low sectors. The decisive unresolved calculation is the exact coefficient-side cross-frequency leakage in (28)--(29): determine whether the physical `d_n` weight plus the PF-212 local high/Dirichlet structure controls `PDH/HDP` at the required weak endpoint, or produce a geometric counterexample showing that it does not. PF-204 and PF-183 remain independent alternative gates.