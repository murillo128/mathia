# FD-234 — Nearest-integer repair is a capacity-negligible switched-blind perturbation of block-Mertens inversion

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact divisor-response inversion / Mertens block increments / rounding stability / switched-blind affine class / one-sided capacity
- **Depends on:** FD-233, FD-225
- **Classification:** `EXACT-DERIVED + ROUNDING-REMOVAL + BLOCK-MERTENS-CONVOLUTION + SWITCHED-BLIND-EQUIVALENCE + ONE-SIDED-DENSITY-STABILITY`

## Claim

The nearest-integer target used in FD-225 is not part of the remaining positivity obstruction. It differs from the canonical real-valued Mertens repair by a coefficient profile that is simultaneously **uniformly switched-blind** and **negligible in dyadic capacity**. Consequently the FD-233 affine positive-lift problem is exactly unchanged if the rounded integer repair is replaced by an explicit divisor convolution of block Mertens increments.

Retain the divisor-response operator

\[
(\mathscr A c)(m)
=
\sum_{d\le m}c_d M\!\left(\left\lfloor\frac md\right\rfloor\right).
\tag{1}
\]

For a fixed integer `N>=1`, put `M(0)=0` and define the exact real target

\[
\widetilde y_N(m):=-\frac12 M(mN),
\qquad
\widetilde y_N(0)=0.
\tag{2}
\]

Let

\[
y_N(m)=\operatorname{nint}\!\left(-\frac12M(mN)\right),
\qquad y_N(0)=0,
\tag{3}
\]

be the FD-225 nearest-integer target, and let

\[
\mathscr A\widetilde c_N=\widetilde y_N,
\qquad
\mathscr A c_N=y_N
\tag{4}
\]

be their exact divisor inverses from FD-225. Then:

1. if

\[
U_N(d):=M(dN)-M((d-1)N)
=
\sum_{(d-1)N<a\le dN}\mu(a),
\tag{5}
\]

then the canonical real correction is exactly

\[
\boxed{
\widetilde c_N(n)
=-\frac12\sum_{d\mid n}U_N(d)
=-\frac12(\mathbf 1*U_N)(n),
}
\tag{6}
\]

and hence

\[
\boxed{
\mu*\widetilde c_N=-\frac12U_N.
}
\tag{7}
\]

2. the rounding difference

\[
r_N:=c_N-\widetilde c_N
\tag{8}
\]

satisfies

\[
\boxed{
|r_N(n)|\le\tau(n),
\qquad
\mathscr A r_N=e_N,
\qquad
|e_N(m)|\le\frac12,
}
\tag{9}
\]

where `e_N=y_N-\widetilde y_N`;

3. for the switched row orders of FD-233,

\[
r_j=q_j+1\in\{1,4\},
\qquad
\mathcal R_j(v)=(E-I)^{r_j}(\mathscr A v)(2^j),
\]

one has the uniform bound

\[
\boxed{|\mathcal R_j(r_N)|\le8}
\tag{10}
\]

for every `N` and `j`;

4. on every dyadic band `B_k=[2^k,2^{k+1})`, with

\[
C_k=\sum_{n\in B_k}n\asymp4^k,
\]

one has uniformly in `N`

\[
\boxed{
\frac{\sum_{n\in B_k}|r_N(n)|}{C_k}
=O\!\left(\frac{k}{2^k}\right).
}
\tag{11}
\]

In particular,

\[
\left|
\frac{\sum_{n\in B_k}c_N(n)^-}{C_k}
-
\frac{\sum_{n\in B_k}\widetilde c_N(n)^-}{C_k}
\right|
=O\!\left(\frac{k}{2^k}\right),
\tag{12}
\]

and, more strongly, `c_N` and `\widetilde c_N` lie in the same FD-233 affine class modulo signed switched-blind profiles. Therefore the existence or nonexistence of a switched-null adjustment making the concrete repair asymptotically negative-sparse is exactly the same for the rounded FD-225 correction and for the canonical block-Mertens convolution (6).

