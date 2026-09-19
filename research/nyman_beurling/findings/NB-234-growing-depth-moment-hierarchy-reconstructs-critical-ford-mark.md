# NB-234 — A growing depth-moment hierarchy reconstructs the critical Ford mark

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + POSITIVE-REDUCTION + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + DEPTH-MOMENT-HIERARCHY + EXACT-FORD-TRANSITION + NB-233-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-233` shows that even perfect local equidistribution of the unweighted carrier phases can miss an order-one Ford residue: the depth mark

\[
e^{-(YD_\rho-\log J)}
\]

can be correlated with phase and resurrect the first carrier Fourier coefficient. That leaves a more structured possibility than trying to prove the marked estimate directly: control mixed depth--phase moments such as

\[
\frac1J\sum d_\rho^m e^{iX(\gamma-t)}F(Hv_\rho),
\qquad
d_\rho:=YD_\rho-\log J,
\]

and reconstruct the exponential mark from those moments.

On every fixed transition layer `|d_rho|<=C`, this works exactly, but only with a **growing** hierarchy. Taylor expansion gives a factorially accurate reconstruction of the full profiled Ford residue from the mixed moments. Conversely, for every fixed moment order `K`, one can build a Bellotti-compatible matched packet for which all profiled mixed moments of orders `0,...,K` tend to zero while the exact exponentially marked residue stays bounded away from zero. Thus no fixed finite hierarchy of polynomial depth marks can replace the Ford mark. The smallest natural surrogate is a slowly growing family of local profiled depth moments.

The generic ingredients -- Taylor approximation of `e^{-d}` and finite differences annihilating polynomials -- are classical. The line-specific content is their exact insertion into the carrier-width Ford transition and the matched packet showing sharp failure of every fixed hierarchy under the same audited zeta population constraints as `NB-231`--`NB-233`.

## 1. The transition residue is an exponential generating function of profiled depth moments

Use the exact-Ford notation of `NB-230`--`NB-233`:

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR\to Y_*\in(0,\infty),
\]

and work in the conservative carrier regime

\[
J:=\frac RH\to\infty,
\qquad
J\le L.
\tag{1}
\]

Fix `r>0` and a nonzero real `phi>=0` in `C_c^infty((0,1))`. Put

\[
\sigma_X=1+\frac rX,
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{2}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity, define

\[
D_\rho=R(1-\beta),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta),
\qquad
\theta_\rho=X(\gamma-t),
\tag{3}
\]

and the exact profiled carrier coefficient

\[
b_\rho
:=
m(\rho)e^{i\theta_\rho}F(Hv_\rho).
\tag{4}
\]

The residue coefficient from `NB-228` is

\[
m(\rho)L_{X,H}(v_\rho)
=
e^{-r}e^{-YD_\rho}b_\rho.
\tag{5}
\]

Now center normalized depth on the sharp carrier-width threshold of `NB-230`--`NB-231`:

\[
\boxed{
d_\rho:=YD_\rho-\log J.
}
\tag{6}
\]

For fixed `C>0`, let

\[
\mathcal T_C
:=
\{\rho:\ |d_\rho|\le C\}.
\tag{7}
\]

The contribution of this transition layer is exactly

\[
\boxed{
\mathcal Z_C
=
\frac{e^{-r}}J
\sum_{\rho\in\mathcal T_C}
 e^{-d_\rho}b_\rho.
}
\tag{8}
\]

Define its profiled mixed moments

\[
\boxed{
\mathcal M_m(C)
:=
\frac1J
\sum_{\rho\in\mathcal T_C}
 d_\rho^m b_\rho,
\qquad m\ge0.
}
\tag{9}
\]

Bellotti's local count, already converted in `NB-230` into the source-matched population estimate

\[
\sum_{D_\rho\le D}m(\rho)|F(Hv_\rho)|
\ll D+J,
\tag{10}
\]

applies here because

\[
D_\rho
\le
\frac{\log J+C}{Y}
=O(\log L)
=o(L).
\tag{11}
\]

Hence throughout the fixed transition layer

\[
\boxed{
\frac1J
\sum_{\rho\in\mathcal T_C}|b_\rho|
\ll_{C,\phi,Y_*}1.
}
\tag{12}
\]

For an integer `K>=0`, Taylor's formula gives uniformly on `|d|<=C`

\[
e^{-d}
=
\sum_{m=0}^{K}\frac{(-d)^m}{m!}
+R_K(d),
\]

with

\[
|R_K(d)|
\le
 e^C\frac{C^{K+1}}{(K+1)!}.
\tag{13}
\]

Insert this into (8) and use (12). One obtains the exact quantitative reconstruction

\[
\boxed{
\mathcal Z_C
=
e^{-r}
\sum_{m=0}^{K}
\frac{(-1)^m}{m!}\mathcal M_m(C)
+
O_{C,\phi,Y_*}\!\left(
\frac{e^C C^{K+1}}{(K+1)!}
\right).
}
\tag{14}
\]

Thus the marked Ford coefficient is the exponential generating function of the local profiled depth moments, up to a factorial tail.

## 2. A slowly growing moment theorem would be sufficient

Equation (14) gives a precise substitute for a direct theorem on the exponential mark. Let `K=K(Q)->infinity`. If actual zeta zeros satisfy

\[
\boxed{
\max_{0\le m\le K(Q)}
|\mathcal M_m(C)|
=o(1)
}
\tag{15}
\]

uniformly in the carrier windows under consideration, then

\[
\left|
\sum_{m=0}^{K}
\frac{(-1)^m}{m!}\mathcal M_m(C)
\right|
\le
e\max_{m\le K}|\mathcal M_m(C)|
=o(1),
\]

while the remainder in (14) tends to zero. Therefore

\[
\boxed{
(15)
\quad\Longrightarrow\quad
\mathcal Z_C=o(1).
}
\tag{16}
\]

The required growth of `K` can be extremely slow if one only wants a prescribed accuracy. For fixed `C` and `eta->0`, Stirling's formula shows that

\[
\frac{e^C C^{K+1}}{(K+1)!}\le\eta
\]

once

\[
\boxed{
K
=(1+o(1))
\frac{\log(1/\eta)}{\log\log(1/\eta)}.
}
\tag{17}
\]

For example, making the Taylor tail at most `1/log J` needs only

\[
K
\asymp
\frac{\log\log J}{\log\log\log J}.
\tag{18}
\]

This does not prove that moments of these orders are accessible for zeta. It changes the target, however: one does not need a new theorem phrased directly in terms of the nonlinear Ford mark. A sufficiently uniform, slowly growing hierarchy of **profiled local mixed depth--phase moments** would already imply the desired marked cancellation on every fixed transition layer.

The profile in (9) is essential. Dropping `F(Hv_rho)` would return to the projection loss exposed by `NB-233`; (14) retains the exact source-faithful residue coefficient.

## 3. Every fixed finite hierarchy is still blind

The converse boundary is sharp in the matched-control sense. Fix once and for all an integer `K>=0` and a transition width `C>0`. Set

\[
n=K+1,
\qquad
h=\frac{2C}{n},
\qquad
d_j=-C+jh,
\qquad 0\le j\le n,
\tag{19}
\]

and define the signed finite-difference coefficients

\[
\boxed{
c_j=(-1)^j\binom nj.
}
\tag{20}
\]

For every polynomial `p` of degree at most `K`, the `n`-th finite difference vanishes:

\[
\sum_{j=0}^{n}c_j p(d_j)=0.
\tag{21}
\]

In particular,

\[
\boxed{
\sum_{j=0}^{n}c_jd_j^m=0
\qquad(0\le m\le K).
}
\tag{22}
\]

But the exponential mark is not a polynomial of degree `K`:

\[
\boxed{
A_{K,C}
:=
\sum_{j=0}^{n}c_je^{-d_j}
=
e^C(1-e^{-h})^n
>0.
}
\tag{23}
\]

Also

\[
B_K:=\sum_{j=0}^{n}|c_j|=2^n.
\tag{24}
\]

A microblock will contain `|c_j|` points at centered depth `d_j`, with carrier phase `0` when `c_j>0` and phase `pi` when `c_j<0`. Thus the total carrier coefficient of the `d_j` group is exactly `c_j` before the smooth profile is inserted.

Choose a fixed integer `q>=2` and a small fixed `delta>0`. Let

\[
N
=\left\lfloor\frac{\delta J}{B_K}\right\rfloor
\tag{25}
\]

and concatenate `N` such microblocks. Enumerate their `NB_K` points consecutively by an index `ell`. If the required sign of the point is `s_ell in {+1,-1}`, choose `theta_ell=0` for `+1` and `theta_ell=pi` for `-1`, and set

\[
\gamma_\ell
=t+
\frac{2\pi q\ell+\theta_\ell}{X}.
\tag{26}
\]

Then

\[
e^{iX(\gamma_\ell-t)}=s_\ell,
\tag{27}
\]

while consecutive vertical spacings remain `Theta(1/X)=Theta(1/R)`. Give a point belonging to the `d_j` group horizontal depth

\[
D_j=\frac{\log J+d_j}{Y},
\qquad
\beta_j=1-\frac{D_j}{R}.
\tag{28}
\]

Every point therefore lies exactly inside `|YD_j-log J|<=C`.

The total packet occupies only a fixed small part of the physical carrier window:

\[
H\max_\ell|\gamma_\ell-t|
=O_{q,Y_*}(\delta).
\tag{29}
\]

Choose `delta` sufficiently small that `Re F(z)>=F(0)/2` throughout the resulting fixed real neighborhood of the origin. The imaginary profile coordinate satisfies

\[
H(\sigma_X-\beta_j)
=
\frac{r}{YJ}+
\frac{D_j}{J}
=O\!\left(\frac{\log J}{J}\right)
=o(1).
\tag{30}
\]

Inside one microblock, both the real and imaginary arguments of `F(Hv)` vary by `O_{K,C}(1/J)`. Since `F` has bounded derivative on the compact region used here, there is a block value `F_s` such that

\[
F(Hv_\ell)=F_s+O_{K,C,\phi}(1/J)
\tag{31}
\]

for every point in that block.

For `0<=m<=K`, equations (22) and (31) give a profiled block moment

\[
\sum_{\ell\in\text{block}}
 d_\ell^m e^{i\theta_\ell}F(Hv_\ell)
=O_{K,C,\phi}(1/J).
\tag{32}
\]

There are `N=Theta(J)` blocks. After the normalization in (9), their total contribution therefore satisfies

\[
\boxed{
\mathcal M_m(C)=O_{K,C,\phi}(1/J)=o(1)
\qquad(0\le m\le K).
}
\tag{33}
\]

Thus **all profiled mixed moments through the prescribed fixed order vanish asymptotically**, not merely the unweighted phase marginal of `NB-233`.

The exponential mark behaves differently. By (23) and (31), one block contributes

\[
F_sA_{K,C}+O_{K,C,\phi}(1/J).
\tag{34}
\]

With `delta` fixed small, every `F_s` in the packet has positive real part bounded below. Hence

\[
\boxed{
\liminf_{Q\to\infty}
\Re\left[
\frac1J
\sum_{\ell}
 e^{-d_\ell}e^{i\theta_\ell}F(Hv_\ell)
\right]
\ge
\frac{\delta F(0)}{4B_K}
A_{K,C}
>0,
}
\tag{35}
\]

after reducing `delta` once if necessary to absorb the floor in (25) and the profile error. Multiplying by `e^{-r}` gives an order-one exact Ford residue.

Equations (33)--(35) are the promised separation: **any predetermined finite polynomial depth hierarchy can look asymptotically perfectly decorrelated while the nonlinear Ford mark remains macroscopically correlated with carrier phase.**

## 4. The matched packet remains inside the audited zeta population envelope

The construction has the same conservative geometry as `NB-231`--`NB-233`. Its total population is

\[
M=NB_K=\delta J+O_K(1)
\le O(L),
\tag{36}
\]

and every point has

\[
D_j=\frac{\log J+O_{K,C}(1)}{Y}
=O(\log L).
\tag{37}
\]

Thus it stays in the same growing-density range previously audited. Its vertical spacing is bounded above and below by fixed multiples of `1/R`; consequently a Bellotti disk of radius `K'/R` meets only `O(K')` points. The horizontal modulation among the finitely many depth nodes is `O(1/R)` and does not change that count.

The normalized depth tends to infinity, so the packet eventually lies to the left of every fixed normalized zero-free boundary used in the previous controls. Ordinary zero counting has ample room for `O(L)` points. Functional-equation reflections and conjugates may be added as in `NB-231`: the reflected near-zero real parts are exponentially suppressed in the selected near-one Ford carrier, while the conjugates are remote from a chosen positive high ordinate.

None of these checks asserts that actual zeta zeros realize the packet. They show only that the population, symmetry, spacing and zero-free inputs already used in this branch do not rule it out. Therefore a theorem controlling only finitely many depth moments cannot be deduced from those inputs strongly enough to kill the critical packet.

## 5. Prior-art and representation boundary

The analytic algebra in (13)--(23) is classical. On a compact interval, polynomial moments determine integration against any continuous mark once the polynomial degree is allowed to grow; Taylor approximation gives the particularly sharp factorial tail for `e^{-d}`. Finite differences annihilating polynomials of bounded degree are equally standard. No novelty is claimed for either fact in isolation.

The source-specific statement is the identification of these two classical mechanisms with the exact zeta carrier left by `NB-233`. The Ford transition mark is not an arbitrary weight: after centering at `YD=log J`, it is exactly `e^{-d}`, and Bellotti's local population law supplies the uniform `O(J)` total profiled mass needed in (12). This turns moment approximation into an exact criterion for the source-faithful residue and lets the finite-difference control be embedded in the same admissible carrier geometry as the earlier matched packets.

The literature audit found neighboring but weaker projections. Landau--Gonek type formulas control exponential zero sums related to `x^rho`, and `NB-228` already records that boundary. Montgomery-type pair-correlation theory and the 2025 work of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh and Goldston--Lee--Schettler--Suriajaya can extract some horizontal information from global pair statistics, but they do not give a uniform `1/H`-window hierarchy of the profiled mixed moments (9) in the moving transition layer. The present result does not use those theorems, so `SOURCES.md` acquires no new load-bearing dependency.

This finding is also not a new fact about the zeros of zeta. Its positive half is a reduction: a growing mixed-moment theorem would suffice. Its negative half is a matched spectral control: every fixed finite hierarchy remains compatible with the audited source constraints.

## 6. Consequence for the live research target

`NB-231` ruled out population-only control, `NB-232` ruled out global pair correlation, and `NB-233` ruled out local unweighted phase equidistribution. The present result sharpens the next step in both directions.

A fixed list of local correlations such as

\[
\sum d_\rho^m e^{iX(\gamma-t)}F(Hv_\rho),
\qquad m=0,1,\ldots,K,
\]

cannot be the missing theorem for any fixed `K`: the packet above kills all of them while keeping the exact residue order one. But one also does not need an opaque new statistic. On each bounded transition layer, the Ford mark is recoverable from a **slowly growing hierarchy** of precisely those moments, with factorial accuracy.

The resulting source-side target is therefore concrete: prove sufficiently uniform cancellation of the profiled local mixed moments (9) for orders `m<=K(Q)` with `K(Q)->infinity`, or prove the equivalent exponentially marked coefficient directly. If the desired error is only inverse-logarithmic in the carrier capacity, the approximation side itself asks for merely `K~log log J/log log log J` moments; the hard part is obtaining any such growing-order zeta theorem uniformly in the `1/H` window and the critical horizontal layer.

The destination bridge remains separate. Even complete control of this transition residue still has to be converted into a quantitative Nyman--Beurling distance statement without re-importing RH in equivalent form.

## Conclusion

The critical Ford mark is neither an irreducibly nonlinear mystery nor something that a fixed number of depth statistics can capture. On `|YD-log J|<=C`, its exact profiled residue is the exponential generating function of the local depth--phase moments, with a factorial Taylor tail. Consequently a slowly growing mixed-moment hierarchy is sufficient.

That growth is genuinely necessary at the level of the currently admitted source information. For every fixed order `K`, a finite-difference packet with `Theta(J)` Bellotti-compatible points makes every profiled moment through order `K` tend to zero while leaving the exact Ford residue bounded away from zero. The next useful zeta input must therefore control a growing depth hierarchy -- or the equivalent Laplace-marked coefficient itself -- rather than add another fixed collection of marginal or mixed statistics.