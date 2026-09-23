# FD-282 — Absolute grouped Perron contours retain a self-divisor depth plateau

- **Date:** 2026-09-23
- **Status:** proved method-level contour obstruction
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** truncated Perron / grouped repair kernel / horizontal contour / divisor replication / self-divisor plateau / route pruning
- **Depends on:** FD-261, FD-267, FD-281
- **Classification:** `EXACT-DERIVED + GROUPED-PERRON-KERNEL + SELF-DIVISOR-LOWER-BOUND + METHOD-LEVEL-OBSTRUCTION + PRIOR-ART-BOUNDARY`

## Claim

FD-281 shows that the classical pointwise truncated-Perron error remains too expensive after consecutive differencing and divisor replication. Its natural surviving suggestion is to move the physical repair operations inside the Perron contour before taking absolute values. That move does improve the kernel on the critical line, but it does **not** by itself solve the low-height remainder problem: the horizontal contour retains a right-hand collar near `Re(s)=1` whose grouped physical kernel has an unavoidable depth-scale plateau.

For `Re(s)>0`, define

\[
h_s(q):=\frac{q^s-(q-1)^s}{s},
\qquad
K_s(d):=\sum_{q\mid d}h_s(q),
\tag{1}
\]

with `0^s=0`. These are exactly the consecutive-difference and divisor-replication factors obtained by applying the FD-267 physical transform to the Perron kernel `y^s/s` before inserting `1/zeta(s)`.

Let

\[
I_x:=\{d:x<d\le 2x\},
\qquad
m_x(q):=\#\{d\in I_x:q\mid d\}.
\tag{2}
\]

For `s=sigma+it`, `|t|=T>=2`, one has the exact integral representation

\[
\boxed{
h_s(q)=\int_{q-1}^{q}u^{s-1}\,du.}
\tag{3}
\]

Consequently, after the divisor sum has already been grouped,

\[
\sum_{d\in I_x}|K_s(d)|
\le
\sum_{q\le2x}m_x(q)|h_s(q)|.
\tag{4}
\]

The right side has the frequency/depth transition

\[
\sum_{d\in I_x}|K_s(d)|
\ll_\sigma
\begin{cases}
 xT^{\sigma-1}, & 0<\sigma<1,\ 2\le T\le2x,\\
 x\left(1+\log\dfrac{2x}{T}\right), & \sigma=1,\ 2\le T\le2x,\\
 \dfrac{x(2x)^\sigma}{T}, & T\ge2x.
\end{cases}
\tag{5}
\]

Thus the critical-line kernel gains the useful factor `T^(-1/2)`, but the gain disappears as the horizontal edge approaches `sigma=1`. This is not merely an artifact of the upper bound. Put

\[
Y:=2Nx,
\qquad
c:=1+\frac1{\log Y}.
\tag{6}
\]

For all sufficiently large `x`, uniformly for

\[
2\le T\le \frac{x}{4},
\qquad
1\le\sigma\le c,
\tag{7}
\]

the **actual grouped kernel** satisfies

\[
\boxed{
\sum_{d\in I_x}|K_{\sigma+iT}(d)|
\gg
\frac{x}{\log x}.
}
\tag{8}
\]

The lower bound comes from the self-divisor coordinate on primes `p in (x,2x]`; it survives after summing all divisors of each such physical coordinate, so it is not the ungrouped triangle loss from FD-281.

Now consider the absolute-value cost of the right collar of the upper horizontal Perron edge,

\[
\mathfrak H(N,x,T)
:=
\int_1^c
\frac{N^\sigma}{|\zeta(\sigma+iT)|}
\sum_{d\in I_x}|K_{\sigma+iT}(d)|\,d\sigma.
\tag{9}
\]

Using the classical uniform estimate `|zeta(sigma+iT)| << log(2T)` for `sigma>=1`, `T>=2`, equation (8) yields

\[
\boxed{
\mathfrak H(N,x,T)
\gg
\frac{Nx}
{\log x\,\log(2T)\,\log(2Nx)}
}
\qquad
(2\le T\le x/4).
\tag{10}
\]

Up to logarithms, the absolute horizontal-collar certificate therefore costs `Nx` throughout every polynomially low cutoff `T=x^(tau+o(1))` with `tau<1`.

