# RE-136 — reciprocal-box visibility has a sharp exponential radius law

**Status:** `EXACT-DERIVED + QUANTITATIVE-RECIPROCAL-BOX + EXPONENTIAL-VISIBILITY-FLOOR + LOGARITHMIC-MESOSCOPIC-RADIUS + SHARP-MATCHED-CONTROL + MACROSCOPIC-WINDOW + REAL-PACKET-OBSERVABILITY + ESCAPE-COST + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-135` removes the occupancy hypothesis from reciprocal-box visibility, but its compactness proof leaves the dependence of the visibility constant on the scaled box radius `R` completely qualitative. That dependence is the next live quantity: a hiding packet can escape every fixed reciprocal box only by sending cancellation to scaled radii tending to infinity, so the useful question is how much suppression a radius `R` can buy.

The answer is exponential, and that scale is sharp. For the normalized positive-measure transforms underlying `RE-135`, bounded spectral radius `R` forces an interval visibility floor `exp(-O_kappa(R))`. The same exponential floor transfers to the real Robin packet, uniformly even for a slowly growing radius `R(U)<=c log U`. Conversely, the subset-product cluster mechanism already present in `RE-133` produces simple reciprocal packets of scaled radius `O(j)` whose residual is `exp(-Omega(j))`. Thus the radius needed to buy suppression `epsilon` is, up to constants, logarithmic in `1/epsilon`.

This does **not** prove reciprocal-scale tightness for the actual zeta packet. It quantifies the only remaining escape mechanism from `RE-135`: any source-specific theorem that makes the exterior tail smaller than the exponential radius floor would contradict macroscopic hiding.

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

There are constants `C_kappa,c_kappa>0` such that for every `R>=1`,

\[
\boxed{
\sup_{x\in I_\kappa}|F_\mu(x)|
\ge
\exp(-C_\kappa R)
}
\tag{3}
\]

and

\[
\boxed{
\int_{I_\kappa}|F_\mu(x)|^2\,dx
\ge
\exp(-C_\kappa R).
}
\tag{4}
\]

The constant may change from line to line. The important point is the **linear exponent in `R`**, with no dependence on the number of atoms of `mu`.

This exponent is optimal in order. Define

\[
\mathcal V_\kappa(R)
:=
\inf_{\substack{\Lambda\subset\mathcal K_R\text{ finite simple}\\0\in\Lambda}}
\sup_{x\in I_\kappa}
\left|
\sum_{\lambda\in\Lambda}e^{\lambda x}
\right|.
\tag{5}
\]

Then, after changing constants,

\[
\boxed{
 e^{-C_\kappa R}
 \le
 \mathcal V_\kappa(R)
 \le
 e^{-c_\kappa R}
}
\qquad(R\ge R_\kappa).
\tag{6}
\]

Thus no radius-independent floor survives as `R->infinity`, but neither can bounded-radius packets buy superexponential suppression.

Finally, in the Robin setting of `RE-135`, fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad \gamma_*>0.
\tag{7}
\]

There exist constants `c_*,C_*>0` depending only on these fixed parameters and on `kappa` such that, whenever

\[
1\le R(U)\le c_*\log U,
\tag{8}
\]

`rho_0=beta_0+i gamma_0` has `gamma_0>=gamma_*`, and a finite packet `C_U` containing `rho_0` satisfies

\[
|\beta-\beta_0|\le\frac{R(U)}U,
\qquad
|\gamma-\gamma_0|\le\frac{R(U)}U,
\tag{9}
\]

then for all sufficiently large `U`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
 e^{-C_*R(U)}\,#C_U\,|a_{\rho_0,K}(U)|.
}
\tag{10}
\]

Equation (10) is a quantitative mesoscopic extension of `RE-135`: the reciprocal box may grow logarithmically in scaled coordinates, at the cost of an exponentially decaying visibility constant.

## 1. Taylor truncation gives a cardinality-free exponential floor

Put

\[
B:=\sqrt2\,R.
\tag{11}
\]

For `mu` as above, write its moments

\[
m_j:=\int_{\mathcal K_R}\lambda^j\,d\mu(\lambda)
\tag{12}
\]

