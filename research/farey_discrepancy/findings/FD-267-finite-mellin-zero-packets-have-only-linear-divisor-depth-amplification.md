# FD-267 — Finite Mellin zero packets have only linear divisor-depth amplification

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** canonical full-grid repair / Mellin zero packets / divisor smoothing / source-side route pruning / spectral-complexity threshold / first-row comparison
- **Depends on:** FD-040, FD-234, FD-260, FD-261, FD-262, FD-265, FD-266
- **Classification:** `EXACT-DERIVED + FINITE-MELLIN-PACKET + DIVISOR-REPLICATION-BOUND + LINEAR-DEPTH-CEILING + SPECTRAL-COMPLEXITY-THRESHOLD + ROUTE-PRUNING`

## Claim

FD-265--FD-266 reduce the canonical full-grid positivity problem to one-sided mass of the divisor-smoothed Mertens block field

\[
U_N(q)=M(qN)-M((q-1)N),
\qquad
G_N(d)=\sum_{q\mid d}U_N(q).
\]

FD-261 shows that, at the same arithmetic amplitude as the first switched row, the general positive-cushion theorem can improve the first-row obstruction only if the source demand gains a divisor-depth exponent

\[
\alpha>2-\beta,
\qquad
\beta=\log_2\frac32,
\qquad
2-\beta=1.4150374992\ldots .
\]

A natural hope is that an off-critical zeta-zero mode, or a finite packet of such modes, might supply that amplification through the many Mertens blocks in the canonical inverse. It cannot.

Fix a finite Mellin packet

\[
F(t)=\sum_{j=1}^J a_j t^{\rho_j},
\qquad
\rho_j=\sigma_j+i\gamma_j,
\qquad
0<\sigma_j\le\theta<1,
\tag{1}
\]

and put `F(0)=0`. For a horizon `N`, sample

\[
A_{F,N}(q)=F(Nq),
\qquad
U_{F,N}(q)=A_{F,N}(q)-A_{F,N}(q-1),
\tag{2}
\]

and apply the same divisor smoothing as the full-grid repair,

\[
G_{F,N}(d)=\sum_{q\mid d}U_{F,N}(q).
\tag{3}
\]

Define the fixed packet norm

\[
W(F):=\sum_{j=1}^J |a_j|(1+|\rho_j|).
\tag{4}
\]

Then for every integer `x>=1`,

\[
\boxed{
\sum_{x<d\le2x}|G_{F,N}(d)|
\ll_\theta
W(F)N^\theta x.
}
\tag{5}
\]

Consequently the real canonical correction contributed by this packet,

\[
\widetilde c_{F,N}(d)=-\frac12G_{F,N}(d),
\tag{6}
\]

has one-sided negative demand

\[
\boxed{
\sum_{x<d\le2x}(-\widetilde c_{F,N}(d))_+
\ll_\theta
W(F)N^\theta x.
}
\tag{7}
\]

Thus every **fixed** finite packet has only linear divisor-depth amplification. The same remains true up to fixed powers of `log(Nx)` for packets whose terms are

\[
t^{\rho_j}P_j(\log t)
\tag{8}
\]

with fixed polynomials `P_j`, as arise from finite-order poles or repeated residues.

In the polynomial-depth regime `D=N^{\lambda+o(1)}`, a fixed packet therefore contributes at most

\[
N^{\theta+o(1)}D^{1+o(1)}.
\tag{9}
\]

Its effective depth exponent is `alpha=1`, so by FD-261 it cannot make the general FD-260 deep-band obstruction decisive at or before the independent first-row scale. A finite collection of rightmost zero residues can carry the off-critical arithmetic exponent, but **cannot by itself supply the missing superlinear depth exponent**.

There is a quantitative growing-packet version. If a packet family has weighted complexity

\[
W_D=D^{\omega+o(1)},
\tag{10}
\]

then (5) gives effective depth exponent at most

\[
\alpha\le1+\omega.
\tag{11}
\]

Therefore a Mellin-packet route can cross FD-261's first-row comparison only if

\[
\boxed{
\omega>1-\beta
=0.4150374992\ldots .
}
\tag{12}
\]

So the missing amplification, if it is spectral, must come from **polynomially growing weighted spectral complexity**. Fixed packets, logarithmically growing packets, and more generally `W_D=D^{o(1)}` packets remain below the required phase boundary.

## 1. One Mellin mode loses one power under block differencing

For a single exponent `rho=sigma+i gamma` with `0<sigma<1`, and every integer `q>=2`,

\[
q^\rho-(q-1)^\rho
=
\rho\int_{q-1}^{q}t^{\rho-1}\,dt.
\tag{13}
\]

Hence

\[
\begin{aligned}
|q^\rho-(q-1)^\rho|
&\le
|\rho|\int_{q-1}^{q}t^{\sigma-1}\,dt\\
&\le
|\rho|(q-1)^{\sigma-1}\\
&\le
2|\rho|q^{\theta-1},
\end{aligned}
\tag{14}
\]

