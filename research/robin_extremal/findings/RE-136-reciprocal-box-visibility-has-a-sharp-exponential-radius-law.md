# RE-136 — reciprocal-box visibility has a sharp exponential radius law

**Status:** `EXACT-DERIVED + QUANTITATIVE-RECIPROCAL-BOX + EXPONENTIAL-VISIBILITY-FLOOR + LOGARITHMIC-MESOSCOPIC-RADIUS + SHARP-MATCHED-CONTROL + MACROSCOPIC-WINDOW + REAL-PACKET-OBSERVABILITY + ESCAPE-COST + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-135` removes the occupancy hypothesis from reciprocal-box visibility, but its compactness proof leaves the dependence of the visibility constant on the scaled box radius `R` qualitative. That dependence is now the live quantity: a hiding packet can escape every fixed reciprocal box only by sending cancellation to scaled radii tending to infinity, so the useful question is how much suppression a radius `R` can buy.

The answer is exponential, and that scale is sharp. For the normalized positive-measure transforms underlying `RE-135`, bounded scaled spectral radius `R` forces an interval visibility floor `exp(-O_kappa(R))`. The same floor transfers to the real Robin packet while `R(U)` grows up to a sufficiently small constant multiple of `log U`. Conversely, the subset-product mechanism of `RE-133` produces simple packets of scaled radius `O(j)` with residual `exp(-Omega(j))`. Thus buying suppression `epsilon` costs radius `Omega(log(1/epsilon))`, and that dependence cannot be improved in the matched formal class.

This does **not** prove reciprocal-scale tightness for the actual zeta packet. It quantifies the only remaining escape mechanism from `RE-135`: any source-specific exterior-tail theorem that beats the exponential visibility loss would contradict macroscopic hiding.

Fix

\[
0<\kappa<\frac12,
\qquad
I_\kappa:=[1-\kappa,1],
\qquad
\mathcal K_R:=\{z\in\mathbb C:|\Re z|\le R,\ |\Im z|\le R\}.
\tag{1}
\]

For a Borel probability measure `mu` on `K_R`, put

\[
F_\mu(z):=\int_{\mathcal K_R}e^{\lambda z}\,d\mu(\lambda).
\tag{2}
\]

There is `C_kappa>0` such that for every `R>=1`,

\[
\boxed{
\sup_{x\in I_\kappa}|F_\mu(x)|
\ge e^{-C_\kappa R}
}
\tag{3}
\]

and, after changing `C_kappa`,

\[
\boxed{
\int_{I_\kappa}|F_\mu(x)|^2\,dx
\ge e^{-C_\kappa R}.
}
\tag{4}
\]

The exponent is optimal in order. Define

\[
\mathcal V_\kappa(R)
:=
\inf_{\substack{\Lambda\subset\mathcal K_R\text{ finite simple}\\0\in\Lambda}}
\sup_{x\in I_\kappa}
\left|\sum_{\lambda\in\Lambda}e^{\lambda x}\right|.
\tag{5}
\]

Then there are `c_kappa,C_kappa>0` and `R_kappa` such that

\[
\boxed{
 e^{-C_\kappa R}
 \le \mathcal V_\kappa(R)
 \le e^{-c_\kappa R}
}
\qquad(R\ge R_\kappa).
\tag{6}
\]

Finally, in the Robin setting of `RE-135`, fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad \gamma_*>0.
\tag{7}
\]

There exist `c_*,C_*>0` depending only on these fixed parameters and on `kappa` such that the following holds. Let

\[
1\le R(U)\le c_*\log U,
\tag{8}
\]

let `rho_0=beta_0+i gamma_0` satisfy `gamma_0>=gamma_*`, and let `C_U` be any finite nonempty packet containing `rho_0` with

\[
|\beta-\beta_0|\le\frac{R(U)}U,
\qquad
|\gamma-\gamma_0|\le\frac{R(U)}U.
\tag{9}
\]

Write

\[
N_U:=\#C_U.
\tag{10}
\]

