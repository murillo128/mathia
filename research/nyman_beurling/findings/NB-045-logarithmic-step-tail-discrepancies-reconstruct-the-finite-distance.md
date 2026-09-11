# NB-045 — logarithmic step-tail discrepancies reconstruct the finite Nyman distance

**Status:** `EXACT-DERIVED + MULTISCALE-TAIL-SELECTOR-DECOMPOSITION + BEST-RESIDUAL-DISTANCE-IDENTITY + BURNOL-SCALE-DIRECTIONAL-OCCUPATION + TARGET-CONDITIONED-SIGNAL + ORACLE-BOUNDARY-REFINEMENT`. The bounded step-tail selectors of `NB-035` do more than control one weighted-tail coordinate at a chosen cutoff. Across all cutoffs they form an exact logarithmically weighted decomposition of the finite best-approximation distance. If
\[
p_N=P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n,
\qquad
r_N=e-p_N,
\qquad
d_N=\|r_N\|,
\tag{1}
\]
and
\[
D_{L,N}
:=m(L)-\sum_{n=L+1}^{N}\frac{a_{N,n}}n
=\langle r_N,\Psi_L\rangle,
\qquad 1\le L<N,
\tag{2}
\]
then, with
\[
\delta_L:=\log\frac{L+1}{L},
\qquad
\Theta(N):=1-\sum_{n\le N}\frac{\mu(n)}n\log\frac Nn,
\tag{3}
\]
one has the finite exact identity
\[
\boxed{
\sum_{L=1}^{N-1}\delta_LD_{L,N}
=d_N^2-\Theta(N).
}
\tag{4}
\]

Thus the source-selected reciprocal-Möbius tail discrepancies are not merely individually bounded by the residual. Their full logarithmic aggregate is the residual norm squared itself, up to the explicit source-only mollified Möbius defect `Theta(N)`.

The identity has an unconditional quantitative consequence. Let Burnol's critical-line constant, in the normalization already used in `NB-023`, be
\[
\mathfrak B_\zeta
:=\sum_{\Re\rho=1/2}\frac{m(\rho)^2}{|\rho|^2}>0,
\tag{5}
\]
so that
\[
\liminf_{N\to\infty}d_N^2\log N\ge\mathfrak B_\zeta.
\tag{6}
\]
The classical de la Vallée Poussin zero-free-region estimate for the Möbius summatory function implies
\[
\Theta(N)=o\!\left(\frac1{\log N}\right).
\tag{7}
\]
Since `sum_{L<N} delta_L=log N`, (4) therefore gives the one-sided directional floor
\[
\boxed{
\liminf_{N\to\infty}
(\log N)^2
\max_{1\le L<N}D_{L,N}
\ge\mathfrak B_\zeta.
}
\tag{8}
\]
In particular, at every sufficiently large section there is at least one cutoff at which the actual optimal reciprocal tail undershoots its Möbius baseline by order at least `1/log^2 N`. No RH assumption enters (8).

There is also a quantitative occupation statement. `NB-035` gives the uniform selector norm
\[
|D_{L,N}|\le C_*d_N,
\qquad
C_*:=\sqrt{4+20\zeta(2)}<7.
\tag{9}
\]
Put
\[
A_N:=\frac{d_N^2-\Theta(N)}{\log N}
\tag{10}
\]
and, for all sufficiently large `N` when `A_N>0`, define
\[
\mathcal G_N
:=\left\{
1\le L<N:
D_{L,N}\ge\frac{A_N}{2}
\right\}.
\tag{11}
\]
Then
\[
\boxed{
\sum_{L\in\mathcal G_N}\delta_L
\ge
\frac{d_N^2-\Theta(N)}{2C_*d_N}.
}
\tag{12}
\]
Consequently
\[
\boxed{
\liminf_{N\to\infty}
\sqrt{\log N}
\sum_{L\in\mathcal G_N}\delta_L
\ge
\frac{\sqrt{\mathfrak B_\zeta}}{2C_*}.
}
\tag{13}
\]
At the same time,
\[
\liminf_{N\to\infty}(\log N)^2\frac{A_N}{2}
\ge\frac{\mathfrak B_\zeta}{2}.
\tag{14}
\]
So the Burnol-scale directional signal cannot be confined to a family whose total logarithmic cutoff weight is `o(1/sqrt(log N))` while all other step-tail discrepancies stay below half of the logarithmic mean.

## 1. Exact logarithmic decomposition

`NB-035` constructs `Psi_L` with the exact pairings
\[
\langle e,\Psi_L\rangle=m(L),
\qquad
\langle g_n,\Psi_L\rangle
=\begin{cases}
0,&n\le L,\\
1/n,&n>L.
\end{cases}
\tag{15}
\]
Therefore (2) is exact for the canonical best residual.

