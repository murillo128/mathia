# ANF-209 — Real two-site notch attainment has a sharp cubic width window

**Status:** EXACT-DERIVED + ALL-REAL-MULTISETS + WIDTH-UNIFORM-TWO-SITE-REDUCTION + SHARP-ORDER. There are absolute positive constants `c,C` such that a triangular notch of width `eta` has its unrestricted real energy floor attained by two sites whenever its removed height satisfies `0<a<=c eta^3`. For sufficiently small width, no configuration supported on at most two sites attains that floor when `C eta^3<=a<=1/20`. Thus the initial two-site attainment window has order `eta^3`. The lower bound is new here; the upper obstruction is ANF-207. Neither the exact transition constant nor the unrestricted complex floor is determined.

## Object and statement

Use `f_hat(x)=int f(u) exp(-2 pi i u x) du` and put
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-b x\sin(\pi x)}{1-dx^2},\qquad
b=\sqrt2\pi\cot(1/\sqrt2),\quad d=2\pi^2.
\tag{1}
\]
The removable values are continued, and `K(0)=1`. For `0<eta<=1/4`,
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
\Phi_\eta(x)=\widehat{\tau_\eta}(x)
=\eta\operatorname{sinc}^2(\eta x),\quad
J_{\eta,a}=J_0-a\tau_\eta,
\tag{2}
\]
where `sinc(x)=sin(pi x)/(pi x)` continuously at zero. The parameter
`a` is the removed height; for the profile `(1/10)tau_eta` it equals
one tenth of the relative amplitude. Restrict `a<=1/20`, so
`J_(eta,a)>=J_0/2` by the domination checked in ANF-207.

For a finite nonempty real multiset with distinct sites `x_i` and
positive integer multiplicities `m_i`, write
\[
\ell(1)=1,\quad \ell(m)=2m\ (m\ge2),\quad
L(W)=\sum_i\ell(m_i),\quad S_W(u)=\sum_i m_i e^{-2\pi iux_i},
\]
\[
E_f(W)=\int f|S_W|^2,\qquad
q^{\mathbb R}_{\eta,a}=\inf_W E_{J_{\eta,a}}(W)/L(W).
\tag{3}
\]
There is no cardinality, separation, diameter or density constraint.

There is an absolute `c>0` such that
\[
\boxed{
q^{\mathbb R}_{\eta,a}
=1-a\eta+\min_{x>0}\{F(x)-a\Phi_\eta(x)\}
\quad(0<\eta\le1/4,\ 0<a\le c\eta^3).
}
\tag{4}
\]
The minimum exists and a simple pair at a minimizing separation attains
the left side. Two sites both of multiplicity two also attain it.

For all sufficiently small `eta`, the opposite conclusion holds throughout
\[
\boxed{(8\pi^2)^3\eta^3\le a\le1/20:}
\tag{5}
\]
no real multiset supported on at most two distinct sites attains the floor.
In particular, if `A_2(eta)` is the supremum of all `A<=1/20` for
which (4) holds for every `0<a<=A`, then
\[
A_2(\eta)\asymp\eta^3\qquad(\eta\downarrow0).
\tag{6}
\]
This defines an initial interval; it does not assert a unique transition
or identify the minimizing configurations beyond it.

## A pair coercivity estimate uniform in its growing separation

ANF-114 proves that any three ordered real sites of span at most `T` obey
\[
F(x_1-x_2)+F(x_1-x_3)+F(x_2-x_3)
\ge\kappa_T:=\frac1{16(1+dT^2)^2}.
\tag{7}
\]
Coincident arguments also satisfy this bound because `F(0)=1`.

There are absolute `epsilon_0,k_0>0` such that for every `R>=1`,
\[
0<r\le R,\quad F(r)\le\epsilon_0R^{-4}
\quad\Longrightarrow\quad
\boxed{F(y)+F(y-r)\ge\frac{k_0}{R^2(R^2+y^2)}
\quad(y\in\mathbb R).}
\tag{8}
\]
The constants are independent of which approximate source zero occurs
and of how many source zeros lie in `[0,R]`.