Then, for all sufficiently large `U`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge e^{-C_*R(U)}N_U|a_{\rho_0,K}(U)|.
}
\tag{11}
\]

Equation (11) is the quantitative mesoscopic extension of `RE-135`: the reciprocal box may grow logarithmically in scaled coordinates, at the cost of an exponentially decaying visibility constant.

## 1. Taylor truncation gives a cardinality-free exponential floor

Put

\[
B:=\sqrt2 R.
\tag{12}
\]

For `mu` as above, define

\[
m_j:=\int_{\mathcal K_R}\lambda^j\,d\mu(\lambda),
\qquad
P_n(x):=\sum_{j=0}^n\frac{m_j}{j!}x^j.
\tag{13}
\]

Because `mu` is a probability measure,

\[
P_n(0)=1.
\tag{14}
\]

Use the `n+1` equally spaced points

\[
x_j:=1-\kappa+\frac{\kappa j}{n},
\qquad 0\le j\le n.
\tag{15}
\]

Lagrange interpolation at `0` gives

\[
P_n(0)=\sum_{j=0}^nP_n(x_j)L_j(0).
\tag{16}
\]

Since `0<x_j<=1`,

\[
|L_j(0)|
\le
\frac{(n/\kappa)^n}{j!(n-j)!}.
\tag{17}
\]

Hence

\[
\begin{aligned}
1
&\le
\|P_n\|_{L^\infty(I_\kappa)}
\left(\frac n\kappa\right)^n
\sum_{j=0}^n\frac1{j!(n-j)!}
\\
&=
\|P_n\|_{L^\infty(I_\kappa)}
\left(\frac n\kappa\right)^n
\frac{2^n}{n!}.
\end{aligned}
\tag{18}
\]

Using `n!>=(n/e)^n`,

\[
\boxed{
\|P_n\|_{L^\infty(I_\kappa)}
\ge A_\kappa^{-n},
\qquad
A_\kappa:=\frac{2e}{\kappa}.
}
\tag{19}
\]

The Taylor remainder is uniform over the whole probability-measure class. For `x in [0,1]`,

\[
\begin{aligned}
|F_\mu(x)-P_n(x)|
&\le
\int e^{|\lambda|x}
\frac{(|\lambda|x)^{n+1}}{(n+1)!}
\,d\mu(\lambda)
\\
&\le
e^B\frac{B^{n+1}}{(n+1)!}
\\
&\le
e^B\left(\frac{eB}{n+1}\right)^{n+1}.
\end{aligned}
\tag{20}
\]

Choose `L_kappa` so large that

\[
\log L_\kappa\ge 2+\log A_\kappa
\tag{21}
\]

and set

\[
n:=\lceil L_\kappa(B+1)\rceil.
\tag{22}
\]

After increasing `L_kappa` once if necessary, (20) gives

\[
\|F_\mu-P_n\|_{L^\infty([0,1])}
\le\frac12A_\kappa^{-n}.
\tag{23}
\]

Combining (19) and (23),

\[
\sup_{I_\kappa}|F_\mu|
\ge\frac12A_\kappa^{-n}
\ge e^{-C_\kappa(1+R)}.
\tag{24}
\]

For `R>=1` this is (3). The proof uses only bounded support, total positive mass `1`, and therefore `F_mu(0)=1`; the number of atoms never enters.

## 2. The `L^2` floor has the same exponential scale

For real `x in I_kappa`,

\[
|F_\mu'(x)|
\le\sqrt2 R e^R.
\tag{25}
\]

Let

\[
M_R:=\sup_{I_\kappa}|F_\mu|.
\tag{26}
\]

At a point where `|F_mu|` reaches `M_R`, (25) implies that on a one-sided subinterval of length

\[
\ell_R
\gg_\kappa
\min\left\{1,\frac{M_R}{Re^R}\right\}
\tag{27}
\]

one has `|F_mu|>=M_R/2`. Therefore

\[
\int_{I_\kappa}|F_\mu(x)|^2\,dx
\gg_\kappa M_R^2\ell_R
\ge e^{-C_\kappa R},
\tag{28}
\]

