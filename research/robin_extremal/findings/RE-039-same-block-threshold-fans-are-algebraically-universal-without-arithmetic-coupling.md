# RE-039 — same-block threshold fans are algebraically universal without arithmetic coupling

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SYNTHETIC-CONTROL + ADAPTIVE-KINEMATICS + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-038` strengthens the false-RH reduction from unrelated fixed-`b` selectors to one ordered family of adaptive amplitude maximizers living on the same finite Robin-counterexample blocks. That coherence is real, but its **convex-envelope part is not by itself an obstruction**. Any prescribed finite ordered switch pattern in `b` can be realized exactly by positive synthetic Robin heights, while simultaneously preserving the quantitative left-endpoint witness inherited in `RE-038`, the exact breakpoint secant law, the small-positive-height regime used by `RE-034`, and even logarithmic spacing in the intrinsic coordinate `Y=log C`.

More precisely, fix

\[
0<b_0<b_1<\frac12,
\qquad
J=[b_0,b_1],
\qquad
c_0>0.
\tag{1}
\]

Choose any integer `k>=0`, any strictly increasing breakpoints

\[
b_0<\beta_1<\cdots<\beta_k<b_1,
\tag{2}
\]

and any strictly increasing intrinsic coordinates

\[
Y_0<Y_1<\cdots<Y_k.
\tag{3}
\]

Define positive synthetic excesses recursively by

\[
\boxed{
R_0:=c_0Y_0^{-b_0},
\qquad
R_i:=R_{i-1}
\left(\frac{Y_{i-1}}{Y_i}\right)^{\beta_i}
\quad(1\le i\le k),
}
\tag{4}
\]

and define the same adaptive amplitude used in `RE-034`--`RE-038`,

\[
A_b(i):=Y_i^bR_i.
\tag{5}
\]

Then the rightmost maximizer of `A_b(i)` is **exactly**

\[
\boxed{
i(b)=\#\{j:\beta_j\le b\}.
}
\tag{6}
\]

Thus an arbitrary monotone finite threshold fan can be manufactured with no arithmetic input at all. At the left endpoint, state `0` is the unique maximizer and

\[
A_{b_0}(0)=c_0,
\tag{7}
\]

while for every `b in J`

\[
\boxed{
\max_i A_b(i)
\ge A_b(0)
=c_0Y_0^{b-b_0},
}
\tag{8}
\]

which is exactly the quantitative same-block inheritance used by `RE-038`. Consequently, neither the ordered fan, its breakpoint secants, nor the inherited quantitative lower bound can supply a contradiction without an additional arithmetic coupling.

## 1. Exact realization of an arbitrary threshold fan

Put

\[
\ell_i(b):=\log A_b(i)=\log R_i+b\log Y_i.
\tag{9}
\]

The recursion (4) gives the exact adjacent difference

\[
\boxed{
\ell_i(b)-\ell_{i-1}(b)
=(b-\beta_i)
\log\frac{Y_i}{Y_{i-1}}.
}
\tag{10}
\]

Suppose

\[
\beta_m\le b<\beta_{m+1},
\tag{11}
\]

with the conventions `beta_0=b_0` and `beta_{k+1}=b_1` only for indexing the cells. For `j>m`, summing (10) gives

\[
\ell_j(b)-\ell_m(b)
=
\sum_{r=m+1}^{j}
(b-\beta_r)
\log\frac{Y_r}{Y_{r-1}}<0.
\tag{12}
\]

For `j<m`, the same telescoping identity gives `ell_m(b)>=ell_j(b)`. At the exact switch `b=beta_m`, only states `m-1` and `m` tie locally, and the rightmost convention chooses `m`. Hence (6) follows.

This construction also reproduces the exact secant law of `RE-038`. At the switch `beta_i`,

\[
R_iY_i^{\beta_i}
=R_{i-1}Y_{i-1}^{\beta_i},
\tag{13}
\]

so

\[
\boxed{
\frac{R_i}{R_{i-1}}
=
\left(\frac{Y_{i-1}}{Y_i}\right)^{\beta_i}.
}
\tag{14}
\]

Over the whole fan,

\[
\log\frac{R_0}{R_k}
=
\sum_{i=1}^k
\beta_i\log\frac{Y_i}{Y_{i-1}}.
\tag{15}
\]

Therefore, when `k>0`, there is a weighted mean `bar beta in (b_0,b_1)` such that

\[
\boxed{
\frac{R_k}{R_0}
=
\left(\frac{Y_0}{Y_k}\right)^{\bar\beta}.
}
\tag{16}
\]

The same-block cone of `RE-038` is therefore automatic for the synthetic control. It is a consequence of ordered affine-envelope geometry, not an arithmetic rigidity statement.

## 2. The control lives in the same asymptotically small-height regime

The construction can be made asymptotic in exactly the regime used by the adaptive tangent argument. Let `Y_0=T->infinity` and allow `k=k(T)` to vary. Assume only

\[
\frac{Y_k}{T}\longrightarrow1.
\tag{17}
\]

Since every `beta_i` lies in `[b_0,b_1]`, equation (4) gives uniformly in `i`

\[
-b_1\log\frac{Y_i}{T}
\le
\log\frac{R_i}{R_0}
\le
-b_0\log\frac{Y_i}{T}.
\tag{18}
\]

Thus (17) implies

\[
\boxed{
R_i=(c_0+o(1))T^{-b_0}
}
\tag{19}
\]

uniformly over the whole block. If we encode the synthetic Robin height in the natural way,

\[
h_i:=\log(1+R_i),
\tag{20}
\]

then

\[
\boxed{
h_i\log Y_i\longrightarrow0}
\tag{21}
\]

uniformly. This is the same small-positive-height regime that makes the adaptive barrier strictly concave in `RE-034`. The control is therefore not exploiting large artificial excesses that would disappear before the genuine asymptotic argument begins.

A concrete family shows that neither block stretch nor a bounded number of selector changes is forced by the fan. Let

\[
k(T):=\left\lfloor T^{1-b_0/2}\right\rfloor,
\qquad
Y_i:=T+i\log T,
\tag{22}
\]

and take an evenly spaced breakpoint mesh

\[
\beta_i
:=b_0+\frac{i}{k(T)+1}(b_1-b_0).
\tag{23}
\]

Then

\[
Y_k-T
=O\!\left(T^{1-b_0/2}\log T\right)
=o(T),
\tag{24}
\]

so (17)--(21) hold, yet the number of threshold switches tends to infinity and the largest `b`-cell tends to zero. Every adjacent intrinsic jump is exactly `log T`, matching the **coarse logarithmic jump scale** available for consecutive CA states in `RE-034`. This is not a model of the actual CA event lattice, but it prevents any argument based only on relative block length, small Robin height, or logarithmic local spacing from turning the fan into a contradiction.

## 3. Even the adaptive tangent displacement is algebraically reproducible

The obstruction is narrower still. For each synthetic state put

\[
a_i:=1-e^{-h_i}=\frac{R_i}{1+R_i},
\qquad
g(x):=\frac1{x\log x}.
\tag{25}
\]

For a `b` lying in the selection cell of state `i`, define `Z_i(b)>Y_i` by the same exact tangent equation as `RE-034`,

\[
\boxed{
g(Z_i(b))
=g(Y_i)-\frac{ba_i}{Y_i}.}
\tag{26}
\]

Equation (19) gives, uniformly over `i` and `b in J`,

\[
\frac{ba_i/Y_i}{g(Y_i)}
=ba_i\log Y_i
=o(1).
\tag{27}
\]

Hence the right side of (26) is positive for all sufficiently large `T`, the solution exists uniquely, and

\[
\frac{Z_i(b)}{Y_i}\longrightarrow1.
\tag{28}
\]

Using

\[
-g'(x)
=\frac{\log x+1}{x^2(\log x)^2}
\sim\frac1{x^2\log x},
\tag{29}
\]

the mean-value theorem yields the uniform displacement law

\[
\boxed{
Z_i(b)-Y_i
=(b+o(1))h_iY_i\log Y_i.
}
\tag{30}
\]

Thus the **kinematic** part of the adaptive tangent mechanism is also universal: once a positive height profile is supplied, the same tangent displacement can be reconstructed without primes, CA exponent thresholds, or zeta zeros.

What the construction cannot supply is exactly what matters arithmetically. It does not prove

\[
Y_i=\Phi(Z_i(b)),
\tag{31}
\]

for the genuine prime-layer staircase, does not generate `theta(Z)-Z` and the logarithmic Mertens-product error from one shared prime source, and does not reproduce the translated nonlinear prime-race relation of `RE-037` simultaneously across the fan. Those are not cosmetic omissions: they are the surviving places where arithmetic information enters.

## 4. Consequence for the live false-RH strategy

`RE-038` remains a correct strengthening of the fixed-parameter picture: under hypothetical RH failure, the actual CA states selected for different thresholds are coupled inside the same counterexample blocks. The present control shows, however, that **the convex-envelope coherence itself has complete algebraic flexibility**. Even an arbitrarily dense ordered fan with the correct quantitative inheritance, exact breakpoint laws, vanishing Robin heights, and CA-scale local `Y` jumps can be realized synthetically.

Therefore a closing argument cannot have the form

\[
\text{same-block monotone fan}
+\text{small height}
+\text{short relative block}
\Longrightarrow\text{contradiction}.
\tag{32}
\]

Any such implication is falsified by (4)--(24) unless it imports an additional hypothesis absent from the synthetic control. The missing hypothesis must involve genuine arithmetic structure: the exact CA supporting/event staircase, a bound tying the number or placement of exposed states to that staircase, or a simultaneous source relation connecting the fan to the standard/reciprocal prime-race coordinates of `RE-037`.

This also sharpens the interpretation of the correction already made to `RE-038`. A threshold cell should not be assigned an arithmetic CA-chamber capacity merely because it is an exposed cell of the amplitude envelope. The envelope is freely programmable; any useful capacity statement must be proved from the actual CA support geometry and its compatibility with the adaptive tangent, not inferred from convexity alone.

## 5. Prior-art boundary and falsification scope

Convex-envelope representations of divisor-sum extrema are classical in spirit. In particular, Musin's highest-abundant framework organizes divisor-sum extremizers through convex envelopes, and the ordinary fact that maxima of affine functions form a monotone piecewise-affine envelope is elementary. No novelty is claimed for those facts, for the recursion that realizes prescribed affine breakpoints in an abstract finite family, or for the weighted-mean identity (16).

The line-specific contribution is a **matched negative control** for `RE-038`: equations (4)--(30) show explicitly that all of the non-arithmetic data isolated there can coexist with an arbitrary threshold fan, even in the asymptotic small-height and logarithmic-spacing regime used by the real adaptive CA argument. A targeted current prior-art search found neighboring Robin/CA convex-envelope work, including Musin's highest-abundant construction, but no source in the audit turns this particular scale-invariant amplitude family into an arithmetic exclusion theorem. `SOURCES.md` now records Musin as the closest convex-envelope boundary.

The evidence boundary is essential. The synthetic states are **not** claimed to be integers, colossally abundant numbers, or values of the true divisor-sum function. Consequently this finding does not refute `RE-038`, Robin's theorem, or any future theorem that uses `Y=Phi(Z)` or the common prime source. It refutes only deductions whose hypotheses reduce to the amplitude-envelope structure reproduced above.

That negative result materially narrows the next step. The same-block fan is best treated as an interface through which arithmetic information must pass, not as an obstruction by itself. The live target is now to prove a genuinely source-dependent coupling across `b`: either enough simultaneous compatibility with the true CA event staircase to constrain the fan, or enough simultaneous prime-race structure to show that the algebraically realizable controls cannot come from the primes.