Here is a constructive choice, also proving the tail part of (8). Set
\[
\alpha=b/d,\quad B=\frac{1+\alpha}{d-1},\quad
s_0=\frac3{4\sqrt{1+b^2}},\quad A=\alpha s_0/\sqrt2,
\]
\[
D=\max(2,6B/A),\qquad
k_D=\frac1{16[1+d(D+1)^2]^2},\qquad
k_2=\frac1{16(1+4d)^2},
\]
\[
\epsilon_0=\min\left\{\frac1{16(1+d)^2},\frac{k_D}{2},
\frac{k_2}{4},\frac14\right\},\qquad
k_0=\min(k_D/2,A^2/9).
\tag{9}
\]
If `p=cos(pi r)-b r sin(pi r)`, the hypothesis in (8) gives
`|p|<=sqrt(epsilon_0)(1+d)<=1/4`. The unit-circle identity gives
\[
1\le |p|+\sqrt{1+b^2r^2}|\sin(\pi r)|,
\qquad |\sin(\pi r)|\ge s_0/R.
\tag{10}
\]
The identity `p=(1-dr^2)K(r)` is valid also at the removable points.

Directly from (1), for `|x|>=1`,
\[
\left|xK(x)-\alpha\sin(\pi x)\right|
=\left|\frac{x\cos(\pi x)-\alpha\sin(\pi x)}{1-dx^2}\right|
\le B/|x|.
\tag{11}
\]
For any real `theta`,
\[
\sin^2\theta+\sin^2(\theta-\pi r)
\ge1-|\cos(\pi r)|\ge\tfrac12\sin^2(\pi r).
\]
Thus, when `|y|>=DR`, the vector
`(yK(y),(y-r)K(y-r))` has norm at least
\[
A/R-3B/|y|\ge A/(2R).
\]
Here `|y-r|>=|y|/2`, so the error from the two applications of
(11) is at most `sqrt(5) B/|y|<3B/|y|`. Also
`max(|y|,|y-r|)<=3|y|/2`, giving
\[
F(y)+F(y-r)\ge A^2/(9R^2y^2).
\tag{12}
\]
For `|y|<=DR`, the triple `0,r,y` has span at most `(D+1)R`.
Equation (7) gives
\[
F(y)+F(y-r)\ge(k_D-\epsilon_0)R^{-4}
\ge(k_D/2)R^{-4}.
\tag{13}
\]
Together these prove (8). This avoids a compactness constant whose
dependence on the number of roots or on `R` was unspecified in ANF-200.

Now fix the physical scale
\[
R=4/\eta,\qquad \gamma=\epsilon_0R^{-4}.
\tag{14}
\]
For `0<r<=R`, the actual notch tail satisfies
\[
\Phi_\eta(y)+\Phi_\eta(y-r)
\le\frac{10\eta R^2}{R^2+y^2}.
\tag{15}
\]
For `|y|<=2R`, use the bound `2eta` on the left. Outside that
interval, use `5/(pi^2 eta y^2)` and `eta R=4`. Consequently
\[
\boxed{
F(r)\le\gamma, 0<r\le R
\quad\Longrightarrow\quad
\Phi_\eta(y)+\Phi_\eta(y-r)
\le\frac{10}{k_0}\eta R^4\{F(y)+F(y-r)\}.}
\tag{16}
\]
The loss is `eta R^4=256 eta^(-3)`, including the entire tail.

## Preserve matched-pair energy and charge everything else uniformly

For the multiset in (3), the real excess is exactly
\[
\Delta=E_{J_0}(W)-L(W)
=\sum_{m_i\ge3}m_i(m_i-2)
 +2\sum_{i<j}m_im_jF(x_i-x_j)\ge0.
\tag{17}
\]
Perform the whole-site decomposition of ANF-200 with the explicit scale
(14). Let `B_0` contain sites of multiplicity at least three. Among
the remaining sites `H`, mark
\[
B_1=\{i\in H:D_i>\gamma\},\qquad
D_i=\sum_{j\in H,\ j\ne i}m_jF(x_i-x_j).
\]
Put `Bcal=B_0 union B_1` and `G=W\setminus Bcal`. Every good
multiplicity is one or two and every interaction between two good
sites is at most `gamma`. Three good sites with two distance-`R`
edges would have span at most `2R`, contradicting
`3gamma<kappa_(2R)` by (9). The distance-`R` graph on `G` is
therefore a matching. Let `P` be its paired sites, `U` its isolated
sites, and `Ecal` its edges. Set
\[
\Delta_P=2\sum_{\{i,j\}\in\mathcal E}m_im_jF(x_i-x_j),
\qquad\Delta_{\rm out}=\Delta-\Delta_P\ge0.
\tag{18}
\]
All subsets retain entire sites, so their `L` values are additive.

