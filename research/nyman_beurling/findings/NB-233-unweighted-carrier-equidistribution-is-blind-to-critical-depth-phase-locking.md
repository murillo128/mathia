# NB-233 — Unweighted carrier equidistribution is blind to critical depth-phase locking

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + DEPTH-PHASE-LOCKING + CARRIER-PHASE-MARGINAL-BLINDNESS + EXACT-FORD-SCALE + NB-231/NB-232-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-232` shows that global pair correlation can average away the carrier-critical packets left by `NB-231`. That still leaves a seemingly stronger local possibility: perhaps one can control the carrier phases

\[
\theta_\rho=X(\gamma-t)\pmod{2\pi}
\]

inside the actual `1/H` window and prove that they are equidistributed.

Unweighted phase equidistribution is still not enough. In the same conservative regime

\[
Q=\log(10+|t|),\qquad L=\log Q,\qquad R=Q^{2/3}L^{1/3},
\]

\[
Y=\frac XR\to Y_*\in(0,\infty),\qquad
J_0=\frac RH\to\infty,\qquad J_0\le L,
\]

one can build an abstract packet with `M~delta J_0` points whose carrier phases are the complete `M`-th roots of unity. Consequently

\[
\boxed{
\frac1M\sum_{j=1}^M e^{ik\theta_j}=0
\qquad (1\le |k|<M),
}
\]

so every nontrivial unweighted Fourier mode below the packet size vanishes **exactly**. Nevertheless, by correlating the horizontal Ford depth with phase through

\[
YD_j-\log J_0=w-\varepsilon\cos\theta_j,
\]

the exact signed residue remains bounded away from zero.

The missing statistic is therefore not phase discrepancy by itself. It is a **marked depth--phase statistic**: the first carrier Fourier coefficient after weighting each zero by its Ford damping (and ultimately by the full profile coefficient). The transition layer can be harmless only if actual zeta zeros exhibit decorrelation between normalized depth and carrier phase, or if an equivalent arithmetic theorem controls that weighted coefficient directly.

This is again a matched spectral control, not a construction of actual zeta zeros.

## 1. Exact carrier and a roots-of-unity phase packet

Keep the `NB-231` profile

\[
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\]

with fixed `r>0`, nonzero real `phi>=0` in `C_c^infty((0,1))`, and

\[
F(z)=\int_0^1\phi(y)e^{izy}\,dy,
\qquad F(0)>0.
\]

For a zero `rho=beta+i gamma`, write

\[
D_\rho=R(1-\beta),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta).
\]

The exact residue coefficient is

\[
L_{X,H}(v_\rho)
=
 e^{-r}e^{-YD_\rho}
 e^{iX(\gamma-t)}F(Hv_\rho).
\tag{1}
\]

Fix a positive integer `q` as in `NB-231`. Choose fixed `epsilon>0` sufficiently small. After `epsilon` is fixed, choose a fixed `delta>0` sufficiently small, and put

\[
M=\lfloor\delta J_0\rfloor.
\tag{2}
\]

For all sufficiently large `Q`, `M>=3`. Define

\[
\theta_j=\frac{2\pi j}{M},
\qquad 1\le j\le M,
\tag{3}
\]

and choose ordinates

\[
\gamma_j
=t+\frac{2\pi qj+\theta_j}{X}.
\tag{4}
\]

Then

\[
\boxed{
e^{iX(\gamma_j-t)}=e^{i\theta_j}.
}
\tag{5}
\]

The vertical spacing is

\[
\gamma_{j+1}-\gamma_j
=
\frac{2\pi q+2\pi/M}{X}
\asymp_{Y_*,q}\frac1R,
\tag{6}
\]

and the whole packet still occupies only a fixed small part of the profile window:

\[
H|\gamma_M-t|
\le
\frac{2\pi q}{Y}\frac{M}{J_0}
+
\frac{2\pi}{YJ_0}
=
O_{Y_*,q}(\delta)+o(1).
\tag{7}
\]

The roots-of-unity identity gives, exactly,

\[
\boxed{
\sum_{j=1}^M e^{ik\theta_j}=0
\qquad
(1\le |k|<M).
}
\tag{8}
\]

Thus the packet is not merely small in one phase discrepancy observable. Its full unweighted phase marginal annihilates every Fourier mode of order below `M`.

## 2. Lock Ford depth to phase inside the critical transition layer

Let `w=w(Q)` satisfy `|w|<=W` for a fixed `W`, and define

\[
D_j
=
\frac{\log J_0+w-\varepsilon\cos\theta_j}{Y}.
\tag{9}
\]

Put abstract packet zeros at

\[
\rho_j=1-\frac{D_j}{R}+i\gamma_j.
\tag{10}
\]

Every point remains in the same bounded transition layer because

\[
\boxed{
YD_j-\log J_0
=w-\varepsilon\cos\theta_j=O(1).
}
\tag{11}
\]

Moreover `D_j->infinity` uniformly and the depth spread is only `O(1)`. The Ford damping is

\[
\boxed{
e^{-YD_j}
=
\frac{e^{-w}}{J_0}e^{\varepsilon\cos\theta_j}.
}
\tag{12}
\]

This bounded depth modulation is enough to undo the cancellation in (8). Set

\[
A_M(\varepsilon)
=
\frac1M\sum_{j=1}^M
 e^{\varepsilon\cos\theta_j}e^{i\theta_j}.
\tag{13}
\]

For fixed small `epsilon`, Taylor expansion is uniform in `M`:

\[
e^{\varepsilon\cos\theta}
=1+\varepsilon\cos\theta+O(\varepsilon^2).
\]

Using (8) for `k=1,2`,

\[
\frac1M\sum_j e^{i\theta_j}=0,
\]

and

\[
\frac1M\sum_j \cos\theta_j\,e^{i\theta_j}
=
\frac12\frac1M\sum_j(1+e^{2i\theta_j})
=
\frac12.
\]

Hence

\[
\boxed{
A_M(\varepsilon)
=
\frac\varepsilon2+O(\varepsilon^2).
}
\tag{14}
\]

Choose `epsilon` once so small that

\[
\Re A_M(\varepsilon)\ge\frac\varepsilon4
\tag{15}
\]

for every `M>=3`.

This already identifies the correct observable. If

\[
d_j:=YD_j-\log J_0,
\]

then the unweighted phase measure has zero low Fourier coefficients, while the first Fourier coefficient of the depth-weighted measure

\[
\nu_{J_0}
=
\frac1{J_0}\sum_{j=1}^M e^{-d_j}\delta_{\theta_j}
\tag{16}
\]

satisfies

\[
\widehat\nu_{J_0}(1)
=
\frac{M}{J_0}e^{-w}A_M(\varepsilon)
\to
\delta e^{-w}
\left(\frac\varepsilon2+O(\varepsilon^2)\right),
\tag{17}
\]

which is nonzero.

## 3. The full profile does not restore cancellation

Equation (17) would be insufficient if the exact profile `F(Hv_rho)` destroyed the weighted harmonic. It does not.

From (7), the real parts of all profile arguments satisfy

\[
|H(\gamma_j-t)|=O_{Y_*,q}(\delta)+o(1).
\tag{18}
\]

Their imaginary parts satisfy, uniformly in `j`,

\[
H(\sigma_X-\beta_j)
=
\frac{r}{YJ_0}+\frac{D_j}{J_0}
=o(1),
\tag{19}
\]

because `D_j=O(log J_0)`.

Since `F` is continuous at zero, after fixing `epsilon` we may choose `delta` sufficiently small that for all sufficiently large `Q`,

\[
\sup_{1\le j\le M}
|F(Hv_{\rho_j})-F(0)|
\le
\frac{\varepsilon F(0)}{16e^\varepsilon}.
\tag{20}
\]

Insert (5), (12), and (20) into (1). The packet residue is

\[
\mathcal R
=
\frac{e^{-r-w}}{J_0}
\sum_{j=1}^M
 e^{\varepsilon\cos\theta_j}
 e^{i\theta_j}
 F(Hv_{\rho_j}).
\tag{21}
\]

Replacing `F(Hv_rho_j)` by `F(0)` produces an error bounded by

\[
\frac{e^{-r-w}M}{J_0}
 e^\varepsilon
\frac{\varepsilon F(0)}{16e^\varepsilon}
=
\frac{e^{-r-w}M}{J_0}
\frac{\varepsilon F(0)}{16}.
\tag{22}
\]

The main term has real part at least

\[
\frac{e^{-r-w}M}{J_0}
\frac{\varepsilon F(0)}4.
\tag{23}
\]

Therefore

\[
\boxed{
\liminf_{Q\to\infty}
\Re\mathcal R
\ge
\frac{3\delta\varepsilon F(0)}{16}
 e^{-r-W}
>0.
}
\tag{24}
\]

The exact unweighted phase marginal can thus be perfectly Fourier-flat while the exact signed Ford residue is order one.

## 4. The packet obeys the same audited population constraints

The construction changes only a bounded amount of horizontal depth relative to `NB-231`. Its population and spacing checks therefore survive intact.

First,

\[
M\asymp J_0\le L,
\qquad
D_j=O(\log L),
\tag{25}
\]

so the packet remains inside the same conservative `O(L)` growing-density allowance used in `NB-225` and `NB-231`. Since `D_j->infinity`, it eventually lies to the left of every fixed normalized-depth zero-free boundary used there.

Second, (6) gives spacing `Theta(1/R)`. A Bellotti disk of radius `K/R` therefore meets at most `O(K)` consecutive packet points once the fixed `q` is chosen as in `NB-231`. The bounded `O(1)` modulation of horizontal depths cannot increase that vertical count.

Third, `M=O(L)=o(Q)`, so ordinary local zero counting leaves ample room. Functional-equation reflections and conjugates may be added exactly as in `NB-225` and `NB-231`; their near-one contribution at the selected positive height is harmless for the same reason as before.

Finally, the sparse-height insertion used in `NB-232` may be repeated with these packets: their cardinality is unchanged up to constants, so the same `A(T)log T+A(T)^2=o(T log T)` stability argument keeps them invisible to the globally normalized Montgomery statistic. The new obstruction is stronger in a different direction: even a **local theorem about the unweighted carrier-phase marginal of each packet window** would not by itself control (24).

As before, none of these compatibility checks asserts that actual zeta zeros realize the packet.

## 5. Representation audit and prior-art boundary

The algebra behind the counterexample is representation-general. An equidistributed phase marginal can have a nonzero weighted Fourier coefficient whenever the weight is correlated with phase. Here the source-specific content is the exact identification of the mark:

\[
\boxed{
d=YD-\log J_0,\qquad \text{weight }e^{-d},
}
\tag{26}
\]

which is forced by Ford damping at the carrier-width transition.

The prior-art audit found the expected neighboring literature rather than this local marked observable. Montgomery-type pair-correlation work is primarily vertical. Recent work of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (`arXiv:2501.14545`) and Goldston--Lee--Schettler--Suriajaya (`arXiv:2503.15449`) shows that pair-correlation methods can also constrain horizontal zero distribution under suitable hypotheses or conjectures. Those results reinforce that horizontal information can interact with spacing statistics, but they do not provide the uniform short-window, carrier-frequency, depth-marked coefficient required by (24).

No external theorem is load-bearing for (8)--(24): the construction uses only roots of unity, a first-order Taylor expansion, continuity of the already-defined profile, and the same audited zeta population inputs as `NB-231`. Therefore `SOURCES.md` acquires no new dependency.

The scope is deliberately narrow. This finding does **not** exclude a theorem controlling carrier phases separately in every thin depth slice; such a theorem would detect the locking in (9). It does not exclude a direct explicit-formula estimate for the weighted sum, and it does not establish any new fact about the actual zeros of zeta. It only shows that the marginal phase statistic is mathematically the wrong projection of the transition layer.

## 6. The surviving target is a marked local carrier coefficient

`NB-232` left a local depth-conditioned carrier statistic as the likely missing input. The present construction shows that all three qualifiers are essential. Dropping the depth mark loses the exact information used by Ford damping even if phase equidistribution is perfect.

A natural target is therefore a uniform estimate of the form

\[
\boxed{
\frac1{J_0}
\sum_{\substack{
|\gamma-t|\lesssim1/H\\
|YD_\rho-\log J_0|\le C}}
 e^{-(YD_\rho-\log J_0)}
 e^{iX(\gamma-t)}
 \Psi_\rho
=o(1),
}
\tag{27}
\]

where `Psi_rho` retains the bounded profile information needed by the exact residue. An equivalent theorem could instead show that, uniformly in every carrier-sized window, normalized depth and carrier phase become sufficiently decorrelated that the first marked Fourier coefficient vanishes.

Pure phase discrepancy

\[
\sum e^{iX(\gamma-t)}=o(J_0)
\]

is not enough: the construction makes it exactly zero while (24) stays positive. Pure depth density is not enough by `NB-231`, and global pair correlation is not enough by `NB-232`. The surviving source question is genuinely about the **joint empirical law of depth and carrier phase** at the Ford transition.

The destination bridge remains separate. Even a theorem proving (27) would still need to be converted into a quantitative Nyman--Beurling distance statement.

## Conclusion

At the sharp carrier-width transition, the Ford damping is a mark attached to each zero, not a scalar common to the whole depth layer. A roots-of-unity packet can make every unweighted carrier Fourier mode below its size vanish exactly while a bounded correlation

\[
YD-\log J_0=w-\varepsilon\cos\theta
\]

turns the first **depth-weighted** mode into an order-one exact residue.

The missing actual-zeta input is therefore more specific than local phase equidistribution. It must control the joint depth--phase distribution, or directly bound the marked carrier coefficient that the exact Ford residue consumes.