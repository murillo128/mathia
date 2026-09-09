# PC-231 — fixed-base Cauchy-packet bilinearities close in rational-shift algebra

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY` for the first canonical nonlinear operations on the fully mode-resolved fixed-base packet state left open by PC-227 and still outside the scalar/operator compressions of PC-229--PC-230. At fixed coarse conductor `N`, the shifted Cauchy packets produced by a fresh prime are closed, in a strong finite-state sense, under the two Fourier-dual bilinear operations intrinsic to the cyclic label space: pointwise multiplication and discrete convolution. Pointwise products produce only confluent Cauchy poles at the same rational shifts; the bilateral convolution of two simple packets produces exactly one packet whose shift is the sum modulo `1`, except for the complementary-shift resonance, where it collapses to a single lattice delta.

Consequently, applying either canonical bilinear operation to the PC-227 packet state before any scalar positive-square compression does **not** create a new expanding fixed-base spectral coordinate. The possible shifts remain in the finite subgroup `(1/N) Z / Z`; all new singularity types are ordinary finite pole confluence or a resonant delta. This closes a natural first nonlinear escape at fixed base, but it does not classify operation depth growing with the conductor, simultaneous squarefree-radical growth, genuinely non-translation-invariant packet operators, several noncommuting source-forced operators, or the global uniformization/accessory sector.

## 1. The PC-227 limiting state has rational shifted-Cauchy coordinates

PC-227 proves that, for fixed `N` and fresh primes `q -> infinity` in one residue class modulo `N`, every nonzero local mode packet is a scalar multiple of

\[
f_\sigma(j):=\frac{1}{j+\sigma},
\qquad j\in\mathbb Z,
\qquad
\sigma\in\left\{\frac1N,\ldots,\frac{N-1}{N}\right\}.
\tag{1}
\]

There are only finitely many packet centers and amplitudes at fixed `N`; the growing `q` coordinate has been converted into the bilateral lattice coordinate `j`. PC-227 also proves `ell^2` convergence of each identified finite-`q` column to a finite direct sum of such packets. Thus the first nonlinear question is not whether one can invent another scalar of the packet, but whether the canonical algebra operations on the underlying cyclic/Fourier coordinates generate a new kind of state before scalarization.

With normalized Fourier coefficients, physical pointwise multiplication corresponds to cyclic convolution of Fourier coefficients,

\[
(\widehat f *_q \widehat g)(k)
:=\sum_{\ell\bmod q}\widehat f(\ell)\widehat g(k-\ell),
\tag{2}
\]

while physical convolution corresponds to Fourier pointwise multiplication. No shell-dependent coefficient or external kernel is chosen in either operation.

## 2. Pointwise multiplication gives only finite Cauchy confluence

For two distinct packet shifts,

\[
\boxed{
 f_\sigma(j)f_\tau(j)
 =\frac{f_\sigma(j)-f_\tau(j)}{\tau-\sigma}
}
\qquad(\sigma\ne\tau).
\tag{3}
\]

If the shifts coincide, one obtains only the double pole

\[
\boxed{
f_\sigma(j)^2=\frac1{(j+\sigma)^2}.
}
\tag{4}
\]

More generally, ordinary confluent partial fractions imply that every fixed finite pointwise product of packets is a finite linear combination of

\[
\boxed{
 f_{\sigma,m}(j):=\frac1{(j+\sigma)^m},
 \qquad m\ge1,
}
\tag{5}
\]

at the finitely many shifts already present in the factors. Equivalently,

\[
f_{\sigma,m}
=\frac{(-1)^{m-1}}{(m-1)!}
\partial_\sigma^{m-1}f_\sigma.
\tag{6}
\]

Thus pointwise nonlinearity can raise finite pole order but cannot create a new shift parameter, new conductor scale, or expanding packet multiplicity at fixed `N`.

The passage from the finite fresh-prime vectors to this limit is stable. If `x_q -> x` and `y_q -> y` in the PC-227 packet identification in `ell^2`, then

\[
\|x_qy_q-xy\|_1
\le
\|x_q-x\|_2\|y_q\|_2
+\|x\|_2\|y_q-y\|_2
\longrightarrow0.
\tag{7}
\]

Hence this is not merely formal multiplication of asymptotic profiles: the finite pointwise products converge to the confluent packet product.

## 3. Bilateral convolution of two simple packets is exactly one packet

For `sigma,tau in (0,1)` define

\[
(f_\sigma*f_\tau)(n)
:=
\sum_{k\in\mathbb Z}
\frac1{(k+\sigma)(n-k+\tau)}.
\tag{8}
\]

For each fixed `n` the series is absolutely convergent, since its summand is `O(k^{-2})`. Put

\[
D=n+\sigma+\tau.
\]

When `D != 0`, the exact partial fraction identity

\[
\frac1{(k+\sigma)(n-k+\tau)}
=
\frac1D
\left(
\frac1{k+\sigma}
+
\frac1{n-k+\tau}
\right)
\tag{9}
\]

combined with the classical Mittag--Leffler principal-value formula

\[
\operatorname{PV}\sum_{k\in\mathbb Z}\frac1{k+\sigma}
=\pi\cot(\pi\sigma)
\tag{10}
\]

gives

\[
\boxed{
(f_\sigma*f_\tau)(n)
=
\frac{\pi\bigl(\cot(\pi\sigma)+\cot(\pi\tau)\bigr)}
{n+\sigma+\tau}
}
\qquad(D\ne0).
\tag{11}
\]

Equivalently,

\[
\boxed{
(f_\sigma*f_\tau)(n)
=
\frac{\pi\sin\pi(\sigma+\tau)}
{\sin(\pi\sigma)\sin(\pi\tau)}
\frac1{n+\sigma+\tau}.
}
\tag{12}
\]

If `sigma+tau<1`, this is a scalar multiple of `f_{sigma+tau}`. If `sigma+tau>1`, it is an integer translate of `f_{sigma+tau-1}`. Since every PC-227 shift is in `(1/N)Z/Z`, convolution therefore keeps the shift in the same finite subgroup.

The use of principal values in (10) is only an evaluation device: the combined series (8) is absolutely convergent, so (11) has no summation-order ambiguity.

## 4. Complementary shifts collapse more strongly to a delta

The only resonance is

\[
\sigma+\tau=1,
\qquad n=-1.
\]

For every `n != -1`, equation (11) applies and its numerator vanishes because

\[
\cot(\pi(1-\sigma))=-\cot(\pi\sigma).
\]

At `n=-1`, the two denominators coincide up to sign:

\[
\frac1{(k+\sigma)(-1-k+1-\sigma)}
=-\frac1{(k+\sigma)^2}.
\]

The differentiated cotangent identity therefore gives

\[
\boxed{
 f_\sigma*f_{1-\sigma}
 =-\pi^2\csc^2(\pi\sigma)\,\delta_{-1}.
}
\tag{13}
\]

This is a stronger collapse than ordinary shift closure. The convolution of two infinite `1/j` tails can lose the entire tail and leave one lattice site.

The PC-227 control `N=6`, whose displayed packet has `sigma=1/2`, is maximally resonant:

\[
\boxed{
 f_{1/2}*f_{1/2}=-\pi^2\delta_{-1}.
}
\tag{14}
\]

As a nonresonant control,

\[
\boxed{
 f_{1/3}*f_{1/3}
 =\frac{2\pi}{\sqrt3}f_{2/3}.
}
\tag{15}
\]

Both behaviors are universal shifted-Cauchy identities; neither depends on primality.

## 5. The finite cyclic operation has the same local limit

The convolution identity is relevant to an operation performed **before** taking the fixed-base packet limit, not only to an abstract operation introduced afterwards. The local packet coordinate is itself an affine coordinate on the fresh cyclic fiber. In the notation of PC-227, a packet around the primitive root `alpha_t=zeta_N^t` has

\[
z_{t,j}^{(q)}
=\alpha_t\exp\!\left(\frac{2\pi i}{q}(j+\sigma)\right),
\qquad
\sigma=\frac{s}{N},
\tag{16}
\]

while `z=zeta_{Nq}^{qu-k}`. Equating exponents gives the exact congruence

\[
\boxed{
k_{t,j}^{(q)}
\equiv
q(u-t)-Nj-s
\pmod{Nq}.
}
\tag{17}
\]

Thus within every packet sector, `j` is an affine coordinate on the `q`-fiber, with slope `-N`, a unit modulo the fresh prime `q`. If two packet sectors with integer shift numerators `s_1,s_2` are combined by cyclic convolution, their Fourier labels add as

\[
k_1+k_2
\equiv
q(u_1-t_1+u_2-t_2)
-N(j_1+j_2)
-(s_1+s_2)
\pmod{Nq}.
\tag{18}
\]

Writing

\[
s_1+s_2=s_0+cN,
\qquad 0\le s_0<N,
\tag{19}
\]

shows at finite `q` that the output packet coordinate is `j_1+j_2+c` and its fractional shift is exactly `s_0/N`. This is the finite cyclic origin of the shift-addition law modulo `1` in (11)--(13); no asymptotic coordinate choice inserts it by hand.

PC-227 supplies `ell^2` convergence of the packet-identified finite vectors. For a fixed output offset `n`, the cyclic convolution coefficient on a fixed pair of sectors is an `ell^2` pairing of one packet vector with a fixed translated/reflected copy of the other. After embedding the centered cyclic coordinate into `Z`, fixed translations converge to bilateral translations; the wrap-around discrepancy lies in the `ell^2` tails, whose norm tends to zero. Therefore Cauchy--Schwarz gives

\[
\boxed{
(x_q *_q y_q)(n)
\longrightarrow
(x*y)(n)
}
\tag{20}
\]

for every fixed local output coordinate. Since a PC-227 column has only finitely many packet sectors at fixed `N`, bilinearity leaves only finitely many pairwise sums of their rational shifts. The finite fresh-prime cyclic product thus has no hidden local limit beyond (11)--(13).

Equation (20) is intentionally a fixed-local-coordinate statement. No claim is made here that arbitrary nonlinear operation depth is uniformly bounded in a simultaneously growing conductor regime.

## 6. Prior art and novelty boundary

The analytic engines are classical. The Mittag--Leffler partial-fraction expansion of `pi cot(pi z)` and its differentiated cosecant identity are standard; NIST DLMF, §4.22, records the classical trigonometric partial-fraction framework. Warren P. Johnson, *Trigonometric Identities à la Hermite*, American Mathematical Monthly 117 (2010), 311--327, gives a modern partial-fraction derivation and product-to-sum development of Hermite's cotangent identities; Johnson is already a Prime-Circle source anchor for PC-094. Ordinary Fourier duality between pointwise products and cyclic convolution is standard finite harmonic analysis.

A directed search around bilateral shifted-Cauchy convolution, discrete Hilbert kernels, cotangent convolution identities, and shifted reciprocal lattices did not locate a source making the exact PC-227 packet application above. That absence is **not** treated as a historical novelty claim. Equations (3), (9)--(13), and the finite-state shift closure are direct consequences of classical partial fractions and cotangent summation once PC-227 has supplied the source-forced packet state.

A matched non-cyclotomic control makes the universality explicit: any finite collection of abstract shifted Cauchy sequences with the same rational shifts obeys exactly the same product and convolution laws. Thus the bilinear algebra itself carries no prime-specific selector.

## 7. Consequence for the Prime-Circle frontier

At fixed coarse conductor, the route

\[
\boxed{
\text{PC-227 full Cauchy packet state}
\longrightarrow
\text{canonical pointwise product or cyclic convolution}
\longrightarrow
\text{new expanding nonlinear packet spectrum}
}
\]

is closed at the first bilinear level. The only outputs are finite confluent poles at rational shifts already living in `(1/N)Z/Z`, integer translates, and the complementary-shift delta resonance. No free complex spectral parameter, gamma factor, functional-equation symmetry, zeta zero divisor, or critical-line constraint is generated.

This does **not** close the live squarefree-radical direction. In particular, it leaves open simultaneous growth of `N` so that the rational-shift subgroup itself expands; nonlinear depth or network size growing with the conductor; an intrinsic non-translation-invariant packet operator whose coefficients are forced by old/new chord geometry; several noncommuting source-forced insertions retained jointly; operations on the complete PC-227 numerator/shift/normalization state that are not reducible to the packet bilinearities above; and the global uniformization/accessory-parameter sector. Those are the regimes in which a genuinely growing cross-prime relation would still have to appear.