where (3) was used in the last step and the polynomial factor in `R` was absorbed by changing `C_kappa`. This proves (4). In particular, the compactness constant `m(R,kappa)` left implicit in `RE-135` can always be taken at least exponentially small in the scaled radius.

## 3. A simple subset-product packet attains exponential suppression

The exponential lower scale cannot be replaced by a radius-independent constant, a power of `R`, or any `exp(-o(R))` floor.

Choose `0<r<1` so that

\[
r^{1-\kappa}<2\cos(\pi\kappa),
\tag{29}
\]

and put

\[
\lambda_0:=-\log r>0.
\tag{30}
\]

As in `RE-133`, for `s in [-kappa,0]`,

\[
\left|1-r^{1+s}e^{i\pi s}\right|<1.
\tag{31}
\]

Thus there is `q_1<1` and `epsilon_0>0` such that

\[
\left|1-r^{1+s}e^{i\pi s}e^{i\epsilon(1+s)}\right|
\le q_1
\tag{32}
\]

for every `s in [-kappa,0]` and `|epsilon|<=epsilon_0`.

Take

\[
\epsilon_\ell:=\epsilon_0 3^{-\ell-2},
\qquad
v_\ell:=-\lambda_0+i(\pi+\epsilon_\ell),
\tag{33}
\]

and for each subset `S` of `{1,...,j}` define

\[
\Lambda_S:=\sum_{\ell\in S}v_\ell.
\tag{34}
\]

The subset sums are distinct: different cardinalities are separated by the integer multiple of `pi`, while equal cardinalities are separated by uniqueness of finite ternary sums with digits `0,1`.

Let

\[
H:=\max\{\lambda_0,\pi+\epsilon_0\}.
\tag{35}
\]

If `jH<=R`, every `Lambda_S` lies in `K_R`, and the empty subset gives `0`. Writing `x=1+s`,

\[
\begin{aligned}
\sum_Se^{\Lambda_Sx}
&=\prod_{\ell=1}^j(1+e^{v_\ell x})
\\
&=\prod_{\ell=1}^j
\left[
1-r^{1+s}e^{i\pi s}e^{i\epsilon_\ell(1+s)}
\right].
\end{aligned}
\tag{36}
\]

Hence

\[
\sup_{I_\kappa}
\left|\sum_Se^{\Lambda_Sx}\right|
\le q_1^j.
\tag{37}
\]

Taking `j=floor(R/H)` proves

\[
\mathcal V_\kappa(R)\le e^{-c_\kappa R}
\tag{38}
\]

for large `R`. Conversely, if `Lambda` has `N` points, its empirical probability measure and (3) give

\[
\sup_{I_\kappa}
\left|\sum_{\lambda\in\Lambda}e^{\lambda x}\right|
\ge Ne^{-C_\kappa R}
\ge e^{-C_\kappa R},
\tag{39}
\]

proving the lower half of (6). Every exponential factor of suppression therefore consumes a proportional amount of scaled spectral radius.

## 4. Quantitative transfer to growing Robin boxes

Use the Robin coefficient law

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^K\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{40}
\]

Put

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
\lambda_{\rho,U}:=U\bigl((\beta-\beta_0)+i(\gamma-\gamma_0)\bigr).
\tag{41}
\]

Under (8)--(9), `R(U)/U->0`; since `gamma_0>=gamma_*`, every packet coordinate has ordinate at least `gamma_*/2` for large `U`. Logarithmic differentiation of `d_rho` on this fixed pole-free region gives

\[
\frac{d_\rho}{d_{\rho_0}}
=1+O\left(\frac{R(U)}U\right),
\tag{42}
\]

uniformly over the packet. The finite-`K` correction remains `O_K(U^-1)` relatively. Because

\[
|e^{\lambda_{\rho,U}x}|\le e^{R(U)}
\qquad(x\in I_\kappa),
\tag{43}
\]

the normalized positive-frequency packet has the representation

