# PC-013 — pure projective transfer is flat, and a Hill spectrum needs extra gauge

**Status:** `DECISIVE-NEGATIVE` for a spectrum obtained from the prime-circle projective sequence alone by multiplying canonical projective moving-frame transfers.

## Motivation

After PC-012, one attractive non-classical direction is to keep the exact ordered prime-circle vertices and treat them as a projective discrete curve rather than collapsing them to a scalar prime-gap statistic.

For example, after a Cayley chart one may use

\[
x_n=\cot\frac{\pi}{p_n}\in \mathbb R\subset\mathbb{RP}^1.
\]

Four consecutive vertices have the Möbius-invariant cross-ratio

\[
s_n=[x_n,x_{n+1},x_{n+2},x_{n+3}],
\]

which is an exact function of the circle geometry. Writing \(\Delta_n=x_{n+1}-x_n>0\), with the convention used by Marshall--Semenov-Tian-Shansky,

\[
\boxed{
 s_n=
 \frac{(\Delta_n+\Delta_{n+1})(\Delta_{n+1}+\Delta_{n+2})}
 {\Delta_n\Delta_{n+2}}.
}
\]

Since \(\Delta_n\sim g_n/\pi\), this retains a genuine multi-gap projective fluctuation instead of a single cuff or gap.

The known discrete-projective correspondence makes this look especially promising: a nondegenerate projective configuration may be lifted to vectors \(V_n\in\mathbb R^2\) with unit consecutive Wronskian,

\[
\det(V_{n+1},V_n)=1,
\]

and then satisfies a discrete Hill/Schrödinger recurrence

\[
V_{n+2}=k_nV_{n+1}-V_n.
\]

In the standard convention the projective Schwarzian obeys

\[
\boxed{s_n=k_nk_{n+1}.}
\]

The question was whether this gives a canonical transfer operator / monodromy spectrum attached directly to the prime-circle projective geometry.

## Obstruction 1: canonical projective transport telescopes

Choose any projective moving frame \(\rho_n\in PSL_2(\mathbb R)\) for the ordered configuration, for example the unique projective map normalizing three consecutive points to a fixed reference triple. Its Maurer--Cartan transport is

\[
K_n=\rho_{n+1}\rho_n^{-1}
\]

(up to the left/right convention).

Then on every finite interval,

\[
\boxed{
K_{N-1}K_{N-2}\cdots K_m
=\rho_N\rho_m^{-1}.
}
\]

Thus the actual group-valued transport of a globally defined one-dimensional moving frame is **pure gauge**: it depends only on the endpoint frames. It cannot accumulate an independent holonomy from the interior prime-gap fluctuations.

This is not special to the prime sequence. It is an elementary moving-frame identity, and Marí Beffa--Mansfield explicitly note that products of discrete Maurer--Cartan matrices along a path telescope to the frames at the endpoints. Nontrivial global relations arise only from topology/closed paths or patching different frame domains.

Our prime-circle sequence is a one-sided path, so no nontrivial fundamental-group holonomy is available without adding an external closure or another direction.

## Obstruction 2: the discrete Hill coefficients are not projectively unique on the infinite path

The Hill recurrence appears to evade the previous telescoping because it uses a lift \(V_n\), not merely the projective points \([V_n]\). But on a nonperiodic infinite sequence the unit-Wronskian lift still has an alternating gauge.

If \(V_n\) is normalized by

\[
\det(V_{n+1},V_n)=1,
\]

then so is

\[
\widetilde V_n=t_nV_n,
\qquad
t_nt_{n+1}=1.
\]

Hence

\[
t_n=c^{(-1)^n}
\]

for an arbitrary \(c>0\). The recurrence coefficient changes as

\[
\boxed{
\widetilde k_n=t_n^2 k_n
=c^{2(-1)^n}k_n,
}
\]

while the cross-ratio remains unchanged:

