# PF-302 — bidirectional pant attenuation has infinite intrinsic mass

**Status:** `EXACT-DERIVED + VARIATIONAL + POSITIVE/ROUTE-NARROWING`.

PF-298--PF-301 leave the constant-channel accumulation problem at a sharp but apparently undecided endpoint. For the `n`th one-cusp pant core the exact constant response is a large conductance edge `c_n` with two positive shifted-killing coefficients `\kappa_{n,L},\kappa_{n,R}`. Each relative killing

\[
r_{n,L}:=\frac{\kappa_{n,L}}{c_n},
\qquad
r_{n,R}:=\frac{\kappa_{n,R}}{c_n}
\]

is only known a priori to be `O(s_n)`, where `s_n` is the exact tight-pant seam scale. PF-301 therefore correctly leaves the directional intrinsic attenuation masses open.

There is nevertheless a one-sided conclusion strong enough to close the **bidirectional** scalar-survival alternative. PF-216 gives a uniform positive lower bound for the equal-sign pant energy, while a direct distance-cutoff trial gives an upper bound `E_{-,n}\lesssim L_n/s_n` for the opposite-sign pant energy. Since

\[
\kappa_{n,L}+\kappa_{n,R}=E_{+,n},
\qquad
4c_n=E_{-,n}-E_{+,n},
\]

this implies

\[
\boxed{
r_{n,L}+r_{n,R}\gtrsim \frac{s_n}{L_n}.}
\]

The prime mesh forces the right side to have divergent sum. Quantitatively,

\[
\boxed{
\sum_{n\le M}\frac{s_n}{L_n}
\gtrsim \log\log p_M-O(1),
}
\]

so

\[
\boxed{
\sum_n(r_{n,L}+r_{n,R})=\infty.
}
\]

Equivalently, the PF-301 attenuation density obtained by adding the two directional constant-channel densities is not in `L^1` of the intrinsic prime coordinate. The product of the two scalar directional transmissions therefore vanishes:

\[
\boxed{
\prod_n
\theta_{n,L\to R}\theta_{n,R\to L}=0.
}
\]

Hence both scalar directions cannot retain positive infinite-depth survival. At least one of the two directional relative-killing series diverges, and the scalar round-trip channel is necessarily extinguished. This does **not** determine which fixed direction carries the divergent mass, does not make the constant channel invariant under the full boundary response, and does not solve the physical `P/H` return/reassembly problem in the accepted source-weighted-return clue.

## Claim

Let `E_n` be the PF-205/PF-216 one-cusp pant core between the two natural-width artificial seam boundaries `\Sigma_{n,L}` and `\Sigma_{n,R}`. On constant boundary data write

\[
M_n=
\begin{pmatrix}A_n&B_n\\B_n&C_n\end{pmatrix}
=
c_n
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
+
\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\tag{1}
\]

with `c_n=-B_n>0` as in PF-298. Put

\[
E_{+,n}:=E_n(1,1),
\qquad
E_{-,n}:=E_n(1,-1).
\tag{2}
\]

Then after a finite head there are constants independent of `n` such that

\[
\boxed{
0<c_0\le E_{+,n}\le2\pi,
\qquad
E_{-,n}\le C\frac{L_n}{s_n}.
}
\tag{3}
\]

The first two bounds are PF-216/PF-298. The new variational upper bound in (3) implies

\[
\boxed{
\frac{\kappa_{n,L}+\kappa_{n,R}}{c_n}
\ge c\frac{s_n}{L_n}.
}
\tag{4}
\]

For the exact prime mesh,

\[
\boxed{
\sum_n\frac{s_n}{L_n}=\infty,
}
\tag{5}
\]

indeed the partial sums dominate a positive constant times `\log\log p_M`. Consequently

\[
\boxed{
\sum_n\left(
\frac{\kappa_{n,L}}{c_n}
+
\frac{\kappa_{n,R}}{c_n}
\right)=\infty.
}
\tag{6}
\]

If

\[
\theta_{n,L\to R}=\frac{c_n}{c_n+\kappa_{n,R}},
\qquad
\theta_{n,R\to L}=\frac{c_n}{c_n+\kappa_{n,L}},
\tag{7}
\]

are the two PF-298 scalar transmissions, then

\[
\boxed{
\prod_n\theta_{n,L\to R}\theta_{n,R\to L}=0.
}
\tag{8}
\]

In particular at least one of the two one-direction products vanishes.

## 1. A distance cutoff gives `E_- \lesssim L/s`

Let

\[
\delta_n:=\operatorname{dist}(\Sigma_{n,L},\Sigma_{n,R}).
\tag{9}
\]

PF-216's natural-width geometry, after the fixed admissible shrinking of the strip parameter used there, gives

