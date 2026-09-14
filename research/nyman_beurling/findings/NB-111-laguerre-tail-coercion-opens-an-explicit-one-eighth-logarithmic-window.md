# NB-111 — Laguerre tail coercion opens an explicit one-eighth logarithmic window

**Status:** `DERIVED + FULL-EARLY-CELL-BACKFILL + GROWING-CONFLUENT-RANK + TARGET-AWARE-STATE-SUBSPACE + LAGUERRE-COERCION + REPRESENTATION-INVARIANT + SOURCE-COMPATIBLE-WHEN-MULTIPLICITY-PRESENT + NEGATIVE/METHOD-BOUNDARY`.

`NB-110` proves that a one-zero confluent/Jordan packet remains asymptotically target-poor for `d <= c log G`, but the constant `c>0` is left implicit because two fixed-base exponential losses are paid: a Remez loss on a sparse mesoscopic annulus and a Chebyshev extrapolation loss from that annulus to the target endpoint. Both losses are avoidable if the radial weight already present in the exact cell norm is retained.

The resulting polynomial geometry is Laguerre. It yields an explicit logarithmic window and also identifies where the present deterministic phase-resolution argument stops.

Let

\[
\rho_j=\frac12+a_j+iG_j,
\qquad 0<a_j<\frac12,
\qquad G_j\to\infty,
\]

put

\[
m_j=\lceil G_j\rceil,
\qquad R_j=m_jq_j,
\qquad L_j:=2a_j\log q_j\longrightarrow L\in(0,\infty),
\tag{1}
\]

and fix `r>=1`. For the derivative-state space and target

\[
S_j^{(d_j)}=\operatorname{span}\{w_{0,j},\ldots,w_{d_j-1,j}\},
\qquad
e_j=\sum_{n=r}^{R_j-1}\phi_n,
\]

write

\[
\delta_j^2
:=
\frac{\|P_{S_j^{(d_j)}}e_j\|_2^2}{\|e_j\|_2^2}.
\tag{2}
\]

Define the intrinsic early-cell depth

\[
T_j:=2(1-a_j)\log\frac{m_j}{r}.
\tag{3}
\]

Then

\[
\boxed{
\limsup_{j\to\infty}\frac{d_j}{T_j}<\frac18
\quad\Longrightarrow\quad
\delta_j\longrightarrow0.
}
\tag{4}
\]

Since `a_j<1/2` and `m_j~G_j`, this has the uniform consequence

\[
\boxed{
 d_j\le\left(\frac18-\varepsilon\right)\log G_j
 \quad\Longrightarrow\quad
 \delta_j\longrightarrow0
}
\tag{5}
\]

for every fixed `epsilon>0`. If `a_j -> a_*`, the scale-sensitive version is

\[
 d_j\le
 \left(\frac{1-a_*}{4}-\varepsilon\right)\log G_j.
\tag{6}
\]

A genuine zeta zero of multiplicity at least `d_j` supplies these derivative states exactly as in `NB-108`--`NB-110`; `(4)` is a statement about how much target access that entire one-zero packet can have after **all** earlier cells have been restored.

## 1. The exact radial weight is Laguerre, not an unweighted annulus

For

\[
p(u)=\sum_{k=0}^{d-1}c_ku^k,
\qquad
w[p]=\sum_{k=0}^{d-1}c_kw_k,
\]

`NB-110` writes the exact cell functional as

\[
I_n[p]
=
\int_0^{h_n}
 p(u_n+2av)e^{-\rho v}\,dv,
\qquad
h_n=\log(1+1/n),
\qquad
u_n=2a\log(n/m).
\tag{7}
\]

Introduce instead

\[
z=2(1-a)\log\frac mn
=-\frac{1-a}{a}u,
\qquad
Q(z):=p\!\left(-\frac{a}{1-a}z\right).
\tag{8}
\]

This is an invertible affine rescaling of the degree-`<d` polynomial space, so it changes neither its dimension nor the principal-angle quantity `(2)`. The weight in the frozen early-cell norm becomes exactly

\[
\left(\frac nm\right)^{2-2a}=e^{-z}.
\tag{9}
\]

The fixed target endpoint `u(r)=-A`, with `A=2a log(m/r)`, is sent to

\[
z=T=\frac{1-a}{a}A
=2(1-a)\log\frac mr.
\tag{10}
\]

