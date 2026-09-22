# FD-262 — Full-grid Mertens repair has only linear-log depth amplification

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact divisor-response inversion / source-side repair demand / full-grid flattening / depth-amplification ceiling / route closure
- **Depends on:** FD-225, FD-226, FD-260, FD-261
- **Classification:** `EXACT-DERIVED + DIVISOR-INVERSION + FULL-GRID-FLATTENING + SOURCE-DEMAND-UPPER-BOUND + DEPTH-AMPLIFICATION-CEILING + ROUTE-CLOSURE`

## Claim

The superlinear depth amplification isolated as the missing general-cone mechanism in FD-261 cannot come from the canonical full-grid divisor inverse of FD-225, nor more generally from any repair whose **entire integer-multiple residual grid** has increments no larger than the arithmetic Mertens forcing scale.

Let

\[
(\mathscr A c)(m)
=
\sum_{d\le m}c_d
M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad 1\le m\le D,
\]

and for a horizon `N` define the repaired full-grid residual

\[
R_N(m)
:=
M(mN)+2(\mathscr A c)(m),
\qquad R_N(0):=0.
\]

Also write the consecutive block-Mertens forcing as

\[
B_q(N)
:=
M(qN)-M((q-1)N).
\]

Then for every `1<=d<=D` there is the exact identity

\[
\boxed{
2c_d
=
\sum_{q\mid d}
\bigl(\Delta R_N(q)-B_q(N)\bigr),
}
\tag{1}
\]

where `\Delta R_N(q)=R_N(q)-R_N(q-1)`.

Consequently, if

\[
\mathcal B_N(T)
:=
\max_{1\le q\le T}|B_q(N)|,
\qquad
\mathcal E_N(T)
:=
\max_{1\le q\le T}|\Delta R_N(q)|,
\]

then every dyadic band `x<d<=2x<=D` satisfies

\[
\boxed{
\sum_{x<d\le2x}|c_d|
\le
\bigl(\mathcal B_N(2x)+\mathcal E_N(2x)\bigr)
\,x\bigl(1+\log(2x)\bigr).
}
\tag{2}
\]

In particular the negative repair demand obeys the same bound,

\[
\boxed{
\sum_{x<d\le2x}(-c_d)_+
\ll
\bigl(\mathcal B_N(2x)+\mathcal E_N(2x)\bigr)
\,x\log(2x).
}
\tag{3}
\]

For the FD-225 canonical full-grid repair one has

\[
R_N(m)=\varepsilon_m,
\qquad |\varepsilon_m|\le1,
\]

so `\mathcal E_N(T)<=2`. Therefore at the deepest band `x\asymp D`,

\[
\boxed{
R_N^{\rm neg}(x)
:=
\sum_{x<d\le2x}(-c_d)_+
\ll
\bigl(1+\mathcal B_N(D)\bigr)
D\log D.
}
\tag{4}
\]

Thus, **relative to its own block-Mertens forcing amplitude**, the canonical exact divisor inverse has at most linear depth amplification up to one logarithm. If on a family

\[
1+\mathcal B_N(D)=N^{\theta+o(1)},
\qquad
D=N^{\lambda+o(1)},
\]

then

\[
R_N^{\rm neg}(x)
\le
N^{\theta+o(1)}D^{1+o(1)}.
\tag{5}
\]

FD-261 showed that, at a fixed arithmetic amplitude exponent, the general FD-260 positive-cushion ceiling can beat the independent first-row scale only if the repair demand carries depth exponent

\[
\alpha>2-\beta
=1.4150374992\ldots,
\qquad
\beta=\log_2\frac32.
\]

Equation (5) rules out obtaining that missing exponent from the canonical full-grid repair: its depth exponent is at most `1`. Any successful continuation of the general-cone route must therefore obtain its advantage from something **other than divisor-depth accumulation of the FD-225 inverse**: for example a stronger arithmetic forcing scale in deeper blocks, a switched-only repair whose unsampled integer rows are allowed to move substantially, or additional one-sided structure that upgrades the cushion ceiling itself.

This is a route closure, not a contradiction for the existing source construction. The FD-225--FD-226 block remains valid, and the result does not claim that arbitrary switched-only repairs have linear depth demand.

## 1. Exact repair identity from one ordinary difference

FD-225 proved the full divisor-response inversion

\[
(\mathscr A c)(m)
=
\sum_{n\le m}(c*\mu)(n).
\tag{6}
\]

Taking an ordinary difference gives

\[
(\mathscr A c)(q)-(\mathscr A c)(q-1)
=(c*\mu)(q).
\tag{7}
\]

By definition of `R_N`,

\[
\Delta R_N(q)
=
B_q(N)+2(c*\mu)(q),
\tag{8}
\]

so

\[
(c*\mu)(q)
=
\frac{\Delta R_N(q)-B_q(N)}2.
\tag{9}
\]

Dirichlet-convolving with the constant-one function and using `\mu*1=\varepsilon` yields

\[
c
=
1*(c*\mu),
\]

which is exactly (1).

The point is not merely that the inverse exists. Equation (1) says that the repair coefficient at depth `d` can only add the forcing increments attached to **divisors of `d`**. If every forcing increment has size at most `A`, the number of terms is `\tau(d)`, not a power of the ambient depth.

## 2. Summing a dyadic band costs only the divisor average

From (1), for every `d<=T`,

\[
|c_d|
\le
\frac{\mathcal B_N(T)+\mathcal E_N(T)}2\,\tau(d).
\tag{10}
\]

The needed divisor estimate is elementary:

