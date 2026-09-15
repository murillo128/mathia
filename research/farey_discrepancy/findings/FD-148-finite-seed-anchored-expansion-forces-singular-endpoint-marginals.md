# FD-148 — Finite-seed anchored expansion forces singular endpoint marginals

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact reweighting obstruction / quantitative anchored-cut refinement
- **Depends on:** FD-147

## Claim

FD-147 leaves one local coefficient-side escape open: replace uniform ancestry-edge weights by source-native nonuniform weights whose anchored cut exposure stays uniformly positive. The first necessary condition on such a reweighting is already severe.

Let

\[
V_T=\{n\le T:\mu^2(n)=1\},
\qquad
E_T=\{(n,pn):n,pn\in V_T,\ p\text{ prime}\},
\tag{1}
\]

and equip `V_T` with the uniform coefficient measure

\[
\nu_T(n)=|V_T|^{-1}.
\tag{2}
\]

Let `D` be any fixed finite divisor-closed subset of the squarefree integers containing `1`, and let `eta_T` be an arbitrary probability measure on `E_T`. Write its parent and child endpoint marginals as

\[
\eta_T^-(n)
:=\sum_{p:(n,pn)\in E_T}\eta_T(n,pn),
\tag{3}
\]

and

\[
\eta_T^+(m)
:=\sum_{p\mid m}\eta_T(m/p,m).
\tag{4}
\]

Define the children reached in one ancestry step from the fixed seed,

\[
C_D(T)
:=\{m\in V_T\setminus D:\exists n\in D,\ \exists p\text{ prime},\ m=np\}.
\tag{5}
\]

For the anchored binary Cheeger constant of FD-147,

\[
h_{D,T}
:=
\inf_{\varnothing\ne A\subseteq V_T\setminus D}
\frac{\eta_T(\partial A)}{\nu_T(A)},
\tag{6}
\]

one always has

\[
\boxed{
h_{D,T}
\le
\frac{\sum_{n\in D}\eta_T^-(n)}{1-\nu_T(D)}
}
\tag{7}
\]

and

\[
\boxed{
h_{D,T}
\le
\frac{\sum_{m\in C_D(T)}\eta_T^+(m)}{1-\nu_T(D)}.
}
\tag{8}
\]

These elementary bounds turn the finite-seed geometry into two quantitative amplification taxes.

If the parent marginal is `K_T`-dominated by the coefficient measure on the seed,

\[
\eta_T^-(n)\le K_T\nu_T(n)
\qquad(n\in D),
\tag{9}
\]

then

\[
\boxed{
h_{D,T}
\le
(\zeta(2)|D|+o_D(1))\frac{K_T}{T}.
}
\tag{10}
\]

Hence every fixed finite `q` binary coercivity constant satisfies

\[
\boxed{
C^{\rm bin}_{q,D}(T)
\ge
\left(
\frac{T}{(\zeta(2)|D|+o_D(1))K_T}
\right)^{1/q}.
}
\tag{11}
\]

In particular **every parent-balanced reweighting with `K_T=o(T)` still has vanishing anchored expansion**.

There is a weaker but more permissive child-side obstruction. If

\[
\eta_T^+(m)\le L_T\nu_T(m)
\qquad(m\in C_D(T)),
\tag{12}
\]

then, with

\[
\kappa_D:=\sum_{n\in D}\frac1n,
\tag{13}
\]

one has

\[
\boxed{
h_{D,T}
\le
(\zeta(2)\kappa_D+o_D(1))
\frac{L_T}{\log T},
}
\tag{14}
\]

and therefore

\[
\boxed{
C^{\rm bin}_{q,D}(T)
\ge
\left(
\frac{\log T}
{(\zeta(2)\kappa_D+o_D(1))L_T}
\right)^{1/q}.
}
\tag{15}
\]

Thus **every child-balanced reweighting with `L_T=o(log T)` also fails**.

Equivalently, if one wants `h_{D,T}\ge c>0` for a fixed finite seed, then the edge measure must become singular relative to the uniform coefficient measure. It must place `Omega_c(1)` total edge mass on edges leaving the fixed seed, which is an average parent amplification of order at least `T`; and it must place `Omega_c(1)` incoming mass on the one-step child set `C_D(T)`, whose coefficient mass is only `O_D(1/log T)`, forcing average child amplification of order at least `log T`.

For the minimal anchor `D={1}`, the one-step child set is exactly the prime layer. Hence **uniform anchored expansion requires logarithmic amplification of the prime layer relative to its coefficient mass**, or an even more singular concentration on the anchor side.

## 1. The complement cut already controls every reweighting

FD-147 proves for binary Möbius orientations that the optimal finite-`L^q` anchored coercivity constant is exactly

\[
C^{\rm bin}_{q,D}(T)=h_{D,T}^{-1/q}.
\tag{16}
\]

To upper-bound `h_{D,T}`, no search over complicated cuts is needed. Test only

\[
A_T:=V_T\setminus D.
\tag{17}
\]

