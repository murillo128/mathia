# FD-152 — Growing rank anchors have a Gaussian child-depth window

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing-anchor obstruction / Gaussian depth phase diagram
- **Depends on:** FD-147, FD-149, FD-150, FD-151

## Claim

FD-151 shows that bounded parent distortion forces a low-rank squarefree anchor to enter the Erdős--Kac window and therefore to contain a positive fraction of the coefficient space. That leaves a second question: after paying for a macroscopic growing anchor, how much additional ancestry depth is still needed before the child side of the same complement cut can carry a positive amount of boundary mass?

For the canonical rank anchors, the answer is exact at the level of this cut. The fixed-anchor `log log T` child-depth scale of FD-149--FD-150 collapses to the **Erdős--Kac fluctuation scale `sqrt(log log T)`**, but it does not disappear.

Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1},
\qquad
\lambda_T:=\log\log T.
\tag{1}
\]

For an integer rank `r>=0`, define the divisor-closed anchor

\[
D_T(r):=\{n\in V_T:\omega(n)\le r\},
\qquad
p_T(r):=\nu_T(D_T(r)).
\tag{2}
\]

For an integer depth `L>=1`, retain the positive divisibility relation

\[
E_T^{(\le L)}
:=
\{(n,m)\in V_T^2:n\mid m,\ 1\le\omega(m/n)\le L\}.
\tag{3}
\]

Let `eta_T` be any probability measure on `E_T^(<=L)`, write `eta_T^-` and `eta_T^+` for its parent and child marginals, and let `h_{r,T}^{(<=L)}` denote the anchored Cheeger constant with anchor `D_T(r)`.

The descendants outside the anchor that can be reached from the anchor in at most `L` prime adjunctions are **exactly** the next `L` multiplicative ranks:

\[
\boxed{
R_{r,L}(T)
=
\{m\in V_T:r<\omega(m)\le r+L\}.
}
\tag{4}
\]

Put

\[
s_T(r,L)
:=\nu_T(R_{r,L}(T)).
\tag{5}
\]

Assume the endpoint marginals satisfy

\[
\eta_T^-(d)\le P_T\nu_T(d)
\qquad(d\in D_T(r)),
\tag{6}
\]

and

\[
\eta_T^+(m)\le K_T\nu_T(m)
\qquad(m\in R_{r,L}(T)).
\tag{7}
\]

Then the same complement cut gives the **joint parent/child screen**

\[
\boxed{
 h_{r,T}^{(\le L)}
 \le
 \frac{
 \min\{P_Tp_T(r),\ K_Ts_T(r,L)\}
 }{1-p_T(r)}.
}
\tag{8}
\]

Equivalently, the child part can be written as

\[
\boxed{
 h_{r,T}^{(\le L)}
 \le
 K_T\,
 \nu_T\!\left(
 r<\omega(n)\le r+L
 \;\middle|\;
 \omega(n)>r
 \right).
}
\tag{9}
\]

Thus depth is priced not by the total mass below rank `r+L`, but by the fraction of the **still-unanchored upper tail** captured by the first `L` ranks above the anchor.

Now take a central rank-anchor sequence `r_T` and depth sequence `L_T` such that

\[
\frac{r_T-\lambda_T}{\sqrt{\lambda_T}}
\longrightarrow z\in\mathbb R,
\qquad
\frac{L_T}{\sqrt{\lambda_T}}
\longrightarrow \ell\in[0,\infty).
\tag{10}
\]

Squarefree Erdős--Kac gives

\[
\boxed{
 p_T(r_T)\longrightarrow\Phi(z),
}
\tag{11}
\]

and, using the exact shell (4),

\[
\boxed{
 s_T(r_T,L_T)
 \longrightarrow
 \Phi(z+\ell)-\Phi(z).
}
\tag{12}
\]

Hence if `P_T<=P` and `K_T<=K`,

\[
\boxed{
\limsup_{T\to\infty} h_{r_T,T}^{(\le L_T)}
\le
\frac{
\min\{P\Phi(z),\ K[\Phi(z+\ell)-\Phi(z)]\}
}{1-\Phi(z)}.
}
\tag{13}
\]

This produces a sharp three-regime child transition for every fixed central anchor location `z`:

\[
L_T=o(\sqrt{\lambda_T})
\quad\Longrightarrow\quad
\frac{s_T(r_T,L_T)}{1-p_T(r_T)}\to0,
\tag{14}
\]

while

