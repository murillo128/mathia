# FD-040 — nonsquarefree Jordan rows frame finite supercritical Mellin packets

**Status:** `EXACT-DERIVED + FINITE-MELLIN-PACKET + NONSQUAREFREE-JORDAN-FRAME + POSITIVE-OCCUPATION + HYPERBOLA-SAMPLING-BOUNDARY + PHYSICAL-SOURCE-CONDITIONAL`.

`FD-039` shows that the generic source properties used in `FD-037`--`FD-038` do not force a positive nonsquarefree occupation fraction. A fixed one-Lipschitz shell source with divergent critical square energy can build sparse triangular spikes so that, at selected horizons, essentially one fixed squarefree Jordan row carries all the energy. The next question is whether that escape is compatible with the Mellin-type oscillations naturally suggested by the physical coefficient series from `FD-033`.

For every **finite** packet at a fixed supercritical real exponent, it is not. Fix `D>=1`, `beta>1/2`, and distinct real frequencies

\[
\Gamma=\{\gamma_1,\ldots,\gamma_m\}.
\]

Put

\[
w(r):=\frac{J_2(r)}{r^2}.
\tag{1}
\]

For `z=(z_1,\ldots,z_m)\in\mathbb C^m`, define the Mellin sample

\[
A_z(r):=\sum_{j=1}^m z_j r^{-i\gamma_j}.
\tag{2}
\]

Then there is a constant

\[
\boxed{\kappa_{D,\beta,\Gamma}>0}
\tag{3}
\]

such that every coefficient vector satisfies

\[
\boxed{
\sum_{\substack{r>D\\\mu(r)=0}}
 w(r)r^{-2\beta}|A_z(r)|^2
\ge
\kappa_{D,\beta,\Gamma}
\sum_{r>D}w(r)r^{-2\beta}|A_z(r)|^2.
}
\tag{4}
\]

Thus the union of nonsquarefree Jordan rows is a coercive sampling frame on every finite Mellin-frequency span once `beta>1/2`. The statement is pointwise in the packet coefficients: phase cancellation can rotate with the horizon, but no nonzero finite packet can asymptotically hide from all nonsquarefree rows.

Consequently, suppose a real shell profile has a finite supercritical Mellin asymptotic

\[
F(n)
=n^\beta(\log(en))^q
\bigl(P(\log n)+o(1)\bigr),
\qquad \beta>\frac12,
\tag{5}
\]

where `q>=0` is fixed and

\[
P(t)=\sum_{j=1}^m a_j e^{i\gamma_j t}
\tag{6}
\]

is a nonzero real-valued finite exponential sum with distinct real frequencies. Define the exact Jordan-shell energies

\[
E^F_{H,D}
:=\sum_{D<r\le H}w(r)
 F(\lfloor H/r\rfloor)^2,
\tag{7}
\]

\[
U^F_{H,D}
:=\sum_{\substack{D<r\le H\\\mu(r)=0}}w(r)
 F(\lfloor H/r\rfloor)^2.
\tag{8}
\]

Then

\[
\boxed{
\liminf_{H\to\infty}
\frac{U^F_{H,D}}{E^F_{H,D}}
\ge \kappa_{D,\beta,\Gamma}>0.
}
\tag{9}
\]

This sharply separates the `FD-039` countermodel from a finite dominant Mellin packet. The triangular-spike escape is genuine for generic bounded-increment sources, but it cannot arise from finitely many fixed logarithmic frequencies at one exponent `beta>1/2`.

For the physical source this is a conditional boundary, not yet an occupation theorem. `FD-033` gives the exact Dirichlet series

\[
\sum_{n\ge1}\frac{\Delta\mathcal H(n)}{n^s}
=\frac{\zeta(s+1)}{\zeta(s)}.
\tag{10}
\]

Therefore an explicit-formula regime in which finitely many rightmost poles with common real part `beta>1/2` dominate `mathcal H` and leave a lower-order remainder would fall under (5), after keeping the maximal logarithmic multiplicity. In such a regime the physical ratio `U_(H,D)/E_(H,D)` cannot tend to zero. What remains open is precisely the genuinely infinite or non-separated spectral case: infinitely many comparable poles, no rightmost spectral gap, growing packet complexity, or another arithmetic mechanism capable of defeating every fixed finite-frame constant.

## 1. The finite nonsquarefree Mellin Gram matrix is positive definite

Because `2 beta>1` and `0<w(r)<=1`, the two Hermitian matrices

\[
G_{\mathrm{all}}(j,k)
:=\sum_{r>D}w(r)r^{-2\beta}
 r^{i(\gamma_j-\gamma_k)},
\tag{11}
\]

and

\[
G_{\mathrm{ns}}(j,k)
:=\sum_{\substack{r>D\\\mu(r)=0}}w(r)r^{-2\beta}
 r^{i(\gamma_j-\gamma_k)}
\tag{12}
\]

converge absolutely. Their quadratic forms are exactly

\[
z^*G_{\mathrm{all}}z
=\sum_{r>D}w(r)r^{-2\beta}|A_z(r)|^2,
\tag{13}
\]