Write `C_B=2+2/epsilon_0` and `C_K=16(1+d)^2`. The bad-site
budget is
\[
L(\mathcal B)\le(2+2/\gamma)\Delta_{\rm out}
\le C_B R^4\Delta_{\rm out},\qquad
\Delta(\mathcal B)\le\Delta_{\rm out}.
\tag{19}
\]
Indeed, `2m<=2m(m-2)` for `m>=3`; and on `B_1`,
`m_i^2<=2m_iD_i/gamma`. Summing the latter counts a source
edge at most twice, exactly its ordered weight in (17). None is
an internal good matching edge. Internal bad-site source excess
also uses only terms retained in `Delta_out`.

The width-explicit cell estimate of ANF-208, applied to any whole-site
submultiset `Z`, is
\[
E_{\tau_\eta}(Z)
\le(3\eta+2/R)\{3L(Z)+3\kappa_R^{-1}\Delta(Z)\}.
\tag{20}
\]
Its ingredients are the weighted triple bound
`sum_j n_j^2<=3L(Z)+3 Delta(Z)/kappa_R` for length-`R` cell
occupancies and the notch interaction row sum `<=3eta+2/R`.
Since `kappa_R^(-1)<=C_K R^4`, equations (19)--(20) give
\[
E_{\tau_\eta}(\mathcal B)
\le\tfrac{21}{2}(C_B+C_K)\eta R^4\Delta_{\rm out}.
\tag{21}
\]
Using only `E_tau(Bcal)<=10 E_0(Bcal)` here would lose the factor
`eta` and would not give the cubic window.

Each interval of length `R` contains at most two good sites, with total
multiplicity at most four. Center the same cell partition at any real
`y`. The row sum used in (20) gives
\[
\sup_y\sum_{j\in G}m_j\Phi_\eta(y-x_j)
\le4(3\eta+2/R)=14\eta.
\tag{22}
\]
Thus the ordered bad--good notch interaction is at most
`28 eta L(Bcal)<=28 C_B eta R^4 Delta_out`.

For an internal good pair and an outside good site, (16) controls
the sum of the two notch interactions by its source counterpart.
Endpoint multiplicities in `{1,2}` cost at most a factor two.
Summing over good pairs counts pair--pair interactions twice and
pair--isolated interactions once. The entire notch interaction involving
`P`, excluding internal matching edges, is consequently at most
\[
(40/k_0)\eta R^4\Delta_{\rm out}.
\tag{23}
\]
This uses no part of `Delta_P`.

Choose a zero `r_1 in (1,3/2)` of `K`, whose existence follows from
the opposite signs of its numerator at the endpoints, and put
\[
\mu_\eta=\Phi_\eta(r_1)\ge4\eta/\pi^2.
\tag{24}
\]
Here `eta r_1<1/2`. Isolated good sites are more than `R` apart.
Their multiplicities are at most two, so from any one of them the
potential of all the others is at most
\[
\frac4{\pi^2\eta R^2}\sum_{n\ge1}n^{-2}
\le\frac8{\pi^2\eta R^2}
\le\mu_\eta/2.
\tag{25}
\]
The ordered isolated--isolated interaction is therefore at most
`(mu_eta/2)L(U)`.

The good diagonal is `eta L(G)<=eta L(W)`. Combining it with
(21)--(25) proves the uniform retained-edge bound
\[
\boxed{
E_{\tau_\eta}(W)\le\eta L(W)
 +2\sum_{\{i,j\}\in\mathcal E}m_im_j\Phi_\eta(x_i-x_j)
 +\frac{\mu_\eta}{2}L(U)
 +C_0\eta^{-3}\Delta_{\rm out},}
\tag{26}
\]
where one explicit absolute choice is
\[
C_0=256\left[\tfrac{21}{2}(C_B+C_K)+28C_B+40/k_0\right].
\tag{27}
\]
Empty subsets cause no exception. All diagonal terms, multiplicities
and cross-interactions have been included.

## The exact floor and its sharp amplitude order

Let
\[
v=\min_{x>0}\{F(x)-a\Phi_\eta(x)\}.
\]
This is an attained negative minimum: the value at `r_1` is
`-a mu_eta`, the value at zero is positive, and the function tends
to zero at infinity. Thus `v<=-a mu_eta<0`.