Thus the natural continuous norm is not a flat polynomial norm followed by a remote Chebyshev extrapolation. It is the Laguerre norm

\[
\|Q\|_{\mathrm{Lag}}^2
:=
\int_0^\infty e^{-z}|Q(z)|^2\,dz,
\tag{11}
\]

and the target sits at the moving point `z=T`.

This representation passes the information audit: `p <-> Q` is bijective, no state is discarded, the target endpoint is carried exactly to `T`, and expanding in Laguerre polynomials below is only an orthonormal change of coordinates inside the same polynomial subspace.

## 2. One integration by parts reaches the square-root cell scale

The crude freezing error in `NB-110` is not sharp enough near `n~sqrt(G)`. Integrating `(7)` by parts once gives the exact identity

\[
I_n[p]
=
\frac{p(u_n)-e^{-\rho h_n}p(u_{n+1})}{\rho}
+
\frac{2a}{\rho}
\int_0^{h_n}p'(u_n+2av)e^{-\rho v}\,dv.
\tag{12}
\]

If

\[
J_n:=\frac{1-e^{-\rho h_n}}{\rho},
\]

then

\[
I_n[p]-p(u_n)J_n
=
-\frac{e^{-\rho h_n}}{\rho}
\bigl(p(u_{n+1})-p(u_n)\bigr)
+
\frac{2a}{\rho}
\int_0^{h_n}p'(u_n+2av)e^{-\rho v}\,dv.
\tag{13}
\]

Cauchy--Schwarz therefore yields

\[
|I_n[p]-p(u_n)J_n|^2
\ll
\frac{a h_n}{G^2}
\int_{u_n}^{u_{n+1}}|p'(u)|^2\,du.
\tag{14}
\]

This gains two powers of the cell length over the rough estimate used in `NB-110`.

Take

\[
N=\left\lceil m^{1/2}(\log m)^6\right\rceil,
\qquad
\eta=(\log m)^{-10},
\tag{15}
\]

and use the cells `N<=n<m`. Their phase variable

\[
x_n:=Gh_n
\]

has mesh

\[
|x_{n+1}-x_n|
\ll \frac{G}{N^2}
\ll(\log m)^{-12}=o(\eta).
\tag{16}
\]

Call a cell phase-good when

\[
\operatorname{dist}(x_n,2\pi\mathbb Z)\ge\eta.
\]

Then

\[
|J_n|\gg\frac{\eta}{G}
\tag{17}
\]

on every good cell. Because the phase mesh is now much smaller than the excluded phase width, the discrete cells resolve the continuous phase sweep. In the `z` coordinate, on every interval of bounded length the phase is monotone and a neighborhood of width `eta` around the multiples of `2pi` occupies `O(eta)` of the interval; `(16)` changes this by only `o(eta)`.

For a polynomial of degree `<d`, the elementary local Nikolskii estimate on a unit interval gives

\[
\sup_I |Q|^2
\ll d^2\int_I|Q|^2.
\tag{18}
\]

Since the weight `e^{-z}` varies only by a fixed factor on such an interval, `(18)` shows that deleting all phase-bad cells removes at most

\[
O(d^2\eta)=o(1)
\tag{19}
\]

of the weighted polynomial mass whenever `d=O(log G)`. Thus no fixed-base Remez loss is needed.

The radial interval resolved by `(15)` is

\[
0\le z\le X,
\qquad
X:=2(1-a)\log\frac mN
=rac T2+O_r(\log\log G).
\tag{20}
\]

The endpoint-sampling error is negligible because the `z` mesh is `O(1/N)`. The freezing error is negligible as well. Indeed, for the standard Laguerre basis `L_k`,

\[
L_k'(z)=-\sum_{j=0}^{k-1}L_j(z),
\]

so for every degree-`<d` polynomial

\[
\int_0^\infty e^{-z}|Q'(z)|^2\,dz
\le d^2\|Q\|_{\mathrm{Lag}}^2.
\tag{21}
\]

After summing `(14)` through the exact orthogonal-cell norm, the squared freezing error relative to the phase-good frozen scale is

\[
\ll
\frac{d^2}{\eta^2N^2}
=
G^{-1+o(1)}.
\tag{22}
\]

Hence, once the polynomial mass on `[0,X]` is known to control `(11)`, the actual state satisfies

\[
\boxed{
\|w[p]\|_2^2
\gg_r
a\,\eta^2\,\|Q\|_{\mathrm{Lag}}^2.
}
\tag{23}
\]

