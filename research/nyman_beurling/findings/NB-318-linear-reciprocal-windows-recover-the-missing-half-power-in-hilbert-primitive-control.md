# NB-318 — Linear reciprocal windows recover the missing half-power in Hilbert primitive control

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-303, NB-315, NB-316, NB-317
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + PHASE-SPACE + WINDOW-LOCALIZATION + CENTERED-PRIMITIVE + FAREY-DENOMINATOR + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
F_u(t):=u(1/t),
\qquad
\widetilde F_u(t):=F_u(t)-\mu_N(u),
\]

and

\[
G_u(T):=\int_0^T\widetilde F_u(s)\,ds.
\]

Use the centered Cesàro shell energy `Q_N^0` and the reduced-denominator quantities from `NB-317`,

\[
Q_N^0(u)=\sum_{q=2}^NW(q)|B_q(u)|^2,
\qquad
W(q)=\frac{J_2(q)}{12},
\]

\[
G_u(K)=-\sum_{q=2}^NB_q(u)D_q(K)
\qquad(K\in\mathbb Z_{\ge0}).
\]

The apparent `N^(3/2)` Cesàro-to-primitive loss of `NB-317` is not a long-period phenomenon. It is already saturated at reciprocal time `K=Theta(N)`. At the same time, the physical Nyman `L^2(0,1)` norm recovers the missing half-power uniformly on every bounded linear reciprocal-time window.

More precisely, for `r>=1` put

\[
s_r(K):=K\bmod r\in\{0,\ldots,r-1\}.
\]

Then the reduced-denominator primitive kernel has the exact arithmetic formula

\[
\boxed{
D_q(K)
=\frac12\sum_{d\mid q}\mu(d)\,
s_{q/d}(K)\bigl(q/d-s_{q/d}(K)\bigr).
}
\tag{1}
\]

Define the fixed-time Cesàro evaluation norm

\[
\mathcal A_N(K)
:=
\sup_{0\ne u\in U_N}
\frac{|G_u(K)|}{\sqrt{Q_N^0(u)}}.
\tag{2}
\]

Let

\[
M:=2\left\lfloor\frac N2\right\rfloor,
\qquad
K_N:=\frac M2=\left\lfloor\frac N2\right\rfloor,
\]

and

\[
\kappa
:=
\frac19-rac{\zeta(2)-1}{8}
=0.030494\ldots>0.
\tag{3}
\]

For every `N>=4`,

\[
\boxed{
\mathcal A_N(K_N)
\ge
\frac{3\sqrt3}{4}\,\kappa\,M^{3/2}.
}
\tag{4}
\]

Together with `NB-317`, this gives

\[
\boxed{
\mathcal A_N(K_N)=\Theta(N^{3/2}).
}
\tag{5}
\]

Thus the sharp Cesàro primitive exponent is already visible in the first `N/2` reciprocal cells; the common period `lcm(2,...,N)` used in the averaging proof of `NB-317` is not responsible for the sharp lower exponent.

Now define the Hilbert-normalized fixed-time evaluation norm

\[
\mathcal H_N(K)
:=
\sup_{0\ne u\in U_N}
\frac{|G_u(K)|}{\|u\|_2}.
\tag{6}
\]

For every integer `K>=1`,

\[
\boxed{
\mathcal H_N(K)
\le
\sqrt{\frac{(K-1)K(K+1)}{3}}
+
K\sqrt{4N^2+2}.
}
\tag{7}
\]

Consequently, for every fixed `C>0`,

\[
\boxed{
\max_{1\le K\le CN}\mathcal H_N(K)
=O_C(N^2),
}
\tag{8}
\]

and in the same window in which (4) is proved one has the explicit bound

\[
\boxed{
\max_{1\le K\le N/2}\mathcal H_N(K)
<\frac54N^2
\qquad(N\ge2).
}
\tag{9}
\]

