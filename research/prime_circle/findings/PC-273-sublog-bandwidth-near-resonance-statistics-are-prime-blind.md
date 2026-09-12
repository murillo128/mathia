# PC-273 — sublog-bandwidth near-resonance statistics are prime-blind

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the ordered mesoscopic `Delta_B` source-statistics branch left open by PC-271/PC-272.

PC-272 proves that the exact dual lattice loses the common multiplicative placement of the prime pair, while the finite-window quantity

\[
\Delta_B(p,r;q)
=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}
\]

retains it: two admissible prime pairs can have the same quotient `pr^{-1} mod q` but different `Delta_B`. That finite-level information gain is real. However, it does not give an asymptotic prime discriminator at fixed or sufficiently slowly growing Fourier bandwidth.

For prime `q`, let

\[
P_q=\{p:2<p<q,\ p\text{ prime}\},\qquad M_q=|P_q|,
\]

and define the prime-source `Delta_B` law on unordered distinct pairs

\[
\rho^{\mathrm{prime}}_{q,B}
:=
\frac{2}{M_q(M_q-1)}
\sum_{p<r\atop p,r\in P_q}
\delta_{\Delta_B(p,r;q)}.
\tag{1}
\]

As a matched non-prime rational-torus control, use all distinct nonzero residues below the same prime upper level,

\[
\rho^{\mathrm{grid}}_{q,B}
:=
\frac{2}{(q-1)(q-2)}
\sum_{1\le a<b\le q-1}
\delta_{D_B(a/q,b/q)},
\tag{2}
\]

where

\[
D_B(x,y)
:=
\min_{0<\max(|h|,|k|)\le B}
\|hx+ky\|_{\mathbb R/\mathbb Z}.
\tag{3}
\]

The identity

\[
\boxed{\Delta_B(p,r;q)=D_B(p/q,r/q)}
\tag{4}
\]

is exact. Moreover, with `W_1` the Wasserstein distance on `[0,1/2]`, the prime number theorem gives the quantitative matched-control bound

\[
\boxed{
W_1\!\left(\rho^{\mathrm{prime}}_{q,B},
           \rho^{\mathrm{grid}}_{q,B}\right)
\ll \frac{B}{\log q}+\frac{\log q}{q}.
}
\tag{5}
\]

Consequently, for every bandwidth sequence

\[
B(q)=o(\log q),
\tag{6}
\]

the entire `Delta_B` distribution on prime source pairs becomes asymptotically indistinguishable from the non-prime residue-grid control:

\[
\boxed{
W_1\!\left(\rho^{\mathrm{prime}}_{q,B(q)},
           \rho^{\mathrm{grid}}_{q,B(q)}\right)\to0.
}
\tag{7}
\]

In particular, for fixed `B` both converge to the same continuum law `(D_B)_*(dx\,dy)` on the unit square. Thus the pointwise ordered-information witness of PC-272 survives at finite level, but its uncentered source distribution is asymptotically prime-blind throughout the sublogarithmic Fourier window. Any surviving arithmetic mechanism must use finer source fluctuations, bandwidth at least comparable with the scale unresolved by this argument, or additional source-forced structure not contained in the raw `Delta_B` distribution.

## 1. The prime source becomes a uniform one-dimensional measure

Let

\[
\nu_q
:=
\frac1{M_q}\sum_{p\in P_q}\delta_{p/q}
\tag{8}
\]

on `[0,1]`, and let `m` denote Lebesgue probability measure. Its distribution function is, up to the omitted prime `2`,

\[
F_q(t)=\frac{\pi(qt)}{\pi(q)}+O\!\left(\frac1{M_q}\right).
\tag{9}
\]

The prime number theorem implies not only `F_q(t)->t` for each fixed `t`, but the uniform estimate

\[
\boxed{
\sup_{0\le t\le1}|F_q(t)-t|\ll\frac1{\log q}.
}
\tag{10}
\]

A short derivation uses the standard PNT expansion

\[
\pi(x)=\frac{x}{\log x}+O\!\left(\frac{x}{\log^2x}\right).
\tag{11}
\]

