# RE-163 — Chebyshev modes diagonalize sharp approximate terminal leakage

**Status:** `EXACT-DERIVED + CHEBYSHEV-SPECTRAL-DECOMPOSITION + SHARP-APPROXIMATE-LEAKAGE-LAW + ENDPOINT-HIDDEN-MODE-OBSTRUCTION + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-160, RE-161, RE-162.

`RE-161` showed that approximate matching of raw terminal moments leaks into the Robin coordinate before the factorial Taylor remainder, while `RE-162` showed that **exact** matching through degree `r-1` has a much sharper Chebyshev capacity,

\[
D_{r,U}(L)
=(4+o(1))\frac{(L/4)^r}{r!}.
\]

These two statements leave a natural gap: what is the correct error coordinate when lower moments are only approximately matched but one wants to retain the sharp `RE-162` scale rather than the coarser endpoint-Taylor scale of `RE-161`?

The answer is that the terminal kernel itself selects the basis. After mapping `[0,L]` to `[-1,1]`, its Chebyshev expansion has positive coefficients whose leading law is

\[
A_j
=(2+o(1))\frac{(L/4)^j}{j!}.
\]

Consequently, approximate terminal leakage is diagonal in the Chebyshev moments. The sharp exact-match remainder of `RE-162` is literally the unresolved Chebyshev tail, while approximate lower-moment errors enter as the resolved low modes with the same `4^{-j}` geometry.

Let

\[
U:=U_A(p),
\qquad
G_U(z)
:=U\left[
 a(Ue^{-z})-a(U)
 +\frac{a(U)}{\log U}z
\right],
\qquad
a(t):=-\log(1-t^{-1}),
\tag{1}
\]

as in `RE-160`--`RE-162`. Let `L=L_p=o(1)`, let `r=r(p)>=2`, and retain the `RE-162` growing-order condition

\[
\rho_{r,U,L}
:=\frac{2^{r-1}e^L}{U}
=o(1).
\tag{2}
\]

For two equal-cardinality terminal packets with empirical probability measures `mu_1,mu_2` on `[0,L]`, put

\[
\nu:=\mu_1-\mu_2,
\qquad
x(z):=\frac{2z}{L}-1,
\tag{3}
\]

and define their normalized Chebyshev-moment discrepancies

\[
\chi_j
:=\int T_j(x(z))\,d\nu(z),
\qquad j\ge0.
\tag{4}
\]

Equal cardinality gives `chi_0=0`, and because each packet is a probability measure,

\[
|\chi_j|\le2.
\tag{5}
\]

Then there are positive coefficients `A_j=A_j(U,L)` such that

\[
\boxed{
\int G_U\,d\nu
=
\sum_{j\ge1}A_j\chi_j
}
\tag{6}
\]

with absolute convergence. Uniformly for `1<=j<=r`,

\[
\boxed{
A_j
=(2+o(1))\frac{(L/4)^j}{j!},
}
\tag{7}
\]

and the unresolved tail satisfies

\[
\boxed{
\sum_{j\ge r}A_j
=(2+o(1))\frac{(L/4)^r}{r!}.
}
\tag{8}
\]

Therefore, with the signed low-mode leakage

\[
\mathcal L_r(\nu)
:=\sum_{j=1}^{r-1}A_j\chi_j,
\tag{9}
\]

one has the sharp decomposition

\[
\boxed{
\int G_U\,d\nu
=
\mathcal L_r(\nu)+R_r(\nu),
\qquad
|R_r(\nu)|
\le
(4+o(1))\frac{(L/4)^r}{r!}.
}
\tag{10}
\]

For separate control of the lower Chebyshev moments, define

\[
\mathfrak C_r(\nu)
:=
\sum_{j=1}^{r-1}
\frac{(L/4)^j}{j!}|\chi_j|.
\tag{11}
\]

Equations (7)--(10) give the coordinate-wise robust bound

\[
\boxed{
\left|\int G_U\,d\nu\right|
\le
(2+o(1))\mathfrak C_r(\nu)
+(4+o(1))\frac{(L/4)^r}{r!}.
}
\tag{12}
\]

This is the sharp-scale approximate analogue of `RE-162`. Exact matching of the first `r-1` ordinary moments forces `chi_j=0` for `j<r`, because every `T_j(2z/L-1)` is a polynomial of degree `j`; then (12) collapses exactly to the sharp Chebyshev capacity upper bound.

## 1. The terminal kernel has an exact positive Chebyshev spectrum

The exact absolutely convergent series from `RE-161` is

\[
G_U(z)
=
U\sum_{n\ge1}\frac{e^{nz}-1}{nU^n}
+\frac{Ua(U)}{\log U}z.
\tag{13}
\]

Write `z=L(x+1)/2`. For `t>=0`, define the modified-Bessel coefficients by their absolutely convergent series

\[
I_j(t)
:=
\sum_{m\ge0}
\frac{(t/2)^{2m+j}}{m!(m+j)!}.
\tag{14}
\]

Grouping the Fourier modes in the exponential series gives the classical identity

\[
e^{tx}
=I_0(t)+2\sum_{j\ge1}I_j(t)T_j(x),
\qquad -1\le x\le1.
\tag{15}
\]

Applying (15) termwise to (13) yields

\[
G_U\!\left(\frac L2(x+1)\right)
=A_0+\sum_{j\ge1}A_jT_j(x),
\tag{16}
\]

where, for `j>=2`,

\[
\boxed{
A_j
=2U\sum_{n\ge1}
\frac{e^{nL/2}I_j(nL/2)}{nU^n},
}
\tag{17}
\]

and

\[
\boxed{
A_1
=2U\sum_{n\ge1}
\frac{e^{nL/2}I_1(nL/2)}{nU^n}
+\frac{Ua(U)}{\log U}\frac L2.
}
\tag{18}
\]

Every term is nonnegative, and in fact `A_j>0`. Since the Chebyshev series is absolutely and uniformly convergent on `[-1,1]`, integrating (16) against `nu` proves (6).

The representation is useful conceptually as well as technically. The raw Taylor coefficients of `RE-161` mix strongly after the interval is rescaled. In contrast, (6) says that the response of the full nonlinear terminal kernel is already diagonal in the bounded coordinates `chi_j`.

## 2. The coefficient law contains the same factor four as the exact capacity

The `n=1` term in (17) is dominant. From (14), uniformly for `j>=1` while `L=o(1)`,

\[
I_j(L/2)
=
\frac{(L/4)^j}{j!}
\left(1+O\!\left(\frac{L^2}{j+1}\right)\right).
\tag{19}
\]

Also,

\[
I_j(t)
\le
\frac{(t/2)^j}{j!}e^t,
\qquad t\ge0,
\tag{20}
\]

which follows directly from (14) using `(m+j)!>=j!m!` and `I_0(t)<=e^t`.

For `j<=r`, (20) bounds the contribution of all `n>=2` terms relative to the `n=1` scale by

\[
\sum_{n\ge2}
\frac{n^{j-1}e^{nL}}{U^{n-1}}
\le
 e^L
\sum_{n\ge2}
\left(
\frac{2^{r-1}e^L}{U}
\right)^{n-1}
=o(1),
\tag{21}
\]

where `n<=2^{n-1}` and (2) were used. For `j=1`, the extra linear coefficient in (18) is only a relative `O(1/log U)` correction because

\[
Ua(U)=1+O(U^{-1}).
\tag{22}
\]

Equations (19)--(22) prove (7).

The tail retains the same constant. For the `n=1` term,

\[
\sum_{j\ge r}I_j(L/2)
=
(1+o(1))\frac{(L/4)^r}{r!}.
\tag{23}
\]

For `n>=2`, summing (20) first over `j>=r` gives

\[
\sum_{j\ge r}
\frac{n^{j-1}(L/4)^j}{j!}
\le
n^{r-1}\frac{(L/4)^r}{r!}e^{nL/4}.
\tag{24}
\]

Hence their total contribution is bounded by a geometric series with ratio

\[
\frac{2^{r-1}e^{5L/4}}{U}
=o(1),
\tag{25}
\]

which is equivalent to (2) because `L=o(1)`. Thus the `n>=2` tail is lower order, and (8) follows from (23).

Finally, (5) and (8) imply

\[
\left|
\sum_{j\ge r}A_j\chi_j
\right|
\le
2\sum_{j\ge r}A_j
=(4+o(1))\frac{(L/4)^r}{r!},
\tag{26}
\]

proving (10). This gives a spectral explanation of the constant in `RE-162`: its sharp `4(L/4)^r/r!` envelope is twice the positive Chebyshev tail because the difference of two probability measures has mode amplitude at most `2`.

## 3. Approximate stability at the sharp radius is a Chebyshev leakage condition

Retain

\[
\eta_p
:=\frac{\log U}{\sqrt p\log p},
\qquad
\tau_r:=(r!\eta_p)^{1/r}.
\tag{27}
\]

For insertion budget

\[
m_p
=(1+o(1))\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\tag{28}
\]

`RE-160`--`RE-162` give

\[
\Delta\mathcal A_p
=
-\frac{\delta_p}{Z_p\eta_p}
\int G_U\,d\nu
+o(1),
\qquad
Z_p=2+o(1),
\tag{29}
\]

with the harmless rounding error absorbed into `o(1)`. Combining (12) and (29),

\[
\boxed{
|\Delta\mathcal A_p|
\le
\frac{\delta_p}{Z_p\eta_p}
\left[
(2+o(1))\mathfrak C_r(\nu)
+(4+o(1))\frac{(L/4)^r}{r!}
\right]
+o(1).
}
\tag{30}
\]

Thus the exact quantitative stability condition for this coordinate-wise control is

\[
\boxed{
\frac{\delta_p}{\eta_p}
\left[
\mathfrak C_r(\nu)
+rac{(L/4)^r}{r!}
\right]
\longrightarrow0.
}
\tag{31}
\]

At the sharp `RE-162` radius

\[
L=4\tau_r,
\tag{32}
\]

one has

\[
\frac{(L/4)^r}{r!}=\eta_p.
\tag{33}
\]

Therefore a budget-independent sufficient condition that preserves the sharp exact-match scale under every `delta_p->0` is

\[
\boxed{
\mathfrak C_r(\nu)=O(\eta_p).
}
\tag{34}
\]

More generally, for a specified vanishing insertion budget, only

\[
\delta_p\mathfrak C_r(\nu)=o(\eta_p)
\tag{35}
\]

is needed. If one has a signed arithmetic identity instead of separate mode bounds, the still weaker exact requirement is on the single scalar

\[
\boxed{
\mathcal L_r(\nu)
=\sum_{j<r}A_j\chi_j,
}
\tag{36}
\]

because cancellation between Chebyshev modes is genuine in (6). This identifies more precisely what a positive CA-specific coupling theorem could target: it need not control every raw moment separately if it controls the kernel-weighted signed spectral leakage.

## 4. Raw moment accuracy is an ill-conditioned description of the sharp problem

Let

\[
\mu_k:=\int z^k\,d\nu(z)
\tag{37}
\]

be the raw average discrepancies of `RE-161`. The first Chebyshev discrepancies are

\[
\chi_1
=\frac{2\mu_1}{L},
\tag{38}
\]

\[
\chi_2
=\frac{8\mu_2}{L^2}
-\frac{8\mu_1}{L},
\tag{39}
\]

and

\[
\chi_3
=\frac{32\mu_3}{L^3}
-\frac{48\mu_2}{L^2}
+\frac{18\mu_1}{L}.
\tag{40}
\]

The transformation remains triangular at all orders, so exact raw matching and exact Chebyshev matching are equivalent below the cutoff. Approximate matching is different: the coefficients of that triangular transform grow rapidly with degree. Separate small errors in the monomial coordinates can therefore combine into an order-one Chebyshev mode even when every normalized raw discrepancy tends to zero.

The counterexample from `RE-161` makes this mechanism explicit. There the second packet is obtained from the first by a small normalized endpoint displacement

\[
h_p:=\frac{t_p}{L_p}\longrightarrow0,
\tag{41}
\]

with the first packet concentrated at `z/L=o(h_p)` and the translated packet at `z/L=h_p+o(h_p)`. In Chebyshev coordinates the two locations are therefore

\[
x_-= -1+o(h_p),
\qquad
x_+= -1+2h_p+o(h_p).
\tag{42}
\]

Choose any fixed `c>0` for which `cos(2c) != 1`, and let

\[
j_p
:=\left\lfloor\frac{c}{\sqrt{h_p}}\right\rfloor.
\tag{43}
\]

Since

\[
\arccos(-1+2h)
=\pi-2\sqrt h+O(h^{3/2}),
\tag{44}
\]

one gets

\[
T_{j_p}(x_-)
=(-1)^{j_p}+o(1),
\tag{45}
\]

while

\[
T_{j_p}(x_+)
=(-1)^{j_p}\cos(2c)+o(1).
\tag{46}
\]

Hence, after choosing a subsequence if necessary only to fix the parity sign,

\[
\boxed{
|\chi_{j_p}|
\longrightarrow
|1-\cos(2c)|>0.
}
\tag{47}
\]

This occurs simultaneously with the `RE-161` property

\[
\sup_{k\ge1}
\frac{|\mu_k|}{L_p^k}
\longrightarrow0.
\tag{48}
\]

Thus the qualitative obstruction in `RE-161` has a concrete spectral interpretation: **the discrepancy does not disappear; it migrates to a Chebyshev degree `j_p` of order `h_p^{-1/2}` near the endpoint**. Monomials normalized by `L^k` fail to see that mode uniformly because the monomial-to-Chebyshev change of basis becomes increasingly ill-conditioned with degree.

The point is not that Chebyshev moments solve the arithmetic problem automatically. Equation (47) instead shows what information was missing from qualitative raw-moment matching. A theorem that controls the sharp terminal ambiguity must prevent these growing endpoint modes, control their weighted leakage through (31), or produce signed cancellation in (36).

## 5. Relation to `RE-161`, `RE-162`, and the remaining arithmetic frontier

`RE-161` remains correct: its raw-moment budget

\[
\sum_{k<r}\frac{|\mu_k|}{k!}
\tag{49}
\]

is the natural robust cost obtained by retaining the endpoint Taylor coefficients separately. What changes is the interpretation once one asks for the **sharp** `RE-162` scale. The endpoint Taylor basis does not encode the `4^{-r}` minimax gain; the Chebyshev basis does. Equation (12) supplies the corresponding sharp-scale leakage norm.

`RE-162` is recovered as the exact special case `chi_1=...=chi_{r-1}=0`, and its constant `4` is explained directly by the first unresolved Chebyshev coefficient plus the total-variation factor `2`. Conversely, (47) explains why the qualitative all-moment closeness constructed in `RE-161` does not contradict the Chebyshev capacity: the hidden discrepancy lives at a growing spectral degree rather than vanishing uniformly in the bounded polynomial basis.

This sharpens the source-side frontier without changing the generalized-source scope. For the ordinary-prime/CA problem, a useful positive input can now take one of three more precise forms: control the weighted Chebyshev leakage `mathfrak C_r`; force cancellation in the signed kernel-weighted leakage `mathcal L_r`; or impose an arithmetic selector constraint that prevents the endpoint spectral migration (47). The accepted selector-height coupling clue remains open because no such CA-specific identity is proved here.

## 6. Prior-art boundary and scope

Chebyshev expansions of exponentials into modified-Bessel coefficients are classical, and noisy Chebyshev-moment recovery is an active general subject. In particular, Musco--Musco--Rosenblatt--Singh (COLT 2025) study distribution recovery from noisy Chebyshev moments and exploit decay of Chebyshev coefficients for generic test functions. A focused audit also recovers the classical moment-space and Chebyshev-approximation literature already bounded in `RE-162`.

Those results provide context, not a load-bearing theorem here. Equations (13)--(26) derive the coefficient law and tail directly from absolutely convergent series, and the endpoint hidden-mode calculation (41)--(47) is elementary. The audit did not locate the Robin terminal kernel (1), the source normalization (29), the sharp leakage criterion (31)--(35), or the spectral explanation (47) of the `RE-161` generalized-source obstruction. No new external result is therefore needed in `SOURCES.md`.

As with `RE-157`--`RE-162`, this is a matched generalized-source information result. It does not rearrange the ordinary primes, does not construct a Robin counterexample, and does not establish the missing CA-specific coupling. Its contribution is to identify the **correct sharp approximate coordinate system** for the terminal placement problem: exact lower moments remove the low Chebyshev modes, approximate lower moments pay precisely through those modes, and the surviving tail is the same `4^{-r}` capacity already pinned by `RE-162`.