The remaining coefficient-level frontier can thus be stated without nearest-integer bookkeeping: study the one-sided dyadic capacity of

\[
-\frac12(\mathbf 1*U_N)(n),
\]

modulo legitimate switched-blind directions. Integer prime occupancy and finite reservoir capacity remain separate source-side questions after that coefficient-level problem.

## 1. Exact real inversion is a divisor sum of block Möbius increments

FD-225 gives the inverse formula

\[
\mathscr A c=y
\quad\Longleftrightarrow\quad
c(n)=\sum_{d\mid n}\bigl(y(d)-y(d-1)\bigr).
\tag{13}
\]

Applying (13) to (2) gives

\[
\begin{aligned}
\widetilde c_N(n)
&=
-\frac12
\sum_{d\mid n}
\bigl(M(dN)-M((d-1)N)\bigr)\\
&=
-\frac12\sum_{d\mid n}U_N(d),
\end{aligned}
\]

which is (6). Since the constant-one arithmetic function is the Dirichlet-convolution inverse of `mu`, convolving (6) with `mu` gives (7).

This identifies the exact arithmetic object hidden behind the FD-225 repair. The target `\widetilde y_N` cancels the physical Mertens baseline with no residual at all:

\[
M(mN)+2(\mathscr A\widetilde c_N)(m)=0
\qquad(m\ge1).
\tag{14}
\]

Thus the ideal coefficient correction is not defined implicitly by a triangular system. It is the divisor smoothing of the length-`N` Möbius block sums `U_N`.

For each fixed `N`, this profile lies within the linear-envelope framework used in FD-233. Indeed `|U_N(d)|<=N`, so

\[
|\widetilde c_N(n)|
\le\frac N2\tau(n)
\le\frac N2 n.
\tag{15}
\]

No cancellation estimate for `M` is needed for this structural statement.

## 2. Nearest-integer rounding produces an explicitly blind correction

Write

\[
e_N(m):=y_N(m)-\widetilde y_N(m).
\tag{16}
\]

Because `y_N(m)` is a nearest integer to `\widetilde y_N(m)`, one has

\[
|e_N(m)|\le\frac12,
\qquad e_N(0)=0.
\tag{17}
\]

By linearity of the exact inverse,

\[
r_N=c_N-\widetilde c_N=\mathscr A^{-1}e_N.
\]

Using (13) again,

\[
\boxed{
r_N(n)
=
\sum_{d\mid n}
\bigl(e_N(d)-e_N(d-1)\bigr).
}
\tag{18}
\]

Each ordinary difference in (18) has absolute value at most `1`, so

\[
|r_N(n)|\le\tau(n).
\]

Equation `\mathscr A r_N=e_N` is exact by construction. Therefore, for the bounded switched orders `r_j in {1,4}`,

\[
\mathcal R_j(r_N)
=(E-I)^{r_j}e_N(2^j).
\tag{19}
\]

The coefficient `l^1` norm of `(E-I)^r` is `2^r`. Together with (17),

\[
|\mathcal R_j(r_N)|
\le2^{r_j-1}
\le8,
\]

which proves (10). Thus rounding does not merely become small asymptotically: **its entire coefficient correction is a uniformly bounded switched-blind direction**.

The rounded physical residual from FD-225 is exactly

\[
M(mN)+2(\mathscr A c_N)(m)=2e_N(m),
\]

so the familiar `+-1` flattening error is precisely the image of this blind perturbation.

## 3. The rounding correction is negligible in one-sided dyadic capacity

The same correction is much smaller than the capacity scale relevant to FD-230--FD-233. From (9),

\[
\sum_{n\in B_k}|r_N(n)|
\le
\sum_{2^k\le n<2^{k+1}}\tau(n).
\tag{20}
\]

No analytic divisor estimate is needed. The elementary identity