\[
L_T\sim\ell\sqrt{\lambda_T}
\quad\Longrightarrow\quad
\frac{s_T(r_T,L_T)}{1-p_T(r_T)}
\to
\frac{\Phi(z+\ell)-\Phi(z)}{1-\Phi(z)},
\tag{15}
\]

and

\[
\frac{L_T}{\sqrt{\lambda_T}}\to\infty
\quad\Longrightarrow\quad
\frac{s_T(r_T,L_T)}{1-p_T(r_T)}\to1.
\tag{16}
\]

Therefore, for a rank anchor that leaves a nonzero Gaussian tail unanchored, bounded child distortion cannot support positive finite-`L^q` anchored expansion at depth `o(sqrt(log log T))`. Once the anchor itself has moved from fixed rank to typical rank, the remaining child-depth obstruction is no longer order `log log T`; it is exactly the fluctuation width of the squarefree prime-factor distribution.

More quantitatively, suppose for some constants `c>0`, `P<infinity`, and `K<infinity`,

\[
\liminf h_{r_T,T}^{(\le L_T)}\ge c,
\qquad
P_T\le P,
\qquad
K_T\le K.
\tag{17}
\]

For a central limit point `(z,ell)` with finite `z` and finite `ell`, (8)--(13) force

\[
\boxed{
\Phi(z)\ge\frac{c}{P+c}
}
\tag{18}
\]

and

\[
\boxed{
\Phi(z+\ell)-\Phi(z)
\ge
\frac{c}{K}\,[1-\Phi(z)].
}
\tag{19}
\]

If `0<c<K`, then

\[
\boxed{
\ell
\ge
\Phi^{-1}\!\left(
\Phi(z)+\frac{c}{K}[1-\Phi(z)]
\right)-z.
}
\tag{20}
\]

The right side is strictly positive for every finite `z`. Thus any central anchor that leaves a fixed positive fraction of coefficients unanchored requires `L_T=Omega(sqrt(log log T))` under bounded child distortion. If `c=K`, no finite `ell` can satisfy (19); the complement cut requires `L_T/sqrt(lambda_T)->infinity`. If `c>K`, positive expansion is impossible under the stated child domination because (9) always gives `h<=K`.

## 1. The reachable set is an exact rank shell

Let `m\in V_T\setminus D_T(r)`. If `m` is reachable from the anchor in one `E_T^(<=L)` edge, there is some `d\in D_T(r)` with

\[
d\mid m,
\qquad
1\le\omega(m/d)\le L.
\tag{21}
\]

Because `d` and `m` are squarefree,

\[
\omega(m)
=\omega(d)+\omega(m/d)
\le r+L.
\tag{22}
\]

Since `m` lies outside the anchor, `omega(m)>r`. This proves one inclusion in (4).

Conversely, suppose

\[
r<\omega(m)\le r+L.
\tag{23}
\]

Choose any squarefree divisor `d|m` containing exactly `r` prime factors when `r>0`; for `r=0`, take `d=1`. Then `d<=m<=T`, so `d\in D_T(r)`, and

\[
1\le\omega(m/d)=\omega(m)-r\le L.
\tag{24}
\]

Hence `(d,m)\in E_T^(<=L)`, proving the reverse inclusion. Unlike the fixed-anchor squeeze in FD-150, the rank anchor therefore gives an exact shell rather than only upper and lower rank bounds.

## 2. One cut now exposes both resource bills

Take the complement of the anchor,

\[
A_T:=V_T\setminus D_T(r).
\tag{25}
\]

Divisor closure prevents an ancestry edge from starting in `A_T` and ending in `D_T(r)`. Every edge crossing this cut therefore starts in the anchor and ends in the reachable shell (4).

The parent estimate is exactly the FD-151 argument:

\[
\eta_T(\partial A_T)
\le
\sum_{d\in D_T(r)}\eta_T^-(d)
\le
P_Tp_T(r).
\tag{26}
\]

The same boundary can instead be charged to its child endpoints:

\[
\eta_T(\partial A_T)
\le
\sum_{m\in R_{r,L}(T)}\eta_T^+(m)
\le
K_Ts_T(r,L).
\tag{27}
\]

Since

\[
\nu_T(A_T)=1-p_T(r),
\tag{28}
\]

both estimates hold simultaneously, giving (8). Equation (9) is simply the child quotient in conditional-probability form.

This resolves a resource ambiguity left between FD-150 and FD-151. Anchor growth does not merely reduce the parent tax. It also changes the population against which the child depth must be measured: after rank `r` has been anchored, depth `L` only needs to expose a fixed fraction of the remaining upper tail, not a fixed fraction of the whole squarefree population.

