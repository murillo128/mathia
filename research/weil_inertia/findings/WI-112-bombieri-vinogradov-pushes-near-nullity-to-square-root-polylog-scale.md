# WI-112 — Bombieri--Vinogradov pushes full-packed near-nullity to square-root scale up to polylogarithms

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion. It materially strengthens WI-111's obstruction to low-codimension linear rescue of the exact full-packing Ramanujan interface: the same quotient-character construction can be driven essentially to the Bombieri--Vinogradov endpoint. For every fixed `B>5`, there are simultaneous positive-defect full-packed prime interactions with an explicit near-null sector of dimension

\[
\ell-1\asymp \frac{\sqrt p}{(\log p)^B},
\]

and relative singular scale

\[
O\!\left(p^{-1/4}(\log p)^{-(B-1)/2}\right).
\]

Consequently, for every fixed `C>5`, arbitrary linear pre/post-processing cannot keep both a fixed relative singular gap and fixed normalized transmission merely by deleting

\[
O\!\left(\frac{\sqrt p}{(\log p)^C}\right)
\]

source directions. WI-111 only excluded every fixed power `O(p^beta)` with `beta<1/2`; the present argument reaches the square-root scale up to a classical polylogarithmic loss.

## 1. Near-endpoint Bombieri--Vinogradov input

Fix `B>5`. Let `X` tend to infinity and set

\[
Q_0=\frac{\sqrt X}{4(\log X)^B}.
\tag{1}
\]

Use the classical maximal Bombieri--Vinogradov estimate in the form

\[
\sum_{M\le Q} E^*(x,M)
\ll x^{1/2}Q(\log x)^5,
\tag{2}
\]

valid in particular throughout

\[
x^{1/2}(\log x)^{-A}\le Q\le x^{1/2}
\tag{3}
\]

for fixed sufficiently large `A`, where

\[
E^*(x,M)=
\max_{y\le x}\max_{(a,M)=1}
\left|\psi(y;M,a)-\frac{y}{\varphi(M)}\right|.
\tag{4}
\]

Apply (2) at `x=2X` and `Q=2Q_0`. For any fixed `A>B`, (3) holds for all sufficiently large `X`, and therefore

\[
\sum_{M\le2Q_0}E^*(2X,M)
\ll \frac{X}{(\log X)^{B-5}}.
\tag{5}
\]

Restrict to

\[
\mathcal M=
\{M:Q_0\le M\le2Q_0,\ M\equiv2\pmod4\}.
\tag{6}
\]

This family has `asymp Q_0` members. Fix a sufficiently small absolute `eta>0` and call `M in mathcal M` bad when

\[
E^*(2X,M)>\eta\frac{X}{Q_0}.
\tag{7}
\]

By (5),

\[
\#\{M\in\mathcal M:M\text{ bad}\}
\ll
\frac{Q_0}{(\log X)^{B-5}}
=o(Q_0).
\tag{8}
\]

Thus a good `M` exists for every sufficiently large `X`. Write

\[
M=2\ell.
\tag{9}
\]

Since `M equiv 2 mod 4`, `ell` is odd, and

\[
\boxed{
\ell\asymp Q_0
\asymp\frac{\sqrt X}{(\log X)^B}.
}
\tag{10}
\]

The logarithmic restriction `B>5` is exactly what makes the bad-modulus proportion in (8) vanish using the classical `log^5` formulation. No Elliott--Halberstam-type input is used.

## 2. The good modulus supplies one source and two nearby targets

Take fixed separated intervals

\[
I_s=[X,1.05X],
\qquad
I_t=[1.10X,1.15X].
\tag{11}
\]

Use the source residue

\[
a_s=1\pmod{2\ell}
\tag{12}
\]

and the target residue

\[
a_t=\ell+2\pmod{2\ell}.
\tag{13}
\]

Because `ell` is odd,

\[
\gcd(\ell+2,2\ell)=1.
\tag{14}
\]

For either reduced residue, subtracting the two endpoint estimates supplied by (7) gives, for an interval of length `0.05X`,

\[
\psi(bX;M,a)-\psi(aX;M,a)
\ge
\frac{0.05X}{\varphi(M)}-2\eta\frac{X}{Q_0}.
\tag{15}
\]

Since `M<=2Q_0`, the main term is at least `0.025 X/Q_0`. Choosing for example `eta<0.01` leaves

\[
\psi(bX;M,a)-\psi(aX;M,a)
\gg\frac{X}{Q_0}.
\tag{16}
\]

Prime powers with exponent at least two contribute only `O(X^{1/2}\log X)`, whereas

\[
\frac{X}{Q_0}\asymp X^{1/2}(\log X)^B.
\tag{17}
\]

