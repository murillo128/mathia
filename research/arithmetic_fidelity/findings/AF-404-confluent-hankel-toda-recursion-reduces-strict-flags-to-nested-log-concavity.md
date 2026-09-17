# AF-404 — Confluent Hankel Toda recursion reduces strict flags to nested log-concavity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-IDENTITY` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `TODA` · `STRICT-INTERIOR` · `NO-NOVELTY-CLAIM`

## Claim

Let `I` be an interval, let `m>=1`, and let `f\in C^{2m}(I)`. Put

\[
\tau_m(t):=\det\!\left(f^{(i+j)}(t)\right)_{i,j=0}^{m-1},
\qquad
H_m(t):=(-1)^{m(m-1)/2}\tau_m(t),
\tag{1}
\]

with `H_0=\tau_0:=1`. Then the Hankel/Wronskian determinants satisfy the classical Toda-molecule identity

\[
\boxed{
\tau_m\tau_m''-(\tau_m')^2=\tau_{m+1}\tau_{m-1}.
}
\tag{2}
\]

After the orientation used in AF-403 this becomes

\[
\boxed{
H_{m+1}H_{m-1}
=-\big(H_mH_m''-(H_m')^2\big)
=-H_m^2(\log H_m)''
}
\tag{3}
\]

where the logarithmic form is used on a region with `H_m>0`.

Consequently, for fixed `r>=2` and `f\in C^{2r-2}(I)` with `f>0`, the complete strict confluent flag

\[
H_1>0,\ldots,H_r>0
\tag{4}
\]

is equivalent to the recursive chain

\[
\boxed{
(\log H_m)''<0
\qquad (m=1,\ldots,r-1).
}
\tag{5}
\]

Here the logarithms are well-defined inductively: `H_1=f>0`; strict log-concavity of `H_m`, together with positivity of `H_{m-1}`, forces `H_{m+1}>0` by `(3)`.

Thus AF-403's complete local flag is not an unrelated list of higher-derivative inequalities. In the strict interior it is a **Toda chain of nested log-concavity certificates**. Each new total-positivity order asks whether the previous confluent certificate is itself strictly log-concave.

This is classical determinant/Toda mathematics. The durable Arithmetic Fidelity consequence is a sharper representation of the live higher-order resource: after AF-403 removes arbitrary node placement, equation `(3)` removes most of the apparent algebraic independence between successive confluent orders.

## Determinant identity and orientation

The determinant in `(1)` is simultaneously a Hankel determinant of the derivative sequence and the Wronskian

\[
\tau_m=W(f,f',\ldots,f^{(m-1)}).
\tag{6}
\]

The standard Jacobi/Desnanot--Jacobi determinant identity applied to this derivative-Hankel family gives `(2)`; equivalently, `(2)` is the one-dimensional Toda-molecule equation for these Hankel `tau` functions.

The sign in `(3)` is forced, not conventional. Since

\[
\tau_k=(-1)^{k(k-1)/2}H_k,
\tag{7}
\]

the product of the two orientation factors on the right of `(2)` is

\[
(-1)^{(m+1)m/2}\,(-1)^{(m-1)(m-2)/2}=-1,
\tag{8}
\]

while the common factor on the left squares to `+1`. Therefore

\[
H_mH_m''-(H_m')^2=-H_{m+1}H_{m-1},
\tag{9}
\]

which is exactly `(3)`.

The first case is already AF-218's curvature identity:

\[
H_2=-f^2(\log f)''.
\tag{10}
\]

The second case says

\[
H_3=-\frac{H_2^2}{H_1}(\log H_2)'',
\tag{11}
\]

so once `H_2>0`, order three is equivalent to strict log-concavity of the order-two certificate itself.

## Normalized curvature recursion

For a positive profile write

\[
g=\log f,
\qquad
q=-g'',
\qquad
R_m:=\frac{H_m}{f^m}.
\tag{12}
\]

Then `R_0=R_1=1`, and on a strict positive flag `(3)` becomes

\[
\boxed{
R_{m+1}R_{m-1}
=R_m^2\left(mq-(\log R_m)''\right).
}
\tag{13}
\]

Indeed,

\[
(\log H_m)''
=m(\log f)''+(\log R_m)''
=-mq+(\log R_m)'',
\tag{14}
\]

and all powers of `f` cancel from `(3)`.

The first normalized certificates are therefore

\[
R_2=q,
\tag{15}
\]

and

\[
R_3
=q^2\left(2q-(\log q)''\right)
=2q^3-qq''+(q')^2,
\tag{16}
\]

recovering AF-403's order-three formula without an independent fourth-derivative determinant expansion.

Writing

\[
S:=R_3=2q^3-qq''+(q')^2,
\tag{17}
\]

the next order is

\[
\boxed{
R_4
=\frac{S^2}{q}\left(3q-(\log S)''\right).
}
\tag{18}
\]

Hence, on the already-certified order-three region `q>0`, `S>0`, the exact order-four gate is simply

\[
\boxed{
(\log S)''<3q.
}
\tag{19}
\]

For audit purposes, expanding `(18)` gives

\[
\begin{aligned}
R_4={}&12q^6-24q^4q''+24q^3(q')^2+2q^3q''''
-12q^2q'q'''+7q^2(q'')^2\\
&+12q(q')^2q''-qq''q''''+q(q''')^2
-9(q')^4+(q')^2q''''-2q'q''q'''+(q'')^3.
\end{aligned}
\tag{20}
\]

The compact Toda form `(18)` is therefore not hiding a weaker condition; it exactly reorganizes the sixth-derivative order-four determinant anticipated in AF-403.

## Concrete full-Euler consequence

For the full Euler-log profile already studied in AF-218 and AF-219,

\[
f(t)=-\log(1-e^{-e^t}),
\tag{21}
\]

those findings establish globally

\[
q>0
\qquad\text{and}\qquad
S=R_3>0.
\tag{22}
\]

Therefore the next unresolved finite-order question for that concrete Riemann-facing kernel is no longer an arbitrary `4 x 4` placement problem, nor an opaque sixth-derivative sign expansion. By AF-403 and `(18)`, full-Euler `STP_4` is reduced exactly to the one-variable differential inequality

\[
\boxed{
(\log S(t))''<3q(t)
\qquad\text{for every }t\in\mathbb R.
}
\tag{23}
\]

No claim is made here that `(23)` holds. AF-217 still proves that the full Euler-log kernel cannot be totally nonnegative at every order, so the Toda hierarchy must eventually fail at some finite order. AF-404 only identifies the exact recursive gate at which each possible failure occurs.

This is the required arithmetic stress test of the abstract identity: the universal Toda recurrence immediately turns the concrete finite-order Euler problem left by AF-219/AF-403 into a sharply falsifiable scalar inequality.

## Relation to AF-403

AF-403 proves, through a two-pass extended-complete-Chebyshev argument, that strict positivity of

\[
H_1,\ldots,H_r
\tag{24}
\]

forces every ordinary translation minor through order `r` to be positive. It therefore compresses arbitrary row/column placement to the complete confluent flag.

AF-404 performs a second compression inside that flag. In the strict region, successive entries are linked by `(3)`: retaining `H_{m-1}` and `H_m` plus the local curvature of `H_m` determines the sign and magnitude of `H_{m+1}`. The information flow becomes

\[
\text{nested log-concavity/Toda chain}
\Longrightarrow
\text{complete confluent flag}
\Longrightarrow
\text{all ordinary translation minors}.
\tag{25}
\]

This does **not** make the all-order problem finite. To certify `PF_\infty` one still needs the hierarchy for unbounded `m`, consistent with AF-372 and AF-217. The result instead removes the misleading appearance that every higher confluent determinant is a wholly new local object.

## Arithmetic-fidelity interpretation

The retained target remains the Boolean ordered property `K_f\in STP_r`, not recovery of `f` itself. AF-403 showed that a severe placement compression is target-faithful on the strict complete-flag source class. AF-404 identifies an additional internal rigidity of that certificate: the flag evolves by a deterministic Toda recursion, and strict positivity propagates exactly when each current certificate has the required log-concavity.

This is a clean example of **source-class rigidity replacing retained data**. The omitted next-order determinant is not stored independently; it is reconstructed from the current determinant and its local differential geometry. Conversely, when `(\log H_m)''` reaches zero, the next confluent certificate reaches the boundary and the strict propagation mechanism stops. That makes the first loss of nested log-concavity a natural exact failure location for finite-order fidelity.

The mechanism is source-independent and creates no arithmetic discriminator. Rational primes gain nothing merely from being labelled primes. Any RH-facing consequence still has to prove the relevant Toda/log-concavity gate from the actual arithmetic profile or from a justified source restriction.

## Prior-art and novelty audit

Equation `(2)` is classical Toda/Hankel-determinant mathematics, closely tied to the Jacobi/Desnanot--Jacobi identity. No novelty is claimed for the determinant recurrence, Toda interpretation, or the general fact that Hankel determinant `tau` functions satisfy Toda equations.

Relevant literature anchors are:

- Kenji Kajiwara, Tetsu Masuda, Masatoshi Noumi, Yasuhiro Ohta, and Yasuhiko Yamada, **“Determinant Formulas for the Toda and Discrete Toda Equations,”** *Funkcialaj Ekvacioj* 44(2), 291--307 (2001), arXiv:`solv-int/9908007`. Role: determinant formulas for general Toda solutions and the classical `tau`-function setting.
- Kenji Kajiwara, Marta Mazzocco, and Yasuhiro Ohta, **“A remark on the Hankel determinant formula for solutions of the Toda equation,”** *Journal of Physics A: Mathematical and Theoretical* 40(42), 12661--12675 (2007), DOI `10.1088/1751-8113/40/42/S11`, arXiv:`nlin/0701029`. Role: direct Hankel-determinant/Toda prior art.
- The classical Desnanot--Jacobi identity (the `2 x 2` case of Sylvester's determinant identity). Role: elementary determinant engine behind `(2)` for derivative-Hankel/Wronskian matrices.

The line-specific contribution is therefore not a new integrable-system theorem. It is the exact **representation change** at the AF-403 frontier: strict confluent total-positivity certificates can be organized as a nested log-concavity/Toda hierarchy, and the full-Euler order-four question reduces to `(23)`.

## Boundaries and falsification checks

- The logarithmic forms require strict positivity of the current certificate. At a zero of `H_m`, equation `(9)` still makes sense algebraically, but `\log H_m` does not; AF-386--AF-394 already show that nonstrict boundary strata can retain extra support/topology information.
- The recurrence does not prove positivity. It relocates the sign question from an `(m+1) x (m+1)` determinant to the curvature of `H_m`.
- Strict log-concavity of `H_m` is sufficient for the next sign only together with positivity of the preceding flag entry. Dropping `H_{m-1}>0` reverses or destroys the implication in `(3)`.
- No fixed cutoff is produced. AF-217's all-order obstruction for the Euler-log kernel remains untouched.
- The normalized form `(13)` is invariant under positive exponential tilts `f(t)\mapsto e^{at+b}f(t)`: such a tilt changes `\log f` only affinely and rescales each `H_m` positively. This is consistent with the translation-kernel gauge already used in AF-217/AF-218.
- Equation `(23)` is an exact reduction, not evidence that full-Euler order four succeeds. A sign change or equality in `3q-(\log S)''` at any point would falsify strict order-four confluent positivity and, by coalescence, rule out `STP_4`.
- The result supplies no conditioning bound. Even with every sign strict, margins may collapse as some `H_m` approaches zero.

## Consequence for the research line

The strict higher-order translation-kernel frontier should now be attacked recursively rather than by independent determinant expansions or arbitrary-node searches. For a concrete profile already certified through order `m`, the next exact question is the log-concavity of `H_m`, or equivalently the normalized curvature inequality from `(13)`.

For the full Euler-log kernel, the immediate finite-order frontier is `(23)`. For general Riemann-facing kernels, the first failure of the Toda/log-concavity chain identifies the exact local order at which AF-403's strict global propagation can no longer continue. Degenerate/nonstrict strata and quantitative conditioning remain separate problems.