and let

\[
P_n(x):=\sum_{j=0}^n\frac{m_j}{j!}x^j.
\tag{13}
\]

Because `mu` is a probability measure,

\[
P_n(0)=m_0=1.
\tag{14}
\]

We first prove a crude but explicit Remez-type bound for `P_n` without importing any external theorem. Use the `n+1` equally spaced points

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

Therefore

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
\ge
A_\kappa^{-n},
\qquad
A_\kappa:=\frac{2e}{\kappa}.
}
\tag{19}
\]

On the other hand, the exponential Taylor remainder is uniform over the whole probability-measure class. For `x in [0,1]`,

\[
\begin{aligned}
|F_\mu(x)-P_n(x)|
&\le
\int
 e^{|\lambda|x}
 \frac{(|\lambda|x)^{n+1}}{(n+1)!}
 \,d\mu(\lambda)
\\
&\le
 e^B\frac{B^{n+1}}{(n+1)!}
\\
&\le
 e^B
\left(\frac{eB}{n+1}\right)^{n+1}.
\end{aligned}
\tag{20}
\]

Choose a fixed `L_kappa` so large that

\[
\log L_\kappa\ge 2+\log A_\kappa,
\tag{21}
\]

and set

\[
n:=\lceil L_\kappa(B+1)\rceil.
\tag{22}
\]

Then (20), Stirling's elementary lower bound, and (21) give, after enlarging `L_kappa` once if necessary,

\[
\|F_\mu-P_n\|_{L^\infty([0,1])}
\le
\frac12A_\kappa^{-n}.
\tag{23}
\]

Combining (19) and (23),

\[
\sup_{x\in I_\kappa}|F_\mu(x)|
\ge
\frac12A_\kappa^{-n}
\ge
\exp[-C_\kappa(1+R)].
\tag{24}
\]

For `R>=1` this is (3), after changing `C_kappa`.

The proof is deliberately elementary. The only properties used are bounded spectral support, total positive mass `1`, and therefore `F_mu(0)=1` together with uniform moment bounds. The number of atoms never enters.

## 2. The `L^2` floor has the same exponential scale

The carrier step in the physical Robin packet needs an integral norm rather than one large complex value. The same exponential radius scale survives.

For real `x in I_kappa`,

\[
|F_\mu'(x)|
\le
\int |\lambda|e^{\Re\lambda x}\,d\mu(\lambda)
\le
\sqrt2\,R e^R.
\tag{25}
\]

Let

\[
M_R:=\sup_{I_\kappa}|F_\mu|.
\tag{26}
\]

By (24), `M_R>=exp(-C_kappa R)`. At a point where `|F_mu|` reaches `M_R`, the derivative bound (25) implies that on a one-sided subinterval of `I_kappa` of length at least

\[
\ell_R
\gg_\kappa
\min\left\{1,
\frac{M_R}{R e^R}
\right\},
\tag{27}
\]

one has `|F_mu|>=M_R/2`. Consequently

\[
\int_{I_\kappa}|F_\mu(x)|^2\,dx
\gg_\kappa
M_R^2\ell_R
\ge
\exp[-C_\kappa R],
\tag{28}
\]

again after changing `C_kappa` and absorbing the harmless polynomial factor in `R`. This proves (4).

Thus the compactness constant `m(R,kappa)` left implicit in `RE-135` can always be taken at least exponentially small in the scaled radius.

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

Exactly as in the contractive factor of `RE-133`, for `s in [-kappa,0]`,

\[
\left|1-r^{1+s}e^{i\pi s}\right|<1.
\tag{31}
\]

Compactness gives a `q<1` with the left-hand side at most `q`. Choose `q<q_1<1`. There is then an `epsilon_0>0` such that

\[
\left|
1-r^{1+s}e^{i\pi s}e^{i\epsilon(1+s)}
\right|
\le q_1
\tag{32}
\]

for every `s in [-kappa,0]` and `|epsilon|<=epsilon_0`.

Take distinct tiny ternary perturbations