Against the FD-261/FD-281 same-amplitude repair threshold

\[
N^\theta x^{2-\beta},
\qquad
\beta:=\log_2\frac32,
\tag{11}
\]

and polynomial depth

\[
x=N^{\lambda+o(1)},
\tag{12}
\]

the ratio forced by (10) has exponent

\[
\boxed{
1-\theta-\lambda(1-\beta).
}
\tag{13}
\]

Hence any proof that first groups the physical divisor kernel but then bounds the horizontal edge by pointwise absolute values in `sigma` and physical coordinate `d` is still power-inadequate whenever

\[
\boxed{
\lambda<\frac{1-\theta}{1-\beta}.
}
\tag{14}
\]

At the critical calibration `theta=1/2`, the boundary is

\[
\frac{1}{2(1-\beta)}
=1.2047104198\ldots .
\tag{15}
\]

In particular this absolute grouped-contour route fails throughout the first-row scale `lambda=1/2` and, indeed, throughout every `lambda<=1`. At `lambda=1/2`, the collar cost exceeds the target by the polynomial factor

\[
N^{\beta/2-o(1)}
=N^{0.2924812503\ldots-o(1)}.
\tag{16}
\]

This is a **certificate obstruction**, not a lower bound for the true Perron remainder. The horizontal integral can still be small through cancellation in `sigma`, cancellation between the upper and lower horizontal edges, a signed/modified Perron formula, smoothing, or a contour architecture that never pays the pointwise absolute collar. What (8)--(16) rule out is the simpler hope that merely moving consecutive differencing and divisor replication inside the hard Perron contour makes a low-height triangle-inequality estimate strong enough.

## 1. The grouped repair kernel and its frequency cap

Equation (3) follows from the fundamental theorem of calculus for `Re(s)>0`:

\[
q^s-(q-1)^s
=s\int_{q-1}^{q}u^{s-1}\,du.
\]

For `q>=2`, it gives

\[
|h_s(q)|
\ll_\sigma q^{\sigma-1}.
\tag{17}
\]

The endpoint representation gives independently

\[
|h_s(q)|
\le
\frac{q^\sigma+(q-1)^\sigma}{|s|}
\le
\frac{2q^\sigma}{T}.
\tag{18}
\]

Thus

\[
|h_s(q)|
\ll_\sigma
q^{\sigma-1}
\min\left(1,\frac qT\right).
\tag{19}
\]

Also `h_s(1)=1/s`. Since

\[
m_x(q)
=
\left\lfloor\frac{2x}{q}\right\rfloor
-
\left\lfloor\frac{x}{q}\right\rfloor
\le \frac{x}{q}+1
\le \frac{3x}{q}
\qquad(q\le2x),
\tag{20}
\]

triangle inequality after the **full divisor grouping** gives (4). Split the `q`-sum at `q=T`. For `0<sigma<1`,

\[
\begin{aligned}
\sum_{q\le T}m_x(q)|h_s(q)|
&\ll_\sigma
\frac{x}{T}\sum_{q\le T}q^{\sigma-1}
\ll_\sigma xT^{\sigma-1},\\
\sum_{T<q\le2x}m_x(q)|h_s(q)|
&\ll_\sigma
x\sum_{q>T}q^{\sigma-2}
\ll_\sigma xT^{\sigma-1}.
\end{aligned}
\tag{21}
\]

At `sigma=1`, the first sum is `O(x)` and the second is

\[
O\!\left(x\sum_{T<q\le2x}\frac1q\right)
=O\!\left(x\left(1+\log\frac{2x}{T}\right)\right).
\tag{22}
\]

If `T>=2x`, use (18) throughout to obtain

\[
\sum_{q\le2x}m_x(q)|h_s(q)|
\ll_\sigma
\frac{x}{T}
\sum_{q\le2x}q^{\sigma-1}
\ll_\sigma
\frac{x(2x)^\sigma}{T}.
\tag{23}
\]

This proves (5). In particular the same consecutive difference that caps high Mellin frequencies in FD-268 genuinely helps on `sigma=1/2`, but it cannot give a power of `T` at `sigma=1` until the spectral height reaches the divisor depth itself.

## 2. Prime self-divisors make the right-collar plateau genuine