If `t<=1/log q`, then both `t` and `pi(qt)/pi(q)` are `O(1/log q)` by the standard upper bound `pi(x)\ll x/log x`. If `t>=1/log q`, put `L=log q`; uniformly in this range,

\[
\frac{\pi(qt)}{\pi(q)}
=
t\frac{L}{L+\log t}
+O\!\left(\frac{t}{L}\right).
\tag{12}
\]

Since `t|log t|<=e^{-1}` and `L+log t>=L-log L`, the difference between the main term in (12) and `t` is `O(1/L)`. This proves (10). Omitting `2` changes the distribution function by only `O(1/M_q)=O(log q/q)`.

On the real line, Wasserstein distance has the CDF representation

\[
W_1(\nu_q,m)=\int_0^1|F_q(t)-t|\,dt,
\tag{13}
\]

hence

\[
\boxed{W_1(\nu_q,m)\ll\frac1{\log q}.}
\tag{14}
\]

For the nonzero residue grid

\[
\eta_q:=\frac1{q-1}\sum_{a=1}^{q-1}\delta_{a/q},
\tag{15}
\]

one has `W_1(eta_q,m)=O(1/q)`. Therefore

\[
\boxed{W_1(\nu_q,\eta_q)\ll\frac1{\log q}.}
\tag{16}
\]

This is the only arithmetic input needed below.

## 2. `Delta_B` is only `B`-Lipschitz in the source coordinates

For every integer vector `(h,k)` in the defining box,

\[
(x,y)\mapsto\|hx+ky\|_{\mathbb R/\mathbb Z}
\]

is `B`-Lipschitz for the `l^1` metric on `[0,1]^2`, because `|h|,|k|<=B`. A finite minimum preserves the same Lipschitz bound, so

\[
\boxed{
|D_B(x,y)-D_B(x',y')|
\le
B\bigl(|x-x'|+|y-y'|\bigr).
}
\tag{17}
\]

Couple two independent copies of an optimal one-dimensional coupling between `nu_q` and `eta_q`. With the `l^1` transportation cost this gives

\[
W_1(\nu_q\otimes\nu_q,\eta_q\otimes\eta_q)
\le2W_1(\nu_q,\eta_q)
\ll\frac1{\log q}.
\tag{18}
\]

Wasserstein distance contracts under a Lipschitz map. Pushing (18) through `D_B` and using (17) yields

\[
W_1\!\left((D_B)_*(\nu_q^{\otimes2}),
           (D_B)_*(\eta_q^{\otimes2})\right)
\ll\frac{B}{\log q}.
\tag{19}
\]

The function `D_B` is symmetric in its two coordinates because the vector box is invariant under `(h,k)<->(k,h)`. Passing from ordered product pairs to distinct unordered pairs therefore changes either pushforward by at most the diagonal mass. The prime diagonal has mass `1/M_q=O(log q/q)` and the grid diagonal has mass `1/(q-1)`. Since `D_B` takes values in `[0,1/2]`, these corrections contribute `O(log q/q)`. Equation (5) follows.

## 3. Fixed bandwidth has a universal continuum law

For fixed `B`, the map `D_B` is continuous. The PNT statement `nu_q => m` and ordinary grid convergence `eta_q => m` therefore give

\[
\rho^{\mathrm{prime}}_{q,B}
\Longrightarrow
(D_B)_*(m\otimes m)
\Longleftarrow
\rho^{\mathrm{grid}}_{q,B}.
\tag{20}
\]

No primality remains in the limiting law. This is stronger than saying that a generic Dirichlet bound also holds for non-prime controls: it identifies the **complete source distribution** of the surviving PC-272 ordered observable at every fixed Fourier resolution.

The quantitative estimate (5) extends the same conclusion to moving bandwidths `B=o(log q)`. It does not require character sums, prime-pair conjectures, GRH, or a spectral ansatz. The source pairs are sampled from the Cartesian square of the one-dimensional prime set, so at this resolution the only source input is the one-point empirical measure `nu_q`; PNT already makes that measure indistinguishable from its non-arithmetic continuum control at the precision seen by a `B`-Lipschitz probe.

## 4. Relation to PC-271 and PC-272