\[
\boxed{\delta_n\asymp s_n.}
\tag{10}
\]

Indeed the original cuffs are separated by `s_n`; the two pant-facing artificial boundaries are normal offsets by

\[
\rho_j=\operatorname{arsinh}(w_j)=O(P_j^{-1}),
\]

and PF-216 uses the elementary lower scale `s_n\gtrsim P_n^{-1}` to make those offsets a fixed small fraction of the narrow corridor.

Define the Lipschitz trial function

\[
u_n(x)
:=1-2\min\left\{\frac{d(x,\Sigma_{n,L})}{\delta_n},1\right\}.
\tag{11}
\]

It has trace `+1` on `\Sigma_{n,L}` and trace `-1` on `\Sigma_{n,R}` because every point of the latter has distance at least `\delta_n` from the former. Moreover `|u_n|\le1`, and almost everywhere

\[
|\nabla u_n|\le\frac2{\delta_n},
\]

with nonzero gradient only in the `\delta_n`-neighborhood of `\Sigma_{n,L}`.

The length of `\Sigma_{n,L}` is `L_n\cosh\rho_n\asymp L_n`. Normal flow from that hypercycle has uniformly bounded Jacobian on a distance `\delta_n=o(1)`. Even if the normal map ceases to be injective, the area formula only overcounts the image, so

\[
\boxed{
\operatorname{Area}\{d(x,\Sigma_{n,L})<\delta_n\}
\le C L_n\delta_n.
}
\tag{12}
\]

The whole pant core has area at most `2\pi`. The variational characterization of the positive shifted DtN energy therefore gives

\[
\begin{aligned}
E_{-,n}
&\le
\int_{E_n}(|\nabla u_n|^2+|u_n|^2)\,d\mu\\
&\le
\frac4{\delta_n^2}\,C L_n\delta_n+2\pi\\
&\le C\frac{L_n}{s_n},
\end{aligned}
\tag{13}
\]

which is the new estimate in (3). This bound is deliberately crude: it does not claim the sharp asymptotic of the antisymmetric pant energy. Its role is only to prevent the conductance from growing faster than `L_n/s_n`.

## 2. Equal-sign mass converts the capacity bound into relative killing

PF-216 proves the uniform positive floor

\[
E_{+,n}\ge c_0>0,
\tag{14}
\]

while PF-298 identifies

\[
E_{+,n}=\kappa_{n,L}+\kappa_{n,R}.
\tag{15}
\]

From (1)--(2),

\[
E_{-,n}=4c_n+\kappa_{n,L}+\kappa_{n,R},
\]

hence

\[
4c_n=E_{-,n}-E_{+,n}\le E_{-,n}.
\tag{16}
\]

Combining (13)--(16) yields

\[
\frac{\kappa_{n,L}+\kappa_{n,R}}{c_n}
\ge
\frac{4c_0}{E_{-,n}}
\ge c\frac{s_n}{L_n},
\tag{17}
\]

which proves (4).

This is exactly the information missing from the one-sided PF-298 bound. PF-298 says each relative killing is at most `Cs_n`; (17) says the **sum of the two directional relative killings cannot be arbitrarily smaller than `s_n/L_n`**.

## 3. The prime mesh makes `sum s_n/L_n` diverge

Use PF-299 notation

\[
P_n=p_{n-1},
\qquad
g_n=p_n-P_n,
\qquad
h_n=F(p_n)-F(P_n),
\qquad
s_n=\frac{h_n+h_{n+1}}2.
\tag{18}
\]

PF-216 gives the two-sided logarithmic cuff scale, in particular

\[
L_n\le C\log P_n
\tag{19}
\]

on the tail. PF-299/PF-107 give

\[
h_n=\frac{g_n}{P_n}(1+o(1)),
\tag{20}
\]

so for all sufficiently large `n`,

\[
\frac{s_n}{L_n}
\ge c\frac{g_n}{P_n\log P_n}.
\tag{21}
\]

The right side has a useful exact integral comparison that does not require a prime number theorem. Since `x\mapsto1/(x\log x)` is decreasing,

\[
\frac{g_n}{P_n\log P_n}
\ge
\int_{P_n}^{p_n}\frac{dx}{x\log x}.
\tag{22}
\]

The intervals `[P_n,p_n]=[p_{n-1},p_n]` concatenate. Therefore

\[
\sum_{n=N}^{M}\frac{s_n}{L_n}
\ge
c\int_{p_{N-1}}^{p_M}\frac{dx}{x\log x}
=
c\bigl(\log\log p_M-\log\log p_{N-1}\bigr),
\tag{23}
\]

which proves (5) and gives the announced quantitative lower growth.