\[
\sum_{n\le x}\tau(n)
=
\sum_{a\le x}\left\lfloor\frac xa\right\rfloor
\le
x\sum_{a\le x}\frac1a
\le
x(1+\log x)
\tag{21}
\]

gives

\[
\sum_{n\in B_k}|r_N(n)|=O(k2^k),
\tag{22}
\]

uniformly in `N`. Since `C_k\asymp4^k`, (11) follows.

The negative-part map is `1`-Lipschitz:

\[
|x^- -z^-|\le|x-z|.
\tag{23}
\]

Applying (23) coordinatewise to `c_N=\widetilde c_N+r_N` and using (11) proves (12). Hence nearest-integer rounding cannot create or remove a positive limiting negative-capacity density. In any regime with `k->infinity`, including a triangular family where `N` and the available depth vary together, the estimate remains valid because its constant is independent of `N`.

There is an even stronger affine statement. The profile `r_N` has a linear envelope because `tau(n)<=n`, and (10) makes it switched-subquadratic. Therefore `r_N` belongs to the FD-233 signed switched-blind class `N_sw`. Consequently

\[
\boxed{
c_N+\mathcal N_{\rm sw}
=
\widetilde c_N+\mathcal N_{\rm sw}.
}
\tag{24}
\]

So the one-sided optimization problem of FD-233 is not merely stable under rounding; it is literally the same affine problem.

## 4. The live frontier is now a canonical arithmetic convolution

FD-233 reduced coefficient-level physical liftability to the existence of a switched-blind adjustment `h` such that the corrected profile has vanishing late-band negative density. Equation (24) means the rounded vector introduced only to obtain integer reservoir counts can be removed from that question entirely.

The canonical representative is

\[
\boxed{
\widetilde c_N
=-\frac12\mathbf1*U_N,
\qquad
U_N(d)=\sum_{(d-1)N<a\le dN}\mu(a).
}
\tag{25}
\]

Thus a decisive next step has a cleaner arithmetic form. One must determine whether the affine class

\[
-\frac12\mathbf1*U_N+\mathcal N_{\rm sw}
\tag{26}
\]

contains profiles whose negative mass is `o(C_k)` on late dyadic divisor bands, in the scale regime relevant to the growing reservoir construction. A positive lower bound for the best achievable negative density would give the coefficient-level obstruction sought after FD-233. A construction driving that density to zero would remove coefficient-level positivity as an obstruction and return the problem to finite prime capacity and integer source realization.

What FD-234 rules out is a more superficial possibility: the apparent one-sided difficulty is **not** caused by parity or nearest-integer choices in FD-225. Those choices move the correction only by a uniformly blind, capacity-negligible vector.

This finding does not prove either sign alternative for (25), does not improve a Mertens estimate, and does not assert that the real-valued profile (25) is itself a feasible prime occupancy. It only identifies the exact canonical coefficient object on which the remaining one-sided question depends.

## 5. Prior-art boundary and verdict

The prior-art audit found only the standard Möbius-inversion/Dirichlet-convolution identities underlying (13), together with the classical elementary divisor-sum bound used in (21). No external theorem is load-bearing, and no novelty is claimed for those general identities. The research-specific content is their combination with the FD-225 divisor-response inverse and the FD-233 one-sided lift criterion to show exact affine equivalence between the integer repair and the block-Mertens convolution.

No new source anchor is therefore needed in `SOURCES.md`.

**Verdict.** The nearest-integer step can be removed from the live positivity frontier. The concrete FD-225 repair and the canonical real divisor smoothing of block Möbius sums differ by a profile with `|r_N(n)|<=tau(n)`, uniformly bounded switched response and vanishing normalized dyadic total variation. They define the same switched affine class, so the remaining coefficient-level question is genuinely arithmetic and one-sided: understand the negative-capacity distance of `-(1/2)(1*U_N)` to the switched-blind subspace.