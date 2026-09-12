# PC-271 — mesoscopic torus resolution is a classical dual-lattice spectral test

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the growing-resonance and inverse-near-resonance escape left open by PC-270.

Fix distinct primes

\[
2<p<r<q,
\qquad
z_u=\left(\left\{\frac{up}{q}\right\},\left\{\frac{ur}{q}\right\}\right),
\qquad 0\le u<q.
\tag{1}
\]

PC-258 identified this rational torus orbit as the exact base coding of the shared-upper collision chain, PC-269 classicalized bounded-mode nonresonant bulk limits, and PC-270 classicalized every persistent fixed exact resonance. The remaining obvious Fourier escape is therefore to let the resonance vector itself grow, or to inspect windows short enough to resolve a near-resonance before the full `q`-orbit cancels it.

That escape has an exact classical resolution parameter. Define the annihilator/dual lattice

\[
\Lambda_{p,r;q}
:=\{(h,k)\in\mathbb Z^2:hp+kr\equiv0\pmod q\},
\tag{2}
\]

and its sup-norm systole

\[
\lambda_{p,r;q}
:=\min_{(h,k)\in\Lambda_{p,r;q}\setminus\{0\}}
\max(|h|,|k|).
\tag{3}
\]

Then `lambda` is exactly the first Fourier resolution at which the complete torus orbit can be distinguished from Haar measure. Bounded-mode nonresonance is equivalent to `lambda -> infinity`, but every finite level satisfies the sharp-scale geometry-of-numbers ceiling

\[
\boxed{\lambda_{p,r;q}\le \lfloor\sqrt q\rfloor.}
\tag{4}
\]

For shorter orbit windows, define

\[
\Delta_B(p,r;q)
:=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}.
\tag{5}
\]

A two-dimensional pigeonhole argument gives the universal Dirichlet bound

\[
\boxed{\Delta_B(p,r;q)\le\frac1{(B+1)^2}.}
\tag{6}
\]

Thus the first growing-resonance / near-resonance obstruction is not a new prime-circle spectral object: it is precisely the classical dual-lattice/spectral-test and Diophantine-approximation data of a rank-one lattice orbit. What remains potentially source-sensitive is not the existence of such mesoscopic resonances, but the arithmetic statistics of the dual lattice or of `Delta_B` along the prime source, after matched non-prime rational-rotation controls.

## 1. The full orbit is exactly a rank-one lattice rule

For a Fourier character

\[
e_{h,k}(x,y)=e^{2\pi i(hx+ky)},
\]

the exact finite geometric sum is

\[
\frac1q\sum_{u=0}^{q-1}e_{h,k}(z_u)
=
\frac1q\sum_{u=0}^{q-1}
\exp\!\left(\frac{2\pi i u(hp+kr)}q\right)
=
\begin{cases}
1,&(h,k)\in\Lambda_{p,r;q},\\
0,&(h,k)\notin\Lambda_{p,r;q}.
\end{cases}
\tag{7}
\]

This is PC-258's character calculation, now read at growing Fourier frequency. It immediately gives the exact resolution statement.

Let

\[
T(x,y)=\sum_{(h,k)\in S}\widehat T(h,k)e_{h,k}(x,y)
\tag{8}
\]

be any trigonometric polynomial whose nonzero Fourier support satisfies

\[
\max(|h|,|k|)<\lambda_{p,r;q}.
\tag{9}
\]

Then no nonzero frequency in `S` belongs to the dual lattice, so

\[
\boxed{
\frac1q\sum_{u=0}^{q-1}T(z_u)
=
\int_{\mathbb T^2}T\,dm.
}
\tag{10}
\]

Conversely, choose a shortest nonzero `(h_*,k_*)` in (3). The single real mode

\[
T_*(x,y)=\cos 2\pi(h_*x+k_*y)
\tag{11}
\]

has Haar average zero but orbit average one. Therefore `lambda` is not merely a sufficient cutoff: it is the **exact first Fourier detection scale** of the finite lift.

For any continuous function with absolutely summable Fourier coefficients one also has the exact error identity

\[
\boxed{
\frac1q\sum_{u=0}^{q-1}f(z_u)-\int_{\mathbb T^2}f\,dm
=
\sum_{m\in\Lambda_{p,r;q}\setminus\{0\}}\widehat f(m).
}
\tag{12}
\]

In particular, for `s>1` and `f in H^s(T^2)`, Cauchy--Schwarz and the two-dimensional Fourier tail give

\[
\left|
\frac1q\sum_{u=0}^{q-1}f(z_u)-\int f\,dm
\right|
\le C_s\lambda_{p,r;q}^{\,1-s}\|f\|_{H^s}.
\tag{13}
\]

So the natural quantitative parameter for smooth full-orbit observables is the dual-lattice systole, not primality by itself.

## 2. PC-269 nonresonance is exactly `lambda -> infinity`

