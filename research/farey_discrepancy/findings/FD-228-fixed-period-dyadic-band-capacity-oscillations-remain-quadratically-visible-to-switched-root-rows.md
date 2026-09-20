# FD-228 — Fixed-period dyadic-band capacity oscillations remain quadratically visible to switched root rows

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** oscillatory divisor-cushion test / log-periodic response / Fourier nonvanishing / switched-Floquet mismatch / scale-adapted reservoir capacity
- **Depends on:** FD-227, FD-226, FD-225, FD-212
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + LOG-PERIODIC-DIVISOR-RESPONSE + UNIFORM-FOURIER-NONVANISHING + FINITE-PERIOD-CAPACITY-VETO + SWITCHED-FLOQUET-MISMATCH`

## Claim

FD-227 rules out smooth power-law cushions as a way to exploit the scale-adapted reservoir capacities of FD-226. The first genuinely oscillatory escape is to fill different dyadic bands by different order-one fractions of capacity, perhaps synchronized with the period-three switched schedule. That entire fixed-period class is still visible.

Let

\[
(\mathscr A b)(m)
=
\sum_{d\le m} b_d M\!\left(\left\lfloor\frac md\right\rfloor\right)
\tag{1}
\]

be the exact divisor-response operator from FD-225. Fix an integer `P>=1` and a nonzero `P`-periodic complex sequence `(a_j)`. Suppose

\[
\boxed{
 b_d=d\,a_{\lfloor\log_2 d\rfloor}+o(d).
}
\tag{2}
\]

Then there is a nonzero `P`-periodic sequence `(c_j)` such that

\[
\boxed{
(\mathscr A b)(2^j)
=4^j c_j+o(4^j).
}
\tag{3}
\]

Moreover the linear map from the dyadic-band amplitudes `(a_j)` to the response amplitudes `(c_j)` is invertible for every fixed period `P`.

Now use the switched root-row orders of FD-212,

\[
r_j=q_j+1=(1,4,4,1,4,4,\ldots).
\tag{4}
\]

Then (3) cannot be asymptotically null for all scheduled rows. There is a residue class modulo `lcm(P,3)` and a constant `eta>0` such that along that class

\[
\boxed{
\left|
(T-I)^{r_j}(\mathscr A b)(2^j)
\right|
\ge \eta 4^j
}
\tag{5}
\]

for all sufficiently large `j`, where `(TF)(m)=F(2m)`.

Thus an order-one oscillation among any **fixed finite collection of dyadic capacity fractions** cannot remove the FD-226 common-cushion bottleneck. This includes the most natural scheduler-matched attempt: a period-three occupancy profile proportional to `d` with one coefficient for each phase `(1,4,4)`. A subrelative perturbation of such a profile still leaks at the full quadratic scale.

For the scale-adapted reservoirs of FD-226, write

\[
B_N=\frac{N}{D\log N},
\qquad
|I_d^*\cap\mathbb P|
=\left(\frac14+o(1)\right)B_Nd.
\tag{6}
\]

If, on every cell needed by a growing scheduled row,

\[
k_{N,d}
=B_Nd\bigl(a_{\lfloor\log_2d\rfloor}+o(1)\bigr)
\tag{7}
\]

uniformly, with fixed-period amplitudes and not all amplitudes zero, then along some scheduled phase the reservoir contribution has size

\[
\boxed{
\left|
2(T-I)^{r_j}\mathscr A k_N(2^j)
\right|
\gg B_N4^j.
}
\tag{8}
\]

Here (8) is understood on rows with `j->infinity` and whose deepest sample remains within the available divisor grid. Consequently neither a fixed positive phase pattern nor an `o(1)` relative correction to it can be a capacity-feasible switched-null cushion.

The remaining escape is therefore narrower than after FD-227: it must have period or combinatorial complexity growing with depth, vary nonperiodically across divisor scales, or exploit substantial structure *inside* dyadic divisor bands. Fixed finite log-periodicity is not enough.

## 1. Fourier reduction of a finite dyadic-band period

Because `(a_j)` is `P`-periodic, expand it in the finite Fourier basis

\[
a_j=\sum_{z^P=1}\widehat a_z z^j.
\tag{9}
\]

It is therefore enough to understand one mode

\[
b_z(d):=d\,z^{\lfloor\log_2 d\rfloor},
\qquad |z|=1.
\tag{10}
\]

Let

\[
B_z(x):=\sum_{d\le x}b_z(d).
\tag{11}
\]

On a complete dyadic band,

\[
\sum_{2^k\le d<2^{k+1}}d
=\frac32\,4^k-\frac12\,2^k.
\tag{12}
\]

Hence at a dyadic endpoint

\[
\frac{B_z(2^j)}{4^jz^j}
\longrightarrow
C_0(z):=\frac{3}{2(4z-1)}.
\tag{13}
\]

In particular, uniformly on the unit circle,

\[
\boxed{|C_0(z)|\ge\frac3{10},}
\tag{14}
\]

because `|4z-1|<=5`.

More generally, for every fixed positive integer `a`, the limit

\[
L_a(z)
:=
\lim_{j\to\infty}
\frac{B_z(\lfloor2^j/a\rfloor)}{4^jz^j}
\tag{15}
\]

exists. One direct way to see this is to choose `ell=ceil(log_2 a)`. Apart from the harmless endpoint convention when `a` is a power of two, `floor(2^j/a)` eventually lies in dyadic band `j-ell` with a fixed limiting mantissa `2^ell/a`. Formula (12) gives a geometric sum over the complete earlier bands plus one quadratic partial-band contribution, so after division by `(4z)^j` every term has a limit.

The crude bound

\[
|B_z(x)|
\le\sum_{d\le x}d
=\frac{x(x+1)}2
\tag{16}
\]

will be more useful than the explicit expression for `L_a(z)`.

## 2. The Möbius divisor response has no blind Fourier phase

Expanding the Mertens kernel in (1) gives the exact identity

\[
(\mathscr A b_z)(m)
=
\sum_{a\le m}\mu(a)
B_z\!\left(\left\lfloor\frac ma\right\rfloor\right).
\tag{17}
\]

Set `m=2^j` and divide by `4^jz^j`. Equations (15)--(16), followed by dominated convergence, give

\[
\boxed{
(\mathscr A b_z)(2^j)
=C(z)(4z)^j+o(4^j),
}
\tag{18}
\]

where

\[
C(z)=\sum_{a\ge1}\mu(a)L_a(z).
\tag{19}
\]

The domination can be checked without any analytic number theory. From (16),

\[
\frac{|B_z(\lfloor2^j/a\rfloor)|}{4^j}
\le
\frac1{2a^2}+\frac1{2a2^j}.
\tag{20}
\]

The first majorant is summable, while summing the second over `a<=2^j` gives `O(j/2^j)`.

The key point is that **`C(z)` is uniformly nonzero for every phase on the unit circle**. The `a=1` term is exactly `C_0(z)`. For the remaining terms, (20) gives

\[
\left|
\sum_{a\ge2}\mu(a)L_a(z)
\right|
\le
\frac12\sum_{a\ge2}\frac{\mu(a)^2}{a^2}.
\tag{21}
\]

The absolutely convergent Euler product yields

\[
\sum_{a\ge1}\frac{\mu(a)^2}{a^2}
=
\frac{\zeta(2)}{\zeta(4)}
=
\frac{15}{\pi^2}.
\tag{22}
\]

Combining (14), (21), and (22),

\[
\boxed{
|C(z)|
\ge
\frac3{10}
-rac12\left(\frac{15}{\pi^2}-1\right)
=
\frac45-\frac{15}{2\pi^2}
>0.
}
\tag{23}
\]

Numerically the uniform margin in (23) is about `0.04009`. Thus the divisor/Mertens response cannot erase even one Fourier phase of a finite dyadic-band oscillation.

Returning to (9), linearity and (18) give

\[
(\mathscr A b)(2^j)
=
4^j
\sum_{z^P=1}
\widehat a_zC(z)z^j
+o(4^j).
\tag{24}
\]

Define

\[
c_j:=
\sum_{z^P=1}\widehat a_zC(z)z^j.
\tag{25}
\]

This is `P`-periodic. Since every Fourier multiplier `C(z)` is nonzero, the map `a->c` is invertible. In particular `c` cannot vanish identically unless `a` did. This proves (3).

The conclusion is stable under the `o(d)` perturbation in (2). If `e_d=o(d)` and

\[
E(x)=\sum_{d\le x}e_d,
\]

then `E(x)=o(x^2)`. Expanding as in (17),

\[
\mathscr A e(m)
=
\sum_{a\le m}\mu(a)
E\!\left(\left\lfloor\frac ma\right\rfloor\right).
\tag{26}
\]

Split at `m/a>=Y`. On that part, for large fixed `Y`, the definition of `o(x^2)` bounds the sum by an arbitrarily small multiple of `m^2 sum a^(-2)`. On the complementary part `m/a<Y`, only bounded values of `E` occur and the total is `O_Y(m)`. Hence

\[
\boxed{\mathscr A e(m)=o(m^2).}
\tag{27}
\]

## 3. The switched recurrence cannot carry a quadratic periodic mode

Let

\[
y_j:=(\mathscr A b)(2^j),
\qquad
v_j:=4^jc_j.
\tag{28}
\]

Equation (3) says `y_j=v_j+o(4^j)`. Applying any fixed row order `r` preserves an `o(4^j)` remainder, so for the period-three schedule (4),

\[
(T-I)^{r_j}(\mathscr A b)(2^j)
=(E-I)^{r_j}v_j+o(4^j).
\tag{29}
\]

The normalized leading coefficient in `(E-I)^{r_j}v_j/4^j` is periodic modulo `lcm(P,3)`. Suppose, toward a contradiction, that every one of those leading coefficients vanished. Then the nonzero sequence `(v_j)` would satisfy exactly

\[
(E-I)^{r_j}v_j=0
\qquad(j\ge0).
\tag{30}
\]

FD-212 already identifies the Floquet spectrum of this switched recurrence. For completeness, write

\[
x_m=v_{3m}=v_{3m+1},
\qquad
z_m=v_{3m+2}.
\tag{31}
\]

The two fourth-difference equations in each period give

\[
z_{m+1}+2x_{m+1}-4z_m+x_m=0,
\tag{32}
\]

\[
x_{m+2}-4z_{m+1}+2x_{m+1}+z_m=0.
\tag{33}
\]

Thus

\[
\begin{pmatrix}
x_{m+2}\\z_{m+1}\\x_{m+1}
\end{pmatrix}
=
\begin{pmatrix}
-10&15&-4\\
-2&4&-1\\
1&0&0
\end{pmatrix}
\begin{pmatrix}
x_{m+1}\\z_m\\x_m
\end{pmatrix}.
\tag{34}
\]

The characteristic polynomial is

\[
(\lambda-1)(\lambda^2+7\lambda+1),
\tag{35}
\]

so every exact solution of (30) grows at most like

\[
\rho^j,
\qquad
\rho=
\left(\frac{7+3\sqrt5}{2}\right)^{1/3}
=\varphi^{4/3}
<2.
\tag{36}
\]

But a nonzero periodic `(c_j)` makes `v_j=4^jc_j` have size comparable to `4^j` along at least one residue class. This contradicts (36). Therefore at least one normalized leading switched coefficient is nonzero. Periodicity then supplies a fixed `eta>0` and an infinite residue class on which (5) holds.

The mismatch is strong: the candidate capacity profile carries a quadratic dyadic multiplier `4`, whereas the largest switched-null Floquet multiplier per dyadic step is only `rho<2`. Synchronizing the occupancy with the three scheduler phases cannot bridge that spectral gap.

## 4. Consequence for scale-adapted prime reservoirs

FD-226 gives, under its existing prime-resolution condition, the uniform capacity law (6). A fixed choice of phase fractions of those cells has the form (7), after absorbing the factor `1/4` into the amplitudes. The finite-range version of Sections 1--2 needs no new uniform asymptotic theorem: for any scheduled rows with `m=2^j->infinity` and deepest sample at most `D`, only cells `d<=O(m)` enter, and a uniform `o(B_Nd)` occupancy error contributes `o(B_Nm^2)` by the trivial bound `|M(x)|<=x` and the same split used in (27).

After restoring the factor `2` contributed by each core-prime flip, (5) therefore yields (8). In particular, if the amplitudes `a_0,...,a_(P-1)` are fixed nonnegative fractions of local capacity and at least one is positive, no subrelative adjustment can make all the switched observations small. Allowing signs in the theorem only strengthens the veto: even an unphysical signed fixed-period cushion cannot hide its quadratic leading mode.

This sharply separates two notions of oscillation. The Floquet obstruction of FD-212 is itself period three in the **response sequence** and has growth radius below `2`; it can therefore be realized by bounded source increments. The attempted reservoir cushion here oscillates in the **divisor occupancy** while retaining the natural linear capacity envelope `b_d asymp d`. The divisor-response operator raises that envelope to quadratic scale, and the nonvanishing Fourier multipliers (23) prevent finite phase cancellation before the switched rows are applied.

Consequently FD-227's smooth-profile veto was not merely an artifact of averaging over dyadic phase. Order-one phase alternation across a fixed number of bands still fails. Any successful nonconstant positive cushion must leave the finite-period log-scale regime altogether.

## 5. Prior-art boundary and next test

Log-periodic functions, complex scaling exponents, and discrete scale invariance are classical. Sornette's review, *Discrete-scale invariance and complex dimensions*, Physics Reports **297** (1998), 239--270, DOI `10.1016/S0370-1573(97)00076-8`, is a standard general reference for power laws decorated by periodic functions of logarithmic scale. Regularly log-periodic functions have also been studied directly in analysis; see Péter Kevei, *Regularly log-periodic functions and some applications*, Probability and Mathematical Statistics **40** (2020), 159--182, DOI `10.37190/0208-4147.40.1.10`.

No claim is made that finite Fourier decomposition of a log-periodic profile or discrete-scale invariance is new. The repository-specific content is the exact interaction with the FD-225 divisor/Mertens response: the uniform Fourier nonvanishing estimate (23), its invertibility consequence for every finite dyadic phase pattern, and the mismatch with the explicit `(1,4,4)` switched Floquet spectrum. No external theorem is load-bearing, so no new durable source anchor is required in `SOURCES.md`.

The boundary remains important. FD-228 does **not** show that the smallest-cell cushion of FD-226 is intrinsic. It does not rule out periods `P=P(D)` growing with the block depth, nonperiodic divisor-scale profiles, sparse order-one depletions, or oscillation within individual dyadic bands. Nor does it prove a lower bound on the best cellwise slack over the full finite-dimensional switched nullspace.

The next discriminating test is therefore no longer merely “try an oscillatory profile.” It is to let the oscillatory complexity itself grow: either quantify the maximum feasible lower slack among exact switched-null occupancy vectors on `1<=d<=D`, or construct a growing-period/nonstationary null cushion whose occupancies stay a positive fraction of the scale-adapted capacities while leaving room for the physical Mertens correction. If even those profiles must repeatedly approach the small-cell boundary, the remaining `D^2` pressure would begin to look structural rather than a consequence of using an overly regular cushion.
