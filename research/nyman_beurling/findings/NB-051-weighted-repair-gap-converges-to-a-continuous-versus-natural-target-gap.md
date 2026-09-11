# NB-051 — weighted repair gap converges to a continuous-versus-natural target gap

**Status:** `EXACT-DERIVED + TWO-SCALE-LIMIT + TARGET-PROJECTION-NORMAL-FORM + DECISIVE-MESH-ERROR-OBSTRUCTION`. `NB-050` identifies the recursive weighted-repair slack with the finite enrichment gap between the reciprocal-integer Báez-Duarte section and the denser finite Nyman grid

\[
\mathcal C_{M,N}
=
\operatorname{span}\{\rho_{M/n}:M<n\le N\},
\qquad
\rho_\theta(x)=\left\{\frac\theta x\right\}-\theta\left\{\frac1x\right\}.
\]

That gap is not generically a discretization error that must disappear merely because `M` grows. In the genuine two-scale regime `M->infinity` and `N/M->infinity`, it converges exactly to a **global target-projection gap between the full continuous Nyman closure and the natural Báez-Duarte closure**. At fixed aspect ratio it need not shrink at all: for every even `M`, the section `C_(M,2M)` already improves the natural `K=2` section by an absolute amount at least `1/324` in squared target distance.

Let

\[
\mathcal B_{\mathrm{cont}}
:=
\overline{\operatorname{span}}
\{\rho_\theta:0<\theta\le1\},
\qquad
\mathcal B_{\mathrm{nat}}
:=
\overline{\operatorname{span}}
\{\rho_{1/j}:j\ge2\}
\]

inside `L^2(0,1)`, and write

\[
d_{\mathrm{cont}}
:=\operatorname{dist}(e,\mathcal B_{\mathrm{cont}}),
\qquad
d_{\mathrm{nat}}
:=\operatorname{dist}(e,\mathcal B_{\mathrm{nat}}),
\qquad e(x)=1.
\]

Since `B_nat subseteq B_cont`, define the nonnegative target gap

\[
\boxed{
\Delta_*:=d_{\mathrm{nat}}^2-d_{\mathrm{cont}}^2
=\|P_{\mathcal B_{\mathrm{cont}}}e-P_{\mathcal B_{\mathrm{nat}}}e\|^2.
}
\tag{1}
\]

For any integer sequences `(M_r,N_r)` satisfying

\[
M_r\to\infty,
\qquad
\frac{N_r}{M_r}\to\infty,
\tag{2}
\]

put

\[
K_r=\left\lfloor\frac{N_r}{M_r}\right\rfloor,
\qquad
\delta_{M_r,N_r}
=\operatorname{dist}(e,\mathcal C_{M_r,N_r}).
\]

Then

\[
\boxed{
\delta_{M_r,N_r}\longrightarrow d_{\mathrm{cont}},
\qquad
d_{K_r}\longrightarrow d_{\mathrm{nat}},
}
\tag{3}
\]

and hence

\[
\boxed{
d_{K_r}^2-\delta_{M_r,N_r}^2
\longrightarrow
\Delta_*.
}
\tag{4}
\]

Using the exact `NB-050` identity

\[
\widetilde d_{M,N}^2-d_N^2
=
\frac{d_{\lfloor N/M\rfloor}^2-\delta_{M,N}^2}{M},
\tag{5}
\]

one obtains the repair normal form

\[
\boxed{
M_r\bigl(\widetilde d_{M_r,N_r}^2-d_{N_r}^2\bigr)
\longrightarrow
\Delta_*.
}
\tag{6}
\]

Thus the first-order `1/M` repair slack is governed by a fixed target component in the extra continuous Nyman directions, not by the local mesh size alone.

## 1. The sampled finite spaces converge to the full continuous Nyman closure

The only analytic input needed is continuity of the Nyman generator map

\[
(0,1]\ni\theta\longmapsto\rho_\theta\in L^2(0,1).
\tag{7}
\]

Suppose `theta_j -> theta`. For almost every `x`, the number `theta/x` is not an integer, so the fractional-part map is continuous at that point and

\[
\left\{\frac{\theta_j}{x}\right\}
\longrightarrow
\left\{\frac\theta x\right\}.
\]