Consider a sequence `(p_n,r_n,q_n)` with `q_n -> infinity`. PC-269 assumes bounded-mode nonresonance: for every fixed nonzero `(h,k)`,

\[
q_n\nmid hp_n+kr_n
\tag{14}
\]

for all sufficiently large `n`.

This condition is equivalent to

\[
\boxed{\lambda_{p_n,r_n;q_n}\longrightarrow\infty.}
\tag{15}
\]

Indeed, (15) plainly implies (14). Conversely, if `lambda_n` failed to tend to infinity, some bound `B` would contain a nonzero resonant vector for infinitely many `n`. There are only finitely many integer vectors in the sup-norm box of radius `B`, so one of them would recur infinitely often, contradicting (14).

Thus the PC-269/PC-270 bounded-frequency dichotomy has a simple geometric reformulation:

- fixed exact resonances correspond to a bounded dual-lattice systole;
- bounded-mode nonresonance corresponds exactly to the systole escaping to infinity.

The unresolved growing-resonance sector is therefore the geometry of a moving index-`q` lattice, not a new kind of Fourier object.

## 3. The first exact growing resonance occurs by square-root frequency

Because `p` is invertible modulo the prime `q`, the homomorphism

\[
\mathbb Z^2\longrightarrow\mathbb Z/q\mathbb Z,
\qquad
(h,k)\longmapsto hp+kr\pmod q
\tag{16}
\]

is surjective. Hence `Lambda_{p,r;q}` has index and covolume exactly `q`.

Put

\[
H=\lfloor\sqrt q\rfloor.
\tag{17}
\]

Since a prime `q` is not a square,

\[
(H+1)^2>q.
\tag{18}
\]

Map the `(H+1)^2` pairs `(a,b)` with `0<=a,b<=H` to the `q` residues

\[
ap+br\pmod q.
\tag{19}
\]

Two distinct pairs have the same residue. Their difference `(h,k)` is nonzero, belongs to `Lambda_{p,r;q}`, and satisfies

\[
|h|,|k|\le H.
\tag{20}
\]

This proves (4).

The scale cannot be improved to `o(sqrt(q))` as a uniform lattice theorem. Already the source-level example

\[
(p,r,q)=(7,11,13)
\]

has

\[
-7+3\cdot11=2\cdot13,
\]
so `lambda<=3=floor(sqrt(13))`; direct inspection of `|h|,|k|<=2` in `7h+11k=0 mod 13` shows there is no shorter nonzero relation. Thus the square-root ceiling is attained even inside the all-prime source class.

This is the two-dimensional Minkowski/Dirichlet scale for an index-`q` lattice. In quasi-Monte Carlo terminology, the same shortest dual vector is the basic spectral-test resolution of a rank-one lattice point set.

## 4. Partial windows reduce exactly to inverse near-resonance time

Full-orbit cancellation can hide information that a shorter collision-chain window still sees. For one mode write

\[
\theta_{h,k}
:=\frac{hp+kr}{q}\pmod1
\tag{21}
\]

and average only the first `M` raw cells:

\[
A_M(h,k)
:=\frac1M\sum_{u=0}^{M-1}e^{2\pi i u\theta_{h,k}}.
\tag{22}
\]

The geometric-series identity gives

\[
\boxed{
|A_M(h,k)|
=
\frac{|\sin(\pi M\theta_{h,k})|}
{M|\sin(\pi\theta_{h,k})|}.
}
\tag{23}
\]

For a nonresonant mode,

\[
|A_M(h,k)|
\le
\min\!\left(1,
\frac1{2M\|\theta_{h,k}\|_{\mathbb R/\mathbb Z}}
\right).
\tag{24}
\]

Conversely, if

\[
\|\theta_{h,k}\|_{\mathbb R/\mathbb Z}\le\frac1{2M},
\tag{25}
\]

then the elementary sine bounds on `[0,pi/2]` give

\[
\boxed{|A_M(h,k)|\ge\frac2\pi.}
\tag{26}
\]

Therefore the exact quantity controlling a bandwidth-`B`, length-`M` mesoscopic probe is `M Delta_B`. A near resonance with `M Delta_B=O(1)` stays coherently visible; if all relevant phases satisfy `M||theta|| -> infinity`, the corresponding Fourier modes cancel.

The near-resonance scale itself has a universal two-dimensional Dirichlet bound. Consider the `(B+1)^2` phases

\[
\left\{\frac{ap+br}{q}\right\},
\qquad 0\le a,b\le B.
\tag{27}
\]

If two coincide, `Delta_B=0`. Otherwise, ordering these points around the circle produces two whose cyclic distance is at most `1/(B+1)^2`; subtracting their indices gives a nonzero vector of sup norm at most `B`. Hence (6).

Combining (6) and (26), whenever

\[
M\le\frac{(B+1)^2}{2},
\tag{28}
\]