Hence actual primes still contribute positive mass for large `X`. In particular there is a source prime

\[
p\in I_s,
\qquad
p\equiv1\pmod{2\ell},
\tag{18}
\]

and the target interval contains

\[
J\gg\frac{X}{Q_0\log X}
\tag{19}
\]

primes satisfying

\[
q\equiv\ell+2\pmod{2\ell}.
\tag{20}
\]

Choose two consecutive primes `q_1<q_2` in this target set. Pigeonholing their gaps inside the fixed-length interval gives

\[
\boxed{
\Delta:=q_2-q_1
\ll Q_0\log X
\asymp\frac{\sqrt X}{(\log X)^{B-1}}.
}
\tag{21}
\]

The interval separation gives `p<q_i`, while `q_i<=1.15X<4p/3` because `p>=X`. Also `p asymp X`, so (10) and (21) may be rewritten with `p` in place of `X`.

## 3. WI-111's exact quotient-character geometry applies unchanged

Set

\[
d_i=q_i-p,
\qquad
h_i=d_i/2,
\qquad
t_i=2p-q_i.
\tag{22}
\]

Equations (18) and (20) imply

\[
d_i\equiv\ell+1\pmod{2\ell},
\quad
h_i\equiv\frac{\ell+1}{2}\pmod\ell,
\quad
\ell\mid t_i.
\tag{23}
\]

The common-center construction of WI-111 therefore produces one observation length `N` for which both `(p,q_i,N)` are genuinely positive-defect exact full-packed interactions. Writing

\[
G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\qquad
K_i=\ker G_i^*,
\tag{24}
\]

each `K_i` contains an explicit `(ell-1)`-dimensional quotient-character subspace `W_i`. For suitable orthonormal character bases `X_i`, WI-111's finite geometric-sum computation gives the exact cross Gram

\[
\boxed{
X_1^*X_2=
\sqrt{\frac{t_2}{t_1}}I_{\ell-1}.
}
\tag{25}
\]

Thus every unit vector in either `W_i` lies close to the other left kernel:

\[
\operatorname{dist}(x,K_j)^2
\le
\frac{\Delta}{t_1}
\le
\frac{3\Delta}{2p}.
\tag{26}
\]

Nothing in (22)--(26) is a new arithmetic or spectral assumption. It is exactly the WI-104/WI-111 full-packing normal form, with only the size of `ell` and the target gap changed by the near-endpoint choice of modulus.

## 4. The near-null sector reaches square-root dimension up to logs

Allow arbitrary target-local right processing

\[
C_i:E_i\to\mathbf C^{q_i-1},
\qquad
B=[\,G_1C_1\;G_2C_2\,].
\tag{27}
\]

As in WI-111, target-local processing preserves each original left kernel. Courant--Fischer on the entire `(ell-1)`-dimensional `W_i` therefore yields, with singular values padded to the source dimension `p-1`,

\[
\frac{\sigma_{p-\ell+1}(B)}{\sigma_1(B)}
\le
\sqrt{\frac{3\Delta}{2p}}.
\tag{28}
\]

Combining (21) with `p asymp X` gives

\[
\boxed{
\frac{\sigma_{p-\ell+1}(B)}{\sigma_1(B)}
\ll
p^{-1/4}(\log p)^{-(B-1)/2}
\longrightarrow0,
}
\tag{29}
\]

while

\[
\boxed{
\ell-1
\asymp
\frac{\sqrt p}{(\log p)^B}.
}
\tag{30}
\]

Thus the exact full-packed interface can have nearly square-root-many simultaneously weak source singular directions, not merely `p^theta` for a preassigned `theta<1/2`.

## 5. Low-codimension rescue is closed at square-root/polylog scale

For arbitrary further linear processing

\[
A=LBS,
\tag{31}
\]

retain WI-110/WI-111's normalized quantities

\[
r_k(A)=\frac{\sigma_k(A)}{\sigma_1(A)},
\qquad
\tau_B(L,S)=
\frac{\sigma_1(A)}{\|L\|_2\sigma_1(B)\|S\|_2}.
\tag{32}
\]

The singular-value ideal property gives at every retained index

\[
\boxed{
r_k(A)\tau_B(L,S)
\le
\frac{\sigma_k(B)}{\sigma_1(B)}.}
\tag{33}
\]

Suppose a rescue deletes `d(p)` source dimensions, so `k=p-1-d(p)`. If

\[
d(p)=o\!\left(\frac{\sqrt p}{(\log p)^B}\right),
\tag{34}
\]

then eventually `d(p)<=ell-2`, hence `k>=p-ell+1`, and (29)--(33) imply