where the last inequality uses `sigma<=theta<1`. At `q=1`, with `0^rho=0`, the difference is exactly one. Summing the packet terms and using `N^{sigma_j}<=N^theta` gives

\[
|U_{F,N}(1)|
\le
W(F)N^\theta,
\tag{15}
\]

and, for `q>=2`,

\[
\boxed{
|U_{F,N}(q)|
\le
2W(F)N^\theta q^{\theta-1}.
}
\tag{16}
\]

This is the crucial loss. A Mellin mode has amplitude `N^theta q^theta`, but a consecutive block increment has amplitude only `N^theta q^(theta-1)`. Since `theta<1`, the block amplitudes decay after normalization by their first-scale amplitude rather than grow with divisor depth.

For a logarithmic residue term `t^rho P(log t)`, differentiation gives

\[
\frac d{dt}\bigl(t^\rho P(\log t)\bigr)
=
t^{\rho-1}\bigl(\rho P(\log t)+P'(\log t)\bigr).
\tag{17}
\]

The same argument therefore inserts only a fixed factor `O((log(Nx))^k)` where `k` is the maximum polynomial degree. Such factors are `D^{o(1)}` in every fixed polynomial-depth comparison.

## 2. Divisor replication restores only the one lost power

For the dyadic coefficient band

\[
I_x=\{d:x<d\le2x\},
\]

let

\[
m_x(q)
:=
\#\{d\in I_x:q\mid d\}
=
\left\lfloor\frac{2x}{q}\right\rfloor
-
\left\lfloor\frac{x}{q}\right\rfloor.
\tag{18}
\]

This is the exact replication multiplicity used in FD-263. Triangle inequality and exchange of the finite sums give

\[
\sum_{d\in I_x}|G_{F,N}(d)|
\le
\sum_{q\le2x}|U_{F,N}(q)|m_x(q).
\tag{19}
\]

For `q<=x`,

\[
m_x(q)\le\frac{2x}{q},
\tag{20}
\]

while for `x<q<=2x` one has exactly `m_x(q)=1`. Insert (15)--(16). The `q=1` term is `O(W(F)N^theta x)`. For `2<=q<=x`,

\[
\begin{aligned}
\sum_{2\le q\le x}
|U_{F,N}(q)|m_x(q)
&\ll
W(F)N^\theta x
\sum_{q=2}^{x}q^{\theta-2}\\
&\ll_\theta
W(F)N^\theta x,
\end{aligned}
\tag{21}
\]

because `theta-2<-1`. Finally,

\[
\sum_{x<q\le2x}|U_{F,N}(q)|
\ll_\theta
W(F)N^\theta x^\theta
\ll
W(F)N^\theta x.
\tag{22}
\]

Equations (19)--(22) prove (5).

This identifies exactly why divisor smoothing does not turn a fixed zero mode into a superlinear source. Differencing costs one power of the block index. The shallow divisor rays replicate a block about `x/q` times, restoring at most that one power. The remaining series is `sum q^(theta-2)`, which converges precisely because every nontrivial zeta zero lies to the left of `Re(s)=1`.

The argument is insensitive to phases. Arbitrary interference among finitely many frequencies can only reduce the left side of (19); no phase alignment can defeat the absolute packet bound.

## 3. One-sided demand cannot be larger than the packet `l^1` field

For the real canonical correction (6), coordinatewise

\[
(-\widetilde c_{F,N}(d))_+
\le
|\widetilde c_{F,N}(d)|
=
\frac12|G_{F,N}(d)|.
\tag{23}
\]

Summing (23) and applying (5) proves (7). Thus the packet cannot generate a one-sided demand larger than linear depth even under the most favorable sign polarization.

This is stronger, for this source class, than the general route diagnostics in FD-265--FD-266. Those findings correctly show that arbitrary Mertens blocks could in principle accumulate a large post-convolution positive field if enough deep positive variation survives negative divisor ancestry. A fixed Mellin packet cannot populate that arbitrary block geometry: its own consecutive increments already obey (16), and the full divisor-replication ledger sums to only (5).

In particular, the prime/ancestry-free channel of FD-266 also stays below the same ceiling. Restricting (22) to primes, or to any other subset of the deep shell, can only decrease the absolute mass.

## 4. Stability under an explicit-formula remainder

The conclusion is not restricted to an exact packet identity. Suppose on `0<=q<=2x` a sampled source decomposes as

\[
A_N(q)=F(Nq)+E_N(q),
\qquad
E_N(0)=0.
\tag{24}
\]

Let

\[
\Delta E_N(q)=E_N(q)-E_N(q-1).
\]

By linearity of the divisor transform,

\[
G_N=G_{F,N}+\mathbf 1*\Delta E_N.
\tag{25}
\]

Therefore

\[
\boxed{
\sum_{d\in I_x}|G_N(d)|
\ll_\theta
W(F)N^\theta x
+
\sum_{q\le2x}|\Delta E_N(q)|m_x(q).
}
\tag{26}
\]

A coarse but useful uniform form follows from

\[
\sum_{q\le2x}m_x(q)
=
\sum_{d\in I_x}\tau(d)
\ll x\log x.
\tag{27}
\]

If

\[
\max_{0\le q\le2x}|E_N(q)|\le\mathcal E_N(x),
\]

then `|Delta E_N(q)|<=2 mathcal E_N(x)` apart from an irrelevant endpoint improvement, so

\[
\boxed{
\sum_{d\in I_x}|G_N(d)|
\ll_\theta
W(F)N^\theta x
+
\mathcal E_N(x)x\log x.
}
\tag{28}
\]

Thus a finite dominant packet together with a remainder that stays at the same arithmetic power scale, `mathcal E_N(D)=N^{theta+o(1)}`, still produces only

\[
N^{\theta+o(1)}D^{1+o(1)}
\]

repair mass. Any successful explicit-formula implementation of the FD-265/266 route must therefore place the missing polynomial depth growth either in the **weighted complexity of the zero packet** or in a remainder whose amplitude itself grows polynomially across the sampled divisor range.

For the nearest-integer repair of FD-225/FD-234, the additional rounding field has band `l^1` norm `O(x log x)`, so it does not change any of these polynomial depth exponents.

## 5. Phase consequence: fixed packets cannot improve the first-row ceiling

Take `x asymp D` and suppose the packet lives at arithmetic scale `N^{theta+o(1)}`. Equations (7) and (28), in the amplitude-stable remainder regime, have the FD-261 form

\[
R_N(x)
\le
N^{\theta+o(1)}D^{1+o(1)}.
\tag{29}
\]

Thus any lower bound extracted solely from such a packet has `alpha<=1`. FD-261 already proves that a linear-depth demand can contradict the general FD-260 cushion ceiling only beyond

\[
\lambda>\frac{1-\theta}{\beta},
\tag{30}
\]

whereas the same arithmetic amplitude is visible in the first switched row at

\[
\lambda=1-\theta.
\tag{31}
\]

Since `beta<1`, (30) is strictly later than (31). The finite-packet mechanism therefore cannot improve the first-row polynomial-depth obstruction.

Now let the packet itself grow with depth and write `W_D=D^{omega+o(1)}`. Equation (5) changes (29) to effective exponent `alpha<=1+omega`. For the deep-band route to become decisive at or before the first-row scale, FD-261 requires

\[
1+\omega>2-\beta,
\]

which is exactly (12).

This gives the surviving spectral target a quantitative form. It is not enough that more zero modes be present; their derivative-weighted absolute coefficient mass must grow at least polynomially at exponent `1-beta` in the divisor depth before this route can improve the first-row bound.

For a standard simple-zero residue term

\[
\frac{t^\rho}{\rho\zeta'(\rho)},
\tag{32}
\]

the derivative weight appearing in (14) is

\[
\left|\frac1{\rho\zeta'(\rho)}\right||\rho|
=
\frac1{|\zeta'(\rho)|}.
\tag{33}
\]

Thus, under a simple-zero explicit-formula interpretation, the relevant packet complexity is naturally controlled by sums of reciprocal `|zeta'(rho)|`. This observation is only a calibration: no simplicity assumption, zero-sum estimate, or explicit-formula truncation theorem is used in the proof above.

## 6. Prior-art boundary and finite audit

The classical Perron/residue representation of the Mertens function by zeta zeros is standard; the line already anchors the Mertens/zeta-zero frontier in Titchmarsh and uses finite Mellin packets elsewhere in FD-040. Modern work on negative discrete moments of `zeta'(rho)` studies exactly the reciprocal derivative weights that appear in (33), including the Gonek--Hejhal moment framework and recent conditional bounds. A targeted search found no matching result for the repository-specific composition used here: consecutive Mellin block differencing, exact divisor-replication into the canonical Farey full-grid repair, and the resulting `D^(1-beta)` spectral-complexity threshold. No external theorem is load-bearing, so `SOURCES.md` does not need a new dependency.

As a finite sign/scale audit, taking one mode `rho=0.6+14i` and evaluating the exact definitions (2)--(3) on dyadic bands gives `sum|G|/(N^0.6 x)` remaining bounded as `x` grows, while the triangle replication ledger in (19) approaches a larger but still bounded constant. The computation only checks conventions; the proof is (13)--(22).

The result does **not** prove that the actual Mertens function is controlled by a fixed zero packet on the required scales, nor that a growing zero packet satisfies or fails (12). It therefore does not close the canonical full-grid route. It removes a more specific possibility: the missing superlinear source demand cannot be attributed to one off-critical zero, finitely many rightmost zeros, or any subpower-weight Mellin packet whose remainder stays on the same arithmetic amplitude scale.

**Verdict.** FD-266 localizes one-sided escape to a signed cross-scale divisor cover. FD-267 shows that a fixed Mellin spectral explanation of the Mertens path is too smooth to make that cover problem exponent-critical: block differencing loses one power and divisor replication restores only one, leaving linear depth. Any spectral route that genuinely beats the first-row ceiling must introduce at least `D^(1-beta-o(1))=D^(0.415037...-o(1))` weighted complexity, or else obtain the missing amplification from the non-packet remainder or from a stronger positive cone such as FD-259.