PC-271 shows that `Delta_B` controls inverse near-resonance time for partial orbit windows and that the existence/scale of near resonances is universal rank-one-lattice geometry. PC-272 then shows that `Delta_B` retains information lost by the multiplicative ratio quotient. Equation (5) supplies the missing source-statistics test between those two statements.

The finite witness

\[
\Delta_1(3,5;13)\ne\Delta_1(7,3;13)
\]

remains correct. It proves that `Delta_B` is not a function of `pr^{-1} mod q`. What (5) proves is different: when all prime source pairs are viewed at fixed or sublogarithmic bandwidth, that extra placement information has the same asymptotic distribution as for all nonzero residue pairs. Information gain relative to the ratio quotient therefore does not by itself imply an asymptotic arithmetic discriminator.

This closes the route

\[
\text{ordered prime placement}
\to
\text{raw }\Delta_B\text{ distribution at }B=o(\log q)
\to
\text{prime-specific asymptotic spectral signal}.
\tag{21}
\]

It does **not** close the intermediate/growing-resolution regime `B` comparable to or larger than `log q` but below the exact-resonance scale `sqrt(q)`, nor centered fluctuations of the prime empirical measure, singular observables whose effective Lipschitz constant grows faster than `B`, conditioned source subfamilies, or couplings of the near-resonance vector to an additional nonlocal transfer operator.

## 5. Prior-art and novelty audit

Every external ingredient is classical.

H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press (2006), Chapter 6, is a standard reference for the prime number theorem and its quantitative forms. The deduction `pi(qt)/pi(q)->t`, and the uniform `O(1/log q)` estimate used here, are immediate scaled consequences of the classical PNT expansion rather than a new theorem about primes.

Patrick Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley (1999), gives the standard weak-convergence/continuous-mapping framework. The Wasserstein contraction used in (18)--(19) is the elementary coupling form of the same general stability principle. PC-271 already records the classical rank-one-lattice/spectral-test literature (Sloan--Joe, Niederreiter, Cassels, Pillichshammer--Sonnleitner) for the geometric carrier itself.

A targeted literature search against normalized prime empirical measures, rank-one lattice spectral tests, and near-resonance distributions found no need for a new external theorem: the argument is exactly PNT plus a Lipschitz pushforward estimate. **No novelty is claimed for PNT, weak convergence, Wasserstein contraction, or the rank-one-lattice carrier.** The project-local contribution is the quantitative application to the precise ordered-time escape left open by PC-272: the extra finite-level information in `Delta_B` is provably washed out against a matched non-prime control throughout `B=o(log q)`.

## 6. Audit and falsification tests

The claim has several direct failure tests.

1. Find a sequence of prime upper levels `q` for which the scaled prime empirical CDF differs from the uniform CDF by more than `C/log q` for every fixed `C`; this would contradict the standard PNT expansion used in (10).
2. Find two source points for which (17) fails; the circle-distance function and the finite minimum make this impossible under the stated `l^1` metric.
3. For a sequence `B=o(log q)`, exhibit a 1-Lipschitz test function on `[0,1/2]` whose prime-pair and residue-grid expectations stay a fixed distance apart. This would contradict (5) by the Kantorovich dual characterization of `W_1`.
4. Keep `B` comparable to `log q` or larger. The present estimate then no longer forces the two source laws together; such a discrepancy would be outside rather than contrary to the claim.
5. Center or magnify `Delta_B` at a scale comparable with the prime empirical discrepancy. The resulting observable can amplify PNT error terms and is likewise outside the uncentered statement.

## 7. Consequences for the research line

The PC-272 ordered-time branch remains open, but its first asymptotic regime is now classified. Fixed Fourier resolution, and more generally `B=o(log q)`, cannot turn the raw `Delta_B` source law into a prime-specific Prime-Circle mechanism: the matched all-residue rational-torus control has the same asymptotic law.

Accordingly, a continuation must pay for genuinely finer information. The mathematically live regimes are growing resolution beyond this PNT-stability window, centered/subleading source fluctuations, singular observables, or an additional source-forced coupling that is not merely a Lipschitz function of `(p/q,r/q)`. Any RH relevance appearing only through the rate at which `nu_q` approaches its smooth limit must also be separated from the already-classical prime-counting/explicit-formula channel rather than counted as a new geometric bridge.