\[
\epsilon_\ell:=\epsilon_0 3^{-\ell-2},
\qquad
v_\ell:=-\lambda_0+i(\pi+\epsilon_\ell).
\tag{33}
\]

For each subset `S` of `{1,...,j}`, define

\[
\Lambda_S:=\sum_{\ell\in S}v_\ell.
\tag{34}
\]

The subset sums are distinct. Different cardinalities are separated by the integer multiple of `pi` in the imaginary part, while equal cardinalities are separated by uniqueness of finite ternary sums with digits `0,1`.

Let

\[
H:=\max\{\lambda_0,\pi+\epsilon_0\}.
\tag{35}
\]

If `jH<=R`, then every `Lambda_S` lies in `K_R`, and the empty subset gives `0`. Moreover, writing `x=1+s`,

\[
\begin{aligned}
\sum_{S\subseteq\{1,\ldots,j\}}e^{\Lambda_Sx}
&=
\prod_{\ell=1}^j(1+e^{v_\ell x})
\\
&=
\prod_{\ell=1}^j
\left[
1-r^{1+s}e^{i\pi s}e^{i\epsilon_\ell(1+s)}
\right].
\end{aligned}
\tag{36}
\]

Hence

\[
\sup_{x\in I_\kappa}
\left|
\sum_Se^{\Lambda_Sx}
\right|
\le q_1^j.
\tag{37}
\]

Taking `j=floor(R/H)` gives

\[
\sup_{I_\kappa}
\left|
\sum_Se^{\Lambda_Sx}
\right|
\le
\exp(-c_\kappa R)
\tag{38}
\]

for all sufficiently large `R`, proving the upper half of (6). The lower half follows from (3): if `N=#Lambda`, the empirical probability measure on `Lambda` has transform `N^-1 sum exp(lambda x)`, so

\[
\sup_{I_\kappa}
\left|
\sum_{\lambda\in\Lambda}e^{\lambda x}
\right|
\ge
N e^{-C_\kappa R}
\ge
 e^{-C_\kappa R}.
\tag{39}
\]

This is the exact concentration--compactness scale hidden in `RE-133` and `RE-135`: every factor of exponential suppression consumes a proportional amount of scaled spectral radius.

## 4. Quantitative transfer to growing Robin reciprocal boxes

We now keep the `R`-dependence that `RE-135` was free to suppress.

For the Robin coefficient law

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^K
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\tag{40}
\]

put

\[
d_\rho:=\frac1{\rho(1-\rho)}
\tag{41}
\]

and define the scaled offsets

\[
\lambda_{\rho,U}
:=U\bigl((\beta-\beta_0)+i(\gamma-\gamma_0)\bigr).
\tag{42}
\]

Assume (8)--(9). Since `R(U)/U->0` and `gamma_0>=gamma_*`, every packet coordinate has ordinate at least `gamma_*/2` for large `U`. Logarithmic differentiation of `d_rho` on this fixed pole-free region gives

\[
\frac{d_\rho}{d_{\rho_0}}
=1+O\left(\frac{R(U)}U\right),
\tag{43}
\]

uniformly over the packet. The finite-`K` bracket still contributes only `O_K(U^-1)` relatively. Since

\[
|e^{\lambda_{\rho,U}x}|\le e^{R(U)}
\qquad(x\in I_\kappa),
\tag{44}
\]

the normalized positive-frequency packet has the representation

\[
\frac1{N_U}
\sum_{\rho\in C_U}
a_{\rho,K}(Ux)e^{i\gamma Ux}
=
e^{-(\Theta-\beta_0)Ux}
d_{\rho_0}e^{i\gamma_0Ux}
\bigl(Q_U(x)+E_U(x)\bigr),
\tag{45}
\]

where

\[
Q_U(x)
:=\frac1{N_U}
\sum_{\rho\in C_U}e^{\lambda_{\rho,U}x}
\tag{46}
\]

and now the growing-radius error is explicit:

\[
\boxed{
\|E_U\|_{L^\infty(I_\kappa)}
\ll
\frac{(1+R(U))e^{R(U)}}U.
}
\tag{47}
\]

The transform bounds are likewise explicit,