The factor `a` is genuine but harmless: the exact target pairing carries the same factor after squaring.

## 3. The Laguerre `4d` scale converts half-depth into the `1/8` threshold

The remaining step is to justify the premise used in `(23)`: a degree-`<d` polynomial cannot put a significant fraction of its Laguerre mass beyond `X` when `X>4d` by a fixed proportion.

This can be derived directly, so no asymptotic theorem is needed. The standard Laguerre polynomials satisfy

\[
\int_0^\infty e^{-z}L_j(z)L_k(z)\,dz=\delta_{jk}
\tag{24}
\]

and have generating function

\[
\sum_{k\ge0}L_k(x)\zeta^k
=
\frac1{1-\zeta}
\exp\!\left(-\frac{x\zeta}{1-\zeta}\right).
\tag{25}
\]

For `0<s<1`, Cauchy's coefficient estimate on `|zeta|=s` gives

\[
|L_k(x)|
\le
\frac{s^{-k}}{1-s}
\exp\!\left(\frac{xs}{1+s}\right).
\tag{26}
\]

Consequently

\[
\int_X^\infty e^{-x}|L_k(x)|^2\,dx
\ll_s
s^{-2k}
\exp\!\left(-\frac{1-s}{1+s}X\right).
\tag{27}
\]

If `d/X<=1/4-epsilon_0`, one can choose `s<1`, depending only on `epsilon_0`, so that

\[
\frac{1-s}{1+s}
+2\frac dX\log s>c_{\varepsilon_0}>0.
\tag{28}
\]

Expanding `Q=sum_{k<d}a_kL_k` and bounding the tail Gram operator by its trace yields

\[
\boxed{
\int_X^\infty e^{-x}|Q(x)|^2\,dx
\le
 e^{-c_{\varepsilon_0}X}
\|Q\|_{\mathrm{Lag}}^2
}
\tag{29}
\]

for all large `X`; polynomial factors in `d` are absorbed into the exponential. The constant `1/4` appears because, as `s->1`, the inequality in `(28)` becomes possible exactly below the classical Laguerre turning scale `X=4d`.

Now `(20)` gives `X=T/2+o(T)`. Hence

\[
\limsup\frac dT<\frac18
\]

implies `d/X<1/4` with a fixed margin, so `(29)` makes the observed early cells carry `1-o(1)` of the **entire** Laguerre polynomial norm. This proves `(23)`.

## 4. The full target jet is exponentially outside the Laguerre bulk

The exact target identity from `NB-109` is

\[
\langle e,w[p]\rangle
=
\sqrt{2a}\,m^\lambda
\sum_{\ell=0}^{d-1}
\frac{(2a)^\ell}{\rho^{\ell+1}}
\left[
 p^{(\ell)}(-A)r^{-\rho}
 -p^{(\ell)}(L)R^{-\rho}
\right].
\tag{30}
\]

At the left endpoint, `(8)` turns the jet into

\[
p^{(\ell)}(-A)
=
\left(-\frac{1-a}{a}\right)^\ell Q^{(\ell)}(T),
\tag{31}
\]

so the derivative coefficient in `(30)` becomes

\[
\left(\frac{2(1-a)}{\rho}\right)^\ell.
\tag{32}
\]

Differentiating the generating function `(25)` merely inserts the factor

\[
\left(-\frac{\zeta}{1-\zeta}\right)^\ell.
\]

Thus the same Cauchy-circle estimate used in `(26)` controls the whole endpoint jet: since `|rho|~G`, the sum over `ell` is geometric on every fixed circle `|zeta|=s<1`. Under `(4)` there is therefore `c>0` such that

\[
\boxed{
 e^{-T}
\left|
\sum_{\ell<d}
\left(\frac{2(1-a)}{\rho}\right)^\ell
Q^{(\ell)}(T)
\right|^2
\le
 e^{-cT}\|Q\|_{\mathrm{Lag}}^2.
}
\tag{33}
\]

The physical prefactor at the left endpoint satisfies

\[
\frac{m^{2a}}{|\rho|^2}r^{-1-2a}
\asymp_r e^{-T},
\tag{34}
\]

because `m~G` and

\[
e^{-T}=\left(\frac rm\right)^{2(1-a)}.
\]

Combining `(30)`--`(34)` gives