This strengthens PF-299's bare `\ell^1` seam divergence in a direction relevant to the actual pant matrix: even after paying the extra logarithmic cuff factor introduced by the crude capacity upper bound, the prime-gap increments still accumulate infinitely.

## 4. The combined PF-301 attenuation density is not integrable

Set

\[
r_{n,L}=\frac{\kappa_{n,L}}{c_n},
\qquad
r_{n,R}=\frac{\kappa_{n,R}}{c_n}.
\tag{24}
\]

Equations (17),(23) give

\[
\sum_n(r_{n,L}+r_{n,R})=\infty.
\tag{25}
\]

PF-298 also gives `r_{n,L},r_{n,R}=O(s_n)`, hence both tend to zero. Consequently, after a finite head,

\[
\log(1+r_{n,L})+\log(1+r_{n,R})
\ge\frac12(r_{n,L}+r_{n,R}).
\tag{26}
\]

Using (7),

\[
\prod_{n=N}^{M}
\theta_{n,L\to R}\theta_{n,R\to L}
\le
C\exp\left[-c\sum_{n=N}^{M}\frac{s_n}{L_n}\right]
\le
C(\log p_M)^{-c'},
\tag{27}
\]

for some positive constants. This proves (8).

Equivalently, apply PF-301 separately to the bounded directional densities

\[
b_{n,L}=\frac{r_{n,L}}{s_n},
\qquad
b_{n,R}=\frac{r_{n,R}}{s_n}.
\tag{28}
\]

For the same intrinsic hat basis `\psi_n`, the combined density

\[
B_N^{\Sigma}
=\sum_{n\le N}(b_{n,L}+b_{n,R})\psi_n
\tag{29}
\]

satisfies the exact mass identity

\[
\int B_N^{\Sigma}(t)\,dt
=\sum_{n\le N}(r_{n,L}+r_{n,R})
\longrightarrow\infty.
\tag{30}
\]

Thus the **combined** directional constant-channel attenuation is not `L^1` in intrinsic prime distance. PF-301's arbitrary-oscillation freedom cannot make both directional masses finite.

## 5. Consequence for the source/escape investigation

This removes one scalar escape hatch but does not promote the scalar model to the physical response. The neighboring pant is locally almost conservative because each `r_{n,\pm}\to0`, yet the two directions together accumulate enough positive shifted killing to extinguish scalar round trips at infinite depth. Therefore the source-weighted-return investigation should no longer treat “both scalar pant directions have summable killing” as a live explanation for recurrence.

Three harder possibilities remain untouched:

- the divergent mass may live predominantly in only one fixed orientation, so this finding does not prove both one-way products vanish;
- nonconstant boundary modes can screen/rearrange the constant compression, as PF-217 already demonstrates for a different raw coercivity claim;
- the actual PF-290 `P/H` mixed Riesz response still needs its genuine return/reassembly equation, source forcing, signed cancellation, and any residual physical-high term.

In particular, (27) is an attenuation statement, not a Green-potential bound. A product decaying only like an unspecified power of `\log p_M` need not make the source-weighted return potential summable. The accepted clue therefore remains open, but its scalar calibration is strictly narrower.

## Prior-art and novelty audit

The ingredients used in the new step are classical: variational characterization of Dirichlet-to-Neumann energy, Lipschitz distance cutoffs/capacity estimates, and the resistor-network interpretation of narrow elliptic channels. PF-216 already audits nearby DtN/network literature, including Borcea--Gorb--Wang's thin-gap network asymptotics and Wentworth's Riemann-surface DtN degeneration with a graph/external-potential structure. A targeted literature search found those general mechanisms but no statement identifying the prime-flute quantity in (17)--(30).

No novelty is claimed for the cutoff estimate or network algebra. The project-specific content is the combination of the **actual PF-205 pant geometry**, PF-216's positive equal-sign energy floor, PF-298's exact killed-edge decomposition, and PF-299's ordered-prime mesh to force nonintegrability of the combined directional scalar attenuation.

## Decisive falsification/audit test

The load-bearing geometric step is (12)--(13). Audit the actual PF-205 artificial boundary placement and verify directly that `\delta_n\asymp s_n` and that the inward normal `\delta_n`-tube of `\Sigma_{n,L}` has area `O(L_n\delta_n)` with constants uniform on the tail. This can be checked in the same Fermi coordinates already used by PF-205/PF-215/PF-216. If either comparison fails, the new lower bound (17) must be withdrawn or weakened.

Independently, a finite-pant numerical DtN calculation can compare `E_{-,n}` with `L_n/s_n` and verify the matrix identities in (15)--(17), but numerical agreement is not needed for the proof. Any stronger claim that both directional products vanish requires a new lower bound controlling the split between `\kappa_{n,L}` and `\kappa_{n,R}`; (6) alone does not provide it.