\[
\|Q_U\|_\infty\le e^{R(U)},
\qquad
\|Q_U'\|_\infty
\le \sqrt2 R(U)e^{R(U)}.
\tag{48}
\]

By (4),

\[
\int_{I_\kappa}|Q_U(x)|^2\,dx
\ge e^{-C_1R(U)}
\tag{49}
\]

for some fixed `C_1`.

Write `d_(rho_0)=|d_(rho_0)|e^(i theta_0)` and `omega_U=gamma_0 U`. As in `RE-135`, for

\[
G_U(x):=\Re\left(
e^{i(\omega_Ux+\theta_0)}Q_U(x)
\right)
\tag{50}
\]

we have

\[
\int G_U^2
=
\frac12\int|Q_U|^2
+
\frac12\Re
\int e^{2i(\omega_Ux+\theta_0)}Q_U(x)^2\,dx.
\tag{51}
\]

One integration by parts and (48) give

\[
\left|
\int_{I_\kappa}e^{2i\omega_Ux}Q_U(x)^2\,dx
\right|
\ll
\frac{(1+R(U))e^{2R(U)}}U,
\tag{52}
\]

because `omega_U>=gamma_* U`.

Choose `c_*>0` small enough, depending on `C_1` and the fixed parameters, that `R(U)<=c_* log U` makes both the right-hand side of (52) and the square of the perturbation scale in (47) `o(exp(-C_1R(U)))`. Then (49)--(52) imply

\[
\left\|
\Re\left(
e^{i(\omega_Ux+\theta_0)}(Q_U(x)+E_U(x))
\right)
\right\|_{L^2(I_\kappa)}
\ge
 e^{-C_2R(U)}
\tag{53}
\]

for a fixed `C_2`.

Finally, `x<=1` gives

\[
e^{-(\Theta-\beta_0)Ux}
\ge
e^{-(\Theta-\beta_0)U},
\tag{54}
\]

and the target bracket at `u=U` satisfies

\[
|a_{\rho_0,K}(U)|
=
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|(1+O_K(U^{-1})).
\tag{55}
\]

Multiplying (53) by the common factor in (45), restoring the factor `N_U`, and passing from `L^2` to `L^infinity` on the fixed interval proves (10).

The logarithmic upper range in (8) is not claimed to be optimal. It is simply the range in which the explicit exponential visibility floor still dominates the coefficient and fast-carrier approximation errors by an elementary argument.

## 5. Escape now has a quantitative price

Let

\[
M(U):=|a_{\rho_0,K}(U)|
\tag{56}
\]

and suppose the full strict-subedge residual obeys

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_K(u)|
\le
\varepsilon_U M(U).
\tag{57}
\]

For a packet `C_U(R)` inside a scaled radius `R<=c_*log U`, (10) supplies a point `u_R` in the same window at which

\[
|\mathcal S_{C_U(R),K}(u_R)|
\ge
 e^{-C_*R}\,#C_U(R)\,M(U).
\tag{58}
\]

Therefore its exterior complement must satisfy

\[
\boxed{
|\mathcal S_{\mathrm{outside}\ R/U,K}(u_R)|
\ge
\left(
e^{-C_*R}\,#C_U(R)-\varepsilon_U
\right)M(U).
}
\tag{59}
\]

Whenever

\[
\varepsilon_U
\le
\frac12e^{-C_*R}\,#C_U(R),
\tag{60}
\]

the required exterior cancellation is at least

\[
\frac12e^{-C_*R}\,#C_U(R)M(U).
\tag{61}
\]

In particular, if there is **no** exterior packet and the local packet itself is suppressed to `epsilon_U M(U)`, then