\[
\widetilde k_n\widetilde k_{n+1}=k_nk_{n+1}=s_n.
\]

This is precisely why the literature obtains uniqueness from an odd periodic/twisted closure: Mansfield--Marí Beffa--Wang state that the normalization can be uniquely solved when the period \(N\) is odd. The infinite prime-circle path has no such canonical periodic closure.

## The ambiguity changes the spectrum, not merely coordinates

Take the simplest projective configuration

\[
x_n=n.
\]

Its exact cross-ratio sequence is constant,

\[
s_n=4.
\]

The obvious unit-Wronskian lift \(V_n=(n,1)^T\) gives

\[
k_n=2.
\]

But the equally valid lift with alternating scale gives

\[
k_{2j}=2c^2,
\qquad
k_{2j+1}=2c^{-2}.
\]

All these lifts have the **same projective points and the same cross-ratios**.

If one now promotes the zero-energy recurrence to the usual self-adjoint discrete Schrödinger operator

\[
(H_c\psi)_n
=\psi_{n+1}+\psi_{n-1}-k_{n-1}\psi_n,
\]

its spectrum genuinely depends on \(c\). For \(c=1\),

\[
\sigma(H_1)=[-4,0].
\]

For example, for \(c=2\) the diagonal potential is period two with values \(-8\) and \(-1/2\); the Floquet discriminant is

\[
D(E)=(E+8)(E+1/2)-2,
\]

so

\[
\boxed{
\sigma(H_2)=[-17/2,-8]\cup[-1/2,0],
}
\]

which is manifestly different from \([-4,0]\).

Therefore the full Schrödinger spectrum is **not determined by the projective configuration** even though its zero-energy projective Schwarzian is.

## Consequence for the prime-circle program

This rules out the tempting chain

\[
\boxed{
\text{prime-circle vertices}
\to
\text{projective cross-ratios}
\to
\text{canonical }PSL_2\text{ transfer/monodromy}
\to
\text{new spectral invariant / RH}.
}
\]

There are two independent failures:

1. pure moving-frame transport on the one-dimensional path is flat/telescoping;
2. promoting the projective recurrence to a spectral Hill operator requires lift data that the projective geometry alone does not fix.

Thus a future spectral construction must use **additional geometry already present in the original circle**, not an arbitrary normalization. Legitimate candidates include the Euclidean/unit-circle metric, off-circle harmonic fields and the exact interior/exterior inversion, or a genuinely two-dimensional labeled structure with nontrivial loops. Introducing a periodic closure or choosing the alternating gauge merely to obtain a desired spectrum would be artificial.

## Literature check

- E. Mansfield, G. Marí Beffa, J. P. Wang, *Discrete Moving Frames and Discrete Integrable Systems*, Foundations of Computational Mathematics 13 (2013), 545--582, DOI 10.1007/s10208-013-9153-0. Their projective-line example constructs the unit-Wronskian lift and recurrence \(V_{s+2}=k_sV_{s+1}-V_s\), and notes uniqueness under an odd periodic/twisted condition.
- G. Marí Beffa, E. L. Mansfield, *Discrete Moving Frames on Lattice Varieties and Lattice-Based Multispaces*, Foundations of Computational Mathematics 18 (2018), 181--247. Their path transport is explicitly the product of Maurer--Cartan matrices and is noted to telescope to endpoint frames when a frame exists along the path.
- I. Marshall, M. Semenov-Tian-Shansky, *Poisson Groups and Differential Galois Theory of Schrödinger Equation on the Circle*, Communications in Mathematical Physics 284 (2008), 537--552. In the discrete projective setting the cross-ratio is the discrete Schwarzian and satisfies \(s_n=u_nu_{n+1}\).

No novelty is claimed for discrete moving-frame or Hill theory. The new research consequence is the exact obstruction for the prime-circle route: cross-ratio fluctuations are genuine projective invariants, but they do **not** by themselves canonically produce a global spectral operator on the infinite prime path.