Therefore the two multiplicative losses in `NB-315` cannot be simultaneously saturated on bounded linear reciprocal-time windows. If `Q_N^0(u)=1` and, for some `K<=CN`,

\[
|G_u(K)|\gg N^{3/2},
\]

then (8) forces

\[
\boxed{
\|u\|_2\gg_C N^{-1/2},
\qquad
\frac{\sqrt{Q_N^0(u)}}{\|u\|_2}\ll_C N^{1/2}.
}
\tag{10}
\]

The worst-case `sqrt(Q_N^0(u))/||u||_2=O(N)` comparison from `NB-303` therefore loses a half-power on every linear-time profile that is actually primitive-large. This closes the `N^(5/2)` versus `N^2` half-power gap **inside bounded linear reciprocal windows**, but not globally.

The distinction is genuine. The adjacent witness of `NB-316`, which gives the current global lower bound `Pi_N >> N^2/sqrt(log N)`, reaches its exact primitive maximum at reciprocal time

\[
K=b(N-1),
\qquad
b\in\left\{\left\lfloor\frac N2\right\rfloor,
\left\lceil\frac N2\right\rceil\right\},
\tag{11}
\]

hence at `K=Theta(N^2)`, not at linear time. Thus any hypothetical superquadratic growth of the global Hilbert-normalized primitive amplification must come from reciprocal times escaping every bounded multiple of `N`.

This does not improve the moving rank-one mixing threshold of `NB-315`, does not prove `Pi_N=O(N^2)`, and does not address target occupation, first-free gain, or RH.

## 1. A reduced-residue discrete Green formula for `D_q(K)`

Start from the complete-residue identity. For `r>=2` and `s=K mod r`,

\[
E_r(K)
:=
\sum_{a=1}^{r-1}
\frac{1-\cos(2\pi aK/r)}{|1-e^{2\pi ia/r}|^2}
=
\frac{s(r-s)}{2}.
\tag{12}
\]

This is elementary. Since

\[
\frac{1-\cos(2K\theta)}{4\sin^2\theta}
=\frac12\frac{\sin^2(K\theta)}{\sin^2\theta},
\]

when `theta=pi a/r`, equation (12) is equivalent to

\[
\sum_{a=1}^{r-1}
\frac{\sin^2(\pi a s/r)}{\sin^2(\pi a/r)}
=s(r-s).
\tag{13}
\]

For `0<=s<r`, expand `sin(s theta)/sin(theta)` as a finite geometric sum of unit complex phases. Summing its squared modulus over the nontrivial `r`-th roots of unity leaves exactly `rs-s^2`, proving (13).

To restrict to reduced residues, use

\[
\mathbf 1_{(a,q)=1}
=
\sum_{d\mid(a,q)}\mu(d).
\]

Inserting this into the definition of `D_q(K)` and writing `a=db`, `r=q/d`, gives

\[
D_q(K)
=
\sum_{d\mid q}\mu(d)E_{q/d}(K),
\]

which is exactly (1). The `q/d=1` term vanishes because `s_1(K)=0`.

Equation (1) is useful here because it makes the dependence on the **evaluation time** explicit. `NB-317` diagonalized the denominator coordinate; (1) additionally localizes the numerator in reciprocal time.

## 2. A deterministic linear time already saturates the Cesàro exponent

Take `M=2 floor(N/2)` and `K=M/2`. Consider denominators

\[
\left\lceil\frac{3M}{4}\right\rceil\le q\le M.
\tag{14}
\]

For every such `q`, one has `K<q` and

\[
\frac12\le\frac Kq\le\frac23.
\]

The `d=1` contribution in (1) is therefore

\[
\frac{K(q-K)}2
\ge
\frac{q^2}{9}.
\tag{15}
\]

For every divisor `d>=2`, with `r=q/d`,

\[
\frac12s_r(K)(r-s_r(K))
\le
\frac{r^2}{8}
=
\frac{q^2}{8d^2}.
\]

Hence, without assuming any cancellation among the remaining Möbius terms,