there exists a Fourier mode of bandwidth at most `B` whose `M`-cell average has magnitude at least `2/pi` (or equals one in the exactly resonant case). Thus **uniform mixing over all modes of bandwidth `B` cannot cross the parabolic scale `B asymp sqrt(M)` without extra Diophantine input**. This is a generic rank-one-rotation fact, not a prime signature.

## 5. Matched controls and what remains source-sensitive

Nothing in Sections 1, 3, or 4 uses primality except to guarantee the convenient source ordering and invertibility modulo `q`; the same statements hold for any admissible rational rotation with the corresponding coprimality. In particular, matched non-prime rational-partition controls inherit the same dual-lattice exactness, the same `sqrt(q)` exact-resonance ceiling, and the same `1/B^2` near-resonance ceiling.

This rules out the following candidate mechanism by itself:

\[
\text{growing Fourier resonance or slow mesoscopic phase}
\longrightarrow
\text{prime-specific spectral signal}
\longrightarrow
\text{new RH mechanism}.
\tag{29}
\]

The **presence** and natural scales of those effects are universal. A source-sensitive continuation would have to prove something genuinely arithmetic about their distribution along prime triples, for example the statistics of

\[
\lambda_{p,r;q},
\qquad
\Delta_B(p,r;q),
\tag{30}
\]

the directions of shortest/near-shortest resonance vectors, or the way those vectors couple to a source-forced nonlocal transfer observable. Such a claim must then survive matched coprime/composite controls and the established theory of modular lattices, Diophantine approximation, discrepancy, and continued fractions.

This result does **not** classicalize Lyapunov exponents, singular log-determinants, microscopic eigenvalue spacings, shrinking collision windows with source-dependent geometry, or cross-level operators. Nor does it assert a typical size for `lambda` or `Delta_B` along the primes. It identifies the exact classical carrier that any such proposal must beat.

## 6. Prior-art and novelty audit

The abstract mathematics is standard in several equivalent languages.

I. H. Sloan and S. Joe, *Lattice Methods for Multiple Integration* (Oxford University Press, 1994, DOI `10.1093/oso/9780198534723.001.0001`) develops rank-one lattice rules and their dual-lattice Fourier exactness. Harald Niederreiter, *Random Number Generation and Quasi-Monte Carlo Methods* (SIAM/CBMS, Chapter 5, DOI `10.1137/1.9781611970081`) places the same mechanism in lattice quadrature and pseudorandom/spectral testing. J. W. S. Cassels, *An Introduction to the Geometry of Numbers* (Springer Classics reprint, DOI `10.1007/978-3-642-62035-5`) is a standard geometry-of-numbers reference for Minkowski/Dirichlet shortest-vector bounds. Friedrich Pillichshammer and Mathias Sonnleitner, **A note on isotropic discrepancy and spectral test of lattice point sets**, *Journal of Complexity* 58 (2020), 101441, DOI `10.1016/j.jco.2019.101441`, explicitly relate discrepancy of lattice point sets to the spectral test/shortest dual-vector scale.

A targeted search against rank-one lattice rules, dual lattices, the spectral test, geometry-of-numbers shortest-vector bounds, and Diophantine control of rational rotations found the same mechanisms. No novelty is claimed for (7), the dual lattice, the `sqrt(q)` bound, the geometric-series window estimate, or the `1/B^2` Dirichlet scale.

The durable project-local contribution is the identification of the **specific escape left by PC-270** with this classical package: growing exact resonances are precisely short vectors in the dual lattice, and inverse near-resonance drift is precisely the finite-window Diophantine resolution of the same rational torus orbit. This gives an exact resolution boundary between the already classical fixed-complexity IDS sector and any genuinely new fine-scale Prime-Circle proposal.

## 7. Falsification and audit tests

The result is exact and has direct checks.

1. Produce a trigonometric polynomial supported strictly below `lambda_{p,r;q}` whose complete `q`-orbit average differs from Haar; this would contradict (7)--(10).
2. Produce a bounded-mode nonresonant sequence for which `lambda_n` does not tend to infinity, or conversely; finiteness of every bounded integer box rules either out.
3. Produce a prime `q` and source pair `(p,r)` for which every nonzero dual vector has sup norm greater than `floor(sqrt(q))`; the pigeonhole proof of (4) rules this out.
4. Produce `B` for which `Delta_B>1/(B+1)^2`; the cyclic-spacing argument from (27) rules this out.
5. Produce a mode obeying (25) but `|A_M|<2/pi`; the exact sine quotient (23) rules this out.
6. Produce an admissible non-prime rational-rotation control for which any of the arguments in Sections 1, 3, or 4 fails solely because the conductors are composite; no primality input is used there.

The finding is therefore a **classicalization/boundary result**, not an RH advance. It removes the mere existence of growing or near resonances as a novelty claim while isolating their source-dependent statistics and coupling to nonlocal observables as the remaining potentially meaningful questions.