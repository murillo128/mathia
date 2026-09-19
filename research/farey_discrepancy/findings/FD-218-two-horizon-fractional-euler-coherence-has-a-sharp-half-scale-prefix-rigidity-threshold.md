# FD-218 — Two-horizon fractional Euler coherence has a sharp half-scale prefix-rigidity threshold

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** same-source cross-horizon coherence / switched root-filter countermodel / exact prime-reservoir cancellation / sharp finite-horizon representation boundary
- **Depends on:** FD-217, FD-029
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + TWO-HORIZON-COHERENCE + SHARP-HALF-SCALE-THRESHOLD + EXACT-RESERVOIR-CANCELLATION`

## Claim

`FD-217` shows that one isolated horizon remains blind when an `N`-dependent source obeys every Möbius Euler relation below any fixed fractional cutoff `theta N`, `theta<1`. The first genuinely same-source test is to require the **same** source to serve two adjacent horizons `N` and `2N`, with the cutoff scaling with the horizon.

Keep the period-three switched schedule

\[
q_j=(0,3,3,0,3,3,\ldots),
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

and

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix `0<theta<1/2`. For every sufficiently large integer `N` with

\[
\lfloor\log_2N\rfloor\equiv0\pmod3,
\]

there is one deterministic sequence

\[
\xi_n^{(N)}\in\{-1,0,1\},
\qquad (\xi_n^{(N)})^2=\mu(n)^2,
\qquad \xi_1^{(N)}=1,
\]

which obeys, globally,

\[
\boxed{
\xi_{pn}^{(N)}=-\xi_n^{(N)}
\quad
(p\le2\theta N,\ p\nmid n).
}
\tag{1}
\]

Thus the same source satisfies every requested relation `p<=theta H` at both `H=N` and `H=2N`. Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

one can arrange simultaneously

\[
\boxed{|\mathcal C_0^{X_N}(N)|\le1,}
\qquad
\boxed{|\mathcal C_3^{X_N}(2N)|\le3,}
\tag{2}
\]

while

\[
\boxed{
X_N(N)\asymp_\theta \frac{N}{\log N}.
}
\tag{3}
\]

The congruence condition on the dyadic band makes `q(N)=0` and `q(2N)=3`, so (2) is exactly simultaneous boundedness of the scheduled switched observation at the two adjacent horizons.

The boundary is sharp for this finite-horizon source class. If `theta>=1/2` and one source satisfies the same requirement at `2N`, then its imposed set contains every prime `p<=N`; squarefree support, `xi_1=1`, and the Euler law force

\[
\boxed{\xi_n=\mu(n)\quad(n\le N),}
\tag{4}
\]

hence `X(N)=M(N)`. Therefore the reservoir freedom that produces (3) survives two-horizon coupling for every fixed `theta<1/2`, and disappears exactly when the later horizon's cutoff reaches the earlier prefix.

This is a representation/information threshold, not an RH estimate. Equation (4) merely returns the physical Möbius prefix; it does not prove square-root cancellation for `M`.

## 1. Encode both horizons in one Euler-coherent source

Put

\[
Y=2\theta N,
\qquad
P_N=\{p\text{ prime}:p\le Y\},
\qquad
Q_N=\prod_{p\in P_N}p.
\]

Every squarefree integer has a unique factorization `n=dm`, with `d|Q_N` and `(m,Q_N)=1`. Choose core signs `eta_m in {-1,+1}`, set

\[
\xi_{dm}=\mu(d)\eta_m
\]

on squarefree integers, and put `xi_n=0` on nonsquarefree integers. Then (1) holds identically for every selected prime.

Begin with the physical core `eta_m=mu(m)` and flip only selected **unconstrained core primes** `r>Y`, changing their core sign from `-1` to `+1`. For all reservoirs used below, `r>(32/33)N`. Hence for every sampled point `x<=32N`,

\[
\left\lfloor\frac xr\right\rfloor\le32.
\]

For sufficiently large `N`, every prime at most `32` lies in `P_N`. Consequently the contribution of one flipped core prime is exactly

\[
2\sum_{\substack{d\mid Q_N\\d\le x/r}}\mu(d)
=
2M\!\left(\left\lfloor\frac xr\right\rfloor\right),
\]

and for any finite flip set `R`,

\[
\boxed{
X_N(x)-M(x)
=
2\sum_{r\in R}M\!\left(\left\lfloor\frac xr\right\rfloor\right)
\qquad
(x\in\{N,2N,4N,8N,16N,32N\}).
}
\tag{5}
\]

Thus simultaneous two-horizon control reduces to a finite exact response-vector problem.

## 2. Three prime reservoirs diagonalize the two observations

Let

\[
a_\theta=\max\{2\theta,32/33\}.
\]

Use three disjoint prime reservoirs

\[
L=(a_\theta N,N],
\qquad
H_1=(32N/29,8N/7),
\qquad
H_2=(32N/11,16N/5).
\tag{6}
\]

All their primes exceed `Y`. For `r in L`, the floor vector at multiples `N,2N,4N,8N,16N,32N` is

\[
(1,2,4,8,16,32).
\]

For `r in H_1` it is

\[
(0,1,3,7,14,28),
\]

and for `r in H_2` it is

\[
(0,0,1,2,5,10).
\]

Using

\[
(M(1),M(2),M(4),M(8),M(16),M(32))=(1,0,-1,-2,-1,-4),
\]

\[
(M(1),M(3),M(7),M(14),M(28))=(1,-1,-2,-2,-1),
\]

and

\[
(M(1),M(2),M(5),M(10))=(1,0,-2,-1),
\]

formula (5) gives the exact response pair

\[
(\Delta\mathcal C_0(N),\Delta\mathcal C_3(2N))
=
\begin{cases}
(-2,-16),&r\in L,\\
(+2,0),&r\in H_1,\\
(0,+6),&r\in H_2.
\end{cases}
\tag{7}
\]

A flip in `L` also increases `X_N(N)` by `2`; flips in `H_1` or `H_2` do not change that prefix. The response matrix is therefore already triangular: one high reservoir repairs the first observation without touching the second, and the other repairs only the second.

The prime number theorem gives

\[
|L|\sim(1-a_\theta)\frac N{\log N},
\qquad
|H_1|\sim\frac8{203}\frac N{\log N},
\qquad
|H_2|\sim\frac{16}{55}\frac N{\log N}.
\tag{8}
\]

Because `theta<1/2`, the first constant is positive. Choose a fixed `kappa_theta>0` sufficiently small compared with the three capacities, for example

\[
0<\kappa_\theta<
\frac14\min\left\{1-a_\theta,\frac8{203},\frac6{55}\right\},
\]

and let

\[
A=\left\lfloor\kappa_\theta\frac N{\log N}\right\rfloor
\]

be the number of low-reservoir flips.

Let the physical baselines be

\[
b_0=M(2N)-M(N),
\]

\[
b_3=M(32N)-4M(16N)+6M(8N)-4M(4N)+M(2N).
\]

The Davenport bound already anchored in `SOURCES.md` gives

\[
b_0=o(N/\log N),
\qquad
b_3=o(N/\log N).
\tag{9}
\]

Choose `B` primes from `H_1` with `B` the nearest admissible integer to

\[
A-b_0/2,
\]

and choose `C` primes from `H_2` with `C` the nearest admissible integer to

\[
(16A-b_3)/6.
\]

By (8)--(9) and the choice of `kappa_theta`, for all sufficiently large `N` both counts are nonnegative and lie strictly inside their reservoir capacities. Equation (7) then gives exactly the bounded residuals in (2): nearest-integer rounding leaves at most `1` in the first coordinate and at most `3` in the second.

Only the `A` low flips lie below `N`, so

\[
X_N(N)=M(N)+2A
=
(2\kappa_\theta+o(1))\frac N{\log N},
\tag{10}
\]

again by Davenport. This proves (3).

## 3. Why one half is the exact locking point

Suppose now `theta>=1/2`. The later-horizon requirement includes every prime

\[
p\le2\theta N\ge N.
\]

If `n<=N` is squarefree, write `n=p_1\cdots p_k`. Starting from `xi_1=1`, every prime factor `p_i` is in the imposed set, so repeated use of the exact Euler relation gives

\[
\xi_n=(-1)^k=\mu(n).
\]

On nonsquarefree integers both sequences vanish. Hence (4) follows.

The mechanism is therefore not “two observations are automatically coercive.” For `theta<1/2`, even two bounded switched readouts leave a macroscopic prime reservoir and can be repaired independently by exact response vectors. Coercivity appears only when cross-horizon prime coverage itself reaches the earlier prefix. This is the same pointwise recovery mechanism isolated abstractly in `FD-029`, now paired with an explicit two-horizon countermodel showing sharpness below the threshold.

## 4. Representation audit, prior art, and research consequence

The countermodel is one arithmetic sequence for the pair `(N,2N)`, not two independently retuned sources. Its squarefree zero set and amplitudes are physical, and every selected Euler relation holds globally. The remaining nonphysical freedom is equally explicit: signs of core primes above `2 theta N` are not constrained multiplicatively, and the whole source may still depend on the target pair `N,2N`. Therefore the construction cannot be diagonalized into one persistent source over infinitely many horizons without new work.

The closest prior art located remains the literature on globally multiplicative squarefree-supported functions with prescribed prime signs, notably Aymone, *A note on multiplicative functions resembling the Möbius function* (arXiv `1908.11014`), and Liu, *Multiplicative functions resembling the Möbius function* (arXiv `2205.00972`), together with Tao's treatment of Möbius sums on semigroups generated by arbitrary prime sets. Those works concern genuine multiplicativity or prime-generated semigroups; they do not provide the finite-horizon triangular reservoir cancellation in (6)--(7). No external theorem beyond the fixed-ratio prime number theorem and Davenport cancellation already anchored in line-local `SOURCES.md` is load-bearing, so no source-file update is required.

The substantive boundary is now sharper than after `FD-217`: **same-source coupling of two adjacent horizons is still insufficient whenever the later cutoff stops short of the earlier prefix.** The relevant resource is not merely overlap between horizons, but whether cumulative multiplicative coverage actually closes the earlier source degrees of freedom. A next genuinely different test is a longer horizon block or one persistent source across growing blocks, where reservoir signs chosen to repair an early observation must survive several later observations and cannot be relocated freely.