## 3. Erdős--Kac turns the remaining tail into a Gaussian window

Under the uniform squarefree law `nu_T`, the normalized rank

\[
X_T(n):=
\frac{\omega(n)-\lambda_T}{\sqrt{\lambda_T}}
\tag{29}
\]

converges in distribution to a standard Gaussian. Since the Gaussian distribution function is continuous, the corresponding distribution functions converge uniformly. From (10),

\[
p_T(r_T)
=\nu_T\!\left(
X_T\le
\frac{r_T-\lambda_T}{\sqrt{\lambda_T}}
\right)
\to\Phi(z),
\tag{30}
\]

which is (11). Likewise

\[
s_T(r_T,L_T)
=
\nu_T\!\left(
\frac{r_T-\lambda_T}{\sqrt{\lambda_T}}
<X_T\le
\frac{r_T+L_T-\lambda_T}{\sqrt{\lambda_T}}
\right)
\to
\Phi(z+\ell)-\Phi(z),
\tag{31}
\]

proving (12).

The same argument gives (14): when `L_T=o(sqrt(lambda_T))`, both normalized shell endpoints converge to the same finite `z`, so their probability difference tends to zero. Since `1-p_T(r_T)->1-Phi(z)>0`, the conditional shell fraction also tends to zero.

If `L_T/sqrt(lambda_T)->infinity`, then for every fixed `B>z`, the shell eventually contains all ranks with normalized coordinate in `(z,B]`. Taking the lower limit and then `B->infinity` yields

\[
\liminf s_T(r_T,L_T)\ge1-\Phi(z).
\tag{32}
\]

The reverse bound `s_T<=1-p_T` is automatic, so (16) follows.

Thus `sqrt(log log T)` is not an artifact of choosing a particular fixed percentile. It is the exact width on which a central rank anchor can expose a nonzero but non-total fraction of the remaining coefficient mass.

## 4. The quantitative depth requirement is a conditional Gaussian quantile

Assume (17). From the parent half of (8),

\[
c
\le
\liminf\frac{P_Tp_T}{1-p_T}
\le
\frac{P\Phi(z)}{1-\Phi(z)},
\tag{33}
\]

which rearranges to (18).

From the child half,

\[
c
\le
K\,
\frac{\Phi(z+\ell)-\Phi(z)}{1-\Phi(z)},
\tag{34}
\]

which is (19). When `0<c<K`, its right-hand probability target lies strictly between `Phi(z)` and `1`, so applying the increasing inverse Gaussian CDF gives (20).

The interpretation is especially transparent: with child distortion budget `K`, a target expansion `c` requires the ancestry shell to capture at least the fraction `c/K` of the entire unanchored Gaussian tail. The needed depth is exactly the corresponding conditional-tail quantile measured in units of `sqrt(log log T)`.

At the smallest central anchor permitted by the parent cut,

\[
\Phi(z)=\frac{c}{P+c},
\tag{35}
\]

the required normalized depth becomes

\[
\ell
\ge
\Phi^{-1}\!\left(
\frac{c(K+P)}{K(P+c)}
\right)
-
\Phi^{-1}\!\left(
\frac{c}{P+c}
\right),
\qquad 0<c<K.
\tag{36}
\]

Equation (36) is not an optimum over all possible anchors: increasing the anchor further can reduce the remaining depth bill. That is precisely the trade exposed by (8). Driving the depth below the Gaussian width is possible only by moving the anchor farther into the upper tail, thereby fixing an even larger fraction of source coefficients. The theorem does not treat the near-total-anchor moderate-deviation regime, where `z=z_T->infinity` and a finer tail law is needed.

## 5. Relation to FD-149--FD-151

For a fixed finite anchor, FD-149--FD-150 measure descendants from a seed of bounded multiplicative rank. Reaching a positive fraction of all squarefree coefficients then requires absolute rank about `lambda_T`, so bounded child distortion forces depth `L_T` of order `log log T`.

FD-151 changes the parent side: bounded parent distortion is possible under the complement cut only after a rank anchor itself enters the central Erdős--Kac window. FD-152 shows what that purchase does to the child side. Once rank `r_T=lambda_T+O(sqrt(lambda_T))` has already been fixed, the unresolved coefficient population begins only one Gaussian fluctuation away, so the next positive fraction is reached after only `Theta(sqrt(lambda_T))` additional ranks.

The two depth scales therefore describe different starting points rather than competing estimates:

\[
\boxed{
\text{fixed seed}
\;\Rightarrow\;
L_T\asymp\log\log T,
\qquad
\text{central rank anchor}
\;\Rightarrow\;
L_T\asymp\sqrt{\log\log T}
}
\tag{37}
\]

at bounded child distortion, provided the central anchor leaves a nonvanishing fraction of coefficients unanchored.

This also sharpens the source-cost interpretation of FD-151. A macroscopic anchor buys more than parent regularity: it prepays almost all of the multiplicative-rank distance that the child transfer previously had to traverse. The remaining ancestry bill is only the Gaussian tail width. A proposal cannot therefore count a central anchor and a `log log T` transfer as independent evidence of strong nonlocality; much of that rank reach has already been spent in the anchor.

## 6. Stress tests and boundaries

The result is a **necessary-condition screen for one anchored complement cut**, not a sufficiency theorem for expansion. Even when (18)--(20) hold, another cut may have vanishing boundary. The theorem does not construct an admissible Farey edge measure with positive Cheeger constant.

The exact shell identity uses all of the following hypotheses: squarefree coefficients, rank anchor `omega<=r`, positive directed divisibility ancestry, and a depth measured by `omega(m/n)`. An arbitrary divisor-closed anchor need not have an exact shell description. Signed/oscillatory transfers, non-divisibility observations, `L^infinity`, or a different destination norm fall outside the claim.

The Gaussian phase law is stated only for central anchors with finite normalized location `z`. If the anchor mass tends to one, then `z_T` can leave every compact set and the unanchored tail itself becomes a moderate- or large-deviation object. In that regime `L_T=o(sqrt(lambda_T))` may capture a nontrivial conditional tail fraction, and weak Erdős--Kac alone cannot decide the scale. Such an escape is not free: the anchor then fixes `1-o(1)` of all squarefree source orientations. Quantifying that near-total-anchor regime requires a separate local/moderate-deviation theorem rather than extrapolating (15).

No local central-limit rate is used. In particular, FD-152 does **not** claim that a fixed-depth shell has mass asymptotic to a specific multiple of `1/sqrt(log log T)`. The vanishing statement (14) follows from weak convergence to a continuous Gaussian and remains valid without a local limit theorem.

## 7. Prior-art and novelty boundary

The arithmetic input is classical squarefree Erdős--Kac, already anchored in `research/farey_discrepancy/SOURCES.md` and already used in FD-149 and FD-151. The cut/Poincaré reduction is the established local framework of FD-147--FD-151. A literature audit also finds the classical Boolean-lattice rank/normalized-matching viewpoint as a nearby combinatorial analogue, but no external theorem is needed for the exact rank-shell identity or for the present Farey/Möbius resource splice.

No novelty is claimed for Gaussian rank fluctuations, Boolean-lattice rank geometry, or Cheeger testing on a boundary complement. The line-specific derived result is the combination (4), (8), and (11)--(20): **for growing squarefree rank anchors, the child endpoint tax is the conditional mass of a finite rank shell, and its bounded-distortion transition moves from the fixed-seed `log log T` scale to the central Gaussian width `sqrt(log log T)`.**

Because no new external theorem is load-bearing, this finding requires no addition to `SOURCES.md`.

## 8. Consequence for the Farey ancestry route

The coefficient-side resource audit now has a two-stage scale law. A sparse anchor with bounded parent distortion is impossible by FD-151. Moving the anchor into the typical-rank window repairs that particular parent cut only by fixing a macroscopic source fraction. After that move, shallow ancestry is still insufficient: if the unanchored fraction stays macroscopic, bounded child distortion requires traversal across `Theta(sqrt(log log T))` further multiplicative ranks.

A source-native positive proposal should therefore expose not only anchor mass `p_T`, parent distortion `P_T`, and absolute ancestry depth `L_T`, but the **conditional shell exposure**

\[
\frac{\nu_T(r_T<\omega\le r_T+L_T)}
{\nu_T(\omega>r_T)}.
\tag{38}
\]

If that ratio tends to zero while `K_T=O(1)`, the complement cut kills finite-`L^q` coercivity even though the anchor is already macroscopic. If the ratio stays positive, the next question is source validity: whether the actual Farey observable can justify both the macroscopic anchor and the required transfer weights without merely observing or reconstructing Möbius orientation.

Thus growing the anchor does not eliminate the ancestry bill. It **renormalizes the bill from absolute multiplicative depth to conditional tail depth**, and for every nontrivial central rank anchor that depth lives on the Erdős--Kac fluctuation scale.