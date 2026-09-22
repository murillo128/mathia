# PC-398 — subcritical Kron macroscopic forms have a universal Buchstab–Riesz limit

**Status:** `ASYMPTOTIC-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` + `MATCHED-CONTROL-CLASSICALIZATION` for the nonsummable positive Riesz/Kron branch `0<alpha<1/2` opened by PC-397.

PC-397 proves that for sufficiently long polynomial primorial windows the positive simultaneous-deletion Kron correction can survive, and even diverge, when `alpha<1/2`. Its lower bound uses one affine macroscopic test mode. The stronger question is whether that surviving sector carries an arithmetic operator at leading order, or whether its whole smooth macroscopic part has a classical continuum limit.

It has a classical continuum limit. Put

\[
\beta=2\alpha\in(0,1),\qquad H=p^u,\qquad u>2,
\tag{1}
\]

let `q` be the next prime after `p`, and retain the successive-primorial boundary decomposition

\[
S=R_q(H),\qquad T=qR_p(H/q).
\tag{2}
\]

For every fixed nonzero `g in C([0,1])`, define the normalized survivor vector

\[
f_s^{(p)}=
\frac{g(s/H)}{\left(\sum_{r\in S}|g(r/H)|^2\right)^{1/2}},
\qquad s\in S.
\tag{3}
\]

Let

\[
J_\beta(y)=\int_0^1|x-y|^{-\beta}\,dx,
\qquad
(\mathcal A_\beta g)(y)=
\frac{\int_0^1|x-y|^{-\beta}g(x)\,dx}{J_\beta(y)},
\tag{4}
\]

and let the integrable Riesz Dirichlet form be

\[
\mathcal E_\beta(h)
:=\frac12\int_0^1\int_0^1
|y-z|^{-\beta}|h(y)-h(z)|^2\,dy\,dz.
\tag{5}
\]

Then the exact simultaneous-deletion correction `Delta_T` from PC-391--PC-397 satisfies

\[
\boxed{
\frac{q^2\log p}{H^{1-\beta}}
\left\langle f^{(p)},\Delta_T f^{(p)}\right\rangle
\longrightarrow
(2\pi)^{-\beta}
\frac{\omega(u-1)^2}{\omega(u)}
\frac{\mathcal E_\beta(\mathcal A_\beta g)}{\int_0^1|g(x)|^2\,dx}.
}
\tag{6}
\]

Here `omega` is Buchstab's function. Thus, after the only natural macroscopic normalization, the surviving positive Kron form is the universal nonlocal Riesz form of the normalized averaging operator `A_beta`; the rough-number arithmetic remains only in the scalar Buchstab density ratio. This is a boundary result, not a new RH mechanism.

## 1. A local upper-bound sieve supplies the missing singular-integrability control

Weak equidistribution of the rough-number clouds is not by itself enough to pass to the singular kernel `|x-y|^{-beta}`. The required extra input is a standard local consequence of the one-dimensional upper-bound linear sieve.

Fix `eta>0`. If `z` tends to infinity and `I` is any interval of consecutive integers of length `Y>=z^{1+eta}`, then

\[
\boxed{
\#\{m\in I:P^-(m)>z\}
\ll_\eta \frac{Y}{\log z},
}
\tag{7}
\]

uniformly in the position of `I`. For a translated interval one has `|I_d|=Y/d+O(1)` for squarefree `d` composed of primes at most `z`. Applying standard Rosser/linear-sieve upper weights at level `D=Y/(\log z)^3`, the sieve parameter satisfies

\[
\frac{\log D}{\log z}\ge 1+\frac\eta2
\tag{8}
\]

for large `z`; the main term is `O(Y prod_{ell<=z}(1-1/ell))=O(Y/log z)` and the total interval remainder is `O(D)=o(Y/log z)`. This is the usual dimension-one upper-bound sieve, not a new rough-number estimate.

For the survivor cloud choose a fixed `eta<u-1` and put `R_0=p^{1+eta}`. At distances below `R_0`, even the crude integer bound gives

\[
\sum_{1\le |s-t|<R_0}|s-t|^{-\beta}
\ll R_0^{1-\beta}.
\tag{9}
\]

Relative to the macroscopic star scale `H^{1-beta}/log p`, this is

\[
O\!\left(\log p\left(\frac{R_0}{H}\right)^{1-\beta}\right)=o(1).
\tag{10}
\]

On the mesoscopic annuli `R_0<=|s-t|<=epsilon H`, (7) and dyadic summation instead give an `O(epsilon^{1-beta})` fraction of the macroscopic scale. Hence the singular star sums are uniformly integrable. The same argument applies to the deleted cloud after writing `t=qm`, `L=H/q`, and choosing `0<eta<u-2`: below `R_0=p^{1+eta}` in the `m` coordinate the normalized pair contribution is

\[
O\!\left(\log p\left(\frac{R_0}{L}\right)^{1-\beta}\right)=o(1),
\tag{11}
\]