The exceptional set `{theta/k:k>=1}` is countable. Moreover `|rho_theta(x)|<=1` for `0<theta<=1`. Dominated convergence therefore gives

\[
\boxed{
\|\rho_{\theta_j}-\rho_\theta\|_2\longrightarrow0.
}
\tag{8}
\]

Now fix a finite continuous Nyman combination

\[
f=\sum_{i=1}^s c_i\rho_{\theta_i},
\qquad 0<\theta_i<1.
\tag{9}
\]

For each `i`, choose integers `n_{i,r}` with

\[
\frac{M_r}{n_{i,r}}\longrightarrow\theta_i.
\tag{10}
\]

For example one may take a nearest integer to `M_r/theta_i`. Because `M_r -> infinity`, eventually `n_(i,r)>M_r`; because `N_r/M_r -> infinity`, eventually `n_(i,r)<=N_r`. Hence

\[
f_r:=\sum_{i=1}^s c_i\rho_{M_r/n_{i,r}}
\in\mathcal C_{M_r,N_r}
\]

and (8) gives `||f_r-f||_2 -> 0`.

Every `C_(M,N)` is contained in `B_cont`, so

\[
\delta_{M,N}\ge d_{\mathrm{cont}}.
\tag{11}
\]

Conversely, approximate the target by a finite `f` with

\[
\|e-f\|_2<d_{\mathrm{cont}}+\varepsilon
\]

and then use `f_r`. This yields

\[
\limsup_r\delta_{M_r,N_r}
\le d_{\mathrm{cont}}+\varepsilon.
\]

Since `epsilon>0` is arbitrary, the first limit in (3) follows. The second is the standard monotone finite-section convergence

\[
V_K=\operatorname{span}(\rho_{1/2},\ldots,\rho_{1/K})
\uparrow \mathcal B_{\mathrm{nat}},
\]

and `K_r -> infinity` follows from (2). Equation (4) is immediate.

Finally, because the two closed spaces are nested, orthogonal projection gives

\[
\|P_{\mathcal B_{\mathrm{cont}}}e\|^2
-
\|P_{\mathcal B_{\mathrm{nat}}}e\|^2
=
\|P_{\mathcal B_{\mathrm{cont}}}e-P_{\mathcal B_{\mathrm{nat}}}e\|^2,
\]

which is exactly (1).

## 2. Fixed aspect ratio does not produce a small mesh gap

There is a simple exact control showing why one must not interpret the `NB-050` quantity as ordinary discretization error.

Take any even integer `M>=2` and put `N=2M`. Then

\[
K=\left\lfloor\frac NM\right\rfloor=2,
\qquad
V_2=\operatorname{span}(g_2),
\qquad g_2=\rho_{1/2}.
\]

The finite continuous grid contains both

\[
\rho_{M/(2M)}=\rho_{1/2}=g_2
\]

and, because `3M/2` is an integer,

\[
\rho_{M/(3M/2)}=\rho_{2/3}.
\]

Put `h=rho_(2/3)`. We show that this one off-grid direction already gives a uniform improvement.

Use `t=1/x`. On the harmonic shell `t in [k,k+1)`, writing `t=k+u`, `0<=u<1`, one has

\[
g_2=
\begin{cases}
0,&k\text{ even},\\
1/2,&k\text{ odd}.
\end{cases}
\tag{12}
\]

Hence the projection of `e` onto `V_2` is exactly `2g_2`, and the residual

\[
r_2=e-2g_2
\tag{13}
\]

is the indicator of the union of the even harmonic shells.

For `h=rho_(2/3)`, the same shell calculation gives

\[
h=
\begin{cases}
0,&k\equiv0\pmod3,\\
2/3,&k\equiv1\pmod3,\ 0\le u<1/2,\\
-1/3,&k\equiv1\pmod3,\ 1/2\le u<1,\\
1/3,&k\equiv2\pmod3.
\end{cases}
\tag{14}
\]

Since `dx=dt/t^2`, only even shells contribute to `<r_2,h>`. For `k congruent 2 mod 6`, the contribution is

\[
\frac13\left(\frac1k-\frac1{k+1}\right)>0.
\tag{15}
\]

For `k congruent 4 mod 6`, it is

\[
\frac{2}{3k}
-
\frac1{k+1/2}
+
\frac1{3(k+1)}
=
\frac{k+2}{3k(k+1)(2k+1)}>0.
\tag{16}
\]

