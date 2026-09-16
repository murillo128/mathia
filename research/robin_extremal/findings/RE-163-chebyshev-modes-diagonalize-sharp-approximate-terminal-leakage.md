# RE-163 — Chebyshev modes diagonalize sharp approximate terminal leakage

**Status:** `EXACT-DERIVED + CHEBYSHEV-SPECTRAL-DECOMPOSITION + SHARP-APPROXIMATE-LEAKAGE-LAW + ENDPOINT-HIDDEN-MODE-OBSTRUCTION + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-160, RE-161, RE-162.

`RE-161` showed that approximate matching of raw terminal moments leaks into the Robin coordinate before the factorial Taylor remainder. `RE-162` then showed that **exact** matching through degree `r-1` has the sharper capacity

\[
D_{r,U}(L)=(4+o(1))\frac{(L/4)^r}{r!}.
\]

The missing question is what approximate-moment coordinate preserves this sharp `4^{-r}` geometry. The terminal kernel itself supplies the answer: after rescaling `[0,L]` to `[-1,1]`, its Chebyshev expansion has positive coefficients

\[
A_j=(2+o(1))\frac{(L/4)^j}{j!}.
\]

Thus approximate terminal leakage is diagonal in Chebyshev moments. Exact lower-moment matching removes the resolved low modes, and the sharp `RE-162` capacity is precisely the unresolved Chebyshev tail.

Let

\[
U:=U_A(p),
\qquad
G_U(z):=U\left[a(Ue^{-z})-a(U)+\frac{a(U)}{\log U}z\right],
\qquad
a(t):=-\log(1-t^{-1}),
\tag{1}
\]

as in `RE-160`--`RE-162`. Let `L=L_p=o(1)`, `r=r(p)>=2`, and assume

\[
\rho_{r,U,L}:=\frac{2^{r-1}e^L}{U}=o(1).
\tag{2}
\]

For two equal-cardinality terminal packets with empirical probability measures `mu_1,mu_2` on `[0,L]`, put

\[
\nu:=\mu_1-\mu_2,
\qquad
x(z):=\frac{2z}{L}-1,
\tag{3}
\]

and define normalized Chebyshev-moment discrepancies

\[
\chi_j:=\int T_j(x(z))\,d\nu(z),
\qquad j\ge0.
\tag{4}
\]

Then `chi_0=0` and `|chi_j|<=2`. There are positive coefficients `A_j=A_j(U,L)` for which

\[
\boxed{
\int G_U\,d\nu=\sum_{j\ge1}A_j\chi_j
}
\tag{5}
\]

with absolute convergence, and uniformly for `1<=j<=r`,

\[
\boxed{
A_j=(2+o(1))\frac{(L/4)^j}{j!}.
}
\tag{6}
\]

Moreover,

\[
\boxed{
\sum_{j\ge r}A_j=(2+o(1))\frac{(L/4)^r}{r!}.
}
\tag{7}
\]

Define the signed low-mode leakage

\[
\mathcal L_r(\nu):=\sum_{j=1}^{r-1}A_j\chi_j
\tag{8}
\]

and the coordinate-wise robust leakage norm

\[
\mathfrak C_r(\nu):=
\sum_{j=1}^{r-1}\frac{(L/4)^j}{j!}|\chi_j|.
\tag{9}
\]

Then

\[
\boxed{
\int G_U\,d\nu=\mathcal L_r(\nu)+R_r(\nu),
\qquad
|R_r(\nu)|\le(4+o(1))\frac{(L/4)^r}{r!},
}
\tag{10}
\]

and therefore

\[
\boxed{
\left|\int G_U\,d\nu\right|
\le(2+o(1))\mathfrak C_r(\nu)
+(4+o(1))\frac{(L/4)^r}{r!}.
}
\tag{11}
\]

This is the sharp-scale approximate analogue of `RE-162`. Exact matching of the ordinary moments through degree `r-1` forces `chi_j=0` for `j<r`, because `T_j(2z/L-1)` is a polynomial of degree `j`; then (11) reduces to the sharp exact-match capacity upper bound.

## 1. Exact positive Chebyshev spectrum of the terminal kernel

The exact series from `RE-161` is

\[
G_U(z)=
U\sum_{n\ge1}\frac{e^{nz}-1}{nU^n}
+\frac{Ua(U)}{\log U}z.
\tag{12}
\]

Write `z=L(x+1)/2`. Define

\[
I_j(t):=
\sum_{m\ge0}\frac{(t/2)^{2m+j}}{m!(m+j)!}.
\tag{13}
\]

Grouping Fourier modes in the exponential series gives

\[
e^{tx}=I_0(t)+2\sum_{j\ge1}I_j(t)T_j(x),
\qquad -1\le x\le1.
\tag{14}
\]

Applying (14) termwise to (12), for `j>=2` one gets

\[
\boxed{
A_j=2U\sum_{n\ge1}
\frac{e^{nL/2}I_j(nL/2)}{nU^n},
}
\tag{15}
\]

while

\[
\boxed{
A_1=2U\sum_{n\ge1}
\frac{e^{nL/2}I_1(nL/2)}{nU^n}
+\frac{Ua(U)}{\log U}\frac L2.
}
\tag{16}
\]

All coefficients are positive. Absolute uniform convergence on `[-1,1]` justifies integration against `nu` and proves (5).

For the coefficient asymptotics, the `n=1` term dominates. From (13),

\[
I_j(L/2)=
\frac{(L/4)^j}{j!}
\left(1+O\left(\frac{L^2}{j+1}\right)\right),
\tag{17}
\]

and, for `t>=0`,

\[
I_j(t)\le\frac{(t/2)^j}{j!}e^t.
\tag{18}
\]

For `j<=r`, the `n>=2` contribution relative to the `n=1` scale is bounded by

\[
\sum_{n\ge2}\frac{n^{j-1}e^{nL}}{U^{n-1}}
\le e^L\sum_{n\ge2}
\left(\frac{2^{r-1}e^L}{U}\right)^{n-1}=o(1),
\tag{19}
\]

using `n<=2^{n-1}` and (2). The extra linear term in `A_1` is a relative `O(1/log U)` correction because `Ua(U)=1+O(U^{-1})`. This proves (6).

For the tail, the `n=1` contribution satisfies

\[
\sum_{j\ge r}I_j(L/2)
=(1+o(1))\frac{(L/4)^r}{r!}.
\tag{20}
\]

For `n>=2`, (18) and

\[
\sum_{j\ge r}\frac{n^{j-1}(L/4)^j}{j!}
\le n^{r-1}\frac{(L/4)^r}{r!}e^{nL/4}
\tag{21}
\]

reduce the total to a geometric series with ratio

\[
\frac{2^{r-1}e^{5L/4}}{U}=o(1),
\tag{22}
\]

which is equivalent to (2) because `L=o(1)`. This proves (7). Finally `|chi_j|<=2` turns (7) into (10), explaining spectrally the constant `4` in `RE-162`: it is twice the positive unresolved Chebyshev tail.

## 2. Sharp approximate stability is a Chebyshev leakage condition

Retain

\[
\eta_p:=\frac{\log U}{\sqrt p\log p},
\qquad
\tau_r:=(r!\eta_p)^{1/r}.
\tag{23}
\]

For insertion budget

\[
m_p=(1+o(1))\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\tag{24}
\]

the Robin-source difference is

\[
\Delta\mathcal A_p
=-\frac{\delta_p}{Z_p\eta_p}
\int G_U\,d\nu+o(1),
\qquad
Z_p=2+o(1).
\tag{25}
\]

Combining (11) and (25),

\[
\boxed{
|\Delta\mathcal A_p|
\le\frac{\delta_p}{Z_p\eta_p}
\left[
(2+o(1))\mathfrak C_r(\nu)
+(4+o(1))\frac{(L/4)^r}{r!}
\right]+o(1).
}
\tag{26}
\]

Hence the coordinate-wise stability criterion is

\[
\boxed{
\frac{\delta_p}{\eta_p}
\left[
\mathfrak C_r(\nu)+\frac{(L/4)^r}{r!}
\right]\longrightarrow0.
}
\tag{27}
\]

At the sharp `RE-162` radius `L=4 tau_r`,

\[
\frac{(L/4)^r}{r!}=\eta_p.
\tag{28}
\]

Thus a budget-independent sufficient condition preserving the sharp exact-match scale under every `delta_p->0` is

\[
\boxed{
\mathfrak C_r(\nu)=O(\eta_p).
}
\tag{29}
\]

For a specified vanishing insertion budget, the weaker condition

\[
\delta_p\mathfrak C_r(\nu)=o(\eta_p)
\tag{30}
\]

suffices. If arithmetic information controls a signed combination rather than each mode separately, the exact object is the single scalar `mathcal L_r(nu)` in (8). Genuine cancellation among modes is therefore usable; a positive CA-specific theorem need not control every raw moment separately if it controls this kernel-weighted signed leakage.

## 3. Raw moments are ill-conditioned coordinates at growing degree

Let

\[
\mu_k:=\int z^k\,d\nu(z).
\tag{31}
\]

The first transformed discrepancies are

\[
\chi_1=\frac{2\mu_1}{L},
\tag{32}
\]

\[
\chi_2=\frac{8\mu_2}{L^2}-\frac{8\mu_1}{L},
\tag{33}
\]

and

\[
\chi_3=\frac{32\mu_3}{L^3}-\frac{48\mu_2}{L^2}+\frac{18\mu_1}{L}.
\tag{34}
\]

The transformation is triangular at all orders, so exact raw and exact Chebyshev matching are equivalent below the cutoff. Approximate matching is different: the change-of-basis coefficients grow rapidly with degree. Small separate monomial errors can therefore combine into an order-one Chebyshev mode even when every normalized raw discrepancy tends to zero.

The generalized-source construction from `RE-161` makes this visible. There the second packet is a small endpoint translation of the first. With

\[
h_p:=\frac{t_p}{L_p}\to0,
\tag{35}
\]

the two rescaled locations satisfy

\[
x_-=-1+o(h_p),
\qquad
x_+=-1+2h_p+o(h_p).
\tag{36}
\]

Fix `c>0` with `cos(2c) != 1` and set

\[
j_p:=\left\lfloor\frac{c}{\sqrt{h_p}}\right\rfloor.
\tag{37}
\]

Since

\[
\arccos(-1+2h)=\pi-2\sqrt h+O(h^{3/2}),
\tag{38}
\]

one obtains

\[
T_{j_p}(x_-)=(-1)^{j_p}+o(1),
\qquad
T_{j_p}(x_+)=(-1)^{j_p}\cos(2c)+o(1).
\tag{39}
\]

Therefore

\[
\boxed{
|\chi_{j_p}|\longrightarrow|1-\cos(2c)|>0.
}
\tag{40}
\]

At the same time `RE-161` gives

\[
\sup_{k\ge1}\frac{|\mu_k|}{L_p^k}\longrightarrow0.
\tag{41}
\]

So the discrepancy in `RE-161` did not disappear; it migrated to a Chebyshev degree `j_p` of order `h_p^{-1/2}` near the endpoint. This supplies a concrete spectral mechanism for the noncoercivity of qualitative raw-moment matching.

## 4. Consequences for the Robin frontier

`RE-161` remains correct: its raw-moment quantity `sum_{k<r}|mu_k|/k!` is the natural robust cost produced by endpoint Taylor expansion. `RE-163` identifies the sharper coordinate system required after `RE-162`: the endpoint basis does not encode the `4^{-r}` minimax gain, while the Chebyshev spectrum does.

`RE-162` is recovered exactly when the lower Chebyshev modes vanish. Conversely, (40) explains why the all-moment relative closeness in `RE-161` does not contradict the sharp capacity: the hidden discrepancy sits at a growing bounded-polynomial mode that the normalized monomial coordinates do not control uniformly.

For the ordinary-prime/CA problem, a useful positive input can therefore take one of three more precise forms: control the weighted Chebyshev leakage `mathfrak C_r`; force cancellation in the signed kernel-weighted leakage `mathcal L_r`; or impose a selector constraint preventing the endpoint spectral migration (40). The accepted selector-height coupling clue remains open because no such CA-specific identity is proved here.

## 5. Prior-art boundary and scope

Chebyshev expansions of exponentials into modified-Bessel coefficients are classical, and noisy Chebyshev-moment recovery is an established general subject. Musco--Musco--Rosenblatt--Singh (COLT 2025), for example, study distribution recovery from noisy Chebyshev moments using decay of Chebyshev coefficients for generic test functions. The moment-space and Chebyshev-approximation literature already bounded in `RE-162` is also relevant context.

Those works are not load-bearing here. Equations (12)--(22) derive the required coefficient law and tail directly from absolutely convergent series, and the endpoint hidden-mode calculation (35)--(40) is elementary. The targeted audit did not locate the Robin terminal kernel (1), the source normalization (25), the sharp leakage criterion (27)--(30), or the spectral explanation (40) of the `RE-161` generalized-source obstruction. No new external theorem is required in `SOURCES.md`.

As with `RE-157`--`RE-162`, this is a matched generalized-source information result. It does not rearrange the ordinary primes, construct a Robin counterexample, or establish the missing CA-specific coupling. Its contribution is to identify the **sharp approximate coordinate system** for terminal placement: exact lower moments remove low Chebyshev modes, approximate lower moments pay through those modes, and the unresolved tail is the same `4^{-r}` capacity pinned by `RE-162`.