\[
\frac1{N_U}\sum_{\rho\in C_U}
a_{\rho,K}(Ux)e^{i\gamma Ux}
=
e^{-(\Theta-\beta_0)Ux}d_{\rho_0}e^{i\gamma_0Ux}
\bigl(Q_U(x)+E_U(x)\bigr),
\tag{44}
\]

where

\[
Q_U(x):=\frac1{N_U}\sum_{\rho\in C_U}e^{\lambda_{\rho,U}x}
\tag{45}
\]

and

\[
\boxed{
\|E_U\|_{L^\infty(I_\kappa)}
\ll\frac{(1+R(U))e^{R(U)}}U.
}
\tag{46}
\]

Also

\[
\|Q_U\|_\infty\le e^{R(U)},
\qquad
\|Q_U'\|_\infty\le\sqrt2R(U)e^{R(U)}.
\tag{47}
\]

By (4),

\[
\int_{I_\kappa}|Q_U(x)|^2\,dx
\ge e^{-C_1R(U)}.
\tag{48}
\]

Write `d_(rho_0)=|d_(rho_0)|e^(i theta_0)` and `omega_U=gamma_0 U`. For

\[
G_U(x):=\Re\left(e^{i(\omega_Ux+\theta_0)}Q_U(x)\right),
\tag{49}
\]

we have

\[
\int G_U^2
=
\frac12\int|Q_U|^2
+
\frac12\Re\int e^{2i(\omega_Ux+\theta_0)}Q_U(x)^2\,dx.
\tag{50}
\]

One integration by parts and (47) give

\[
\left|
\int_{I_\kappa}e^{2i\omega_Ux}Q_U(x)^2\,dx
\right|
\ll\frac{(1+R(U))e^{2R(U)}}U,
\tag{51}
\]

because `omega_U>=gamma_*U`.

Choose `c_*>0` small enough that `R(U)<=c_*log U` makes the right-hand side of (51) and the perturbation scale in (46) negligible compared with the appropriate exponential powers of the lower bound (48). Then

\[
\left\|
\Re\left(e^{i(\omega_Ux+\theta_0)}(Q_U(x)+E_U(x))\right)
\right\|_{L^2(I_\kappa)}
\ge e^{-C_2R(U)}.
\tag{52}
\]

Finally, `x<=1` gives

\[
e^{-(\Theta-\beta_0)Ux}
\ge e^{-(\Theta-\beta_0)U},
\tag{53}
\]

while

\[
|a_{\rho_0,K}(U)|
=e^{-(\Theta-\beta_0)U}|d_{\rho_0}|(1+O_K(U^{-1})).
\tag{54}
\]

Multiplying (52) by the common factor in (44), restoring `N_U`, and passing from `L^2` to `L^infinity` on the fixed interval proves (11).

The logarithmic upper range in (8) is not claimed optimal. It is the range where the explicit exponential floor provably dominates the coefficient and carrier approximation errors by this elementary argument.

## 5. Escape now has a quantitative price

Let

\[
M(U):=|a_{\rho_0,K}(U)|
\tag{55}
\]

and suppose the full strict-subedge residual obeys

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_K(u)|
\le\varepsilon_U M(U).
\tag{56}
\]

For a packet `C_U(R)` inside a scaled radius `R<=c_*log U`, write `N_U(R):=#C_U(R)`. Equation (11) supplies a point `u_R` such that

\[
|\mathcal S_{C_U(R),K}(u_R)|
\ge e^{-C_*R}N_U(R)M(U).
\tag{57}
\]

Therefore the exterior complement must satisfy

\[
\boxed{
|\mathcal S_{\mathrm{outside}\ R/U,K}(u_R)|
\ge
\left(e^{-C_*R}N_U(R)-\varepsilon_U\right)M(U).
}
\tag{58}
\]

If

\[
\varepsilon_U\le\frac12e^{-C_*R}N_U(R),
\tag{59}
\]

the exterior cancellation required at `u_R` is at least

\[
\frac12e^{-C_*R}N_U(R)M(U).
\tag{60}
\]

In particular, if there is no exterior packet and the local packet itself is suppressed to `epsilon_U M(U)`, then