Subtracting `a` times (26) from `E_0=L+Delta_P+Delta_out` gives
\[
E_{J_{\eta,a}}(W)\ge(1-a\eta)L
 +2\sum_{\{i,j\}\in\mathcal E}m_im_j
       [F(x_i-x_j)-a\Phi_\eta(x_i-x_j)]
 +(1-aC_0\eta^{-3})\Delta_{\rm out}
 -\frac{a\mu_\eta}{2}L(U).
\tag{28}
\]
Take
\[
c=\min\{1/100,1/(2C_0)\}.
\tag{29}
\]
For `a<=c eta^3`, the retained excess has nonnegative coefficient.
Since good multiplicities are one or two, `L(P)=sum_P m_i^2`;
`2m_i m_j<=m_i^2+m_j^2` and the negativity of `v` make the
pair sum in (28) at least `v L(P)`. Also
`-a mu_eta L(U)/2>=v L(U)` and `0>=v L(Bcal)`.
Dropping the remaining nonnegative excess gives
\[
E_{J_{\eta,a}}(W)\ge(1-a\eta+v)L(W).
\tag{30}
\]
A simple pair at a minimizing separation realizes equality, proving
(4). No compactness argument in growing cardinality is needed.

For completeness, the opposite scale is already certified by ANF-207.
Every multiset supported on at most two real sites obeys
\[
E_{J_{\eta,a}}(W)/L(W)\ge1-2a\eta.
\tag{31}
\]
To see this, put `D_m=sum m_i^2`, `N=sum m_i`. Then
`E_0>=D_m>=L`, `N^2<=2D_m`, and `E_tau<=eta N^2`;
use `2a eta<1`. ANF-207's finite lattice, of integer spacing
`ceil(a^(-1/3))` and span at most `1/(2eta)`, satisfies
\[
q^{\mathbb R}_{\eta,a}\le1-\frac{a^{4/3}}{2\pi^2}
\le1-4a\eta<1-2a\eta
\tag{32}
\]
under (5). Its conditions `eta<=a^(1/3)/4` and `a<=1/20`
hold throughout that range. This proves (5)--(6).

## Prior art, audit and remaining boundary

The kernel is classical: [Carneiro--Chandee--Littmann--Milinovich,
section 3.5, Corollary 14](https://arxiv.org/pdf/1406.5462) gives its
explicit extremal square. No RH-conditional zero statistic from that
paper is used. [Ruelle's cell occupation-square framework, section 1](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B28%5D.pdf)
is the classical neighboring stability method. [Sütő's compact-Fourier
ground states](https://arxiv.org/pdf/math-ph/0508004) fix density in an
infinite-volume problem; [Procacci's stability constant](https://arxiv.org/pdf/2005.10362)
belongs to the classical pair-potential framework. None is imported as
a finite two-site or shrinking-width theorem.

The contemporary [Knausgård preprint, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
also studies real Montgomery--Taylor pair energy, but imposes an
asymptotic span/density condition and uses periodic trial states. Its
zero-counting claims are not needed or independently certified here.
Searches by the exact kernel, weak attractive perturbations, two-site
ground states and narrow Fourier notches did not identify (4)--(6);
this is a derived specialization, not an exhaustive novelty claim.
The existing source anchors suffice.

The local mathematical delta is the uniform estimate (8), combined
with the **notch** energy of discarded sites in (21). ANF-200's
fixed-profile matching proof then has a constant `O(eta^(-3))`
instead of an unspecified width dependence. ANF-208's two-scale
energy order alone does not imply this exact finite attainment.
Together with ANF-207, the result closes the initial real two-site
window at sharp order; it does not locate its constant.

The decisive audit controls are the inverse-square tail in (11)--(16),
the fourth-power threshold `gamma`, whole-site removal, the sign of
`v` when comparing unequal multiplicities, and exclusion of internal
matching energy from every error budget. In particular an estimate
charging `Delta` instead of `Delta_out` would not prove (4).
Equations (9), (27) and (29) define positive constants without any
numerical optimization. The proof is analytic, not a numerical or Lean
certificate.

As noncertifying falsification checks, ordinary double-precision
calculations with seed 209 tested (8) and (16) at 3,384 combinations
of widths, near-root pair separations and signed observation points,
including distant tails. Another 320 real multiset configurations
checked the matching, bad-site budget, good-site row sum and (26),
with one through 26 sites and multiplicities one through seven.
No violation was found. These coarse-constant checks do not establish
the theorem or its optimal constant; the analytic argument above is
the evidence. The explicit choice (29) is deliberately conservative.

Real pair positivity is essential to (17)--(23). Nothing here transfers
the cubic interval to arbitrary conjugation-invariant complex multisets,
closes the fixed-profile complex exposure envelope, classifies the
larger-cluster minimizers, proves nonattainment beyond the two-site
window, improves a zeta-zero proportion, or resolves RH.