\[
\boxed{
r_k(A)\tau_B(L,S)
\ll
p^{-1/4}(\log p)^{-(B-1)/2}
\to0.}
\tag{35}
\]

A convenient fixed-exponent corollary is obtained by taking any `C>5` and choosing `B` with

\[
5<B<C.
\tag{36}
\]

Then

\[
d(p)=O\!\left(\frac{\sqrt p}{(\log p)^C}\right)
=o\!\left(\frac{\sqrt p}{(\log p)^B}\right),
\tag{37}
\]

so (35) applies. Therefore no arbitrary linear rescue at that deletion scale can retain both `r_k(A)>=c>0` and `tau_B(L,S)>=c'>0` uniformly over the full-packed prime family.

This is a strict strengthening of WI-111: every `p^beta`, `beta<1/2`, is much smaller than the sector in (30), but (37) also excludes deletion scales with polynomial exponent exactly `1/2` and any fixed logarithmic saving stronger than `log^5`.

## 6. Boundary and no-overclaim

The argument does **not** close deletion of order `sqrt(p)` itself. With the classical maximal estimate (2), the elementary good-modulus selection above needs `B>5`; at `B=0` there is no vanishing bad-modulus proportion from this calculation. Thus the present conclusion is square-root scale **up to polylogarithms**, not a genuine endpoint theorem.

There is known prior art improving logarithmic factors in Bombieri--Vinogradov. In particular, Alisa Sedunova, **A logarithmic improvement in the Bombieri--Vinogradov theorem**, *J. Théorie des Nombres de Bordeaux* 31 (2019), 635--651, DOI `10.5802/jtnb.1098`, improves the strongest logarithmic factor in a refined version of the theorem. That paper is relevant to whether the exponent `5` in the present bookkeeping can be lowered, but no such translation is used here: (1)--(37) rely only on the classical `log^5` maximal form.

Likewise, nothing here improves the zeta simple-critical proportion, identifies the uncertified complement, or proves that these exact full-packed windows occur with positive analytic density. The conclusion is a uniform structural obstruction inside the auxiliary Ramanujan/full-packing operator pathway. Positive slack away from exact packing, extra zeta-specific arithmetic information, nonlinear processing, or a normalization that changes the operator before this compression remain outside the claim.

## 7. Prior-art and novelty audit

The load-bearing prime-distribution theorem is classical Bombieri--Vinogradov. Primary sources are E. Bombieri, **On the large sieve**, *Mathematika* 12 (1965), 201--225, DOI `10.1112/S0025579300005313`, and A. I. Vinogradov, **The density hypothesis for Dirichlet L-series**, *Izv. Akad. Nauk SSSR Ser. Mat.* 29 (1965), 903--934, with corrigendum 30 (1966), 719--720. The exact `x^(1/2) Q (log x)^5` maximal formulation used above is a standard classical form of their mean-distribution theorem.

WI-111 already combined a Bombieri--Vinogradov-selected modulus `M asymp X^theta`, `theta<1/2`, with the WI-104 quotient-character kernel normal form, exact isoclinic subspaces, Courant--Fischer, and WI-110's conditioning-times-transmission product law. The only new deduction here is to choose the modulus **inside the logarithmically thinned endpoint window** `M asymp sqrt(X)/(log X)^B`, quantify the bad-modulus count directly from the classical maximal theorem, and propagate that improved arithmetic scale through the already exact geometric and singular-value steps.

Targeted searches around Bombieri--Vinogradov-selected Ramanujan kernels, isoclinic Ramanujan subspaces, principal-angle multiplicity, finite-window restricted invertibility, and square-root/polylogarithmic source deletion located no matching theorem. That negative search is not a priority claim. The durable result is the exact strengthening of WI-111's deletion barrier from every fixed sub-square-root power to square-root scale with a fixed logarithmic saving.

## 8. Program consequence

WI-111 left open the possibility that a restricted inverse deleting a genuinely square-root-scale but submacroscopic sector could avoid the known full-packing obstruction. The present finding narrows that escape sharply: for every fixed `C>5`, deleting only

\[
O\!\left(\frac{\sqrt p}{(\log p)^C}\right)
\]

directions is still insufficient to retain fixed conditioning and fixed normalized transmission.

The next honest endpoint question is now arithmetic rather than matrix-theoretic: how far can the logarithmic thinning in (1) be reduced while still selecting one congruence modulus that simultaneously supplies the source progression and enough nearby targets? A sharper Bombieri--Vinogradov logarithmic form may improve the polylog exponent; removing the logarithmic loss altogether would require a genuinely stronger endpoint selection argument. The quotient-character geometry and the conditioning/transmission law themselves no longer create the gap between WI-111 and the square-root scale.