\[
\sum_{d\le X}\tau(d)
=
\sum_{ab\le X}1
=
\sum_{a\le X}\left\lfloor\frac Xa\right\rfloor
\le
X\sum_{a\le X}\frac1a
\le
X(1+\log X).
\tag{11}
\]

Hence

\[
\begin{aligned}
\sum_{x<d\le2x}|c_d|
&\le
\frac{\mathcal B_N(2x)+\mathcal E_N(2x)}2
\sum_{d\le2x}\tau(d)\\
&\le
\bigl(\mathcal B_N(2x)+\mathcal E_N(2x)\bigr)
\,x(1+\log(2x)),
\end{aligned}
\]

which proves (2). Since `(-c_d)_+<=|c_d|`, equation (3) follows immediately.

This upper bound is deliberately insensitive to signs. Any cancellation among the block-Mertens increments can only reduce the actual repair mass. For the present purpose that is exactly what is needed: superlinear **lower** depth amplification is impossible if even the absolute repair mass has only linear-log growth at fixed forcing amplitude.

## 3. Apply the bound to the FD-225 rounded flattening

FD-225 chooses the integer response target

\[
y_N(m)
=
\operatorname{nint}\!\left(-\frac{M(mN)}2\right),
\qquad y_N(0)=0,
\tag{12}
\]

and takes `c` to be the exact divisor inverse `\mathscr A c=y_N`. Therefore

\[
R_N(m)
=
M(mN)+2y_N(m)
=:\varepsilon_m,
\qquad |\varepsilon_m|\le1.
\tag{13}
\]

For `q>=2`,

\[
|\Delta R_N(q)|
\le2,
\]

and the same bound trivially covers `q=1`. Thus `\mathcal E_N(D)<=2`, and (4) follows from (3).

The positive common occupancy `A` used in FD-225 does not alter this conclusion. Its response is constant on the integer-multiple grid because `\mathscr A 1=1`; hence it disappears under `\Delta`. Equivalently, the actual source values are `2A+R_N(m)`, and subtracting the common constant leaves exactly the residual above.

More generally, replacing the rounded target by any full-grid repair whose residual has bounded first differences changes only the additive `\mathcal E_N` term in (2). A bounded residual itself gives `\mathcal E_N=O(1)`. A constant target offset likewise affects no deep increment once the common occupancy is separated.

## 4. Comparison with the FD-261 phase boundary

FD-261 considers a repair-demand lower bound on the deepest dyadic band of the form

\[
R_N^{\rm neg}(x)
\ge
N^{\theta-o(1)}D^{\alpha-o(1)}
\tag{14}
\]

and shows that, against the general FD-260 cushion ceiling, beating the same-amplitude first-row obstruction requires

\[
\alpha>2-\beta
=1.4150374992\ldots .
\tag{15}
\]

Suppose the actual block forcing controlling the full-grid repair satisfies

\[
1+\mathcal B_N(D)=N^{\theta+o(1)}.
\tag{16}
\]

Then (4) gives

\[
R_N^{\rm neg}(x)
\le
N^{\theta+o(1)}D^{1+o(1)}.
\tag{17}
\]

So a lower bound (14) for this same canonical repair cannot hold with any fixed `\alpha>1`. In particular it cannot cross (15).

This closes one natural interpretation of the frontier left by FD-261. The missing `D^{1.415...}` behavior cannot be hiding in repeated divisor inversion, triangular conditioning, or accumulation of the canonical block corrections. The exact inverse is too sparse: after factoring out the largest arithmetic increment, only the divisor count remains.

There are two important limitations.

First, `\mathcal B_N(D)` is a **maximum over deep block-Mertens increments**. It can in principle have a larger `N`-exponent than the first block `M(2N)-M(N)`. Equation (17) rules out extra gain from the *depth variable*; it does not rule out stronger arithmetic forcing at larger multiples.

Second, the theorem assumes control of the complete integer-multiple residual grid. A construction constrained only on the scheduled switched observations may allow very large intermediate `\Delta R_N(q)` and is not covered by (4). Such uncontrolled intermediate motion is therefore one of the few remaining ways a switched-only repair could generate additional aggregate demand without contradicting the exact inverse.

## 5. Finite audit and prior-art boundary

A direct finite audit was performed with `N=100`, `D=32`. Computing `\mu` by a sieve, forming `M`, choosing the FD-225 nearest-integer target (12), and applying the divisor inverse reproduces every target value exactly. In this sample

\[
\max_{q\le32}|B_q(100)|=16,
\qquad
\max_{q\le32}|\Delta y_N(q)|=8,
\]

while the top half-band has

\[
\sum_{16<d\le32}|c_d|=57.
\]

The elementary bound above gives `621` for the same band. The audit is not used in the proof; it only checks the indexing, the factor `2`, and the boundary convention at `q=1`.

A targeted prior-art search found the expected classical ingredients: Möbius/Dirichlet inversion, divisor-sum estimates, and the classical relation between Farey discrepancy and the summatory Möbius function. No external theorem was found that matches the repository-specific statement that the FD-225 full-grid repair cannot provide the superlinear depth exponent demanded by FD-261. No external result is load-bearing here, so `SOURCES.md` does not require an update.

**Verdict.** The general positive-cushion route cannot be completed by proving that the canonical FD-225 full-grid correction accumulates a Mertens-sized negative demand independently in every divisor layer. Exact divisor inversion gives the opposite ceiling: after the arithmetic block scale is factored out, the entire deep-band repair has only `D log D=D^{1+o(1)}` mass. To obtain a source-side contradiction earlier than the current first-row ceiling, one must now exploit stronger deep arithmetic amplitudes, deliberately leave the full-grid-flattening class and use switched-only degrees of freedom, or prove additional one-sided structure strong enough to improve the FD-260 cushion depletion law itself.