\[
\boxed{
R
\ge
\frac1{C_*}\log\frac{N_U}{\varepsilon_U}
\ge
\frac1{C_*}\log\frac1{\varepsilon_U}.
}
\tag{61}
\]

Thus “scaled diameter must diverge” from `RE-135` has a quantitative form: buying `epsilon` suppression requires at least logarithmic scaled radius.

`RE-133` matches this law. Its stage-`j` cluster has scaled diameter `O(j)` while its product residual is `q_1^j=exp(-Omega(j))`. Hence (61) has the correct functional dependence in the matched synthetic class.

## 6. Adversarial and representation audit

Several distinctions are load-bearing.

First, (3)--(4) use the **positive probability normalization** inherited from the Robin coefficient alignment. Generic exponential polynomials with arbitrary complex coefficients do not have the same cardinality-free moment control.

Second, the abstract transform statements (3)--(6) hold for every `R`. The physical transfer (11) is proved only for `R(U)<=c_*log U`; for faster growth the coefficient-ratio error, the factor `e^R`, or the carrier integration error may swamp the floor.

Third, (11) is a statement about a **local packet**, not the full residual. Equation (58), rather than a global lower bound, is the correct consequence in the presence of exterior atoms.

Fourth, the factor `N_U` is real information. The strongest lower bound is relative to the aligned local mass scale `N_U M(U)`, not merely one target atom. Equation (61) keeps that occupancy contribution explicit.

Fifth, the upper construction in Section 3 is a transform-level and formal matched-control obstruction. `RE-133` embeds the same mechanism into the finite-order Robin coefficient law with simple coordinates, functional-equation symmetry, and arbitrarily sparse one-level density. None of this asserts that actual zeta zeros realize such clusters.

Finally, the theorem quantifies escape but does not establish actual-zeta tightness. An exterior tail comparable to `e^{-CR}M(U)` remains compatible with everything proved here. The source-specific problem is to beat that scale or to exploit arithmetic geometry absent from the compact-support probability-transform model.

## 7. Prior-art boundary

The literature audit found classical Remez and Turan--Nazarov observability as the nearest general language. Those inequalities control polynomial or exponential-polynomial behavior on subsets of intervals, usually with an effective degree or number of exponential terms in the constant. A June 2026 preprint of Omer Friedland gives a modular disk-growth proof of the measurable Turan--Nazarov inequality and explicitly discusses bounded spectral diameter as a favorable regime.

No external observability theorem is load-bearing here. Equations (15)--(24) derive the required lower bound directly from Taylor truncation and elementary Lagrange interpolation, and cardinality disappears because the normalized Robin packet is a positive probability measure. The exponential upper bound is the subset-product construction already native to this line. `SOURCES.md` therefore needs no new durable anchor.

Novelty is claimed only for the line-specific quantitative splice: exposing the `R`-dependence hidden in `RE-135`, extending the physical packet to logarithmically growing scaled boxes, and matching that lower scale to the formal `RE-133` obstruction. No novelty is claimed for Remez-type observability itself.

## 8. Consequence for the research line

`RE-135` reduced the remaining obstruction to loss of reciprocal-scale tightness. `RE-136` measures that loss. A local canceling mechanism confined to scaled radius `R` cannot suppress the aligned Robin packet by more than an exponential factor in `R`, while the formal subset-product control achieves exponential suppression.

The next source-specific target can therefore be stated quantitatively. It is enough to prove an exterior-tail estimate that, on the relevant hypothetical off-critical packet, beats

\[
\boxed{
\sup_I|\mathcal S_{\mathrm{outside}\ R/U,K}|
=o\!\left(e^{-CR}M_K(U)\right)
}
\tag{62}
\]

for some admissible radius regime, or to derive an arithmetic obstruction to the subset-product geometry attaining the exponential law. A merely qualitative statement that the exterior mass tends to zero is not automatically sufficient, because the local visibility constant itself decays exponentially with radius.

The frontier is therefore an explicit race between **source-specific tail decay** and **exponential visibility loss**.