The upper estimate (5) alone would not exclude cancellation inside `K_s(d)`. Prime physical coordinates show that such cancellation cannot remove the whole right collar.

Let `p` be prime with `x<p<=2x`. Then its only divisors are `1` and `p`, so

\[
K_s(p)
=
\frac1s
+
\int_{p-1}^{p}u^{s-1}\,du.
\tag{24}
\]

Take `s=sigma+iT` under (7). Across `[p-1,p]`, the phase `T log u` varies by

\[
\Delta_p
=T\log\frac{p}{p-1}
\le
\frac{T}{p-1}
\le
\frac12
\tag{25}
\]

for all sufficiently large `x`. Rotate the integral in (24) by the midpoint phase. Since `sigma>=1`,

\[
\left|
\int_{p-1}^{p}u^{s-1}\,du
\right|
\ge
\cos\!\left(\frac14\right)
\int_{p-1}^{p}u^{\sigma-1}\,du
\ge
\cos\!\left(\frac14\right).
\tag{26}
\]

Meanwhile `|1/s|<=1/T<=1/2`. Therefore

\[
|K_s(p)|
\ge
\cos\!\left(\frac14\right)-\frac12
=:c_0>0.
\tag{27}
\]

Summing only over primes in `(x,2x]` and using the classical prime-number theorem (a Chebyshev lower bound would already suffice) gives

\[
\sum_{d\in I_x}|K_s(d)|
\ge
c_0\bigl(\pi(2x)-\pi(x)\bigr)
\gg
\frac{x}{\log x},
\tag{28}
\]

uniformly throughout the collar. This proves (8).

The mechanism is worth isolating. For a prime coordinate `d=p`, the terminal divisor `q=p` is a one-cell increment whose phase changes by only `O(T/p)`. At heights `T<<x` it therefore behaves almost like an undamped diagonal entry. Grouping the divisor sum has already happened in (24); the surviving mass is carried by the physical self-divisor itself.

## 3. The absolute horizontal collar is too expensive at the live depth scales

For `1<=sigma<=c` and `T>=2`, the standard partial-summation/Euler--Maclaurin estimate gives

\[
|\zeta(\sigma+iT)|\ll\log(2T).
\tag{29}
\]

One quick derivation is to truncate the Dirichlet series at height comparable to `T`: the finite sum is bounded by the harmonic sum `O(log T)`, while the tail correction `T^{1-s}/(s-1)` and the ordinary remainder are `O(1)` on `sigma>=1`. No zero-free estimate or RH input is needed.

Insert (8) and (29) into (9). Since `N^sigma>=N` and the collar width is exactly

\[
c-1=\frac1{\log(2Nx)},
\tag{30}
\]

we obtain (10).

This quantity is not asserted to equal the true horizontal contribution. It is the exact positive functional incurred by the following proof architecture:

\[
\text{move }\Delta_N\text{ and divisor replication inside the contour}
\;\to\;
\text{form }K_s(d)
\;\to\;
\text{take }|\cdot|\text{ in each }d
\;\to\;
\text{take pointwise absolute values along the horizontal edge}.
\tag{31}
\]

Because the collar is a positive subset of that absolute contour integral, any certificate of this form already pays (10) before the contour even reaches the critical strip.

At polynomial depth (12), logarithms are subpower. Dividing (10) by (11) gives

\[
\frac{\mathfrak H(N,x,T)}{N^\theta x^{2-\beta}}
\gg
N^{1-\theta-\lambda(1-\beta)-o(1)},
\tag{32}
\]

which proves (13)--(16).

The range relevant to the FD-278 low-height cluster ledger lies safely inside the hypothesis `T<=x/4`: every cutoff `T=x^(tau+o(1))` with fixed `tau<1` satisfies it eventually, in particular the informative cluster-pruning heights `tau` around `0.27--0.42`. Thus the right-collar obstruction appears precisely in the spectral-height regime FD-281 was trying to preserve.

## 4. Stress tests and failure modes

The first stress test is to remove divisor replication. The same prime calculation still leaves the single increment `h_s(p)`, so the plateau is not produced by a bad divisor-counting estimate. Replication matters because it maps that diagonal increment into the physical repair coordinates, but the low-height survival mechanism is already local.