Now sum with the positive logarithmic increments `delta_L`. The Möbius side telescopes exactly as in `NB-041`:
\[
\begin{aligned}
\sum_{L=1}^{N-1}\delta_Lm(L)
&=\sum_{n<N}\frac{\mu(n)}n
\sum_{L=n}^{N-1}\delta_L\\
&=\sum_{n<N}\frac{\mu(n)}n\log\frac Nn\\
&=1-\Theta(N).
\end{aligned}
\tag{16}
\]
For the optimal coefficient tail,
\[
\begin{aligned}
\sum_{L=1}^{N-1}\delta_L
\sum_{n=L+1}^{N}\frac{a_{N,n}}n
&=\sum_{n=2}^{N}\frac{a_{N,n}}n
\sum_{L=1}^{n-1}\delta_L\\
&=\sum_{n=2}^{N}\frac{a_{N,n}\log n}{n}\\
&=\langle e,p_N\rangle.
\end{aligned}
\tag{17}
\]
Because `p_N=P_{V_N}e`, orthogonality of `r_N` and `p_N` gives
\[
\langle e,p_N\rangle=\|p_N\|^2=1-d_N^2.
\tag{18}
\]
Subtracting (17) from (16) proves (4).

The same identity is visible as a discrete flow through the logarithmic duals of `NB-041`. Extend its family by `Omega_1:=e`. Since
\[
\Omega_{M+1}=\Omega_M-\delta_M\Psi_M,
\tag{19}
\]
one has
\[
\langle r_N,\Omega_M\rangle
-\langle r_N,\Omega_{M+1}\rangle
=\delta_MD_{M,N}.
\tag{20}
\]
The endpoints are
\[
\langle r_N,\Omega_1\rangle=d_N^2,
\qquad
\langle r_N,\Omega_N\rangle=\Theta(N),
\tag{21}
\]
because the `NB-041` logarithmic tail coordinate vanishes at `M=N`. Summing (20) is exactly (4). Thus the step-tail discrepancies are the increments by which the target correlation of the explicit dual path moves from the full finite distance to the source-only Möbius endpoint.

There is an equivalent weighted-skeleton form. With the `NB-035` endpoint coordinate
\[
\tau_{M,N}=M\sum_{n=M}^N\frac{a_{N,n}}n,
\tag{22}
\]
equation (2) reads
\[
\boxed{
D_{L,N}=m(L)-\frac{\tau_{L+1,N}}{L+1}.
}
\tag{23}
\]
Hence the family of weighted-skeleton endpoint errors across all cutoffs reconstructs `d_N^2` exactly after logarithmic averaging.

## 2. Burnol forces a positive discrepancy at `1/log^2 N` scale

The only asymptotic source term in (4) is `Theta(N)`. A classical zero-free-region consequence of the prime number theorem gives, for some `c>0`,
\[
\mathcal M(x):=\sum_{n\le x}\mu(n)
\ll x\exp(-c\sqrt{\log x}).
\tag{24}
\]
Partial summation and the limit `sum mu(n)/n=0` then give, after reducing `c` if necessary,
\[
m(x)\ll\exp(-c\sqrt{\log x}),
\qquad
\Theta(x)=\int_x^\infty m(u)\frac{du}{u}
\ll\exp(-c\sqrt{\log x}).
\tag{25}
\]
Polynomial factors in `sqrt(log x)` from either tail integral are absorbed by decreasing `c`. In particular,
\[
\boxed{\log x\,\Theta(x)\to0.}
\tag{26}
\]
This is much weaker than the best known quantitative PNT remainder and is used only to separate the source endpoint from the Burnol scale.

Normalize the positive weights by
\[
\nu_N(L):=\frac{\delta_L}{\log N},
\qquad
\sum_{L=1}^{N-1}\nu_N(L)=1.
\tag{27}
\]
Equation (4) becomes
\[
\boxed{
\mathbb E_{\nu_N}D_{L,N}
=A_N
=\frac{d_N^2-\Theta(N)}{\log N}.
}
\tag{28}
\]
By (6) and (26),
\[
\liminf_{N\to\infty}(\log N)^2 A_N
\ge\mathfrak B_\zeta.
\tag{29}
\]
The right side is positive, so `A_N>0` eventually. Since the maximum of finitely many real numbers is at least their positive weighted mean, (8) follows immediately. The sign is part of the conclusion: the guaranteed witness is a positive `D_{L,N}`, not merely a large absolute discrepancy.

## 3. Uniform selector bounds force logarithmic occupation