\[
z^*G_{\mathrm{ns}}z
=\sum_{\substack{r>D\\\mu(r)=0}}
 w(r)r^{-2\beta}|A_z(r)|^2.
\tag{14}
\]

The key point is that `G_ns` is strictly positive definite. Suppose instead that

\[
z^*G_{\mathrm{ns}}z=0.
\tag{15}
\]

Every summand in (14) is nonnegative and every Jordan weight is positive, so

\[
A_z(r)=0
\tag{16}
\]

for every nonsquarefree `r>D`. In particular, all sufficiently large squares are admissible, hence

\[
0=A_z(n^2)
=\sum_{j=1}^m z_j e^{-2i\gamma_j\log n}
\tag{17}
\]

for every sufficiently large integer `n`.

Set

\[
h(x):=\sum_{j=1}^m z_j e^{-2i\gamma_jx}.
\tag{18}
\]

Then `h(log n)=0` for all large `n`, while

\[
\|h'\|_\infty
\le 2\sum_j|\gamma_jz_j|<\infty.
\tag{19}
\]

Given large `x`, choose an integer `n` nearest to `e^x`. Since

\[
|x-\log n|=O(e^{-x}),
\tag{20}
\]

(17)--(19) imply

\[
|h(x)|=O_z(e^{-x}).
\tag{21}
\]

Thus `h(x)->0` as `x->infinity`.

On the other hand, distinctness of the frequencies gives the elementary mean-square identity

\[
\frac1T\int_0^T|h(x)|^2\,dx
=\sum_{j=1}^m|z_j|^2+o(1).
\tag{22}
\]

Indeed every off-diagonal integral is `O(1/T)`. Equation (21) forces the left side of (22) to tend to zero, so all `z_j` vanish. Hence

\[
\boxed{G_{\mathrm{ns}}>0.}
\tag{23}
\]

Since

\[
G_{\mathrm{all}}-G_{\mathrm{ns}}\succeq0,
\tag{24}
\]

`G_all` is also positive definite. Finite-dimensional compactness now gives

\[
\kappa_{D,\beta,\Gamma}
:=\inf_{z\ne0}
\frac{z^*G_{\mathrm{ns}}z}
{z^*G_{\mathrm{all}}z}
=\lambda_{\min}\!\left(
G_{\mathrm{all}}^{-1/2}
G_{\mathrm{ns}}
G_{\mathrm{all}}^{-1/2}
\right)>0,
\tag{25}
\]

which proves (4).

The proof uses only the presence of all sufficiently large squares inside the nonsquarefree set. Positive ambient density is not needed. This is stronger than the block-density mechanism of `FD-038` for the finite-dimensional packet class: even a very sparse deterministic subsequence of nonsquarefree rows already determines every finite logarithmic-frequency vector.

## 2. Hyperbola sampling preserves the finite packet

We now prove (9). Write

\[
L(x):=(\log(ex))^q.
\tag{26}
\]

The asymptotic (5), together with boundedness of the finite exponential sum `P`, gives a global envelope after enlarging a constant:

\[
|F(n)|\le C n^\beta L(n)
\qquad(n\ge1).
\tag{27}
\]

For each fixed Jordan row `r`, as `H->infinity`,

\[
\frac{F(\lfloor H/r\rfloor)}
{H^\beta L(H)}
=
 r^{-\beta}
\bigl(P(\log H-\log r)+o(1)\bigr).
\tag{28}
\]

The floor changes the logarithm by `o(1)` for fixed `r`, and `L(floor(H/r))/L(H)->1`.

Moreover (27) supplies the summable domination

\[
\left|
\frac{F(\lfloor H/r\rfloor)}{H^\beta L(H)}
\right|
\ll r^{-\beta},
\tag{29}
\]

uniformly for `r<=H`. Because `2 beta>1`, the squares of the right side are summable over `r`. Dominated convergence in the exact energies therefore yields

\[
\frac{E^F_{H,D}}
{H^{2\beta}L(H)^2}
=
\sum_{r>D}w(r)r^{-2\beta}
 P(\log H-\log r)^2+o(1),
\tag{30}
\]

and

\[
\frac{U^F_{H,D}}
{H^{2\beta}L(H)^2}
=
\sum_{\substack{r>D\\\mu(r)=0}}w(r)r^{-2\beta}
 P(\log H-\log r)^2+o(1).
\tag{31}
\]

Because `P` is real-valued, its square is its modulus square. Set

\[
z_j(H):=a_j e^{i\gamma_j\log H}.
\tag{32}
\]

Then

\[
P(\log H-\log r)
=\sum_{j=1}^m z_j(H)r^{-i\gamma_j}
=A_{z(H)}(r),
\tag{33}
\]

so (30)--(31) become

\[
\frac{E^F_{H,D}}
{H^{2\beta}L(H)^2}
=z(H)^*G_{\mathrm{all}}z(H)+o(1),
\tag{34}
\]

\[
\frac{U^F_{H,D}}
{H^{2\beta}L(H)^2}
=z(H)^*G_{\mathrm{ns}}z(H)+o(1).
\tag{35}
\]