\[
\begin{aligned}
D_q(K)
&\ge
q^2\left(
\frac19-rac18\sum_{d=2}^{\infty}\frac1{d^2}
\right)\\
&=
\boxed{\kappa q^2}.
\end{aligned}
\tag{16}
\]

The constant `kappa` is positive by (3).

From the exact dual formula of `NB-317`,

\[
\mathcal A_N(K)^2
=
\sum_{q=2}^N\frac{D_q(K)^2}{W(q)}.
\tag{17}
\]

Since

\[
W(q)=\frac{J_2(q)}{12}\le\frac{q^2}{12},
\]

each denominator in the band (14) contributes at least

\[
\frac{D_q(K)^2}{W(q)}
\ge
12\kappa^2q^2.
\tag{18}
\]

There are at least `M/4` integers in (14), each at least `3M/4`, so

\[
\mathcal A_N(K)^2
\ge
12\kappa^2\frac M4\left(\frac{3M}{4}\right)^2
=
\frac{27}{16}\kappa^2M^3.
\tag{19}
\]

Taking square roots proves (4). The upper bound in (5) is immediate from the global estimate of `NB-317`,

\[
\mathcal A_N(K)
\le
\mathcal A_N
\le
2\sqrt{S_N}
=O(N^{3/2}).
\]

The important point is not the constant. The full `N^(3/2)` Cesàro exponent already occurs at the deterministic time `K=floor(N/2)`, long before a common reciprocal period can matter.

## 3. Physical `L^2` geometry caps every linear-time primitive at `O(N^2)`

Let `u_k=F_u(k)` denote the reciprocal-shell values. Every generator has shell value zero at `k=0`, hence `u_0=0`. Therefore for integer `K>=1`,

\[
G_u(K)
=
\sum_{k=1}^{K-1}u_k-K\mu_N(u).
\tag{20}
\]

The exact Nyman norm is

\[
\|u\|_2^2
=
\sum_{k\ge1}\frac{|u_k|^2}{k(k+1)}.
\tag{21}
\]

Weighted Cauchy--Schwarz gives

\[
\begin{aligned}
\left|\sum_{k=1}^{K-1}u_k\right|
&\le
\|u\|_2
\left(\sum_{k=1}^{K-1}k(k+1)\right)^{1/2}\\
&=
\|u\|_2
\sqrt{\frac{(K-1)K(K+1)}3}.
\end{aligned}
\tag{22}
\]

The reciprocal mean is the zero Fourier coefficient of the shell sequence, so

\[
|\mu_N(u)|^2
\le
Q_N(u).
\]

The large-sieve shell estimate of `NB-303` gives

\[
Q_N(u)
\le
(4N^2+2)\|u\|_2^2.
\tag{23}
\]

Combining (20)--(23) yields (7).

If `K<=CN`, equation (7) gives

\[
\mathcal H_N(K)
\le
\frac{C^{3/2}}{\sqrt3}N^{3/2}
+C\sqrt{4+2/N^2}\,N^2,
\tag{24}
\]

which proves (8). In particular, if `K<=N/2` and `N>=2`, then

\[
\frac{\mathcal H_N(K)}{N^2}
\le
\frac1{\sqrt{24N}}
+
\frac12\sqrt{4+\frac2{N^2}}
<\frac54,
\]

proving (9).

This estimate uses the physical reciprocal-shell weights `1/[k(k+1)]`. It is therefore exactly the kind of phase-space information that the pure Cesàro metric of `NB-317` discards.

## 4. The known adjacent obstruction lives at quadratic reciprocal time

For the adjacent witness

\[
u_N=g_N-\frac{N-1}{N}g_{N-1},
\]

`NB-316` writes the primitive minimum in block `a` as

\[
Q_a
=-\frac{(a+1)(N-1-a)}{2N}.
\]

That minimum occurs after `N-1-a` cells of the block beginning at `aN`, hence at