\[
|\langle e,w[p]\rangle|^2_{
\text{left endpoint}}
\ll_r
 a e^{-cT}\|Q\|_{\mathrm{Lag}}^2.
\tag{35}
\]

The terminal endpoint is smaller uniformly, including when `a->0`. Put

\[
U:=\frac{1-a}{a}L,
\]

so that `u=L` corresponds to `z=-U`. Applying `(25)` on the fixed circle `|zeta|=1/9` gives

\[
|L_k^{(\ell)}(-U)|
\ll
9^k8^{-\ell}e^{U/8}.
\tag{36}
\]

For `(4)`, `d<=T/8+o(T)<=\frac14\log G+o(\log G)`. The factor `R^{-1-2a}` in `(30)` contributes

\[
q^{-(1+2a)}
=
\exp\!\left(-\frac{(1+2a)L}{2a}\right),
\]

which dominates the `e^{U/4}` cost after squaring `(36)`, while the remaining `9^{2d}` is still dominated by the physical `G^{-3+o(1)}` terminal prefactor. Hence

\[
|\langle e,w[p]\rangle|^2_{
\text{terminal endpoint}}
=o\!\left(a\eta^2\|Q\|_{\mathrm{Lag}}^2\right).
\tag{37}
\]

Finally

\[
\|e\|_2^2
=\frac1r-\frac1R\longrightarrow\frac1r.
\tag{38}
\]

Taking the supremum of `(35)` and `(37)` over nonzero degree-`<d` polynomials and dividing by the coercive state bound `(23)` proves `(4)` and `(5)`.

## 5. Stress test: why `1/8` is a method boundary, not a claimed universal threshold

Two independent scales meet in `(4)`.

First, deterministic control of the phase-good cells by continuity requires the phase mesh

\[
\frac{G}{n^2}=o(1),
\]

so without additional arithmetic information the present argument can only push uniformly to

\[
n\ge G^{1/2+o(1)}.
\]

In the Laguerre coordinate this exposes at most half of the total target depth:

\[
X=\frac T2+o(T).
\]

Second, a degree-`d` Laguerre polynomial has exponentially negligible mass beyond `X` only on the safe side of the classical turning scale

\[
4d<X.
\]

Putting the two together gives `d<T/8`. At `d~X/4`, estimate `(29)` necessarily loses its exponential margin; this is not removable by whitening or by changing the polynomial basis. Conversely, pushing below the square-root cell scale would require new information about the sampled phases `G log(1+1/n)` or a coercive treatment of the exact twisted differences in `(12)`, not merely a sharper polynomial inequality.

Thus `(4)` should **not** be read as proving that rank `T/8` is the true target-access transition. It is the explicit boundary of the current deterministic phase-resolution plus Laguerre-tail architecture.

## Prior art and novelty boundary

The Laguerre orthogonality, generating function, and the `x~4n` turning geometry are classical; no novelty is claimed for them. Szego's classical Laguerre asymptotics and DLMF §18.15(iv) encode the same turning scale through the parameter `nu=4n+2alpha+2`. The proof above deliberately derives only the inequalities it needs directly from `(25)` rather than importing Plancherel--Rotach asymptotics.

A targeted search of Nyman--Beurling/Baez--Duarte literature did not locate this Laguerre-weight reduction of the one-zero confluent packet or the resulting `d<T/8` target-poorness criterion. The line-local contribution is the combination of: the exact Nyman early-cell weight `(9)`, the improved freezing identity `(12)`--`(14)`, square-root phase resolution `(15)`--`(20)`, and the Laguerre tail/endpoint comparison `(29)`--`(35)`. The classical orthogonal-polynomial ingredient is only the ambient geometry.

## Consequence for the research line

`NB-110` left open an unspecified logarithmic rank threshold. This finding makes a fixed part of that window explicit:

\[
\boxed{d<(1/8-o(1))\log G\quad\text{is uniformly target-poor}.}
\]

The next one-zero question is therefore no longer whether a better conditioning argument can merely make the constant in `NB-110` visible. To enlarge the window substantially using the same source, one must either control the oscillatory cell phases below `n~sqrt(G)` or exploit the exact twisted-difference structure of `(12)` without selecting phase-good cells. Separately, any source-specific multiplicity theorem placing all zeta-zero multiplicities below the explicit window would eliminate the one-zero multiplicity rescue altogether; no such theorem is assumed here.