The coefficient norm is independent of `H`:

\[
\|z(H)\|_2=\|a\|_2>0.
\tag{36}
\]

Since `G_all` is positive definite, the denominator in (34) is bounded below uniformly in `H`. Applying (4) to `z(H)` and dividing (35) by (34) gives

\[
\frac{U^F_{H,D}}{E^F_{H,D}}
\ge \kappa_{D,\beta,\Gamma}+o(1),
\tag{37}
\]

which proves (9).

This step is where `beta>1/2` matters. Absolute summability of `r^{-2 beta}` makes the low fixed Jordan rows themselves a stable frame. At the critical value `beta=1/2`, the row sum is logarithmically divergent and the correct mechanism is instead the long-block weighted-density law developed in `FD-038`; (4) is not asserted there.

## 3. Pure-power audit

For a single zero frequency, `P` is constant and the frame constant is exactly the physical weighted nonsquarefree proportion for the convergent power tail:

\[
\boxed{
\kappa_{D,\beta,\{0\}}
=
\frac{
\sum_{\substack{r>D\\\mu(r)=0}}
 w(r)r^{-2\beta}
}{
\sum_{r>D}w(r)r^{-2\beta}
}>0.
}
\tag{38}
\]

For `D=0`, the full denominator has the Euler product identity

\[
\sum_{r\ge1}\frac{w(r)}{r^s}
=\frac{\zeta(s)}{\zeta(s+2)},
\qquad \Re s>1,
\tag{39}
\]

while the squarefree part is

\[
\sum_{\substack{r\ge1\\\mu(r)\ne0}}
\frac{w(r)}{r^s}
=
\prod_p\left(1+(1-p^{-2})p^{-s}\right).
\tag{40}
\]

Thus the nonsquarefree numerator in (38) is already strictly positive in the simplest one-mode model. The matrix argument proves that no finite collection of phases can cancel this positivity simultaneously across all nonsquarefree rows.

## 4. Consequence for the physical frontier

The physical coefficient law from `FD-033` is

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\qquad
\sum_{n\ge1}\frac{\Delta\mathcal H(n)}{n^s}
=\frac{\zeta(s+1)}{\zeta(s)}.
\tag{41}
\]

Hence nontrivial zeros of `zeta(s)` are the natural Mellin singularities of the physical shell source. If a finite family of poles at a common real part `beta>1/2` is isolated strongly enough that residue inversion gives

\[
\mathcal H(x)
=x^\beta(\log(ex))^q
\bigl(P(\log x)+o(1)\bigr)
\tag{42}
\]

with a nonzero finite packet `P`, then (9) applies directly and yields

\[
\liminf_{H\to\infty}
\frac{U_{H,D}}{E_{H,D}}>0.
\tag{43}
\]

Equation (42) is **not** proved here for the actual source, under RH or under failure of RH. In particular, failure of RH does not automatically provide a finite rightmost packet: the supremum of zero real parts need not be attained by a finite isolated family, and an explicit formula may have infinitely many comparable terms or no error small enough for (42). Those possibilities are exactly outside the theorem.

The durable restriction is therefore narrower but genuine. `FD-039` prevents the line from deducing occupation from one-Lipschitz regularity and critical-energy divergence alone; `FD-040` now prevents the opposite overreaction that arbitrary hyperbola amplification remains compatible with every spectral model. **Finite supercritical Mellin packets are coercive.** Any physical vanishing-occupation mechanism must exploit spectral complexity that escapes every fixed finite frequency span, or use a different arithmetic concentration mechanism not represented by (42).

## 5. Prior art, falsification boundary, and research consequence

Finite exponential sums, trigonometric polynomials, and almost-periodic uniqueness are classical subjects. A targeted audit of exponential-polynomial zero theory, almost-periodic functions, Mellin/Dirichlet-series formulations, and Jordan/squarefree weighted sums found no external theorem needed for the argument above. No novelty is claimed for the elementary fact that a nonzero finite exponential sum cannot decay to zero on a half-line, nor for the Smith/Jordan or zeta-ratio identities already anchored in this line. The Mathia-specific contribution is the exact placement of that finite-dimensional uniqueness inside the nonsquarefree Jordan occupation problem and the resulting separation between `FD-039`-type spikes and finite dominant Mellin packets. No new `SOURCES.md` dependency is load-bearing.

The result is falsified if `G_ns` has a nonzero null vector, if sampling on all large squares fails to force that vector to vanish, or if the exact hyperbola energies of a profile satisfying (5) do not converge to the quadratic forms (34)--(35). The physical consequence is falsified as an application if the source does not actually satisfy the finite-packet asymptotic (42); the theorem must not be cited as proof that it does.

The next source-specific target is now more precise. To turn the accepted joint-occupation clue into a physical theorem, it is enough to obtain either a finite/quantitatively compact spectral approximation whose nonsquarefree frame constant stays bounded away from zero, or a direct arithmetic substitute using the exact coefficient law (41). Conversely, a genuine physical escape must explain how increasingly rich Mellin content defeats every fixed finite-frame bound rather than merely reproduce the synthetic triangular spikes of `FD-039`.