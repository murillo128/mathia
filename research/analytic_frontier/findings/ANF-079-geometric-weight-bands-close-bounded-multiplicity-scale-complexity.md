# ANF-079 — geometric weight bands close bounded multiplicity-scale complexity

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + GEOMETRIC-WEIGHT-DECOMPOSITION + SUPPORT-UNBOUNDED + OCCUPANCY-MAGNITUDE-UNBOUNDED + FINITE-SCALE-COMPLEXITY-CLOSED + EXPONENTIAL-CAP-COROLLARY`. `ANF-077` reduces arbitrary real multiplicity to a nested-set excess defect, while `ANF-078` closes every prescribed upper bound on the largest site multiplicity by Bernoulli thinning. The absolute size of the multiplicities is not, however, the correct remaining parameter. A geometric decomposition shows that only the **number of occupied multiplicity scales** enters the central-notch loss.

Fix `rho>1`. For positive integer occupancies `k_1,...,k_r`, define the occupied geometric bands

\[
\mathcal B_\rho(k)
:=
\left\{
j\ge0:
\exists i\text{ with }\rho^j\le k_i<\rho^{j+1}
\right\},
\qquad
D_\rho(k):=|\mathcal B_\rho(k)|.
\tag{1}
\]

Then for every fixed integer `D>=1` there is a central-notch profile

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad
F_s=\widehat J_s,
\tag{2}
\]

and a positive amplitude `t` such that **every finite real multiset** whose multiplicities satisfy

\[
D_\rho(k)\le D
\tag{3}
\]

obeys the universal affine inequality

\[
\boxed{
\sigma\ge 2N-tE_{F_s}(k;X),
}
\tag{4}
\]

while

\[
\boxed{
2-tC(J_s)>2-C_{\rm MT}.
}
\tag{5}
\]

There is no bound on the number of support sites and, importantly, **no bound on the largest multiplicity**. The occupied bands may lie arbitrarily far apart. Thus a two-scale occupancy vector with values near `1` and `10^{1000}`, for example, is still in a fixed-`D` class.

For bounded occupancies this gives a much stronger quantitative corollary than `ANF-078`. If `1<=k_i<=K`, then

\[
D_\rho(k)\le1+\lfloor\log_\rho K\rfloor.
\tag{6}
\]

With the notch width `eta` tending to zero and `L^{-1}=o(eta)`, one may therefore close occupancy caps of size

\[
\boxed{
K\le \exp\!\left(\frac{c}{\eta}\right)
}
\tag{7}
\]

for every fixed

\[
\boxed{
c<\frac{c_0}{8eC_{\rm MT}}=0.03127404138\ldots,}
\tag{8}
\]

by taking the optimal geometric ratio `rho=sqrt(e)` and then choosing the notch amplitude `s>0` sufficiently small. `ANF-078` obtained only an `O(eta^{-1})` occupancy ceiling from the same near-face input. The remaining real-multiplicity obstruction must therefore occupy **many multiplicative scales**, not merely attain a large maximum multiplicity.

## 1. The triangular notch has a nonnegative spatial transform

Retain the notation of `ANF-034` and `ANF-078`. The notch is

\[
\phi_\eta(\alpha)
=
b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\tag{9}
\]

and its spatial Fourier transform is explicitly

\[
\boxed{
\Phi_\eta(x)
:=\widehat\phi_\eta(x)
=
b_\eta\eta
\left(
\frac{\sin(\pi\eta x)}{\pi\eta x}
\right)^2
\ge0.
}
\tag{10}
\]

This elementary positivity is the extra piece that makes a multiplicative-scale decomposition useful: within one weight band, replacing all coefficients by the top of the band can only increase the `Phi_eta` energy.

For the Montgomery--Taylor kernel write

\[
R:=R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
R(0)=1.
\tag{11}
\]

For a weighted real configuration put

\[
W_2:=\sum_i k_i^2,
\qquad
u:=\frac{E_R(k;X)}{W_2}-1\ge0.
\tag{12}
\]

The nonnegativity in (12) is pointwise, not merely positive-definiteness: every off-diagonal term of the Montgomery--Taylor energy is nonnegative.

Finally recall from `ANF-078` the simple-support central-mass estimate

\[
E_{\Phi_\eta}(Y)
\le
|Y|\left[
b_\eta B_{\eta,L}+E_L(\Delta(Y))
\right],
\tag{13}
\]

where

\[
B_{\eta,L}
=
\frac4{c_0}\left(\eta+\frac4L\right),
\qquad
E_L(u)
=
2\sqrt{a_Lu(1+u)}+a_Lu,
\tag{14}
\]

and

\[
\Delta(Y)
:=
\frac{E_R(Y)}{|Y|}-1\ge0.
\tag{15}
\]

No small-excess assumption is present in (13).

## 2. One geometric band costs only its squared scale

For every occupied band `j in mathcal B_rho(k)`, put

\[
C_j
:=
\{i:\rho^j\le k_i<\rho^{j+1}\},
\qquad
m_j:=\rho^j,
\qquad
n_j:=|C_j|.
\tag{16}
\]

Let `S_j(alpha)` be the exponential polynomial contributed by that band,

\[
S_j(\alpha)
:=
\sum_{i\in C_j}k_i e^{2\pi i\alpha x_i}.
\tag{17}
\]

Since `Phi_eta>=0` in physical space and `k_i<rho m_j` on `C_j`,

\[
\begin{aligned}
E_{\Phi_\eta}(k;C_j)
&=
\sum_{i,l\in C_j}
k_ik_l\Phi_\eta(x_i-x_l)\\
&\le
\rho^2m_j^2E_{\Phi_\eta}(C_j).
\end{aligned}
\tag{18}
\]

Applying (13) to the simple set of sites in this band gives

\[
\boxed{
E_{\Phi_\eta}(k;C_j)
\le
\rho^2m_j^2n_j
\left[
b_\eta B_{\eta,L}+E_L(\Delta_j)
\right],
}
\tag{19}
\]

with `Delta_j:=Delta(C_j)`.

The cross-band terms are handled in frequency space. If `d=D_rho(k)` is the number of nonempty bands, Cauchy--Schwarz gives pointwise

\[
\left|\sum_jS_j(\alpha)\right|^2
\le
d\sum_j|S_j(\alpha)|^2.
\tag{20}
\]

Since `phi_eta>=0`, integration yields

\[
E_{\Phi_\eta}(k;X)
\le
d\sum_jE_{\Phi_\eta}(k;C_j).
\tag{21}
\]

Thus cross-scale interference costs only the **number of occupied scales** `d`; it does not see their absolute indices or the ratio between the smallest and largest occupied bands.

## 3. Global Montgomery--Taylor excess controls all within-band defects

Set

\[
w_j:=m_j^2n_j,
\qquad
W_0:=\sum_jw_j.
\tag{22}
\]

Because `k_i>=m_j` in band `j`,

\[
W_0\le W_2.
\tag{23}
\]

Moreover, using `R>=0`, the global weighted Montgomery--Taylor excess controls the sum of all simple-set excesses inside the bands:

\[
\begin{aligned}
\sum_jw_j\Delta_j
&=
2\sum_jm_j^2
\sum_{\{i,l\}\subset C_j}R(x_i-x_l)\\
&\le
2\sum_{i<l}k_ik_lR(x_i-x_l)\\
&=
W_2\nu.
\end{aligned}
\tag{24}
\]

Call the left side `U`. The special form of `E_L` lets the one-variable near-face estimate survive summation over bands. Weighted Cauchy--Schwarz gives

\[
\begin{aligned}
\sum_jw_j\sqrt{\Delta_j(1+\Delta_j)}
&\le
\sqrt{
\left(\sum_jw_j\Delta_j\right)
\left(\sum_jw_j(1+\Delta_j)\right)
}\\
&\le
W_2\sqrt{\nu(1+\nu)}.
\end{aligned}
\tag{25}
\]

Together with (14) and (24),

\[
\boxed{
\sum_jw_jE_L(\Delta_j)
\le
W_2E_L(\nu).
}
\tag{26}
\]

Combining (19), (21), (23), and (26) proves the weighted central-mass bound

\[
\boxed{
E_{\Phi_\eta}(k;X)
\le
\rho^2dW_2
\left[
b_\eta B_{\eta,L}+E_L(\nu)
\right].
}
\tag{27}
\]

This is the main new inequality. Compare it with the Bernoulli bound of `ANF-078`, whose loss was proportional to the maximum occupancy `K`. Here the loss is proportional only to `D_rho(k)`.

## 4. Bounded scale complexity gives a universal quadratic floor

Fix an integer `D>=1` and restrict only to occupancies with `D_rho(k)<=D`. Put

\[
\lambda:=\rho^2Ds.
\tag{28}
\]

Since

\[
F_s=R-s\Phi_\eta,
\]

(12) and (27) give

\[
\frac{E_{F_s}(k;X)}{W_2}
\ge
1+\nu
-\lambda b_\eta B_{\eta,L}
-\lambda E_L(\nu).
\tag{29}
\]

As in `ANF-078`, use

\[
E_L(u)
\le
2\sqrt{a_L}\sqrt u
+\bigl(2\sqrt{a_L}+a_L\bigr)u.
\tag{30}
\]

If

\[
\lambda\bigl(2\sqrt{a_L}+a_L\bigr)
\le\frac12,
\tag{31}
\]

then completing the square gives

\[
\nu-\lambda E_L(\nu)
\ge-2a_L\lambda^2.
\tag{32}
\]

Therefore every multiset in the class satisfies

\[
\boxed{
E_{F_s}(k;X)
\ge
q_{\rho,D}W_2,
}
\tag{33}
\]

where

\[
\boxed{
q_{\rho,D}
:=
1-ho^2D\,s b_\eta B_{\eta,L}
-2a_L\rho^4D^2s^2.
}
\tag{34}
\]

For fixed `rho,D,eta,L`, this floor is positive for all sufficiently small `s>0`.

Take

\[
t=q_{\rho,D}^{-1},
\qquad
A=2.
\tag{35}
\]

For

\[
N=\sum_i k_i,
\qquad
\sigma=\#\{i:k_i=1\},
\]

the affine slack obeys

\[
\begin{aligned}
\sigma-2N+tE_{F_s}(k;X)
&\ge
\sigma-2N+W_2\\
&=
\sum_{k_i\ge2}k_i(k_i-2)\\
&\ge0.
\end{aligned}
\tag{36}
\]

This proves (4). Notice that `A=2` here does **not** restore the zero-slack regime of `ANF-005`: after the rescaling (35), the diagonal is `tF_s(0)>1` for the parameter range below, so the normalization slack is positive.

## 5. The spectral gain beats the scale-decomposition loss

Write as in `ANF-078`

\[
\beta:=sb_\eta,
\qquad
c_\eta:=1+\frac{\eta^2}{3}.
\tag{37}
\]

The exact central-notch cost is

\[
C(J_s)
=C_{\rm MT}-\beta c_\eta.
\tag{38}
\]

Define the scale-complexity margin

\[
\boxed{
G_{\rho,D}(\eta,L)
:=
c_\eta
-\rho^2D\,C_{\rm MT}B_{\eta,L}.
}
\tag{39}
\]

For every fixed `rho>1` and `D`, one may first choose `eta>0` sufficiently small and then `L` sufficiently large so that

\[
G_{\rho,D}(\eta,L)>0,
\tag{40}
\]

because `c_eta->1` whereas `B_{eta,L}->0` under that ordered choice.

After fixing such `rho,D,eta,L`, choose `s>0` small enough to satisfy `s<1`, (31), `q_{rho,D}>0`, and

\[
\boxed{
2a_LC_{\rm MT}\rho^4D^2s
<
b_\eta G_{\rho,D}(\eta,L).
}
\tag{41}
\]

A direct expansion then gives

\[
\begin{aligned}
C(J_s)-C_{\rm MT}q_{\rho,D}
&=
-sb_\eta G_{\rho,D}(\eta,L)
+2a_LC_{\rm MT}\rho^4D^2s^2\\
&<0.
\end{aligned}
\tag{42}
\]

Hence

\[
\boxed{
\frac{C(J_s)}{q_{\rho,D}}
<C_{\rm MT},
}
\tag{43}
\]

which is equivalent to (5). Thus bounded multiplicity-scale complexity is closed by a genuine strict Montgomery--Taylor improvement, not just by a feasibility estimate.

The result includes much more than bounded maximum occupancy. For example, if all occupancies lie in any fixed collection of `D` geometric bands, those bands may drift to infinity or separate from one another without changing the proof. Absolute multiplicity size cancels because both the useful Montgomery--Taylor diagonal and the within-band notch loss scale quadratically.

## 6. Bounded maximum occupancy improves from linear to exponential in `1/eta`

Condition (40) is equivalent to

\[
D
<
\frac{c_\eta}
{\rho^2C_{\rm MT}B_{\eta,L}}.
\tag{44}
\]

If all multiplicities satisfy `1<=k_i<=K`, equation (6) converts this into a bound on `K`. Choose `L=L(eta)` with `L^{-1}=o(eta)`. Then

\[
B_{\eta,L}
=
\left(\frac4{c_0}+o(1)\right)\eta.
\tag{45}
\]

Therefore every fixed constant

\[
c<
\frac{c_0\log\rho}
{4\rho^2C_{\rm MT}}
\tag{46}
\]

is admissible in the sense that, for all sufficiently small `eta`, one can choose `L` and then `s>0` so that one profile closes every real multiset with

\[
K\le e^{c/\eta}.
\tag{47}
\]

The factor `log(rho)/rho^2` is maximized at

\[
\rho=\sqrt e,
\]

which gives

\[
\boxed{
\sup_{\rho>1}
\frac{c_0\log\rho}
{4\rho^2C_{\rm MT}}
=
\frac{c_0}{8eC_{\rm MT}}
=0.03127404138\ldots.
}
\tag{48}
\]

The decimal is only a numerical check; the exact constant in (48) is the result.

This exponentially enlarges the bounded-occupancy region obtained from the one-shot Bernoulli thinning of `ANF-078`. More importantly, (44) identifies the true surviving parameter: an obstruction must populate on the order of `eta^{-1}` distinct logarithmic weight scales. Merely making one site enormously multiple is insufficient.

## 7. Boundary, prior art, and decisive audit

This finding does **not** close arbitrary real multiplicities for one fixed central-notch profile. The number `D_rho(k)` is still unbounded, and the Cauchy factor in (20) is linear in that number. A surviving real obstruction can therefore escape by spreading its occupancy mass through more and more multiplicative scales. Combined with `ANF-075`, such an obstruction must also use growing real support. The remaining scalar gate is consequently narrower than the doubly growing `support x max-occupancy` description of `ANF-078`: it requires growing support **and growing logarithmic occupancy-scale complexity**.

Nor does this establish the exact `A=2,t=q_real^{-1}` three-set excess inequality left open in `ANF-077`. The present certificate uses a different explicit floor `q_{rho,D}` and pays the corresponding positive normalization slack after amplitude rescaling. It has no consequence yet for the complex one-pair gate or for RH.

Geometric/dyadic decomposition, Cauchy--Schwarz, and weighted quadratic-energy estimates are classical devices, and no novelty is claimed for those ingredients. A targeted prior-art check found the neighboring classical stability/superstability literature for pair potentials and local occupation numbers, but no theorem that supplies (27)--(43) in this finite deterministic BGSST normalization. The load-bearing analytic estimate (13) and the Montgomery--Taylor positivity are already canonical in `ANF-030`, `ANF-034`, and `ANF-078`; the Sütő/Procacci stability anchors already recorded in `SOURCES.md` remain sufficient, so no source-file change is needed.

The proof has four cheap falsification points. First, (10) must be nonnegative; it is the exact Fourier transform of the triangular tent. Second, (18) uses that nonnegativity and would fail for a generic notch shape. Third, (24) uses the stronger fact `R_MT>=0` pointwise, so the argument cannot be transplanted unchanged to an arbitrary positive-definite base kernel. Fourth, the cross-band factor in (20) is exactly the number of **nonempty** bands; replacing it by the logarithmic diameter of the weights would be unjustified when many bands are empty. With those interfaces intact, (27), (33), and the strict objective comparison (42) follow algebraically.