\[
K_a
=aN+(N-1-a)
=(a+1)(N-1).
\tag{25}
\]

Writing `b=a+1`, the maximizing factor is `b(N-b)`. It is largest for `b` nearest `N/2`, proving (11). Thus the explicit witness which currently forces

\[
\Pi_N\gg\frac{N^2}{\sqrt{\log N}}
\]

uses a primitive excursion of quadratic reciprocal duration.

This does not prove that all near-quadratic Hilbert amplification must occur at quadratic time. It does prove the sharper one-sided statement supplied by (8): **no superquadratic Hilbert-normalized primitive amplification can occur at any bounded linear reciprocal time**.

## 5. Consequence for the primitive route

`NB-315` obtained its global primitive bound by multiplying

\[
\|G_u\|_\infty
\lesssim
N^{3/2}\sqrt{Q_N^0(u)}
\]

by the global comparison

\[
\sqrt{Q_N^0(u)}\lesssim N\|u\|_2.
\]

`NB-317` proved that the first factor is genuinely sharp in its own metric. The present result shows why that does not force a global `N^(5/2)` Hilbert loss: at the deterministic linear time which already saturates the first factor, the second factor can contribute at most another `N^(1/2)` on a primitive-large vector, not `N`.

So the remaining global half-power window has acquired a concrete phase-space location. To realize growth above `N^2`, a sequence must move its relevant primitive evaluation time beyond every fixed multiple of `N`. The adjacent witness demonstrates that the known lower-bound mechanism indeed migrates as far as `Theta(N^2)`.

This narrows the next useful question to a long-window problem: control `G_u(K)` relative to `||u||_2` uniformly for `N<<K<=O(N^2)`, rather than further optimizing the already sharp reduced-denominator Cesàro count.

## 6. Prior-art audit and boundary

A fresh search covered the neighboring Nyman--Beurling Fourier/Gram literature, including the Fourier-based estimates of Maier--Rassias, Werner Ehm's Gram/reciprocity analysis, and recent multiscale Gram work of Carvill. It also checked the classical finite trigonometric-sum/discrete-cycle Green-function neighborhood behind (12). The complete-residue identity (12), Möbius inclusion-exclusion, and the resulting reduced-residue arithmetic are classical elementary ingredients; no novelty is claimed for them individually.

I did not identify in the reviewed material the line-specific combination used here: reduced-denominator primitive evaluation localized at `K=Theta(N)`, together with the physical reciprocal-shell weights to prove an `O(N^2)` Hilbert cap on every bounded linear window and thereby separate the two losses in `NB-315`. This is an audit result, not a bibliographic novelty claim.

No external theorem is load-bearing: equations (1), (4), and (7) are derived above from finite Fourier/root-of-unity algebra, Möbius inversion, weighted Cauchy--Schwarz, and the already canonical `NB-303` shell bound. Therefore `SOURCES.md` requires no new dependency.

## 7. Falsification and limits

The most direct audit is finite and exact. For small `q,K`, compute `D_q(K)` both from its reduced-residue definition in `NB-317` and from (1); they must agree. The lower-bound constant in (16) uses only the `d=1` term and the absolute worst-case sum over `d>=2`, so a sign or residue error would show immediately in this comparison.

For the Hilbert estimate, the fragile point is the centering term. Equation (20) includes `-K mu_N(u)` explicitly; omitting it would incorrectly improve the power. The only bound used on that term is `|mu_N(u)|^2<=Q_N(u)<=(4N^2+2)||u||_2^2`, so (7) does not assume an unproved uniform bound on the mean functional.

The result is source-side and windowed. It neither controls the target's occupation of any primitive-large direction nor rules out `Pi_N` growing faster than `N^2` because the global supremum ranges over arbitrarily late reciprocal times. It also does not improve the `m/N^2->infinity` sufficient rank-one mixing regime of `NB-315`; turning the window localization into such an improvement would require a new estimate that keeps track of where the integration-by-parts weight samples the primitive.