while the mesoscopic contribution below `epsilon L` is `O(epsilon^{1-beta})`.

This local-sieve truncation is the technical point that upgrades the macroscopic weak convergence used in PC-397 to convergence against the singular Riesz kernels needed for the exact limit below.

## 2. The two boundary clouds converge to Lebesgue measure with Buchstab cardinalities

PC-388 identifies the boundary sets with classical rough numbers. Fixed-parameter Buchstab asymptotics give

\[
n_S:=|S|
\sim \omega(u)\frac{H}{\log q},
\qquad
n_T:=|T|
\sim \omega(u-1)\frac{H}{q\log p},
\tag{12}
\]

because `q/p->1`. Applied to fixed subintervals, the same asymptotics imply

\[
\nu_S:=\frac1{n_S}\sum_{s\in S}\delta_{s/H}
\Longrightarrow dx,
\qquad
\nu_T:=\frac1{n_T}\sum_{t\in T}\delta_{t/H}
\Longrightarrow dx
\tag{13}
\]

on `[0,1]`.

For bounded continuous tests this is ordinary weak convergence. Equations (7)--(11) are what allow the diagonal singularity to be restored afterward. In particular, no short-interval asymptotic for rough numbers is being assumed: only a standard local upper sieve is required for uniform integrability.

## 3. The star map converges to normalized Riesz averaging

Write the exact Schur factorization from PC-391 as

\[
\Delta_T=PQP^\top,
\qquad
P=BD^{-1},
\qquad
Q=D-D(D+K)^{-1}D,
\tag{14}
\]

where `D` contains the survivor-to-deleted star degrees and `K` is the deleted-layer weighted Laplacian. For `x=P^T f^(p)`, each deleted coordinate is the normalized positive star average

\[
x_t=
\frac1{\left(\sum_{s\in S}|g(s/H)|^2\right)^{1/2}}
\frac{\sum_{s\in S}\kappa_M(|s-t|)g(s/H)}
{\sum_{s\in S}\kappa_M(|s-t|)}.
\tag{15}
\]

The normalized chord kernel from PC-390 has, uniformly on every polynomial window `d<=H=o(M)`,

\[
\kappa_M(d)
=(\tau^2+4\pi^2d^2)^{-\alpha}(1+o(1)).
\tag{16}
\]

Away from the diagonal this becomes

\[
H^\beta\kappa_M(Hr)
\longrightarrow
(2\pi)^{-\beta}|r|^{-\beta}.
\tag{17}
\]

Combine (13), the diagonal control of Section 1, and the cancellation of the common density factor between numerator and denominator of (15). Uniformly for deleted points `t/H in [0,1]`,

\[
\boxed{
\sqrt{n_S}\,x_t
\longrightarrow
h(t/H),
\qquad
h:=\frac{\mathcal A_\beta g}{\|g\|_{L^2(0,1)}}.
}
\tag{18}
\]

Thus the nontrivial macroscopic profile seen in PC-397 for `g(x)=x` is not an isolated test-vector phenomenon: `P^T` converges on every fixed continuous macroscopic observable to the classical normalized Riesz averaging operator.

## 4. The deleted-layer quadratic form has an exact continuum limit

Deleted points have the form `t=qm` with `m in R_p(L)` and `L=H/q`. Distinct deleted points are therefore at least `q` apart, so the regularizing parameter `tau` disappears uniformly on every deleted-to-deleted edge:

\[
\kappa_M(|t-t'|)
=(2\pi)^{-\beta}H^{-\beta}
\left|\frac{t-t'}H\right|^{-\beta}(1+o(1)).
\tag{19}
\]

The weighted Laplacian energy is

\[
x^TKx
=\sum_{t<t'}\kappa_M(|t-t'|)|x_t-x_{t'}|^2.
\tag{20}
\]

Using (18), the deleted empirical convergence in (13), and the pairwise uniform-integrability estimate (11), one obtains

\[
\boxed{
x^TKx
\sim
(2\pi)^{-\beta}
\frac{n_T^2}{n_S}H^{-\beta}
\mathcal E_\beta(h).
}
\tag{21}
\]

The factor `1/2` in (5) matches the unordered-pair convention in (20), so no additional factor of two occurs.

PC-397 already proves, with `A=D^{-1/2}KD^{-1/2}`, that

\[
\|A\|_{\rm op}=O\!\left(\frac{\log H}{q}\right)=o(1)
\tag{22}
\]

and consequently

\[
(1+o(1))K\preceq Q\preceq K.
\tag{23}
\]

Therefore `x^TQx=(1+o(1))x^TKx`. Substituting (12) into (21) gives

\[
\frac{n_T^2}{n_S}H^{-\beta}
\sim
\frac{\omega(u-1)^2}{\omega(u)}
\frac{H^{1-\beta}}{q^2\log p},
\tag{24}
\]

because `log q/log p->1`. Equations (21)--(24) prove (6).

## 5. The affine PC-397 mode has an exact scale, including the equality boundary

Take `g(x)=x`. Then

\[
(\mathcal A_\beta g)(0)=\frac{1-\beta}{2-\beta},
\qquad
(\mathcal A_\beta g)(1)=\frac1{2-\beta},
\tag{25}
\]

so `A_beta g` is nonconstant and

\[
\mathcal E_\beta(\mathcal A_\beta g)>0.
\tag{26}
\]

Hence PC-397's lower-bound scale is the exact asymptotic scale for this mode:

\[
\boxed{
\left\langle f^{(p)},\Delta_Tf^{(p)}\right\rangle
\sim
C_{\beta,u}
\frac{H^{1-\beta}}{q^2\log p},
\qquad C_{\beta,u}>0.
}
\tag{27}
\]

This sharpens the macroscopic threshold statement. If `u(1-beta)>2`, the affine mode diverges as already detected by PC-397. If

\[
u(1-\beta)=2,
\tag{28}
\]

then this mode tends to zero like `C_beta,u/log p`; if `u(1-beta)<2`, it vanishes polynomially faster. The same conclusion holds for every fixed macroscopic `g` for which `E_beta(A_beta g)>0`.

This is **not** an operator-norm vanishing theorem at or below (28). A sequence of test vectors concentrating on mesoscopic or arithmetic scales can evade the fixed-continuum-observable limit. The statement closes only the smooth/macroscopic sector left quantitatively unresolved by PC-397.

## 6. Prior-art and matched-control audit

The arithmetic inputs are classical. PC-388 anchors the identification with rough numbers and cites H. Halberstam and H.-E. Richert, *Sieve Methods* (Academic Press, 1974), together with Kai (Steve) Fan, *Numerically explicit estimates for the distribution of rough numbers*, Journal of Number Theory 260 (2024), 120--150, DOI `10.1016/j.jnt.2024.01.008`, arXiv:2306.03347. Equation (7) is the standard upper-bound linear-sieve estimate on a translated interval, while (12)--(13) are fixed-parameter Buchstab theory.

The Schur/Kron component is the classical framework of Dörfler--Bullo already anchored in `SOURCES.md`. The limiting energy (5) is likewise an ordinary positive nonlocal Dirichlet/Riesz form; generic graph-to-continuum convergence for nonlocal energies is established prior art, for example Y. Hafiene, J. M. Fadili and A. Elmoataz, *Continuum Limits of Nonlocal p-Laplacian Variational Problems on Graphs*, SIAM Journal on Imaging Sciences 12:4 (2019), 1772--1807, DOI `10.1137/18M1223927`. Targeted searches did not locate the exact rough-number/Kron composition in (6), but absence from search is not evidence of novelty of the continuum operator.

More decisively, (6) passes a matched-control test in the negative direction. Replace `S` and `T` by deterministic point clouds with the same two cardinality asymptotics, empirical Lebesgue limit, and a comparable mesoscopic occupancy bound. The proof is unchanged and gives the same limit. The only arithmetic data surviving at leading smooth scale are the Buchstab density constants

\[
\frac{\omega(u-1)^2}{\omega(u)}.
\tag{29}
\]

Thus the naturally renormalized macroscopic Kron sector is, in quadratic-form language, the universal operator

\[
(2\pi)^{-\beta}
\frac{\omega(u-1)^2}{\omega(u)}
\mathcal A_\beta^*\mathcal L_\beta\mathcal A_\beta,
\tag{30}
\]

where `L_beta` denotes the nonlocal operator associated with (5). This operator contains no zeta zeros, no functional-equation symmetry, no gamma factor, and no distinguished critical line.

## 7. Falsification boundary and consequence for the line

There are three load-bearing checks. First, the local sieve estimate (7) must hold uniformly on translated intervals at the stated polynomial lengths; standard linear-sieve weights give exactly that range. Second, the singular star and pair sums must be uniformly integrable; equations (9)--(11) isolate the only diagonal issue. Third, the exact Kron response must remain asymptotic to `K`; this is independently controlled by the finite-matrix estimate (22)--(23).

A finite numerical falsification test is direct: for fixed `alpha<1/2`, `u>2`, and several continuous `g`, compute the normalized form in the left side of (6). It should converge to the continuum constant in the right side, while matched near-uniform clouds with the same cardinalities should converge to the same constant. Failure after accounting for finite-size rough-number density would invalidate the derivation.

The research consequence is narrower but stronger than PC-397: **the entire fixed smooth macroscopic part of the surviving subcritical positive Kron contrast classicalizes.** Any RH-facing arithmetic signal in this branch must therefore occur below that leading continuum scale: centered rough-number fluctuations, genuinely mesoscopic/fine modes, cross-level orientation or coherence, or a nonlinear/signed observable not reproduced by matched clouds. Merely renormalizing the positive macroscopic Kron energy cannot expose a new zeta mechanism.