The second stress test is to use the critical line only. At `sigma=1/2`, (5) gives `O(x/sqrt(T))`, so grouping before absolute values **does** recover a power saving there. The obstruction is specifically the horizontal path needed to connect the original Perron line `c>1` to the shifted contour. Treating the critical-line packet alone therefore misses the place where the hard-cutoff remainder pays its cost.

The third stress test is to increase the cutoff past divisor depth. Equation (23) then restores the familiar `x^2/T` decay. FD-282 does not say grouped contours never help; it says the simple absolute treatment only starts receiving that power saving after `T` reaches `x`, already beyond the low-height regime in which the FD-278 population obstruction is informative.

The fourth stress test is cancellation along the horizontal edge. Equations (8)--(10) deliberately say nothing against it. For each physical coordinate the complex phase changes with `sigma`, and the upper and lower horizontal edges are conjugate for the real Mertens source. Integrating first and taking absolute values later may therefore be much smaller than `mathfrak H`. Such cancellation is exactly the additional information a successful low-height contour argument must now expose.

The fifth stress test is smoothing or a modified Perron formula. A smooth Mellin cutoff can replace the hard rectangular edge by a kernel with stronger frequency decay; a signed truncated-Perron identity can also preserve coefficient cancellation that the classical absolute formula loses. Those architectures are outside the theorem and remain live, but they must still be bridged back to the sharp consecutive Mertens blocks used by the physical repair.

## Prior-art and novelty audit

The idea of modifying Perron's formula to control **variations** of summatory functions rather than first estimating pointwise errors is not new. Olivier Ramaré, *Modified truncated Perron formulae*, Annales Mathématiques Blaise Pascal **23** (2016), 109--128, DOI `10.5802/ambp.356`, develops general formulae relating variations of summatory functions directly to truncated Perron integrals. D. S. Ramana and O. Ramaré, *Variant of the truncated Perron formula and primes in polynomial sets*, International Journal of Number Theory **16**(2) (2020), 309--323, DOI `10.1142/S1793042120500165`, explicitly replace the classical dependence on `|a_n|` by signed sums of the coefficients in their variant.

Those papers therefore delimit the novelty claim sharply: FD-282 does **not** claim that differencing before Perron estimation, signed Perron formulae, or smooth/modified truncations are new. A targeted search found no source coupling such a variation kernel to the specific Mathia operation

\[
\text{consecutive sampling at }Nq
\to
\text{divisor replication}
\to
\text{physical dyadic }\ell^1\text{ repair}
\to
\text{FD-261 capacity threshold},
\]

nor the prime self-divisor lower bound (8) used to diagnose the right-collar failure of the naive grouped hard contour. The proof of (3)--(16) is elementary apart from standard PNT/zeta estimates already within the line's classical background, and the Ramaré papers are contextual prior-art boundaries rather than load-bearing inputs. No new `SOURCES.md` dependency is required for the claim itself.

## Implications

FD-281 left two obvious ways to avoid its pointwise Perron tariff: keep the contour grouped with the physical repair kernel, or replace the hard pointwise formula by a signed/smoothed architecture. FD-282 separates them. **Grouping alone is insufficient if one then applies pointwise absolute values on the hard horizontal contour.** The critical-line part improves, but the right collar contains a prime self-divisor channel of size `x^(1-o(1))`, and at low spectral height this forces an `Nx`-scale absolute certificate up to logarithms.

The next useful target is therefore no longer merely "put the divisor kernel inside Perron." One must preserve cancellation one step further: integrate the horizontal kernel before taking the physical absolute value, combine the conjugate edges, use a signed variation formula of the Ramaré type, or introduce smoothing with a quantitatively controlled desmoothing bridge back to the sharp Mertens blocks. Any of those would be genuinely new information relative to FD-281; repeating the grouped contour with triangle inequality cannot cross the current capacity threshold at the live polynomial depths.

**Verdict.** The hard-cutoff repair-aware Perron route has a second, distinct absolute-value barrier. Pointwise Mertens errors lose too much before the physical transform (FD-281), while pointwise absolute values on the grouped horizontal contour lose too much **after** the transform (FD-282). A viable low-height remainder estimate must therefore retain signed contour cancellation beyond divisor grouping or alter the truncation architecture itself.