Since `D` is divisor-closed, no ancestry edge can enter `D` from `A_T`: if `pn\in D`, then `n\mid pn` forces `n\in D`. Therefore every boundary edge of `A_T` leaves a vertex of `D` and lands in `C_D(T)`.

Consequently

\[
\eta_T(\partial A_T)
\le
\sum_{n\in D}\eta_T^-(n),
\tag{18}
\]

which gives (7), and also

\[
\eta_T(\partial A_T)
\le
\sum_{m\in C_D(T)}\eta_T^+(m),
\tag{19}
\]

which gives (8). No reversibility, degree regularity, positivity beyond `eta_T` being a probability measure, or source model is used.

The point is structural. FD-147 says that a nonuniform edge measure can escape the uniform-edge obstruction only by making every macroscopic anchored cut expensive. Equations (7)--(8) show that the single complement cut already forces that expense to be paid through endpoint marginal concentration.

## 2. Parent-balanced local weights pay a linear amplification tax

The squarefree counting law gives

\[
|V_T|=\frac{T}{\zeta(2)}+o(T).
\tag{20}
\]

Because `D` is fixed,

\[
\nu_T(D)
=
\frac{|D|}{|V_T|}
=
(\zeta(2)|D|+o_D(1))T^{-1}.
\tag{21}
\]

Under (9),

\[
\sum_{n\in D}\eta_T^-(n)
\le
K_T\nu_T(D).
\tag{22}
\]

Substituting (21)--(22) into (7), and using `1-\nu_T(D)=1+o(1)`, proves (10). Equation (11) follows from the exact FD-147 identity (16).

The contrapositive is useful. If

\[
h_{D,T}\ge c>0,
\tag{23}
\]

then

\[
\sum_{n\in D}\eta_T^-(n)
\ge c(1-\nu_T(D))
=c+o(1).
\tag{24}
\]

Dividing by the coefficient mass of the seed gives

\[
\boxed{
\frac{\sum_{n\in D}\eta_T^-(n)}{\nu_T(D)}
\ge
\left(\frac{c}{\zeta(2)|D|}+o_D(1)\right)T.
}
\tag{25}
\]

So a weighting whose parent marginal is a bounded-distortion version of the target coefficient measure cannot possibly yield a positive anchored Cheeger constant. The edge law has to spend constant probability mass on a fixed set whose coefficient mass is `Theta_D(1/T)`.

This obstruction is stronger than the uniform-edge obstruction of FD-147 because uniform edge measure is already highly nonuniform in its parent marginal. FD-148 says that making the edge law *more balanced by parent* moves in the wrong direction for fixed-seed coercivity.

## 3. Child-balanced local weights still pay a logarithmic prime-ray tax

The child side is less singular because one fixed seed vertex has many prime children. For each `n\in D`, every child in `C_D(T)` arising from `n` has the form `np` with

\[
p\le T/n.
\tag{26}
\]

Hence, allowing overlaps between different seed parents,

\[
|C_D(T)|
\le
\sum_{n\in D}\pi(T/n).
\tag{27}
\]

Because `D` is fixed, the prime number theorem gives uniformly over its finitely many elements

\[
\sum_{n\in D}\pi(T/n)
=
(\kappa_D+o_D(1))\frac{T}{\log T}.
\tag{28}
\]

Combining (20), (27), and (28),

\[
\boxed{
\nu_T(C_D(T))
\le
(\zeta(2)\kappa_D+o_D(1))\frac1{\log T}.
}
\tag{29}
\]

Under (12),

\[
\sum_{m\in C_D(T)}\eta_T^+(m)
\le
L_T\nu_T(C_D(T)).
\tag{30}
\]

Equations (8), (29), and (30) prove (14), and (15) again follows from (16).

Conversely, positive anchored expansion as in (23) forces

\[
\sum_{m\in C_D(T)}\eta_T^+(m)
\ge c+o(1).
\tag{31}
\]

Since the entire child set has coefficient mass at most `O_D(1/log T)`, its average incoming amplification must obey

\[
\boxed{
\frac{\sum_{m\in C_D(T)}\eta_T^+(m)}
{\nu_T(C_D(T))}
\ge
\left(\frac{c}{\zeta(2)\kappa_D}+o_D(1)\right)\log T.
}
\tag{32}
\]

Thus the weakest local escape visible from the complement cut already requires logarithmic distortion of the child marginal.

## 4. The minimal anchor makes the tax exact on the prime fan

Take `D={1}`. Then

\[
C_D(T)=\{p\le T:p\text{ prime}\},
\tag{33}
\]

and every prime has exactly one incoming ancestry edge, namely `1->p`. Therefore

\[
\eta_T(\partial D)
=
\sum_{p\le T}\eta_T(1,p)
=
\sum_{p\le T}\eta_T^+(p).
\tag{34}
\]

The prime layer has uniform coefficient mass

\[
\nu_T(C_D(T))
=
\frac{\pi(T)}{|V_T|}
=
\frac{\zeta(2)+o(1)}{\log T}.
\tag{35}
\]

Hence a positive anchored expansion constant forces the prime fan to carry `Omega(1)` edge mass even though the prime coefficients carry only `Theta(1/log T)` of the target mass.