Let
\[
\alpha_N:=\nu_N(\mathcal G_N).
\tag{30}
\]
On `\mathcal G_N`, equation (9) gives `D_{L,N}<=C_*d_N`; on its complement, the definition (11) gives `D_{L,N}<A_N/2`. Therefore
\[
A_N
=\mathbb E_{\nu_N}D_{L,N}
\le
\alpha_NC_*d_N+(1-\alpha_N)\frac{A_N}{2}.
\tag{31}
\]
Rearranging,
\[
\alpha_N
\ge
\frac{A_N}{2(C_*d_N-A_N/2)}
\ge
\frac{A_N}{2C_*d_N}.
\tag{32}
\]
Multiplying by `log N` proves (12).

Burnol and (26) also imply
\[
\frac{\Theta(N)}{d_N^2}\to0,
\tag{33}
\]
because `d_N^2 log N` has a positive liminf. Hence the right side of (12) is
\[
\frac{d_N}{2C_*}(1+o(1)).
\tag{34}
\]
Finally (6) gives
\[
\liminf_{N\to\infty}d_N\sqrt{\log N}
\ge\sqrt{\mathfrak B_\zeta},
\tag{35}
\]
which proves (13). Equation (14) is just (29) divided by two.

The occupation statement is deliberately in logarithmic cutoff measure. It does not imply a positive ordinary density of indices, and it does not localize the witness to a prescribed range of `L`.

## 4. Adversarial checks and method boundary

Optimality is load-bearing. For an arbitrary finite approximant
\[
v=\sum_{n=2}^Na_ng_n,
\qquad r=e-v,
\tag{36}
\]
the same finite summation gives only
\[
\sum_{L=1}^{N-1}\delta_L
\left(m(L)-\sum_{n=L+1}^N\frac{a_n}{n}\right)
=\langle e,r\rangle-\Theta(N).
\tag{37}
\]
The conversion of the target pairing `\langle e,r_N\rangle` into the squared residual norm is exactly the normal equation for the best projection. Thus (4) is target-selected structure, not a universal coefficient identity that would hold with `||r||^2` for arbitrary controls.

The result is also not a cheap distance formula. Every `D_{L,N}` contains the optimal coefficient tail. Indeed (4) shows that knowing their complete logarithmic aggregate has already recovered `d_N^2` up to the explicit source term `Theta(N)`. A proposed oracle that obtains all these discrepancies to sufficient aggregate accuracy has therefore not bypassed the target problem merely by changing coordinates.

Conversely, (8) does not say where the useful cutoff lies, and (12) supplies only logarithmic measure, not a deterministic predeclared index. The surviving possibility is precisely more selective: obtain one scale, a sparse family, a one-sided envelope, or a partial aggregate from arithmetic data **without** first recovering the full optimal coefficient vector. Such a directional certificate could still be strictly cheaper than ambient control of `||Omega_M||`, whose polynomial decay is priced exactly by the zeta zero frontier in `NB-044`.

The quantitative PNT input in (24)--(26) is unconditional. It is used only for `Theta(N)=o(1/log N)`. Burnol supplies only a lower bound for `d_N`; neither input proves `d_N->0`, supplies an upper approximation rate, or improves any zeta zero-free region.

## 5. Prior art and research consequence

The ingredients are individually classical or already canonical in this line. The best-projection identity `\langle e,r_N\rangle=d_N^2` is elementary Hilbert-space geometry; the Möbius logarithmic smoothing and quantitative PNT remainder are classical; Burnol supplies (6); and `NB-035`/`NB-041` supply the exact bounded selectors and logarithmic dual path. No novelty is claimed for any ingredient in isolation.

A targeted literature audit covered Báez-Duarte's arithmetical Nyman--Beurling criteria, Vasyunin's step-function/biorthogonal work, Burnol's finite-distance lower bound, work on optimal Nyman coefficients, and modern Möbius/Nyman estimates. The located literature contains Möbius-based approximants, distance lower bounds, dual/step-function systems, and coefficient studies, but no located source states the finite best-residual decomposition (4) together with the one-sided Burnol-scale consequences (8) and (12). Search absence is not a priority claim; the durable line-local delta is the exact coupling of the already-persisted selector family to the **actual target-selected finite distance**.

For the live weighted-skeleton oracle question, this changes the directional picture in two complementary ways. First, the actual residual is not starved of bounded source-direction signal: its `Psi_L` correlations have a positive logarithmic mean forced at Burnol scale, and a controlled amount of logarithmic cutoff weight lies above half that mean. Second, the complete family is too informative to count as a cheap oracle, because its natural aggregate reconstructs `d_N^2` exactly. The productive remaining target is therefore a source-predictable **partial** directional certificate: identify or control enough of the positive `D_{L,N}` mass without implicitly summing the whole distance identity.