The even shells with `k congruent 0 mod 6` contribute zero. In particular the first contributing shell, `k=2`, already gives

\[
\boxed{
\langle r_2,h\rangle\ge\frac1{18}.
}
\tag{17}
\]

Let

\[
v=(I-P_{V_2})h.
\]

Then `v perp V_2`, `<r_2,v>=<r_2,h>`, and `||v||<=||h||<=1`. Adding the line `span(v)` to `V_2` therefore decreases the squared target distance by

\[
\frac{|\langle r_2,v\rangle|^2}{\|v\|^2}
\ge
\frac1{324}.
\tag{18}
\]

Because `span(g_2,h) subseteq C_(M,2M)`, we obtain the uniform lower bound

\[
\boxed{
d_2^2-\delta_{M,2M}^2\ge\frac1{324}
\qquad(M\text{ even}).
}
\tag{19}
\]

Thus sending `M -> infinity` while keeping `N/M=2` does **not** make the finite enrichment gap small. The grid acquires finer local parameter spacing near its existing range, but it does not extend toward `theta=0`, and the extra continuous directions remain target-bearing.

## 3. Consequence for the recursive-repair route

`NB-050` left open the possibility that

\[
d_{\lfloor N/M\rfloor}^2-\delta_{M,N}^2
\]

might be a cheap finite mesh correction even when the whole smaller-section distance `d_floor(N/M)^2` is not. The present result separates what is true from what would still need arithmetic input.

When both scales grow as in (2), the gap has the deterministic limit `Delta_*`. Therefore an estimate based only on sampling density can at best recover

\[
\boxed{
\widetilde d_{M,N}^2-d_N^2
=
\frac{\Delta_*+o(1)}{M}.
}
\tag{20}
\]

To improve this to `o(1/M)` in such a regime one must prove

\[
\boxed{
P_{\mathcal B_{\mathrm{cont}}}e
=
P_{\mathcal B_{\mathrm{nat}}}e,
}
\tag{21}
\]

or obtain a finite cancellation that is stronger than the generic two-scale limit. Equation (21) is a target statement, not an equality of the two closed spaces.

Under RH, both target distances are zero by the classical Nyman--Beurling and Báez-Duarte criteria, so `Delta_*=0`. The converse is **not** established here: it is logically possible that `d_cont=d_nat>0`, so (21) must not be advertised as another RH equivalence without a separate theorem. This distinction makes `Delta_*` a potentially weaker source-specific object worth isolating, but not yet a route to RH.

The fixed-ratio control (19) also prevents a common false shortcut. A proof that the parameter mesh `M/n` is locally fine does not imply the target gap is small; the accessible parameter interval must itself expand toward zero, and even then the limit is `Delta_*`, not automatically zero.

## 4. Prior-art boundary and audit conditions

The full continuous Nyman family and the natural reciprocal-integer strengthening are classical. Báez-Duarte's strengthening, already anchored in `SOURCES.md`, proves the RH-equivalence of target membership in the natural closure; it does not supply the finite `C_(M,N)` two-scale limit above or an unconditional equality of the two target projections. A targeted audit over continuous-versus-natural Nyman spaces, finite parameter grids, Hilbert-space distances, projection formulations, and recent Gram/multiscale work found no additional theorem needed for (3)--(6) or for the explicit control (19). Search absence is not a priority claim, and no new load-bearing literature dependency is introduced, so `SOURCES.md` is unchanged.

The first half of the finding can be falsified at two elementary points: failure of the `L^2` continuity (8), or failure of the sampled parameters `M/n` to approximate every fixed `theta in (0,1)` under (2). Once those hold, (3)--(6) are Hilbert-space closure algebra. The fixed-ratio lower bound can be audited independently by checking the shell formulas (12)--(16); it uses no numerical approximation or zeta hypothesis.

The line-local consequence is a sharper interpretation of the `NB-050` oracle. The missing repair data are not merely an unknown finite discretization constant. In the only regime where the finite grid approaches the full continuous family, they converge to the target component carried by `B_cont` beyond `B_nat`. Any successful source-only repair below the `NB-049` ambient threshold must therefore explain why that target component vanishes, cancels at finite scale, or can be bounded without reconstructing equivalent full-section target information.