\[
\boxed{
R
\ge
\frac1{C_*}
\log\frac{#C_U}{\varepsilon_U}
\ge
\frac1{C_*}\log\frac1{\varepsilon_U}.
}
\tag{62}
\]

Thus the qualitative phrase “scaled diameter must diverge” from `RE-135` has a quantitative form: buying `epsilon` suppression requires at least logarithmic scaled radius, and every extra constant amount of scaled radius can buy at most a constant factor of suppression.

`RE-133` matches this law. Its stage-`j` cluster has scaled diameter `O(j)` while its product factor is `q_1^j=exp(-Omega(j))`. Hence (62) has the right functional dependence. The formal control does not merely show that `R` must grow; it shows that exponential suppression per unit scaled radius is genuinely attainable in the matched synthetic class.

## 6. Adversarial and representation audit

Several distinctions are load-bearing.

First, (3)--(4) use the **positive probability normalization** inherited from the Robin coefficient alignment. Generic exponential polynomials with arbitrary complex coefficients do not satisfy `F(0)=1` with uniformly bounded moments after normalization, and the argument does not apply to them.

Second, the abstract transform statements (3)--(6) hold for every `R`. The physical growing-box transfer (10) is weaker and is proved only for `R(U)<=c_*log U`. For faster-growing radii the coefficient-ratio error, the factor `e^R`, or the carrier integration error can swamp the exponential floor. No conclusion is claimed there.

Third, (10) is still a statement about a **local packet**, not the full residual. Equation (59), not a nonexistent global lower bound, is the correct consequence in the presence of exterior atoms.

Fourth, the factor `#C_U` matters. The strongest lower bound is relative to the aligned total local mass scale `#C_U M(U)`, not merely to one target atom. Equation (62) records both versions and does not silently discard occupancy when translating suppression into radius.

Fifth, the upper construction in Section 3 is a transform-level and formal matched-control obstruction. Its subset sums can be made simple, and `RE-133` already embeds the same mechanism into the finite-order Robin coefficient law with functional-equation symmetry and arbitrarily sparse one-level density. None of this asserts that actual zeta zeros realize such clusters.

Finally, the theorem quantifies escape but does not establish actual-zeta tightness. An exterior tail of size comparable to `e^{-CR}M(U)` remains fully compatible with all conclusions here. The source-specific problem is now to beat that scale, or to exploit arithmetic geometry not represented by the positive compact-support transform model.

## 7. Prior-art boundary

The literature audit found classical Remez and Turan--Nazarov observability as the nearest general language. Those inequalities control polynomial or exponential-polynomial behavior on a subset of an interval, typically with an effective degree or number of exponential terms in the constant. A June 2026 preprint of Omer Friedland gives a modular disk-growth proof of the measurable Turan--Nazarov inequality and explicitly discusses bounded spectral diameter as a favorable regime.

No external observability theorem is load-bearing here. Equations (15)--(24) give the needed lower bound directly by Taylor truncation plus elementary Lagrange interpolation, and the cardinality disappears only because the normalized Robin packet is a positive probability measure. The exponential upper bound is the explicit subset-product construction already native to this research line. Therefore `SOURCES.md` needs no new durable anchor.

Novelty is claimed only for the line-specific quantitative splice: making the hidden `R`-dependence in `RE-135` explicit, extending the physical packet to logarithmically growing scaled boxes, and matching that lower scale to the formal `RE-133` obstruction. No novelty is claimed for Remez-type observability itself.

## 8. Consequence for the research line

`RE-135` reduced the remaining obstruction to loss of reciprocal-scale tightness. `RE-136` now measures that loss. A local canceling mechanism confined to scaled radius `R` cannot suppress the aligned Robin packet by more than an exponential factor in `R`, while the formal subset-product control achieves exactly exponential suppression.

The next source-specific target can therefore be stated quantitatively. It is enough to prove an exterior-tail estimate that, on the relevant hypothetical off-critical packet, beats the visibility scale

\[
\boxed{
\sup_I
|\mathcal S_{\mathrm{outside}\ R/U,K}|
=
o\!\left(e^{-C R}M_K(U)\right)
}
\tag{63}
\]

for some admissible radius regime, or to derive an arithmetic obstruction to the subset-product geometry that attains the exponential law. A merely qualitative assertion that the exterior mass tends to zero is not automatically enough, because the local visibility constant itself decays exponentially with the radius.

This is a stricter and more useful frontier than “prove tightness”: the required theorem must now win an explicit race between **tail decay** and **exponential visibility loss**.