A canonical child-balanced normalization illustrates the barrier. Give each nontrivial child `m\in V_T\setminus\{1\}` total incoming edge mass `1/(|V_T|-1)` and split it arbitrarily among its `omega(m)` parents. Then the prime fan has mass exactly

\[
\frac{\pi(T)}{|V_T|-1}
=
\frac{\zeta(2)+o(1)}{\log T},
\tag{36}
\]

so

\[
h_{\{1\},T}
\le
\frac{\zeta(2)+o(1)}{\log T}
\tag{37}
\]

and

\[
C^{\rm bin}_{q,\{1\}}(T)
\ge
\left(\frac{\log T}{\zeta(2)+o(1)}\right)^{1/q}.
\tag{38}
\]

Thus rebalancing the uniform-edge law by child removes the extra `log log T` dilution seen in FD-147, but it still cannot produce uniform finite-`L^q` recovery. The remaining obstruction is the prime-layer density itself.

For comparison, the three normalizations have different failure scales on the same complement cut:

- uniform edges, as in FD-147, expose the minimal prime fan at order `1/(log T log log T)`;
- child-balanced edge mass can improve this to order `1/log T`;
- parent-balanced mass dominated by the uniform coefficient measure exposes a fixed seed at only order `1/T`.

A constant-order cut exposure is therefore not obtained by a benign local renormalization between these choices. It requires an explicitly singular emphasis on the seed boundary.

## 5. What this rules out, and what it does not

FD-148 does **not** prove that no nonuniform source-native weighting can have positive anchored expansion. It gives necessary marginal concentration conditions for any such weighting. A measure may deliberately assign constant mass to the prime fan, or otherwise overweight the one-step seed boundary by the required factors. The theorem permits that.

But such a weighting has changed something substantive: it is no longer a bounded-distortion redistribution of coefficient mass across local ancestry relations. For uniform coefficient recovery, a successful local edge law must overweight a set of child coefficients of mass `O(1/log T)` by at least a logarithmic factor, or overweight the fixed seed as a parent by a linear factor. This is a concrete cost that a proposed Farey-derived normalization must justify rather than hide inside the word “nonuniform.”

The result is also restricted to fixed finite anchoring and finite `L^q`. If the anchor grows with `T`, then `nu_T(D)` and `nu_T(C_D(T))` may have different scales. If the target vertex measure itself gives nonvanishing mass to the prime rays, the child-side logarithmic tax disappears, but then the coefficient norm has changed and its relevance to the Farey/Franel target must be proved separately. As in FD-147, `L^infinity` and genuinely nonlocal Farey/Fourier destination functionals are outside the finite-mass cut obstruction.

## 6. Prior-art and evidence boundary

Weighted Cheeger constants, Dirichlet boundary conditions, and the relation between boundary flow and Poincare-type coercivity are classical graph analysis. FD-147 already records that prior-art boundary. FD-148 claims no new abstract Cheeger theory.

The new line-specific statement is the arithmetic rate forced by the squarefree ancestry geometry: a fixed divisor-closed Möbius anchor has coefficient mass `Theta_D(1/T)`, while all of its one-step prime children have coefficient mass only `O_D(1/log T)`. Splicing those two scales with the exact binary cut identity of FD-147 yields the linear parent-amplification and logarithmic child-amplification necessities above.

No external theorem beyond the squarefree counting asymptotic and prime number theorem already anchored in `SOURCES.md` is load-bearing, so no source update is required.

## 7. Falsifiable next test

Any proposed source-native nonuniform ancestry weight should now be checked first at the endpoint-marginal level. Given its edge law `eta_T`, compute

\[
\eta_T^-(D)
\qquad\text{and}\qquad
\eta_T^+(C_D(T))
\tag{39}
\]

for a fixed divisor-closed Möbius seed. If the first is `o(1)`, or if the second is `o(1)`, the complement cut already forces `h_{D,T}->0`; there is no need to search for a subtler bad cut. More quantitatively, any child marginal dominated by `o(log T)` times the uniform coefficient measure is ruled out by (14).

Only after a candidate spends constant edge mass on this prime-thin seed boundary does the full all-cut problem of FD-147 become relevant. Passing FD-148 is therefore necessary but not sufficient: the next stage must still prove a uniform lower bound for *every* macroscopic anchored cut, and only after that does the independent information-budget obstruction of FD-144 become the live threshold.

## Conclusion

FD-147 showed that nonuniform ancestry weights could in principle evade the uniform-edge cut obstruction. FD-148 identifies the minimum price of that escape under the uniform coefficient norm:

\[
\boxed{
\text{positive finite-seed anchored expansion}
\Longrightarrow
\begin{cases}
\text{parent amplification }=\Omega_D(T),\\
\text{child prime-ray amplification }=\Omega_D(\log T).
\end{cases}
}
\tag{40}
\]

Thus ordinary local rebalancing is not enough. A successful coefficient-side ancestry observable must make a deliberately singular allocation of observation mass to the finite anchor boundary before it can even reach the all-cut coercivity test.